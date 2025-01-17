# Store value or reference?

2024-11-17

A typical situation:

  * Text value = "The Artist's Name"
  * Identifier = Some ID string

What if AHAlodeck standard would simply use Markdown Linksyntax to store key value pairs like:

  * Artist = [XBloome](http://www.xbloome.com/)
  * Artist = [XBloome](Q1234777)
 
The string used to "ID" the entry, doesn't matter.
Just like W3C standards in XML, RDF, etc.

It makes sense:
If a URL can be accessed directly by that string, it /is/ a unique-enough identifier.
Quite noisy/ugly to handle visually, without IDEs though.

Using namespace syntax and functionality here, we could also "ID" the keys:

  * [Artist](rdf:Artist) = [XBloome](http://www.xbloome.com/)

The string syntax is so trivial to parse, one could even use that data in this form easily from bash-script to python to CERN science cores.


As simple as that.
And it may make sense to allow nested-resolution of this syntax.

  * [[Artist](wikipedia:Artst)](rdf:Artist) = ...

Or to disallow it?
The information would still remain perfectly readable, parsable and non-contradictory or fuzzy in any way.
Good.


Anyway, with this simple hack, and support by UIs to render it as working links:
Even pure-metadata-only Objects may use this syntax to describe related IDs.


I'm pretty sure, big-data circus people have found interesting ways to deal with this "ref(ID) vs value".


## Namespace = storage size relevant

Assuming I'd like to go RDF on my filesystem, I'd have full-blown URLs - for *each* key.
Lots of them.

This may grow kBs pretty fast for nothing.
Therefore I guess it's mandatory that a proper AHAlodeck system supports namespace-prefix handling by default. Very well and handling multi-namespaces in parallel, reliably.

I assume this to reduce the information being able to store as much into the current 4k xattr primary storage place.


So:

  * [aha:ns](xb=http://www.xbloome.com/)
  * [Artist](rdf:Artist) = [XBloome](xb:about_us.html)

This has the same disadvantages/risks as any other form of data-compression - because that's what this would be.
If the namespace information is lost, the referenced form becomes "unclear". However, it is /very/ likely that popular namespaces for metadata keys are publicly known (eg "rdf" or "dc" in XML, etc).

And depending on your use-case, it will still work flawlessly, if there is no collission with your ns-tag-prefixes, using different ns URLs for the same prefix. Not so common, I'd say.


Anyways:
Markdown URL syntax for ID+Value storage in key/value anywhere.
