# Object Storage(s): S3 compatibility as issue - rather than feature.

I may be completely wrong on this one.

I am so new to running and using Object Storages - and most of my assumptions
are based on what I could find in online material, such as official
documentation, articles, papers, tutorials (html and video) - as well as online
blogs by the manufacturers of "professionally used" IT stack components.  I've
listed my sources below.

> Certain Amazon AWS S3 design "limitations" may merely be due to satisfying
> *their* business concept of storage-rental, rather than for technical
> reasons.  All existing "S3-compatible" Object Storage implementations (even
> FOSS) may therefore be unnecessarily limited in metadata handling, usage and
> access.

For example: S3 (a) only allows 10 tags (128 length) in S3, but allows 50 tags
in their other enterprise product model (AFAIU). And it (b) distinguishes
between metadata and tags. For performance reasons, I presume.

> Additionally, the concept of "files-in-folders" is kept as "object name"
> being the main access identifier instead of a syntactically and semantically
> decoupled Object ID?

Therefore, I currently question if "S3 compatibility" is actually a feature,
when trying to unleash the full potential of this new data storage paradigm, or
actually a set of artificial restrictions, I've currently put on my "CONS" list
for choosing between different implementations.

The official documentation Minio Python API example code, Objects are always
referred to by their "bucket/path/filename.suffix" conventional, well-known
"string".  The main advantage in that "usage mode" where the
"bucket/path/filename" is used as main identifier, is that it's 1:1 compatible
with existing data layouts and naming.

Unfortunately, either S3 (or minio) has put the restriction to stay
"filesystem-safe" in code, therefore only supporting a limited
"filename-and-folder-safe" option in that "string".

I'm surprised by these IMO obviously ludicrous and oddly "low" numbers of tags,
and limited bysize and length and charset of user-based Object Metadata. And
I'm even more surprised that I seem to be the only one who doesn't understand
how to use "the new Object metaphor" properly - and I don't seem to find
metadata-handling code publicly.


I therefore propose my question:

> Could it be that a plain key-value Object Storage could actually be very
> simple to implement, built on the already existing very-scalable and
> production-stable implementations of Swift, Minio, Ozone, etc - merely
> patching their value-limits in code to "key=value" with "as much size/length
> as your storage can allocate - and also as many - and make it bit-proof, and
> meta-only: therefore *no* restrictions whatsoever in the bytes allowed as
> both key and/or value?

Redis on flash - but not limited to flash.  Just something like "Redis as
Storage" from SD to cluster.

Why not?  That would pretty much already *be* the first AHAlodeck engine.

**Please challenge existing or future S3 implementations/support for their
`technical` or practical necessity - and patch your code accordingly to make it
more awesome, if possible.**



Thank you.


## My online research consulted sources, such as:

* Apache Hadoop, Ozone, Iceberg, ... Parquet?
* OpenStack Swift
* "Oasis" T10 ANSI key-value Object Store implementation
* Min.io
* Redis
* NoSQL MongoDB
* etc.

There's even HowTo videos and web-documentation by major companies, such as
IBM, Microsoft, Google, etc - that confirm my following perception of "What is
an Object Storage" - and what is it designed and used for:

  * Store a very large number of objects.
  * Go beyond `filenames in folders` as access paradigm.
  * Store metadata *with* (payload) data as "an Object".

Especially in comparison and difference to /conventional/ files-in-folders
storage concepts and other /classic/ paradigms. Because would the "large(r)
number of files per folder" as only reason suffice to go through all the
efforts of implementing, advertising and maintaining "a new storage paradigm"?

