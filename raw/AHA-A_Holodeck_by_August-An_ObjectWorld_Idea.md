---
title: AHA - A Holodeck by August - An Object World idea.
author: |-
        Peter Bubestinger-Steindl \
        `(peter @ ArkThis.com)`
geometry: a4paper, margin=2cm
toc: false
toc-depth: 2
linkcolor: blue

date: 2022-something (singapore national archives, INA)
---


2023-05-06 (just came home from EQZE)


# A Holodeck by August, Please (AHBAP)

or: 
> "keep your meta where your data is: in the file system."
> "why not?"

why (not)?
I have some very good answers for you. Read on!



# summary
whoever implements this, if it ain't seamlessly interoperable, persistent and stable, it's not what I meant. :)
We can do this.

# Abstract

Eigentlich nur einfach, interoperabel und standardisiert alle Metadaten im Dateisystem handhaben können. So selbstverständlich wie Dateinamen und Ordner. Bis hin zum USB-Stick oder Sdkarte in Gerät XY.
"Ganz normale Objectfiles" 
---

Using an object storage filesystem as database for metadata. Like a catalogue. With no more gap between file payload and metadata.

There shall be no difference between files, just metadata and relationship entries. It's all just a bunch of objects.

No more folders. Just metadata. All objects are in a pool.

Current MAM GUIs and use cases will simply use the Object data (like a basic filesystem), instead of their own database.


# Intro

So this is it.
We've reached it.
Gratulations!

The way software has evolved has, and is increasingly hitting "invisible, but very real" barriers where it seems that the relational metadata(-standard) layout and/or embedded tags in container formats in files, including the fact that it's always a ... pleasure and excitement to deal with keeping the links between the database/catalog/dam/cms - mam, etc and the actual payload (your files in some folders) working.
And their hashcodes.

Well, and relationships.
And yes: Also metadata schemata that "make sense" and can actually be used interoperably and comfortably.

Unpossible?
I don't think so.
Please walk with me through this idea.

The following is a SciFi short-story describing the idea of putting puzzle pieces together that already exist in the professional and community computing scene to literally solve most of todays meta/data efforts. I am serious about that.

If you like, you may entertain yourself with the following idea:
With the budget for a regular 5 year EU-funded science GLAM project, I propose to be able to implement a working prototype - or share with anyone willing to do so any ideas and concepts. Happily!

**If we can take the time for it.**

And find the right people.
A prototype. Enjoy.


# Interpretation Remarks

## serious/seriously
  * tech-wise I'd say I'm serious: I really think this could be technically absolutely feasible to implement an already useful prototype
  * serious: Please if you think I'm wrong somewhere, or you know better, or whatever: Please let me know! I hope I can publish this so people are able to comment, patch and commit.
  * serious: I've been involved and read quite a few "standards definitions papers" in order to make sense of them - and to implement them. Multiple times in different environments, pc-epocs, OSs, programs, etc. I've seen things.
  * seriously: I would not call myself a good software developer. I can write code, and I like a certain style. But I like keeping it fun - and working proper. A joke shall always be welcome.
  * seriously: Again, I like playing with ideas - so I really think: A joke shall always be welcome.
  * seriously: Maybe it's my way of trying to make reading "standards papers" or scientific papers more like reading the script for a smart comedy. - And I'm very emotionally-biased about the "usage" of the term "smart". Good and bad.
  * serious: If you feel offended in any way: Sorry, I'd actually consider myself a well-raised person. Please let me know what you experienced and how we can improve on that.
  * I'm a passionate engineer, yet a clever joker who even may drink with artists and punks. And loves it.
  
## controlled vocabulary terms used

Having something to point to for reference is so helpful and awesome and so omnipresent.
Computers have "IDs" to point (allocate) things - to do anything, you need an "ID". As Digital As the Real World.

**vocabulary lists could also be the very same AHA-Objects (AOs)**

So like, agree on one common (xml-thinking? then json) schema of what we currently know we need for interoperable import/export/usage-of long (possibly sub-structured/grouped) terms - classes to serve iso-ish-id-term-mapping capabilities and meta/data sources?

Is there any "WikiTerms" project/website that does offer something like that?
I remember having seen one shown at the DFF (Frankfurt / DE), but can't find it in my notes.

## Abbreviations and "tech-terms".

