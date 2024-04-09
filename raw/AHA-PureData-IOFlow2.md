2023-12-15 21:22:29

# AHA - Working with Data Object Flows as in `Pure Data` (pd).

After having applied the following transformations from conventional "classic" 80s Files-in-Folders Data Layouts - and resolved, translated the Data, APIs and Applications into a working Object Data digital paradigm.

  * Support metadata already supported right now preferred from the filesystem level.
  * This prefers tags available on the FS-layer, over eg "embedded" - or from another database/XML/anything.
  * Relationships are properly supported as:
    * Links to other Objects (even remote pools)
    * Any kind of "possibly-referring" metadata
      Like a URI.
      Even terms of vocabulary lists.

This already relieves all applications and developers - including users - of the choice of a file-format to support annotating and working with data graphs directly over API UIs or CLI.

The availability of functionality like "keep meta with data as Objects" on any basic system is extremely inviting for any developer to make use of it.

It's like having a heating and a kitchen - and rather freeze and be hungry instead of making use of what's there?

If I don't need to worry/think about which database-system to "build on" and deploy and support: No. I'll just use the default filesystem. It just works. If you need it faster or different: Apply some other "transformers" (tools and UIs) - and have it your way.

Caches and Indexers are easily handled, because they've become "so common" that it's just another "basic admin lesson: data index-and-search".



# Pure Data: Visually editing Object Graphs.

If:

  * Any current data format can be broken down into a different set of
    related Objects.

  * And any application programming code is depicted - and run "as normal"
    from its Data Object (on FS-level) structure.

  * This means, Data Objects can be actively running code.

  * If we now map a generic visual programming language (see PD), and use that to "edit" (and interact with) our filesystem Objects.

  * Accessing and working with "Meta" or "Data" is same-same, and very clear because all (technical) properties of any "Data Object" (eg Movie, Image, Song, Construction Plans, Document, etc) is represented in the ever-repeating, all-familiar way:

> "An Object that has a meta and a data part. And meta may be pointing at other things"

And it just works.
From ground school-kindergarden to building "space station 11".

There is no more difference between working with files - and working with Objects that are the components of run-able applications/programs.

Since all Object Classes and methods are visible - in any way you interact with your "File" Objects: Even visually in 3D or VR.

Since you could attach and use any metadata to any objects, if one comes up with displaying options for Data Types, they'd probably come-and-stick with some Objects sooner or later, and then be distributed from there (if you like to) - to other Objects of the same "type".

Types are at first mind-wards compatible to MIME type-thinking.
Later on, "types" of Data goes into "phrasing Data properties" for related, weighted graphs. It is neither expected nor desired to always receive "the same correct answer".

Because with a complex datasystem, computing answers must at some point become fuzzy- or otherwise either take way too long - or be plain wrong in the end. The complex considerations, variations, etc etc - at some point don't pay out in the end, considering the "costs".
Just live with the fact that it's probably right, but we all know it had to make assumptions on the way.

There's always the "skip, we know better" button in my systems.
(Ich bin alt genug und weiß was ich tue-Knopf)

So, if I can store and handle my day-to-day data conveniently using Data Objects for storage of "payload" and my private-and-professional database/query/search/restructure needs.

99% of whatever is needed as "engine" functionality is provided by the local filesystem. And since that filesystem scales and works on large online networks, too and supports merging any kind of pools and types of data.

As long as their "accumulated" metadata and structural (relationship/links) information can be used to query "sense out of them". Or "select" anthing in a certain order.


# Let's go inside and play.

Now that any kind of Data can be handled and dealt with all the same:
By a common, yet highly personalizable and variable interfaces.

How?
As simple as we see now that "if we want and have the code" to support eg "FAT32" or EXT: it's there. It's done. It works.

And any other "application" is browser-engine based in most cases.
So anything you could do "in a browser" - or as an 'Internet website', you can render your Data - as web-app.

This means that any functionality you'd have locally, you could also have remote. Using identical code.

