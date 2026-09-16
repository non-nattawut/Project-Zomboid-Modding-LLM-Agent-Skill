# Creating Craft Recipes in Project Zomboid (Build 42 / 40.20.4)

## Overview
In Build 42 / 40.20.4, crafting recipes are defined using the modern `craftRecipe` block instead of the legacy `recipe` block. Recipes define inputs, outputs, time, required skills, tools, and animation actions.

## Standard `craftRecipe` Syntax

```java
module MyMod
{
    craftRecipe MakeImprovisedBandage
    {
        timedAction = Making,
        Time = 40,
        category = Health,
        Tags = InHandCraft;CanBeDoneInDark;CanBeDoneFromFloor,
        xpAward = FirstAid:5,
        
        inputs
        {
            item 1 tags[SharpKnife;Scissors] mode:keep flags[MayDegradeLight;Prop1],
            item 1 [Base.Sheet;Base.Tshirt_White;Base.Pillowcase] mode:destroy flags[Prop2],
        }
        outputs
        {
            item 2 Base.RippedSheets,
        }
    }
}
```

## Recipe Components

### 1. Header Properties
- **`timedAction`**: Animation played during crafting (`Making`, `SawLogs`, `SharpenStake`, `RipClothes`, etc.).
- **`Time`**: Duration in game ticks (e.g. `50` is ~1.5 real seconds at normal speed).
- **`category`**: Tab in the crafting UI (`Carpentry`, `Cooking`, `Health`, `Survival`, `Welding`, `Electrical`, `Blacksmithing`).
- **`Tags`**: Execution requirements:
  - `InHandCraft`: Can be crafted directly in inventory hands.
  - `CanBeDoneInDark`: Player does not require light.
  - `CanBeDoneFromFloor`: Materials can be taken from the floor without picking them up first.
  - `AnySurfaceCraft`: Requires a table or flat surface.
- **`SkillRequired`**: Minimum skill to craft, formatted as `SkillName:Level` (e.g. `Carpentry:3`).
- **`xpAward`**: XP awarded upon completion (e.g. `Carpentry:15;FirstAid:10`).
- **`needToBeLearn`**: Set to `true` if this recipe requires reading a magazine or selecting a trait.
- **`AutoLearnAny`**: Automatically learned when reaching a skill level (e.g. `Carpentry:5`).

### 2. `inputs` Block
Each input line specifies:
- Type: `item <count>` or `-fluid <amount>`
- Item specifier:
  - By item ID: `[Base.Log;Base.Plank]`
  - By Tag: `tags[SharpKnife;Saw]`
  - Any item: `[*]`
- Mode:
  - `mode:destroy`: Consumed during craft (default for materials).
  - `mode:keep`: Returned after craft (default for tools like knives and hammers).
- Flags:
  - `flags[Prop1]`: Character holds this item in primary hand during animation.
  - `flags[Prop2]`: Character holds this item in secondary hand during animation.
  - `flags[MayDegradeLight]`: Tool may lose a point of durability.
  - `flags[AllowDestroyedItem]`: Broken items can be used.

### 3. `outputs` Block
Specifies items or fluids produced:
```java
outputs
{
    item 1 MyMod.ReinforcedVest,
    item 2 Base.Thread,
}
```

## Recipe Translations
Add your recipe display name to `media/lua/translations/EN/Recipes_EN.json`:
```json
{
  "MakeImprovisedBandage": "Make Improvised Bandage"
}
```
*Note: Do NOT prefix the key with the module name in `Recipes.json` — use only the recipe ID.*
