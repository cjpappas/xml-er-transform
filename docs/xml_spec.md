# XML Specification

This file outlines the XML specification we use for writing EER diagrams.

## Structure

Our XML diagrams consist of a top level `diagram` tag followed by an `entities` tag and a `relationships`
tag. The `entities` tag contains `entity` tags which define the entities in the ER diagram. The `entity` tag
can contain multiple `attribute` tags, which define the attributes of the entity. Inside a `relationships` tag
there can be multiple `relationship` tags, which describe the relationships between entities in the diagram.
A full list of tags is provided below:

| Tag | Attributes | Description | 
| --- | ---------- | ----------- |
| `<diagram>` | None | Top level tag, contains **one** `<entities>` and **one** `<relationships>` tag. |
| `<entities>` | None | Tag that can contain **one or more** `<entity>` tags. |
| `<realtionships>` | None | Tag that contains **one or more** `<relationship>` tags. |
| `<entity>` | `id` - id of the entity (unique, required)<br>`name` - name of the entity (required)<br>`type` - one of `strong`, `weak`, `associative` (optional, default is `strong` if `pi` attribute present or `weak` otherwise) | Tag that defines an entity in an ER diagram |
| `<attribute>` | `id` - id of the attribute (unique, required)<br>`value` - name of the attribute (required)<br>`pi` - one of `true` or `false`, indicates attribute is the primary identifier for the entity (optional, default is `false`)<br>`type` - one of `simple` or `multi`, indicated the type of the attribute (optional, default is `simple`) | Describes an attribute of the parent `<entity>`.
| `<realtionship>` | `id` - id of the relationship (unique, required)<br>`name` - name of the realtionship (unique, required)<br>`fromEnt` - id of the entity from which the relationship starts (required)<br>`toEnt` - id of the entity to which the relationship goes to (required)<br>`value` - one of `one-one`, `one-many`, `many-many`, describes the cardinatlity of the realtionship (required)<br>`leftCons` - one of `opt` (optional) or `mand` (mandatory), describes the constraint of the `fromEnt`(required)<br>`rightCons` - one of `opt` (optional) or `mand` (mandatory), describes the constraint of the `toEnt` (required)<br>`leftVal` - one of `0,1`, `1,1`, `0,M`, `1,M`, describes the cardinality and constraint of the `fromEnt` (optional)<br>`rightVal` - one of `0,1`, `1,1`, `0,M`, `1,M`, describes the cardinality and constraint of the `toEnt` (optional) | Describes a realtionship in the ER diagram. |

In summary the XML should look like:
```xml
<diagram>
    <entities>
        <entity>
            <attribute />
            ...
            <attribute />
        </entity>
    </entities>
    <relationships>
        <relationship />
        ...
        <relationship />
    </relationships>
</diagram>
```