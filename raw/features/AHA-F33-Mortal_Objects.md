## "Mortal" Objects (optional):

2023-12

For security or other reasons, one may define objects as "mortal" - so they
de-manifest (=delete, erase, destroy, cancel, etc) itself after a certain time.
It may even be possible to define graph-queries that allow ending an object
under "certain conditions".

If performance allows this graph-query filter by default, the TTL handling
could merely be 1 special case for such a default query.

Overview:

  * Set a Time-To-Live (TTL): manually or automatically (optional / depends)
  * For example: per object space, a preset profile defines for how long a (new) Object's TTL is.
  * or: to define a graph query under "which conditions" to terminate.


UPDATE 2024-01
I'm pretty sure I saw something like this in existing MinIO documentation online. Possibly related to "tiering" profiles/scheduling - and auto-deletion features.
