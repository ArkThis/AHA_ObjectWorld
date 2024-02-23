# Collision Friendly Identifiers


## Abstract

Reconsidering the "uniqueness" of a digital identifier to a point where a "pattern collision" limits the number of individual Objects that could theoretically co-exist at the same time.

The address-range, so to say.

Including the fact that actual collision sometimes shall happen on purpose, triggering a policy-rule based merge situation. Yet, when and how often for which "kind of Data Object" this shall happen can also be configured easily, and individually.


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

So what are the chances of 2 individuals choosing the same, identical `label` at the very nanosecond `timestamp`, being given a matching random character sequence of random-length (up to max. chars).


I am considering this ID syntax for an Object Storage based `Object reference/linking engine`.

A Data Object can literally be anything you'd now be able to conceive - and use - as a `file in a folder`.
Giving them auto-generated IDs with the above syntax, would introduce a design-limitation for "noise" (over-creation of Objects) - due to limiting the address space on purpose.



## Collide on purpose?

Imagine you're cataloging/annotating/linking a public author/creator of any (digital) work.

You know the birth-date.
Or the date a group was founded.
The usual "Agents" date metadata standards.

Now if I `labelled` the catalog entry Object of the band XBloome with:

>  🌟️TIMESTAMP-LABEL

And selected the date/year I believe the band was formed.
As fuzzy (00-00 and all) as I like.

```
TIMESTAMP = 20061200
LABEL = XBloome
RANDOM = 
```

Yes, random is empty.
So it's quite likely that someone else did just the same.

Now if we connect different meta/data collections ID'd like that, they would collide - theferore providing the option to `update` our existing Objects - without requiring that more (address) space.

So our "database" entries become auto-annotated, auto-referenced by default over time.

This is the "collision-friendly" nature of this design.
And one possible benefit of such a syntax.

It would also be very easy to memorize for anyone:

> 2006-XBloome

And so yes: This would be a different, separate non-colliding Object.
btw: Given the fact that each Object *does have* a full as-unique as well ID string stored:

TIMESTAMP-LABEL-RANDOM

Again: with nanosec precision, and random-random characters.
That address space should be quite sufficient for a while, I guess?


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
  * Policy rule (=preference) config option to store that selection

In case the meta/data content(s) differ "too much" (beyond a configurable, sane-default threshold) - the user may optionally be altered and asked for their opinion.

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




## Aging Object become "fuzzy".

Transformations could be applied to Objects (defined again by policies) to "lose their precision" (=timestamp sub-seconds index) when being copied and being above a certain age "or condition".

Therefore the chances of older Objects to "collide" increase over time (and configured aging parameters).

Actually, using Object Storage queries to decide which Objects shall be processed "over time" - and how.

Implementing and support digital data aging functionality by default is an interesting way to avoid data-congestion - and overwhelming storage consumption - even running long-term.

There are means to refresh Objects to "keep them alive" longer.
Any Objects not used for over a certain period, are simply merged or prefer mine/theirs and be good with it.

Introductin quasi-natural aging to digital data.
It feels like a good new option.



# Refreshing

Although it requires a write operation to the Object filesystem (problematic for tape, or other offline media), if one wants to "pull a certain Object copy out" of the collission ID pool - they can simply do so by "refreshing" the fuzzy parts of the original full-ID of that very copy.

This would still keep the visible ancestry/relationship by ID: this is like `family` of data.

Yet, anyone may refresh a copy.
It would quasi "bump" it out of its previous collision spaces - and "throw the dice anew".

If that would be the "required action to preserve digital data", wow.

I think I know how to build a working prototype for this right now.
A FOSS stack of production stable implementations and documentation.
With slight alterations to orchestrate the full potential of a graph-DB data storage system.


AHAlodeck ;)
