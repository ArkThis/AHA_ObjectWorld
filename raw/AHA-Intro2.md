# Another introduction:

So I assume we all know the following workflow:

  1. You want to do something on a computer.
  2. For example, design a flyer.
  3. You web-search for images, fonts, templates and examples.
  4. You download or otherwise use those ressources.
  5. You save your project files.
  6. You publish the final results.
  7. You sware to make a proper backup plan - next time.
  8. You hope you'll find it again - in proper shape - when ever needed.

In the end, you probably may know the case of "you find *your own* stuff easier by asking 'the Internet' - than trying to find it in your local "collection" (of copies somewhere. Maybe.)

Sounds familiar?
Or am I just getting too old for this?

So why do the "elderly" computer users feel that the kids have it way to easy by simply "putting it up in the clouds". Handing it over to the Internet-Lords we follow and obey, sometimes annoyed by actual disruptions in service - or simply being disconnected.

Just put it in the cloud.
What if that cloud was under your control?
What if "that control" didn't mean you need to become a system-administrator?
What if you are one and want to simply have fun with computers again?

Just put it in the cloud.
And I'm suggesting that that data-storage-engine is based on an Object Storage with Indexers and awesome UIs.
And running on your local environment - seamlessly interconnecting with online servers.
Self-set-up or paid-for services.

Putting it in the cloud is now also saving it to USB or SD-card or harddisk.
We didn't care which blocks were allocated howandwhereandwhy - as long as it works.

Never having to come up with a clever folder-structure and file-naming convention.
Never having to implement any form of file-format-specific metadata specifications.
Never having to worry about "the file format" again for tagging anything.
Never having to think about which application to work your annotations into.

Right-click > Edit.
Or: API and UI of your choice.

Your family data collections are now simply stored in different pools with different backup-plans.
All taken care of by your new filesystem.
Like going from 8.3 characters over long-filenames now one step further to: Data Objects.

This is not yet-another-filesystem.
I'm merely proposing an orchestrated structure for handling Data Objects to serve collection-handling needs.
As this will benefit anyone who now has-and-uses any kind of digital data.
From home-use to professional and beyond.

Just put it in your own cloud-like data system.
You query, master and setup like a pro.
It literally is like playing lego - using a `pure data` (pd) interface for starters.

Imagine Minecraft playing your real "files": Now juggling them around easily, interconnecting and annotating - and using them directly from there.

Who wouldn't want to give this a 12 months paid project funding?
For a proper small A-Team to build it.


# Short:

You could simply web-search your local assets as well as you can browse youtube and a search engine.

Noone's ever going (or ever had the idea) to clean up the Internet - just imagine: Sorting out Youtube's collection in a file/folder+database system.

Good luck.
Of course it'd be technically possible, but I doubt that's how it's done.
Especially not, after having read parts of the documentation and white-papers that form the base of FOSS-licensed reference implementations.

Since the mid-2000s, HLS-Storage systems were already in use in larger data-centers. And they spread out from there: Object Storage being the term under which I find more modern (late 2010-onwards) implementations.


# That was not short.

You could simply web-search your local assets as well as you can browse youtube and a search engine.

Noone's ever going (or ever had the idea) to clean up the Internet - just imagine: Providing Youtube's collection as web-service, based on a file/folder+database system.

That is not how they're doing it.
And thanks to white-papers, we know it.

There would be no more need to have a specific "photo" or "music" or whatever local application-specific database, forced in some metadata layout - requiring conversion and import/export capabilities on all ends.

And mapping and code to be written whenever one was interfacing to another.
This is still the case today.
Metadata and coding-standards make it at least less painful to hack interface connectors and converters.

This is not necessary anymore.
We can simply skip this.
And cherry-pick the best.

**By agreeing to a common filesystem that has a proper place for metadata and relationship-handling. Graph-optimized. Thinking Wikidata on your local and network drives.**

As taken for granted as "naming a file or folder" is now.

We had 8.3 characters (UPPERCASE only) - and switched in no-time to 250+ - even allowing spaces. O.O

Anyone can feel that it's a clever, but faulty hack:
Spaces or certain special characters in filenames: causing problems still.
Since Windows95 - that's almost 30 years with "long-filenames.whatever".

It's time to move on.


