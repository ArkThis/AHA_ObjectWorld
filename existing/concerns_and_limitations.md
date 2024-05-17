I've done some practical research and test-coding.

2024-05-18

I'm disappointed.
There is very strong limitation in:

  * how metadata is treated.
  * divided into separately-syntaxed kinds of metadata (tags vs metadata, vs system)
  * charset, length and number of metadata entries

Currently I fail to simply import a regular EXIF metadata extraction from an MP3 audio file.
The characters in there can't be "too toxic" for UTF-8 metadata fields?

Yet, I get a 400-something "bad request" error when I try to use that metadata in an `fput_object()` upload.


Something's strange:
All documentation, from advertisement, to small hacker-clips on youtube or professional howto or tutorial blogs, articles and also videos: They all say the following about Object Storages:

  * Object = Meta + Data, referenced by an Identifier
  * That this is a new paradigm beyond files-in-folders (and their names)
  * They support extensive user-metadata
  * Any kind of Data Object, from many small to many big.
  * Scales from single-disk to world-wide-spanning clusters.
  * By design knowing about the importance of meta+data, and the query-ability of meta - especially "tags".
  * Full UTF-8 support.

There's also the OSD standards:

https://en.wikipedia.org/wiki/Object_storage

> "An extensible set of attributes describe objects."

...which even seems to support "related objects" in Collections:

> OSD-2: "A collection is a special kind of object that contains the identifiers of other objects. There are operations to add and delete from collections, and there are operations to get or set attributes for all the objects in a collection."


So all documentation and tutorials and hands-on "reports" concur in the fact that "object is *not* files-in-folders".
Yet, I found this:

https://min.io/docs/minio/container/operations/checklists/thresholds.html

Which lists very reasonable and expected values for some properties, and then says:

> "Object Names in MinIO are restricted primarily by the local operating system and filesystem."

Now I can't have Objects that won't reside in a "files-in-folders" like structure - and their limitations - again?
Why?

Where's the Object-Spirit in that?
I get it that it replicates its data in a clever way. I don't get it, why metadata characters like "," won't work for tags - and exif basic key-value lists fail to pass "sanity checks".


# S3 limitations:

  * 10 tags. Seriously?
  * max length: 127 UTF or 256 if single-byte encoded.
  * metadata:
    * 4 or 8 kB per Object.
    * also (very) limited charset.

I hope those were arbitrary values, decided in 2006 (?), when they first released it - and that these values could either simply be increased, as long as the hardware supports it, and performance is "enough".

Further down the road, I'd really imagine boiling it all down to:

  * Store Objects "by ID" (and have the object storage deal with block-allocation and the layers below)
  * Be able to define rules/syntax for Object IDs
  * Any Object is a collection of "key=value" pairs
  * There is no distinction (necessary) between "meta and data" anymore, as conventionally was separated by "meta=small" and "data=big".
  * data (=payload) could be yet-another key-value pair, called "data" (or payload).
  * Bit-proof "what goes in, goes out" data-store for every key-value. All equal.
  * Full, seamless Unicode (beyond UTF-8) support as MUST.
  * Relationships support by handling any kind of "link" in a key-value field.
  * Sparql-ish (?) system to query the Data Objects - by default.
  * IIIF-compatible, or inspired browser as default "~~File~~ Data Objects Manager"
  * UIs web-engine based.
  * CLI tools proper
  * Proper libs


I do not yet understand why it seems necessary to have so many, individually-complex, components and layers are necessary, when "information found online" says that "An Object Storage is designed to do already *exactly that*"?

Of course, certain features require add-ons like "Parquet", or Redis to speed things up - however, plain-vanilla key-value meta+data "As Object" stored and referred to by an "Object ID" - which in my understanding *is NOT* something that looks like `/bucket/container/sub/sub/folder/name/looks_like_a_file_in_a_folder_to_me.jpg`

Where'd be the benefit of that?
I get the reason for making it backwards compatible to files-in-folders for interfacing and import, but how come that any "put" and "get" example I found refers to the "Object Name" as a file-in-a-folder string?

Okay, all buckets are replicated and available according to administration - probably from anywhere connected to "such a storage network". That's what makes it "easier" to scale than "mounted partitions". That's (still) the underlying disk layout?

On what layer does it do the erasure coding?
And how can it be that Object Storage are said to exist "because they're faster" than conventional storage - when they build *on top of* regular filesystems (still)?

Ceph seems to do it differently, but I'm not sure if Ceph seems too "grown over time", under rapidly changing outside world conditions and possibilities. This usually means, carrying a lot of legacy-burden in code-and-support, especially when doing commercial software development. The good thing is, that for that reason, Ceph may have the resources and experience to come up with something practically useful - and open.

I'm a bit tired that I now have to read up something new completely, as "OpenStack's Swift" sounds quite promising - again, according to docs and blogs, and articles, etc - even when it comes to Metadata - yet, their API docs mention s3 compatibility - therefore I wonder about their charset+size limits for meta/data?

Keeping fingers crossed, as the wording on Wikipedia (and the rest of the Web) clearly points in the direction that Object Storage and components for "Big Data" and Data Lakes, etc - are designed and used for managing mixed-structured data - in a commonly accessible pool of data/information.

This sounds exactly what we need for meta+data.
Actually, there should be companies one could contact to ask about exactly this.

Since this actually requires manpower and budget to setup - and deploy.
...and obviously also to research beyond theory.

