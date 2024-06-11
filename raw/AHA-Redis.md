Due to the current limitations of S3 regarding metadata size and handing, I'm considering to use Redis for most of the meta - and even smaller data, such as images - or anything below a certain bytesize (MB?) threshold.

If we can store 98% of our "files" and definitely all of their ever-existing metadata - and only need minio as large-object backend, that doesn't feel too bad.

Especially considering that it is extremely easy to setup.


However, I do not like the idea of having meta+data separate again.
On the long run, they must be handled together. always. as "Full Objects: meta AND data".

However, the next step is to build a proof-of-concept for these:

  * As files-in-folders mountable storage:
    for import and seamingless migration from files to objects.
  * de-embed metadata:
    simple copy/paste exiftool output as key=value pairs, linked to an object ID.
  * query metadata:
    This should be where redis is supposed to be made for.



# Redis

Redis as installed as easy as "apt install redis" (on xubuntu 20.04)ô

```
How is Redis different from other key-value stores?

    Redis has a different evolution path in the key-value DBs where values can contain more complex data types, with atomic operations defined on those data types. Redis data types are closely related to fundamental data structures and are exposed to the programmer as such, without additional abstraction layers.

    Redis is an in-memory but persistent on disk database, so it represents a different trade off where very high write and read speed is achieved with the limitation of data sets that can't be larger than memory. Another advantage of in-memory databases is that the memory representation of complex data structures is much simpler to manipulate compared to the same data structures on disk, so Redis can do a lot with little internal complexity. At the same time the two on-disk storage formats (RDB and AOF) don't need to be suitable for random access, so they are compact and always generated in an append-only fashion (Even the AOF log rotation is an append-only operation, since the new version is generated from the copy of data in memory). However this design also involves different challenges compared to traditional on-disk stores. Being the main data representation on memory, Redis operations must be carefully handled to make sure there is always an updated version of the data set on disk.
```

https://redis.io/docs/latest/develop/get-started/faq/



# KeyDB:

[https://docs.keydb.dev/]()

> "KeyDB is a fully open source database, backed by Snap, and a faster drop in alternative to Redis"

This may be a useful alternative to Redis, as it provides persistent Flash support (instead of RAM-only).


