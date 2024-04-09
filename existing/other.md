Possibly related, existing projects/things:


# https://www.databricks.com/

[Introduction to Data Lakes/Lakehouse (by DataBricks.com)](https://www.databricks.com/discover/data-lakes)


# https://solidproject.org/

[W3 Solid Community Group](https://www.w3.org/community/solid/)
[Solid Specification (Github)](https://github.com/solid/specification)


## Scope

Source: https://www.w3.org/community/solid/charter/

```
In general, topics that are “in scope” include anything related to enabling affordances for decentralised Web applications to create and use data across decentralised storages in a way that is secure and privacy respecting for individuals and communities. Work items are intended to be compatible with or extend the Architecture of the World Wide Web. These topics include, but not limited to, the following:

    Protocols for the storage, transmission and portability of data.
    Authentication and authorization mechanisms.
    Notifications.
    Query interfaces.
    (Meta)data models that can be used in storages, e.g., policies, data privacy and rights, provenance records and auditing, error messages.
    Profile descriptions for social and software agents.
    Data interoperability: sharing semantics of the content of resources, e.g., data shapes, data portability.
    Service interoperability: sharing semantics on the discovery of actions and access to resources, e.g, web service descriptions, provisioning, portability.
    User interface affordances: the display of data and services in a view.
    Vocabularies providing the necessary semantics for the mechanisms defined within the scope of this group.
    Signing messages.
    Federation, e.g., message passing, trust, data cascading.
    Evaluation tools (software programs or online services) that help determine implementation conformance.
    Publishing test reports and communicating the level of adoption of technical reports.

With the exception of integrating or bridging specifications developed by another active community in an open standards development body that specialises in a particular topic, the Solid Community Group defer the work to the other community.
```


# https://flur.ee/

From Content to Knowledge

Best-in-class content classification and tagging software, powered by NLP.

Fluree Content Auto-Tagging Manager transforms unstructured data into semantically organized content that is searchable and available across your organization.




# https://www.enterprisestorageforum.com/hardware/file-system-management-is-headed-for-trouble/

This is from 2009 - yet I think Newman is addressing similar concerns regarding
'the [classical](POSIX) file system interface isn't up to the task of managing
today's data'"

By Henry Newman
February 24, 2009

> "The POSIX file system interface isn’t up to the task of managing today’s
> data, resulting in costly fixes for users to solve problems [...]"

> "The problem with management of files is just that: they’re being managed as
> files, not as information. The standard POSIX information is far too basic.
> There are applications like Google Desktop that help you find what you’re
> looking for, but that solves only part of the problem."

> So why has no one done this yet? I think there are a number of reasons:

  * Vendors do not want to make changes, and any changes to the POSIX standard
    would require both file system and operating system changes.

  * Vendors are making money on user space applications. This is a poor reason,
    but I believe it is likely true. If something was standardized, then you
couldn’t sell it.

  * These changes would generate more overhead, as you will have additional
    space for attribute data. This will increase the size and space needed for
file system metadata (inode data) and will increase the time to open and read
files.


