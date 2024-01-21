## May replace all embedded metadata needs.

Probably, because Object Metadata feels like embedded.

But even better, because noone needs to care about "which file format".
Metadata access is the same for any format.

For developers: No more need to go through any file-format parsing or
implementation-support overhead. Handling Object Metadata is probably in one of
the first introduction lessions of an Object-Storage support tutorial.

So, why bother to write support for yet-another-fileformat, if anyone can simply
use the Object Storage default features?  Any program/developer not doing so
would spend way more time, while becoming less-interoperable and user-friendly
over time in comparison to simply using default libraries/functionality.

So yes, Object Metadata is "in some way" embedded. But now on a different level:
The filesystem. Not the file format anymore. And that's a big difference in
daily usage of any kind.

