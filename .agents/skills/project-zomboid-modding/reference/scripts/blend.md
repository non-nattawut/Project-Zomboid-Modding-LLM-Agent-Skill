
# blend

- **Soft Override:** Unknown

Used to define blend rules for the [mapping tools ](https://pzwiki.net/wiki/Mapping#Mapping_tools) painting tool.

## Hierarchy

This block can be a child of the following blocks:

- [ROOT-Blends ](#scripts-root-blends)

ID
--

This block should have no ID.

## Parameters

### `blendTile`

- **Type:** Unknown

Used to define the tiles which will be used for the blend around the `mainTile`. This can be a single tile or an array of tiles, and it supports `alias` blocks.

For example:

```java

blendTile = vegetation_farm_01_35

```

```java

blendTile = [
    vegetation_farm_01_32
    vegetation_farm_01_33
    vegetation_farm_01_34
    vegetation_farm_01_35
    vegetation_farm_01_36
    vegetation_farm_01_37
    vegetation_farm_01_38
    vegetation_farm_01_39
]

```

Or with one or more alias blocks:

```java

alias
{
    name = treez1
    tiles = [
        vegetation_trees_01_13
        vegetation_trees_01_14
        vegetation_trees_01_15
        vegetation_trees_01_8
        vegetation_trees_01_9
        vegetation_trees_01_10
        vegetation_trees_01_11
        vegetation_trees_01_17
    ]
}

```

```java

blendTile = [
  treez1
]

```

### `dir`

- **Type:** Unknown

- **Allowed values:** `e` | `n` | `ne` | `nw` | `s` | `se` | `sw` | `w`

The direction the blend applies to.

### `exclude`

- **Type:** Unknown

A list of tiles which will be excluded from being blended. This can be a single tile or an array of tiles, and it supports `alias` blocks.

The format needs to be like this:

```java

exclude = water lightgrass medgrass darkgrass

```

Where each entries separated by a space are an alias.

### `exclude2`

- **Type:** Unknown

No description provided.

### `layer`

- **Type:** Unknown

The layer the blend rule applies to. Should be one of the layers defined in the `TMXconfig.txt` file.

### `mainTile`

- **Type:** Unknown

Used to identify which tiles will trigger the blend. This can be a single tile or an array of tiles, and it supports `alias` blocks.

For example:

```java

mainTile = vegetation_farm_01_35

```

```java

mainTile = [
    vegetation_farm_01_32
    vegetation_farm_01_33
    vegetation_farm_01_34
    vegetation_farm_01_35
    vegetation_farm_01_36
    vegetation_farm_01_37
    vegetation_farm_01_38
    vegetation_farm_01_39
]

```

Or with one or more alias blocks:

```java

alias
{
    name = treez1
    tiles = [
        vegetation_trees_01_13
        vegetation_trees_01_14
        vegetation_trees_01_15
        vegetation_trees_01_8
        vegetation_trees_01_9
        vegetation_trees_01_10
        vegetation_trees_01_11
        vegetation_trees_01_17
    ]
}

```

```java

mainTile = [
  treez1
]

```
