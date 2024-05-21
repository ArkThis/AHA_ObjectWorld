Possibly related, existing projects/things:


# "Real" Object Storages

Preferrably conforming to OSD (2, 3?), as according to [Object Storage on Wikipedia](https://en.wikipedia.org/wiki/Object_storage), this sounds more what I'm loooking for that what S3 (and therefore Minio) seems to provide.


## Ceph

I don't have a good feeling about this.


## SwiftStack

https://platform.swiftstack.com/docs/introduction/openstack_swift.html

Feels better.

Quote:

The most commonly used storage systems in the enterprise data center today are filesystem storage and block level storage. Filesystem storage is typically deployed as Network Attached Storage (NAS) systems and used for storing and sharing files over a network. Block storage is typically deployed as Storage Area Network (SAN) systems and appears to an operating system like locally attached drives, which is required for running things like databases. Generally organizations have to build a dedicated pool of these storage systems for each application (e.g., CRM system, email system) which isolates both the storage resource and the data from other applications. This approach means your organization has to scale these storage systems independently from other storage resources - and as the number of applications increases, so does the number of storage systems in your datacenter.

For the applications your developers are writing today, this storage model has several drawbacks which, according to the industry analyst firm Gartner, includes:

    It doesn’t efficiently scale to support new workloads
    It's bogged down by operational overhead
    It's difficult to match storage to application requirements
    It's time-consuming to adjust to workload changes and migrations
    It's manually managed, or at best semi-automated

These drawbacks become increasingly important as the rapid growth of unstructured data that many, if not most, enterprises are experiencing today continues. Nearly every industry is storing and serving more data at higher fidelity to an increasing number applications and users.

End Quote.



## OpenStack Swift

https://docs.openstack.org/swift/latest/

> Swift is a highly available, distributed, eventually consistent object/blob store. Organizations can use Swift to store lots of data efficiently, safely, and cheaply.



# Related to handling metadata

## Open-Metadata

[https://open-metadata.org/]()


# Possibly interesting filesystems


## BFS (BeOS)

  * [The 'Be File System'](https://en.wikipedia.org/wiki/Be_File_System)
  * [Linux BFS driver](https://www.kernel.org/doc/html/latest/filesystems/befs.html)
  * https://sourceforge.net/directory/file-systems/linux/
  * [Haiku OS](https://www.haiku-os.org/get-haiku/r1beta4/)

1997

https://arstechnica.com/information-technology/2018/07/the-beos-filesystem/

> One of BFS's most important and widely touted features is its support for extended attributes. An example of the importance of attributes is illustrated with an example of MP3 files. Information fields important to an MP3 file would be: song title, band, album, release date, encoding rate, length, number of times played. If you want to associate this information with each MP3 file using a conventional file system, you might have to create your own database to support searching, creating, updating, or deleting these attributes as your music collection grows and changes. With BFS, in contrast, these attributes, or any other attributes, can be added to the file system itself. This means that a program for editing or playing MP3s does not need to create or maintain a database, because the file system will handle these functions for you. BFS supports associating attributes with a file, either under program control or from the command line. Attributes can be searched and sorted by the file system, as an extension of any application. How this is done will be discussed in detail later.



## UFS (Unix File System)

[Unix File System (UFS)](https://en.wikipedia.org/wiki/Unix_File_System#UFS1)

In 4.4BSD UFS2 was split in 2 layers:

  * UFS: upper layer (meta)
  * FFS: lower layer (data)

I know I said: Keep the meta with the data, but thinking about this:
It may make sense to not divide by semantics/meaning of the "meta/data" at all - yet simply move smaller data from UFS to FFS - once it grows beyond certain thresholds - or according to other copy/keep-dynamics profiles. Those profiles may be adjusted according to usage logs (Warning: This may encode personal user behavior in data).

So to have means of handling smaller/lighter data differently - regarding performance - yet being completely transparent to the accessing user/function.

For many bulk-operations, regarding search, annotation or reseach. Find-and-retrieval is trivial, since the payload is yet another (identical) "key=value" meta/data Object. The underlying storage technology may therefore offer slower/cheaper/larger digital storage options/devices for "data" - and have faster/expensive/smaller memory for "meta".

All done in the filesystem.
I assume optimizations like this will currently not work out of the box on existing network-scalable (object) storage filesystems. However, it doesn't strike me as particularly hard (in comparison to the existing, stable complex functionality) to implement/add being able to have a proper meta+data handling capabilities.






# https://www.databricks.com/

[Introduction to Data Lakes/Lakehouse (by DataBricks.com)](https://www.databricks.com/discover/data-lakes)


# https://solidproject.org/

[W3 Solid Community Group](https://www.w3.org/community/solid/)
[Solid Specification (Github)](https://github.com/solid/specification)


## Scope

Source: https://www.w3.org/community/solid/charter/

```
In general, topics that are “in scope” include anything related to enabling affordances for decentralised Web applications to create and use data across decentralised storages in a way that is secure and privacy respecting for individuals and communities. Work items are intended to be compatible with or extend the Architecture of the World Wide Web. These topics include, but not limited to, the following:

    Protocols for the storage, transmission and portability of data.
    Authentication and authorization mechanisms.
    Notifications.
    Query interfaces.
    (Meta)data models that can be used in storages, e.g., policies, data privacy and rights, provenance records and auditing, error messages.
    Profile descriptions for social and software agents.
    Data interoperability: sharing semantics of the content of resources, e.g., data shapes, data portability.
    Service interoperability: sharing semantics on the discovery of actions and access to resources, e.g, web service descriptions, provisioning, portability.
    User interface affordances: the display of data and services in a view.
    Vocabularies providing the necessary semantics for the mechanisms defined within the scope of this group.
    Signing messages.
    Federation, e.g., message passing, trust, data cascading.
    Evaluation tools (software programs or online services) that help determine implementation conformance.
    Publishing test reports and communicating the level of adoption of technical reports.

With the exception of integrating or bridging specifications developed by another active community in an open standards development body that specialises in a particular topic, the Solid Community Group defer the work to the other community.
```


# https://flur.ee/

From Content to Knowledge

Best-in-class content classification and tagging software, powered by NLP.

Fluree Content Auto-Tagging Manager transforms unstructured data into semantically organized content that is searchable and available across your organization.




# https://www.enterprisestorageforum.com/hardware/file-system-management-is-headed-for-trouble/

This is from 2009 - yet I think Newman is addressing similar concerns regarding
'the [classical](POSIX) file system interface isn't up to the task of managing
today's data'"

By Henry Newman
February 24, 2009

> "The POSIX file system interface isn’t up to the task of managing today’s
> data, resulting in costly fixes for users to solve problems [...]"

> "The problem with management of files is just that: they’re being managed as
> files, not as information. The standard POSIX information is far too basic.
> There are applications like Google Desktop that help you find what you’re
> looking for, but that solves only part of the problem."

> So why has no one done this yet? I think there are a number of reasons:

  * Vendors do not want to make changes, and any changes to the POSIX standard
    would require both file system and operating system changes.

  * Vendors are making money on user space applications. This is a poor reason,
    but I believe it is likely true. If something was standardized, then you
couldn’t sell it.

  * These changes would generate more overhead, as you will have additional
    space for attribute data. This will increase the size and space needed for
file system metadata (inode data) and will increase the time to open and read
files.


# Atempo Miria

https://www.atempo.com/products/miria-backup-and-migration-for-large-file-storages-3/

