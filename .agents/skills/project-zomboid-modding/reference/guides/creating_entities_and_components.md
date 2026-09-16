# Creating Entities and Components in Project Zomboid (Build 42 / 40.20.4)

## Overview
Build 42 introduces an entity-component architecture for interactive game objects (workbenches, forges, kilns, drying racks, animals, and interactive machinery).

## Entity Script Syntax

Entities are defined in `media/scripts/` files:

```java
module MyMod
{
    entity Workbench_Advanced
    {
        component SpriteConfig
        {
            sprite = carpentry_02_16,
            face = E,
        }
        
        component UiConfig
        {
            uiStyle = workbench,
            title = UI_AdvancedWorkbench_Title,
        }

        component CraftBench
        {
            recipeTags = AdvancedCarpentry;Metalworking,
        }

        component Durability
        {
            maxCondition = 200,
            conditionLowerChance = 20,
        }

        component FluidContainer
        {
            capacity = 15.0,
            fluids = Water;Oil,
        }
    }
}
```

## Core Components Catalog

| Component | Description | Key Properties |
| --- | --- | --- |
| `SpriteConfig` | Visual sprite rendering and tile facing | `sprite`, `face` (N, S, E, W), `northSprite` |
| `UiConfig` | Configures the interaction UI menu | `uiStyle`, `title`, `icon` |
| `CraftBench` | Turns the entity into a workbench for craft recipes | `recipeTags` (allows recipes with matching tags) |
| `Durability` | Handles object health and degradation | `maxCondition`, `conditionLowerChance` |
| `FluidContainer` | Stores liquid (water, fuel, oil) inside the entity | `capacity`, `fluids` |
| `Resources` | Tracks internal inventory or materials | `maxWeight`, `resourceFilter` |
| `WallCoveringConfig` | Defines wall mounting behavior | `isWallMounted`, `offset` |
| `ContextMenuConfig` | Adds custom context menu actions to the entity | `contextMenuClass`, `actionPriority` |
| `DryingCraftLogic` | Logic for food drying racks or curing hides | `drySpeedMod`, `maxItems` |
