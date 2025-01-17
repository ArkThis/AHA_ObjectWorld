---
title: Exposing extended attributes. Finally.
---

> **Executive summary:** 
> Using extended filesystem attributes as professional default for any digital
> collections saves billions of tax-money - almost immediately - and makes permanent savings
> due to eliminating common update/migration/interoperability issues = costs.

> **HR / Marketing**
> "It's cheaper, finally stable - and therefore fun again!"
> "Right-click-edit-metadata: on anything. anywhere" seriously.

> **Development / Sysops**
> Runs very well and is used on FOSS/GNU/Linux and MacOS.

Any code/time/effort put into supporting common filesystem features in tools/configs, we immediately connect to any other environment doing the same.

Nothing new.
Still really useful.


# What are "extended filesystem attributes"?

They are an old, and widely used, yet highly unknown - and IMO underrated -
**way to store almost any "key/value" information alongside *with* your files
and folders.**

  * Very simple. Highly effective.
  * 20 year stable standard.
  * Runs on Linux, MacOS, Windows
  * - and possibly IBM, Unix, Solaris - etc. machines.

Already "All-ready" :D

> Metadata handling on xattrs, works on any data and file-format. Identically. Consistently and Interoperable.


# In this article I would like to ask the question:

> "If xattrs are so awesome and solve the comuting world: How come, not even most IT people have heard of them, and they're nowhere to be seen?"

Even asking the ones who do know about xattrs (senior IT admins, thx to SE-linux) seem rather pointing away from it: don't trust them. they get lost easily. And no application supports it.

Which is understandable.
I want to address exactly that "myth" as possibly outdated.

The ice is thick enough.
It's safe to step on it and start dancing with meta+data on the filesystem - by design.


TODO:
Links to Linux,Mac,Win,Haiku and other xattr links


# Why "expose" them?

I'm working with Linux and servers and all things commandline and hardware since ~1991.
And I've discovered in 2024 (!) that I can use xattrs to store my MP3 tags for /any/ music file-format now.
The same way.

Wow.
It works quasi out-of-the-box, with a few config options to set to `xattrs=yes`, and you can right-click-edit-metadata on a GUI file-manager, on a file on ZFS on a Samba server, mounted on a local client. You can even copy to/from ext4: And the meta stays with the data.

Wow.
So simple, elegant, easy - and accessible.
And widely supported.

F2FS, a flash-filesystem supported by default on Android, supports xattrs too.

Imagine, you can simply copy your "metadata" as thin-copy from your existing files, and share that with friends, or simply publish online - as browseable - or even editable catalog.

Generic filesystem as data editing-and-exchange system.
This is meta+data interoperability by design. Not by format.
Format/Syntax/Structure/Naming of keys is identical to current form/standards UI interfaces and naming required.

Any application supporting metadata from xattrs, can be used on the any xattr-tagged-stack of data.

Therefore I believe many digital collection holders will profit greatly from using this stable standard.
That's why I'd like to expose the immediate benefits of using xattrs - and therefore spawn interesting and funding and support for improving the reliability and feature-set of extended filesystem attributes.

Making the basic filesystem the common "data-base".
A homebase for 99% of anyone's metadata "tagging" needs.


# How expose what?

Exposing the fact that using the filesystem as serious common-database, and funding proper support may overall reduce costs and maintenance significantly. Especially continuing meta/data/format/database migrations could become less necessary - as the need for updates regarding anything "metadata" handling should stabilize itself rather quickly, considering that most is "simply using a 20 year old stable standard".

So xattrs are nothing new, and they are ready and waiting to be taken seriously! :)
Finally.

Right-Click-Edit-Metadata on *anything* anywhere.

Thank you.


## Anywhere? Filesystems? OS?

  * OS: Operating System (Linux, Mac, Windows)
  * Filesystem: The "phone book" to access your data as files-in-folders.
  * Anywhere: Which OS/filesystem (FS)?
    Any POSIX-compliant FS since 2005 probably supports xattrs.
    Therefore even code/libs dating back to then.
  * That alone is already pretty well-and-widely supported computing environments.


# Outdated?

  * MacOS and Haiku proof that regular and basic use of xattrs works great in UI metaphors and data-handling.
  * I believe "the old ways" worked too well (for most) until now, and for big-data earlier (around 2001).
  * old ways = embedded metadata, overload-filename, sidecar metadata, external database, spreadsheet files, etc.
  * Around 1999, when xattrs were designed and used, there was way little memory (harddisk and RAM).
    XML as structured-text data format appeared around that time, too.
    And it was hard(ware-demanding) to handle strings instead of numbers/binary.

With today's memory sizes and prices, the gain in using more memory to support common key/value storage filesystems and tools - all plaintext and basic-types and URIs.

Since xattrs have only been neglected in the "user." tagging/annotation domain, or simple popularity and trust:
The system xattrs are heavily in use for serious high-grade data servers.
So they can be considered very reliable.
Military/Hospital grade I presume.

