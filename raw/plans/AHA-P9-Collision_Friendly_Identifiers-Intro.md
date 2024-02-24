# Collision Friendly Identifiers

2024-02-24

## Abstract

Reconsidering the "uniqueness" of a digital identifier to a point where a "pattern collision" limits the number of individual Objects that could theoretically co-exist at the same time.

The address-range, so to say.

Including the fact that actual collision sometimes shall happen on purpose, triggering a policy-rule based merge situation. Yet, when and how often for which "kind of Data Object" this shall happen can also be configured easily, and individually.
With policy rules.

> **The collision events are desired triggers for (transformation-)actions on Meta/Data in Objects.**

Such as:

  * auto-merge / auto-relate matching Data Objects.
  * and cluster similar ones.
  * all by a simply plaintext, human-friendly ID.


# Introduction

Imagine: You catalog a band named "XBloome" - and my friend also did that - in his local collection.
We're pretty sure talking about the same artist, therefore we intentionally encourage our Objects to be found together on the same storage "realm" one day - colliding.

Merging or selecting yours/theirs.
As you like.
As your system preferences are set.

Catalog metadata entries stored as Data Objects, with IDs like that would auto-cluster similar "intentions" of Object copies. Auto-generating 1 new out of 2 previous versions.

If desired, version-control could keep track of all previous data-layouts.

Simply including one aspect of `data-aging` by simple collision-friendly IDs.
:D


## Why not UUIDs?

I don't like them.
I find them unpractical and uncomfortable to work with. Seriously.
I find them **very useful** and necessary though at the same time.
I prefer technology that is designed with actual people in mind.
I prefer things I like to use myself.

Try generating a few UUIDs to get a feeling for the readability of them:

`$ uuidgen -t -r`

Or:

`for i in $(seq 10); do uuidgen -t -r; done`

To get a bunch of them. Including on timestamp and random as input.
I personally find them very hard to read, memorize and work with in general.
They're like hurting my pattern-loving brain-nerves. QR codes alike.

Looks like this:

```
4fab499b-b42f-4fdf-a069-7dc4304510ea
2d3769c3-c31f-4729-8b3c-8b7ec4e8d4f2
0e9e8372-0679-44a7-8db7-6c5fe80451cf
1541e700-4720-4291-9a05-6a624fa8fccd
c764fe69-2bd5-4dde-a623-c14f85c7afba
0b671a7c-c102-4afd-86a6-a9e5afc7cc14
3fd9b307-6422-4b18-ab0a-5082670114d5
90d78a7c-87ac-4611-a274-fad8451b7baf
a622e22b-3183-43f7-af09-8e3a0d0b70e8
f39ac3f6-c02e-457b-a091-165ac862c12d
```

😕️


# I suggest a different, more inviting syntax for `unique-enough` IDs


## Option 1:

I really imagine the following ID syntax as replacement option for UUIDs:

> **Syntax: [🌟️]TIMESTAMP-LABEL[-RANDOM]**

Yes, the 🌟️ is mandatory and required by standards definitions :)

In order to be *sure* that full unicode support is given on all implementations.
Any meta-and-data field is bit-proof and unicode-capable.
Seamlessly.

This is the most original version I've been using so far.


## Option 2:

> **Syntax: [🌟️]TIMESTAMP-LABEL-CREATOR[-RANDOM]**

Where `CREATOR` is intended like [DublinCore `Creator`](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/creator/) - but can be any pseudonym-nickname-whatever string the user prefers and has set.

This is the most recent version I'm considering at the moment.


## Challenge Accepted

However, I do invite you to challenge the collision-chances, given the fact that Data Objects are create for a reason - and at a certain date/time.

So what are the chances of 2 individuals choosing the same, identical `label` at the very nanosecond `timestamp`, being given a matching random character sequence of random-length (up to max. chars)?


I am considering this ID syntax for an Object Storage based `Object storage/reference/linking engine`.
Considering both: small and local, yet also distributed, super large scale data collections by design.

A Data Object can literally be anything you'd now be able to conceive - and use - as a `file in a folder`.
Giving them auto-generated IDs with the above syntax, would introduce a design-limitation for "noise" (over-creation of Objects) - due to limiting the address space on purpose.



