# AHA - A Holodeck by August

## Protoyping ideas.

**This is still a rough draft. A braindump if you will.**

Although I am pretty certain, that it is rather feasible to implement quite quickly.
User acceptance is probably very much related to how inviting it is to make use of our APIs and MinIO configs. And if there's a way to also have it on mobile devices. Literally travelling-well by copy/paste over microSD cards - or instant messenger file transfer.
How quickly and seamlessly more and more "apps" and systems support AHFX-compatibility.

> "Just add the meta to the data whenever you load/save/edit/copy/whatever data."
> Use common libs if possible.
> Port them where needed.
> Get paid to do so.

It's just so much better.
Like tipping a good waiter and
Like washing your hands before you eat.
It's common sense.
And good courtesy.

> Support and use Object storages, and encourage developers to support it in their applications, too.

With GNU/Linux FOSS software, it may even be feasible to retro-fit *any*
application to keep on rocking in an Object filesystem world.

A working prototype should display the following features:

  1. Copy/Paste and Edit Data-Objects: Bit-Proof.
     * (binary) Payload
     * Its Metadata

  2. Query metadata directly off the filesystem.

  3. Provide means for speeding up filesystem requests:
     Have indexer with sane default configuration presets.

  4. Scale as currently reasonably useful.
     For example: From local HDDs to NAS to cloud storage provider.
     If you need more diskspace: Does it scale?

  5. Work on local, any existing (!) filesystem SD-card or USB-Stick.
     To show how a native Object-Filesystem entry can be converted easily to
     something like a SQLLite containing the metadata for your files (on the microSD
     you put in your phone). And basic OS libs that allow native handling and access
     of that metadata by the abstraction layer of a simulated "Object Filesystem 'Lite'.

  6. Provide some means of "access security".
     Or at least concepts for guarding Data-Objects.


# Prototype PT-AHFX: Ideas and Plans.

Why should this work?

If what I say would be true, why doesn't that already exist?

Especially, since I myself say:
All the required components exist, FOSS-licensed (!) and global-network, large-scale production stable.
So what am I proposing as "new" here?

A different implementation paradigm. A different way of thinking/seeing data:
If you could store a database entry as natively and plain-dead-simple as writing data into "a file", why bother to *not* do it?

It may require more diskspace than the previous (binary) encoded, embedded and located all over different systems and places: normalizing this onto the filesystem layer, in plain text, may become a new underlying base ground that makes it really more "natively" to interact with computing and data.

You can actually mould your digital environment.
In VR if you like.
Plug-and-Play compatible.

Simply, because we finally have the tech to **put our META where our DATA is.**

Nothing more.
Nothing less.
So much will change.


Enjoy reading on!


## Existing Components

These are my suggestions for possible candidates to assemble and test the very first prototype system with.
My requirements are that they are FOSS-licensed, and "feel right" to be part of this - and Open Standards, Open Hardware, Open Specs, Open-Anything. Please: Let us do it open and awesome for everyone of us right from the beginning.

We have the tech and computing overpowers to do so.
So, here is a list of existing software/hardware projects, that should provide building blocks and documentation for setting up a first PT-AHFX system.

  * MinIO
  * SNMP tools/specs/libs
  * CSV, JSON (XML?)
  * Indexing for full-text search
  * Graph-Relationship-Indexing
  * IIIF
  * Web-Browser Engine (HTML5/CSS3/etc)
  * Filtering/Transformation engine for metadata (like XSLT for XML)
  * A few demo-applications to test potential behavior:
    * music library player application
    * picture collection organization application
    * asset management system


# PT-AHFX Mark 1

"Mark 1": The first level of feature implementation.  A basic working version,
performance put aside for starters, and simple "import files + metadata and
convert them to filesystem "Objects".

The notes here also contain possible candidates that could be use as jumping base.
Like literally jumping off the shoulders of Giants. :)

The basic components required for a good demo system which could give developers and users a glimpse of how the AHA-Object World would "look and feel". From commandline to GUI: IIIF viewers being the base for the Object display and interaction base.

## The basic core

