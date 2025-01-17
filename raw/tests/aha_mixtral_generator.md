Would you be so free and please write me a python qt5 (qt6-compatible) gui with the following features?

1. A table-view of extended filesystem metadata (such as xattrs)
2. By columns "key", "value"
3. Showing the "user.\*" keys of the filesystem. Editable.

Thank you :)

Wow!


# Step 2: Tree-View

1. Same data (xattrs user.\*) shown as folder/file tree widget.
2. folders (in tree-view) are the folders *and* files (of the source)
3. filenames of the files (in tree-view) are the "key" strings from the source.

Thank you :)
All the best!


# Step 3: UI pimping 1

1. folders (tree-view) are colored differently whethere their source was/is a folder or a file.
    (default: a decent green/blue) - or any other nice visual indicator for this information.
2. The default prefix is "user.\*".
3. This prefix can be configured in a variable (configfile)
4. And is hidden by default, but has a config-option to show/hide it. (config file + GUI menu, please)
3. A button to "add entry" adds a new pair of key/value filesystem attributes.
4. A "save" button saves all edits back to the filesystem, and makes sure that operation was successful.
5. If that validation-step causes significant performance, make it an optional GUI+config option, too.

Thank you :)
This is amazing!



