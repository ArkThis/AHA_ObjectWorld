# AHA - A Holodeck by August: Keeping things sane and tidy.

2024-01-07

The term "data swamp" already exists, and my design suggestion to try keeping (accumulating) metadata over the lifetime of a file, some questions arise, and I'm sure some engineers must have given them thought already:

  * What makes a data lake swampy?
  * What are the (negative) effects?

  * Shall I clean up (normalize) tag "names" or rather keep and auto-reference them?

  * **How important is controlled vocabulary, over fast full-text indexing?**

  * Perform dynamic "normalization" by creating look-up Object graphs, that contain lists or values, to help the indexers provide "(more) common/existing terms"?

  * Fuzzy search as functionality is already provided by in-house office data management systems with ElasticSearch and API queries. So code exists and performance is surprisingly great actually.

  * Dublin Core and "required fields and common terms" lists (TODO: ask Philip about the github page/standard)
    Definitely a good start!
    Including dcterms of course.

  * What if:
    * the same "intentional value" (eg "camera type") is stored under n+ very different "name" tags?
    * Does it matter, if a generic mapping information can be given that "name tags with the following labels, map to 'camera type'". Am I thinking too blue-eyed here?

  * When should (dead-link) relationships be removed?
    Does it matter for handling/usage or is it merely affecting performance, due to "unnecessary load cycles" in processing and data I/O.

  * Whatif each Object had its own "Trash" area for metadata?
    * Or simply keep it in versioning, but work on the currently checked out copy (! good one !)
    (More about that below)

  * What about doing "atime" (for a while? on demand) on meta/data?
    Using those stats to decide which meta is accessed to later on (disable atime when happy) use that to auto-map and weight your preferred tag names/values?

  * Would it make sense to allow tag-relationships?
    Would it be okay to implement that as separate Object-Graph?
    (To keep it Lego simple, knowing it costs more performance?)



# May versioning and tiering play a role in this?

If tiering and versioning concepts may be applied to any Object all alike, and since `meta-equals-data` is the design key, metadata changes can properly be versioned/tiered as well.

Therefore, your "swamp" may keep itself clean, by "digesting" by versioning - and moving less-accessed meta/data into a shadow copy, accessible and logged by eg "git"?

I'm pretty sure git is used on embedded systems like wifi-routers, so we can assume doing the same on "smaller" devices than fully-blown PCs or RPis.

Requirement: A way to "duplicate/relate" tags to each other?
Is this a good idea, or trying to do it all and fail?
Imagine being able to tell your filesystem that "artist" is the term you prefer for ... (<- select suggested tags here). And you can convert any metadata layout at any time using any tool.

Have a trigger to re-index caches and services.

Auto-remove with commit-message "meta/data not accessed since ..."?
So the old copy is still there, but not considered "present" anymore.
I recall MinIO offering config options for data "fading out".


# Learning attribute names/patterns

Even without AI, but probably quite a nice field to deploy "machine beings" to help with our data (digestion).

I'm simply wondering how to diffuse the quite-likely "creative term" mismatches, though similar intentions (thx different vendors)? 

Imagine implementing "digestion" processing Objects. Transformers of different kinds.

Any Object Graph containing code may be "ran".
Therefore it is trivial to create generic Transformer Objects that may transform one input data to another (format/layout.

There is technically no difference between runnable Transformer Object's code - and that of any other Object that may contain code (and be marked runnable).

The first and most populars are audio/video/document/image format converter Transformers.
Since Transformers may operate on themselves, they could literally transform themselves - in arbitrary Object-Graphs that perform functions. PureData as engine.

Interesting whatif a good AI would understand that Transformer way of coding, and being able to (re-)construct itself - and even new Transformers (=replicate? O.O).

The simple nature of the AHFX design would allow basic elements to function automatically, if spawned by code-generators.

Wow.
