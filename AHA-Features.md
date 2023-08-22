---
title: AHA - A Holodeck by August - Feature Overview
author: |-
        Peter Bubestinger-Steindl \
        `(peter @ ArkThis.com)`
geometry: a4paper, margin=2cm
toc: false
toc-depth: 2
linkcolor: blue

date: 2023-08-16/17
---

# Abstract

This contains a listing of "features" that AHA would provide.
I'll try to keep them short for starters, then gradually reveal complexity and details - and sort them in order of "ease of implementation and user desires/priorities".


# Glossary

  * Object: "Meta and/or Data Object"
  * Object: A data object, as implemented in current state of the art "object cloud storage" storage systems.
  * AHA world: An environment, where the AHFX is supported and implemented beyond any transition stage: This is a well-running object oriented digital environment. The AHA world.
  * AHFX: Name of the "AHA-world Filesystem. X." like ext4 or fat or ahfx.



# To clarify: Kernel vs Userspace vs Other

  1. Basic, common funcationality may be implemented on the kernel's filesystem (driver?) level.
    For speed and reliability.

  2. Other (even considered basic) features should probably be implemented in Userspace.
    For convenience of development and interoperability.
    I imagine something like [POSIX (Portable Operating System Interface)](https://en.wikipedia.org/wiki/POSIX).

  3. Even more high-level functionality that is considered "more specific" or "more complex than average".


Some features that would make AHFX really powerful, may be functionalities that are too complex to belong on a filesystem driver-level, but should be "taken for granted" and reliable enough to be available on any computing environment (if anyhow possible).

Similar to a unix-ish system:
Some commands or other things are on 99% of all environments. Some are more specific. There's great benefit in any common ground though. With AHFX to work at its best, it should be similar.



# Keeping it simple.

## References

When it comes to refering to "other things", it may be better to always spawn a new Object for this.
Instead of having a syntax (and complexity) for referencing local fields, maybe it's better to intentionally *not* have that option, and rather live with (possibly way-)more Objects.

That may be an issue when AHFX is new though.
I expect accessing "local metadata fields" quicker (not necessarily "easier" from a users or developers point of view) - and more reliable (or simply without interrupted flow in any way).

Whereas "lifting" related Objects: That may greatly depend on how "Objects" are actually allocated and their binary data being read.

On the other hand:
If it's simply *required* for regular use to have a good performance/behavior with getting the data from related Objects: May this provide a better "engine" earlier or more widely supported?
Like: They had to come up with hardware-decoding to make digital video go mobile.

What if the "name" field may have syntax? What if XPath may work by default?
That would require an XML-like structure syntax. Possibly JSON would suffice.
Stored as EBML on the actual filesystem blocks? Only rendered like "text-tagged" data in the Data Browser?


## Small payload stored as metadata "value"

Hm...
One object shall have 1 payload. Right?
So that would be clear and clever hack. Right?

If not limiting the data size of what is stored in a (bit-proof!) metadata name=value field, it's quite tempting to put existing metadata (XML, JSON, CSV, text, etc - even PDF!) right as a "value" with the Object's "other" main payload.
Anyone who likes embedded-everything or "packed" AIPs: Here's your friend.

Should that hack be allowed?
It would allow an Object to exist "more robust/standalone".

Whereas, if we didn't allow this "feature", anything "not just a regular string" would have to spawn a new Object+payload - and relate to it properly.

Depending on how well "implementation dialects" would evolve and be resolved in the AHA world. Because it may not matter that much, if "Resolving Objects" is a commonly used basic feature of any Data Browser or Object-aware tool that anyone would now of.

Resolving would simply mean to pack/unpack any Objects by either "packing" as much metadata into the fields as possible, or "unpack": move as much "embedded" metadata to a proper Object-thinking data structure. In this case "embedded" may mean binary-embedded (like "MP3 tags") or "embedded payload as metadata field".
The "unpacking" steps (and code) would be almost identical.

For the beginning, traversing the graphs may cost quite some performance.
It's already noticable when handling metadata standards: There's a reason why some field is "here" and not "related to..." - in order to become more widely "accessible". In a performant and usable way.

So maybe "packed" Objects make sense when AHFX is new.
Later, if performance allows, working with "unpacked" - more related - Objects to handle as preferred default.
This will only be the case if any "AHA world" is built so well that "it just works" - and even your related objects are as reliably accessible (and travel and "age" well over time) as filenames right now.

Probably we'll see a mix of "packed" and "unpacked" - even "mixpacked" ;)

In the end, all that matters is that the right "data" can be accessed and used at the right point.


## 


# Overview of Features

## May replace all embedded metadata needs.

Why bother to write support for yet-another-fileformat, if anyone can simply use the AHFX features?
Any program/developer not doing so would spend way more time, while becoming less-interoperable and user-friendly over time in comparison to simply using AHFX.


## Seamlessly (downwards-)compatible to file/folder naming workflows and applications.

In AHFX, your data objects will be "called to life" whenever you copy a path or a file over to your "AHA world". You will then "see" and handle your "files" the way you're used to:

  * Folder structure
  * Filename
  * Timestamps, access rights, etc.

But now these metadata fields are stored on the AHFX object filesystem layer. Using the very basic and intergalactic uber-standard, just like "plain filenames" are now.

Now, you can choose to work with your objects like that, or you can use other "interfaces" (think IIIF.org) to interact with your "digital objects". Technically they are all the same now: They're just "views".

These "views" are to be implemented in a browser-based manner.
I would suggest that, since then all web-proven website code can be re-used here easily.
Your "file manager" would be renamed to "Data browser", or "Habakuck!" or whatever.
Under the hood it'll be a friendly Firefox-fork (like Tor), 


## Hardcoded black/white security:

private/public.

that's it.
You wanted digital, here it is: Either yours or theirs.
;)

