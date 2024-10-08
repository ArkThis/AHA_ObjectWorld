# Some thoughts about S3 "Object Names" 

First of all: 
It's actually a great (hack) idea to suggest a default "Object ID" syntax that resembles a "files-in-folders" paradigm.

And therefore supporting importing existing data, by simply mimicing (copying) it's "path + filename", and prepending a "bucket" (like a drive-letter or mountpoint).


## Great, but now it starts to get confusing.

An Object has no path, and not necessarily a filename, or extension at all.
This is what's new and different about Object Storage systems (as I understood them, and seems to be defined in ANSI T10), compared to the classic "files-in-folders" way of thinking.

So Amazon mentions this in [their official documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html):

> "Amazon S3 supports buckets and objects, and there is no hierarchy. However,
> by using prefixes and delimiters in an object key name, the Amazon S3 console
> and the AWS SDKs can infer hierarchy and introduce the concept of folders."

This also makes it possible to "mount" S3 storages as a folder in a classic filesystem.


## Great, but now it's time to let go.

It's time to let go of files-in-folders - and all it's syntax/structure and character-set limitations.

But how?
The imaginary concept of data residing as "a file in a folder" has been with all of us who work with computers since like forever. It's hard to imagine data differently. How to "let go" of this concept?

> Let go of the handlebars, and ... remove the side-wheels?

Actually, the information currently chosen as file/foldernames/structure actually belongs in key=value metadata fields /of/ your data Objects.

**Actually, why not simply have: Right-Click-Edit-Metadata?**

On *any* file/data format. Anywhere. Any tool, anything: accessing the same common thing: "A Data Object"
With useful basic filesystem functionalities.

And Meta+Data simply stay together. Identified by it's "Object ID".
(My suggestion is a CFID (Collision Friendly ID), with a proper UI to make it even more useful. :D)


## What's wrong with folder+filename as an "Object ID"?

For now, coming from a files-in-folders structure of data, using Object Names like that makes sense.

I'm worried though what happens when these "Objects" now are copied, travelling - and referred to from many, possibly very different contexts?

Won't these "old path and filenames" become confusing one day?
Or will this legacy-source speaking-metadata information merely be "just an ID"?

However, most Tutorials and Example-Code for S3 compatible APIs (I read mostly Python) even talk about paths and delimiters, and folders.

[That very official documentation from Amazon on 'Object Keys'](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html), I mentioned above does exactly that. It describes files-in-folders on S3.

Only below, it is noted that "there is no hierarchy" and this Object ID - namely "Object Key Name" (`object_name`, later in code) - is hardly seen with "a more regular" ID.


Yet, right afterwards, a 2nd note says:

> "The Amazon S3 console implements folder object creation by creating a zero-byte object with the folder prefix and delimiter value as the key. These folder objects don't appear in the console. Otherwise they behave like any other objects and can be viewed and manipulated through the REST API, AWS CLI, and AWS SDKs."

So back to files-in-folders-thinking.

Why?

Also, why does min.io have a charset limitation below UTF-8? Why?
In some online docs, they mention it's due to filesystem-filename backwards-compatibility. Varying between OS and filesystems minio stores the Objects on.

Alright.
The "Object ID" is again a technical handle.

Okay, but then why can't I find any default/official/popular/common suggestion/role models/examples/documentation to suggest proper metadata field (key names) to hold the structural/tagging information that now all we had was file/folder naming to put it into?

**Why is there no example code or tutorials showing exactly that?**


## Great, but now it's even more confusing.

These Data Objects are said to hold meta+data, and be accessible by an Open ID - namely "Object Key Name". 

And again, the abovementioned docs even list which characters are "safe, okay, possibly special, to-avoid". None of them seem forbidden (I presume also not by code). This would suggest I may use any character/string-sequence of my choice as Object Name?

**Why is there no example code or tutorials showing exactly that?**

So one should assume "the default/proper/state-of-the-art" way of structuring an Object Storage is with "thinking in files-in-folders-in-buckets". Okay for world-wide high-availability replication and failover.

However, every other article highlights "Object Storage for large, unstructured data processing and storage" - yet, I cannot find online material showing such use-cases, or metadata-handling in general.

Nothing beyond a few "foo=bar" tagging examples is all for "Object Storage Metadata features".

And it seems even basic ASCII chars like "," or ";" seem "illegal" on minio (and possibly other S3-compatible implementations?)


# Object Store implementations older than S3 seem superior in handling "meta"

  * Ceph has [xattr and omaps](https://medium.com/opsops/rados-objects-omaps-and-xattrs-32e66d2b528b)
  * OpenStack Swift nicely handles UTF-8 and binary-safe values for Objects (as xattrs, too?)
  * others?


# I'm looking for a *real* key/value/blob store.

And the ANSI T-10 "Object Storage" standard seems to declare just that.
Yet, that's only a paper.
Not an actual implementation.

For comparison:
Redis/KeyDB is cool with everything, but it ain't a persistent large-volume Object Store. It's a Cache DB.

I would hope for some real-world daily metadata-handling example code.
Like I wrote a Python that would extract, and copy/paste EXIF metadata from an MP3 file (and any other format known to exiftool) to a key=value Object - in Redis.

I've created an ObjectID to my liking (CFID), and then added the actual "file" data as "payload=<DATA/>" pair to the other "metadata". **Now meta+data are equal. Just different in size and encoding.**

Now I know it is possible to store data like that - and eg Redis or KeyDB shall prove how to dynamically work with such a storage set.
