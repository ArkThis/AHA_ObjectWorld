## Metadata XML/JSON preproc-cache.

I imagine simple metadata-only objects, for example with a proper filled out
set of Dublin Core (DC)-described (data) items.

With something like an XSD-for-AHA, and an AHA-to-XML/JSON API/libset, it
should easily be possible to generate any pre-formatted, (standardlayout)
metadata text format (as common now) by (eg Python) programming code.

Or even cooler: By AHA-XSLTs. 
(Something open and makes sense - possibly reusing already exisiting, proven
code/specs)

And that output is either stored as "preferred payload" at the main metadata
object, or as a new object with a relationship back (reverse relationship).

It's good practice to include either some README (or reference to one) or a
preview/summary form of the contained "name=value" metadata. More "default or
popular views" can be created as new objects, also each with a relationship to
its "parent".

Since it now becomes very likely (over the lifespan of an object and
"collection"), that someone has generated "a preview" data format, or classic
text-metadata version: interoperability and performance should at least equal
that of nowadays comparable setups and use-cases.

Maybe even faster, due to less wheel-reinventing-syssyphus overhead, due to
"everything already being an object" filesystem-aware.


#JSON (`<- see? This could already be a link to "another Object" or URI.`)

For example, tell your text-editor to run a regular "parse-for-links" on "Save" or "Exit".