Yet, of course the AHFX implementation specification clearly encourages anyone to add more "object spaces", yet I'd ask you to at least hardcode-hardcore respect private/public as good as you can. In code and spirit.

Have respect.
Anything marked private is off limits.
Anything marked public is as good as gone out into the wild! Anything can happen.

Yes, you can add additional so called "object spaces" to group access conditions.
You can create a new object space, by right-click-new then drag-n-drop whatever you want to assign this to. Done.



## Private Object IDs

Like localhost or LAN address spaces "reserved" to be discarded when leaving a certain domain.
Object spaces are one thing.

It can make sense to define some object IDs to mark as "seriously private".
Like `🌟️M20230816...`

Any code by any developer should respect that "M-prefix" and make sure to discard M-prefix Objects if encountered "out of private". As a courtesy of the housekeeper ;)

Should one consider making a private-ID object, you can simply copy/paste it over and assign it a new, regular ID.
It may give you the hint that you're "de-privatizing" that object, which you confirm. Done.
It really *is* that simple.


## May make backup plans and archiving more convenient

  * apply crontab-like timed-execution information to the object you'd like to "start".
  * There are no more folders! You don't have to worry about "where" to store (or find) your backup/copies. Your tags stay and travel well.


## May replace all (media) container file formats.

By "dissolving" (or translating) them into Objects.


## May provide links to editing/playback/view requirements

Imagine you receive a "copy of whatever.xyz" from a friend or anyone else:
How do you open it?
It's common courtesy for anyone to at least (if they can) provide a link where I can download the right stuff to access this file. To watch it, to listen, to read - to create, anything.

Like:
  * "application=vlc"
Or:
  * "encoding=h264"


## May cover file/data versioning needs.

If any versioning metadata would be stored in proper AHFX MDO layout, the object layer could be used to store interoperable versioning information.


## May replace Package Management functionality.

Where do you get your executables from?


## May provide torrent/magnet links and functionality in userspace.

With common or popular objects it would be great to easily "enable" a torrent share on it.
You can now not only share any payload data (files, as we call them now) - but also any metadata-only entry. Your catalog.



## May replace the necessity for spreadsheets index files.

Using spreadsheet applications (eg LibreOffice, Excel, etc) to create an "index for some collection" comes naturally, when there is no way for properly annotating your work in a consistent and reliable way.

Like we all did and do with filenames and the quest for the right foldername.

If there was a way to actually put the metadata right with the digital object it's talking about:
Why even bother using another application?
You just put the metadata in a right-click-whatever interface, and off you go!



## DAM features may be replaced by plugins/views for a Object browser.

Modern DAMs are already web-browser based. Front- as well as back-end.
Now if the database "is already there" - because it's your filesystem - any DAM functionality should be made as "website plugin" for your data browser.

Why bother to have an extra program for annotating files - and have search queries to access them?



## May work even more awesome with IIIF.

I imagine the data browser to be a friendly awesome-FOSS-web-browser fork (like Firefox/Tor), running "object-fields to IIIF manifest code".

  * Implement default file manager functionality in an open web standard.
  * Implement all data-views of any kind in the same way.
  * Examples:
    * Image viewer
    * Annotator
    * Video player
    * Music player
  * Handle relationships to other objects (of other types, etc)

Assuming that the mainstream trends currently are towards "all in a browser engine app" - this may not be the most efficient (energy, etc) wise way, but it'd work well.

I'm not sure if it's actually better to support generating IIIF manifest on the fly, based on whatever data comes with the objects, compared to IIIF actually on the long-term moving away from manifest to native object-speak. That might also be an interesting option.


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


## May include hashcode metadata field by default.

This should be a very basic feature.
Nothing that should need to be worried about anymore ever again.
It's just there.


## May contain duplicate entries for the same "name=value" pair.

On any level.
If you think about an XML or JSON dataset, hierarchies, tree structured values.
AHFX should allow duplicate entries with the same "name=", even if they're on the same "level" on a branch.



