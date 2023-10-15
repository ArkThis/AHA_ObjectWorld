# AHA - Security

2023-10-15

The basic concept of AHA was designed, simply completely ignoring access rights
handling - any of that - simply ignoring it.
Just: What would be the most awesome way of doing this?

And *then* think about what level of "security" is needed *when* - and before that:
What *is* "security"?


## Realms of Rules in Object Spaces.

**TL;DR**

> I'd like to suggest a trust-first approach in the AHA design.
> And Spaces are grouped in rule-Realms (Chatrooms), running in Worlds
> (servers) with transitional conditional rules and running each others code.
> As engagement of trust.


And we just switch Rules-or-Realms-or-Worlds (read below) and Sysadmins or
Developers until we have teams what we enjoy collaborating with.  And the AHFX
security concept is designed to reflect a social level of trust over your Data
- implemented in code.

If there are flaws: Fix them. Socially or patch code if you agree to do so.
Remember: You each have to run *the other one's code*.  And of course: That
code has to be FOSS and auto-build from source if you want to.
Completely transparent.

You can set the rules:

> No specs, no game. No money.
> FOSS? We subscribe. With money.

Object Spaces are like Chat Rooms - and the way of administrating Data Object
access is now more like having a messenger application in the background,
logged into multiple chatrooms (Object Spaces). And there's literally a
chatroom for each space. The larger the chatroom (=Data Space Realm) member
list, the more likely that it may have chatbots installed, or split into
smaller chatrooms.

This security concept auto-scales in the same technical nature that social chat
networks and websites do.  And will function at the exact same security level.
But at a different level of trust.

The very first PT-AHFX Prototype shall start as a free-speech-and-hate-yet-safe-space:

  * Everyone is allowed in. As the hardware allows.
  * At the beginning, you may only add tweet-ish metadata objects.
  * Little payload. Images, GIFs, the usual.
  * And you can add 10 flags. name=value.
  * And you can "elbow": An imaginary value of virtual "space" you'd like to be put between you and "the other Object (Realm)".
  * And you can "kick":
    It gives any other User/Realm notice that you would like to be left alone (by them).
    This is not considered rude. At first.
  * Therefore any polarised political world views are all welcome: If they agree to be friends "In That Realm".
  * They'd not be noticing each other more than "if you went online".
    We all browse in our context-interest-bubbles. And that's not always a bad thing.
    And we meet in common places.
    Increasingly online anyways. Why not the same with our data? We want to show everyone our photos and videos - so it's all in the cloud already.

Now the Object World is a great place to enter with the intention upon agreeing to a common ground.
We would all benefit from.



## House rules. Different Houses.

Anyone may set up an AHFX-compatible environment, and have their own "house rules".

If too many users kick each other out of the first AHA-Space, publicly provided, where shall the "kicked users" go? Since AHFX is and shall always be FOSS - there shall be any proper implementation available to setup your "own Object World". And then figure out a way how to transition your Data-Objects between those "Worlds".

Yet it is encouraged to fork of into a new Realm before setting up a new World.

So we have Realms and Worlds now.
In a digital Universe.
Quite big, and still with individual house rules.

If you set up your own AHFX system, you can (just like with your own web-server at home or anywhere) decide what's happening - and what isn't.

If you have someone else running an AHFX system, and you like/trust them: You can get the service from them.
Just like you do now.

This is mentioned here in the security paper, because this trust-access model expects that if a certain level of dis-trust is reached, a Realm is either forked - or groups split up and run their own AHFX system (World).

In any way:
It is better to fork off than to wage wars - of any kind.
Let's just meet if we like to.
Why virutal things, if we can't get our peace of mind every now and then.
And I happily welcome you into my "domain" if we agree to engage in mutual respect.

Sounds too bold?


## Object Spaces

I've written this down already somewhere else (TODO: Find and copy here).

Imagine each Object can be accessible (be in) a virtual Space.
Like a disk "space".
It's stored somewhere.
You access it it from somewhere (else).
Can you do that?

Object Spaces are simple tags you can assign to any Object.
It's like drawers or rooms. Mind-spaces.
Mind-palaces, if you will.

Imagine Object Spaces like virtual-reality chatrooms.
(At first interacted with through a 2D computer screen)

If 2 Objects are in the "same Space", certain "rules" apply.
A "rule" is an Object Graph that declares (in a machine-readable way, yet plaintext) code-scripts.
A code-script allows to verify or transform any "incoming" Data Object.
Or be a plaintext human-readable banner that shows up as an alert message when you try to "enter" a new Object Space.

If nothing else, it is primarily used for simply "grouping" Data.


## Security and boundaries?

If you tag an Object (or Graph) as *private* it stays private.
That is, that any AHFX-compatible component is considered common courtesy and good will to apply the respect for Object Spaces.

So whenever an Object would be accessed from within a "different" Object Space, you'd get a notice.
You can configure - and there's supposed to be good default presets - simple yes/no/if rules, like email-filters to decide which Digital Space Transitions you'd like to auto-accept, which to decline - and which to be informed of.

Like a default user-firewall.
Could be annoying.

Actually, it could be treated like a "local WWW".
Object Spaces can and should be used locally as well, too.
Merely setting a filter on/off: online=yes/no.