Current state-of-the art mass-content asset-manging systems and workflow as well as preservation designs and efforts are suffering from the files-in-folder paradigm limitations.

We have reached the end of the good old "f-in-f":
So long. You have served us well.
We are very grateful for that.

Our computing capabilities have outgrown a data-warehouse world, and is able to handle data in a more liquid - in flux - ways. More fluently.

Imagine a brand new, incredibly intuitive - like playing lego - and creating and handling worlds - like minecraft. And applying that, mixed with a pd-meets-minecraft user-interface options - including the whole range of web-engine based frontends.

Basically I present you with a new kind of universal engine driving data-handling to finally getting the real benefits out of the 21st century computing powers.


# Another try: Maybe short this time. Executive summary.

Google-like find and retrieval options on your local and network data storages.
Your basic filesystem offering meta-and-data capabilities to provide database operations.

Your filesystem (which used to be files-in-folders) now become a graph-database, that can be queried - like you would search for things on the Internet.
Adding clever indexer configurations to that mix, and it'd very likely even be snappier, faster and more convenient than what you're used to today.

Imagine, just "saving your data" - giving it a few "tags" (start with what you'd have put in a file or foldername).
And just "store".
And you never have to think about "cleaning up that data-nest" one day.
You can add-and-edit tags at any point in time later on.
You simply have the same metadata information that you have now.
Only better.

A prototype could be built in 6 months.

That would accomplish:

  * De-embedding all metadata of any format readable by a FOSS implementation.
  * Provide APIs for handling metadata on the filesystem level.
  * Provide basic support for relationships between Objects.
  * Provide basic web-engine based UIs for handling/using Data Objects daily.
  * Support Dublin Core (DC) metadata templates and profiles.
  * Optionally translations/mappings of existing popular metadata layouts such as mp3/mp4 and other media-container formats.
  * Simply offering a collection of clever presets for popular use cases. Including professional ones.
  * Therefore adhering to existing standards in a way at least as good as state-of-the-art database or XML/JSON mappings.

This system template could then theoretically be used in any memory institution, to store their collections.
As a copy.
This would allow a seamless transition onto that new storage/data paradigm. AHAlodeck.

The 1st prototype would be called `AHA-PT1`.


# Another try.

Imagine you could just "store" any data, any file - just save it.
And your storage is awesome enough to provide you a query field.
Or a folder-tree-file view, as fallback if you like.

Imagine you can keep on using files-in-folders, knowing you simply don't have to anymore.
You can just "save" your data - and it'll be there.

You need to give it at least 1 tag.
Full Unicode support. You can even use emojis.
Tags can be unlimited size, bit-proof and have full URI and Python support built-in.

Imagine your data transforms into a arbitrarily small-to-large, from orderly to personal tagging.
Anything goes.
As long as you've either tagged it properly enough - Same as you would do today.
The very same data that you now put into:

  * the filename
  * the foldername
  * and structure
  * embedded metadata (title, artist, album, etc)
  * an excel sheet
  * any other means where you keep your metadata already

Now the proper place for that is *keeping your meta with the data*.
Simple as that.

Anything you'd use as search term to find your stuff when you need it - on any device connected to "your storage". Your data server, locally in-house all the time.

Add tags as you like.
You'll be presented nice simple masks with tabs that offer standardized or common metadata naming and layouts.

It'd be great to cooperate with Wikidata on this, since I'm imagining - if time allows - to proof-of-concept the ground-breaking-ness of this filesystem change: Wikidata-Data could simply (by API?) be direct-plugged as remote-pool, yet nicely cache-indexed locally for seamless access.

Yes, metadata may be converted, transformed, anything - as desired.
However, the ways of doing so are again *withing the filesystem*.
Since by allowing Python code contained in metadata fields to be executed (if policies allow), the filesystem becomes an active "agent" on handling the data it is being given access to.

This is a good thing.
Some may consider using this against one another.
I hope not.

We will find ways to deal with that.
I hope people may understand that sometimes we may be better to leave something good be.
And support that, rather than what exploits us.

Add tags as you like.
Then go to bed knowing your data will be there when you need it.
It'll be exactly there in the same way you left it 20 years ago.
Or even longer.

It's self-structured and well-described.
Plaintext on the filesystem level.

Like a file-or-foldername.
Only better.


2024-03-19