## Collide on purpose?

  * Yes!
  * Absolutely.
  * On purpose, but *not by accident or error*.

Imagine you're cataloging/annotating/linking a public author/creator of any (digital) work.

You know the birth-date.
Or the date a group was founded.
The usual "Agents" date metadata standards.

Now if I `labelled` the catalog entry Object of the band XBloome with:

>  🌟️TIMESTAMP-LABEL

And selected the date/year I believe the band was formed.
As fuzzy (00-00 and all) as I like.

**Examples:**

>  =🌟️200610-0-XBloome  
>  =🌟️2006-0-XBloome  
>  =🌟️20XX12?-0-XBloome  
>  =🌟️20061200-0-XBloome  


```
TIMESTAMP = 20061200
NANOSECONDS = 0
LABEL = XBloome
RANDOM = <none>
```

Yes, random is empty.
So it's quite likely that someone else created an Object for the band XBloome using the same ID.
On purpose.

Now if we connect different meta/data collections ID'd like that, or query an online shared-source - matching entries would collide - theferore providing the option to `update` our existing Objects - without requiring that more (address) space.

So our "database" entries become auto-annotated, auto-referenced by default over time.

This is the "collision-friendly" nature of this design.
And one possible benefit of such a syntax.

It would also be very easy to memorize for anyone:

> 2006-XBloome

And so yes: This would be a different, separate non-colliding Object.
btw: Given the fact that each Object *does have* a full as-unique-enough ID string stored:

`TIMESTAMP-NSEC-LABEL-RANDOM`

Again: with nanosec precision, and random-random characters.
That address space should be quite sufficient for a while, I guess?

Keep in mind that `2006-XBloome` was also sufficient to get what you wanted - because it's linked to other Objects (if copies exist) that may have "more or different" information about the "XBloome" from 2006.

The data your querying or working with may of course be "as fuzzy as short-and-uniform their ID is".
Intentionally.

Yet never losing the option to keep certain Objects alive and sharp as new.
By each having their full-ID.


## What if Object IDs collide?

So there's the case when:

  * The label
  * The timestamp (nanoseconds = 10^9 digits)
  * The random sequence (random length, preferred local charset)

...are exactly the same.


Okay.

How do we deal with it?

I suggest this:

  * To select: merge?
  * Or prefer yours/theirs/other?
  * And: this includes relationships/links to other meta/data.
  * Policy rule (=preference) setup option to store and configure that selection.

In case the meta/data content(s) differ "too much" (beyond a configurable, sane-default threshold) - the user may optionally be altered and asked for their opinion. So if some things that really refer to something completely different (eg 2 different bands - not even sharing the same metadata "title", etc.).

**Exactly the same we already do with version control conflict handling.**

Again, I do consider the case of actually colliding Object IDs (given the above syntax) to be very high or practically significant, too: So most of the time there isn't even any problem.


## Heavy and thin and "pure" Data Objects

Objects with shorter, less random IDs (=more collision friendly) will accumulate more "encounter" metadata, by merging or adding references to other Objects.

These may always be both equally: meta or data (payload).

Here's a suggestion for categorization:

  * heavy
  * great
  * light
  * thin
  * link

Meaning:

  1. Heavy is the one including the large-bytesize chunks of data payload.
  2. Great ones are with your preferred working format(s) for data and just enough meta.
  3. Light is meta-only, preferred plaintext (non-binary) - may include wholefile syntax clobs. Still "just meta" no real "data" (payload).
  4. Thin is meta-only, below a certain bytesize of selected keys. 
  5. Link is links where possible and reasonable - and hard-copy strings where it makes sense.

Be generous with your meta!
I believe the computing resources will be sufficent. And can be improved if necessary.



## What if I don't remember the whole "ID"?

No problem.

If you remember parts (label most prominently), then maybe a year?
Or a month? day? particular pattern in sub-seconds or random?

Yes, IDs may also include emojis. Again: Full Unicode support.

So, `2006-XBloome` - and you'll get a list of all entries matching fuzzy-match Object IDs.

Objects with short IDs like that are intended to accumulate meta and relate (or carry) the data, too.

**Examples:**