This already is the case:
Some applications you install on your home computer actually are browser-engines running "web code" that feels like a locally installed application. It's just "slightly" *cough* larger than an average other application of the same type/kind.


## Streaming data between Transformers

Imagine you'd like to use a certain functionality of your "favorite old program for doing X".

If that "old program" was already running as Holodeck process (\*)

(\*): Holodeck Process: Just an application being executed on runtime from the code/instructions/data in their Related Data Object Structure. Actually the same thing when binaries are executed nowadays, but imagine it like this:

A running process is not "one thing that uses up memory and CPU", but:
Data (compiled) source code doesn't need to be linked to "one executable". Any part of the code itself is "run-able". Like Python library code is written to have "active" parts when being "run" - additionally to its library classes, objects and functionalities.

So if program are written with AHFX systems in mind, any of their parts should be copy-paste-able, like querying a subset of "files" to copy to another "folder".

This breaks down data processing of any kind into "any computing languge function/method/property" can be depicted visually as pd-box (node) with connectors. Simply literally applying the "Pure Data" metaphor on the filesystem level.

It all becomes alive then.

As we see in "pd", any "box" seems passive at first. Think of boxes that hold plain "values" (strings or numbers), then boxes with hold "a block of text" - and others that even contain "binary data".

Any you interconnect them - and have active components that transform and forward any data you "feed" into it.

Thinking in the AHFX design, "data to feed" itself would be "another box" - if it's like "a file" - and group/query of Objects alongside a "folder" metaphor. Streaming data would simply be enabled by "referencing a source of meta/data to "something else".

And if that "something else" can be read (meta and data) - it can be "used" as input - or other socket to work with.


Having meta-and-data Objects on the filesystem with a pure-data interface and functionality to design active "coded" Objects.
Coated with run-able code.

Source code text is broken into individual, related Objects on the FS-level.

Imagine running the "Inspect Website" functionality web-developers know from any modern browser: you can WYSIWYG-interact with the rendering of your data-and-instructions.

So if there's a functionality "you like" - you can literally "rip" it out of any Holodeck application: By select-copy a certain button, then "pasting" it into a "Clean" (empty) "Object-Space" on a filesystem.

The program code knows (by relationships, and attached queries/code) what its dependencies/requirements are to work. This is the same code used to throw exceptions until it works.
I guess a compiler could figure out which parts of code are required to function standalone (=without warnings, when cut out).

Since we're not "cutting out parts of text from different files/folders", but the code is already stored as "related objects", like each Class/methods stored as separate Objects.

If it helps, imagine saving a source code object:

  * 1 Object Class definition (properties, methods, tests) = 1 file.
  * 2 Objects = 2 files, 3=3, n=n and so on.

Now split up again:

  * 1 Object Class defintions:
    * Object structure declarations (like Java "Interface" idea)
    * Class Property definitions : 1 related Object
    * Class Methods : each one a related Object

So you could cherry-pick even which methods a class "has access to". Because since methods are "related Objects", it's trivial to use "Other related Objects" that match the requirements (Interface definitions).

These mechanisms can be used to "know" by-copy request which code-and-data parts (=All the same FS-default Data Objects. Just different types with different information stored).


If the Holodeck-FS performance allows to strip "the pure encoding" as plain and raw as possible by default - and move anything else to either the "meta part" - or have as related Object: What would remain is in many cases the "Data Payload" of most objects is "pure, somehow stream-able" data.

Because any outside structure has already been resolved onto the filesystem level.

If we break down programming code components into filesystem-objects, and keep code-and-programs like that even until (or during?) runtime: Interacting with computing machines would become "native" in its own way. Interoperability by design.


# Where's the catch?

Overhead.
More spaces, more computing resources.
Yet, however: it may actually be so, that by providing the "real basic" functionlity now on the FS-level, and shifting balancing and performance off to "CDNs" - Content Delivery Networks - and Indexer farms, and so on?

