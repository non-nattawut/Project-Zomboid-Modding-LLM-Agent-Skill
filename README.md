# Project Zomboid Modding - LLM Agents Skill & Knowledge Base

[![Project Zomboid](https://img.shields.io/badge/Project%20Zomboid-Version%2040.20.4%20%2F%20Build%2042.20.4-red.svg)](https://projectzomboid.com/)
[![PZ API Docs](https://img.shields.io/badge/PZ--API--Docs-Complete%20Scrape-blue.svg)](https://pz-wiki-modding.github.io/PZ-API-Docs/index.html)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill%20Spec-brightgreen.svg)](https://github.com/non-nattawut/Project-Zomboid-Modding-LLM-Agent-Skill)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)

An AI Agent Skill and comprehensive technical knowledge base designed for LLM coding agents (Google Antigravity, Cursor, Claude Code, OpenAI Codex, etc.) to autonomously scaffold, script, develop, validate, and troubleshoot custom **Items**, **Craft Recipes**, **Entities**, **Components**, **Vehicles**, **Translations**, and **Lua Systems** for Project Zomboid.

> [!IMPORTANT]
> **Game Version Notice**: This knowledge base provides complete modding technical specifications for **Project Zomboid version 40.20.4** (as documented in the [PZ API Documentation](https://pz-wiki-modding.github.io/PZ-API-Docs/index.html), covering engine build **42.20.4**). All 134 documentation sections and specifications have been scraped, processed, and formatted into clean agent-navigable references.

---

## 🌟 Features

- 📚 **130+ Complete Reference Specifications**: Full conversion of all PZ-API-Docs sections into markdown catalogs.
- 🗡️ **370+ Item Properties & Subclasses**: Deep documentation for `base:normal`, `base:weapon`, `base:food`, `base:container`, `base:drainable`, `base:clothing`, `base:radio`, etc.
- 🔨 **Modern Build 42 CraftRecipe Engine**: Complete reference for `craftRecipe` blocks, tag matching (`tags[...]`), tool preservation (`mode:keep`), degrade flags (`flags[...]`), inputs/outputs, and timed actions.
- ⚙️ **Entity-Component Architecture**: Guides and references for Build 42 interactive objects (`CraftBench`, `FluidContainer`, `SpriteConfig`, `UiConfig`, `Durability`, `DryingCraftLogic`).
- 🏷️ **Comprehensive Java Engine Catalogs**: Complete list of Java `ItemTag` constants, `ItemBodyLocation` slots, `ActionSoundTime`, and metabolics.
- 🌐 **Build 42 JSON Translation Pipeline**: Accurate schemas and prefix rules for `ItemName_EN.json`, `Recipes_EN.json`, and context menu localizations.
- 🛠️ **Automated CLI Tools**:
  - `generate_mod_scaffold.py`: Boilerplate mod generator.
  - `validate_pz_mod.py`: Syntax, brace balancing, recipe structure, and translation validator.
  - `dump_pz_schema.py`: CLI schema, parameter, tag, and component inspector.
- 📋 **Production-Ready Templates**: 12 pre-built templates covering manifests, scripts, entities, vehicles, clothing XML, translations, and Lua hooks.
- 📦 **Complete Example Mod**: Included working reference mod [`SurvivalGear`](./example%20mods/SurvivalGear/) demonstrating weapons, armor, food, workbenches, and Lua context menus.

---

## 📁 Repository Structure

```
├── .agents/
│   └── skills/
│       └── project-zomboid-modding/
│           ├── SKILL.md              # Agent skill entry point & master index
│           ├── reference/            # 134 documentation specifications
│           │   ├── scripts/          # 88+ script blocks (item, craftrecipe, entity, etc.)
│           │   │   ├── component/    # Build 42 entity components (CraftBench, FluidContainer, etc.)
│           │   │   └── root_files/   # modinfo, sandboxoptions, rules, etc.
│           │   ├── java/             # Java tags, body locations, sound times, metabolics
│           │   ├── mapping/          # Room distributions, procedural loot, tile properties
│           │   ├── translations/     # JSON translation formats & language codes
│           │   ├── xml/              # clothingItem XML, clothing, decals, animNode
│           │   └── guides/           # Practical walkthroughs & best practices
│           ├── templates/            # 12 ready-to-use boilerplate templates
│           └── scripts/              # Python CLI utilities
│               ├── generate_mod_scaffold.py
│               ├── validate_pz_mod.py
│               └── dump_pz_schema.py
├── example mods/
│   ├── SurvivalGear/                 # Complete working sample mod
│   └── SurvivalGear.zip              # Pre-packaged mod archive
├── evals/
│   └── evals.json                    # Benchmark test prompts for the skill
├── AGENTS.md                         # Persona and core directives for AI agents
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Usage

### 1. Integrating with AI Agents / IDEs
Place the `.agents/` folder into your project workspace root or agents skill directory. When using an agentic framework (Antigravity, Cursor, Claude Code, etc.), the agent will read `AGENTS.md` and load `.agents/skills/project-zomboid-modding/SKILL.md` to design schema-accurate Project Zomboid mods.

### 2. Using CLI Tools

#### Generate a New Mod Scaffold
Scaffold a complete, functional mod with all folders, scripts, translations, and manifest:
```bash
python .agents/skills/project-zomboid-modding/scripts/generate_mod_scaffold.py MySurvivalMod "My Survival Mod" --author "YourName"
```

#### Validate Mod Syntax & Directory Structure
Check your mod files for brace balancing, missing recipe inputs/outputs, and translation key errors:
```bash
python .agents/skills/project-zomboid-modding/scripts/validate_pz_mod.py "path/to/YourMod"
```

#### Inspect PZ Schemas, Parameters & Tags
Query documented parameters, allowed values, item tags, or components directly from the terminal:
```bash
# Query parameters of a script block (item, craftrecipe, entity, vehicle, modinfo)
python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --block item

# Search for Item Tags matching a keyword
python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --tags Knife

# List supported Build 42 entity components
python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --components

# View guided search taxonomy categories
python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --taxonomy
python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --taxonomy recipe_flags

# Dynamically append new discovered search vocabulary
python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --add-vocab tags "LaserCutter" --desc "Futuristic cutting tool tag"
```

---

## 📚 Guided Search Taxonomy
The skill includes an extensible search vocabulary database in [`search_taxonomy.json`](file:///.agents/skills/project-zomboid-modding/search_taxonomy.json) and [`reference/taxonomy.md`](file:///.agents/skills/project-zomboid-modding/reference/taxonomy.md):
- **Blocks (96)**: `item`, `craftrecipe`, `entity`, `vehicle`, `container`, `fluid`, etc.
- **Item Types (11)**: `weapon`, `food`, `container`, `drainable`, `clothing`, etc.
- **Components (12)**: `CraftBench`, `FluidContainer`, `Durability`, `SpriteConfig`, `UiConfig`, etc.
- **Tags (459+)**: `SharpKnife`, `BlowTorch`, `Needle`, `Hammer`, `Ammo`, etc.
- **Body Locations (113)**: `TorsoExtra`, `Head`, `Hands`, `Back`, etc.
- **Recipe Flags & Tags**: `Prop1`, `Prop2`, `MayDegradeLight`, `InHandCraft`, `AnySurfaceCraft`, etc.
- **Extensible & Non-Limiting**: Agents and users can dynamically append new search terms anytime using `--add-vocab`.

---

## 📖 Documentation Sources
- [PZ API Documentation](https://pz-wiki-modding.github.io/PZ-API-Docs/index.html)
- [Official Project Zomboid Modding Wiki](https://pzwiki.net/wiki/Modding)
- [Unofficial B42 JavaDocs](https://demiurgequantified.github.io/ProjectZomboidJavaDocs/)
- [Unofficial LuaDocs](https://demiurgequantified.github.io/ProjectZomboidLuaDocs/)
- [ZedScripts VSCode Extension](https://github.com/PZ-Wiki-Modding/ZedScripts)

---

## 📄 License
This repository is licensed under the [MIT License](LICENSE).
