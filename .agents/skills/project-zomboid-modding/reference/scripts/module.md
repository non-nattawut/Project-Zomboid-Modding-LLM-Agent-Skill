
# module

- **Soft Override:** Unknown

A module serves as a namespace for your scripts and is the barebone for most scripts you will create in your mod. The game's namespace is `Base`\ , and while you can insert in it, it is recommended to use your own module for your mod's scripts to avoid conflicts with the game and other mods.

To define a module, you need to create a block as follows, by changing the ID to a unique name for your mods:

```java

module yourID
{
  ...
}

```

Most scripts that are defined in a module will need to be refered to by their 'full type', that is `module.id`\ , but this is a bit inconsistent as some places where a script block needs to be refered to require no module reference. For example, for an item, you can refer to it by its full type `yourModule.yourItemID`.

## Hierarchy

This block can be a child of the following blocks:

- [ROOT-Scripts ](#scripts-root-scripts)

This block can have the following child blocks:

- [animation ](#scripts-animation)
- [timedAction ](#scripts-timedaction)
- [model ](#scripts-model)
- [soundTimeline ](#scripts-soundtimeline)
- [entity ](#scripts-entity)
- [animationsMesh ](#scripts-animationsmesh)
- [template ](#scripts-template)
- [fixing ](#scripts-fixing)
- [vehicle ](#scripts-vehicle)
- [ragdoll ](#scripts-ragdoll)
- [physicsHitReaction ](#scripts-physicshitreaction)
- [craftRecipe ](#scripts-craftrecipe)
- [evolvedrecipe ](#scripts-evolvedrecipe)
- [xuiSkin ](#scripts-xuiskin)
- [character_profession_definition ](#scripts-character_profession_definition)
- [clock ](#scripts-clock)
- [fluid ](#scripts-fluid)
- [physicsShape ](#scripts-physicsshape)
- [energy ](#scripts-energy)
- [vehicleEngineRPM ](#scripts-vehicleenginerpm)
- [mannequin ](#scripts-mannequin)
- [imports ](#scripts-imports)
- [character_trait_definition ](#scripts-character_trait_definition)
- [item ](#scripts-item)
- [sound ](#scripts-sound)

ID
--

This block can have an ID.

- **Optional:** False

- **Can have spaces:** False

## Parameters

This block has no parameters.
