#!/usr/bin/env python3
"""
PZ Modding Schema & Taxonomy Inspector (Build 42 / 40.20.4)
Inspect script parameters, item tags, components, and guided search vocabulary.
Allows autonomous expansion by appending new terms to the taxonomy.

Usage:
    python dump_pz_schema.py --block <item|craftrecipe|entity|vehicle|modinfo|...>
    python dump_pz_schema.py --tags [keyword]
    python dump_pz_schema.py --components
    python dump_pz_schema.py --item-type <weapon|food|container|...>
    python dump_pz_schema.py --taxonomy [category]
    python dump_pz_schema.py --add-vocab <category> <term> [--desc "Description"] [--file "path"]
"""

import sys
import os
import json
import argparse
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
REF_DIR = os.path.join(SKILL_DIR, "reference")
TAXONOMY_PATH = os.path.join(SKILL_DIR, "search_taxonomy.json")
TAXONOMY_MD_PATH = os.path.join(REF_DIR, "taxonomy.md")

def load_taxonomy():
    if os.path.exists(TAXONOMY_PATH):
        try:
            with open(TAXONOMY_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "metadata": {"title": "PZ Search Taxonomy", "game_version": "40.20.4 / Build 42.20.4"},
        "blocks": {},
        "item_types": {},
        "components": {},
        "tags": {},
        "body_locations": {},
        "recipe_flags": {},
        "recipe_tags": {},
        "translation_types": {}
    }

def save_taxonomy(tax):
    with open(TAXONOMY_PATH, "w", encoding="utf-8") as f:
        json.dump(tax, f, indent=2)
    sync_taxonomy_md(tax)

def sync_taxonomy_md(tax_data):
    try:
        md = []
        md.append("# Project Zomboid Modding Search Vocabulary & Guided Taxonomy\n")
        md.append("**Version:** 40.20.4 / Build 42.20.4  ")
        md.append("**Purpose:** Guided taxonomy of search parameters, blocks, tags, item types, components, flags, and translation types.  \n")
        md.append("> [!NOTE]")
        md.append("> **Guiding, Not Limiting:** This taxonomy acts as a guided reference map. If you discover a new engine parameter, tag, or block, append it using `python dump_pz_schema.py --add-vocab <category> <term> [description]`.\n")

        md.append("## 📑 Available Categories\n")
        md.append("| Category Key | Description | Total Terms | Example Query |")
        md.append("| --- | --- | --- | --- |")
        cats = [k for k in tax_data.keys() if k != "metadata"]
        for c in cats:
            md.append(f"| `{c}` | Category `{c}` | {len(tax_data[c])} | `--taxonomy {c}` |")
        md.append("")

        for c in cats:
            md.append(f"## 🔹 `{c}`\n")
            items = tax_data[c]
            if not items:
                md.append("*No entries yet.*\n")
                continue
            md.append("| Term | Description | Details |")
            md.append("| --- | --- | --- |")
            for k, info in sorted(items.items())[:30]:
                term = info.get("term", k)
                desc = info.get("description", "")
                extra = info.get("java_field") or info.get("file") or ""
                md.append(f"| `{term}` | {desc} | `{extra}` |")
            if len(items) > 30:
                md.append(f"| ... | *and {len(items) - 30} more (query via CLI)* | |")
            md.append("")

        with open(TAXONOMY_MD_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(md) + "\n")
    except Exception as e:
        print(f"Notice: Could not sync taxonomy.md: {e}")

def add_vocab(category, term, description=None, ref_file=None):
    tax = load_taxonomy()
    cat_key = category.lower()
    if cat_key not in tax:
        tax[cat_key] = {}
        print(f"Created new taxonomy category: '{cat_key}'")

    term_key = term.lower()
    entry = {
        "term": term,
        "description": description or f"Custom / discovered term {term}"
    }
    if ref_file:
        entry["file"] = ref_file

    tax[cat_key][term_key] = entry
    save_taxonomy(tax)
    print(f"[SUCCESS] Appended new search vocabulary: '{term}' under category '{cat_key}'")
    print(f"Total terms in '{cat_key}': {len(tax[cat_key])}")