I've been juggling with many many many multi-letter-acronyms, starting when I was 10y old or so. BAT. Cool.
BATMAN.
Oh too long. Only 3 letters after the dot allowed.

Yes, I'm not trying to normalize or consequently use the matching yet intentionally similar acronyms or "imaginary professional/domain terms". I rather use them to flavor the sketch, and to help me remember the structure of this idea.

And you may entertain yourself with: "Maybe that's me always wanted to be the crazy awesome "Doc" person."

I consider it fun (it entertains me, and possibly others) to juggle - even enact brilliant-madness-nerd-stuttering when uttering an idea that is very hard to translate to written form. Even creating "a serial string of words" to express myself does not feel like my native language for transmitting my "images/understandings". Please, no guru!

I have this issue that I catch myself:
Oh, yeah right. If that was true, it would be soooo easy to be happy.


# Paper, RFC, Sketchpaper

All of that in some way or another.
Would you ask your friends, loved one(s), colleagues - even kids to "let's have fun together reading a DIN or ISO paper! Who finds, affords and finishes reading all of them - then trying to understand all of that, remember and re-read-reference it when trying to implement it in actually useful and error-less code."

Fun!

Or:
WhatIf getting exactly the same or even better understanding of "The Idea" or Story.
The good old "History or just a Story?"-myth that was common in "The Old Days".

Would you go to a sketch-show where a text like this one would be worth-paying-for entertainment? Just for the fun of it.
Spoiled enough to have time to "play with that idea".
Or be the first one to have understood this "new thing".
Etc.

I suggest a game:
Would you like to take the time to see how well and great your imagination can go? Like why not being the first to come up with the idea to pioneer an engineering breakthrough. All of that in the age of Aquarius-and-AI.

Once my kid is interested enough in this, I'm happily gonna bring her along.
Sounds like a sekt? sect? I wouldn't want to.

Okay: Enjoy the show, and if you'd like to engage in this idea in any way, let me know. Please be friendly. My time is worth something, and I have feelings and a life and friends and bills to pay. You know what I mean?

Okay: Enjoy the show. Welcome to the new world of thinking digital.
Object-Based: Neither new nor obsolete. Alive and kicking and evolving.

-------------------------------

# A Holodeck by August

Let's call it "The AHA". Like "MAM", but it's an "AHA".

WhatIf we could actually just write a name=value + hierarchy + ids directly to our files?

WhatIf we could actually really put whatever text-(including emojis and spaces) filenames as plain "metadata" of type "text"?

WhatIf all of the applications/protocols/technology would actually exist, be there in production use successfully - and *drumroll* - thanks to FOSS quality: All these parts are available in FOSS-licensed projects.

WhatIf it would by design solve many-many use-cases now already implemented and running - and daily and anywhere an OS runs that deals with files and data. Simply translate / morph / interpret data in different, yet seamlessly interoperable ways?

WhatIf the database/catalog/search/archive metadata and applications - and all your data-storage filesystem needs would simply merge into "Thinking in Data as Related Objects with Tags - and IDs"

WhatIf The budget for building that (prototype) may cost less than the average "yet-another-hit-and-run-public-funded-dies-shortly-after-funding-stops" scientific digital evolution plan y3456 project handed out and being allocating ressources of brilliant and highly motivated people (from what I know from the "Archive-Ninjas" community out there!)




