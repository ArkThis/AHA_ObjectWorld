# Transition from files-in-folders to Object Storage one-item-each.

2024-08-06

Short: Simply select, right-click, "Move to AHAolodeck".
And that file/folder on your storage will be replaced by a symlink.
Yet, now already "keyword" annotated by you, and auto-tagged with any information found "inside" the files.



# Scenario 1: "A nest of stuff"

You're in your file-manager of your choice.
Looking at some files (mixed formats, mixed size) in a folder of yours.

Some stuff you've had put together while working on some project.
Loads of subfolders.
File-naming from orderly to wild.
Some got hashcodes, some ain't.
Some was made by you, some by others, some downloaded.
And source-documentation, copyright handling...
Did you write down/link every URL, author, license, etc?

The usual "nest of stuff" on a computer.


# Scenario 2: "It's all in greatest order. Now mix-and-match with external"

You receive a "gift":
A great collection of whatever digital items (anything) on an external data carrier.
And you'd like to have it.
And you may have access - and a copy.

You usually have all your files-in-folders named neatly, properly and stored in a very clever folder structure, which you either came up with for your very own needs - or you adhere to someone else's "standard".
It works, and it's clean. Mostly. But you'll "ingest" those "folders" later somewhen.

So you've received more data from a friend, colleague, celebrity, etc.

And now you need to "transform" those Submission Information Packages somehow to be able to "save" it under your structural layout and capacities.

Well, and of course: Time's ticking. Hurry up!
We're just talking about naming and structure of files-in-folders to save it in your domain.

What do you do?


# Exposing extended file attributes (xattr) and Object Storage systems

Would you need to know "where" your "file" actually is stored?
Wouldn't it suffice to have enough "keywords" or references to find it?

And the data you `refer` to more often, gets shortcuts, mnemonics or even "meta Objects" that help you organize "index things" more easily.


What if such "index things" could simply be "yet another file on your storage?"

What if a "foldername", a 1-dimensional, textual structure - is not necessary to save-and-restore (=use) your digital stuff anymore?

This is exactly what "the Cloud" is currently doing.
Imagine, that functionality isn't a feature that's "cloud-and-network-only", but a basic feature of almost *any* filesystem: The component that handles your filenames and folder structures currently.

> Imagine you've got "**right-click-edit-metadata**" on any digital Object.

And you can already start with your files in folders.


# "Big Data" was heavy in 2003

The technology for that exists since around 2003, and is already widely and heavily in use in the "big data" industry. Mostly due to the fact that the current "UI" for any of those solutions are online or in-house web-services by (mostly very) big companies. Because "big data" used to be expensive.

The term "big data" was coined around 2003.
Things have changed since then:

  * Hardware performance has multiplied
  * Required computing hardware has become more affordable
  * And faster. Everything: Especially from HDD to NVMe
  * FOSS components sponsored and supported by big IT players (IBM, HP, ...)


# Take any files-in-folders real-world set of yours...

and select any, and as many - and whatever - you like:
file-formats, tiny, large, text, binary, folders, subfolders, anything!

select it visually, search & filter recursively: then mark all of them and:

> **Right Click Edit Metadata**


Select your preferred profile to "Upload to AHAlodeck!" - and "apply".


Then what next?

  * Add any keyword(s) in the textfield
  * or select from useful auto-suggestions
  * Add as much or little annotations and relationships as you feel like.
  * A single "aha, article, story" 
  * Select "[x] relocate to Object storage 
  * Select "Save"

Now your file is "gone" from your classical "folder", and relocated to AHAlodeck-compatible storage.
Of course you can have some kind of symbolic links in your classic view.
So, as easy as that, you can "let go" of your folder-structure and filename dependencies.

But how do you access/see/find those "files and folders" again?

That information was easily copied over as new key/value text metadata with your "Object".

See? It's all still there:

  * com.arkthis.aha.filename1=song8.mp3
  * com.arkthis.aha.path1=/home/user/awesome/poc/aha/code
  * com.dublincore.title=Some Title fetched from somewhere (embed, metadata files, etc)
  * ...
  * com.arkthis.aha.keywords=aha, article, story

