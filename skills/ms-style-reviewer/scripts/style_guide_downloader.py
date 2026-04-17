from __future__ import annotations

import argparse
import json
import re
import time
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen


BASE_URL = "https://learn.microsoft.com/en-us/style-guide/"
TOC_URL = urljoin(BASE_URL, "toc.json")
USER_AGENT = "msft-style-guide-downloader/1.0"
@dataclass(frozen=True)
class TocNode:
    href: str
    title: str


@dataclass(frozen=True)
class DownloadResult:
    url: str
    source_url: str
    output_path: Path
    title: str
    skipped: bool


def build_arg_parser(default_output_dir: str, default_limit: int | None = None) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Download Microsoft Writing Style Guide markdown to a local folder layout.",
    )
    parser.add_argument(
        "--output-dir",
        default=default_output_dir,
        help="Directory where the mirrored markdown tree will be written.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=default_limit,
        help="Optional limit on the number of pages to download.",
    )
    parser.add_argument(
        "--start-at",
        type=int,
        default=0,
        help="Skip the first N pages from the TOC before downloading.",
    )
    parser.add_argument(
        "--include-welcome-whats-new",
        action="store_true",
        help="Include the 'welcome/whats-new' page. It is omitted by default because it changes over time.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite files that already exist.",
    )
    parser.add_argument(
        "--pause-seconds",
        type=float,
        default=0.0,
        help="Optional delay between page downloads.",
    )
    parser.add_argument(
        "--toc-snapshot",
        action="store_true",
        help="Write a toc-snapshot.json file in the output directory.",
    )
    parser.add_argument(
        "--manifest",
        action="store_true",
        help="Write a manifest.json file describing downloaded pages.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP timeout in seconds.",
    )
    return parser


def fetch_text(url: str, timeout: float) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def fetch_markdown(url: str, timeout: float) -> tuple[str, str]:
    markdown_url = f"{url}?{urlencode({'accept': 'text/markdown'})}"
    request = Request(
        markdown_url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/markdown",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace"), markdown_url


def fetch_json(url: str, timeout: float) -> dict:
    return json.loads(fetch_text(url, timeout))


def flatten_toc_items(items: Iterable[dict]) -> list[TocNode]:
    nodes: list[TocNode] = []
    for item in items:
        href = item.get("href")
        title = normalize_title(item.get("toc_title", ""))
        if href:
            nodes.append(TocNode(href=href, title=title))
        children = item.get("children") or []
        nodes.extend(flatten_toc_items(children))
    return nodes


def normalize_title(title: str) -> str:
    collapsed = re.sub(r"\s+", " ", title).strip()
    return unescape(collapsed)


def normalize_href(href: str) -> str:
    return href.strip("/")


def should_include(node: TocNode, include_welcome_whats_new: bool) -> bool:
    slug = normalize_href(node.href)
    if not slug:
        return False
    if slug == "welcome/whats-new" and not include_welcome_whats_new:
        return False
    return True


def page_url_from_href(href: str) -> str:
    normalized = normalize_href(href)
    return urljoin(BASE_URL, f"{normalized}/")


def output_path_from_href(output_dir: Path, href: str) -> Path:
    normalized = normalize_href(href)
    return output_dir.joinpath(*normalized.split("/")).joinpath("index.md")


def load_toc(timeout: float, include_welcome_whats_new: bool) -> list[TocNode]:
    toc = fetch_json(TOC_URL, timeout)
    items = toc.get("items") or []
    flattened = flatten_toc_items(items)
    seen: set[str] = set()
    filtered: list[TocNode] = []
    for node in flattened:
        slug = normalize_href(node.href)
        if slug in seen:
            continue
        if not should_include(node, include_welcome_whats_new):
            continue
        seen.add(slug)
        filtered.append(TocNode(href=slug, title=node.title))
    return filtered


def select_nodes(nodes: list[TocNode], start_at: int, limit: int | None) -> list[TocNode]:
    selected = nodes[start_at:]
    if limit is not None:
        selected = selected[:limit]
    return selected


def download_node(node: TocNode, output_dir: Path, overwrite: bool, timeout: float) -> DownloadResult:
    page_url = page_url_from_href(node.href)
    output_path = output_path_from_href(output_dir, node.href)

    if output_path.exists() and not overwrite:
        return DownloadResult(
            url=page_url,
            source_url="",
            output_path=output_path,
            title=node.title,
            skipped=True,
        )

    markdown, source_url = fetch_markdown(page_url, timeout)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    return DownloadResult(
        url=page_url,
        source_url=source_url,
        output_path=output_path,
        title=node.title,
        skipped=False,
    )


def run_download(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    all_nodes = load_toc(args.timeout, args.include_welcome_whats_new)
    selected_nodes = select_nodes(all_nodes, args.start_at, args.limit)

    if args.toc_snapshot:
        snapshot = [
            {
                "href": node.href,
                "title": node.title,
                "page_url": page_url_from_href(node.href),
                "output_path": str(output_path_from_href(output_dir, node.href).relative_to(output_dir)),
            }
            for node in selected_nodes
        ]
        (output_dir / "toc-snapshot.json").write_text(
            json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    manifest: list[dict] = []
    failures: list[dict] = []

    for index, node in enumerate(selected_nodes, start=1):
        try:
            result = download_node(node, output_dir, args.overwrite, args.timeout)
            relative_path = result.output_path.relative_to(output_dir)
            status = "SKIP" if result.skipped else "OK"
            print(f"[{index}/{len(selected_nodes)}] {status} {node.href} -> {relative_path}")
            manifest.append(
                {
                    "href": node.href,
                    "title": node.title,
                    "page_url": result.url,
                    "source_url": result.source_url,
                    "output_path": str(relative_path),
                    "skipped": result.skipped,
                }
            )
        except (HTTPError, URLError, TimeoutError, ValueError) as error:
            print(f"[{index}/{len(selected_nodes)}] ERROR {node.href}: {error}")
            failures.append(
                {
                    "href": node.href,
                    "title": node.title,
                    "error": str(error),
                }
            )
        if args.pause_seconds > 0 and index < len(selected_nodes):
            time.sleep(args.pause_seconds)

    if args.manifest:
        (output_dir / "manifest.json").write_text(
            json.dumps(
                {
                    "base_url": BASE_URL,
                    "toc_url": TOC_URL,
                    "selected_count": len(selected_nodes),
                    "downloaded_count": len([item for item in manifest if not item["skipped"]]),
                    "skipped_count": len([item for item in manifest if item["skipped"]]),
                    "failure_count": len(failures),
                    "items": manifest,
                    "failures": failures,
                },
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

    print(
        "Summary: "
        f"selected={len(selected_nodes)} downloaded={len([item for item in manifest if not item['skipped']])} "
        f"skipped={len([item for item in manifest if item['skipped']])} failures={len(failures)}"
    )
    return 1 if failures else 0