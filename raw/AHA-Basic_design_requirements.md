# Holodeck that shit.

I imagine the following to be rather trivial (seriously. Mainly because i mean: "there's already working code for that, or the code required should be quite basic").

1. Setup an Object Storage: MinIO
2. First setup: Single disk/folder, single pool, single host.
3. Import existing objects: Fotos, videos and documents folders to now be "Data Objects".
4. Add metadata "name=value" to a selection of such Objects.
5. A query possibility to "select from ... which name=value, or relate to ..." for Objects.
6. Simply store source folder/file names as name=value pairs:
`folder=/this/is/where/it/came_from` and `filename=CAM00001.jpg`
7. Implement proper NextCloud WebUI support.
	To really access/browse all Objects folder-free (optional view/plugin) including IIIF-compatible plugins for viewing/editing.
8. Support auto-fetching (harvesting) of popular FOSS/open-licensed platforms, like WikiData, GND, etc. to "fatten up" the relationship and annotation details of your Objects.
9. Audio player to use Object's filesystem metadata (name=value) tags instead of embedded.
10. De-embed all metadata in one run.
Simply put together a sane collection of FOSS metadata extraction tools for all kinds of file-formats. Sorted by interests and accessibility. Theoretically practically open-ended and freely editable.
11. Right-click: Edit Metadata.
A simple nested name=value (JSON-ish?) display/editor for metadata.
12. Support profiles
