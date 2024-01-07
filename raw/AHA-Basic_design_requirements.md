I want to find my stuff.

And I want to get funding and staff for implementing seamless support in a chosen FOSS stack from private to professional.

I seriously technically-professionally cannot imagine why the simple features I imagine shall not be possible with quite basic on-board tools (I'd expect) from any Object Storage filesystem.

read/write/cache/index/copy/keep/resolve/filter basic "name=value" tags and relationships by URI/IDs in a most generic way.


# Holodeck that shit.

I imagine the following to be rather trivial (seriously. Mainly because i mean: "there's already working code for that, or the code required should be quite basic").

1. Setup an Object Storage: MinIO
2. First setup: Single disk/folder, single pool, single host.
3. Import existing objects: Fotos, videos and documents folders to now be "Data Objects".
4. Add metadata "name=value" to a selection of such Objects.
5. A query possibility to "select from ... which name=value, or relate to ..." for Objects.
6. Simply store source folder/file names as name=value pairs:
`folder=/this/is/where/it/came_from` and `filename=CAM00001.jpg`
7. Implement proper NextCloud WebUI support.
	To really access/browse all Objects folder-free (optional view/plugin) including IIIF-compatible plugins for viewing/editing.
8. Support auto-fetching (harvesting) of popular FOSS/open-licensed platforms, like WikiData, GND, etc. to "fatten up" the relationship and annotation details of your Objects.
9. Audio player to use Object's filesystem metadata (name=value) tags instead of embedded.
10. De-embed all metadata in one run.
Simply put together a sane collection of FOSS metadata extraction tools for all kinds of file-formats. Sorted by interests and accessibility. Theoretically practically open-ended and freely editable.
11. Right-click: Edit Metadata.
A simple nested name=value (JSON-ish?) display/editor for metadata.
12. Support profiles:
Several different use cases.

  * copy: to local vs external vs remote carrier
  * view/edit metadata
  * backup decisions
  * access decisions
  * index decisions
  * general filtering
  * pre-defined queries

They all run on any Object.


13. light vs heavy copies:
When copying an Object, the following shall be possible:

  * apply a (filter-)profile by default.
  * use keyboard modifier (hold) to pop-up filter/profile options.
  * deflate objects by:
    * saving URI/IDs instead of values.
    * Replace payload (or anything larger than n-Byte threshold) by a placeholder (URI/ID or text).
  * Ruleset for deflating/pepping-up an Object graph copy.
  * Existing regular options: 
    * "Copy just as IDs and metadata"
    * "Copy just THIS Object"
    * "Copy all related Objects until depth $d"



# Light and heavy copies:


## Imagine you copy a photo collection, and select "thumbnails" profile...

  * All payload is stripped and replaced with a defined placeholder (URI/ID/text)
  * Existing payload is thumbnailed.
  * Thumbnails linked as newly created Objects.
  * Embedded metadata would be extracted and copied onto the filesystem name=value metadata.

You get a thin (small filesize) copy of your collection.
Just like that.


## Imagine you copy a music collection, and select "catalog entry" profile...

  * All payload is stripped and replaced with a defined placeholder (URI/ID/text)
  * Existing payload is thumbnailed.
  * Thumbnails linked as newly created Objects.
  * Embedded metadata would be extracted and copied onto the filesystem name=value metadata.
  * Unless the payload was plaintext. Then it is kept and contained markup may be supported.
  * "Key Objects" (conditions of the source Object Graph) contain web-UI templates for engaging with the (related) Object meta-and-data.

The copy you'd get would depict all descriptive metadata (as well as the source), and feel like browsing/selecting your music in your favorite music library application.

The big difference being:
The default browser(-engine) based UI now servers instantly as a proper cataloging system, as you can annotate and related any Object. Local or remote. Even URIs supported by basic design.


## Imagine a more mixed copy profile...

  * Define at which depth to deflate data.
  * Define rules/queries/filters in profiles to select Objects on the relationship graph beyond (or instead of) a given depth.



## Enflate/Deflate/resolve whenever you like.

Basic Actions should exist for the following:

  * Resolve "value" in common, online databases (eg Wikidata) and additionally store (own tag) the same "name" but the ID as value.
  * Replace payload with a placeholder: URI/ID/text/thumbnail
  * Add a tag that indicates that this is a "proxy copy" or thin/placeholder/reference copy.
  * These actions shall be used on sophisticated copy-profiles. Therefore if the code is stable for one, it works for the other. It's the same use-case, just different timing.
  * Enflate or "pepping-up" Objects:
    This can be done on deflated (light) Objects, or on any regular Object.
    URI/IDs will be resolved to a copy of the linked content (profile defined).
    Example: Wikidata ID resolves the whole Q-entry. Or: Copy of Wikipedia article as "metadata value".
  * Pepping-up means pulling in more Objects:
    Imagine it a bit like torrent-magnet links as a daily thing.
    With magnet-like links as metadata value reference, actual existing data (eg the actual song/movie) referred to in a catalog object can be downloaded (if accessible) and auto-linked to the entry Object providing the links.
    This could be the default way of transferring between institutions who have access to a shared pool of "Files".

  * All actions can be applied recursively and/or by profile selection.

You can perform these actions at any time, and any AHFX-compatible system shall provide simple scheduling options.


## Merging copies

The collission-friendly IDs of the AHFX design make it easily possible that light copies may auto-collapse (merge) with their heavy counterparts. Without collission-IDs, tags previously stored when creating the light copies, would be used to match to their (existing) source Objects.

It can be chosen whether to merge or keep-as-is when copying.


