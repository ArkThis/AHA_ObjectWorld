---
title: A Holodeck by August (AHA) - Introduction
author: |-
        Peter Bubestinger-Steindl \
geometry: a4paper, margin=2cm
toc: false
toc-depth: 2
linkcolor: blue

date: 2023-09-30
---


# AHA Object Filesystem: An Introduction to my "AHA Effect".

My "AHA Effect": It's actually very simple to make and it its components
actually already exist, and only need to be orchestrated to each other...

> **Keeping metadata as native and system-agnostic and simple and self-understood as file- and folder-names. In the filesystem.**

Therefore the slogan:
"Put your meta- where your data is. In the filesystem."

  * As Data-Objects.
  * On an Object-Filesystem.
  * Like MinIO or S3.

If it ain't at least as as simple and natively-interoperable as file-and-foldernames are now, it's not what I meant.

Imagine you can metadata-tag any form of digital data any way you like, even have relationships (links) between these "files" - and all that would be well-supported and stay with your data objects throughout their lifetime and workflows: What would that change?


# What would that change?

Simply having your meta-with-your-data on any regular filesystem. Taken for granted. Stable as hell.
Everyone using such a metadata-object-filesystem would benefit from incredible interoperability between applications, workflows and operating systems. Even mobile.

So, what would it change?

  * Interoperbility. By nature of its design.
  * Condense the number of different file formats
  * Normalize multimedia container formats.
  * Your filesystem would *become* your database.
  * Relationships as plain "Filesystem Objects".
  * Files and Folders.


## Interoperbility. By nature of its design.

This would at first, quickly and easily eleminate all boundaries and incompatiblities for metadata tags exchange between all supporting applications. Seriously.

Tag your photos and videos with any photo-sorting-app of your choice:
Copy-paste the files onto a USB-stick, SD-card or network drive or upload them anywhere.
All your "tags" - even relationships (links) described between your "stuff" will persist and is natively accessible (and edit-able) as simple and convenient as "just putting it" into the filename.


## Condense the number of different file formats

What's the difference between TIFF and PNG when storing RGB24?
The file-format binary structure and what metadata each format "supports".
Each metadata or structural feature a file-formats "supports", adds complexity
to "supporting" that feature throughout a file's lifecycle and workflows.

If any metadata (including relationships/links to other objects) is now
filesystem-standard, there is no more use for *embedding* any metadata, because
there is no more "file" as we know it:
It's a data object that can hold metadata and (binary) data payload (=bigger
than metadata).

Storing metadata in the filesystem, also resolves the need for embedded
metadata (zB EXIT of MP3 tags, and all others). It's very likely a single
extract-and-copy metadata from embedded onto the filesystem
process would probably suffice.

Whatever source metadata is bit-proof transferred onto the filesystem. Right
with its "data payload" (what we think of as "the file data"):
Your image, your song, your construction plan, your text or spreadsheet.  
Anything.

That would thereby reduce the number of different file formats (if their
differences were metadata options).

Moving also the other technical header fields to that AHA object filesystem, would leave only the encoded data playload as "Binary Large OBject" (a "BLOB"). This would make even binary formats easier to be "understood". The actual data-encoding will be wrapped in human-and-machine-well-readable metadata and links.

Anything except the "(binary) encoded" data payload, "the rest" is stored as clear text (think JSON and UTF-8, yet bit-proof), natively on the file system level as metadata. Very convenient and easy. Both to use and to develop for.

That would change quite a bit, don't you think?


## Normalize multimedia container formats.

> **Down to the filesystem level.**

I will keep repeating that a lot, because that's why it's so simple.
Simply letting go of the "old" files/folders paradigm and thinking, by enabling
21st century "Sysadmin's Digest" on the filesystem level.

Resolving media container formats into related data objects.
So AVI, MOV, MKV, MXF, etc - will become mere filesystem graphs of related
objects.

It would also "resolve" any use-case for "remultiplexing" or "demultiplexing"
(remuxing, demuxing): There's an entry-object with "links" (relationships) to
their audio and video and subtitle and timecode and etc - "tracks" (more
objects).
And the container metadata goes: **Down to the filesystem level.**

The "track" objects being the current bitstreams that were stored *embedded* in
the original media container file (format).

