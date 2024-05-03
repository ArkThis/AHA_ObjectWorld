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

