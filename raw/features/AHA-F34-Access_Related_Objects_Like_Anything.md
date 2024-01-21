## Access related objects identical to "local" meta/data.

  * from developer and user point of view:
    If I want to access/query "my_song.title" or "my_song.album.title", it
    doesn't matter if that information is stored directly as:

   object1:
    - title=My Song
    - album.title = The First Album

or as related object structure:

   object1:
    - title=My Song
    - album = object2

   object2:
    - title = The First Album

It may even be over-annotated:

   object1:
    - title = My Song
    - artist = Hooverphonic
    - artist = object43
    - album = The First Album
    - album = object2
    - album.title = The First Album

   object2:
    - title = The First Album
    - artist = Hooverphonic
