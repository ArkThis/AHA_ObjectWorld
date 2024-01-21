## Small payload stored as metadata "value"

Hm...
One object shall have 1 payload. Right?
So that would be clear and clever hack. Right?

If not limiting the data size of what is stored in a (bit-proof!) metadata name=value field, it's quite tempting to put existing metadata (XML, JSON, CSV, text, etc - even PDF!) right as a "value" with the Object's "other" main payload.
Anyone who likes embedded-everything or "packed" AIPs: Here's your friend.

Should that hack be allowed?
It would allow an Object to exist "more robust/standalone".

Whereas, if we didn't allow this "feature", anything "not just a regular string" would have to spawn a new Object+payload - and relate to it properly.

Depending on how well "implementation dialects" would evolve and be resolved in the AHA world. Because it may not matter that much, if "Resolving Objects" is a commonly used basic feature of any Data Browser or Object-aware tool that anyone would now of.

Resolving would simply mean to pack/unpack any Objects by either "packing" as much metadata into the fields as possible, or "unpack": move as much "embedded" metadata to a proper Object-thinking data structure. In this case "embedded" may mean binary-embedded (like "MP3 tags") or "embedded payload as metadata field".
The "unpacking" steps (and code) would be almost identical.

For the beginning, traversing the graphs may cost quite some performance.
It's already noticable when handling metadata standards: There's a reason why some field is "here" and not "related to..." - in order to become more widely "accessible". In a performant and usable way.

So maybe "packed" Objects make sense when AHFX is new.
Later, if performance allows, working with "unpacked" - more related - Objects to handle as preferred default.
This will only be the case if any "AHA world" is built so well that "it just works" - and even your related objects are as reliably accessible (and travel and "age" well over time) as filenames right now.

Probably we'll see a mix of "packed" and "unpacked" - even "mixpacked" ;)

In the end, all that matters is that the right "data" can be accessed and used at the right point.
