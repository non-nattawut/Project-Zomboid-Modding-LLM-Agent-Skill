# Creating Items in Project Zomboid (Build 42 / 40.20.4)

## Overview
Items in Project Zomboid are defined inside `.txt` files in `media/scripts/`. Every item belongs to a `module` (default is `Base`, or your custom module e.g. `module MyMod`).

## Basic Item Syntax

```java
module MyMod
{
    imports
    {
        Base
    }

    item TacticalCombatKnife
    {
        ItemType = base:weapon,
        DisplayName = Tactical Combat Knife,
        Icon = TacticalKnife,
        Weight = 0.8,
        MetalValue = 20,
        ConditionMax = 15,
        ConditionLowerChanceOneIn = 15,
        Categories = SmallBlade,
        SubCategory = Stab,
        Tags = SharpKnife;CutPlant;ButcherAnimal,
        
        /* Weapon specific parameters */
        MinDamage = 0.8,
        MaxDamage = 1.9,
        CriticalChance = 35,
        CritDmgMultiplier = 4,
        MinRange = 0.61,
        MaxRange = 0.95,
        BaseSpeed = 1.1,
        HitSound = SmallBladeHit,
        SwingSound = SmallBladeSlash,
        DoorDamage = 5,
        TreeDamage = 1,
        MinAngle = 0.65,
        PushBackMod = 0.3,
        KnockBackOnNoDeath = false,
        SplatSize = 1,
        SplatNumber = 1,
    }
}
```

## Primary Item Types (`ItemType`)

| ItemType | Script Class | Purpose & Typical Parameters |
| --- | --- | --- |
| `base:normal` | `Item` | Miscellaneous goods, crafting components, materials (`Weight`, `MetalValue`, `Tags`). |
| `base:weapon` | `HandWeapon` | Melee & ranged weapons (`MinDamage`, `MaxDamage`, `MinRange`, `MaxRange`, `CriticalChance`). |
| `base:food` | `Food` | Edible items (`Calories`, `Carbohydrates`, `Lipids`, `Proteins`, `DaysFresh`, `DaysTotallyRotten`, `HungerChange`). |
| `base:container` | `InventoryContainer` | Backpacks, bags, pouches (`Capacity`, `WeightReduction`, `CanBeEquipped`). |
| `base:drainable` | `DrainableComboItem` | Multi-use items with uses count (`UseDelta`, `TicksPerEquipUse`, `ConsolidateOption`). |
| `base:clothing` | `Clothing` | Wearables (`BodyLocation`, `BiteDefense`, `ScratchDefense`, `Insulation`, `Windresistance`). |
| `base:key` | `Key` | Lock keys (`KeyId`, `Digital`). |
| `base:alarmclock` | `AlarmClock` | Clocks, timers (`AlarmSound`). |
| `base:radio` | `Radio` | Walkie-talkies, HAM radios (`MinChannel`, `MaxChannel`, `TransmitRange`). |

## Essential Parameters Reference
- **`ItemType`**: Must specify the type (e.g. `base:normal`, `base:weapon`).
- **`Weight`**: Decimal representing item weight (e.g. `0.5`, `1.2`).
- **`Icon`**: Name of the icon file in `media/textures/Item_<Icon>.png`.
- **`Tags`**: Semicolon-separated list of tags (e.g. `Tags = SharpKnife;Saw;InHandCraft`). Tags are queryable by crafting recipes.
- **`ConditionMax`**: Durability pool (e.g. `10`).
- **`ConditionLowerChanceOneIn`**: Chance of degrading per hit/use (e.g. `10` = 1 in 10 chance).
- **`DisplayCategory`**: Categorization for inventory filters (`Tool`, `Weapon`, `Food`, `FirstAid`, `Material`).

## Display Name & Translations
While `DisplayName` can be placed directly in the item script, for localization in Build 42 you should add the entry to `media/lua/translations/EN/ItemName_EN.json`:
```json
{
  "MyMod.TacticalCombatKnife": "Tactical Combat Knife"
}
```