would be a combination of:

  * An object filesystem that can be used on local and networked storage (eg MinIO).
  * That can handle and store metadata with the file payload.
  * That provides APIs to interact with both: meta *and* data in a generic way.
  * Indexing cascades and caches.
  * Pattern/Graph visualization languages and interpreters to render the semantic views of the filesystem.
  * One-time-off converters (possibly in Python and easily cross-platform):
    * de-embedd metadata into Objects.
    * resolve media container formats into relationship graphs with metadata Objects (eg streams, subtitles, metadata).
  * Stable APIs (FOSS on a FOSS-stack) - for developers.
  * Demo applications (CLI and GUI, web-engine frontend examples (IIIF-ish), etc).
  * Frontend: Web-browser engine locally.
    So any viewer/editor written for AHFX, would also natively run online as well as locally.
    And would scale to any other device - as well as HTML5/CSS3.
  * Since the frontend is merely a looking glass to shape, organize and annotate and use (!) your digital Objects, It very likely doesn't matter with what application you're accessing your stuff: If it speaks AHFX, it's all crystal clear. Plaintext name=value. Possibly nested or grouped.

> As long as the functionality of the underlying (network) object filesystem is stable and sound, and keeps the "meta with the data" in full integrity - it must be possible to implement the basic AHFX features with code-libraries. It may be favorable to re-design certain parts later on, most likely due to performance desires.


## Prototype Setup - Overview in greater detail:

  * Setting up MinIO:
    * Config so that it's easy to switch between local-only and network-aware storage.
    * Just to prove that this design shall scale natively from local-to-nas-to-cloud.
  * Enable metadata storage/handling for each object.
  * Configure and write basic metadata input/output and handling operations.
    As CLI/GUI-Tools as well as programming libs and filesystem highlevel-API.
  * Starting in Python on GNU/Linux.
  * Using the current filesystem options as they are.



# PT-AHFX Mark 2

When having a reliable filesystem with metadata setup, the next steps are to show the benefits of the Data-Object paradigm: 

Import large scale, real-world public cultural heritage collections, and convert the meta and data information into Data-Objects. Then implement a demo-website, showing how easy it is to code and interact with these Data-Objects.

## Demo 1: Cultural Heritage Collections

  * Harvest Kulturpool Metadata and create (script) a real-world copy on the MinIO.
  * Attach the corresponding XML/JSON metadata as-is to each "file".
  * It's likely that only the preview images/media files will be available for automatic download.
  * Build an index to make it accessible - and combine that with a IIIF viewer for browsing.


## Demo 2: Music collections

  * Take a simple FOSS music library application (eg Clementine, Rhythmbox, etc) as base.
  * Switch the internal database methods to the AHFX-aware libs/APIs.
  * Build "the usual music database" using a generic FOSS indexer.


## Demo 3: Show your "Objects" in different ways:

  * the classical folder/files view.
  * by relationships (as weighted, click-able graph)
  * as browse-able tag-clouds
  * Like a professional catalogue-entry

Maybe make use of NoSQL databases (MongoDB, etc) or GraphDB engines to high-level handle the filesystem Objects.
By connecting to those paradigms, it's easier to grasp this new Object-World-Thinking, by making use of existing tools.



# PT-AHFX Mark 3

Show off some more benefits of the AHFX filesystem:

De-embedd metadata. Resolve any embedded metadata use-cases and contents to the filesystem. Offload it there. 
Now, *any* digital data (Object) can be annotated and enriched with any metadata - even relationships to other Objects, forming simple and complex graph structures over time. Quasi automatically.

The data you engage and work with becomes moldable Objects in Space.
All that matters is:

  * How much diskspace do you have? (anywhere in the world)
  * Do you have enough computing power or memory to compute your "quest(ion")?
  * Do you have "access" to the Objects required to fullfill your requests?

With Mark 2, you can see and use all your existing data files with all their (embedded) metadata stripped blank into plaintext onto the filesystem level. As viewable - and editable - as a filename.

> Right Click : Edit. Save.



## Demo 4: Resolve embedded metadata

  * Take embedded-metadata extraction tools/libs and read as many file-formats as possible
  * and copy any metadata tag (mostly name=value, I presume) onto the AHFX filesystem level.
  * Adapt/implement a IIIF web-engine for viewing and editing this metadata.

Which use case would remain, if any metadata could now simply be stored *with* the data payload in the basic filesystem? Safe and interoperable. Even this simple step of de-embedding metadata onto a level that is accessible - and comprehensible - in plaintext name=value pairs for anyone: File formats made (in)visible.

Possibly annotated with URL-online references to related Objects or further (related) information in other "Object Domains".

Right-Click-Whatever:
Imagine the ease of access to any previously embedded metadata is now decoded and visible in any application, to any user - and completely taken for granted.


