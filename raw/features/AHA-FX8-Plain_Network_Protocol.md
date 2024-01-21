## As plain network protocol

I'm thinking something like a replacement for the IP protocol. On that layer.
Or maybe one above: As network-filesystem protocol.
Or both.

Filesystem objects may be able to serve natively as network data objects.

Each object has its (unique?) identifier, and ObjectSpaces as (network) Realms.
So it has a handle, and could be accessed or copied to other Realms - local or remote.
Filtering/transition/conversion rules for moving Objects between ObjectSpaces may directly be used for firewalling, routing, etc.

Performance may be an issue (at first), but technically it may hold as network protocol.

It could be that some currently necessary features may become obsolete or replaced by more "object oriented" data-package thinking.

Any host on a network may be:

  * A filesystem Object, too.
  * An ObjectSpace realm.
  * Related to other "Objects" (=also hosts, and anything else stored as Data Object)

Any network-specific information could also be attached as plain name=value tags or linked as related objects to the transported objects. 

This involves any data that already *is* set and accessible on the Objects already: whatever is required for local acccess.

If a data object is accessed over the network, like a mounted CIFS/Samba share, any information currently required to function, could then be attached to the to-be-transferred Objects. And that metadata can then be interpreted/used to depict the same functionality as already existing.

This may be familiar to the reason why it's possible to resolve binary file formats into Object structures.
Network protocols were designed to allow wrapping "metadata" around a file payload - and preserving the filesystem properties (filename, folder) and have information to "send/receive it remotely".

It's metadata wrapped around "files".
That metadata *and* payload are now expected on the same level: the filesystem - and in detail: with each data Object.

What metadata would I need to send my Object1337 over a network to you?

  * Any metadata already with the Object.
  * Target/Destination: Some ObjectSpace Realm in a Storage pool of your host (Object).
  * How to get from my place to yours.

