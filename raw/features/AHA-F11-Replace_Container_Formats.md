## May replace all (media) container file formats.

> By "dissolving/resolving" (or translating) them into Objects.

Literally as simple as that.
De-mystifies all media container formats immediately.

Strips them down to Objects on your Data Storage that have links/references to other Objects.
This is now regular day-to-day "business" for an AHFX filesystem environment.

There is no more difference between meta and data - and double-click-playback of such a "media graph" would probably already work with a fancy-piped ffmpeg|ffplay|vlc|mpv script-foo. FFmpeg read multiple streams on-the-fly from several filesystem and/or URI ressources - and multiplex them into a meaningful audiovisual, multimedia experience.

Which difference is left when you compare any media container format now, that their contents/streams/metadata - including subtitles and attached any-fileformat "files": All stored as Data Objects, related to each other - with a lib function to conveniently "use that graph as format".

Which current feature of any container format could not be translated into an Object Data graph like this?


As already described for audio:
The AHA world may depict the information provided by current media file formats like Matroska (mkv), AVI, MOV, MXF, etc) - in a Object object graph.

Basic example:

  * MyMovie [title, artist, year, ...] <mkv>
    * Video stream 1
    * Audio stream 1
    * Audio stream 2
    * Subtitle stream 1
    * Timecode track 1

It's right there. This is not the output of MediaInfo anymore, this is the basic way you handle your daily computer needs. Working with "data objects".

It is very likely that by translating container formats to Object graphs, the following additional benefits may occur:

  * Each stream/content object will accumulate its own metadata over its creation and lifecycle.
  * The actual "differences" between features of different container formats will become common code, because most of it is now handled by the default AHFX layer.

This may very well apply to any other "complex" multi-data format.
If bandwidth is enough, or meta/data-filtering fast enough, one may even consider AHFX as plain network protocol.

