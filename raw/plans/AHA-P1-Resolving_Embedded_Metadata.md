
## Initial embedded metadata migration 

### Metadata

For each file format to be supported, a simple decoder may run once on a given object data set, to extract all embedded metadata onto the object filesystem layer. 

Most metadata layouts, from name=value over XML, JSON, etc - the object filesystem keeps text-metadata. binary-safe. Always. So any "value" can be a hole metadata set or text dump.

Should work well for most common cases.

