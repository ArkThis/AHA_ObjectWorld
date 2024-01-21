## May obsolete or simplify future data migrations - and even merging collections.

Simply "pour your set from your data pool over into mine".
Or even copy/paste it on your flash drive.
It's all the same: Your data collections are now a bunch of describable, related objects.

There is no more difference between an object with or without data payload (the actual "big files"). It's yet another object. With different properties.

Instead of having to think of a clever way for integrating previous IDs and existing metadata in whatever (digital) layout - mapping and transformations - hours of coding and evaluating - millions!
Simply copy the data over onto your storage.
And do that copy in the "old image" of creating "a target folder" (<- folders are MDOs too), called "Ingest-202308, then drag-n-drop whatever on it.

Each folder/file will become a Object, with the additional tag "Ingest-202308", is now part of your collection.
They all come with metadata either directly stored as text on their object, or retrievable by relationships with other objects.

Local or remote.
The ID syntax and design of AHFX allows by design to refer to any Object-ID (the one with the 🌟️), and these references will still work, even if your object travels over networks, operating systems, anywhere: "it's just a copy of ...".

There will generally be less metadata field mapping and transformation required, because of the design of AHFX:

  * By making basic metadata handling so native and so basic,
  * I'd assume that most people/users are happy to get a suggestion for metadata field options?
  * I like the familiarities of different music collection/formats and programs (metadata layout).
  * If two "collections" share familiar "name=" schemas, AHFX keeps "both" values.
  * One value of each "name=" set can be toggled "me".
    "me" instead of primary, master, main, first. Just "me".
    The value set as "me" is the one used if no selection which item in the array to get.
