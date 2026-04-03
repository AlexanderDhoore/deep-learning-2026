#!/usr/bin/env python3

"""Remove Office metadata parts that Quarto leaves dangling in rendered PPTX files.

The original PowerPoint template contains custom XML and revision-tracking parts.
Quarto preserves the relationships for those parts when rendering a new deck, but
does not copy the actual package contents. Windows PowerPoint can reject the
resulting file because it contains broken internal relationships.

This script creates a sanitized copy of the reference template that keeps the
visual styling but drops the problematic package parts.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"

REMOVED_REL_TYPES = {
    "http://schemas.openxmlformats.org/officeDocument/2006/relationships/customXml",
    "http://schemas.microsoft.com/office/2015/10/relationships/revisionInfo",
    "http://schemas.microsoft.com/office/2016/11/relationships/changesInfo",
}

REMOVED_PREFIXES = (
    "customXml/",
    "ppt/changesInfos/",
)

REMOVED_FILES = {
    "ppt/revisionInfo.xml",
}

REMOVED_OVERRIDE_PREFIXES = (
    "/customXml/",
    "/ppt/changesInfos/",
)

REMOVED_OVERRIDE_FILES = {
    "/ppt/revisionInfo.xml",
}


def sanitize_presentation_rels(data: bytes) -> bytes:
    root = ET.fromstring(data)
    qname = f"{{{REL_NS}}}Relationship"
    for rel in list(root.findall(qname)):
        if rel.attrib.get("Type") in REMOVED_REL_TYPES:
            root.remove(rel)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def sanitize_content_types(data: bytes) -> bytes:
    root = ET.fromstring(data)
    qname = f"{{{CT_NS}}}Override"
    for override in list(root.findall(qname)):
        part_name = override.attrib.get("PartName", "")
        if part_name in REMOVED_OVERRIDE_FILES or part_name.startswith(
            REMOVED_OVERRIDE_PREFIXES
        ):
            root.remove(override)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def should_skip(name: str) -> bool:
    return name in REMOVED_FILES or name.startswith(REMOVED_PREFIXES)


def sanitize_template(src: Path, dst: Path) -> None:
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w") as zout:
        for info in zin.infolist():
            if should_skip(info.filename):
                continue

            data = zin.read(info.filename)
            if info.filename == "ppt/_rels/presentation.xml.rels":
                data = sanitize_presentation_rels(data)
            elif info.filename == "[Content_Types].xml":
                data = sanitize_content_types(data)

            zout.writestr(info, data)


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "usage: sanitize_reference_template.py INPUT_TEMPLATE OUTPUT_TEMPLATE",
            file=sys.stderr,
        )
        return 1

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])

    if not src.exists():
        print(f"input template does not exist: {src}", file=sys.stderr)
        return 1

    sanitize_template(src, dst)
    print(f"wrote sanitized template to {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
