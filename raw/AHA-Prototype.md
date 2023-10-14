# AHA - A Holodeck by August

# Prototype I: Ideas and Plans.

## Existing Components

  * MinIO
  * SNMP tools/specs/libs
  * CSV, JSON (XML?)
  * Indexing for full-text search
  * Graph-Relationship-Indexing
  * IIIF
  * Web-Browser Engine (HTML5/CSS3/etc)
  * Filtering/Transformation engine for metadata (like XSLT for XML)
  * A few demo-applications to test potential behavior:
    * music library player application
    * picture collection organization application
    * asset management system


## Rough draft


### Level 1

  * Setting up MinIO:
    * Config so that it's easy to switch between local-only and network-aware storage.
    * Just to prove that this design shall scale natively from local-to-nas-to-cloud.
  * Enable metadata storage/handling for each object.
  * Configure and write basic metadata input/output and handling operations.
    As CLI/GUI-Tools as well as programming libs and filesystem highlevel-API.
  * Starting in Python on GNU/Linux.
  * Using the current filesystem options as they are.

  * Demo 1: Cultural Heritage Collections
    * Harvest Kulturpool Metadata and create (script) a real-world copy on the MinIO.
    * Attach the corresponding XML/JSON metadata as-is to each "file".
    * It's likely that only the preview images/media files will be available for automatic download.
    * Build an index to make it accessible - and combine that with a IIIF viewer for browsing.

  * Demo 2: Music collections
    * Take a simple FOSS music library application (eg Clementine, Rhythmbox, etc) as base.
    * Switch the internal database methods to the AHFX-aware libs/APIs.
    * Build "the usual music database" using a generic FOSS indexer.
    * 

  * Demo 3: Show your "Objects" in different ways:
    * the classical folder/files view.
    * by relationships (as weighted, click-able graph)
    * as browse-able tag-clouds
    * Like a professional catalogue-entry

  * Maybe make use of NoSQL (MongoDB, etc) or GraphDB engines to high-level handle the filesystem Objects.


## Level 2

  * Demo 4: Resolve embedded metadata
    * Take embedded-metadata extraction tools/libs and read as many file-formats as possible, and copy any metadata tag (mostly name=value, I presume) onto the AHFX filesystem level.
    * Adapt/implement a IIIF web-engine for viewing and editing this metadata.

  * Demo 5: Resolve media container formats
    * Translate different AV-media container formats (MKV, AVI, MOV, MXF, etc) to a relationship graph between its formerly internal "streams" or metadata.

  * Demo 6: Resolve file formats technical metadata
    * Copy the basic technical metadata, commonly structuring a file format's header, to the filesystem.
    * As Strings. I'm not sure if the complexity overhead is worth it to handle NUMERIC and STRING variable types.
    * This would have to be calculated.
      I assume it may have serious impact on data size (piling up) - and performance.
      Imagine: taking all 2-to-4 Byte header data and blowing it up to a number-string.

