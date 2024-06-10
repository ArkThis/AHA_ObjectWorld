# Extended File Attributes

https://en.wikipedia.org/wiki/Extended_file_attributes#Linux
https://wiki.archlinux.org/title/Extended_attributes

> All major Linux file systems including Ext4, Btrfs, ZFS, and XFS support extended attributes. The kernel allows to have extended attribute names of up to 255 bytes and values of up to 64 KiB, but Ext4 and Btrfs might impose smaller limits, requiring extended attributes to be within a "filesystem block". 


`$ setfattr --name=user.checksum --value="3baf9ebce4c664ca8d9e5f6314fb47fb" file.txt`

# FreeDesktop XDG definitions

https://www.freedesktop.org/wiki/CommonExtendedAttributes/

## Proposed metadata attributes

These attributes are currently proposed

    user.xdg.comment: A comment specified by the user. This comment could be displayed by file managers
    user.xdg.origin.url: Set on a file downloaded from a url. Its value should equal the url it was downloaded from.
    user.xdg.origin.email.subject: Set on an email attachment when saved to disk. It should get its value from the originating message's "Subject" header
    user.xdg.origin.email.from: Set on an email attachment when saved to disk. It should get its value from the originating messsage's "From" header. For example '"John Doe" <jdoe@example.com>', or 'jdoe@example.com'
    user.xdg.origin.email.message-id: Set on an email attachment when saved to disk. It should get its value from the originating message's "Message-Id" header.
    user.xdg.language: Language of the intellectual content of the resource. The value should follow the syntax described in RFC 3066 in conjunction with ISO 639 language codes. When a file is downloaded using HTTP, the value of the Content-Language HTTP header can if present be copied into this attribute. See also the Language element in Dublin core.
    user.xdg.creator: Reserved but not yet defined. The string "user" has a different meaning in ROX Contact Manager (creating application) compared with Dublin core (creating person/entity).
    user.xdg.publisher: Name of the creating application. See also the Publisher element in Dublin core.


## Relation to Dublin Core

    user.dublincore.title
    user.dublincore.creator See also user.xdg.creator
    user.dublincore.subject
    user.dublincore.description
    user.dublincore.publisher
    user.dublincore.contributor
    user.dublincore.date
    user.dublincore.type
    user.dublincore.format
    user.dublincore.identifier
    user.dublincore.source
    user.dublincore.language See also user.xdg.language
    user.dublincore.relation
    user.dublincore.coverage
    user.dublincore.rights