## May scale from personal use to professional and even large-scale cluster demands by design.

Having persistent metadata "tags" with any data, any file format, any application, any anything: from local harddrives, even USB-sticks and SD-cards, to network storages of all sizes and kinds - even super-clusters.

## May replace the "library" parts of any music/image/whatever management tool.

Music library handling players like: Clementine, WinAmp, VLC, iTunes, etc - all have one thing in common:
They scan the media files for metadata, which each application then stores it in their own (internal) database and data-layout, to provide search and sort functionalities.

Filenames may sometimes be considered as valid metadata source, and parsed "best effort" to guess at least the basic fields like "title", "artist" and maybe track-id or album name. Year or more is already a bonus.

But in practice, most well-assorted audio collections contain proper metadata, *embedded* in the file itself. This kind of "tagging" became most popular to the public with the popular MP3 format.

The actual reading/writing of these embedded metadata fields/tags actually require to "understand" any given file format that one may want to read or write this descriptive information.

This requires to know the specification of each format that one wants to support (they pile up over time), and this has to be done again and again for each new format or version or variant of a new (media) file format being released.

Now imagine all metadata (descriptive or technical) would actually be on the Object file system layer. The Object can be queried for all its metadata field as easily, and naturally as reading its filename or folder position before.

Then the actual difference between 2 audio formats would be most likely:

  * The encoding of the actual audio
  * Handling audio channels
  * Handling audio tracks

If you already think in AHA-Objects, then you can pretty much guess and already easily grasp how that would be easily be covered by "AHFX" (Working title for such a kind of filesystem standard):

  * Main Audio Object (Object):
    This is the one you'd "click on" or select if you'd like to handle "the whole recording" or session.
    It's probably a good idea to come up with some id- or naming-guideline or standards listing to make it clear if an object is an "entry" object.

    It contains at least "the usual/common" metadata fields. Which metadata fields/layout that is, may be provided by any Object-aware "data browser". Imagine to right-click it, and you'll get the familiar name=value mask for audio productions/recordings. Like that.

    It may contain references (relationships) to other Objects for:

    * each audio track
    * each audio channel
    * more metadata/relationships to describe the object.
    * anything else?

