# Distributed - and ID collisions/syntax

(work in progress. rough braindump)

  * search anywhere for objects anywhere
  * option: torrent-magnet style
  * what about offline (eg SD-card, HDD, etc) storage?
  * What about thin-vs-thick copies?
  * What about ID syntax and collisions?

Having thin copies to be able to search-n-find data throughout your registered/connected/indexed "realms"?

DNS-like lookup mechanisms for Objects anywhere?

Imagine Objects could be "Ping'ed":
If there's any reference to an Object ID, it could at least let you know "more" about where to find "more" about that referred Object.

Like: "It's not here right now, but it's on your backup-SD-card, label xxx"


# Use case 1: Personal Search over *all* local storages

  * Looking for "Data Object(s)" on your local network/machine.
  * It shall be irrelevant if the actual "heavy copy" of an Object exists: Thin copies (=quasi catalog entries) are sufficient to get the info "it exists".
  * So references remain "valid" (even if pointing only to a metadata stub Object)
  * BUT: 
    What about uniqueness of the ObjectID?
    It is intended to be collision-friendly.
    However, having eg a thin-and-thick copy of the same "meant" Data Entry as 2 separate Objects. Including a backup-copy (of both).

Then there are 4 Objects:


## If they had the identical ID:

    Since Objects can be annotated and referenced arbitrarily (even in the same realm), there is no point in distinguishing between like:

        1. "a more annotated" (heavy MD)
        2. or "verbosely annotated but a little less" (heavy, but less MD)

    Yet, with identical IDs, it would be impossible to explicitely point to "the one or the other" Object (or any copy thereof).

    So each Object *should* really have a definitely-unique ID. Too?
    What if, there was a declared syntax for Object IDs?
    So that each Object acutally had its "timestamp-label-random" ID, stored in full-length, and by query parameters (or filter/profile settings), the graph-engine can be set to search fuzzy-or-precise.

    * How to practically (UI?) handle that there may be more than 1 match?
      Should there be ways to auto-select (=preference profiles) - or the most recently chosen - or otherwise?

    * Most recently chosen seems like the most generic, stable - and predictable - way (for developers and users alike). Coding *with* physics.

    * Also means of explicitely being able to select any other preference (rule?). Policies should be query-templates with conditional rules and branches (imagine MediaConch policy paradigm).

    * Maybe advanced policies could also be implemented using "transformer" Objects.

    * I do believe that the self-similarity by design approach to (ab)using Objects for almost anything: Like building the LEGO compiler out of LEGO itself.

    * So: Unique IDs, yet collision-friendly (selectable) syntax.

    * Policy-rule preferences could actually be stored as "declared metadata" field - or as reference to currently active policies stored externally (Object link reference!)

    * TODO: Write down overview of the "most basic" common functionality of AHAlodeck engine. Like: key=value support, relationships/links, inflating/deflating Object(graph)s. API functions.

    * It most likely makes sense to already consider stages/tiers of feature support, allowing an orchestrated good support across different hardware/stack capabilities and ressources. No need to "hack" or "embrace expand extinguish" anything. This was designed to be useful, used and well supportable by almost anyone.



## If they had different IDs:

   * So we already derived the fact that each Object *must have* a unique ID.
   * I do however question if a UUID as currently "common" is really required - in contrast to a simple (and way more human-comprehensible) syntax of:

   `timestamp-label-random`

   * The nature of "why Data Objects are created" in the first place, provides enough "entropy" (yet common-ness) of any Data Object.

   * Calculating the number of possible non-colliding ID-variations for a given `label+timestamp` pre-entropy input: There is no necessity to limit the length of the `random` ID component.

   * Important:
     Objects are created *in time* - so the timestamp is only identical if someone created Objects with *the same label* at that very moment.

   * Considerations:
     What if the use-case to handle and query Object ID-key combinations of several MD fields? Like "ObjectID + Creator"?
     Except for style and performance considerations, is there any downside to this 'verbose' implementation suggestion?

    

## What if colliding objects would auto-merge?

(Maybe policy option to trigger yes/no popup)

Would that be so bad?
Or there's a "always prefer ..." options.

Oh, alright: We already have intended full version control support as standard functionality. Git on FS level, so to think.

So, there you have your engine and config for handling Object-Merges.

Would it be so bad, if Objects would by default (?) collide - and dissolve into one another?

In which cases could this be "an error" that causes invalid entries, or loss of very desired behavior?

So these Objects:

  * Would have the same label+timestamp (precision!) and random-string.
  * Timestamp-precision (up to nanosec: 10^9) can be adjusted/selected.
  * Default is to "prefer own" (=creator is one of your accounts), and discard the other.
  * If difference is "too great" (easy to evaluate), alert the user and ask for opinion. This case should not appear too often.
  * If that "too-different-but-colliding" case appears too often, there's something flawed in either my theory, or some code :)

Is there any (mathematical) way to (dis)prove my assumption that I consider it *very highly unlikely* to cause collisions on that level (random number matching! Plus nanosec-timestamp!).

Those cases may actually be treated like finding prime-numbers!

Please show/tell me a use-case & code that may produce such Object collisions, that may not be simply resolved by either a merge or "prefer ..." engine?


