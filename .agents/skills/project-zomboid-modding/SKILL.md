---
name: project-zomboid-modding
description: Create, validate, scaffold, and troubleshoot custom Project Zomboid mods, scripts, items, crafting recipes, entities, vehicles, tile definitions, and translations for Project Zomboid version 40.20.4 / Build 42.20.4. Use whenever designing, scripting, modifying, or debugging Project Zomboid mods.
---

# Skill: Project Zomboid Mod Development (Build 42 / 40.20.4)

## Overview
This skill equips AI agents with comprehensive technical modding knowledge for **Project Zomboid** version **40.20.4** (officially **Build 42.20.4**). It covers the complete script block system, modern `craftRecipe` mechanics, entity-component architectures, vehicle configuration, B42 JSON translations, Java engine tags, XML clothing definitions, and Lua client/server scripting.

## Capabilities
- **Scaffold Production-Ready Mods**: Generate exact folder structures (`mod.info`, `media/scripts`, `media/lua`, `media/textures`, `media/translations`).
- **Define Custom Items**: Configure weapons, tools, food, containers, clothing, drainables, keys, and radios with valid script properties.
- **Crafting & Recipes**: Author modern `craftRecipe` blocks with tags (`tags[...]`), inputs/outputs, tools (`mode:keep`), degrade flags (`flags[...]`), XP awards, and timed actions.
- **Entity & Component Architecture**: Build interactive workstations, drying racks, fluid tanks, and containers using Build 42 components (`CraftBench`, `FluidContainer`, `SpriteConfig`, `UiConfig`, `Durability`).
- **Vehicle System**: Script vehicles, parts, passenger seats, engine RPMs, and mechanics.
- **B42 Translation Pipeline**: Structure JSON translation files (`ItemName_EN.json`, `Recipes_EN.json`, `UI_EN.json`) following Build 42 rules.
- **XML & Models**: Configure `clothingItem` XML files with GUIDs, male/female models, and texture choices.
- **Script Validation & Inspection**: Validate brace matching, recipe syntax, and mod manifests using bundled Python utilities.