Existing videos may also "simply" be imported into an object-filesystem:
transformed into object-graphs with an "entry object" (to double-click and open)
and displayed backwards-compatible, sorted by their most recent
file/folder-structure.

And film archivists may also love this:
A usual film "AIP" (Archival Information Package) - the digital "reels" archived
for eternity, consisting of thousands of individual files (=frames). Image and
audio and metadata, and subfolders, and whatnot.

This would now receive also an "entry object" to click/open: Depicting the
original structure of the digital "film" as object-graph. Like a videofile.

Simply add a new audio language, by drag-and-dropping a new audio track onto an
existing film or video "entry object". Done.
No more "ffmpeg -c copy". Sad almost.


## Your filesystem would *become* your database.

It would be accomplished by allow storing "metadata-only" objects on the
fs-level, too. Just like that. Even `right-click: New Object`. Then
`right-click:Edit.Save.`
Voila.

Sounds user-friendly?
It is. And also for developers.

Meaning: 
**Your filesystem will then *be* your catalog. Your database. Your asset storage system.**

And any application dealing with your data will merely be a helper or assistang to work with your "digital objects". In a good way.

This is done by using the filesystem for metadata demands:
putting database, tables and cataloging on the filesystem-level, too. Native and interoperable between applications, because they all access "the default metadata system".

All your descriptive and technical metadata will be easily accessible, editable and also seamlessly travels along networks, storages and systems.

Like file-names. But better.

So all catalog and asset management systems would become plain "interactive filesystem browsers - or object handling assistants".

Possibly fully data-compatible, by filesystem-design.

This may be a huge paradigm change how we interact with our "digital objects"...


## Relationships as plain "Filesystem Objects".

So you can now "tag" any file you have however you want - with any application supporting object-filesystems-metadata. You can also relate one object to another like "this track (object1) is part of this album (object2)" or "this image (object1) is a scan from the cover (object2) of this record (object3+)).

Simply by either drag-and-dropping these objects onto each other and editing their metadata fields.
Your filesystem will become a semantic graph-database to query at your liking. Locally, on a USB-stick as well as remotely over a network.

When you copy "objects" to another destination, you may choose how many relationships to include (hops).


## Files and Folders.

For starters:

Do you know this case, where you have "a bunch of files/folders" that should be "sorted" into their "correct" (or at least sorted somehow) data-nests? Oh, let's just copy all of it as-is onto the new, bigger storage and do it later.
Those dreading "Unsorted" or "to-sort" folders lurking around on all our digital drives?

> "I know I had that file/copy somewhere..."

Imagine, this case would just never ever happen again - and oh, btw: Your "unsorted" data-nests would over time automagically sort themselves out to be "search-and-retrievable"?
"Automagically" in this case, meaning: By importing these "data-nests" into an Object-storage, and a crawler extracts whatever "metadata" it usually harvests from incoming "legacy data" and copies those findings as metadata onto the filesystem entries of these "data-nest objects".

You can now just search and use them from your object-explorer.
It doesn't matter anymore "where they are" or "what their filename is".

**Files and Folders just become "yet another metadata tag":**

  * There are no more "illegal" or "toxic" characters in a file/foldername.
  * An Object can have more than 1 file/foldername. ;)
  * Some folder structures resolve into a relationship-graph.
  * You can view your Objects as-if they were filenames in folders.
  * And you can also sort them (even graphically) by complex (and even semantic)
    search queries.
  * "As in the cloud as on your USB-stick. Amen."
  * Unicode and bit-proof.

Fully downwards-compatible to mapping your Object Storage Filesystem to being
accessed and viewed like a conventional file/folder structure. And adding the
new features like a cherry and ice-cream on top.

Objects need disk- and memory-space.
Their structure is now self-defined by tagging them along over their lifetime.
Across applications, systems, workflows and final storages and later use-cases.

By transforming from a hierarchical filesystem to a "self-structured"
(=self-describing) bunch of digital objects floating around on any kind of
binary storage type. Any.

Files and folders have served us well, and I love to have them still in the real
world. However, there is a need for a change in how "we" (who want or have to
use any kind of digital computing system) interact with our data.

