# Useful shortcuts/aliases

```
alias öe='tracker extract'
alias ös='tracker search'
alias gx='getfattr -d -m - '
```



# Shell magic

## Create a "thin copy"

`$ cp --attributes-only --preserve=all song.mp3 song.xxx`

This copies all extended attributes (key/value pairs) from `song.mp3` to `song.xxx`, but leaves the actual "file payload" behind. Therefore `song.xxx` will be a 0-Byte file, yet contain all xattr information from the source (`song.mp3`) as-is.


## Alias to list all xattrs

`alias gx='getfattr -d -m - '`

  * -d: dump (=show)
  * -m -: match all/any

Simply used to quickly show/list all existing xattrs of any file/folder object:

`$ gx song.xxx`
