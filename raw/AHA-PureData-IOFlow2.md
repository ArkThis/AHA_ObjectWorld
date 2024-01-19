# AHA - Working with Data Object Flows as in `Pure Data` (pd).

After having applied the following transformations from conventional "classic" 80s Files-in-Folders Data Layouts - and resolved, translated the Data, APIs and Applications into a working Object Data digital paradigm.

  * Support metadata already supported right now preferred from the filesystem level.
  * This prefers tags available on the FS-layer, over eg "embedded" - or from another database/XML/anything.
  * Relationships are properly supported as:
    * Links to other Objects (even remote pools)
    * Any kind of "possibly-referring" metadata
      Like a URI.
      Even terms of vocabulary lists.

This already relieves all applications and developers - including users - of the choice of a file-format to support annotating and working with data graphs directly over API UIs or CLI.

The availability of functionality like "keep meta with data as Objects" on any basic system is extremely inviting for any developer to make use of it.

It's like having a heating and a kitchen - and rather freeze and be hungry instead of making use of what's there?

If I don't need to worry/think about which database-system to "build on" and deploy and support: No. I'll just use the default filesystem. It just works. If you need it faster or different: Apply some other "transformers" (tools and UIs) - and have it your way.

Caches and Indexers are easily handled, because they've become "so common" that it's just another "basic admin lesson: data index-and-search".



# Pure Data: Visually editing Object Graphs.

If:

  * Any current data format can be broken down into a different set of
    related Objects.

  * And any application programming code is depicted - and run "as normal"
    from its Data Object (on FS-level) structure.

  * This means, Data Objects can be actively running code.

  * If we now map a generic visual programming language (see PD), and use that to "edit" (and interact with) our filesystem Objects.

  * Accessing and working with "Meta" or "Data" is same-same, and very clear because all (technical) properties of any "Data Object" (eg Movie, Image, Song, Construction Plans, Document, etc) is represented in the ever-repeating, all-familiar way:

> "An Object that has a meta and a data part. And meta may be pointing at other things"

And it just works.
From ground school-kindergarden to building "space station 11".

There is no more difference between working with files - and working with Objects that are the components of run-able applications/programs.

Since all Object Classes and methods are visible - in any way you interact with your "File" Objects: Even visually in 3D or VR.

Since you could attach and use any metadata to any objects, if one comes up with displaying options for Data Types, they'd probably come-and-stick with some Objects sooner or later, and then be distributed from there (if you like to) - to other Objects of the same "type".

Types are at first mind-wards compatible to MIME type-thinking.
Later on, "types" of Data goes into "phrasing Data properties" for related, weighted graphs. It is neither expected nor desired to always receive "the same correct answer".

Because with a complex datasystem, computing answers must at some point become fuzzy- or otherwise either take way too long - or be plain wrong in the end. The complex considerations, variations, etc etc - at some point don't pay out in the end, considering the "costs".
Just live with the fact that it's probably right, but we all know it had to make assumptions on the way.

There's always the "skip, we know better" button in my systems.
(Ich bin alt genug und weiß was ich tue-Knopf)

So, if I can store and handle my day-to-day data conveniently using Data Objects for storage of "payload" and my private-and-professional database/query/search/restructure needs.

99% of whatever is needed as "engine" functionality is provided by the local filesystem. And since that filesystem scales and works on large online networks, too and supports merging any kind of pools and types of data.

As long as their "accumulated" metadata and structural (relationship/links) information can be used to query "sense out of them". Or "select" anthing in a certain order.


# Let's go inside and play.

Now that any kind of Data can be handled and dealt with all the same:
By a common, yet highly personalizable and variable interfaces.

How?
As simple as we see now that "if we want and have the code" to support eg "FAT32" or EXT: it's there. It's done. It works.

And any other "application" is browser-engine based in most cases.
So anything you could do "in a browser" - or as an 'Internet website', you can render your Data - as web-app.

This means that any functionality you'd have locally, you could also have remote. Using identical code.

This already is the case:
Some applications you install on your home computer actually are browser-engines running "web code" that feels like a locally installed application. It's just "slightly" *cough* larger than an average other application of the same type/kind.


## Streaming data between Transformers

Imagine you'd like to use a certain functionality of your "favorite old program for doing X".

If that "old program" was already running as Holodeck process (\*)

(\*): Holodeck Process: Just an application being executed on runtime from the code/instructions/data in their Related Data Object Structure. Actually the same thing when binaries are executed nowadays, but imagine it like this:

A running process is not "one thing that uses up memory and CPU", but:
Data (compiled) source code doesn't need to be linked to "one executable". Any part of the code itself is "run-able". Like Python library code is written to have "active" parts when being "run" - additionally to its library classes, objects and functionalities.

So if program are written with AHFX systems in mind, any of their parts should be copy-paste-able, like querying a subset of "files" to copy to another "folder".

This breaks down data processing of any kind into "any computing languge function/method/property" can be depicted visually as pd-box (node) with connectors. Simply literally applying the "Pure Data" metaphor on the filesystem level.

It all becomes alive then.

