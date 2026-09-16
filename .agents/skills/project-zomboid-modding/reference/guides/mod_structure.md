# Project Zomboid Mod Directory Structure (Build 42 / 40.20.4)

## Overview
In Project Zomboid (Build 42 / version 42.20.4, also referred to as 40.20.4), mods follow a strict directory hierarchy. The game searches for mods located in:
- `C:\Users\<Username>\Zomboid\mods\<ModFolder>\` (Windows user directory)
- `~/Zomboid/mods/<ModFolder>/` (Linux/macOS)
- Steam Workshop directory: `<SteamPath>/steamapps/workshop/content/108600/<WorkshopID>/`

## Standard Mod Directory Hierarchy

```
<ModFolder>/
├── mod.info                           # Main mod manifest (Required)
├── poster.png                         # Thumbnail image for Mod Manager (Required)
├── icon.png                           # Small icon next to mod name (Optional)
└── media/                             # Assets and game definitions (Required)
    ├── scripts/                       # PZ Script definition files (.txt)
    │   ├── items_mymod.txt            # Custom items
    │   ├── recipes_mymod.txt          # Crafting & evolved recipes
    │   ├── entities_mymod.txt         # Custom entities & craftbenches
    │   ├── vehicles_mymod.txt         # Vehicle definitions
    │   └── sounds_mymod.txt           # Custom sound scripts
    ├── lua/                           # Lua scripts
    │   ├── shared/                    # Code loaded on both Client and Server
    │   │   └── MyModShared.lua
    │   ├── client/                    # Client-side code (UI, rendering, input)
    │   │   ├── UI/                    # Custom UI windows and panels
    │   │   └── ContextMenu/           # World / Inventory context menus
    │   ├── server/                    # Server-side code (game rules, commands)
    │   │   └── MyModServer.lua
    │   └── translations/              # Translation files (JSON in B42)
    │       ├── EN/
    │       │   ├── ItemName_EN.json   # Item display names
    │       │   ├── Recipes_EN.json    # Recipe display names
    │       │   ├── UI_EN.json         # UI labels & buttons
    │       │   └── ContextMenu_EN.json
    │       └── TH/                    # Other languages (TH, ES, FR, etc.)
    │           ├── ItemName_TH.json
    │           └── Recipes_TH.json
    ├── textures/                      # Item icons and texture atlas
    │   ├── Item_MyItem.png            # Item icon (referenced as 'Icon = MyItem')
    │   └── ui/                        # UI sprites and buttons
    ├── clothing/                      # Clothing definitions
    │   └── clothingItems/             # Clothing XML files (.xml)
    │       └── MyClothingItem.xml
    ├── models_X/                      # 3D models (.fbx / .txt)
    │   └── MyMod/
    │       └── myModel.fbx
    └── maps/                          # Custom maps (Optional)
        └── MyCustomMap/
            ├── map.info
            └── objects.lua
```

## Critical Rules for B42 / 40.20.4
1. **`mod.info` Placement**: `mod.info` must reside in the root of the mod folder, directly beside `media/`.
2. **Version Isolation (`<version>` subfolder)**: In Build 42, you can also nest mod versions under a version-specific folder:
   ```
   MyMod/
     42/
       media/
       mod.info
   ```
   This allows a single mod on the Steam Workshop to support both Build 41 and Build 42 seamlessly.
3. **PZ Script files**: All `.txt` files in `media/scripts/` are parsed automatically at startup. Do NOT name them with conflicting names; prefix them with your mod ID (e.g. `mymod_items.txt`).
4. **Item Icons**: Placed in `media/textures/`. If your item script has `Icon = MySpecialItem`, the game looks for `media/textures/Item_MySpecialItem.png`.
5. **Translations**: Build 42 transitions translation dictionaries to JSON format (e.g. `media/lua/translations/EN/ItemName_EN.json`). Keys must match the script identifiers (`<Module>.<ID>`).
