# Think about it:

What are you doing when you use any computing device for any purpose?
You're interacting with "data".
Great.

So what is "data" actually?
A file?
A folder?
A subfolder?
A format?

Or just "Something you click on"?

What if you could simply "tag" and describe any file - as natively and taken for granted like "a filename"?

In any computing environment.
Plain and simple.
Like renaming a file.
Drag-n-drop.
Or commandline batch.
As you like.



# Imagine you would see each file as a "Data Object".

A Data Object is:
  * A handle on a filesystem that allows:
  * to store metadata
  * to store a data payload (what you'd call "the file contents")


Why does it matter? For you?

# Intro

  * Imagine you have a picture file.
  * A few MBs in size.
  * The filename is "DMCI/CIMG0815.JPG".
  * Imagine you'd like to view and describe that image.
  * Tag it.
  * Right-click, properties: There you go.
  * name=value tags. As many as you like.
  * No character encoding issues: Full Unicode.
  * Now some are already populated by the camera/app.
  * Some were added by your friend who took the picture.
  * And you can simply add some more, like:
    * My best friend's party.
    * wohooo!


# Stage 1: Tool-independent.

  * Oh, btw: binary-safe!
  * That change is simply saved to wherever location you accessed that image from.
  * local or remote.
  * If you like to work with the metadata, you can either do it in your file manager "app" or in your desktop tool of choice. "It's just like filenames, only better!"
  * Previous workflows and routines stay completely the same, and compatible with regular file/folder metaphor and tools.
  * You now have completely portable "tags".


# Stage 2: Environment-friendly.

  * Yes also to nature, but that's another story.
  * Now imagine, you could access and edit any metadata field or tag in any application that you access that file with.
  * Would that be nice?
  * Imagine, really, it's as "taken for granted" as renaming a file. It's editing metadata all along.
  * There's one common denominator, where all computing systems meet: The filename (handle).
  * Now we've merely added the option to have "more than just a/one filename".
  * And it stays with your "file" (=payload) as reliably like a filename - yet even more reliable, encoding-safe to be exact.

How is that environment-friendly?
It doesn't matter anymore which computing environment you use or interact with ;)

If they can read "your files" - which now are Data Objects - they can access the raw data content (payload) as easy and natively as any metadata that is stored in that Object.

And imagine how much time, money - well energy and nerves - would be saved if your data would simply store and travel well - by default.


# Stage 3: Your music collection

The popular use case of having "digitized" all of your CDs, then later tapes - and vinyls, etc - to audiofiles.
If you haven't: How are you listening to your music in digital? :)
So I assume everyone of us is familiar with "audiofiles".

  * Imagine again: A file. In a folder.
  * This time it's a song you like.
  * Maybe it's even emotionally important to you.
  * I have quite a few of those! :D
  * Imagine you open your favorite music program:
    Probably one that allows you to "search/sort by artist, etc"?
  * Imagine all the common music metadata like title, artist, album, year, etc. is now simply stored "In the Object".
  * All sort/search functionality would stay the same: Any way your favorite player likes it.
  * The difference now is:
    The player wouldn't have to "understand" a certain file-format to handle
metadata tags. Any player application would merely read the tags - as "duh" as
handling filenames.
  * So the usually local player's index-database now just functions as metadata-cache. As "Indexer". To speed things up. The actual data is stored in the Objects.

So what?
  * All music player applications that have their own database, just became interchangeble and compatible.
  * Any audio file format (even WAV) can now be tagged in a way that is treated
    equally across all computing environments and applications.
  * If the Indexer's database format is standardized, these caches may even be
    "taken with you", or shared and synchronized with others. But more on that
    later.

Your digital music player of choice is now literally *your choice*.
The difference between several audioformats has now been greatly reduced.


# Stage 4: Stripping metadata layers.

How would moving descriptive metadata tags to the filesystem level change anything with file formats?

Imagine you'd have a program that can read all kinds of audiofiles' metadata:

  * mp3
  * mp4
  * mp7
  * mp12
  * mp42

and so on.
Currently descriptive (and technical) metadata are "embedded". Inside the file.
Unless you speak "hex" and binary and can read "code" you're probably not able to even "see" it.

Now imagine: All metadata is on the filesystem. Plain text:

  * title=...
  * artist=...
  * album=...

What's left is:

  * The actual audio data you're actually interested in. The music!
  * Technical metadata (tracks, channels, sample-properties, etc)

What are the differences between these file formats?

  1. Their compression rate and/or "quality".
  2. How they store "metadata".

Number (1) is usually The Main Difference between audio formats.
And number (2) has just been "resolved" to a default filesystem feature.

The reason why metadata is nowadays most reliably-travel-safe when "embedded" inside a file format.
The reasons for that are:

  a. legacy reasons
  b. and "issues" with traveling and aging metadata.
  c. because our cataloging import/export options are a technical nightmare.

Why embed metadata in a the Data Object paradigm?

It would just complicate things.
For the end user as well as any developer - and even companies.

Even commercial vendors may find it more profitable to support "Objects"
smoothly, rather than having to infinitely convert and migrate and update and
pay developers to publish their "digital things".

Now imagine: You know someone who can read most file-format metadata tags and
could write a program that copies them to the Object filesystem level.

This is a one-time operation.
Now all metadata of all file formats is right there for you to work with:
**Right-click > properties.**

We have now "resolved" most use cases for embedded metadata.
We have therefore stripped layers of metadata "off our file".

> **Your metadata now stays with your data like embedded tags, yet is as clearly
> available, and easy to edit in any workflow or computing environment?**

Any file format.
Not just audio. Not just images.
Even video.
Even film.


# Stage 5: We need a player!

We've now reduced the differences of file formats on the level of metadata
handling and usage to a common denominator: The filesystem.

We've reduced the need or even wish to even use embedded metadata anymore.
Videofiles are known for their interoperability-complexity-challenges.

Let's imagine a videofile:

  * It's called "video.xyz".
  * You right-click > properties: There you go!
    * title, artist, year, etc.
  * Wonderful.
  * Even technical metadata:
    * resolution, streams, tracks, channels, encodings, etc.
    * even: "Created with libxxx-version.so"
  * You double click it.

A window opens - yes it says:

> "Sorry, can't play that file."
> "but I have a link to a compatible player (FOSS licensed): VLC"
>
> "Would you like me to install it and run the object again?

Just another metadata tag, like "player=..." or "decoder=..."

And if you happen to know the URL of a nice player or tool: Just add it as
metadata tag. Right-click > properties. Tataaa!

Your favorite player now stays up-to-date longer, because there are less
different file-formats to support. Numbers decreasing in the future.

File formats are resolved into "annotated and related data".


# Stage 6: Annotated and Related data.

Any annotation stored on the filesystem level: check!
Easily accessible via any tool of your choice: check!

Imagine, you could now move only the payload data of your MP3 or JPG to a new
Object?
Okay, you'd get 2 objects:

  a. One with only metadata.
  b. One with only payload.

  * Any Object can either be (a) or (b). Same-same.
  * And you can refer to any other Object in the metadata tags by default.
  * It's good practice to have at least "some identifying metadata" with
    just-payload Objects.

Now imagine your audio file is now stored as an Object like this:

  * audio
    - title = ...
    - hasCover = <image>
    - payload = <encodedMusic>

And your image file like this:

  * image
    - title = ...
    - isCoverOf = <audio>
    - payload = <encodedImage>

You get the idea?
You can annotate Objects - and relate them to each other.
In your File Manager. We should start calling it "Object Browser".


# Stage 6+: Relationships between media streams.

Still in your favorite "Object Browser", used like a file-manager with a
web-browser engine.

Still with our videofile: `video.xyz`

So when you browsed the metadata before in your file manager, you saw that it
had multiple tracks of mixed type: video, audio, subtitle, timecode, extras -
even other files embedded.

  * Imagine you would like to see a specific video track in that file.
  * How would you do that?
  * Does your player support multi-video-tracks?
  * Where's the menu option?
  * Can you search a video track by it's language metadata tag?

Imagine the video file is a Data Object.
That points to other Data Objects: video, audio, subtitle streams.

`video.xyz` has its metadata tags and references to "other objects", like:

    * video streams
    * audio streams
    * subtitle streams
   
Each of these media objects is also a plain Data Object that can be tagged.
Language, channels, speaker layout, and any other metadata.

You can now see the actual contents of your `video.xyz`:
Imagine a drop-down option, like opening a folder in your file manager.

video.xyz:
  - video1
  - audio1
  - audio2

If you like to remove an audio track, just "unlink" it.
Right-click > properties. Edit.
Or whatever UI metaphor your prefer to do that.

And same for the other direction:
You have another language for that movie?
Just drag-drop-relate it to `video.xyz` and you're set.

Of course, you can see and edit the language metadata tag on each stream Object.

Translating media containers to related Data Objects with metadata, may also
reduce the differences and needs for different container formats.

They would resolve into data-graphs on your filesystem.
Highly interoperable, and easy to annotate and search.

And now you can even "remultiplex" media files in your file manager.
And access any metadata like a pro - even without MediaInfo.
 
MediaArea might be the go-to team to hire for any initial metadata migration to
the Object filesystem level.


# Stage 7: Relationships.

Wait a minute?! Related Objects?
Imagine, it doesn't matter if a file has a payload or "just metadata".

A value can be any kind of metadata.
Even pre-formatted (XML, JSON, CSV, ...) text.



# Stage TODO: Storage locations.

Did you notice something?
No foldername.
No path.

A Data Object is "just stored somewhere".
Somewhere in a digital storage environment.

Yes:
  + There may be a filename.
  + There may be a path.
  + Now they're just plain metadata.
  + The Object is stored "somewhere" in your filesystem database.

Yes:

  * Filesystems have their own kind of databases.
  * Clever indexes to look up file and folder names.
  * And now any metadata.

So you can continue your workflows absolutely uninterrupted - as usual:
File and foldernames are common and popular defaults for new Objects.
As soon as you copy drag-n-drop your existing files onto that storage, they're metadata tags are set automatically:

  * filename=...
  * folder=...

And you can use them. Keep them.
Or edit them.
But now you can also simply assign "a new filename":

  * filename1=...
  * filename2=...
  * folder1=...
  * folder2=...

An Object can be in several folders at the same time.
It's just being "shown" in that context if you like.

It's all about finding your Objects, rather than moving them around in folders.
The foldername is merely here, because it's a nice metaphor that has served us (and still does) well.
Yet, it may become a thing of the past. And for anyone using an online cloud storage - already somehow is.

Where do you store your files?
Where exactly, in which "order" are your files?


# Stage ...: Mark what's important. For example for backup.

Simply "tag" what you'd like to have an extra backup copy of.
Made automatically.
Any backup tool will read the filesystem tags, and you don't have to worry or dig through config files or dialogs and settings.

Yes, you can configure it as complicated and easy as you like.

Imagine there's a well-supported and consistent "styles" for how to handle multiple copies, or extra-care for Objects tagged in certain ways.

Imagine it like this:

  * Right-click > properties > backup=yes

And another Metadata-Object like this:

  * Backup Settings
    * interval=daily
    * verify=hashcode
    * locations=...
    * other=...

And relate that Config-Object to your backup application.


You've now not only resolved any backup planning down to the filesystem level,
but also shown that config files may be resolved into Config-Objects.
