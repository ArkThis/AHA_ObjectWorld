# The Metadata-edit conundrum.

2024-08-22 23:37

When editing embedded metadata (in any file/data format), there are 2 possibilities, currently state of the art:

  a. The "original" (=previously known) filesystem timestamp is honored - and *kept as is*.
     Even after editing (=completely rewriting the whole file itself).
     This is literally a completely new copy.
     Of the "original".

  b. The modification-timestamp is (properly) updated to "now()" - to represent that an edit has happened.

From an archivist's perspective, this feels like a catch 22.
It produces either a metadata-white-lie (a), and preserves the date-field abused as "creation date-ish". And if one wants to log-and-document that the file has seriously been changed/edited.

This is professional and proper way of doing it right now worldwide.
And there's good reason for that:
The way the basic (=common) filesystem "documentation" functionalities have not really been kept up-to-date since the late 90s. The last major "jump" in filesystem "user empowerment" was the 250+ full-charset filenames in Windows 1995. Wow. That really changed the world.


## What if there were other options?

  c. There are dedicated metadata fields like:
     * date.creation
     * date.modified
     * date.metadata.edit

Also on the filesystem level.

The technical implementation for this already exists, is a 20y good-old POSIX standard - and already available on most GNU/Linux and MacOS environments. Backwards compatibility most likely ranging back about 10 years. So old programs may deal with it, too. Considering to back-port and add extended file attributes as default, this is very feasible.

Low hanging fruit so to say.

Now imagine, this opens the possibilities to:

  d. Add any annotation key=value pair of arbitrary meta/data?
  e. Regardless of the underlying file/data format?
  f. Handle most common DB-requiring situations with basic FS functionalities, tools and APIs?

We are riding the very wave of this paradigm shift in the way "thw world" handles "any data": converging on a common, modular, orchestrate-able toolbox of foss engines. Very scriptable. Very scalable. Very necessary.
And a lot of fun!

It actually transforms our current way of "dealing with computers and data as files" into "a bunch of kids with heavy gear and a good reason to improve ways of doing data": From playmobil to lego.

If we like to keep up with our "collective memory data-mess" that keeps piling up, we need to take a leap.
The cool thing is: That leap is actually pretty well-documented and well-charted territory for more than a decade now: so we can actually make use of that already.

"The BIG ones" have already figured it out - and are crunching and storing "their/your" data in very differnt handling paradigms. Literally comparable to puppet-mastering a bot-net of services and users.

And "data" literally is treated like a morphable liquid.
Regarding storage *and* annotation/relation for search-n-query.


## Key (field) names?

Of course. This will be as clean-and-dirty as XML and JSON for real.
However, the mere fact that it's always accessible as plain-text as basic filesystem data - with cache/indexers expected in place by default, I propose that it may not matter "that much" to keep any key/value pair as-is (as bit-proof) as possible unless you know explicitely what you're doing.

And if developers/(code) libraries respect that, I don't really see any interoperability problems.

I see a bunch of "clever" options to implement data-lensing functionalities.
If they are designed in a "works also outside of my system" easy-portable (=share) way, like "profile.conf" files: Different meta/data-dialects may co-exist.

Yes, this as-is collection of key/value whatevers may feel noisy and untidy at first, but considering that any application has "a good reason" to do it their way, interoperability is still very much improved:

**Simply, because any key/value data can now be handled equally, in plain-text, bit-proof default function**

In my opinion and experience, it really handles very much more harmonizing to use the filesystem for that - than the current "chasing the next meta+data migration" (funded) project. aka "state of the world-wide art".

Key lookup-lists and documentation (Wikidata? Wikipedia?) may very much improve the UI-friendlyness I assume.
Input-suggestions should be doable with basic 101 of index/cache setups.


## What now? I'm busy. Make it quick.

What if we GLAM communities (for starters) simply agreed on something like:

> "Okay. Let's take extended file attributes as serious now as "long filenames with full unicode support" across different computing environments seriously."

We've seen it happen from "DOS 8.3 ASCII-only" file/folder notation - to 250+ (long filenames) in mainstream computing since 1995: It can be done. It takes time.

So then in professional small-mid-to-large-scale GLAM environments, the exchange of "annotated (file) data objects" by copy/pasting "selected objects" - using a basic file manager.

This simple decision will remove the need for 99% of the following use-cases:

  * Use Excel (spreadsheets) to annotate your data (files)
  * Deal with file-format embedded metadata issues, libraries, papers or decisions.
  * Use any DB to store key/value data (yes: sqlite counts! :P)

And provide a set of basic tools and environments to handle annotation/relationships out-of-the-box.
Any application just builds UIs on top of that.
This makes data really interoperable. In the spirit of triplet-RDA ideas.

**This will save you so much time and worries - and bring back great fun and reliability to Object Handling!**





