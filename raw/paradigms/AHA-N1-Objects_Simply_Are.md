## There is no "fixed position" of an object anymore.

The "most fix" part of the data is probably on which actual block-storage "block" your data actually "resides".
How persistent or long-term that storage is, is up to you. Even from HDD to RAM.

Filenames are just "yet another metadata" field: "filename=...".
Folder structure is merely a representation of a delimited-string, like "path=..." or interpreted from references to "folder objects".

The term "folder" may actually be better understood here as "groups" or "context".

However: All objects "just are".
Their bytes are stored in blocks on some physical "carrier" somewhere.
But on the object level of the filesystem, they are only referred to by identifier or context queries and filters.
You can think of them like "floating information bubbles": FIBs.

First maybe it's good to try how it "feels" to have more than one filename. Then "more than one" folder, title, etc. Embrace and Expand to the new featureset as convenient as you feel.

If you are in a hurry, because sorting out data is your job:
Great!

Any efforts trying to handle the "keep existing filenames/paths/identifiers?" may boil down to:

  * Can we merge the tags?
  * Can we keep existing XML-JSON-ish metadata files with "the objects it relates to"?
