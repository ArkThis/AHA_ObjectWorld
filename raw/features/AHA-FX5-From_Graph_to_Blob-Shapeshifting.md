## manifest binary filetype "as needed" (just in time ;)

> "From graph to blob"

Imagine data file formats (eg. {PNG, TIFF, GIF, JPG, ...} or {AVI, MKV, MOV,
MXF, ...} and any other format) are resolved into object graphs with a payload
on your object filesystem.

By knowing the binary data structure of a given file format, that binary "blob"
(matching a "currently common" file-format) may be created on the fly with the
information stored in the related object graphs that replace the eg "image
file".

How to convert data object-structure to a binary stream may be done by defining
graph-queries, combined with an XSLT-ish profile.

Such a conversion profile could then also be an object, making it easy to share
"Transformer Objects" for different data formats.


You can literally think of this like Digital Shapeshifting (ODO) of common data
formats.

