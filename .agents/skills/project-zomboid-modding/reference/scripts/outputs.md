
# outputs

- **Soft Override:** False

The `outputs` block defines the items that will be created when the recipe is finished. Outputs are listed one after the other and follow the format below:

```java

outputs
{

    /* simple item output */
    item quantity item,

    /* using mappers */
    item quantity mapper:mapperID,

    ...
}

```

For example:

```java

outputs
{
    item 1 Base.Tissue,
    item 1 Base.ScratchTicket,
}

```

## Hierarchy

This block can be a child of the following blocks:

- [craftRecipe ](#scripts-craftrecipe)

ID
--

This block should have no ID.

## Parameters

This block has no parameters.
