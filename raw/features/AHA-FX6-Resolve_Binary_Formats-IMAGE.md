# Annotated Filesystems: Resolving binary file formats.

Example: Digital Image (Files)

Using AHAlodeck designs (meta+data, ObjectID, etc) to transform common (even binary) file formats to common denominators, may greatly improve our current situations regarding file-format support. Especially over time (long-term).



Take, for example, digital image information:

**Binary formats**

  * **BMP**: metadata={width, height, bits-per-pixel, palette?, compression mode, ...} + image data
  * **PNG**: metadata={width, height, bits-per-pixel, palette?, compression mode, ...} + image data
  * **TIFF**: metadata={width, height, bits-per-pixel, palette?, compression mode, EXIT tags, ...} + image data
  * ...

As one can see, often different file formats intended for similar purposes, share similar (technical) properties - and therefore (technical) metadata fields. These formats seem very similar here, because here I didn't show the *exact* header and data layout in the file's actual bytes.

With binary formats it matters at which byte-offset exactly a value is stored (eg width/height) - and one must know exactly "the word size" (=how many bits/space that value may have): 32bit, 64bit, signed/unsigned, endianess, and-so-on, etc.
If it's a string somewhere, you also may need to know if it's (null-)terminated in some way or not to read metadata.

This is the reason why each file format, and each of its features and metadata-fields has to be individually supported by an application.

Sure this support is added by using programming libraries (aka "libs") /for each format and feature/.
It works, but it adds quite a lot to (dependency-)maintenance over time.
One lib for each file-format. Different libs for the same format may-or-may-not support/implement/provide the same feature of that same format.


## Using the filesystem as key/value store.

If being able to store key/value metadata with a "file" object, it wouldn't matter at which "byte offset" eg width/height/etc are stored:

Technical (header) metadata, if present as filesystem attribute, can simply be queried. Easy and consistent.
**Regardless of the file/data-format.**

At the cost of byte-size of metadata.
Binary-encoded information (especially numbers) use less bytes than their equivalent in "plain UTF-8 text".
But it's worth it.

(I refer to XML back when it was "new" - as it was "heavy" and resource-hungry to work with as data-format, compared to the well-known binary layouts. Our hardware can handle it better now.)


My claim is, that when moving as much (even technical-)metadata to the filesystem, so it can stay /with/ the (payload) data, the differences between file-formats for a similar use-case will diminish greatly.
It provides instant, easy and consistent ways of storing, accessing and using /any/ object's metadata.

For example:

Imagine 3 different image files:

  * image1 (BMP):
    * metadata = {width=320, height=200, bits-per-pixel=24, color=RGB, **NO METADATA capabilities supported**}
    * payload = Uncompressed image data (RGB24)

  * image2 (PNG):
    * metadata = {width=320, height=200, bits-per-pixel=24, color=RGB, encoding=LZ77+Huffman, **metadata: PNG title**}
    * payload = Compressed (LZ77+Huffman) image data (RGB24)

  * image3 (TIFF):
    * metadata = {width=320, height=200, bits-per-pixel=24, color=RGB, encoding=LZW, **metadata: EXIF tags**}
    * payload = Compressed (LZW) image data (RGB24)


As you can see, the technical-metadata (resolution, `pix_fmt`) of the "Content" (image) are identical.
As you should also see now, the "differences" between file formats for an identical use case (eg images, audio, video, etc) become less relevant, with *no need to parse a binary header or stream-offsets* to get information.

> The only /real/ difference between the 3 files is, their encoding.
> And the fact that they have different (or no) annotation metadata included.

With, for example, extended filesystem attributes (xattrs), any annotation/tags (even RDF tuples) can be stored in the filesystem /with/ your data.
Not /inside/ a file format anymore.
So there is no more limitation to whether or not "a certain file format" could contain/use certain key/value information.
Very similar to RDF: As long as the key/value context is clear, mix-and-match as you like.
It'd be perfectly possible to use and support JSON-LD (Linked Data, Semantic-Web) syntax for filesystem objects.

So any application opening "an image object", would probably care less about "what binary file format" it was, but more about: "can I encode/decode the payload properly"?


# Summary

I believe we've reached the point in computing, where we can re-question very fundamentally-basic paradigms we've grown up with and fond and maybe tired of: Like complex-binary (container-)file-formats.

Simply moving as much metadata as possible (even binary headers) to the filesystem level will greatly change interoperability and feature-support between applications and any data "formats".


What are currently very different file formats in binary layout will become very similar (and therefore easier if not instantly supported) data formats. More complex formats may involve related objects (object graph).

Later, maybe so called "mature" (or AIP? :P) data objects (on such annotated-graph-like-filesystems) may include metadata like "a decoder": in any form, too.
For example, media files could "link" (key/value) to online information or tools how to decode/interpret itself.
Or (if `max. attribute size` allows): Simply contain a codec (in run-able form).


The good news is, that storing and handling data like that is not a new approach at all.
Extended File System Attributes (xattrs), resource-forks, named-forks, BeOS/Haiku, etc were already designed in the 90s.
Apple's `resource forks` (also 90s) already stored data with header-and-payload separately (legend has it) for the very same reasons.

So the underlying tech-stack to support this exists, and now has a stable (open standard!) core since the early 2000s.

I think it's about time to make use of good filesystems the way they were intended / designed to be for.
A long time already! 🌈️



So how many file-formats are we dealing with now - in "the conventional ways"? 😉️
Fun?
Cheap?
Interoperable?
Stable?
