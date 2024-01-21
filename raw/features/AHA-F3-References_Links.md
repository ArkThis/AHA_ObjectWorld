## References and Links

Regarding "related Objects" and Linked Open Data (LOD):

When it comes to refering to "other things", it may be better to always spawn a
new Object for this.  Instead of having a syntax (and complexity) for
referencing local fields, maybe it's better to intentionally *not* have that
option, and rather live with (possibly way-)more Objects.

That may be an issue when AHFX is new though.  I expect accessing "local
metadata fields" quicker (not necessarily "easier" from a users or developers
point of view) - and more reliable (or simply without interrupted flow in any
way).

Whereas "lifting" related Objects: That may greatly depend on how "Objects" are
actually allocated and their binary data being read.


**On the other hand:**

If it's simply *required* for regular use to have a good performance/behavior with getting the data from related Objects: May this provide a better "engine" earlier or more widely supported?
Like: They had to come up with hardware-decoding to make digital video go mobile.

What if the "name" field may have syntax? What if XPath may work by default?
That would require an XML-like structure syntax. Possibly JSON would suffice.
Stored as EBML on the actual filesystem blocks? Only rendered like "text-tagged" data in the Data Browser?
