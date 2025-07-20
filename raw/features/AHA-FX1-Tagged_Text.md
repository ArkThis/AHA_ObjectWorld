
## May store written text as single objects.

Resulting in a graph of related Objects, describing a text document (including images and other embedded Data Objects) on the filesystem level. The only possible downside to this may be performance.

Yet considering the current speed of world-wide-content-indexing "single textfield" interfaces with realtime suggestions of semi-arbitrary context: wow.
I don't expect a big performance issue with this feature.

The concept:

This may be crazy, but one could actually tag each word of a written text,
generate an object for each word or phrase - and then re-create that text by
generating a new Object that refers to these "word objects" in the right order.

Each word-Object would now be capable of not only receiving a referrable ID (URI?),
but also "machine readable" gets a complete new meaning. Because if a machine
is able to use/understand this "hyper-AHA-structured text", these word-Objects
could then be connected to any other digital data object (image, video, audio,
document, etc). And of course the word-objects would be annotated: dictionary 
(reference) links (URL/URI), language tags, translation references, etc.

In that way, any information depicted as Object can be referenced to a
word-Object. The graphs which are dereby being created can then be used to
"decode" any digital data like written text.

Example:

  * Here's a photo of a nice <Tardis>!
    And then you could do a simple search/replace each written-word, by any image file that has the tag "tardis" to it. There's your image search.

  * You could then apply this to the whole text, and you'd get a visual representation of the written text.


There's probably already existing quite-smart AI-related code/tools to do exactly that.
Since the data to-be-stored resembles machine text-learning-understanding requirements, there may be an interesting match to be made, combining those two.

Or the end of the world as we know it.
Who knows?
Yet worth a try if done well.


### Imagine Object Markup O.O

With a structured text like this on a plain level, supported by all basic libs: tagging a word, phrase, anything - group Objects as you please - and link as you desire.

Which feature of any currently existing "WYSIWYG" fancy document/text editor
fileformat could you not translate into Objects?

Any parser of any such format must currently at one point or another handle
*exactly the same structure of text-objects* in one form or another in memory -
or as intermediate format to render, handle and convert.

Considering existing any-to-any text/markup/down document format converter:
Translating them, by breaking them up into individual "Transformer Objects"
that may simply be connected to each other like in "Pure Data".

It wouldn't matter anymore at all which text-format you've chosen.
Of course one can be creative in making things *not work* interoperable again,
but then please, simply do not use such tools - or help them becoming better at
working together.


