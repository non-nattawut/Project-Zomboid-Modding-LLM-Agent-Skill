
# physicsShape

- **Soft Override:** Unknown

Defines a 3D object's physical shape to be used as a world object.

For example:

```java

module YourModule {
  physicsShape ramp20segment5w {
      mesh = physics/ramp20|Segment5,
      translate = 4.0 0.0 0.0,
      rotate = 0.0 270.0 0.0,
  }
}

```

## Hierarchy

This block can be a child of the following blocks:

- [module ](#scripts-module)

ID
--

This block can have an ID.

- **Optional:** False

- **Can have spaces:** False

## Parameters

### `mesh`

- **Type:** string

The path to the model's mesh file, relative to the folder `media/models_X`.

### `rotate`

- **Type:** array (array of float, separator: ' ')

The rotation of the model, in the format `x y z`.

### `translate`

- **Type:** array (array of float, separator: ' ')

The position offset of the model, in the format `x y z`.

