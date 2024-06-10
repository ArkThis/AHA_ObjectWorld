# MinIO

Object Storage for Linux

https://min.io/docs/minio/linux/


# Remarks

## Tagging

  * A tag key must be unique.
    (202401)
    eg There cannot be 2 tags with the same key "tag" for example.
    When adding a new tag with a "colliding" key, the existing tag value will be updated (=overwritten).


https://blog.min.io/managing-objects-tagging-policies/


## Big Challenges in Small Objects

> This is a 1:1 copy/paste from: "[An Article on Min.io](https://blog.min.io/minio-optimizes-small-objects/)"

Working with large numbers of small objects instead of small numbers of large objects places different demands on an object storage system. Typically, storage administrators have had to design and tune storage systems based on anticipated usage and object size, for example adjusting properties for block, chunk or cache size to match typical read/write patterns.

In addition, small object workloads are more heavily affected by metadata I/O than are large object workloads. **MinIO alleviated much of this burden by removing the dependency on an external metadata database.** MinIO stores metadata and data directly on disk to provide greater performance and scalability.

--------

I want to use exactly *that* part of an Object Storage implementation.
I don't get it why they separate tags as "another kind" of metadata - instead of just another `x-amz-meta` data?

Anyways:
This sounds *pretty much exactly* what I'm looking for.
Where is the proper documentation?

Where is the explanation of "the in-your-face-public-but-coded sauce" like this?

```
mc mb play/mybucket
mc cp <path-to-archive>.tar play/mybucket --disable-multipart --attr "X-Amz-Meta-Snowball-Auto-Extract=true"
mc ls play/mybucket
```

Thanks for offering the copy/paste, but where's the docs about "disable-multipart" or "x-amz-meta-snowball"?
Could be an alien-defence mission on Kartoona 5 for all I know.
All that Object "big data" storage research is like being distracted by a bunch of hoax websites that try to lure you into a maze of "admin-nirvana". And in order to get there, you have to become "an employee" of the big ones - to gain access to "the real hardware and stuff" to actually run awesome computing - as it would fit the 21st century, imagined as utopian awesome society fiction!

But seriously: "amz-meta-snowball"?
Code-read anyone?
So this reads "Amazon-Facebook-Something" to me.
And it starts with "x-" and ends in a snowball.
Could be nerd-code "ascii-art in the mind" for all I know.

Anyways: I don't know where to find more information about this.
But I'd like to.


# Taken from documentation:

## Modern Datalake Reference Tech Stack

  * [MinIO Modern Data Lakes: Key Capabilities](https://youtu.be/skMqkix4RT4)

> This repo contains the configuration necessary to spin up a MinIO powered open-source and modern datalake. It can be used for training, experimentation, and hands-on demonstration. It is not production-grade.

[Github: MinioHQ - `datalake_ref_arch`](https://github.com/miniohq/datalake_ref_arch)

Data storage: Minio
File formats: [Apache Parquet](https://parquet.apache.org/docs/file-format/)
Table format: [Apache Iceberg](https://iceberg.apache.org/)
Catalog: [Project Nessie](https://projectnessie.org/)
Compute Engine: [Apache Spark](https://spark.apache.org/)

[Jupyter](https://jupyter.org/)
[Dremio](https://www.dremio.com/)


------------

> An Open-Source, High-Performance Analytical Database
> Fast, Fresh, and Flexible: Analytics With No Compromise

https://www.starrocks.io/



------------


https://www.youtube.com/watch?v=cI9zu5Rk_bQ&list=PL-gIUf9e9CCtGr_zYdWieJhiqBG_5qSPa




# Limitations

Here are notes regarding certain restrictions given by the current implementation(s).
Main focus is on the capabilities of S3 - and the stack(s) around and on top of it, used for data lakes.

## Amazon S3 tags

  * Reference: https://docs.aws.amazon.com/directoryservice/latest/devguide/API_Tag.html
  * Limited to 10 tags per Object
  * Must match this regex: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Quote Docs:


```
**Key**

    Required name of the tag. The string value can be Unicode characters and cannot be prefixed with "aws:". The string can contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-', ':', '@'(Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    Type: String

    Length Constraints: Minimum length of 1. Maximum length of 128.

    Pattern: ^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$

    Required: Yes

**Value**

    The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-', ':', '@' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

    Type: String

    Length Constraints: Minimum length of 0. Maximum length of 256.

    Pattern: ^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$

    Required: Yes
```



# Transforms with Object Lambda

https://min.io/docs/minio/linux/developers/transforms-with-object-lambda.html

Skimming over it, it reminds me of what I called "transformers". Active-code Objects that transform-on-the-fly, or may spawn new Objects: Copies in different encodings.

Metadata is already expected to be accumulated/merge-handled by default during the lifecycle of any Data Object.
Therefore, over time only the actual raw-data "encodings" will matter in comparison to what we now know as "different file formats" - and all related issues, efforts and solutions.


Quote:

    An Object Lambda handler is a small code module that transforms the contents of an object and returns the results. Like Amazon S3 Object Lambda functions, you trigger a MinIO Object Lambda handler function with a GET request from an application. The handler retrieves the requested object from MinIO, transforms it, and returns the modified data back to MinIO to send to the original application. The original object remains unchanged.

    Each handler is an independent process, and multiple handlers can transform the same data. This allows you to use the same object for different purposes without maintaining different versions of the original.




