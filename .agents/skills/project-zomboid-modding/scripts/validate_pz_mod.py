#!/usr/bin/env python3
"""
Validate Project Zomboid (Build 42 / 40.20.4) mod structure and script syntax.
Usage:
    python validate_pz_mod.py <path_to_mod_folder_or_file>
"""

import os
import sys
import json
import re

def validate_mod_info(mod_dir):
    info_path = os.path.join(mod_dir, "mod.info")
    if not os.path.exists(info_path):
        return [f"[FAIL] Missing mod.info in root: {mod_dir}"]

    errors = []
    required_keys = {"id", "name", "description"}
    found_keys = set()

    with open(info_path, "r", encoding="utf-8", errors="ignore") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                found_keys.add(k.strip())
            else:
                errors.append(f"[WARN] mod.info:{line_no}: Invalid key=value line: {line}")

    missing = required_keys - found_keys
    if missing:
        errors.append(f"[FAIL] mod.info missing required keys: {', '.join(missing)}")

    return errors

def validate_pz_script_file(file_path):
    errors = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    # Check brace balancing
    brace_depth = 0
    in_block_comment = False
    lines = text.splitlines()

    for line_no, line in enumerate(lines, 1):
        s = line.strip()
        
        # Simple comment handling
        if in_block_comment:
            if "*/" in s:
                in_block_comment = False
            continue
        if "/*" in s and "*/" not in s:
            in_block_comment = True
            continue
        if s.startswith("//") or s.startswith("/*"):
            continue

        for char in line:
            if char == '{':
                brace_depth += 1
            elif char == '}':
                brace_depth -= 1
                if brace_depth < 0:
                    errors.append(f"[FAIL] {file_path}:{line_no}: Closing brace '}}' without matching opening brace.")
                    brace_depth = 0

    if brace_depth != 0:
        errors.append(f"[FAIL] {file_path}: Unbalanced braces! Final depth={brace_depth}")

    # Check craftRecipe inputs & outputs using brace scanner
    for match in re.finditer(r'craftRecipe\s+([A-Za-z0-9_]+)\s*\{', text):
        recipe_name = match.group(1)
        start_idx = match.end() - 1
        depth = 0
        end_idx = start_idx
        for idx in range(start_idx, len(text)):
            if text[idx] == '{':
                depth += 1
            elif text[idx] == '}':
                depth -= 1
                if depth == 0:
                    end_idx = idx
                    break
        recipe_body = text[start_idx:end_idx+1]
        if "inputs" not in recipe_body:
            errors.append(f"[FAIL] craftRecipe '{recipe_name}' in {file_path} is missing 'inputs {{...}}' block.")
        if "outputs" not in recipe_body:
            errors.append(f"[FAIL] craftRecipe '{recipe_name}' in {file_path} is missing 'outputs {{...}}' block.")

    return errors

def validate_translations(mod_dir):
    errors = []
    trans_dir = os.path.join(mod_dir, "media", "lua", "translations")
    if not os.path.exists(trans_dir):
        return errors

    for root, _, files in os.walk(trans_dir):
        for f in files:
            if f.endswith(".json"):
                fpath = os.path.join(root, f)
                try:
                    with open(fpath, "r", encoding="utf-8") as jf:
                        data = json.load(jf)
                    if not isinstance(data, dict):
                        errors.append(f"[FAIL] {fpath}: Translation file must be a JSON object (dict)")
                    elif "Recipes" in f:
                        for k in data.keys():
                            if "." in k:
                                errors.append(f"[WARN] {fpath}: Recipe key '{k}' should not include module prefix (use '{k.split('.')[-1]}')")
                except Exception as e:
                    errors.append(f"[FAIL] {fpath}: Invalid JSON syntax: {e}")
    return errors

def validate_mod(target):
    if os.path.isfile(target):
        if target.endswith(".txt"):
            return validate_pz_script_file(target)
        elif target.endswith(".json"):
            try:
                with open(target, "r", encoding="utf-8") as f:
                    json.load(f)
                return []
            except Exception as e:
                return [f"[FAIL] {target}: Invalid JSON: {e}"]
        else:
            return [f"[INFO] No validator for file type: {target}"]

    all_errors = []
    all_errors.extend(validate_mod_info(target))
    
    scripts_dir = os.path.join(target, "media", "scripts")
    if os.path.exists(scripts_dir):
        for root, _, files in os.walk(scripts_dir):
            for f in files:
                if f.endswith(".txt"):
                    all_errors.extend(validate_pz_script_file(os.path.join(root, f)))

    all_errors.extend(validate_translations(target))
    return all_errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_pz_mod.py <path_to_mod_or_file>")
        sys.exit(1)

    target = sys.argv[1]
    if not os.path.exists(target):
        print(f"Error: Path not found: {target}")
        sys.exit(1)

    errors = validate_mod(target)
    if not errors:
        print(f"[SUCCESS] All checks passed for: {target}")
        sys.exit(0)
    else:
        print(f"Validation completed with {len(errors)} notice(s):")
        for err in errors:
            print(" ", err)
        has_fails = any(e.startswith("[FAIL]") for e in errors)
        sys.exit(1 if has_fails else 0)

if __name__ == "__main__":
    main()
