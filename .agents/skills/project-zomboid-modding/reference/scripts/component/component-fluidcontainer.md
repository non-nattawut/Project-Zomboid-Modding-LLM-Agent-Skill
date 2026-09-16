
# component FluidContainer

- **Soft Override:** Unknown

- **Is Variant of:** [component ](#scripts-component)

Adds a fluid container to an item

## Hierarchy

This block can be a child of the following blocks:

- [entity ](#scripts-entity)
- [item ](#scripts-item)

This block can have the following child blocks:

- [whitelist ](#scripts-whitelist)
- [Fluids ](#scripts-fluids)

ID
--

This block should have no ID.

## Parameters

### `Capacity`

- **Type:** float

- **Default:** `1.0`

The fluid capacity of the container, the minimum value is `0.05`.

### `ContainerName`

- **Type:** translation

- **Default:** `FluidContainer`

The name of the fluid container. The name cannot have whitespaces, the game will sanitize it to remove them and show an error in the console about it.

### `CustomDrinkSound`

- **Type:** string

- **Default:** `DrinkingFromGeneric`

Refers to a [sound block ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/sound.html) to trigger when drinking.

### `FillsWithCleanWater`

- **Type:** boolean

- **Default:** `False`

When set to true, the container will fill with clean water instead of tainted water when left outside in the rain.

### `HiddenAmount`

- **Type:** boolean

- **Default:** `False`

When true, will hide the fluid quantity from the UI.

### `InitialPercent`

- **Type:** float

- **Incompatible with:** [InitialPercentMax ](#scripts-component-fluidcontainer-initialpercentmax) | [InitialPercentMin ](#scripts-component-fluidcontainer-initialpercentmin)

No description provided.

### `InitialPercentMax`

- **Type:** float

- **Default:** `1.0`

- **Incompatible with:** [InitialPercent ](#scripts-component-fluidcontainer-initialpercent)

The minimum amount of fluid which will appear in this container.

### `InitialPercentMin`

- **Type:** float

- **Default:** `0.0`

- **Incompatible with:** [InitialPercent ](#scripts-component-fluidcontainer-initialpercent)

The maximum amount of fluid which will appear in this container.

### `InputLocked`

- **Type:** boolean

- **Default:** `False`

Unused.

### `Opened`

- **Type:** boolean

- **Default:** `True`

Unused.

### `PickRandomFluid`

- **Type:** boolean

- **Default:** `False`

When set to true, the container will pick one of the available fluids in the [Fluids ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/fluids.html) child block at random when filling. If set to false, it will make every fluids appear.

### `RainFactor`

- **Type:** float

- **Default:** `0.0`

Defines how much rain contributes to filling the container. A high value increases the rate of filling. A value of `0.0` means that rain will not fill the container, which is the default value of the parameter.

If the item is a weapon and `RainFactor` is set to a value above the default, when the player aims with the weapon it will empty it.

