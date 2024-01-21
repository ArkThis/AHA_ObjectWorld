## May replace the "library" parts of any music/image/whatever management tool.

Music library handling players like: Clementine, WinAmp, VLC, iTunes, etc - all have one thing in common:
They scan the media files for metadata, which each application then stores it in their own (internal) database and data-layout, to provide search and sort functionalities.

Filenames may sometimes be considered as valid metadata source, and parsed "best effort" to guess at least the basic fields like "title", "artist" and maybe track-id or album name. Year or more is already a bonus.

But in practice, most well-assorted audio collections contain proper metadata, *embedded* in the file itself. This kind of "tagging" became most popular to the public with the popular MP3 format.

The actual reading/writing of these embedded metadata fields/tags actually require to "understand" any given file format that one may want to read or write this descriptive information.

This requires to know the specification of each format that one wants to support (they pile up over time), and this has to be done again and again for each new format or version or variant of a new (media) file format being released.

Now imagine all metadata (descriptive or technical) would actually be on the Object file system layer. The Object can be queried for all its metadata field as easily, and naturally as reading its filename or folder position before.

Then the actual difference between 2 audio formats would be most likely:

  * The encoding of the actual audio
  * Handling audio channels
  * Handling audio tracks

If you already think in AHA-Objects, then you can pretty much guess and already easily grasp how that would be easily be covered by "AHFX" (Working title for such a kind of filesystem standard):

  * Main Audio Object (Object):
    This is the one you'd "click on" or select if you'd like to handle "the whole recording" or session.
    It's probably a good idea to come up with some id- or naming-guideline or standards listing to make it clear if an object is an "entry" object.

    It contains at least "the usual/common" metadata fields. Which metadata fields/layout that is, may be provided by any Object-aware "data browser". Imagine to right-click it, and you'll get the familiar name=value mask for audio productions/recordings. Like that.

    It may contain references (relationships) to other Objects for:

    * each audio track
    * each audio channel
    * more metadata/relationships to describe the object.
    * anything else?

Depending on your "data browser" aka "AHA browser", you can select whether you see just "the audio file" (like you're used to) - or "the whole set, all channels, tracks, etc" - or "objects that are related in some (other) way". And you'd not only be able to see this like files in a folder in your choice of "file manager".

Yet, you're actually now able to manipulate and interact with the internals of what was previously (before AHA-Objects) some (mostly) binary file format which required you to know the specification, read hex and understand way too much about computing to even begin with.

So, before if you were lucky you saw this:

  * XBloome - X Marks the Spot - Planet Q.mp3

And now you see this:

  * XBloome - X Marks the Spot - Planet Q.mp3

Or this:

  * Planet Q [XBloome, X Marks the Spot] <mp3>
    * Track 1: [english, MP3]
      * Channel L [left]
      * Channel R [right]
    * Track 2: [albanian, PCM]
      * Channel L [mono]
      * Channel R [music]

Imagine seeing this in your default file manager of your choice.
And you could simply right-click-edit if you'd like to change any metadata field. Title, artist, language, album, year, link-to-band-website, youtube, etc.

And if you'd like to add or swap or re-order channels:
Just do so, by either drag-n-drop or changing relationships or references.

Regardless of which file or media format.
So the same for photos, videos, documents, anything. Even construction plans or automation G-codes. Anything can be depicted as Objects.