```
20061225-123456789-XBloome-aj1öf3wle3fa7owief  
2006-0-XBloome  
200612-0-XBloome  
20061200-0-XBloome-lskajdfowihf2a  
```


## What if me or someone else got the date wrong?

So be it.

``` 
20050501-0-XBloome
200800-0-XBloome
2006-0-XBloome
...
``` 

So there'll be clusters of (un)similar `TIMESTAMPS` - but all having the more or less identical `LABEL`.
And no relevant random-factor.

One can still work with fuzzy-search unfiltered, but grouped list of IDs here.
And if one of those Objects is under your control: You may see that others "disagree" - and you may take the time to figure out "why".

This would solve one "value/record source" issue.


## "more prominent" Objects usually get (to keep) a long - or even more awesome ID.

Yes, as long as the values stay within the default syntax, anything custom goes:

  * `🌟️TIMESTAMP-LABEL-RANDOM`
  * `🌟️00001225-Superstar`

Also cool:

  * `🌟️01-xbloome-blue_room`

May all your collisions go well and be fruitful!
Remember: On collisions, your meta/data meets more meta/data - and your collection might be better annotated/related afterwards?

Everyone is in control over their own collection. If one decides for a certain object precision/style it's fine - as long as the syntax is engine-compatible.


## Feature: Aging Object become "fuzzy".

Transformations could be applied to Objects (defined again by policies) to "lose their precision" (=timestamp sub-seconds index) when being copied and being above a certain age "or condition".

Example:

  * **Original:** `20061225-123456789-XBloome-aj1öf3wle3fa7owief`
  * **Random removed:** `20061225-123456789-XBloome `
  * **Less sub-second precision:** `20061225-123456-XBloome`
  * **Just-minutes precision:** `20061225-12-XBloome`
  * **Just the year-and-month:** `200612-XBloome`

You get the idea.

Any implementation is fine, as long as the data owner/user is fine with it (on their systems).

So by reducing the randomness, and length of the ID string in total, the chances of older Objects to "collide" increase over time (and configured aging parameters). Since the IDs will become less precise = shorter again.
The IDs shrink and flatten down.

Actually, using Object Storage queries to decide which Objects shall be processed "over time" - and how - may be interesting to do.

Implementing and supporting `digital data aging` functionality by default is an interesting way to avoid data-congestion - and overwhelming storage consumption - even running long-term.

If collisions become so popular for certain objects, that they payload version collides as well

There are means to refresh Objects to "keep them alive" longer.
Any Objects not used for over a certain period, are simply merged or prefer mine/theirs and be good with it.
They may even be removed at all if garbage collection policies feel free to do so.

Introducting quasi-natural aging to digital data.
It feels like a good new option.



# Refreshing

Although it requires a write-operation to the Object filesystem (problematic for tape, or other offline media), if one wants to "pull a certain Object copy out" of the collission ID pool - they can simply do so by "refreshing" the fuzzy parts of the original full-ID of that very copy.

This would still keep the visible ancestry/relationship by ID: this is like `family` of data.
And "remembering" your valued data is keeping it in shape.
Remembering and toggling "a bit".

And anyone at any time may refresh any copy.
It would quasi "bump" it out of its previous collision spaces - and "throw the dice anew".

That would be the "required action to start preserving that digital object".

I think I know how to build a working prototype for this right now.
A FOSS stack of production stable implementations and documentation.
With slight alterations to orchestrate the full potential of a graph-DB data storage system.

Sounds interesting?



# Remark

I just realized this very much feels like "yet another" suggestion how to name your files and folders.
Maybe it's because this kind of "rather cross-whatever stable" syntax seems so intuitive and familiar to me and everyone grown up with files-in-folders for data.

Indeed:
This ID can absolutely be used as-is described here for filenames.

But, please don't forget:
This is *just* the technical identifier.

> **Yes, people can and shall use it too, but:**
> The "title" or other metadata describing this Object go in separate, regular filesystem fields.

So if you feel like abusing the `LABEL` component like we used to long-label filenames, please do not.
The fact there's a timestamp+label in your ID makes it already pretty fine.

And anything else you'd like to add:
Put the meta with the data: In the filesystem.

Not in the ID.
Thank you. 😘️