I've tested mass-de-embedding music metadata and it feels amazing!
Right-click-edit-metadata on anything, and browse a thin-copy like a catalog.
I would not know how to consider this outdated.

On the contrary:
This is exactly what anyone using data on computers actually can use right now.

What can we do about that?
Make proper support: tools, options, interfaces, plugins, etc.


# Make proper support

Any "complaint" or argument against xattrs in the last 20 years was always the same:
**Lack of proper support by more applications (or the one I want)**

Which is IMO a chicken-egg problem.

Now more and more base applications (rsync, tar, cp, etc) - the "All Stars" on the commandline - support xattrs.
And most filesystems in use also do.

If we stay within some key/value constraints - a common "baseline" - we can already go a long way.
Assuming UTF-8 support for values is given :)

Since most xattr filesystems store the values as bytes, Unicode will work.

If we simply start taking xattrs serious and engage in "supporting them", in applications we use.


# xattrs are literally (a bit) like filenames.

And right now, the world we're living in is before 1995: where filenames were
limited to 8 characters UPPERCASE-ONLY characters in ASCII (=no umlauts). No
spaces.
That was the best about it. The rest wasn't too great as you can imagine.

Being able to right-click-edit-annotate anything anywhere, like renaming a file or folder: For any kind of metadata.
Any file-format. Any application.

Like file- and path names:
  * Manage using a plain file-manager
  * And /any/ other tool/OS that handles that filesystem


# Are there any (size-)limits?

Depends.
Yes. Mostly. Unfortunately.
The magic number `4.0 KB` feels like ANSI/ASCII backwards compatibility-feeling regarding xattrs.
If you stay below that bytesize limit in total, you're (probably) safe.

In tests with XFS, I've written ~15 KiB of metadata (IPTC metadata standards reference image).
Without problems.


# Okay, so again "how"?

  * Setup a single-node "AHA storage" host (node).
  * Perform the following one-time actions:
    * de-embed all known key/value metadata:
      The file-format does NOT matter at this point anymore for accessing and editing metadata.
      The embedded metadata could even be removed from the original file, once
      the xattrs are considered trustworthy and well-usable enough.
    * copy that metadata as xattrs.
    * add additional metadata as desired (dublincore, IPTC, your-standard-here anyone?)
  * Pack that into an uncompressed plain "tar" file.
    * Try compressing that file to gz or bz2:
      Many standard applications support reading tar-data "life" even if compressed like that.
    * Or choose any other compression option:
      That file is a 1:1 replication of all previously-known metadata of your original data collection.


## Example 1: Music collection

I have used exiftool -j | json2xattr -p "user.exiftool." to de-embed the following music collection, found on a harddisk on a shelf:

> 14891 items, totalling 45.0 GiB (48,271,731,434 bytes)

It took a few minutes on an average HP ProBook G6 to do that.
**The resulting .tar.bz2 is 1.5 MiB.**

And the tar-file can be used as catalog query/search/annotate source.
Works already with any standard tools that support xattrs.
Especially awesome: Recoll (Thanks Jean-Francois).

Feels like a simple catalog application already.

----------------------------------

# Cool Tech Section

## How hard/difficult/easy is it?

### Bash (Linux)

`$ setfattr -n key -v value filesystem_object`

Where:

  * key : a string that identifies value.
  * value : a byte/string sequence up to `filesystem_specific_limits`
  * `filesystem_object`: file, folder, symlink, etc

That's it.
Metadata saved.

And to retrieve it:

`$ getfattr -d -m - filesystem_object`

You can even save (pipe) that output to a file, and import that again, using `setfattr --restore file`.


### MacOS / Windows

  * I believe there's an `xattr` command on mac. On Windows I don't know. But I've heard it's possible and works to save extended information on NTFS.
  * exFAT, and FAT can NOT do xattrs (AFAIK)


### Python

  * os.setxattr(), getxattr(), listxattr(), etc.
    In plain vanilla since 3.13.
  * Before 3.13: xattr external library.
  * `pyxattr` is discontinued in favor of `xattr`, as `xattr` is also tested to work on MacOS.


# Where's the catch?

There's probably a handful.
However, I believe technically that the benefits absolutely outweigh any initial obstacles.

What I may consider possible caveats:
(and what I have in mind for/about them)

  * performance:
    (Yet I'm still not sure which sweet-spot in hardware requirements an average-to-larger collection would have.
    How much metadata will fit into 32GB? And how much does more RAM cost these days?
    Even NVMe is blazingly fast - and affordably cheap. 1 TB = ~120 EUR.)
  * split-brain metadata (index-db/filesystem):
    (Fix be reseting index/cache.)
  * filtering keys/values:
    (Finding may require translation/mapping tables of key-to-key for consistent field addressing.)
  * security:
    (*sigh*)