Yet, Object Spaces - can be used for so much more:
If a Space provides running code to be executed by anyone entering: It's like a tech-given ritual to shake hands and engage in a trusted relationship: I execute yours, you execute mine.

Can we now please use a different vocabulary, other than "command execute: run. terminate. exit. die()"?

Terminal.

When Spaces declare their entering rules in valid code, and agree to "do" the other's code, too - we're even.
A Space may well declare their "rules of conduct or whatever" in advance, publicly visible - so it's everyone's free choice if that Object may enter or not.

The Object Filesystem Community would have to agree to a different security paradigm.
Yes, maybe still "read/write/access" permission given to ... - but any community has their own level of preferred security. Shared keys. Let's start with trust. And consider privacy by design.

All data shall be exchanged encrypted with assymetric or equally useful encryption. Let's agree on a digital envelope. Let's be Gentlemen - and be gracious where's plenty.

Object Spaces may also be called Object Realms.
Since any kind of "gatekeeping" functionality is now resolved into other Object Graphs that can be run to perform "border controls".


## Border controls.

I am unhappy with the idea of having Borders. Spaces is better, but at some point we have to agree we don't at all times just want "someone else" peeping in. So we need private Spaces. And therefore some means of "who may enter" have to exist. At least for me.

Therefore I chose the term "Realm" for Data Objects.
A Realm is merely a String plaintext term - like a Chat Room. 
First come, first serve - Let's support DNS as base Realm authentification method here.

Everyone who runs a data service, has to provide running code for the other to execute. And vice versa. By default, that can even be a simple name=value J/N list, that each of you define - plaintext - and check if you "agree" on your conditions.

The big difference is, that: Now *they* must agree to run *your* code.
Who has to draw first, is btw declared by the PT-AHFX Standard:
Larger Graph runs the other's code first.
Be that Great.

The ones who write the actual code, and the ones who run it - practically define "what is happening and what is not". All plaintext visible publicly. Unless declared "In this Space only". You get the idea.

Network security administration would be sysadmin- or -bot chats with someone "from the other Realm".

Yes, any communication on this network would be fully https'ed (in a way) and auto-gpg-signed, so we'd all "know" whom we're talking to.
Where the initial certificate came from: Who cares. But it has to be public, and I can decide how much I trust in that. Let's be excellent to each other.

Important though: It is encouraged to clean logs as desired. Keep as long as minimally necessary.


## Weighted/conditional Rules

Object Space Realms have transition/entering rules.
You may not leave with any Object tagged ...
You shall not try to export Objects tagged ... in any kind.

Yes, I'm pretty sure we'll see demands of that kind pretty much from the beginning.

With an option to put a "severity" level on a transition-rule, it may be so that not all rules are always executed. Not only speeding up transfer, but also putting the option for literally *digitally* letting it slip through.

No security shall ever be perfect.
If we manage that we may as well kill ourselves.
I hope not.

Let it go.
If there's a problem, go and solve it - but don't just lock everyone out.
Why would anyone "break into your realm"?
Most people are already knowingly and willingly - and seemingly (mixed/un)happy about it:
I have nothing to hide anyways, so why bother?

Weighted rules also allow to make it easier to travel between Realms:
You just need to be bothered with what you configured to be notified of.

Filtering of weighted/conditional rules can be evaluted and implemented as 
it's already been done in any web-browsing application today.

The same thing, simply by considering "a realm" technically "a website". With
common Data-Object access. Filesystem *is* the database. As configured. It's exactly like using a web-browser
these days.

You could call this new access handling a Trust System - or Commons Access Conditions (or so).
The Space rules can be called "invitations" - and the user's wishes, still "a menu"?


## The Intarweb 1.0

Remember your first time on "The Internet"?
I do.  
I even have a printout with timestamp and URL.  
Because my Dad thought it was cool that you could search "anything" in the world.  
I looked up song lyrics.  
It was amazing!!  

When we put up our first HTML textfiles on an FTP - we were kids. And yet we
were fully aware that we are now "putting something online public for anyone
(!) to see". And there were many things we knew we'd *never* publish online.
ever.

So if we introduce a new "Space of Realms" in the already omnipresent Digital
World, why not agree that we agree to enter a new Space. Where we could start
being nice to each other. For once.

If we're not, we can just stop the service demons, change URL and relaunch as
other "Realm".

It's exactly what's already happening practically all over the world, all the
time with most online projects. Successfully.

So The AHA-Object World would be a subspace on the Internet, where things just
work - and working with Data is almost haptical again.


## Fuzzy borders: optional

The boundaries between "you are here" and "somewhere else" are Object Space Clusters.
Why Clusters?
Just data "blips" of matching tag values could visually be displayed as a clustered cloud. Gravity defined by sum of equal terms.

So instead of defining Space borders, code-rules are built to respect tag-overlaps. Rule execution is then by community tag-voted up/down to "enforce" rules on Objects whose tags "don't overlap (=agree) enough". Realm-Tags declare security and interest and context boundaries. By filtering out Objects that "stray too far" (according to their accumulated tags).

Simply merging weighted graph networks of filters against equally constructs of indexed matching tags. Cloud against Cloud. Filter against Data. Executing code on condition.

But this goes too far out.
This is more something for a SciFa Novel series of "How proper Metadata-Handling suddenly changed everything for the better". ;)