Depending on your "data browser" aka "AHA browser", you can select whether you see just "the audio file" (like you're used to) - or "the whole set, all channels, tracks, etc" - or "objects that are related in some (other) way". And you'd not only be able to see this like files in a folder in your choice of "file manager".

Yet, you're actually now able to manipulate and interact with the internals of what was previously (before AHA-Objects) some (mostly) binary file format which required you to know the specification, read hex and understand way too much about computing to even begin with.

So, before if you were lucky you saw this:

  * XBloome - X Marks the Spot - Planet Q.mp3

And now you see this:

  * XBloome - X Marks the Spot - Planet Q.mp3

Or this:

  * Planet Q [XBloome, X Marks the Spot] <mp3>
    * Track 1: [english, MP3]
      * Channel L [left]
      * Channel R [right]
    * Track 2: [albanian, PCM]
      * Channel L [mono]
      * Channel R [music]

Imagine seeing this in your default file manager of your choice.
And you could simply right-click-edit if you'd like to change any metadata field. Title, artist, language, album, year, link-to-band-website, youtube, etc.

And if you'd like to add or swap or re-order channels:
Just do so, by either drag-n-drop or changing relationships or references.

Regardless of which file or media format.
So the same for photos, videos, documents, anything. Even construction plans or automation G-codes. Anything can be depicted as Objects.



## May replace any application-internal database backend/layout.

## May replace the backend database for any digital asset management system.

## May store written text as single objects.

This may be crazy, but one could actually tag each word of a written text, generate an object for each word or phrase - and then re-create that text by generating a new Object that refers to these "word objects" in the right order.

Each word-Object would now be capable of not only receiving a referrable GPID, but also "machine readable" gets a complete new meaning. Because if a machine is able to use/understand this "hyper-AHA-structured text", these word-Objects could then be connected to any other digital data object (image, video, audio, document, etc).

In that way, any information depicted as Object can be referenced to a word-Object. The graphs which are dereby being created can then be used to "decode" any digital data like written text.

Example:

  * Here's a photo of a nice <Tardis>!
    And then you could do a simple search/replace each written-word, by any image file that has the tag "tardis" to it. There's your image search.

  * You could then apply this to the whole text, and you'd get a visual representation of the written text.


## May have collission-friendly Global PIDs.

> **Syntax: [🌟️]TIMESTAMP-LABEL[-RANDOM]**

Yes, the Star-Emoji is on purpose in the mandatory section of its implementation: To show (off) that unicode works flawlessly.

Other characters or emojis may be used, but I'd start with a common one. Keeping it simple.
This syntax may provide a surprisingly small number of id-collissions, even if an actual "global P2P storage pool" is considered. 

  * Syntax TIMESTAMP:
    `YYYY-MM-DDT133700-`
  * Precision of TIMESTAMP is arbitrary. Default is Year-to-seconds.
    More fuzzy, like "year-month-only" may be used to encourage collissions with other Objects created by other users. Because however chosen, the more users create "fuzzy" objects, the more you'll see a "single value"-cluster forming. Maybe there'll be thousands (or more) Objects out there in the future, titled "Hooverphonic [Artist]" - most likely meaning the same "Agent" - yet, all with fuzzy IDs chosen: They'll over time auto-sort themselves out.

    Because if someone references to "20??-Hooverphonic-Artist" Object-ID, they'll receive the list of other Objects already describing "The Artist Hooverphonic".

  * "-RANDOM" is optional.
    This is a random number.
    Its purpose is that in the unlikely event that another Object was created at the very same TIMESTAMP with an identical LABEL - another dice is thrown to use "noise" to avoid an ID collission.
    By default: encoded like a youtube identifier (Alphanumeric+CamelCase)
  * Length of RANDOM is arbitrary.
  * RANDOM may be generated either from real random numbers or pseudo or even random-seed.
    Choose wisely.

And yes: Every Object ID starts with a "🌟️".
    

## May be self-sorting (Collission-friendly IDs)

Yes. Imagine your data would "sort itself out". Like coding *with* physics - not against it. Not ignoring it.
CF-IDs in the AHA world are like this:

  * The TIMESTAMP precision is set to:
    * year
    * month
    * day
    * hour, minute, second, nanosecond

  * The label chosen to depict a assumably "common" term for the described object/entry.

  * RANDOM is better omitted if you assume that "your" intention for having that Object is shared by someone else.
    Without RANDOM, it's also clear (by naming convention/style) that the creator *intended* this object to "collide".

### Collission-handling

> "BORG it all out."

Meaning: Why not merge all metadata to a single, new object?
The new Object would It'd keep the "parent" ID, and continue with all "properties" (=metadata) from parent1 and parent2. Question is: How to merge the data payload (if there is one)?

Assuming that most collission-intended Objects will be metadata-only (aka "light" Objects)


## Security: Different "object spaces" - from private to public to anywhere.

There can be any number of "object spaces".
Think of it like chat-rooms or "contexts" or whatever.
Not all Object browsers can have all features implemented - but as with current computing, there are often "common basics" that one can assume to have as common or fallback option to interface with IT.

Oh, btw: Each object space is merely "yet another Object".

Because most configuration options for anything can now actually be stored with a Object. No more registry, no more config files.

And config files will dissolve into annotated and related objects anyways.


## Auto AIP by design

Imagine you already live in a fully immersed "AHA World":
You can tag and handle metadata with anything. It's so easy and plain and simple.

> AHA! It's even more apple than mac.
#FINDEMICH

Any recording device or software or tool may add its (technical or descriptive or elaborate) metadata next to the created file. The whole recording process (including project-files, takes, etc) is stored in related objects. There actually is no more such thing as "a project file format". A "project-file" is merely an entry-object that is related to all the stuff previously stored in a program-specific file/folder structure.o

Any application used to edit the file could leave a commit-message or remark.
Since the object IDs default syntax is designed as "collision-friendly globally persistent ID", any reference (if not manifested or resolved) could very well be found "somewhere" in a common object filesystem network.

Like the "AHA world".

This would also mean, that Linked Open Data is also built-in by design.
When copying to the long-term archival storage, you can simply select "a profile" - and all the references of your object(s) are resolved, and used to create the right archival package and enough environmental data (other packages/objects) until OAIS is checked with "yes" ;)

You can even go as crazy as fetching the embedded hardare configuration over SNMP and store that 1:1 as an object graph. Bi-directionally.



## May replace (necessity for) conventional config files.

How many config files does the average GNU/Linux command have?
None, one - and sometimes a folder or more. But usually (if), then *one*.

So why not put that config information right with the exectuable "file"?
(Since that "exec file" is now also an object, ready to hold metadata. Any.)

Right-click-whatever to view/edit/configure your program.


## May provide build-from-tar recipes (ArchLinux Style).

Imagine you find "a digital object" laying around on a USB stick.
Hm.
What do you do?

In my AHA world, I just double-click (or dot-slash) it.
What would happen?

I'm running my AHA stack on some future-alien-technology-hardware-3000.
Still running something that can run - or build GNU/Linux code.

Then the ArchLinux Pacman-style recipe information should be sufficient to make my host system download, install, build - then install again - whatever I need to work with "that data object".

And if something in the build-chain or environment is borken or missing, it should be rather trivial (compared to now) to deal with it: Even if the pacman and tarball code doesn't compile or work out of the box: This can be debugged.
And if one is lucky, there was also a link to a pre-built binary somewhere.
Why not? ;P

Anyways: This would seriously make data more fun to play and work with.



## May connect seamlessly with SNMP environments and tools.

