# Using folders as taxonomies.

2024-11-05

Why?
Because that's what the "path" (aka "folder structure") was actually used for all these years:
A simple, yet highly effective way for structuring mixed data in a 1-dimensional hierarchical taxonomy of terms.

A digital "file" never was in any folder in the first place:
Your data just "is somewhere on your memory" - with an address (ID).

Any folder structure you already have now for your datas can be used as-is to depict one set of nested-tags.

* folder-structure = hierarchical, 1-dimensional, nested tags.

  * plus: links to other Objects = Now it's a 2-dimensional set.
  * plus: using xattrs for key-value store, it's a 3-dimensional information model.
  * plus: language tags and translations available as xattrs on the folder.
  * default foldername is "the standard term" - if one is available.
  * Links to other objects can be used for handling:
    * aliases
    * fuzzy-search
    * translations

All xattr values may as well be "by-reference", meaning: "only as links to other objects"
I would suggest to go for "reference-and-value" as default, until we see performance or space issues.
Could also be that, depending on the available hardware and needs, we may go from "thin-objects-by-ref-mostly-if-not-only", which can be "deflated" after booting - and stay "swift" upon suspend.


# Depicting existing vocabularies as folder-tree

Example:
https://id.loc.gov/authorities/names.rdf

```{lang=xml}
<rdf:RDF>
    <madsrdf:MADSScheme rdf:about="http://id.loc.gov/authorities/names">

        <madsrdf:hasMADSSchemeMember rdf:resource="http://id.loc.gov/authorities/names/collection_LCNAF"/>
        <rdfs:label xml:lang="en">Library of Congress Names</rdfs:label>

        <rdfs:comment rdf:parseType="Literal" xml:lang="en">
        The Library of Congress Name Authority File (NAF) file provides authoritative data for names of persons, organizations, events, places, and titles. Its purpose is the identification of these entities and, through the use of such controlled vocabulary, to provide uniform access to bibliographic resources. Names descriptions also provide access to a controlled form of name through references from unused forms, e.g. a search under: Snodgrass, Quintus Curtius, 1835-1910 will lead users to the authoritative name for Mark Twain, which is, "Twain, Mark, 1835-1910." Names may also be used as subjects in bibliographic descriptions, so they may be combined with controlled values from subject heading schemes, such as LCSH. Library of Congress Names includes over 8 million descriptions created over many decades and according to different cataloging policies. LC Names is officially called the NACO Authority File and is a cooperative effort in which participants follow a common set of standards and guidelines.
        </rdfs:comment>

        <madsrdf:adminMetadata>
            <ri:RecordInfo>
            <ri:recordStatus rdf:datatype="http://www.w3.org/2001/XMLSchema#string">modified</ri:recordStatus>
            <ri:recordChangeDate rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2011-04-26T00:00:00</ri:recordChangeDate>
            <ri:recordContentSource rdf:resource="http://id.loc.gov/vocabulary/organizations/dlc"/>
            </ri:RecordInfo>
        </madsrdf:adminMetadata>

        <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#ConceptScheme"/>

        <skos:changeNote>
          <cs:ChangeSet>
            <cs:subjectOfChange rdf:resource="http://id.loc.gov/authorities/names"/>
            <cs:creatorName rdf:resource="http://id.loc.gov/vocabulary/organizations/dlc"/>
            <cs:createdDate rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2011-04-26T00:00:00</cs:createdDate>
            <cs:changeReason rdf:datatype="http://www.w3.org/2001/XMLSchema#string">modified</cs:changeReason>
          </cs:ChangeSet>
        </skos:changeNote>

    </madsrdf:MADSScheme>
</rdf:RDF>
```


