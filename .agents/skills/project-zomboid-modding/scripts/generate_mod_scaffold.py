#!/usr/bin/env python3
"""
Generate a complete, production-ready Project Zomboid (Build 42 / 40.20.4) mod scaffold.
Usage:
    python generate_mod_scaffold.py <ModID> [ModName] [--author "Author"] [--output "path/to/target"]
"""

import os
import sys
import argparse
import json

def scaffold_mod(mod_id, mod_name=None, author="Modder", output_dir="."):
    if not mod_name:
        mod_name = mod_id
        
    target_dir = os.path.join(output_dir, mod_id)
    os.makedirs(target_dir, exist_ok=True)
    
    # 1. Root mod.info
    mod_info_content = f"""name={mod_name}
id={mod_id}
description={mod_name} for Project Zomboid (Build 42 / 40.20.4).
poster=poster.png
icon=icon.png
versionMin=42.0
versionMax=42.99
author={author}
category=features
modversion=1.0.0
require=
incompatible=
"""
    with open(os.path.join(target_dir, "mod.info"), "w", encoding="utf-8") as f:
        f.write(mod_info_content)
        
    # Placeholder poster file
    with open(os.path.join(target_dir, "poster.png"), "wb") as f:
        # Minimal 1x1 transparent png
        f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82')

    # Media folders
    media_dir = os.path.join(target_dir, "media")
    scripts_dir = os.path.join(media_dir, "scripts")
    lua_shared = os.path.join(media_dir, "lua", "shared")
    lua_client = os.path.join(media_dir, "lua", "client")
    lua_server = os.path.join(media_dir, "lua", "server")
    lua_trans_en = os.path.join(media_dir, "lua", "translations", "EN")
    textures_dir = os.path.join(media_dir, "textures")
    clothing_dir = os.path.join(media_dir, "clothing", "clothingItems")

    for d in [scripts_dir, lua_shared, lua_client, lua_server, lua_trans_en, textures_dir, clothing_dir]:
        os.makedirs(d, exist_ok=True)
        
    # 2. Items script
    items_content = f"""module {mod_id}
{{
    imports
    {{
        Base
    }}

    item SurvivalKnife
    {{
        ItemType = base:weapon,
        DisplayName = Survival Combat Knife,
        Icon = KnifeSurvival,
        Weight = 0.8,
        ConditionMax = 15,
        ConditionLowerChanceOneIn = 20,
        Categories = SmallBlade,
        SubCategory = Stab,
        Tags = SharpKnife;CutPlant;ButcherAnimal,
        MinDamage = 0.9,
        MaxDamage = 2.0,
        CriticalChance = 30,
        CritDmgMultiplier = 4,
        MinRange = 0.6,
        MaxRange = 0.95,
        BaseSpeed = 1.1,
        HitSound = SmallBladeHit,
        SwingSound = SmallBladeSlash,
        DisplayCategory = Weapon,
    }}
}}
"""
    with open(os.path.join(scripts_dir, f"{mod_id}_items.txt"), "w", encoding="utf-8") as f:
        f.write(items_content)
        
    # 3. Recipes script
    recipes_content = f"""module {mod_id}
{{
    craftRecipe CraftSurvivalKnife
    {{
        timedAction = Making,
        Time = 60,
        category = Survival,
        Tags = AnySurfaceCraft;CanBeDoneFromFloor,
        xpAward = Maintenance:10,
        SkillRequired = Maintenance:2,
        inputs
        {{
            item 1 [Base.KitchenKnife;Base.HuntingKnife] mode:destroy flags[Prop1],
            item 1 [Base.DuctTape] mode:destroy,
            item 1 tags[SharpKnife] mode:keep flags[MayDegradeLight],
        }}
        outputs
        {{
            item 1 {mod_id}.SurvivalKnife,
        }}
    }}
}}
"""
    with open(os.path.join(scripts_dir, f"{mod_id}_recipes.txt"), "w", encoding="utf-8") as f:
        f.write(recipes_content)

    # 4. Lua scripts
    shared_lua = f"""-- media/lua/shared/{mod_id}_shared.lua
{mod_id} = {mod_id} or {{}}
{mod_id}.VERSION = "1.0.0"
"""
    with open(os.path.join(lua_shared, f"{mod_id}_shared.lua"), "w", encoding="utf-8") as f:
        f.write(shared_lua)

    client_lua = f"""-- media/lua/client/{mod_id}_client.lua
local function onGameStart()
    print("[{mod_id}] Initialized on Client.")
end

Events.OnGameStart.Add(onGameStart)
"""
    with open(os.path.join(lua_client, f"{mod_id}_client.lua"), "w", encoding="utf-8") as f:
        f.write(client_lua)

    server_lua = f"""-- media/lua/server/{mod_id}_server.lua
local function onClientCommand(module, command, player, args)
    if module ~= "{mod_id}" then return end
    -- Handle server side mod logic
end

Events.OnClientCommand.Add(onClientCommand)
"""
    with open(os.path.join(lua_server, f"{mod_id}_server.lua"), "w", encoding="utf-8") as f:
        f.write(server_lua)

    # 5. Translations
    item_trans = {
        f"{mod_id}.SurvivalKnife": "Survival Combat Knife"
    }
    with open(os.path.join(lua_trans_en, "ItemName_EN.json"), "w", encoding="utf-8") as f:
        json.dump(item_trans, f, indent=2)

    recipe_trans = {
        "CraftSurvivalKnife": "Craft Survival Knife"
    }
    with open(os.path.join(lua_trans_en, "Recipes_EN.json"), "w", encoding="utf-8") as f:
        json.dump(recipe_trans, f, indent=2)

    print(f"Mod scaffold '{mod_id}' successfully created at: {target_dir}")

def main():
    parser = argparse.ArgumentParser(description="Generate PZ Build 42 / 40.20.4 Mod Scaffold")
    parser.add_argument("mod_id", help="Unique Mod ID (e.g. MySurvivalMod)")
    parser.add_argument("mod_name", nargs="?", default=None, help="Display name for mod")
    parser.add_argument("--author", default="Modder", help="Author name")
    parser.add_argument("--output", default=".", help="Output directory")
    args = parser.parse_args()

    scaffold_mod(args.mod_id, args.mod_name, args.author, args.output)

if __name__ == "__main__":
    main()