## Demo 5: Resolve media container formats

  * Translate different AV-media container formats (MKV, AVI, MOV, MXF, etc) to a relationship graph between its formerly internal "streams" or metadata.
  * Adding new audio/video/subtitle/etc streams to a "video" (Object) would merely be a drag-n-drop of that "new data to attach" onto the "video" (Object) in your browser, describe the relationship and you're done.
  * Same for removing or editing any other stream or metadata field:
    Just right-click-whatever you'd like to do.
    On any file format.
  * What difference would remain between existing media container formats, if resolved onto the filesystem level?
    Could these differences (=interoperability hurdles) be otherwise "resolved" into the Data-Object paradigm?

Annotating each audio- and video-track, even adding links or "embedding" (=linking to another Object or URL) is plain simple drag-n-drop or whatever CLI actions that are common knowledge. As easy as editing filenames or moving things around in folders by flipping a finger.



## Demo 6: Resolve file formats technical metadata

  * Copy the basic technical metadata, commonly structuring a file format's header, to the filesystem.
  * As Strings. I'm not sure if the complexity overhead is worth it to handle NUMERIC and STRING variable types.
  * This would have to be calculated.
    I assume it may have serious impact on data size (piling up) - and performance.
    Imagine: taking all 2-to-4 Byte header data and blowing it up to a number-string.
  * Yet I still encourage to implement this converter to allow experiencing
    what it would be like to handle Objects and see their file format
    properties natively and easily: plaintext name=value.
  * The performance- and storage-increment (if even noticable) may well be worth it.


## Demo 7: eMail Program

  * Move email data(base) storage handling to the Object filesystem.
  * Compare converter needs when now requiring to move emails from one application/system to another.


## Demo 8: The Object Registry.

  * Save configuration *with* the executables.
  * Instead of /etc/me.conf - store the plaintext config as-is with the
    executable (because it's an Object and it can hold its metadata now).
  * If you must store it in its own Object (for access reasons), simply make a relationship to the executable.
  * Therefore, if one wants to view/edit the config: it will instantly be found.
  * And since the config-editor is your default Object Editor (of your choice), your interface is familiar.
  * Comparable to the idea something like "Windows Registry meets object-idea as folder/file paradigm of `/etc` in Linux"

Making backups of specific configuration setups, is making a backup of your Data-Objects. They're self-describing graphs, so you can pull in the required "other Objects with Metadata".


## Demo 9: Blender Objects

Write a converter that translates Blender project files - and all objects therein - into filesystem Object graphs. Regardless how "large" these Object clusters would become: It should not matter on a proper AHFX implementation, because any speed needed is merely defined by two things:

  * Can we make it go faster? Add Indexers? More machines? More electricity?
  * Or: Sorry. That's our current limit. You'll have to wait.
    Yet, rest assured: It'll be worth your while.

A Blender project depicted as Object graph, natively in a filesystem.
You could view whole 3D worlds, simply by your default Object-Browser, since it is based on a Web-Browser engine, and therefore capable of rendering the "Standard 3D Objects - Blender Syntax" in a IIIF viewer.

Or display whole scenes and timelines - just by "looking" at your Data-Objects the usual way:
Seamlessly interoperable.

If this prototype is considered successful, it may be interesting to try translating other CAD-construction formats and standards to that new common "Object Norm". And see how that affects interoperability - backups and archiving.


## Demo 10: The automagic AIP

  * Hashcodes are part of the AHFX standard.
  * So any Object has a hash - and it has been validated (upon request) - and logged the result/timestamp.
  * If anyone ever "touched" an Object and hat auto-resolving/arranging/annotating turned on - with type "public", those tags would from then on go on with the Object over its lifetime.
  * An application (if enabled to do so) can leave a "I was here" mark as "coding history" entry with an Object it engaged with.
  * As verbose as configured.
  * Links (or copies) of related Standards or Decoders can easily be provided with an Object.
  * Links to VLC with media files. Like that.

Any metadata could simply co-exist over the lifetime of an Object - and be preserved as-is on any digital carrier.
In plaintext.

Including the option to link (or relate-copy) ArchLinux build recipes. That would allow to auto-build any environment you'd need to engage with that digital object. As long the the ArchLinux packages are available, and the building environment runs, you could eg compile your MVC media player out of thin air and "just watch" the movie.

And that video file "format" - as Object Graph - was 50 years old. Still alive and kicking.
Just plaintext and relationships and URLs. And payload.

AIP: Solved. In Object Graph Storages.
