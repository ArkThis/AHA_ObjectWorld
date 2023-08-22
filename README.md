# A Holodeck by August.

These are notes regarding a technical draft for using Object Storage Filesystems beyond "just storing files", by moving metadata and database needs to the filesystem's "tagging" feature.

In a nutshell:

  * What if you could put any metadata with your file?
  * What if filename/foldername was "a tag option" and nothing more?
  * What if you could create and handle database/catalog/DAM entries in your regular file manager/browser?
  * What if that would work with any application or digital environment?
  * What if that was all FOSS-licensed?
  * What if that was well-supported by small and big companies?

Sounds pretty crazy, but I'd like to challenge building a working prototype.

The prototype shall at least be able to:

  * Provide an S3 compatible, *local-only* (but network-able) Object storage (MinIO?).
  * Copy cultural heritage object files - and *attach* their metadata as-is.
  * Copy existing pre-structured or embedded metadata values to the "name=value" space.
  * Query that storage by its "Objects and their metadata" in MongoDB.
  * Have a web-browser-based application to display and interact with these objects:
    * regular file manager functionality.
    * display relationships (as graph? node network?)
    * plain viewer for basic formats (think IIIF)

The documents are currently merely a notepad for ideas, as well as may contain
concrete technical implementation considerations or remarks that may be
considered when implementing certain options.

If you like you are welcome to engage in this idea: You may see the whole digital world around you in a very different way. That may be the real, awesome-digital 21st century! 🌟️
