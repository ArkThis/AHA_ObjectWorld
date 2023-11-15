# Transformations in the AHA Object World

Assume we have several Objects - related and with such properties, that you have all the data for the following OAIS information package types:

  SIP
  AIP
  DIP

SIP comes in: Original data as provided by that source. Can be a file/folder package. Maybe structured.
In any way, it is what it is.

Imagine this data simply stored as Objects. As-is.
Merely as related Objects to this Meta-Object (or adding this tag as Metadata):
`source=Provider`
`oais_package=SIP`



Done.

Now the AIP:
Do whatever archival-Fu is necessary and convert, improve, annotate, convert or fix - 
to the SIP Object data. Maybe relate it to other (existing, local or remote/online) Object references.

And tag all new Objects created in this step, with the following tag:
`source=USERNAME`
`oais_package=AIP`
(And any other information you like to add during this step)

You may also add the `oais_package` tag to any existing Objects to group them by tag.
Or create a Meta-Object with that tag - and relate any desired Objects of your current set.


You now have a bunch of related Objects.
All equal "like Files (in the past)".
Just there on your storage.


Which you can now query.


Which brings us to the DIP:
Maybe you want to create a trimmed version of a videoclip or movie sequence -
or convert one text/image/file format from one (AIP/SIP) copy to a new one.

Add tag (or relate a (new) Meta-Object):
`oais_package=DIP`
(And any other information you like to add during this step)

Create or re-use Metadata (Objects).


You now still have "just a bunch of related Objects".
All equal. Like Files in the past.
Just there on your storage.

Backup, Failover, Redundancy, etc:
All covered by default basic IT routines and applications.
Because it's now mostly "just taking care that the filesystem works properly".



So you now still have just a bunch of related Objects laying around.
Yet, they're at least tagged.
They become query-able. You don't have to know their filenames or folder
"locations" - because you can simply "ask for what you want":

Q: `select * from 'test-collection' where oais_package=SIP`
Q: `select * from 'test-collection' where oais_package=DIP`
Q: `select * from 'test-collection' where oais_package=AIP`


There was no folder-file structure renaming step necessary in the lifetime of
all these files and workflow tasks.

When you have extracted certain existing/known metadata for the SIP files (and
in subsequent steps), you could create your AIP, by running queries and scripts
on your SIP Object Set:

  * `select * from 'test-collection' where oais_package=SIP and source=$USERNAME
    and filetype_mime=video or filetype_mime=film from my_object_storage;

  * Offer to perform predefined conversions using ffmpeg, etc.

  * Create Descriptive Metadata entries as "Meta-Objects" or additional tags
    with the Objects.

  * Since handling this kind of data and queries is now basic filesystem
    operations, performing these operations could even be understood and done by
regular users. Because it'd be how they interact with *any* data on a daily
basis, anyways.

One of the interesting features of AHFX is that it reduces complexity, since
complex use-cases (and previously "formats") are now merely larger graphs with
more nodes, more data, and possibly professional metadata.