For large-scale processing: currently working worldwide, and consuming fantastillions of money, time and lives per second. To watch cat-porn-on-youtube-on-a-so-called-smart-or-at-least-mobile "device".

For fun.
So we're already paying for that in one way or another already.

As seen on Linux-vs-Windows: Orchestrating applications and packages made things more stable, interoperable - and consumed less resources.

However:

  * Converting text-based metadata from file-format (or database) onto filesystem level makes no difference in terms of data-size.

  * Converting numerical data to strings "as the new default":

    There was a time, when XML was new, and the choices had to be made, which data is "worth" blowing up in filesize and computing requirements, for the sake of having the data in "TEXT" form now.
Only so we humans could at least have a chance to work with it.

And it was worth it.
Look at "The Internet": HTML+CSS is also "just text" - and requires significant resources to be made "active" and render websites and their functionalities. And looking good and fast at the same time.

We already have that.
Running on hardware we force onto small kids in kindergarten already.

Translating popular data formats, and application (code trees) into active Objects may increase storage requirements, but due to better handling and design of its structure, it may be better to use - even if slower.

Simply by the amazing advantages given by the options to work with "related object graphs" without the currently accepted default-by-design boundaries anymore.



# No need to "sort it out" before.

Or do you think "The big cloud storage providers" on our world right now are ever planning to require you to "clean up your data", or use a given standard?

> **The absence of defined structure can be surpassed by direct-addressing by cascaded queries - in due time.**

It does make sense to agree in using "common terms" (or any other form of common reference/identifiers) to relate data constructs which originate from different sources - and "realms" (times, culture, possibilities, style, etc).

However, it is not necessary anymore to define a fixed structure "where" in a "tree" or hierarchy - a certain "information" can be found.

Is this value for "language" for the whole work, or just parts? Like individual audio tracks, etc.

Since the Data Objects themselves literally "self-describe" their structure - any structure, any relationship they might have with each other - it can be well described on the plain filesystem level.

Annotated, related Objects.

Instead of trying to force order ontop of "the world in data", that time is better spent simply "waiting" until a Holodeck query is returning the desired "answer".

Instead of having to implement field definitions, standards - and mappings from one to another: rather come up with suggestions for "field terms" - and a cataloguing-style handbook, with different styles for different users.

All co-existing on the same Object Types they interact with and create.


# Real world examples


## Self-showing JPG.
## Self-showing "Movie".
## Self-build-and-installing Blender
## 



# Pure Data binding to filesystem API: Example

It should be possible to create pd-nodes for interfacing with the Object Storage API.
If not possible to implement it natively in pd yet, a fallback option may be to use filesystem fifo-pipes.
Maybe not the fastest way, but would work as expected.

Then adding means of accessing the "preferred data query option".

So you could for example:

  * Create a node "object".
    This would have been "a file reference" in classic times.

  * Select, using a data-query widget - any data in your storage pools.

  * Interconnect and annotate their structure as preferred.

  * If pd has a way of loading and running Python code as node, fs-stored metadata code would be shown as GUI option.
Full control over input/output transformations.

These are actually very basic things, very possible to make.
Because the libraries exist, so we'd merely need to make thin wrappers to connect to the filesystem.

Of course Data Objects can be marked executable -and simply run directly.

This allows any code already existing - any programming logic - to be saved as standalone Object.
You run it, providing the "parameters" (CLI arguments, or API calls and bindings).

If you adhere to AHAlodeck conventions, you should easily be able to run standalone Objects also in "compound": Meaning, you can run "a program" - and it sub-executes its Object "lego" blocks.

So your filesystem now offers you to what-you-see-is-what-actually-runs-in-code as yet-another data object group/graph. Nothing other than your other "data things".

They may have different list-icons ;P

Let me think this through...
Any feedback greatly welcome!
I'm proposing means of having codecs natively on the filesystem-level.
If you want to copy your video (and player), you simply select to auto-copy related codec-Object with it. If there are multiple OSs or flavors available, you get to choose which ones.

