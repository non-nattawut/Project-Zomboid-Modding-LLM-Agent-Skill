# Project Zomboid Modding Search Vocabulary & Guided Taxonomy

**Version:** 40.20.4 / Build 42.20.4  
**Purpose:** Guided taxonomy of search parameters, blocks, tags, item types, components, flags, and translation types.  

> [!NOTE]
> **Guiding, Not Limiting:** This taxonomy acts as a guided reference map. If you discover a new engine parameter, tag, or block, append it using `python dump_pz_schema.py --add-vocab <category> <term> [description]`.

## 📑 Available Categories

| Category Key | Description | Total Terms | Example Query |
| --- | --- | --- | --- |
| `blocks` | Category `blocks` | 96 | `--taxonomy blocks` |
| `item_types` | Category `item_types` | 11 | `--taxonomy item_types` |
| `components` | Category `components` | 12 | `--taxonomy components` |
| `tags` | Category `tags` | 459 | `--taxonomy tags` |
| `body_locations` | Category `body_locations` | 113 | `--taxonomy body_locations` |
| `recipe_flags` | Category `recipe_flags` | 9 | `--taxonomy recipe_flags` |
| `recipe_tags` | Category `recipe_tags` | 9 | `--taxonomy recipe_tags` |
| `translation_types` | Category `translation_types` | 8 | `--taxonomy translation_types` |

## 🔹 `blocks`

