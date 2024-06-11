Possibly related, existing projects/things:

# Articles

## 6 best practices for metadata storage and management

> Metadata is crucial to getting the most out of data, so organizations should store it properly. Best practices include protection and understanding the IT architecture.

By Robert Sheldon
Published: 02 Feb 2023

[https://www.techtarget.com/searchstorage/feature/6-best-practices-for-metadata-storage-and-management]()


## How to generate guaranteed unique id for files stored on server? (AWS S3)

https://stackoverflow.com/questions/42732780/how-to-generate-guaranteed-unique-id-for-files-stored-on-server




# Los Alamos, CMU / DeltaFS

  * [CMU/PDL File Systems](https://github.com/pdlfs)
    Scalable file system services for high-end computing and big data applications
  * [Qing Zheng - Breaking the Metadata Bottleneck](https://zhengqmark.github.io/papers/deltafs-sdc19-slides.pdf)
  * [Toward Standardized, Open Object-Based Computational Storage For Large-Scale Scientific Data Analytics](https://zhengqmark.github.io/papers/ocs-pdsw23-vision.pdf)

  * [DeltaFS Overview](http://www.cs.cmu.edu/~qingzhen/files/deltafs_pdsw15.pdf)
  * http://www.cs.cmu.edu/~qingzhen/files/deltafs_pdsw17.pdf
  * http://www.cs.cmu.edu/~qingzhen/files/deltafs_sc18.pdf


> "DeltaFS assumes an underlying object storage service to store file system
> metadata and file data. This underlying object store may just be a shared
> parallel file system such as Lustre, GPFS, PanFS, and HDFS. However, a
> scalable object storage service is suggested to ensure high performance and
> currently DeltaFS supports Ceph RADOS."



# Lustre - Fast, Scalable Storage for HPC

[https://www.lustre.org/]()
[https://wiki.lustre.org/Main_Page]()
[https://www.lustre.org/getting-started-with-lustre/]()
[https://www.opensfs.org/]()

```
Lustre Enables High Performance, Massively Scalable Storage

Lustre is an open-source, distributed parallel file system software platform designed for scalability, high-performance, and high-availability.

Lustre is purpose-built to provide a coherent, global POSIX-compliant namespace for very large scale computer infrastructure, including the world's largest supercomputer platforms. It can support hundred's of petabytes of data storage and hundreds of gigabytes per second in simultaneous, aggregate throughput. Some of the largest current installations have individual file systems in excess of fifty petabytes of usable capacity, and have reported throughput speeds exceeding one terabyte/sec. 
```

-----------------------------

# Interesting Database Engines

## Redis

[https://redis.io/]()

Redis is not an Object storage, but a very simple key-value-blob storage (database) engine - in RAM.

> "Redis is an in-memory data store used by millions of developers as a cache,
> vector database, document database, streaming engine, and message broker.
>
> Redis has built-in replication and different levels of on-disk persistence.
> It supports complex data types (for example, strings, hashes, lists, sets,
> sorted sets, and JSON), with atomic operations defined on those data types."

[https://redis.io/docs/latest/develop/get-started/]()



## KeyDB

[https://docs.keydb.dev/]()

> "KeyDB is a fully open source database, backed by Snap, and a faster drop in alternative to Redis"

> "KeyDB is a high performance open source database used at Snap, and a powerful drop-in alternative to Redis. While many databases keep the best features locked in their paid offerings, KeyDB remains fully open source. This best enables Snap & the community to collaborate and benefit together in the projects development."

### Install on Ubuntu:

```
$ echo "deb https://download.keydb.dev/open-source-dist $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/keydb.list

$ sudo wget -O /etc/apt/trusted.gpg.d/keydb.gpg https://download.keydb.dev/open-source-dist/keyring.gpg

$ sudo apt update

$ sudo apt install keydb
```


## LevelDB

[https://en.wikipedia.org/wiki/LevelDB]()

> "LevelDB stores keys and values in arbitrary byte arrays, and data is sorted by key. It supports batching writes, forward and backward iteration, and compression of the data via Google's Snappy compression library.
>
> LevelDB is not an SQL database. Like other NoSQL and dbm stores, it does not have a relational data model and it does not support SQL queries. Also, it has no support for indexes. Applications use LevelDB as a library, as it does not provide a server or command-line interface.
>
> MariaDB 10.0 comes with a storage engine which allows users to query LevelDB tables from MariaDB."



## RocksDB

[https://en.wikipedia.org/wiki/RocksDB]()

> "RocksDB is a high performance embedded database for key-value data. It is a fork of Google's LevelDB optimized to exploit multi-core processors (CPUs), and make efficient use of fast storage, such as solid-state drives (SSD), for input/output (I/O) bound workloads. It is based on a log-structured merge-tree (LSM tree) data structure."

[https://github.com/facebook/rocksdb]()



# European Open Filesystem (EOFS)

[https://www.eofs.eu/]()

## EOFS goals

  * To promote the establishment and adoption of open source parallel file systems, sustain and enhance its quality, capabilities and functionality and ensure that specific requirements of European organizations, institutions and companies are upheld.
  * To facilitate the extension of business operations to non-members.
  * To initiate projects or to collaborate with existing projects at regional, national, European and international level in order to support Research & Development activities concerning Open File Systems.
  * To ensure that engagement and activities with other organizations will not directly or indirectly interfere with the intellectual property or other contractual and legal obligations of its members.
  * To operate as a non-profit organization.




# "Real" Object Storages

Preferrably conforming to OSD (2, 3?), as according to [Object Storage on Wikipedia](https://en.wikipedia.org/wiki/Object_storage), this sounds more what I'm loooking for that what S3 (and therefore Minio) seems to provide.



## Oasa

https://www.atlantis-press.com/article/25868044.pdf

Active storage can largely reduce the network traffic and application execution time. In this paper, we
present the design and implementation of an active storage architecture called Oasa for object-based
storage system. Compared with previous work, Oasa has the following features.(1) It provides a flexible
and efficient way for user to process data. User functions can process data of one user object or multiple
objects at a time. (2) Oasa supports multiple patterns of user functions: both the input and output of the
functions can a) come from network or disk or b) go to network or disk. (3) It keeps compatible with
the current T10 OSD standard and requires little extra modification to execute user functions. Using the
extended OSD commands, user can conveniently create, delete, associate and execute user functions with
user objects. We also evaluate the performance of Oasa by running a typical application-data selection.
It is a representative data analysis application widely used in solving real problems. Experimental results
show that when the proposed active storage functions are enabled for object-based storage system, the
client can obtain upto 61.9% reduction of application execution time.


## Apache Ozone

https://ozone.apache.org/


### Quote:

     Apache Ozone is a highly scalable, distributed storage for Analytics, Big data and Cloud Native applications. Ozone supports S3 compatible object APIs as well as a Hadoop Compatible File System implementation. It is optimized for both efficient object store and file system operations.

    It is built on a highly available, replicated block storage layer called Hadoop Distributed Data Store (HDDS).

    Applications using frameworks like Apache Spark, YARN and Hive work natively without any modifications.




### Quote:

https://blog.cloudera.com/introducing-apache-hadoop-ozone-object-store-apache-hadoop/

    The Apache Hadoop Distributed File System (HDFS) has been the de facto file system for big data. It is easy to forget just how scalable and robust HDFS is in the real world. Our customers run clusters with thousands of nodes; these clusters store over 100 petabytes of data serving thousands of concurrent clients.

    True to its big data roots, HDFS works best when most of the files are large – tens to hundreds of MBs. HDFS suffers from the famous small files limitation and struggles with over 400 Million files. There is an increased demand for an HDFS-like storage system that can scale to billions of small files.

    Ozone is a distributed key-value store that can manage both small and large files alike. While HDFS provides POSIX-like semantics, Ozone looks and behaves like an Object Store.



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




# OrangeFS

OrangeFS is *NOT* an Object Storage. It is designed to store meta+data and scale large and performant, but it does not provide ObjectIDs (yet):

https://github.com/waltligon/orangefs/discussions/107#discussioncomment-9598607


https://de.wikipedia.org/wiki/OrangeFS

> OrangeFS arbeitet objektbasiert: Dateien und Verzeichnisse bestehen dabei aus mindestens zwei Objekten; eines für die Metadaten und die Nutzdaten. Das Dateisystem benötigt keine Konfiguration und wird vor allem in Forschung und Wissenschaft verwendet.

https://docs.orangefs.com/nix-clients/fuse-client/

http://www.orangefs.org/faq/#item5.12


```
prompt# setfattr -n key1 -v val1 /path/to/mounted/orangefs/foo

To retrieve an extended attribute for a given key ("key1") on a orangefs file foo,

prompt# getfattr -n key1 /path/to/mounted/orangefs/foo

To retrieve all attributes of a given orangefs file foo,

prompt# getfattr -m "" /path/to/mounted/orangefs/foo
```


