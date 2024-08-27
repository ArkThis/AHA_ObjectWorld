# "AHAlodeck" - A Whitepaper

**Do you remember when files could only be 8.3 letters UPPERCASE-ASCII-ONLY until 1995?**

  * What if a filename became finally "just another database metadata field"?
  * What if folder name and path text, too?
  * What if you could annotate/tag any data/file you're working with?
  * Regardless of the file format?
  * No special tools needed. All basic file-manager built-ins?
  * Modern "cloud-features" only available in online web-uis or apps can be supported anywhere - offline too.

**I believe any collection of any size of any GLAM institution is a subset of size/complexity a regular common FOSS 'big-data' stack is built to process and handle.**

> The environment proposed here into a new way of handling "data" may be as magically self-empowering as moving from 8.3 characters in file/foldernames to 250+ full character-set to name things in computers. Adding XML later, introducing the idea of "plain text, yet structured" as replacement for binary-encoded data-formats.

> As harmless as it may seem, but moving to "human-readable computing" as the worldwide standard has greatly and positively influenced the way "we" are able to handle our digital (work)flows. The advancements in hardware speed and accessibility allow us to handle metadata "natively", and store-and-access data by search/query/ID rather than path-and-filename.

> Being able to think in and work with "Data Objects": And you can simply right-click-edit "meta *or* data". On any format, at any time. This also includes a transition from "files-in-folders" as data-handling paradigm onto 21st century big-cloud tech-stacks.

I am proposing a project to implement a basic environment that introduces advanced data-handling paradigms, which may dissolve the barriers between "files in folders" and related "metadata". This is done by moving basic database functionalities to the filesystem. And having basic file-manager/browser capabilities, as well as CLI as common user interfaces.

As part of this, we will configure and document a blueprint for a professional short-to-long-term data storage.

The technologies required to implement this already exist, and are well-known and production-stable in regular large-scale "Big Data" setups and supported by major companies worldwide already.

This project proposes orchestrating existing projects/tools and known best-practices to build a working prototype that will cover most vital use-cases when handling any kind of "digital collection":

  * Generic access to common "embedded metadata" (for different file/media-formats)
  * Generic keyword-tagging of any "file or folder" (Data Object)
  * Immediate replacement for all Excel/CSV list uses in GLAM (or at home).
  * Cross-tool metadata accessibility by design.
  * Full-text/facetted search and query on any of your data as basic filesystem/OS functionality.
  * Full annotation support by "right-click-edit-metadata" in a file manager of your choice.
  * An underlying storage configuration with all state-of-the-art advanced features (failover, (geo-)replication, versioning, HSM, etc).
  * The storage configuration scales from local (1 Disk) to worldwide large-scale cloud network.
  * Provide a (REST) API to publish collection datasets.


## Required/Existing Tech-Components

Here is a list of known existing tech-components which can be used as parts for this protoype:

  * Apache Iceberg
  * Apache Spark
  * Parquet
  * OpenStack (Swift)
  * EXT4, ZFS, HFS+ / Samba
  * Minio?



## Long-Term Storage of large data collections - and catalogs for that.

What if your files were "Objects" you could simply annotate and relate to other "Objects"?
And then search/query/filter that.

The current "best-practice" in the whole GLAM sector, worldwide - regardless of size or budget - is primarily to save "files-in-folder" and store information about them "somewhere else" - or some of it "inside some of those (media)files". Or in Excel-sheets, Filemaker, Access, XMLs, JSONs, Database XY, DAM-MAM-CMS APIs, etc.

It's a mess to be honest.
A very expensive and exhausting mess.

Mainly caused by the fact that handling "files in folders" and related "metadata" in 2 (or more) completely separated data paradigms: File-management/storage and database.

This separation/gap is technically not necessary anymore.