SNMP is Simple Network Management Protocol.
It's been around for a long time, and it's still widely used and well supported for large scale networking and buildings monitoring, etc.

Some tools or ideas may be woven together with the SNMP world.


## May over time auto-convert your data collections into query-able graphs.

## May replace media container formats.

As already described for audio:
The AHA world may depict the information provided by current media file formats like Matroska (mkv), AVI, MOV, MXF, etc) - in a Object object graph.

Basic example:

  * MyMovie [title, artist, year, ...] <mkv>
    * Video stream 1
    * Audio stream 1
    * Audio stream 2
    * Subtitle stream 1
    * Timecode track 1

It's right there. This is not the output of MediaInfo anymore, this is the basic way you handle your daily computer needs. Working with "data objects".

It is very likely that by translating container formats to Object graphs, the following additional benefits may occur:

  * Each stream/content object will accumulate its own metadata over its creation and lifecycle.
  * The actual "differences" between features of different container formats will become common code, because most of it is now handled by the default AHFX layer.

This may very well apply to any other "complex" multi-data format.
If bandwidth is enough, or meta/data-filtering fast enough, one may even consider AHFX as plain network protocol.


## May replace common parts of workflow management systems.

AHFX can be used to depict any kind of workflow graph. By design.


## May dissolve programming code into filesystem objects.

Who would be so crazy to consider this?
Hm... WhatIf.

If you translate program code from "objects in text files" to "objects on the filesystem", even storing each function as separate object: What would this change?

Applying a doxygen-style render webpage as data browser plugin, one could not only browse through the code like through the HTML docs, but whatif one's also a creator and "hacks" the code? In the most amazing ways? :)

It would be interesting if that would have an effect on how code libraries usage and handling?
What if each source-code-function object now comes with its binary (executable) version?

Ignoring any possible performance or hardware-requirement doubts:
WhatIf each "code object" could be executed natively?
Because it was "described" and related well enough to provide the right data graph and payload.

When I consider IDEs: Integrated Development Environments for professional code manufacturing, I imagine it being a relief to see all the IDE-and-build-and-language-environment-specific-gazillion-detail-settings dissolve into configuration object-graphs. Then it's not a shame anymore to "not find the config option I know exists".



## "Mortal" Objects (optional):

For security or other reasons, one may define objects as "mortal" - so they de-manifest (=delete, erase, destroy, cancel, etc) itself after a certain time. It may even be possible to define graph-queries that allow ending an object under "certain conditions".

If performance allows this graph-query filter by default, the TTL handling could merely be 1 special case for such a default query.

Overview:

  * Set a Time-To-Live (TTL): manually or automatically (optional / depends)
  * For example: per object space, a preset profile defines for how long a (new) Object's TTL is.
  * or: to define a graph query under "which conditions" to terminate.



## manifest binary filetype "as needed" (just in time ;)

> "From graph to blob"

Imagine data file formats (eg. {PNG, TIFF, GIF, JPG, ...} or {AVI, MKV, MOV, MXF, ...} and any other format) are resolved into object graphs with a payload on your object filesystem.

By knowing the binary data structure of a given file format, that binary "blob" may be created on the fly with the information stored in the related object graphs that replace the eg "image file".

How to convert data object-structure to a binary stream may be done by defining graph-queries, combined with an XSLT-ish profile.

Such a conversion profile could then also be an object, making it easy to share "transformers" for different data formats.



## Resolve binary file formats: eg Image

For example, digital image information:

**Binary formats:**

  * BMP: metadata={width, height, bits-per-pixel, palette, compression mode, ...} + image data
  * PNG: metadata={width, height, bits-per-pixel, palette, compression mode, ...} + image data
  * TIFF: metadata={width, height, bits-per-pixel, palette, compression mode, EXIT tags, ...} + image data
  * ...

As can see, often different file formats intended for similar purposes, share similar (technical) properties - and therefore metadata fields. These formats seem very similar because here I didn't show the *exact* header and data layout in the file's actual bytes.

With binary formats it matters at exact which byte-offset a value is stored (eg width/height) - and one must know exactly how many bits/space that value may have (32bit, 64bit, signed/unsigned, etc) - or if it's (null-)terminated in some way or not. This is the reason why each file format, and each of its fields has to be individually supported by an application.

Yet, if it wouldn't matter at which "byte offset" eg width/height/etc are stored: 

It may be very likely that the actual differences between eg different image/audio/video/etc data formats may resolve into similar - if not identical - object-metadata, or relationship types.

Leaving mostly the actual "encoding" of the payload as the only difference.
If an application happens to have the proper "codec" for that payload - the previously format-specific header layout would be no issue anymore.

Here are 2 images stored as objects:

  * image1:
    * metadata= {width=320, height=200, bits-per-pixel=24, color=RGB}
    * payload= Uncompressed RGB 24bpp image data
    

  * image2:
    * metadata= {width=320, height=200, bits-per-pixel=24, color=RGB, **EXIF tags**}
    * payload= Uncompressed RGB 24bpp image data