```
  * rdf:RDF
    * madsrdf:MADSScheme
      1. rdf:about="http://id.loc.gov/authorities/names"

    * madsrdf:hasMADSSchemeMember
      1. rdf:resource="http://id.loc.gov/authorities/names/collection_LCNAF"

      * rdfs:label
        - xml:lang="en"
        - value:"Library of Congress Names"

      * rdfs:comment:
        1. rdf:parseType="Literal"
        2. xml:lang="en"

        3. value="The Library of Congress Name Authority File (NAF) file provides authoritative data for names of persons, organizations, events, places, and titles. Its purpose is the identification of these entities and, through the use of such controlled vocabulary, to provide uniform access to bibliographic resources. Names descriptions also provide access to a controlled form of name through references from unused forms, e.g. a search under: Snodgrass, Quintus Curtius, 1835-1910 will lead users to the authoritative name for Mark Twain, which is, "Twain, Mark, 1835-1910." Names may also be used as subjects in bibliographic descriptions, so they may be combined with controlled values from subject heading schemes, such as LCSH. Library of Congress Names includes over 8 million descriptions created over many decades and according to different cataloging policies. LC Names is officially called the NACO Authority File and is a cooperative effort in which participants follow a common set of standards and guidelines."

      * madsrdf:adminMetadata
          * ri:RecordInfo:
              * ri:recordStatus:
                - rdf:datatype="http://www.w3.org/2001/XMLSchema#string"
                - value:"modified"
              * ri:recordChangeDate:
                - rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime"
                - value:"2011-04-26T00:00:00"
              * ri:recordContentSource:
                - rdf:resource="http://id.loc.gov/vocabulary/organizations/dlc"

        * rdf:type:
          - rdf:resource="http://www.w3.org/2004/02/skos/core#ConceptScheme"

        * skos:changeNote:
          * cs:ChangeSet:
            * cs:subjectOfChange:
              - rdf:resource="http://id.loc.gov/authorities/names"
            * cs:creatorName:
              - rdf:resource="http://id.loc.gov/vocabulary/organizations/dlc"
            * cs:createdDate:
              - rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime"
              - value:2011-04-26T00:00:00</cs:createdDate
            * cs:changeReason:
              - rdf:datatype="http://www.w3.org/2001/XMLSchema#string"
              - value:"modified"
```

This should be possible as annotated folder-structure using xattrs, compatible with 4k-limit filesystems.




-------------

# IDEA: Body-swap files-with-folders - as thin-copies, using xattrs.

Something related, yet very different.

Thinking paths equal to nested-term taxonomies.
Therefore if more than one "/nested/string/of/terms" is present as metadata (xattrs), one can switch arbitrarily between multiple "paths" - term structures. Visually represented in any folder-path UX paradigm and tool of your choice.

Since you manifest that structure "for real" on the filesystem again, it's accessible by any existing tool.
Just point it to "the other folder structure" you'd like to view your data as.

Similar to what the main GNU/Linux window managers did when you "mounted an audio CD".
It felt like copying "files" - and there were subfolders for `wav, mp3, flac, ogg, etc`.

And the files already came pre-named (if metadata was in CD-TEXT or freedb.org, cddb, etc).
Simply copying them "from the CD" onto your harddisk - as MP3 file. Great.

This is more or less what I'm talking about:
The file-manager becoming a generic abstraction layer, capable of providing new possibilities for interacting with "data" (previously known as files-in-folders (FinF)).

