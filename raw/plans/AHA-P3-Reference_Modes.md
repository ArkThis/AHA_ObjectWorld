## Reference Modes

Metadata values may either be the actual term, or a reference.
It would be great to be able to reference in different ways, to deal with "context".

  * Local
    * ObjectID
  * Remote
    * ObjectID
    * Any Linked Open Data ID
    * WikidataID


## Local metadata field reference

Another important question is also:

> How to allow reliably referring to 'other metadata fields' on the same object?

For example, I have multiple "title" fields with a song, and I'd like to "annotate" that I know something more about one of these titles:

  * title = X Marks the Spot
  * title = Final Album

I'd like to add that I've made up the 2nd title:

  * title1 = X Marks the Spot
  * title2 = Final Album
  * title2:remark = Bogus invention by me.

I am still uncertain of how much - and even *if* - the "name=" should offer any fancy syntax options.
I like to keep it rather simple.

Therefore I'd suggest to allow at least *one* way to refer a local metadata field to another one.
Related objects are done differently. Those are simple entries, where the "value" is an Object ID.

**There has to be standardized way to know if "value" is literal or reference.**


### Local, but related Object reference

Any VALUE can either be the actual word, or a reference. Like "artist=Q000001". And they may co-exist.

Open question: How to distinguish between a literal value and a reference?
A suggestion would be to support XML-tag syntax for non-literal values.

  * artist=XBloome
  * artist=<ObjectID value=""/>
  * artist=<WikidataID value=""/>            <--| but those would be a remote reference.
  * artist=<NationalLibraryID value=""/>       <|
  * artist=...you get the idea :)

How does [EBML](https://en.wikipedia.org/wiki/Extensible_Binary_Meta_Language) do it?
What if "name" syntax would be SNMP-ish? How do they handle local field references?


## Remote

Anything that requires a network connection.
Must work localhost-compatible.

  * artist=<ObjectID>
  * artist=<WikidataID>

The ObjectIDs are designed to work for local, as well as wide-area storage pools and even long-term contexts.

