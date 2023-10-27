# Object Actions

Feature: Commandline-completion-like Object-Handling offered by applications
installed.  Or in GUI terms: A drop-down or pre-populated selection of
meaningful "Actions" that can be performed on selected Data Objects.

An application can add routines and profiles the the AHFX user-land layers:

  * Example video-modification profiles, that show up when you have ffmpeg
    installed.
  * Example playback a video that has configuration instructions for a
    media-players: When having MPV or VLC installed, you now get
    video-filtering, or other av-specific new options in your context-menus.
  * A bit like installing additional Thunar actions.
  * Since the Object Browser I'm suggesting is technically a web-browser, it
    can be made to fit whatever needs.
  * On the commandline level: Exactly like CLI-shell-completion. An application
    package comes with information about its parameters and presets, and once
    installed these new options simply "show up" where expected - or when desired.


## Feature/Task Profiles

Complex tuning functionality and parameter-settings can easily be stored either
as a standalone (reusable template) Object, or as a copy of such a template,
directly as metadata with the Object.

For example: If you right-click a videofile, and have a proper AHFX-compatible
player, you may simply edit the tag "audio-timing-offset" (or so) to "200ms".

Now you've fixed the audio sync issue.  For players that support that offset
information.  It would make sense to agree on a common set of properties here.


This "setting" can be stored as a metadata-only Object, linked to a video
Object.  And you can have multiple copies of such Config-Objects - with
different values and different relationships.

Application startup presets (the usual batchfile use-case) may be covered by
creating Startup-Objects: A Config-Object Graph.  Well, actually a fancy
version of the usual "Installer" or your favorite Launcher Icons.

So you'd have different launcher icons that call the video with
whatever-presets in the right application, that is AHFX-compatible - and you
can easily handle running video-effects in real time.


## Advanced "actions" 

These "actions" are attached as metadata (=instructions/configurations) used by
external applications, but easily executable by right-clicking, and selecting
the attached "presets" (profiles/even scripts).

An Object can either accumulate Actions as attached Metadata, or as reference
to other Objects (that *are* the referred profiles/scripts).

Imagine you right-click any media file:

  * Convert to ... mp3, m4a, flac, wav, ... etc etc.  Available options
    depending on which applications installed default actions for certain file
types (MIME? suffix? URI? support)

  * Compress as ... zip, 7z, tar.gz, etc etc.  Also: Available, depending on
    which applications installed default actions.
    
These features already exist in modern file-managers, but the difference is:
These are *not* stored in a local registry, *not* stored in any application's
config somewhere, *not* stored in any kind of proprietary application-specific
database. No.  Any necessary information is readily available down on the
filesystem level.

In a standardized, very simple format.

