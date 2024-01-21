## May have collission-friendly Global PIDs.

> **Syntax: [🌟️]TIMESTAMP-LABEL[-RANDOM]**

Yes, the Star-Emoji is on purpose in the mandatory section of its implementation: To show (off) that unicode works flawlessly.

Other characters or emojis may be used, but I'd start with a common one. Keeping it simple.
This syntax may provide a surprisingly small number of id-collissions, even if an actual "global P2P storage pool" is considered. 

  * Syntax TIMESTAMP:
    `YYYY-MM-DDT133700-`
  * Precision of TIMESTAMP is arbitrary. Default is Year-to-seconds.
    More fuzzy, like "year-month-only" may be used to encourage collissions with other Objects created by other users. Because however chosen, the more users create "fuzzy" objects, the more you'll see a "single value"-cluster forming. Maybe there'll be thousands (or more) Objects out there in the future, titled "Hooverphonic [Artist]" - most likely meaning the same "Agent" - yet, all with fuzzy IDs chosen: They'll over time auto-sort themselves out.

    Because if someone references to "20??-Hooverphonic-Artist" Object-ID, they'll receive the list of other Objects already describing "The Artist Hooverphonic".

  * "-RANDOM" is optional.
    This is a random number.
    Its purpose is that in the unlikely event that another Object was created at the very same TIMESTAMP with an identical LABEL - another dice is thrown to use "noise" to avoid an ID collission.
    By default: encoded like a youtube identifier (Alphanumeric+CamelCase)
  * Length of RANDOM is arbitrary.
  * RANDOM may be generated either from real random numbers or pseudo or even random-seed.
    Choose wisely.

And yes: Every Object ID starts with a "🌟️".


## May be self-sorting (Collission-friendly IDs)

Yes. Imagine your data would "sort itself out". Like coding *with* physics -
not against it. Not ignoring it.  CF-IDs in the AHA world are like this:

  * The TIMESTAMP precision is set to:
    * year
    * month
    * day
    * hour, minute, second, nanosecond

  * The label chosen to depict a assumably "common" term for the described object/entry.

  * RANDOM is better omitted if you assume that "your" intention for having that Object is shared by someone else.
    Without RANDOM, it's also clear (by naming convention/style) that the creator *intended* this object to "collide".

### Collission-handling

> "BORG it all out."

Meaning: Why not merge all metadata to a single, new object?
The new Object would It'd keep the "parent" ID, and continue with all "properties" (=metadata) from parent1 and parent2. Question is: How to merge the data payload (if there is one)?

Assuming that most collission-intended Objects will be metadata-only (aka "light" Objects)

