
# attachment

- **Soft Override:** Unknown

Defines an attachment point on a [model ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/model.html) or [vehicle ](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/vehicle.html) block. The ID is the attachment name, it can be a custom ID or an existing one often used to define specific attachments. While manually modifying the attachment block is definitely possible, it is recommended to use the [attachment editor ](https://pzwiki.net/wiki/Attachment_Editor) to create and edit those attachments.

The syntax of this block should be as follows:

```java

model upperScriptDefinition
{
    ...
    attachment attachmentPointName
    {
        ...
    }
    ...
}

```

For example:

```java

model Burger
{
    mesh = Burger,

    attachment Bip01_Prop2
    {
        offset = 0.0142 0.0401 0.0000,
        rotate = -23.3606 21.2788 37.5386,
        scale = 0.8280,
    }
}

```

For a full list of attachment points, see the [attachment ](https://pzwiki.net/wiki/Attachment_(scripts)\ #Attachment_Points) page on the PZ Wiki.

## Hierarchy

This block can be a child of the following blocks:

- [model ](#scripts-model)
- [template ](#scripts-template)
- [vehicle ](#scripts-vehicle)

ID
--

This block can have an ID.

- **Optional:** False

- **Can have spaces:** False

## Parameters

### `bone`

- **Type:** Unknown

The name of the bone to which the model is attached to.

```java

bone = Bip01_L_Hand,

```

### `offset`

- **Type:** array (array of float, separator: ' ')

The position offset of the model relative to the bone. This is a vector in the format `x y z`. `cpp
offset = -0.0300 -0.1020 0.1210,`

### `rotate`

- **Type:** array (array of float, separator: ' ')

The rotation of the model relative to the bone. This is a vector in the format `x y z`. The values are degrees.

```java

rotate = -60.0000 -49.0000 -3.0000,

```

### `scale`

- **Type:** float

The scale multiplier applied to the model attached to this attachment point.

```java

scale = 0.5,

```

### `zoffset`

- **Type:** Unknown

No description provided.