It's like "aim-shoot-zap!" your current filesystem collections up into a new plane of existence:


# You upload them to the Object Storage matrix.

Any information/text you see in the key/value metadata: is automatically indexed for full-text search and facette filtering. Providing useful auto-suggestions as you type.
Doesn't matter if you read or write metadata now.

In all FOSS applications the file-handling dialogs can be patched to allow these "Object Browser" methods as option in the classic "File Open" use cases.


## How do the symbolic links work?

For backwards compatibility, many Object Storages can be mounted like virtual filesystems. By interpreting the file/foldername from a metadata field visually as a folder structure, and a "file with a name".

This is merely "one view" of Data Objects.
The one view, all of us worldwide are currently used to as "the only one view".

Therefore, at first, it's trivial to map that mounted Objects-as-Tree files/folders as placeholders onto the current, local filesystem.

Once all data has been moved to AHAlodeck compatible storage, and your daily-need applications have been patched to handle Objects by name/id, you can temporarily unmount the symlink disk - and use Object Data Pools directly.

Exactly the way you handle your stuff in online cloud web-UIs.
But now anywhere.

And now that you've moved all your stuff to AHAlodeck, and have been working uninterrupted on whatever you like so far: you are now ready to enjoy the next "Update".


# De-embed Metadata

If you want to have a well-annotated musical collection, you have certain file formats and metadata fields to use for that: title, artist, album, year, tracknumber, ...

And enough applications up and down, support those "popular fields" quite well.

And every single one of those applications needs to re-implement (or depend on code-libraries) for every single different audio file format.

And each one of them has very different field names, restrictions, etc.

Ever tried to annotate a WAV file?
Ever tried to read/write metadata in a BWF file?
It works for MP3 and MP4.

ffmpeg implements >70 audio formats alone. Only a fraction of them even capable of annotation.

Imagine to simply use `exiftool` to read all commonly known metadata key/values from almost any file-format in existence - and simply read your existing collection *once* and copy/paste those metadatas as key/value on to the filesystem.


## Then repeat with any other "embedded data"

The next step would be to copy/paste all values of a binary file header as well:

```
  width=720px
  height=576px
  encoding=...
  offset=0x13370
  payload=<BINDATA>
  ...
```

This is the equivalent of the transition from binary data formats in the 90s to XML: a big step from binary encoded, mostly numeric data to Unicode encoded strings in a heavy markup language, and huge structural-text overhead.

XML has its pros and cons, so does JSON, so does CSV.
But what they all have in common is, that they still are *the go-to choices* that somehow make actual interoperability in the digital world possible.

The step from files-in-folders to a new kind of storage that considers "meta+data" by design, is comparable to moving from "8.3 characters" naming limits from DOS to astonishing 250+ full 8-bit character sets - including spaces.

Now it's time to finally progress on:
Regain control over ones data, while at the same time resolving almost all "Datenablage" challenges every single computer using individual is dealing with - in one way or another.

And my proposal will make this accessible to anyone: Online or offline.


# Implementation goals during a 3y funded period

A Proof-of-Concept (PoC) prototype that provides the following functionalities accessible to anyone interested:

  * right-click-edit-metadata: on any filetype/folder.
  * find and select any file/folderset by: search query and filters
  * provide meaningful auto-suggestions after 3 characters input.
    (for searching and saving data)
  * right-click-move-to-ahalodeck
  * sane naming/standard suggestions for metadata layout and handling
  * web-engine based UI (for complex things)
  * Python based tools (CLI / UI) for handling key/value Data Objects


According to previous research, this may be accomplished using the following components:

  * A basic GNU/Linux distribution.
    Preferrably Debian based.
  * Ansi T-10 compatible Object Storage.
    OpenStack Swift?
    Minio?
  * metadata stored in POSIX extended file attributes
    * ext4, zfs, smbd, tar, rsync, hfs+, ...
  * index/cache: KeyDB, Redis, SolR, ElasticSearch, ...
  * A professionally supported big-data stack by Apache:
    * Iceberg: As database capable of schema-evolution
    * Spark: As database translation layer
    * Parquet: for data versioning
  * Python, BASH as programming languages