Yes.
You've now attached a copy or link or reference to VLC, ffmpeg or many other FOSS-allstars.
And if your filesystem is AHAlodeck, it may suggest to deduplify these references to a common copy - to save space.
And save time.

Awesome.
Easily possible to substitute the codec Object with a download-link.
This could even support Arch-Linux like recipes for building any application on the fly. Adding nix-os flakes, you have the perfect self-replicating options. Never worrying about "will my data be there and still work when I need it?".

Any long-term sysadmin knows how to crunch those requirements.

When thinking about possible abuse of these new features, injecting malicious code or data:
Considering simply using the same means of "which data source you trust for software and updates now?"

Just because your data pools can interconnect with literally any other pool on the planet - seamlessly.
Simply accessible by a query-prefix like `pool0`. As tag.

That's it.
Yes, this is how you map a network drive - of *any* kind - from now on.

Query:
(should be sparql? I don't know it yet, so I pseudo-code-sql here)

> select * from "my-tag-for-peters-data" where date>2020 and \*=lena

Or:

> select * from . where data<2011 and \*=xbloome

Or:

> select video,audio,subtitles from . where title="My Movie!" and date<1977 | ffplay -

Something like that.


# I'm not sure I've made myself clear.

Have you fully realized that accessing your own data and *any* other data anywhere on the planet - in any system would now merely get a "longer prefix string" tag.

Which is commonly aliased as needed, exactly as done in programming languages with fully-qualified domain-name for libraries.

And you never have to worry about if you put it in the right folder.
Or if the filename may cause problems or persist.

Your data is now safe.
And way more flexible than it was before.
The filesystem now may be given operating system capabilites - or at least code Objects that can be used by the Operating System to natively interface.

Anyone can now see, use and reconnect data handling programs - as they can now be copied and re-used as pure-data patches. These engines are stable and solid and designed to run on now considered "ancient" hardware.
Therefore they have very little hardware requirements and run faster -or merely consume lower energy.

If pd could handle video in realtime - only limited by the hardware, considering full-HD and even 4k is done on RaspberryPi hardware these days.

You can literally hook up any number of audio Objects with video Objects or subtitle Objects:
Save that relationship reference as a new Object (or -graph).
You now have your videofile.


I'm serious.
By moving the decoding to executable Objects in our data pools.
Any data transformation can be done by plain filesystem Objects.

By having meta+data, those Object's interfaces are self-describing, allowing Objects to auto-map interface connect in advanced future versions of AHAlodeck.



# This goes even further.

We have now broken down any container format into the data "blobs" previously contained "wrapped up". Embedded things.

We can now de-embed not only the meta, but also the data.

This is not limited to any file-format layout.
Any data layout that can be depicted in an object-oriented way in programming code, can be stored - and used - like that on the filesystem of AHAlodeck.

By merely providing means of directly "running" any Data Object - and by piping ins-and-outs of these Objects in a new Object (or -graph).

Funny thing: Kids love these kinds of puzzle games!
And imagine you can do anything you can do already - but nicer - in all environments supporthing AHAlodeck-like features.

In order to be able to simply continuing "business as usual" with your tools - and transitioning over to Object Data handling, simply putting the operating-system on AHAlodeck (MinIO?) - and piece-by-piece write filesystem libraries to support running code from Data Graphs.

Why not?
An Object Graph "call" could somewhat easily boot and quick-boost itself like this:

  1. Init-Object is being "called".
  2. This means the Init-Object may run code.
  3. The Init-Object may now manifest any data itself - or pull in any relationships/links.
  4. And hand over the run-pointer to them.
  5. Iterate as desired and preferred.
  6. Retrieve "results".

If that works, imagine magnet-torrent links - supported by public library/museum/archive data spaces. Full Object Storage and feature set. Publicly available to anyone.
And it is the same system the GLAM-community uses themselves, if you like.
There's plenty of other UI options.

It's actually quite fun and easy.
And has a stable interface - of your choice.
Long-term and premis-able by design.
Linked-open-Data of course, too.
Wikidata-plugin by default.


So audiovisual data would become not only self-structure-describing and annotated Object-graphs, but also self-decoding executable, by having links to required "processing Objects" (AHAFX Transformers).
Allowing to run (=trust) these Transformer Object(-graphs) is based on your profile-preferences which code(-source) you trust.

Whenver you download-and-run any file these days:
The same common sense would be applied to "when to trust" your digital source.

Then, these Objects would be tagged (signed?) by your filesystem/OS on incoming event:
Anything copied from one pool to another get's a signature by the transactioneers (optional).
Therefore it's possible to verify digital signatures on Data blobs (same as repository managers already perfectly handle since 1980s) - same engine here.

So by being a bit more cautious about your "program sources and service providers", you have the same level of control over who runs code on your machines as you do now.

It may be way easier to implement that in a comfortable way on Object Storage, by resolving signature/key/etc sidecar-files or database-entries to the metadata part of the file/payload Object.

Same goes for hashcodes, btw.

So only when an Object has a "you-approved" signature, it's allowed to run.
All these systems exist. They were built for very powerful restriction/access declarations.
Yet, I guess you could easily make a new PAM module to handle "you-approved" rules?


# Similar to the animated european "Es war einmal das Leben"

Did you realize that by being able to depict so many new "new basic" functionality with simple wrappers to the filesystem API and libraries, a pure-data "project file" would be no textfile no longer.

Best HowTos provided by GLAM communities all over the globe!
Great fun!

Where's your app from?
The library, of course!
Thanks everyone.


Think of it as this:

Each pd-Node being saved - by the ones you see/you're working with, being instances of the underlying data class.
So the filesystem can simply cache/hold/suspend a certain level of edits-before-save - and on top of that has git-standards on all by default.

Now each instance of an active (=executable), running its binary/main code, or semi-active (=Python as meta), or even arch-ether by manifesting whole software environments out of what feels like: thin air.

By having signature-and-relationship-and-filter-policy engines at work all the time, any data processing literally breaks down into a mixed-level "pure-data" processing of all kinds imaginable.

Yet, by having each pd-Node as mere plain Data Object - fully portable, and self-relationship-aware to pull its requirements.

> **This reminds me of the animated series where I learned about the human immune system and blood compounds**

Implementing these methods on the common filesystem/OS orchestration, would allow an immune-system kind-of digital environment.

In both directions.
New "attack vectors" will become possible.
However, they already do exist already - since any technical requirement is already present.

Since the Data Objects can be almost arbitrarily inter-referred and annoted about and to each other in any ways, a stable-low-level common implementation for letting the `operator` decide and edit whatever necessary or desired.
Anyone given access of any kind to such a machinery or mechanism, shall be considered a good operator.

So that's actually some kind of data immune system for you.
That's the starting point.
Basically, it's completely able to depict the same level of "security" as we have now.
The tools and workflow slightly change - yet in almost all cases, things get "more native" with the new tech.


## A simple filesystem 

I could write books about things related to `file systems`.
Filing systems.
Files-in-Folders.

That's what most of all of us know.
And then your cloud has stuff somewhere, and you just `search` or `filter`?

I want to move on to meta+data by design and default.
Anywhere.

It is time to say goodbye to the good old "files-in-folders" data-storage paradigm idea.
It's over.
It's hurting and requiring "special code-care" in so many corners.
Please, let it go.
There is no need to separate meta from data anymore.
It's like breaking down the Berlin wall once again: Now for meta+data finally re-united!

I have spent time to realize this change, and I know it's not an easy one.

Just "save".
Just put it in your own cloud.

And I have all sorts of plans of how to turn all our world's computing into the most amazing proof-of-concept that could very well already be used productively (soon after), since all the components required exist in production stable implementations.

2023-03-20