# The Basic idea as a bullet list brainstorm mindmap listing.

  * minio
  * GNU/Linux OS distro (Debian, Ubuntu, Redhat, etc)
  * iiif universal viewers (for images, documents & AV - and possibly 3D and even more)
  * draw.io (for beautiful graphs. generated by data)
  * rrdtools (for more beautiful graphs of everything else)
  * munin (did I already mention more beautyful stats and graphs and monitoring?)
  * mongodb (as a starting point where to put the data-per-object (yet still thought of as "file" with folders(-paradigm).
  * thx to UTF-8 and Emoji-code, "plaintext" became incredibly fancy already.
  * With HTML + WebBrowser (engines), we've basically got the engine(s) for rendering "views" of our data (=objects and their properties and relationships).
  * Sprinkle a little (or lot?) of LOD over this:
  Wikidata already contains a gazillion+1 ID-to-ID mapping table of almost anything (at least "Agents" or possibly "Places" or "Artwork" - etc).
  * As file manager, we could use browser+iiif(funded to go on steroids and even more awesome). Imagine that: Looking like a Windows Explorer or Finder or Thunar or Nautilus or ... - would be nothing more than HTML-website magic.   
  * Already a few "text editors" exist which basically are a gigantic install package, because I guess they're BYOB (bring your own browser) anyways. So there's already feedback/input on what that's like - and how it's done.
  * Now imagine: Your music and/or video including photos, nes-roms application-internal databases would easily dissolve into "copy the media-container-stream-format-specific metadata out of the file, and into the "object metadata space"?
  * This would dissolve any and all data-format "container" interoperability and support (and maintenance, etc) issues and efforts by design. What would be the point of *not* putting your metadata there? If you do can imagine a reason to still write (and maintain) your own "format", could you tell me please?
  * Even further: Go down one more level and have: hashcodes for different levels of content. Media streams are separate objects. Simply "related to each other".
  * It doesn't matter if an object has a "payload" or not.
	  ["payload":the actual content of what you now call "files"].
	  The foldername/path is simply "yet another metadata field". Name=value. Solved.
  * There would be no difference between objects thought of as "files" and objects without "heavyweight" payload (content) data.
  * You get me?
  * Where's the catch? Please I can't yet find one. I've been challenging and discussing this idea for about 6 months or so. Still stands.
  * Let's continue: So imagine your MP3-collection (and a mix of possibly other formats from wav to WM?... 😱️) Why not? Existing awesome audio applications (Clementine!) exist that read quasi all media formats in existence (thx FFmpeg, MediaArea et al again I guess?).
  * The data collected by any audio (or media player) whether Itunes or Clementine or Winamp or Amarok or Rockbox or ... : It doesn't matter anymore.
Also the file format (mp3, mpg, ogg, avi, wav, flac, opus, ...) - doesn't matter. The tags are read *once* - written to your objects storage *filesystem* (more on that later) - and then it's only streams and relationships.
  * You can go even deeper into the rabbit-hole: Why not store the tech-md of "any other" data (file-)format we know and need or like? DXF, MXF, MKV, BMP, JPG, TIF, PDF, \star. - no more "byte offset & word-size and hex-edit". No: Simply put that information (yet, copy-paste from existing files/data) to AHA's Objects-MDs (AHA-OMDs ;).
  * If there's hierarchy between objects, simply create a light object for describing the relationship between AHA-Objects. It's fun to code that translator-lib (reversible/downwards-compatible) handling. Once. Not "with slight variations, due to lack of willingness to cooperate. Or legacy reasons).
  * Oh: This would break (in a good way) with "expensive" (or exhaustive) drawbacks from having to support "legacy formats & data & software".
  * Whoever (developer, company) may think they'd "profit more" by manifesting this idea in a not-awesome, because not so interoperable as the FOSS-stack? Please let me know.


# Seriously. This is possible.

Summary of the basic idea:
> Every file, folder, format, metadata, relationship, name=value, payload - everything: Can be handled by that AHA Object-filesystem. Yes. A real filesystem. Maybe "heavier" than legacy ones, but I believe it's likely to be "as taken-for-granted like FAT16". It just works.

This "aha-fs" concept would require similar computing (and diskspace) as the sum of all "currently usual/common" applications that already have their own databases and catalog-code implemented?


# Performance?

I have no idea.
I also don't think that's really an important question to ask at this point, because all I'm suggesting is to build a working prototype with existing components - by getting independent development projects and companies together - and yes, also end-users, public money, etc: And give this a try.

So, I think I guess it's possible.

This metadata is actually already being extracted and *stored as a copy in a local database* - but well, not one database, but databases - and embedded in files. Sometimes even in tapes stored "offline" in the archive.
We work and live with this already.

Since all that development-and-computing-and-maintenance ressources would not be needed anymore and shifted to "putting possibly a fraction of that old wasteful dev-style thinking"-ressources into performance of actually using these "name-value" forests. With additional meta-metadata.

"Inceptionz(tm)" we call it. Awesome.

So what I'm saying is:
Could it be that the performance of that "new and better idea I'm proposing" is actually *better* (and overall more stable?) than what we have - globally from poor to $$$ - simply more "organized" and "streamlined".

"Lego'd" we call it. Awesome.

The software-and-hardware library stack for handling "this one object format" performantly I imagine may be smaller than "libavcodec*" and friends.

I say let's try - building a funded prototype in 5 years.
Name me any metadata workflow or challenge (or mystery) that this "object world" - aka "AHA".

Simply: A Holdeck by August.
Why not?


# Add Indexers. If necessary.

The design thinks "in Internet" - URIs and friends.
So what is being used to make online web-services (that actually mostly already are media catalogs with CMS, etc) - so the knowhow and code and applications are already well-known deployed.

If someone one the Internet can do it, if they publish a Howto and specs, etc - Anyone can implement it. Cooperatively.

So if the objects-metadata filesystem database is getting "uncomfortably (slow?(ing down?)), because name=value keeps adding up - over the lifetime (or popularity, or tool-chattiness, etc) - Objects (unlike current files) (may) change all the time. Or not at all.

So running Indexer networks or cascades, starting on localhost (by default). May this be an option for even the Windows-Registry?, local webservers?, etc? - I watch my CPU graph for almost 10 years on my main office notebook. And most of the time the cores have nothing to do, and my ram's getting rusty, because XFCE is just so nicely slim, yet beautiful and elegant.

Therefore I think we also may more options to try before going into hardware requirements.
And even if we do: We could scale it from "user to pro". That's also not something new.

I suggested before "MongoDB".
Why? Simply just because I don't know any other non-SQL database engine yet, but I find them very interesting - feels like a radically different data- and UX-protocol style and paradigm.

So a prototype for testing the actualy functionality and usability, etc.
Just to see if this AHA-effect may shift to enter a new age of dealing - living with digital data - our datas - to simply embrace a new concept of: "Aha. Oh-bjects. I get it. That's how you handle "data"".


# Implementation ideas.


## AHA Object class sketch

The "A and O" is the shortest form. "OHM" was already taken as prefix for property and class names.

```
TheAO {
  UUID ich									# Das kleine Ich-bin-Ich is the inspiration for calling this AHA-ID "ich". Instead of ID, Identifier, UUID, etc. Simply "me". Please world: agree on *one* language to use for naming that field and then dublin-core fix it. Call it "{x-i, a-o, q, ...}" or whatever gender neutral and selfie-compatible and long-term sustainable term you like. But please feel free to agree on at least one thing to start with. Thank you :D
What if we agree to use (seriously) a UTF-8 standard Emoji for that? Yes as field-name. Not the value. We can go crazy on that later.

  UUID \star										# Yes, in theory that can compile and run without errors.

  TheAO[] hashes				# <-- That's already a ref to yet-another-object (YAO?AHA!)
  TheAO[] related      # Again... YAO.
  TheAO[] tags          # name=value
  TheAO[] mappings   # x=y look-up tables. Controlled Vocabulary, MD-standards, ISO639, 8601, etc etc.
  
  Constructor						 	 # Initializes "cat-i", etc.
  Constructor(myfiles[]) 	 # +copy/pastes from existing file(s)
  Contructor(foranyotherpropertyordesire)		     # You get the idea?

  BasicFunctionsEveryoneNeedsDailyAlreadyAndWeKnowItSince GNU0 (Thank you! 👏️👏️👏️)
  ThinkLegod()
}
```


##  Required core applications

  * minio: For the object filesystem core.
  * mongodb: as core of the name=value (structured JSON & queries)
  * translators / interpreters of "anything to AOs So this is it.
We've reached it.
Gratulations!

The way software has evolved has, and is increasingly hitting "invisible, but very real" barriers where it seems that the relational metadata(-standard) layout and/or embedded tags in container formats in files, including the fact that it's always a ... pleasure and excitement to deal with keeping the links between the database/catalog/dam/cms - mam? and the actual payload: Your files/folders.
And hashcodes.

Well, and relationships.
And yes: Also metadata schemata that "make sense" and can actually be used interoperably and comfortably.

Unpossible?
I don't think so.
Please walk with me through this idea:


# A Holodeck by August

Let's call it "The AHA". Like "MAM", but it's an "AHA".

WhatIf we could actually just write a name=value + hierarchy + ids directly to our files?

WhatIf we could actually really put whatever text-(including emojis and spaces) filenames as plain "metadata" of type "text"?

WhatIf all of the applications/protocols/technology would actually exist, be there in production use successfully - and *drumroll* - thanks to FOSS quality: All these parts are available in FOSS-licensed projects.

  * minio
  * GNU/Linux OS distro (Debian, Ubuntu, Redhat, etc)
  * iiif universal viewers (for images, documents & AV - and possibly 3D and even more)
  * draw.io (for beautiful graphs. generated by data)
  * rrdtools (for more beautiful graphs of everything else)
  * munin (did I already mention more beautyful stats and graphs and monitoring?)
  * mongodb (as a starting point where to put the data-per-object (yet still thought of as "file" with folders(-paradigm).
  * thx to UTF-8 and Emoji-code, "plaintext" became incredibly fancy already.
  * With HTML + WebBrowser (engines), we've basically got the engine(s) for rendering "views" of our data (=objects and their properties and relationships).
  * Sprinkle a little (or lot?) of LOD over this:
  Wikidata already contains a gazillion+1 ID-to-ID mapping table of almost anything (at least "Agents" or possibly "Places" or "Artwork" - etc).
  * As file manager, we could use browser+iiif(funded to go on steroids and even more awesome). Imagine that: Looking like a Windows Explorer or Finder or Thunar or Nautilus or ... - would be nothing more than HTML-website magic.   
  * Already a few "text editors" exist which basically are a gigantic install package, because I guess they're BYOB (bring your own browser) anyways. So there's already feedback/input on what that's like - and how it's done.
  * Now imagine: Your music and/or video including photos, nes-roms application-internal databases would easily dissolve into "copy the media-container-stream-format-specific metadata out of the file, and into the "object metadata space"?
  * This would dissolve any and all data-format "container" interoperability and support (and maintenance, etc) issues and efforts by design. What would be the point of *not* putting your metadata there? If you do can imagine a reason to still write (and maintain) your own "format", could you tell me please?
  * Even further: Go down one more level and have: hashcodes for different levels of content. Media streams are separate objects. Simply "related to each other".
  * It doesn't matter if an object has a "payload" or not.
	  ["payload":the actual content of what you now call "files"].
	  The foldername/path is simply "yet another metadata field". Name=value. Solved.
  * There would be no difference between objects thought of as "files" and objects without "heavyweight" payload (content) data.
  * You get me?
  * Where's the catch? Please I can't yet find one. I've been challenging and discussing this idea for about 6 months or so. Still stands.
  * Let's continue: So imagine your MP3-collection (and a mix of possibly other formats from wav to WM?... 😱️) Why not? Existing awesome audio applications (Clementine!) exist that read quasi all media formats in existence (thx FFmpeg, MediaArea et al again I guess?).
  * The data collected by any audio (or media player) whether Itunes or Clementine or Winamp or Amarok or Rockbox or ... : It doesn't matter anymore.
Also the file format (mp3, mpg, ogg, avi, wav, flac, opus, ...) - doesn't matter. The tags are read *once* - written to your objects storage *filesystem* (more on that later) - and then it's only streams and relationships.
  * You can go even deeper into the rabbit-hole: Why not store the tech-md of "any other" data (file-)format we know and need or like? DXF, MXF, MKV, BMP, JPG, TIF, PDF, \star.\star - no more "byte offset & word-size and hex-edit". No: Simply put that information (yet, copy-paste from existing files/data) to AHA's Objects-MDs (AHA-OMDs ;).
  * If there's hierarchy between objects, simply create a light object for describing the relationship between AHA-Objects. It's fun to code that translator-lib (reversible/downwards-compatible) handling. Once. Not "with slight variations, due to lack of willingness to cooperate. Or legacy reasons).
  * Oh: This would break (in a good way) with "expensive" (or exhaustive) drawbacks from having to support "legacy formats & data & software".
  * Whoever (developer, company) may think they'd "profit more" by manifesting this idea in a not-awesome, because not so interoperable as the FOSS-stack? Please let me know.


# Seriously. This is possible.

Summary of the basic idea:
> Every file, folder, format, metadata, relationship, name=value, payload - everything: Can be handled by that AHA Object-filesystem. Yes. A real filesystem. Maybe "heavier" than legacy ones, but I believe it's likely to be "as taken-for-granted like FAT16". It just works.

This "aha-fs" concept would require similar computing (and diskspace) as the sum of all "currently usual/common" applications that already have their own databases and catalog-code implemented?


# Performance?

I have no idea.
I also don't think that's really an important question to ask at this point, but please I'm always happy to be told differently.

So, I think I guess it's possible.

This metadata is actually already being extracted and *stored as a copy in a local database* - but well, not one database, but databases - and embedded in files. Sometimes even in tapes stored "offline" in the archive.
We work and live with this already.

Since all that development-and-computing-and-maintenance ressources would not be needed anymore and shifted to "putting possibly a fraction of that old wasteful dev-style thinking"-ressources into performance of actually using these "name-value" forests. With additional meta-metadata.

"Inceptionz(tm)" we call it. Awesome.

So what I'm saying is:
Could it be that the performance of that "new and better idea I'm proposing" is actually *better* (and overall more stable?) than what we have - globally from poor to $$$ - simply more "organized" and "streamlined".

"Lego'd" we call it. Awesome.

The software-and-hardware library stack for handling "this one object format" performantly I imagine may be smaller than "libavcodec*" and friends.

I say let's try - building a funded prototype in 5 years.
Name me any metadata workflow or challenge (or mystery) that this "object world" - aka "AHA".

Simply: A Holdeck by August.
Why not?


# Add Indexers. If necessary.

The design thinks "in Internet" - URIs and friends.
So what is being used to make online web-services (that actually mostly already are media catalogs with CMS, etc) - so the knowhow and code and applications are already well-known deployed.

If someone one the Internet can do it, if they publish a Howto and specs, etc - Anyone can implement it. Cooperatively.

So if the objects-metadata filesystem database is getting "uncomfortably (slow?(ing down?)), because name=value keeps adding up - over the lifetime (or popularity, or tool-chattiness, etc) - Objects (unlike current files) (may) change all the time. Or not at all.

So running Indexer networks or cascades, starting on localhost (by default). May this be an option for even the Windows-Registry?, local webservers?, etc? - I watch my CPU graph for almost 10 years on my main office notebook. And most of the time the cores have nothing to do, and my ram's getting rusty, because XFCE is just so nicely slim, yet beautiful and elegant.

Therefore I think we also may more options to try before going into hardware requirements.
And even if we do: We could scale it from "user to pro". That's also not something new.

I suggested before "MongoDB".
Why? Simply just because I don't know any other non-SQL database engine yet, but I find them very interesting - feels like a radically different data- and UX-protocol style and paradigm.

So a prototype for testing the actualy functionality and usability, etc.
Just to see if this AHA-effect may shift to enter a new age of dealing - living with digital data - our datas - to simply embrace a new concept of: "Aha. Oh-bjects. I get it. That's how you handle "data"".


# Implementation ideas.


## AHA Object class sketch

The "A and O" is the shortest form. "OHM" was already taken as prefix for property and class names.

```
TheAO {
  UUID ich									# Das kleine Ich-bin-Ich is the inspiration for calling this AHA-ID "ich". Instead of ID, Identifier, UUID, etc. Simply "me". Please world: agree on *one* language to use for naming that field and then dublin-core fix it. Call it "{x-i, a-o, q, ...}" or whatever gender neutral and selfie-compatible and long-term sustainable term you like. But please feel free to agree on at least one thing to start with. Thank you :D
What if we agree to use (seriously) a UTF-8 standard Emoji for that? Yes as field-name. Not the value. We can go crazy on that later.

  UUID \star										# Yes, in theory that can compile and run without errors.

  TheAO[] hashes				# <-- That's already a ref to yet-another-object (YAO?AHA!)
  TheAO[] related      # Again... YAO.
  TheAO[] tags          # name=value
  TheAO[] mappings   # x=y look-up tables. Controlled Vocabulary, MD-standards, ISO639, 8601, etc etc.
  
  Constructor						 	 # Initializes "cat-i", etc.
  Constructor(myfiles[]) 	 # +copy/pastes from existing file(s)
  Contructor(foranyotherpropertyordesire)		     # You get the idea?

  BasicFunctionsEveryoneNeedsDailyAlreadyAndWeKnowItSince GNU0 (Thank you! 👏️👏️👏️)
  ThinkLegod()
}
```


##  Required core things

  * minio: For the object filesystem core.
  * mongodb: as core of the name=value (plus meta-metadata)
  * importers for metadata (mediainfo++) to AOs metadata fields (name=value)
  * s3lib? for capabilities/methods/concepts for working with Object Filesystems and read/writing the actual filesystem-database?
  * linux kernel?
  * debian? et al?
  * iiio community/devs/institutions: For implementation guidelines for viewers, then editors for "AHA Objects" (AOs).
  * FOSS web-browser projects: Providing the headless-then-HTML (G)UI - CMD or CLI or text engine to render the UI of "The Application".
  * Nextcloud: For 
  * Wikidata:
  * MediaArea:
  * FFmpeg: speaks for itself. In any format/container.
  * motivated people. I know a handful good ones!
  * Artefactual/Archivematica
  * [TODO]



# Conclusion / Outro

* Yes, we could make this happen right away. Funding and people and interests needed.
* I mean: It's technically practically right in front of our eyes. I mean: `apt-install aha` metapackage.
* Everything here is work in progress. Don't stress yourself or me please. I don't enjoy that.
* Give your self and me some credit that we *spend our time* typing/doing here. Thank you.
* I'm too nerd too be able to come up with a version syntax and revision and publication system - arrrrgghg! burnout. I respond as good and timely fitting as good as I like and can.
* If you disagree, resonate and/or legally or mentally want to engage with me: Please do so. I take no responsibility for what others may think I have meant. That is out of my control. Thank you.
* Would you like a tea, coffee, drink, cigarette, time with each other?
* Call: [ghostbusters/macgyver/krider/...]


**I really think you should read this and with an open mind. Just for fun.**
Be Awesome.
Why not?


# additions 202306

Special metadata, or "system objects" or templates:

* complete functionality of a package management.
* compiler
* source
* build recipe
* dependencies - by object ids
* like pacman arch stuff.
* each object self-deploy and describable.

add IPV6 as global ObjectIPs... wow!🥰

# prototype ideas

btw: all metadata encoding unicode.

demo cases
* translate a fancy dvd to objects with iiif player.
* iiif view mode acting as classical hierarchical file manager.

# addon ideas

* torrent and magnet links
* each object has a PID UUID like it's own ipv6 style id.
* copy thin:
  * only ids
  * only text (including urls)
  * only other metadata, but payload

* name=value tags with snmp "manifest" (MIB).
  * Related links:
  * https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol
  * https://en.wikipedia.org/wiki/Management_information_base
  * https://kb.paessler.com/en/topic/653-how-do-snmp-mibs-and-oids-work
  
* xslt and xsd as idea built in.
* continue tagging as usual. any preferred app or workflow will do.
* presets for copy or edit or any action, are objects, too. with related objects.
* all on file system level.

* ids for objects: timestamp + origin id + index + optional identifying string, given by human or app.

* ipv6-ish uuid may be more collision prone when merging collections or generally over time, and given the fact that objects, just like files and db entries will be created and deleted all the time.

## The Object ID

syntax like:
> timestamp-string[-random]

The precision of the timestamp can be chosen/adjusted on demand. with low precision, collisions are not only expected, but encouraged. to make "possibly common" entities auto-relate and regroup.

### examples:
* minute precision: 202308131337-holodeck-test-UchVsOVxYXQ
* rough precision for auto collide: 2008-xbloome
* 202005-trendxy



# Relational Objects as file format

Pull tech values from file format headers, move them to the AHAFS Object level. Move separate data chunks into separate objects. Leave relationship, "meta" object with references to the chunks. Adding (copying) all necessary metadata to function just like it's originating file format.

An immediate stand-in replacement for all existing user interactions.

Overhead?
"parsing" and executing retrieval of all referred-to objects. Those may lay more fragmented over any storage underneath, but would that delay matter significantly?

If data like that is now already handled and served anyways, in performant ways - even in local sqlite-ish or cached or indexed ways - I believe that overhead would be negligible.

## Gain?

This would dissolve many file formats into [by-nature of such an Ahafs]-way into almost seamlessly interoperable layout.

Even for users: Most Mediainfo output would be a simple view option in any modern object file manager.

It may even eliminate the "interest" in proprietary data formats, as they stand out as uncomfortably odd. Even to regular users.

# Object file system as package management

# Apps built out of thin air
almost. :D
Imagine you need a program to handle (view, edit, etc) an object, double clicking makes the program simply "appear" up and running, like out of nowhere?
kinda what ArchLinux shows does stable and tested for years: recipes for auto-building applications from source.



# 20230817

TODO: Check if the user stories on NFDI4Culture can be depicted/handled with AHFX:
https://nfdi4culture.de/resources/user-stories.html

