## Resolve binary file formats: eg Image

For example, digital image information:

**Binary formats:**

  * BMP: metadata={width, height, bits-per-pixel, palette, compression mode, ...} + image data
  * PNG: metadata={width, height, bits-per-pixel, palette, compression mode, ...} + image data
  * TIFF: metadata={width, height, bits-per-pixel, palette, compression mode, EXIT tags, ...} + image data
  * ...

As can see, often different file formats intended for similar purposes, share similar (technical) properties - and therefore metadata fields. These formats seem very similar because here I didn't show the *exact* header and data layout in the file's actual bytes.

With binary formats it matters at exact which byte-offset a value is stored (eg width/height) - and one must know exactly how many bits/space that value may have (32bit, 64bit, signed/unsigned, etc) - or if it's (null-)terminated in some way or not. This is the reason why each file format, and each of its fields has to be individually supported by an application.

Yet, if it wouldn't matter at which "byte offset" eg width/height/etc are stored: 

It may be very likely that the actual differences between eg different image/audio/video/etc data formats may resolve into similar - if not identical - object-metadata, or relationship types.

Leaving mostly the actual "encoding" of the payload as the only difference.
If an application happens to have the proper "codec" for that payload - the previously format-specific header layout would be no issue anymore.

Here are 2 images stored as objects:

  * image1:
    * metadata= {width=320, height=200, bits-per-pixel=24, color=RGB}
    * payload= Uncompressed RGB 24bpp image data
    

  * image2:
    * metadata= {width=320, height=200, bits-per-pixel=24, color=RGB, **EXIF tags**}
    * payload= Uncompressed RGB 24bpp image data

You can see this information in the AHA world right now "right-click: view object" in your object browser.

The image1 *was* a PNG and the image2 *was* a TIFF.
Since in this case the image encoding (RGB24) is identical, the only difference is that image2 had "EXIF metadata tags" (because TIFF-specs allowed that). In the object filesystem, any tags can be attached and stored - so there's no more limitation to whether or not "a certain file format" could contain certain tags.

So any application opening "an image object", would probably care less about "what binary file format" it was, but more on "can I encode/decode the payload"?

Currently first the "payload" and technical metadata (width, height, etc) needs to be carved out from the binary (file) stream. This is not necessary with objects: Get the metadata fields you're interested in, then handle the payload.

What are now very different file formats in binary layout will become very similar (and therefore easier if not instantly supported) data formats. More complex formats may involve related objects (object graph).

Or "mature" data objects may include metadata like "a decoder": in any form.