As we see in "pd", any "box" seems passive at first. Think of boxes that hold plain "values" (strings or numbers), then boxes with hold "a block of text" - and others that even contain "binary data".

Any you interconnect them - and have active components that transform and forward any data you "feed" into it.

Thinking in the AHFX design, "data to feed" itself would be "another box" - if it's like "a file" - and group/query of Objects alongside a "folder" metaphor. Streaming data would simply be enabled by "referencing a source of meta/data to "something else".

And if that "something else" can be read (meta and data) - it can be "used" as input - or other socket to work with.


Having meta-and-data Objects on the filesystem with a pure-data interface and functionality to design active "coded" Objects.
Coated with run-able code.

Source code text is broken into individual, related Objects on the FS-level.

Imagine running the "Inspect Website" functionality web-developers know from any modern browser: you can WYSIWYG-interact with the rendering of your data-and-instructions.

So if there's a functionality "you like" - you can literally "rip" it out of any Holodeck application: By select-copy a certain button, then "pasting" it into a "Clean" (empty) "Object-Space" on a filesystem.

The program code knows (by relationships, and attached queries/code) what its dependencies/requirements are to work. This is the same code used to throw exceptions until it works.
I guess a compiler could figure out which parts of code are required to function standalone (=without warnings, when cut out).

Since we're not "cutting out parts of text from different files/folders", but the code is already stored as "related objects", like each Class/methods stored as separate Objects.

If it helps, imagine saving a source code object:

  * 1 Object Class definition (properties, methods, tests) = 1 file.
  * 2 Objects = 2 files, 3=3, n=n and so on.

Now split up again:

  * 1 Object Class defintions:
    * Object structure declarations (like Java "Interface" idea)
    * Class Property definitions : 1 related Object
    * Class Methods : each one a related Object

So you could cherry-pick even which methods a class "has access to". Because since methods are "related Objects", it's trivial to use "Other related Objects" that match the requirements (Interface definitions).

These mechanisms can be used to "know" by-copy request which code-and-data parts (=All the same FS-default Data Objects. Just different types with different information stored).


If the Holodeck-FS performance allows to strip "the pure encoding" as plain and raw as possible by default - and move anything else to either the "meta part" - or have as related Object: What would remain is in many cases the "Data Payload" of most objects is "pure, somehow stream-able" data.

Because any outside structure has already been resolved onto the filesystem level.

If we break down programming code components into filesystem-objects, and keep code-and-programs like that even until (or during?) runtime: Interacting with computing machines would become "native" in its own way. Interoperability by design.


# Where's the catch?

Overhead.
More spaces, more computing resources.
Yet, however: it may actually be so, that by providing the "real basic" functionlity now on the FS-level, and shifting balancing and performance off to "CDNs" - Content Delivery Networks - and Indexer farms, and so on?

For large-scale processing: currently working worldwide, and consuming fantastillions of money, time and lives per second. To watch cat-porn-on-youtube-on-a-so-called-smart-or-at-least-mobile "device".

For fun.
So we're already paying for that in one way or another already.

As seen on Linux-vs-Windows: Orchestrating applications and packages made things more stable, interoperable - and consumed less resources.

However:

  * Converting text-based metadata from file-format (or database) onto filesystem level makes no difference in terms of data-size.

  * Converting numerical data to strings "as the new default":

    There was a time, when XML was new, and the choices had to be made, which data is "worth" blowing up in filesize and computing requirements, for the sake of having the data in "TEXT" form now.
Only so we humans could at least have a chance to work with it.

And it was worth it.
Look at "The Internet": HTML+CSS is also "just text" - and requires significant resources to be made "active" and render websites and their functionalities. And looking good and fast at the same time.

We already have that.
Running on hardware we force onto small kids in kindergarten already.

Translating popular data formats, and application (code trees) into active Objects may increase storage requirements, but due to better handling and design of its structure, it may be better to use - even if slower.

Simply by the amazing advantages given by the options to work with "related object graphs" without the currently accepted default-by-design boundaries anymore.



# No need to "sort it out" before.

Or do you think "The big cloud storage providers" on our world right now are ever planning to require you to "clean up your data", or use a given standard?

> **The absence of defined structure can be surpassed by direct-addressing by cascaded queries - in due time.**

It does make sense to agree in using "common terms" (or any other form of common reference/identifiers) to relate data constructs which originate from different sources - and "realms" (times, culture, possibilities, style, etc).

However, it is not necessary anymore to define a fixed structure "where" in a "tree" or hierarchy - a certain "information" can be found.

Is this value for "language" for the whole work, or just parts? Like individual audio tracks, etc.

Since the Data Objects themselves literally "self-describe" their structure - any structure, any relationship they might have with each other - it can be well described on the plain filesystem level.

Annotated, related Objects.

Instead of trying to force order ontop of "the world in data", that time is better spent simply "waiting" until a Holodeck query is returning the desired "answer".

Instead of having to implement field definitions, standards - and mappings from one to another: rather come up with suggestions for "field terms" - and a cataloguing-style handbook, with different styles for different users.

All co-existing on the same Object Types they interact with and create.


# Real world examples


## Self-showing JPG.
## Self-showing "Movie".
## Self-build-and-installing Blender
## 