You can see this information in the AHA world right now "right-click: view object" in your object browser.

The image1 *was* a PNG and the image2 *was* a TIFF.
Since in this case the image encoding (RGB24) is identical, the only difference is that image2 had "EXIF metadata tags" (because TIFF-specs allowed that). In the object filesystem, any tags can be attached and stored - so there's no more limitation to whether or not "a certain file format" could contain certain tags.

So any application opening "an image object", would probably care less about "what binary file format" it was, but more on "can I encode/decode the payload"?

Currently first the "payload" and technical metadata (width, height, etc) needs to be carved out from the binary (file) stream. This is not necessary with objects: Get the metadata fields you're interested in, then handle the payload.

What are now very different file formats in binary layout will become very similar (and therefore easier if not instantly supported) data formats. More complex formats may involve related objects (object graph).

Or "mature" data objects may include metadata like "a decoder": in any form.



## Access related objects identical to "local" meta/data.

  * from developer and user point of view:
    If I want to access/query "my_song.title" or "my_song.album.title", it doesn't matter if that information is stored directly as:

   object1:
    - title=My Song
    - album.title = The First Album

or as related object structure:

   object1:
    - title=My Song
    - album = object2

   object2:
    - title = The First Album

It may even be over-annotated:

   object1:
    - title = My Song
    - artist = Hooverphonic
    - artist = object43
    - album = The First Album
    - album = object2
    - album.title = The First Album

   object2:
    - title = The First Album
    - artist = Hooverphonic


## Add score to "name=value" pairs

To cover the following use-cases:

  * With multiple, identical "name=" entries, one can set a preferred "default".
  * Wrong metadata may be scored "badly" if desired.

The score/weight may be stored in a string syntax in the "name", to avoid an additional column on the basic "name=value" level.
Actually, one may even consider just a numeric "sort index" added to the "name".

Example:

  * title1.0 = default title.
  * title2.100000000 = probably bogus title.

Queries shall be possible in the following intentions:

  * Get default "title":
    `if (object.title == '...') and sortindex == 0 ...`
  * Quick-check if more than 1 "title" is set:
    `if exist (object.title2) ...`
  * Also check if there is more than 1 "title" set:
    `if count(title)>1 ...`

And so on.



--------------------------------

# Later features

## As plain network protocol

I'm thinking something like a replacement for the IP protocol. On that layer.
Or maybe one above: As network-filesystem protocol.
Or both.

Filesystem objects may be able to serve natively as network data objects.

Each object has its (unique?) identifier, and ObjectSpaces as (network) Realms.
So it has a handle, and could be accessed or copied to other Realms - local or remote.
Filtering/transition/conversion rules for moving Objects between ObjectSpaces may directly be used for firewalling, routing, etc.

Performance may be an issue (at first), but technically it may hold as network protocol.

It could be that some currently necessary features may become obsolete or replaced by more "object oriented" data-package thinking.

Any host on a network may be:

  * A filesystem Object, too.
  * An ObjectSpace realm.
  * Related to other "Objects" (=also hosts, and anything else stored as Data Object)

Any network-specific information could also be attached as plain name=value tags or linked as related objects to the transported objects. 

This involves any data that already *is* set and accessible on the Objects already: whatever is required for local acccess.

If a data object is accessed over the network, like a mounted CIFS/Samba share, any information currently required to function, could then be attached to the to-be-transferred Objects. And that metadata can then be interpreted/used to depict the same functionality as already existing.

This may be familiar to the reason why it's possible to resolve binary file formats into Object structures.
Network protocols were designed to allow wrapping "metadata" around a file payload - and preserving the filesystem properties (filename, folder) and have information to "send/receive it remotely".

It's metadata wrapped around "files".
That metadata *and* payload are now expected on the same level: the filesystem - and in detail: with each data Object.

What metadata would I need to send my Object1337 over a network to you?

  * Any metadata already with the Object.
  * Target/Destination: Some ObjectSpace Realm in a Storage pool of your host (Object).
  * How to get from my place to yours.


----------------------------------------


# Other things

## Initial embedded metadata migration 

### Metadata

For each file format to be supported, a simple decoder may run once on a given object data set, to extract all embedded metadata onto the object filesystem layer. 

Most metadata layouts, from name=value over XML, JSON, etc - the object filesystem keeps text-metadata. binary-safe. Always. So any "value" can be a hole metadata set or text dump.

Should work well for most common cases.


### Payload and file formats

Now the embedded metadata was copied to (new or existing) data objects, you can now see either with a library-view (like your music player) or like a graph. Even if a folder hierarchy, if you prefer that.

