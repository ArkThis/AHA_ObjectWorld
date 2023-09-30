# AHA Object Filesystem: An Introduction.

2023-09-30

It's actually very simply and it its components actually already exist, and
only need to be orchestrated to each other...

> **Keeping metadata as native and system-agnostic and simple and self-understood as file- and folder-names. In the filesystem.**

Therefore the slogan:
"Put your meta- where your data is. In the filesystem."

  * As Data-Objects.
  * On an Object-Filesystem.
  * Like MinIO or S3.

If it ain't at least as as simple and natively-interoperable as file-and-foldernames are now, it's not what I meant.

Imagine you can metadata-tag any form of digital data any way you like, even have relationships (links) between these "files" - and all that would be well-supported and stay with your data objects throughout their lifetime and workflows: What would that change?


# What would that change?

This would at first, quickly and easily eleminate all boundaries and incompatiblities for metadata tags exchange between all supporting applications. Seriously.

Then resolve the need for embedded metadata (zB EXIT of MP3 tags, and all others).
Very likely a single extract-and-copy metadata from embedded onto the filesystem process would suffice.
Bit-proof.

That would thereby reduce the number of different file formats (if their differences were metadata options).

Moving also the other technical header fields to that AHA object filesystem, would leave only the encoded data playload as "Binary Large OBject" (a "BLOB"). This would make even binary formats easier to be "understood".

The rest is stored as clear text (think JSON and UTF-8, yet bit-proof), natively on the file system level as metadata. Very convenient and easy. Both to use and to develop for.


# It would allow storing "metadata-only" objects on the fs-level, too.

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


# Relationships as plain "Filesystem Objects".

So you can now "tag" any file you have however you want - with any application supporting object-filesystems-metadata. You can also relate one object to another like "this track (object1) is part of this album (object2)" or "this image (object1) is a scan from the cover (object2) of this record (object3+)).

Simply by either drag-and-dropping these objects onto each other and editing their metadata fields.
Your filesystem will become a semantic graph-database to query at your liking. Locally, on a USB-stick as well as remotely over a network.

When you copy "objects" to another destination, you may choose how many relationships to include (hops).



# Files and Folders.

For starters:
Do you know this case, where you have "a bunch of files/folders" that should be "sorted" into their "correct" (or at least sorted somehow) data-nests? Oh, let's just copy all of it as-is onto the new, bigger storage and do it later.
Those dreading "Unsorted" or "to-sort" folders lurking around on all our digital drives?

Imagine, this case would just never ever happen again - and oh, btw: Your "unsorted" data-nests would over time automagically sort themselves out to be "search-and-retrievable"?
Automagically in this case, meaning: By importing these "data-nests" into an Object-storage, and a crawler extracts whatever "metadata" it usually harvests from incoming "legacy data" and copies those findings as metadata onto the filesystem entries of these "data-nest objects".

You can now just search and use them from your object-explorer.
It doesn't matter anymore "where they are" or "what their filename is".

Files and Folders just become "yet another metadata tag".


# It's been a long way, but: Enough.

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
So many awesome filesystems.

Now for some reason, there's still a huuuuuge gap between "metadata".
How come?

A ton of different "cataloging" or "asset management systems". Awesome. Great. Really helpful and powerful!
Yet, always a great and binding commitment.

Why?

Migrating databases. Import/Export of metadata. File storage access and migration.
And (meta)data layout.

What if "Digital Asset Management" (DAM) vendors would support using the filesystem as their main database? For performance, several caches and indexers will definitely be used. That is the regular case for such a filesystem, anyways.

Any enhancement of the "data quality" by using these asset management systems, would in the end store the outcome as tags on the filesystem. And merely cache-and-index your data for performance. Any other DAM or application can at all times access all that information equally.

Including pure cataloging and relationship data.
Because they're now "just objects on the filesystem".
You can even look at them like "files" in your browser, if you like.

They're not hidden.
Your "object focus" is not very unlikely to look for them.
Unless you want to.

So: Anyone dealing and creating (with) digital objects would profit from this metdata-handling on filesystem level.

From end-users to developers.


think about it...