So if you copy a media Object to a USB-Stick, then "import" it into someone
else's collection/harddisk:

  * Simply drag-n-drop it.
  * And either choose or have configured defaults for how to treat Object
    Relationships.  (eg Recursion depth, or "how to 'deflate' certain Objects
    for better transfer" (more on that in another chapter)).
  * On the receiving end, you now have the profiles attached to the media
    Objects, and the question is now how you get the required applications to
    perform these actions?

Depends.  There's multiple ways to achieve (almost) the same result in the end.
But with different performance and options. More on that later.

So your friend receives your "Object Graph copy". Deflated. Meaning: It did
*not* copy the applications, but attached placeholder-Objects which refer to
"where you can get the App" - or even ArchLinux build recipes. Anything that
allows (semi)-automatic installation and setup to concur will do.


## Deflating 'heavy' Objects

Mainly for data exchange/transfer.

When copying Objects, it's more than just copying "a subfolder tree of files".
It's "cutting out" a Node-Subgraph. A stub.  Easiest way of doing so would be a
simple "recursion-depth" option for any copy tool/function. Easy.

Maybe update IDs of referred (local) Objects to either an Online Placeholder,
or generate Stub Objects. Or leave the references as-is. All valid.

Now, what if?: Imagine, your sub-graph was able to "heal" itself, by generating
(on-the-fly or pre-generated) placeholder-Objects when being "cut out". These
stub-Object(graph)s would allow to consist of any information/layout necessary
to rebuild the "environment it was copied from" as good as possible - and so it
makes sense.

A bit like cross-platform design - and the standard, common-denominator
functions.

Different types of Objects could specify their preferred set of "Cut out
Options/Preprocessors". Simply attached as Metadata.

Examples:

  * Locally Installed Application: Stub may contain: vendor/download website;
    Link to Wikipedia; Link to HowTo; Just the title/name of the application
    the stub "represents".

  * A "portable App" Version-Copy: Or simply zipped the files needed to run
    that program?  (config and settings are attached to the Objects. Not
    required here. Good practice: Still include sane default useful examples)

  * Web-Application: Simply a link (with runtime arguments/parameters support).
    An Object could simply be double-clicked and bring you to a website that
    tells you more about "IT".

  * APT - GNU/Linux Supporting apt:// links or flatpak, or AppImage, etc etc -
    whatever works.  This is simply a link as name=value field of an Object.
    And double-clicking (or running it on the CLI) is all you need to install the
    prerequisites to support the desired new "Object Actions".
    
So, from zipping to "just referencing it, download/install it yourself":
anything is well depictable with the Object Graph metaphor.

Alongside die idea of the OAIS model:
Any SIP/AIP/DIP can be "materialized/unreferenced/real" as desired. Defining at
what recursion-level and Object-Types which level of "deflation" for cutting
out Sub-Graphs for preservation/reusage.


### The main outcome is:

You don't have lose ends in your "cut out" Object Graph copy.  You have
de-materialized (or simply compressed) the desired target Object to something
that is now "less heavy" (in data size), yet able to help assist in
(automatically) re-creating the original computing environment.

> **The config/presets/scripts are with the Objects.  You don't have to set any
> "paths".**

Your Data Objects (eg media files, documents, images, construction plans,
website links, ...) are all just floating around on your digital storage.

You just:

  * Locate whatever Object(s) you want to work with/on.
  * Right-or-Double Click on the Object to run its (default) Actions.  Keyboard
    modifier keys may be used to quickly access ~3 preferred Actions per
"Object-Type" (*).


(*) Object Types can be (complex) Semantic-Graph-Queries to your Filesystem.
Accessible by a user-defined Alias Name/String.  Of course it makes sense to
start mapping existing "Filetypes" to this.

  * MIME Information (strings) as name=value tags.
  * File suffixes (! - yes, plural if you like) (strings) as name=value tags.
  * Index these tags to quickly access your Objects "in a more classical, yet
    elegant way".

If you have enough "Digital Object Space", you may even have "the executable
binary" as attached metadata, call-able by a defined Action.


### Heavy vs Light Objects

Heavy Objects usually contain "the real thing" (of whatever data format) as
their Data Payload. Light Objects usually consist mostly of individual strings
and numbers. Sometimes a few kiloBytes - Megabytes if you go crazy, but still:
lightweight, compared to GB/TB of movie or scientific data.

Each Object can describe ways for deflating it.  Similar as it is done in
Object-Oriented programming: An Object "Class" can define how it can be
incremented, listed, formatted as String, etc etc.

Apply the same logic to an AHFX-compatible filesystem: If anyone comes up with
a new "Data Type" or functionality - they simply add these "infrastructure"
Objects and metadata attachments when creating/publishing it.

So if nothing particular is defined, you'll simply have a "compress Object(s),
select depth/conditions" default Options. Your OS or applications you access
your Data Objects with, may (if you allow that) "write" Actions to your Objects
whenever you "touch" them - or tell your computer to:

>  "search all ... and apply these awesome new Actions to them! Go! Run! :)"

In some cases, "heavy" Objects that exist and are used and dealt with today
already, sometimes could be made "lighter" if their information complexity
could be "broken down" - or "resolved to" an Object-Filesystem-aware version:
An annotated Object Graph.

Audio/video/film files: A digital film would be a large graph (with each frame
being an individual image file, plus audio, plus metadata, ...).  But when you
consider that *your whole data collection* is now "just a large graph" of your
Data Objects: Your "large film" ain't so special/large anymore.  It's just more
"serious" about its "must-have" relationships when being accessed/read or
copied or modified.

That's all just "common annotation practice" in the AHFX world.

Think about it.  A digital movie file is:

  * container metadata
  * video track(s)
  * audio track(s)
  * subtitle track(s)
  * data track(s)

See those as related Objects. The relationships described and annotated. The
(non time-based) container metadata simply written as name=value on a
meta-Object. Another "stub": The one you click on to open *that movie*.

If you even break the AV streams into sub-graphs when annotating chapters: You
could either have the chapters as time-based metadata text, or literally
cutting the referred "parts" (chapters) into stand-alone sub-graphs: New video
Object (graphs) - that are referred to a playlist-like structure in the
"clickme" stub "entry" Object.

Or one could just segment a large/long video track into sequential Objects.
Each Object can have its own hashcode attached (name=value).  A bit like
"slices" of a frame in FFV1: You may slice large Data Objects - and relate them
to each other.


### Can I rely on it?

This is a very very very important question!  And one if not the most important
feature to sign before committing to it.

Any implementation has to be fully reliable in handling payload and basic
metadata actions. Like a common "Basic BIOS" set of methods anyone working with
these digital Objects can count on.

If the basic functionality of handling and keeping nested name=value tags in a
performant way, is key to de-errorizing existing data-processing procedures
known to be error-prone:

I mentioned before to "explode" media files into related Object Graphs - and
then further to "slice" larger media tracks. If the filesystem can reliably
handle "averagely sized payload Objects, with a reasonable amount of
relationships and tags" properly: Your "previously heavy" media objects become
"not so special anymore" from the point of view of that new filesystem.

It's just another graph with average-sized-and-average-properties. Just a
different set of applications and Actions available.

It's a bit like logarithm in Math (as I understood it): I was told it "brought
down the complexity of a certain mathematical operator/function down one level
- to make it easier to grasp and calculate.  For example: multiplication
becomes addition. power becomes multiplication. etc.

An also important and interesting question is: At what point of
references/annotations will the filesystem get bad performance?  And can it be
improved by Indexers/Caches - or more "space"?

The important new feature of an Object Graph filesystem used in that way would be that certain "special" (=not so commonly supported/considered/tested by tools/applications/specs) cases simply become "not so special at all" anymore. Therefore, being processed within the same "normal" range of functionality in any computing and even manually-processing environment.



# So what?

A digital "film" copy, and a videofile are actually not really different at all
modelled as "yet another related annotated graph of average-plus-minus payload
size" in an Object Graph filesystem. The filesystem *is* your database - *and*
your data storage - and you don't really "feel" a big difference between "meta"
Objects (metadata-only, like a DB- or catalog-entry), and "payload" Objects
that have the larger content.

It just works.

This means, that *all* handling of those Digital Objects will now profit from
running on stable code. Anywhere. By the nature of its technical design. Not by
additional code.