The AHFX allows to dissolve multi-data container formats into individual objects, referring to each other in a context.
So your initial conversion/copyy is leaving a relationship-graph with some "light" objects and "heavy" objects.

  * **light objects:**
    lightweight, mostly text-only, a few bytes to kB, possibly growing in the future.

  * **documents:**
    semi. Usually kilobytes, maybe megabytes - possible growing in the future.

  * **heavy objects:**
    That's what we now call "a large file". Like a high-res videofile or so. Or a holo-matrix.

That relationship graph is stored in data objects on the filesystem. You can view and interact with these "files" as you are used to. A main new feature is, that you can interact more directly with the relationships and metadata fields. It's all right-click-whatever. Or long-touch. :P


## Copy/Paste (and Profiles)

Whenever you'd like to copy/paste an object, the application you've chosen to interact with that object will handle copy/paste preference profiles.

They're quite cool.

And it's very important, that there are widely supported sane defaults for these profiles, and also regional or fun deviations easily possible.

When I copy my whatever collection to an external disk, I may be asked:
> "External drive: Which profile would you like to apply?"

And you can choose between something like:

  * My choices
  * Music collector
  * Private
  * Public
  * Professional EN15907 FIAF
  * <downloadlink>
  * <downloadlink>
  * <downloadlink>
  * <downloadlink>
  * etc.

btw: That "collection" I copied was the search result of a clever query I made. Showing up in a graph-y rendered IIIF browser. In my default data browser.
So I already could use my data browser for catalog use-cases.

It's probably sane to ask once; eg with checkbox with "don't ask me again, assume my default answer." - and only have the profile-choice pop-up on certain conditions - or when a certain key is held. Like "Ctrl+Whatever+DragnDrop" to trigger a certain profile (or a dialog window).



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




## Keep everything: How to handle all that meta/data?

Good question.

With the question of "garbage collection" I'm still not sure.
I don't think it's an either-or question.
I think it depends.

For starters, I must say I'm for "keep everything" and merge-equal and add-one more for "different" values.
If there's more than one field value option, prefer the "default" one. Marked as "me".

With more data being moved "into the cloud" for the sake of having it accessible:

  * On our own personal (private?) equipment: phone, tablet, PC, TV, whatever.
  * Online, so we can show off to our friends!
  * For work reasons.

The AHA World was designed to refer to any other data object. Regardless where it is. If your network allows you to "resolve" it, you're set. You can download or whatever it. Just like you do now with your "cloud" data.



## There is no "fixed position" of an object anymore.

The "most fix" part of the data is probably on which actual block-storage "block" your data actually "resides".
How persistent or long-term that storage is, is up to you. Even from HDD to RAM.

Filenames are just "yet another metadata" field: "filename=...".
Folder structure is merely a representation of a delimited-string, like "path=..." or interpreted from references to "folder objects".

The term "folder" may actually be better understood here as "groups" or "context".

However: All objects "just are".
Their bytes are stored in blocks on some physical "carrier" somewhere.
But on the object level of the filesystem, they are only referred to by identifier or context queries and filters.
You can think of them like "floating information bubbles": FIBs.

First maybe it's good to try how it "feels" to have more than one filename. Then "more than one" folder, title, etc. Embrace and Expand to the new featureset as convenient as you feel.

If you are in a hurry, because sorting out data is your job:
Great!

Any efforts trying to handle the "keep existing filenames/paths/identifiers?" may boil down to:

  * Can we merge the tags?
  * Can we keep existing XML-JSON-ish metadata files with "the objects it relates to"?



## Security performance: Relationship matters.

> Security by web-of-trust. Again.

Excellent.
For example:
When you "open" (=load) a movie from its archival "image-sequence plus extra files" folder copy, the performance is hindered by having to check access rights for each frame.

In the AHA-world, (local, default) security policies could use the relationship/lookup-hops like:

"If you are allowed to open this movie (meta-)object, than you're also of course free to access ... whatever's related in a certain way."

Not just recursion-depth, but real graph-data-queries (if performance allows, but things could probably be cached or pre-processed).

Such a design may have great positive impact on the performance of access.



## Security as an option. And a tag.

Imagine the linux multi-desktop metaphor, and think of them as "object spaces".
You can create as many object-spaces as you like (and your system can handle, of course).
Right click-new. "type=space; title=Home". Done.

There will probably be some sane defaults, well-supported conventions and of course proper standards. All living alongside each other.

Object spaces may be sub-spaces of other object spaces.
And of course, since they're AHA objects, they may be related to other Objects.

Now when you switch your "Linux-Object-Desktop" (Ctrl+Alt+Left/Right), you switch your object storage space working context:

In that "context" (=object space & its (transition) rules), can you access the "data objects" you'd like to work/interact with - or merely enjoy or share?

If you open your "data browser" (=like your beloved file manager), you can either access ("see" or read or edit) the objects you're looking for - or not.