These meta/data gaps, introduced by the lack of metadata support on the
filesystem-level, is merely a leftover of the physical world. Introduced by the
file/folder UX paradigm.

Now we have enough diskspace(s) and processing and caching options to solve this
to a new - and actually lower - level.

> **Down to the filesystem level.**



# It's been a long way, but: Enough.

A short ~~history~~ story:

AFAIK.

The hierarchical filesystem "paradigm" in computing was an excellent way of doing things with the technological means they've "booted" from in the 70s/80s. We came from 8.3 (14 characters max) per file/foldername to "i don't how how long, exactly, maybe 255+ - but at least you can almost write an abstract into it-long filenames. For PC users with the introduction of Windows95.

Wow.

There probably were unix-like or other systems that supported longer filenames already before that, but mainstream got it with Win95.
A big paradigm change in computing. Everyone noticed, everyone "used" or developed it at some point.

File and Folders have had their time, and computing has evolved since then.
There is no more need to save on individual bits on the filesystem level, or because we're short on diskspace.

Metadata (any kind), compared to audiovisual or other heavy payload data that we are dealing with, even on our "small and handheld, mobile devices" with ease (almost).

This breakthrough was introduced by "lossy compression". That's why "JPG" and "MP3" were suddenly so damn small, compared to TIFF and WAV.
A big paradigm change in computing. Everyone noticed, everyone "used" or developed it at some point.

Files and Folders made us "locate" a file, by giving it a "name" and a "place". Considering that all this information must absolutely reliably be kept in the filesystem. With as little diskspace- and computing-overhead as reasonably possible.

Excellent job done.
So many awesome filesystems in use today.
And except for a few encoding f-ups now and then, files-and-folders travel well.
Files-and-folders seem to be one of the few very basic, absolutely common
denomiator when it comes to computing systems.

From the 70s to current mobile OSs and other embedded systems.


## Now for some reason, there's still a huuuuuge gap between "metadata".

How come?
There's literally millions (also tax-payer's money) of euros invested regularly
into improving metadata handling. I know it personally from the GLAM sector.
Great work being done.

Yet, when there's "collection import/export" or setting up a new CMS/MAM/DAM,
faces turn pale, and expectations go *uurrrrgh*. Hard.
Or: "Hey that was easy! Puh. I hope I have chosen the right tool. I'll be stuck
with it for a long time now."

A ton of different "cataloging" or "asset management systems". Awesome. Great. Really helpful and powerful!
Yet, always a great and binding commitment.
Even for personal use.
Which "app" do I use to tag my photos?

Can I copy my "collection" (or parts of it) over to a friend?
Including my metadata "tags"?

Depends.
On the following options with:

  * Migrating databases
  * Import/Export of metadata.
  * File storage access and migration.
  * And that system's (internal) (meta)data layout.

What if "Digital Asset Management" (DAM) vendors would support using the filesystem as their main database? For performance, several caches and indexers will definitely be used. That is the regular case for such a future filesystem, anyways.

Any enhancement of the "data quality" by using these asset management systems, would in the end store the outcome as tags on the filesystem. And merely cache-and-index your data for performance. Any other DAM or application can at all times access all that information equally.

Including pure cataloging and relationship data.
Because they're now "just objects on the filesystem".
You can even look at them like "files" in your browser, if you like.

They're not hidden.
Your "object focus" is not very unlikely to look for them.
Unless you want to.


## Meta/Data Gap closed.

An "Object" can have any number of metadata, and a (binary) data payload (the
stuff larger than metadata). A simple structure.
If you'd "like to know more" about what you see as a "file" in your new Object
Browser: Simply right-click it.

Or Shift-double-click. Whatever. Assign your favorite shortcut.

There is no more difference between a metadata Object and a (larger) data
Object.

The only questions left now are:

  * Do you have enough diskspace/memory?
  * Do you have sufficient access (rights)?
  * Is a related Object local, nearline or online - or even archived?
  * Is a related Object accessible?
  * Is a related Object encoding "decode-able"?

But DublinCore is now officially "supported anywhere by default".


# Final worlds

So: Anyone dealing and creating (with) digital objects would profit from having this kind of metdata-handling on filesystem level.

From end-users to developers.


think about it... :)