## Official Documentation & Web References
When local references require deeper verification or additional context, consult:
- **PZ API Documentation**: [https://pz-wiki-modding.github.io/PZ-API-Docs/index.html](https://pz-wiki-modding.github.io/PZ-API-Docs/index.html)
- **Official PZ Modding Wiki**: [https://pzwiki.net/wiki/Modding](https://pzwiki.net/wiki/Modding)
- **Unofficial B42 JavaDocs**: [https://demiurgequantified.github.io/ProjectZomboidJavaDocs/](https://demiurgequantified.github.io/ProjectZomboidJavaDocs/)
- **Unofficial LuaDocs**: [https://demiurgequantified.github.io/ProjectZomboidLuaDocs/](https://demiurgequantified.github.io/ProjectZomboidLuaDocs/)
- **ZedScripts Extension**: [https://github.com/PZ-Wiki-Modding/ZedScripts](https://github.com/PZ-Wiki-Modding/ZedScripts)

Use `read_url_content` or `search_web` to look up specific engine updates or class references if not covered locally.

## Autonomous Expansion Rule (Self-Improvement)
> **Rule**: If the current skill lacks documentation for a specific PZ script block, Java tag, craft recipe flag, component, template, or helper script required for a task:
> 1. **Research & Verify**: Look up the missing specification via official documentation or web search.
> 2. **Implement Task**: Complete the user's immediate request accurately.
> 3. **Persist Knowledge**: Immediately create or update the relevant file in this skill (`reference/`, `templates/`, or `scripts/`) and link it in `SKILL.md` so that the skill continuously evolves and remains self-contained.

---

## Context Navigation & Master Reference Catalogs

### 1. Guides & Fundamentals
- **[Mod Directory Structure Guide](./reference/guides/mod_structure.md)**: Standard folder layouts, version folders (`42/`), and `mod.info` configuration.
- **[Creating Items Guide](./reference/guides/creating_items.md)**: Step-by-step item creation (`base:weapon`, `base:food`, `base:container`, `base:drainable`, `base:clothing`).
- **[Creating Craft Recipes Guide](./reference/guides/creating_craft_recipes.md)**: Modern `craftRecipe` syntax, inputs/outputs, tag selectors, and flags.
- **[Creating Entities & Components Guide](./reference/guides/creating_entities_and_components.md)**: B42 interactive entities, craftbenches, and storage.
- **[Lua Scripting Guide](./reference/guides/lua_scripting_guide.md)**: Client vs Server vs Shared Lua, Event hooks, Context menus, and networking.

### 2. ScriptsDocs Reference (88+ Script Blocks)
- **[Scripts Index & Master Catalog](./reference/scripts.md)**: Overview of all PZ script blocks.
- **Core Definitions**:
  - **[Item Specification](./reference/scripts/item.md)**: Exhaustive reference of 370+ item parameters and `ItemType` subclasses.
  - **[CraftRecipe Specification](./reference/scripts/craftrecipe.md)**: Modern recipes, inputs, outputs, timed actions, and tags.
  - **[EvolvedRecipe Specification](./reference/scripts/evolvedrecipe.md)**: Multi-ingredient cooking and evolving recipes.
  - **[Inputs Block](./reference/scripts/inputs.md)** & **[Outputs Block](./reference/scripts/outputs.md)**: Recipe input/output mechanics.
  - **[Entity Specification](./reference/scripts/entity.md)**: Entity blocks and interactive objects.
  - **[Components Master Index](./reference/scripts/components.md)**: Architecture for Build 42 entity components.
- **Build 42 Entity Components**:
  - **[`CraftBench`](./reference/scripts/component/component-craftbench.md)**: Turns entities into craft stations filtering recipe tags.
  - **[`FluidContainer`](./reference/scripts/component/component-fluidcontainer.md)**: Liquid storage (Water, Petrol, Milk, etc.).
  - **[`Durability`](./reference/scripts/component/component-durability.md)**: Object health and condition loss.
  - **[`SpriteConfig`](./reference/scripts/component/component-spriteconfig.md)**: Tile rendering, facing (N, S, E, W).
  - **[`UiConfig`](./reference/scripts/component/component-uiconfig.md)**: Custom interaction UI style and titles.
  - **[`ContextMenuConfig`](./reference/scripts/component/component-contextmenuconfig.md)**: Entity context menu bindings.
  - **[`DryingCraftLogic`](./reference/scripts/component/component-dryingcraftlogic.md)**: Food drying and hide tanning logic.
  - **[`Resources`](./reference/scripts/component/component-resources.md)**: Internal resource inventory filters.
  - **[`WallCoveringConfig`](./reference/scripts/component/component-wallcoveringconfig.md)**: Wall-mounted object properties.
- **Vehicles & Mechanics**:
  - **[Vehicle Specification](./reference/scripts/vehicle.md)**: Vehicle definitions, mass, engine force, and categories.
  - **[Part Specification](./reference/scripts/part.md)**: Vehicle parts, Lua hooks, containers.
  - **[Passenger Specification](./reference/scripts/passenger.md)**: Seat positions, switch seats.
  - **[Wheel Specification](./reference/scripts/wheel.md)**: Tires, suspension, friction.
  - **[Lightbar Specification](./reference/scripts/lightbar.md)**: Emergency vehicle sirens and light sequences.
- **World, Tiles & Audio**:
  - **[Tile Specification](./reference/scripts/tile.md)** & **[TileGeometry](./reference/scripts/tilegeometry.md)**: Custom map tiles and collision.
  - **[Sound Specification](./reference/scripts/sound.md)**: Sound banks, attenuation, and trigger events.
  - **[Fixing Specification](./reference/scripts/fixing.md)**: Item repair recipes and fixing materials.
  - **[Container Specification](./reference/scripts/container.md)**: Capacity, weight reduction, and container types.
  - **[Fluid Specification](./reference/scripts/fluid.md)** & **[Fluids](./reference/scripts/fluids.md)**: Custom fluids and liquid properties.

### 3. Java Engine Data
- **[Java Reference Index](./reference/java.md)**: Master index of engine enums and Java data.
- **[Item Tags Catalog](./reference/java/item_tags.md)**: Comprehensive list of `ItemTag` fields and script names (`SharpKnife`, `BlowTorch`, `Needle`, `Hammer`, `Ammo`, etc.).
- **[Item Body Locations](./reference/java/item_body_locations.md)**: Valid wear slots (`TorsoExtra`, `Head`, `Hands`, `Back`, `Shoes`, etc.).
- **[Action Sound Times](./reference/java/action_sound_time.md)**: Sound timing triggers for timed actions.
- **[Color Definitions](./reference/java/colors.md)**: Standard RGBA color presets.
- **[Metabolics Reference](./reference/java/metabolics.md)**: Caloric and metabolic burn rates.

### 4. B42 Translations Reference
- **[Translations Master Guide](./reference/translations.md)**: Overview of B42 translation system.
- **[Translation Files Reference](./reference/translations/translation_files.md)**: File types (`ItemName`, `Recipes`, `UI`, `ContextMenu`), prefixes, and pattern properties.
- **[Language Codes Reference](./reference/translations/language_codes.md)**: ISO codes (`EN`, `TH`, `FR`, `DE`, `ES`, `RU`, `CN`, etc.).

### 5. XML & Clothing Reference
- **[XML Master Guide](./reference/xml.md)**: Overview of XML definitions.
- **[ClothingItem XML Specification](./reference/xml/clothingitem.md)**: Models, GUIDs, textures, masks, and tinting.
- **[Clothing Definitions](./reference/xml/clothing.md)** & **[Clothing Decals](./reference/xml/clothingdecals.md)**: Outfits and decals.
- **[File GUID Table](./reference/xml/fileguidtable.md)**: Global GUID registry for assets.

### 6. Mapping & Loot Distribution
- **[Mapping Master Guide](./reference/mapping.md)**: Overview of map properties.
- **[Room Names](./reference/mapping/rooms.md)** & **[Room Distributions](./reference/mapping/rooms_distributions.md)**: Spawn containers by room type.
- **[Procedural Distributions](./reference/mapping/procedural_distributions.md)**: Loot tables and spawn chances.
- **[Tile Properties](./reference/mapping/tile_properties.md)**: Surface, container, and solid flags.

---

## Templates & Helper Scripts

### Ready-to-Use Templates
Found in [`templates/`](./templates/):
- **[`mod.info`](./templates/mod.info)**: Complete mod manifest template.
- **[`item_template.txt`](./templates/item_template.txt)**: Weapons, food, containers, and materials.
- **[`craftrecipe_template.txt`](./templates/craftrecipe_template.txt)**: Modern `craftRecipe` with inputs, outputs, tags, and xp.
- **[`evolvedrecipe_template.txt`](./templates/evolvedrecipe_template.txt)**: Evolved recipe (cooking stews, soups).
- **[`entity_template.txt`](./templates/entity_template.txt)**: Custom entity workstation with components.
- **[`vehicle_template.txt`](./templates/vehicle_template.txt)**: Custom vehicle with parts and passenger seats.
- **[`clothing_item_template.xml`](./templates/clothing_item_template.xml)**: ClothingItem XML with models and GUID.
- **[`translation_itemname_template.json`](./templates/translation_itemname_template.json)**: `ItemName_EN.json` dictionary.
- **[`translation_recipes_template.json`](./templates/translation_recipes_template.json)**: `Recipes_EN.json` dictionary.
- **[`lua_client_template.lua`](./templates/lua_client_template.lua)**: Client events and context menus.
- **[`lua_server_template.lua`](./templates/lua_server_template.lua)**: Server client command listener.
- **[`lua_shared_template.lua`](./templates/lua_shared_template.lua)**: Shared constants and utility functions.

### Automated Helper Tools
Found in [`scripts/`](./scripts/):
1. **Mod Scaffold Generator**:
   ```bash
   python .agents/skills/project-zomboid-modding/scripts/generate_mod_scaffold.py <ModID> [ModName] [--author "Author"] [--output "path/to/target"]
   ```
2. **Mod & Script Validator**:
   ```bash
   python .agents/skills/project-zomboid-modding/scripts/validate_pz_mod.py <path_to_mod_or_file>
   ```
3. **PZ Schema & Tag Inspector**:
   ```bash
   # Query script block parameters
   python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --block item
   python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --block craftrecipe
   python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --block entity

   # Query item tags
   python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --tags SharpKnife

   # List supported Build 42 components
   python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --components

   # View guided search taxonomy categories
   python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --taxonomy
   python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --taxonomy recipe_flags

   # Append new discovered search vocabulary to taxonomy
   python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --add-vocab tags "MyCustomTag" --desc "Description of new tag"
   ```

### 📚 Search Vocabulary & Guided Taxonomy
- **[Search Taxonomy Reference Guide](./reference/taxonomy.md)**: Guided reference mapping blocks, item types, tags, components, body locations, flags, and translation types.
- **Taxonomy Database**: Defined in [`search_taxonomy.json`](./search_taxonomy.json).
- **Extensible & Non-Limiting**: Agents should use this taxonomy as a guided reference map. If a new block, item tag, component, or parameter is discovered or added, append it dynamically via:
  ```bash
  python .agents/skills/project-zomboid-modding/scripts/dump_pz_schema.py --add-vocab <category> <term> --desc "Description"
  ```

### Reference Example Mod
A complete, fully functional example mod is provided in [`example mods/SurvivalGear/`](../../example%20mods/SurvivalGear/):
- Full mod structure with `mod.info`, `poster.png`.
- Custom tactical weapons, rations, vest, and canteen.
- Custom craft recipes with tag matching, repair items, and XP rewards.
- Custom workstation entity with Build 42 components.
- Client, server, and shared Lua scripts.
- English B42 JSON translations.
- Valid clothingItem XML.
