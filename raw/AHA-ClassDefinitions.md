AHA - ObjectWorld

# Object Class Definitions

Yes, it sounds like [something taken right off a programming lesson](https://www.w3schools.com/python/python_classes.asp). That's exactly what I'm proposing.

Define Class Definitions for Data Objects.
Each Data Object can have (=store) its Class Definition (eg a Python source code syntax) in a reserved system space. With the Object. Don't worry. ;)

That Class Definition can be updated on the fly.
Whenever anyone accesses Object Properties (read/write), they are loaded/treated according to the Class Definition.


## A classic example

Here's a copy from a [w3cschools Python tutorial](https://www.w3schools.com/python/python_classes.asp):
(I've added comments)

```
// This is the Class Definition for a "Person" Data Object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

// `p1` now contains an instance (copy) of such an Object:
p1 = Person("John", 36)

// An imaginary example of how easy it'd be to show Name and Age values stored
// with that Data Object:
print(p1.name)
print(p1.age) 
```

Yes, that's [Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html) 101.
So we know (how) it works.
It may make sense (be necessary) to use a language that allows declaring data types for each property.
(strict typing)



## Another example: Musik Objects

  * Support all common music tags, like MP3/MP4.
  * Support professional music tags, like BWF data.
  * Additional tags are declared in the Class Definition, too.
  * Can have "Functions" (Class-Methods) containing executable programming code.
  * Default Methods may include: play, convert, edit, tag.
  * Presets and config can be stored as Object Metadata.
  * You can keep the "Original" filenames (as Object Metadata), as well as any
    later "filename" this Object was known by.

Now you can most likely double- or right-click:Method (=Action) and something
meaningful will happen.  The Object can be well-described to fetch-and-setup
its required dependencies to be able to perform required actions.
(See "NixOS Flakes")

Since descriptive metadata can be stored with each the Object, it "feels" like
embedded metadata. The big difference is, that by supporting relationships
between Data Objects, common descriptions can be split off - or better
"materialized" as standalone Objects. The Music Object can now keep the
metadata value (eg "artist=XBloome") as string - and in parallel as a reference
(by ObjectID) to the Catalog Object "XBloome".

If you copy any sub-parts (Objects) of your music collection, you now also
transfer any information associated with it - and accumulated/added to support
common (and custom) features of different audio applications.

This greatly improves interoperability between different applications/systems.
Imagine, you could drag-n-drop copy any selection of tracks from your music
collection onto a USB-Stick or over a network, and there'd be no need to think
about foldernames, or filenames when merging them with or into an existing
collection. And it would bring its own database (by Catalog Objects), as well
as related files, such as cover art, contain web-links, Wikidata IDs, and even
custom features like "[The Moodbar](https://en.wikipedia.org/wiki/Moodbar)"
only some players support.

Either as attached metadata, or related Objects (=a connected/related Data Graph).
In any way, you don't have to worry *if* your Objects travel well. They simply
do. It's "the job of the filesystem" to take care of that. If it does *not*,
it's a faulty implementation and should be fixed. :)



## Existing system: NixOS "Flakes"

Something similiar is already being provided by [NixOS "Flakes"](https://nixos.wiki/wiki/Flakes):

> "Flakes introduce a policy for managing dependencies between Nix expressions.
> It improves reproducibility, composability and usability in the Nix
> ecosystem. Although it's still an experimental feature, flakes have been
> widely used by the Nix community."

Flakes currently is designed to turn regular folders into active folders that
support reproducing specififed computing environments to support proper
functionality and behavior of whatever is in them.

Flakes contain config and recipes/instructions for automatically setting up a
(build-)environment in a folder.

Code, experiences and functionality from the usage of Flakes could very well be
useful in the AHA ObjectWorld design.