| Term | Description | Details |
| --- | --- | --- |
| `_component_block` | Component blocks are used in the [components ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/components.html) bl | `scripts/_component_block.md` |
| `alias` | Defines an alias for a list of tiles. This can be directly be refered to in [rule ](https://pz-wiki-modding.github.io/PZ | `scripts/alias.md` |
| `anim` | No description provided. | `scripts/anim.md` |
| `animation` | It is unknown what this block does. | `scripts/animation.md` |
| `animationsmesh` | Defines an animated mesh, usually for characters or animals. | `scripts/animationsmesh.md` |
| `area` | No description provided. | `scripts/area.md` |
| `attachment` | Defines an attachment point on a [model ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html) or [vehicle  | `scripts/attachment.md` |
| `blend` | Used to define blend rules for the [mapping tools ](https://pzwiki.net/wiki/Mapping#Mapping_tools) painting tool. | `scripts/blend.md` |
| `blendblacklist` | BlendWhiteList defines a whitelist for fluids that the fluid can be blended with, while BlendBlackList defines a blackli | `scripts/blendblacklist.md` |
| `blends` | The `Blends.txt` file is used in the [mapping tools ](https://pzwiki.net/wiki/Mapping#Mapping_tools) to assign blend til | `scripts/root_files/blends.md` |
| `blendwhitelist` | BlendWhiteList defines a whitelist for fluids that the fluid can be blended with, while BlendBlackList defines a blackli | `scripts/blendwhitelist.md` |
| `box` | [box ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/box.html)\ , [cylinder ](https://pz-wiki-modding.github.io/ | `scripts/box.md` |
| `categories` | Acts as a sort of tag list. Notably used in fluid scripts. Doesn't have parameters and instead just functions as a list. | `scripts/categories.md` |
| `character_profession_definition` | Defines a character profession. | `scripts/character_profession_definition.md` |
| `character_trait_definition` | Defines a character trait. | `scripts/character_trait_definition.md` |
| `clip` | Defines a clip to be used in a [sound script ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/sound.html)\ , whic | `scripts/clip.md` |
| `clock` | No description provided. | `scripts/clock.md` |
| `colors` | Used to create a new color definition which can be then be used in other blocks. Those colors are added to the available | `scripts/colors.md` |
| `component` | A component is a block which can be added as a child to a specific block type like an item, vehicle etc, to provide addi | `scripts/component.md` |
| `components` | No description provided. | `scripts/components.md` |
| `container` | No description provided. | `scripts/container.md` |
| `contextentry` | No description provided. | `scripts/contextentry.md` |
| `copyframe` | It is unknown what this block does. | `scripts/copyframe.md` |
| `copyframes` | It is unknown what this block does. | `scripts/copyframes.md` |
| `craftrecipe` | The 'craftRecipe' script block is used to define a crafting recipe, which allows players to craft items or tiles in the  | `scripts/craftrecipe.md` |
| `crawlthroughwheel` | Similar implementation as a [wheel ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/wheel.html)\ , but unclear wh | `scripts/crawlthroughwheel.md` |
| `cylinder` | [box ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/box.html)\ , [cylinder ](https://pz-wiki-modding.github.io/ | `scripts/cylinder.md` |
| `data` | No description provided. | `scripts/data.md` |
| `default` | The default.txt file is used to select the mods and maps that will be loaded by the game. | `scripts/root_files/default.md` |
| `door` | No description provided. | `scripts/door.md` |
| ... | *and 66 more (query via CLI)* | |

## 🔹 `item_types`

| Term | Description | Details |
| --- | --- | --- |
| `base:alarmclock` | Alarm clocks and watches with timer/beeping mechanics | `` |
| `base:clothing` | Wearable clothing, helmets, vests, armor with protection values | `` |
| `base:container` | Wearable bags, backpacks, pouches, boxes, cases | `` |
| `base:drainable` | Items with limited uses, fluids, batteries, thread, glue | `` |
| `base:food` | Edible and perishable items with nutritional values | `` |
| `base:key` | Keys matching doors, vehicles, or padlocks | `` |
| `base:literature` | Books, magazines, skill manuals, recipe learning items | `` |
| `base:map` | In-game maps with cartography annotations | `` |
| `base:normal` | Standard items, crafting ingredients, miscellaneous goods | `` |
| `base:radio` | Two-way radios, walkie-talkies, and televisions | `` |
| `base:weapon` | Hand weapons, melee weapons (blades, blunts), ranged firearms | `` |

## 🔹 `components`

| Term | Description | Details |
| --- | --- | --- |
| `contextmenuconfig` | No description provided. | `scripts/component/component-contextmenuconfig.md` |
| `craftbench` | Used to add a crafting bench property to an [entity ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/entity.html) | `scripts/component/component-craftbench.md` |
| `craftbenchsounds` | No description provided. | `scripts/component/component-craftbenchsounds.md` |
| `craftrecipe` | No description provided. | `scripts/component/component-craftrecipe.md` |
| `dryingcraftlogic` | No description provided. | `scripts/component/component-dryingcraftlogic.md` |
| `durability` | No description provided. | `scripts/component/component-durability.md` |
| `fluidcontainer` | Adds a fluid container to an item | `scripts/component/component-fluidcontainer.md` |
| `resources` | No description provided. | `scripts/component/component-resources.md` |
| `spriteconfig` | No description provided. | `scripts/component/component-spriteconfig.md` |
| `spriteoverlayconfig` | No description provided. | `scripts/component/component-spriteoverlayconfig.md` |
| `uiconfig` | No description provided. | `scripts/component/component-uiconfig.md` |
| `wallcoveringconfig` | No description provided. | `scripts/component/component-wallcoveringconfig.md` |

## 🔹 `tags`

| Term | Description | Details |
| --- | --- | --- |
| `2d6` | Tag for 2d6 | `ItemTag.DICE_2D6` |
| `2diamondjewellery` | Tag for 2diamondjewellery | `ItemTag.TWO_DIAMOND_JEWELLERY` |
| `2emeraldjewellery` | Tag for 2emeraldjewellery | `ItemTag.TWO_EMERALD_JEWELLERY` |
| `2rubyjewellery` | Tag for 2rubyjewellery | `ItemTag.TWO_RUBY_JEWELLERY` |
| `2sapphirejewellery` | Tag for 2sapphirejewellery | `ItemTag.TWO_SAPPHIRE_JEWELLERY` |
| `aerosol` | Tag for aerosol | `ItemTag.AEROSOL` |
| `alcoholicbeverage` | Tag for alcoholicbeverage | `ItemTag.ALCOHOLIC_BEVERAGE` |
| `alreadybroken` | Tag for alreadybroken | `ItemTag.ALREADY_BROKEN` |
| `alreadycooked` | Tag for alreadycooked | `ItemTag.ALREADY_COOKED` |
| `aluminum` | Tag for aluminum | `ItemTag.ALUMINUM` |
| `alwayshasstuff` | Tag for alwayshasstuff | `ItemTag.ALWAYS_HAS_STUFF` |
| `amethystjewellery` | Tag for amethystjewellery | `ItemTag.AMETHYST_JEWELLERY` |
| `ammo` | Tag for ammo | `ItemTag.AMMO` |
| `ammocase` | Tag for ammocase | `ItemTag.AMMO_CASE` |
| `animalbone` | Tag for animalbone | `ItemTag.ANIMAL_BONE` |
| `animalbrain` | Tag for animalbrain | `ItemTag.ANIMAL_BRAIN` |
| `animalcorpse` | Tag for animalcorpse | `ItemTag.ANIMAL_CORPSE` |
| `animalhead` | Tag for animalhead | `ItemTag.ANIMAL_HEAD` |
| `animalskull` | Tag for animalskull | `ItemTag.ANIMAL_SKULL` |
| `applyownername` | Tag for applyownername | `ItemTag.APPLY_OWNER_NAME` |
| `awkwardgloves` | Tag for awkwardgloves | `ItemTag.AWKWARD_GLOVES` |
| `awl` | Tag for awl | `ItemTag.AWL` |
| `bagsfillexception` | Tag for bagsfillexception | `ItemTag.BAGS_FILL_EXCEPTION` |
| `bakingfat` | Tag for bakingfat | `ItemTag.BAKING_FAT` |
| `ballpeenhammer` | Tag for ballpeenhammer | `ItemTag.BALL_PEEN_HAMMER` |
| `barehands` | Tag for barehands | `ItemTag.BARE_HANDS` |
| `barstock` | Tag for barstock | `ItemTag.BAR_STOCK` |
| `barstockhalf` | Tag for barstockhalf | `ItemTag.BAR_STOCK_HALF` |
| `barstockquarter` | Tag for barstockquarter | `ItemTag.BAR_STOCK_QUARTER` |
| `binding` | Tag for binding | `ItemTag.BINDING` |
| ... | *and 429 more (query via CLI)* | |

## 🔹 `body_locations`

| Term | Description | Details |
| --- | --- | --- |
| `ItemBodyLocation.AMMO_STRAP` | Body location slot: ItemBodyLocation.AMMO_STRAP | `` |
| `ItemBodyLocation.ANKLE_HOLSTER` | Body location slot: ItemBodyLocation.ANKLE_HOLSTER | `` |
| `ItemBodyLocation.BACK` | Body location slot: ItemBodyLocation.BACK | `` |
| `ItemBodyLocation.BANDAGE` | Body location slot: ItemBodyLocation.BANDAGE | `` |
| `ItemBodyLocation.BATH_ROBE` | Body location slot: ItemBodyLocation.BATH_ROBE | `` |
| `ItemBodyLocation.BELLY_BUTTON` | Body location slot: ItemBodyLocation.BELLY_BUTTON | `` |
| `ItemBodyLocation.BELT` | Body location slot: ItemBodyLocation.BELT | `` |
| `ItemBodyLocation.BELT_EXTRA` | Body location slot: ItemBodyLocation.BELT_EXTRA | `` |
| `ItemBodyLocation.BODY_COSTUME` | Body location slot: ItemBodyLocation.BODY_COSTUME | `` |
| `ItemBodyLocation.BOILERSUIT` | Body location slot: ItemBodyLocation.BOILERSUIT | `` |
| `ItemBodyLocation.CALF_LEFT` | Body location slot: ItemBodyLocation.CALF_LEFT | `` |
| `ItemBodyLocation.CALF_LEFT_TEXTURE` | Body location slot: ItemBodyLocation.CALF_LEFT_TEXTURE | `` |
| `ItemBodyLocation.CALF_RIGHT` | Body location slot: ItemBodyLocation.CALF_RIGHT | `` |
| `ItemBodyLocation.CALF_RIGHT_TEXTURE` | Body location slot: ItemBodyLocation.CALF_RIGHT_TEXTURE | `` |
| `ItemBodyLocation.CODPIECE` | Body location slot: ItemBodyLocation.CODPIECE | `` |
| `ItemBodyLocation.CUIRASS` | Body location slot: ItemBodyLocation.CUIRASS | `` |
| `ItemBodyLocation.DRESS` | Body location slot: ItemBodyLocation.DRESS | `` |
| `ItemBodyLocation.EAR_TOP` | Body location slot: ItemBodyLocation.EAR_TOP | `` |
| `ItemBodyLocation.EARS` | Body location slot: ItemBodyLocation.EARS | `` |
| `ItemBodyLocation.ELBOW_LEFT` | Body location slot: ItemBodyLocation.ELBOW_LEFT | `` |
| `ItemBodyLocation.ELBOW_RIGHT` | Body location slot: ItemBodyLocation.ELBOW_RIGHT | `` |
| `ItemBodyLocation.EYES` | Body location slot: ItemBodyLocation.EYES | `` |
| `ItemBodyLocation.FANNY_PACK_BACK` | Body location slot: ItemBodyLocation.FANNY_PACK_BACK | `` |
| `ItemBodyLocation.FANNY_PACK_FRONT` | Body location slot: ItemBodyLocation.FANNY_PACK_FRONT | `` |
| `ItemBodyLocation.FORE_ARM_LEFT` | Body location slot: ItemBodyLocation.FORE_ARM_LEFT | `` |
| `ItemBodyLocation.FORE_ARM_RIGHT` | Body location slot: ItemBodyLocation.FORE_ARM_RIGHT | `` |
| `ItemBodyLocation.FULL_HAT` | Body location slot: ItemBodyLocation.FULL_HAT | `` |
| `ItemBodyLocation.FULL_ROBE` | Body location slot: ItemBodyLocation.FULL_ROBE | `` |
| `ItemBodyLocation.FULL_SUIT` | Body location slot: ItemBodyLocation.FULL_SUIT | `` |
| `ItemBodyLocation.FULL_SUIT_HEAD` | Body location slot: ItemBodyLocation.FULL_SUIT_HEAD | `` |
| ... | *and 83 more (query via CLI)* | |

## 🔹 `recipe_flags`

| Term | Description | Details |
| --- | --- | --- |
| `AllowDestroyedItem` | Allows using a broken or 0-condition item as input | `` |
| `AllowFavorite` | Allows crafting even if the item is marked as favorite | `` |
| `InheritFavorite` | Output item inherits the favorite status of the input | `` |
| `ItemCount` | Matches input based on internal item count or stack | `` |
| `MayDegradeHeavy` | Tool has a high chance to lose significant durability | `` |
| `MayDegradeLight` | Tool has a chance to lose a small amount of durability | `` |
| `NotFull` | Item must not be completely full (e.g. for filling fluid/fuel) | `` |
| `Prop1` | Item held in primary hand during timed action animation | `` |
| `Prop2` | Item held in secondary hand during timed action animation | `` |

## 🔹 `recipe_tags`

| Term | Description | Details |
| --- | --- | --- |
| `AnySurfaceCraft` | Requires a flat surface or tabletop nearby | `` |
| `Blacksmithing` | Requires forge or metalworking station | `` |
| `CanBeDoneFromFloor` | Input items can be pulled directly from adjacent floor tiles | `` |
| `CanBeDoneInDark` | Player does not require a light source to craft | `` |
| `Cookable` | Evolves or finishes through cooking heat | `` |
| `HeatSource` | Requires an active heat source (campfire, stove, oven, forge) | `` |
| `InHandCraft` | Can be crafted directly from hands without standing near a surface | `` |
| `Saw` | Carpentry recipe requiring a saw | `` |
| `SharpKnife` | Requires a cutting or carving knife | `` |

## 🔹 `translation_types`

| Term | Description | Details |
| --- | --- | --- |
| `Attributes` | Character attributes and stat tooltips in Attributes_<LANG>.json | `` |
| `BodyParts` | Body part names in BodyParts_<LANG>.json (Key prefix: BODYPART_) | `` |
| `ContextMenu` | Right-click context menu options in ContextMenu_<LANG>.json (Key prefix: ContextMenu_) | `` |
| `ItemName` | Item display names in translations/<LANG>/ItemName_<LANG>.json (Key format: Module.ItemID) | `` |
| `Multiplayer` | Server and multiplayer UI localizations in Multiplayer_<LANG>.json | `` |
| `Recipes` | Recipe display names in translations/<LANG>/Recipes_<LANG>.json (Key format: RecipeID) | `` |
| `Sandbox` | Custom sandbox options in Sandbox_<LANG>.json (Key prefix: Sandbox_) | `` |
| `UI` | General UI labels, headers, and tooltips in UI_<LANG>.json | `` |