If you want to access "out of space" objects in your pools (can be local as well as remote), rules like this may be applied automatically:

  * Objects marked "private" must never leave "private" space. Unless intentionally said so.
  * You may use any tags to quickly "mark" any object(-tree) or context: And query them for filtering.
  * You may add transition (eg transcoding) recipes and scripts (=other objects) to be executed when being accessed between object spaces.

Within one object-space: All things are equal. Just tagged differently.
But you may access anything, that's in the space you're in.

That's your level of security:
Feels more like the real world.
And you can shape it.

Local and network security administration is fun again!


## DSGVO: Tagged.

Object relationships or queries can be marked as "DSGVO-compliant or not".
Or like: "public / private. Done."

The data will simply not show up where it's not supposed to.
Because it got "filtered out" on the way all the time anyways.
Each object space may have its different graph-rulesets, and that is encouraged.

If there are any "disagreements" over anything, anyone is always free to "fork off".
In a friendly way. Hopefully.

Websites will merely be a web-frontend for a huge collection of stored, annotated objects.
In order to "leak" data, one would have to corrupt each individual host and application involved in accessing the sensible data.

If any application is told by filesystem-rules that "this object is not what you're looking for" - then it's simply dropped and discarded - and maybe (optionally) bit-shredded in memory.

Lawyered by tech-design.


## Security by keys. Public/Private.

It's about time, that this was resolved.
If anyone likes to, they can attach their gpg-public-key (and/or link) and signature and whatever to an object.

So anyone who edits/alters/creates an object, may leave their signature.
Add block-chain storage to this, and interesting things become easily possible.

Due to the "feelable" virtually-tangible object nature of this design, it may even be inviting to use "your private key" to access objects.
Good question is, how do you "provide" that key when needed?

I don't like the "obviously well-known" *eyeball-on-a-pen* entry-hack. At all.
Neither standalone-fingers to start your ... car.

However, integrating gpg and friends to support object storage, may be nice.
We can have group-keys.

Maybe get one automatically when joining any object-space?
One for each space. Meta-Spaces encouraged, of course.
No I don't mean the "FB-Meta".
I'm actually a bit annoyed that I can't use the word "meta" now anymore.
Especially these days.

Anyways:
Imagine you can simply wave your badge (as you do in-house), or type in a password - and decide how long this "login" will be valid, when you enter an object space.

This may also be used as auto-reminder if you remain in a digital space for "longer than intended or expected". Of course, inaction-timers can be set independently, etc.




## Content disagreements and conventions

Anything goes.
I'm just pretty sure we'll all (including you) will find it all way more fun and way less stress to simply adhere to some naming-conventions for starters.

dublin core to begin with.
Nothing new.

If there's more than one title for an object: keep both.
Since it doesn't matter anymore which application or system environment anyone is using to edit and enrich the(ir) data, it pays off to every now and then (especially in the beginning) to provide "better" (meta)data.

Since file-formats and container-formats may be resolved into filesystem objects, and it's easy to implement support for opening "graphs" by double-clicking or loading an "entry object".

Since any "name=" can be occuring [0..n] times (name1, name2, name3, ...), coexisting with different values, it's easily possible to have even "disagreeing" information.
And for the same reason, a digital signature could be stored like "name3=<sig>", and the user could decide (like https) if they "trust it".

Standards may be used to provide naming conventions, relationship and annotation rules, etc. Each object may now link easily contain links to xsd, xslt, etc.


## Metadata XML/JSON preproc-cache.

I imagine simple metadata-only objects, for example with a proper filled out set of DC-described (data) items.

With something like an XSD-for-AHA, and an AHA-to-XML/JSON API/libset, it should easily be possible to generate any pre-formatted, (standardlayout) metadata text format (as common now) by (eg Python) programming code.

Or even cooler:
By AHA-XSLTs. 

And that output is either stored as "preferred payload" at the main metadata object, or as a new object with a relationship back.

It's good practice to include either some README (or reference to one) or a preview/summary form of the contained "name=value" metadata. More "default or popular views" can be created as new objects, also each with a relationship to its "parent".

Since it now becomes very likely (over the lifespan of an object and "collection"), that someone has generated "a preview" data format, or classic text-metadata version: interoperability and performance should at least equal that of nowadays comparable setups and use-cases.

Maybe even faster, due to less wheel-reinventing-syssyphus overhead, due to "everything already being an object" filesystem-aware.


## Security: users and groups.

We could also move this to the filesystem level.
I mean with all data currently stored in LDAP-and-such domain systems, etc.
Dancing Samba.

There's probably a good reason why it hasn't happened yet, but I think it's worth asking what the network-share filesystem veterans have to chip in here.

I believe it should be possible to depict any current (and future) security related information in a meaningful way in the object storage world.

If combined with "object spaces" as rulebased-context, 


## May boost virtual reality.


## May be amazing for machine learning. Of any kind.



# Hardware support

There may be great potential in chips supporting indexing or other common functionality faster (or more energy efficient). Whatever works to speed up graph queries and computations may be useful here, too.