def query_taxonomy(category=None):
    tax = load_taxonomy()
    cats = [k for k in tax.keys() if k != "metadata"]

    if not category:
        print("=== Guided Search Categories ===")
        for c in cats:
            print(f" - {c:<20} ({len(tax[c])} terms)")
        print("\nUsage: python dump_pz_schema.py --taxonomy <category>")
        return

    cat_key = category.lower()
    if cat_key not in tax:
        print(f"Category '{category}' not found. Available categories: {', '.join(cats)}")
        return

    items = tax[cat_key]
    print(f"=== Taxonomy Category: {cat_key} ({len(items)} terms) ===")
    for k, info in sorted(items.items())[:50]:
        t = info.get("term", k)
        d = info.get("description", "")
        extra = info.get("java_field") or info.get("file") or ""
        extra_str = f" [{extra}]" if extra else ""
        print(f"  {t:<25} {extra_str} - {d}")
    if len(items) > 50:
        print(f"  ... and {len(items) - 50} more terms.")

def query_block(block_name):
    # Find matching file in reference/scripts
    name_clean = block_name.lower().strip()
    target_file = None
    
    scripts_dir = os.path.join(REF_DIR, "scripts")
    for root, _, files in os.walk(scripts_dir):
        for f in files:
            if f.endswith(".md"):
                base = f.replace(".md", "").lower()
                if base == name_clean or base == f"component-{name_clean}":
                    target_file = os.path.join(root, f)
                    break
        if target_file:
            break

    if not target_file:
        print(f"Script block '{block_name}' reference not found.")
        print("Hint: Run `python dump_pz_schema.py --taxonomy blocks` to view all 90+ valid blocks.")
        return

    with open(target_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    params = re.findall(r'### `([^`]+)`', content)
    print(f"=== Script Block: {block_name} ({len(params)} documented parameters) ===")
    print(f"Reference: {os.path.relpath(target_file, SKILL_DIR)}")
    for p in params[:40]:
        print(f" - {p}")
    if len(params) > 40:
        print(f" ... and {len(params) - 40} more (see full spec file)")

def query_tags(tag_filter=None):
    tax = load_taxonomy()
    tags_dict = tax.get("tags", {})

    if tag_filter:
        flt = tag_filter.lower()
        matches = {k: v for k, v in tags_dict.items() if flt in k or flt in v.get("java_field", "").lower()}
    else:
        matches = tags_dict

    print(f"=== Project Zomboid Item Tags ({len(matches)} matches) ===")
    for k, info in sorted(matches.items())[:50]:
        t = info.get("term", k)
        jf = info.get("java_field", "")
        desc = info.get("description", "")
        print(f"  {jf:<32} -> {t:<20} {desc}")
    if len(matches) > 50:
        print(f"  ... and {len(matches) - 50} more. Narrow down with `--tags <keyword>`.")

def query_components():
    tax = load_taxonomy()
    comps = tax.get("components", {})
    print(f"=== Build 42 Entity Components ({len(comps)}) ===")
    for k, info in sorted(comps.items()):
        print(f" - {info.get('term', k):<25} : {info.get('description', '')}")

def query_item_type(itype):
    tax = load_taxonomy()
    itypes = tax.get("item_types", {})
    clean = itype.lower().replace("base:", "")
    if clean in itypes:
        info = itypes[clean]
        print(f"=== ItemType: {info['term']} ===")
        print(f"Description: {info['description']}")
    else:
        print(f"ItemType '{itype}' not recognized in default list.")
        print("Available item types:", ", ".join(itypes.keys()))

def main():
    parser = argparse.ArgumentParser(description="Project Zomboid Modding Schema & Taxonomy Inspector (Build 42 / 40.20.4)")
    parser.add_argument("--block", help="Query parameters for a script block (item, craftrecipe, entity, vehicle...)")
    parser.add_argument("--tags", nargs="?", const="", help="Search or list Item Tags")
    parser.add_argument("--components", action="store_true", help="List supported Build 42 entity components")
    parser.add_argument("--item-type", help="Inspect an ItemType class (weapon, food, container, drainable...)")
    parser.add_argument("--taxonomy", nargs="?", const="", help="View or search guided search taxonomy categories")
    parser.add_argument("--add-vocab", nargs=2, metavar=("CATEGORY", "TERM"), help="Append a new search vocabulary term to the taxonomy")
    parser.add_argument("--desc", default="", help="Description for the term when using --add-vocab")
    parser.add_argument("--file", default="", help="Optional reference file for the term when using --add-vocab")

    args = parser.parse_args()

    if args.add_vocab:
        add_vocab(args.add_vocab[0], args.add_vocab[1], args.desc, args.file)
    elif args.taxonomy is not None:
        query_taxonomy(args.taxonomy if args.taxonomy != "" else None)
    elif args.block:
        query_block(args.block)
    elif args.tags is not None:
        query_tags(args.tags if args.tags != "" else None)
    elif args.components:
        query_components()
    elif args.item_type:
        query_item_type(args.item_type)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
