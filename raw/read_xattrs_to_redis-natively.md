Something along the lines of:

What if you simply had a low-level command that knews the filesystem structure - and only reads the required metadata parts where the extended fs attributes (xattrs) are stored.

Best case, that kind of fs-metadata would be stored on a different kind of data storage.
Tiering.

Anyways:
When seriously opening up the compunting world to reliable smoothly-interoperable "key/value" tags, it changes everything.

It's worth considering improvements (mostly on performance, the rest is done in widgets and libs) already before they become an issue (thx ffv1.3, for example ;P)

So I would like to do:

`$ some_short_comand search "whatever"

On everything that's already possibly been known (=stored) in my files already. For starters, using exiftool to extract the most popular and viably necessary metadata from almost any embedded container format - and simply copy/paste that (bit-proof) as xattrs on the related Objects.

Awesome thing being:
This can already be applied to conventional (Files-in-Folders) storage types, while smoothly transitioning to Object-ID based storage and computing.


So why not start with:


```
for object in *; do
    exiftool $object > $object.meta
    import_to_redis($object.meta)
done
```


...and then see what else we need?

Like:
Adding `$object.meta += read($object.csv)`.


What other use cases are there?
Alright: Relationships.

Right-Click -> New.
Select "New" -> Rename to "artist.db"

Right-Click "artist.db" -> Edit Metadata accordingly.
Save when happy: Or import by script from existing data sources.

This migration only has to be done *once* btw.
And then all the information already present is capable of being searched, referenced and used for whatever "collection management" purpose you want.

Simply by opening a "files-in-folders" paradigm thinking tech-world into a new way of storing, querying and using "data".

From Playmobil to Lego.


# Next: Move the file-format data header to the xattr layer.

How's that?
Wanna know anything about that "file"?
Right-Click-Checkitout.

On anything.
Anywhere. Linux/PC, Mac, mobile, other, ...


That can't be too hard to write that loop above in Python? 🤔️


2024-07-18

