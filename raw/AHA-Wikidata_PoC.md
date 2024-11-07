# Ŕunning a Wikidata Data-Copy on AHAlodeck.

2024-11-05

btw, here: magnet:?xt=urn:btih:0852ef544a4694995fcbef7132477c688ded7d9a&tr=https%3A%2F%2Facademictorrents.com%2Fannounce.php&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce

That's a magnet link for a fairly recent dump of Wikidata (all.json.gz, around 130.6 GiB).
Knowledge data of the world out of thin air.
A mere magnet link.

Indeed.
Would this be possible?
Would it make sense to host a local instance of Wikidata?

For performance testing, maybe indeed.
If the performance is useful, maybe even more to come...

The code to migrate and boot should be trivial:

  * Connect to wikidata.
  * Or: Get an offline dump in a way you can query it (DB which?)
  * Iterate through all objects, and copy all key-value pairs.
  * Keep all data (references and values) simply as-is.


How much can that be?
It's just metadata: How much can it be?
(TODO: check if Wikidata published that, if dump is available, and maybe even contact someone there)

Anyways: What are the steps to store that database content as AHAlodeck annotated object structure?
In a way that is scriptable for a one-off migration.

Hardware im Aug:

  * 2x 20 Xeon? Cores mit irgendwas um die 3.2 GHz pro Kern.
  * Supermicro server board (millionen SATA/SAS Anschlüsse für Platz)
  * 128 GB ECC RAM
  * Noch die Hälfte an DIMM slots frei.
  * Etliche PCIe-8x+ glaub' ich. Zumindest 2x volle Länge Slots.

Geht sich das aus?
Wie groß ist Wikidata?
Ich brauch's ja nicht im RAM.

Dorthin hol' ich mir nur Query-Caches.
Schreiboperationen sind ein anderes Thema vorerst.

Eigentlich: "solved as: the way wikidata does it. It's FOSS."

Und dann was?

Then I'd have a quite generically useful "data model" to test performance on.
And by having Wikidata in my "memory pool" then anyways, references to its data could be considered "like native-locally supported".

UPDATE: So the current latest dump of "wikidata.entities.json.bz2" is around 90 GB in size - still downloading...

Then what?

Access it read-only and write code to generate/convert this to AHAlodeck annotated folders.
In's RAM krieg' ich's nicht als Ganzes.
Muss ich das überhaupt?
Wie schaut der Index über diese Datenmenge aus?
Größer? Kleiner?
Jedenfalls ein glaub' ich brauchbarer Korpus an Test-Echtweltdaten der relativ easy programmierbar importiert werden kann.

Und *der* (also der Cache/Index) ist dann im RAM - und auf der NVMe - und dann SSD - und dann HDDs.
Also, ich glaub' wir haben noch kein Speicherproblem mit Größe und so.
Sind immer noch "nur" Metadaten.

In dieser Version.
Später ist schon die Frage wie's mit "HSM" functions ausschaut bzgl:

  * Metadata = lightweight, fast - easy to access and edit/update.
  * Payload = heavier, larger - slower to access, yet makes sense to cache and hierarchical-tier-structure somehow.

Ich will einfach "Daten" wegspeichern können. Mit ID und attributes. Und Boardmitteln in jeder Umgebung, die mit dieser Art des Taggings umgehen können.

`Meta equals Data`: payload is yet-another key-value. Slightly or signifcantly larger than the others ;)

What if there could be more than 1 "big chunk" - and "big" is relative. Especially in computing.
Anyways: Just "tag that thing with that thing".

And live with it.
It's amazing, you'll see.

But that's for another time.

AHA-PT7=AHAlodeck by August, ProtoType VII


# IDEA:

Write an XSLT that generates an executable of any XML to create a copy of itself as AHAlodeck Objects in FinF.