You literally get "another dimension" of data-handling options by key/value-on-anything.
Then another dimension (yes, that's TWO new dimensions!) if you add "by reference" (=links to other datas) by default.
And then realize that by already working with databases, spreadsheets and embedded metadata, and other clever ingenious workarounds: We all are familiar with "how these additional dimensions" of data-handling options affect our data-handling:

It's what people do "because of cloud services".
It's amazing.
It's simply not "a cloud feature", but merely the better use of "dealing with data as Related Objects".
And this online as well as offline.


## In a nutshell demo setup:

  * Have a media FinF collection.
  * de-embed all metadata to xattrs.
  * create a thin shadow-copy of the whole collection (xattrs-only).
  * tar that thin-copy.
  * include recoll with a useful config

You now have a basic annotation setup + catalog with query/search/preview functionality.

Bodyswap?
Now imagine you take the folder-tree structure as "a path" - as a string.
And store that as xattr "path-something".

Now, if there are any other nested-tag path-like strings present as xattrs, one of them could be chosen as "the new actual 'path' in the file manager".

Like:

```
path="/home/user/Pictures/Something/$YEAR"
info="/events/gigs/open_air/xbloome"
```

It may help to think of this as:

```
path.1="/home/user/Pictures/Something/$YEAR"
path.2="/events/gigs/open_air/xbloome"
```

And one could simply "swap" from one path to the other.
Or to another:

```
path.1="/home/user/Pictures/Something/$YEAR/DCN0817.JPG"
path.2="/events/gigs/open_air/xbloome"
path.3="/events/concert/vienna/moonbabies"
path.4="/genre/electronic"
...
...
path.n="/projects/pelihof/food/vegetable/curry"
```

Trivial to implement.
The keys wouldn't have to be named "path". I'm just showing, that the "path" structure can actually be equally to nested-tags.

So, keys named "path" can be assumed to contain a path-string, which can be manifested as folder-structure (of tags).
So can any other key, if the key's name(patterns) are known, to put those keys also on the "use as nested-tags" list.

Now, what if those "paths" depicted in actual folder structures "on your disk" (=in your filesystem, on your screen) - could co-exist?

As "path.2 and 3" are more tagging categories, but also perfect "paths" - imagine looking at the same file switching folder-views to represent nested-taxonomies. A classic "dog-poodle-puppy" case: If you would tag your dog pictures, "dog" is clear, but if you have "puppy" - you want to use both "poodle/puppy" and "puppy/poodle" - depending on what you like to browse for: By kind-of-dog or cute puppies?

Just keep both.
I believe the hardware Überfluss in which we seem to live in right now (while everyone's saying we're running out of real resources really fast... btw.) - and things become obsolete and incompatible faster than ever before.

The current hardware any kid has on the playground would actually have in their pockets is fast enough to go overboard with keeping any-and-all metadata and see What, where, why and when things slow down.
We can target that specific performance issue better (at less cost) then, than considering it an obstacle at this level of development. Too early, and maybe uncalled for :)

Fingers crossed.



# Size/Performance considerations regarding reference and/or value?

I haven't done the math, and it may feel like a chessboard-rice-trap, but:
I currently don't believe keeping both, reference (URI?) and title for a field should not be a major issue performance-or-sizewise.

Like imagine a song as a file:

  * title = "Blue Room"
  * artist = XBloome
  * album = ...Done!
  * year = "2006"

For title and year, imagine "it's a string".
And for artist and album, imagine: they are links to that artist or album.

Now how would that link look?

  * title = "Blue Room"
  * artist = [XBloome](https://www.xbloome.com)
  * album = [...Done!](https://sound.xbloome.com/albums/...done!)
  * year = "2006"


# Worries?

Performance and size:
Jean-Francois (Recoll) said: "Index will be about the same size as all uncompressed strings that were configured to be indexed"

The current latest json export from Wikidata is around 120 GB in size.
That's a lot of key/value metadata-only. I therefore assume its index would be about the same size.


For regular amounts of objects to annotate and index:
I still don't think it adds significantly, compared to regular data-storage-and-usage at the moment.
Which already /is/ quite digi-wasteful IMO. There's a lot of exabytes of probably garbage and heat-generating computing cycles.

On the other hand:

Considering full-brown URLs as IDs, they may actually be way longer than the value they "encode" by reference.
Wouldn't that mean "pi-mal-daumen is die ID sehr oft wahrscheinlich länger als der Value-String".
Somit würde "keep" Ref alleine schon viel mehr Platz "bei jedem Field jedes Objects" bis zu mehr als doppelt soviel Platz brauchen.

Und dann noch Values dazu, wären "mal 2.5" vielleicht nicht unrealistisch?
Und wär das dann überhaupt auch noch ein Problem?
Wieviel wiegen denn die Metadaten die wir alle bereits haben (zB embedded, path, filename, ...)?
Das dann mal 2.5: Ist das das "en gros" an Daten mit denen ein aktuelles Setup zu kämpfen, bzw. knabbern hätte?
oder ist das immer noch peanuts.

vA wenn der Vorteil ist, dass ein generisches, wiederholendes Trivialsystem das meiste abbildet:
Simply repeat "the key-value+reference LEGO pieces at will and hardware"

In the end, the plan is to use a Wikidata dump to test performance on a very large collection of very-mixed-yet-highly-structured-metadata.


# Namespaces

One could consider "context IDs": Where a very-common part is simply stripped or commonly referenced by a shortcut.
Double-reference resolution, so to say:

`https://aha.ArkThis.com/pt3/my_field` = "hallo."

is:

because the namespace reference has been declared:

```
ahans:aha="https://aha.ArkThis.com/pt3"
aha:my_field = "hallo"
aha:my_field = aha:/intro/welcome
```


