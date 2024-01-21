# To clarify: Kernel vs Userspace vs Other

2024-01

Disclaimer: I am not a Kernel hacker, and only know about OS-kernel-things from university and as a programmer myself.

Here's how I understand it:

  1. Basic, common funcationality may be implemented on the kernel's filesystem (driver?) level.
    For speed and reliability.

  2. Other (even considered basic) features should probably be implemented in Userspace.
    For convenience of development and interoperability.
    I imagine something like [POSIX (Portable Operating System Interface)](https://en.wikipedia.org/wiki/POSIX).

  3. Even more high-level functionality that is considered "more specific" or "more complex than average".


Some features that would make AHFX really powerful, may be functionalities that
are too complex to belong on a filesystem driver-level, but should be "taken
for granted" and reliable enough to be available on any computing environment
(if anyhow possible).

Similar to a unix-ish system:
Some commands or other things are on 99% of all environments. Some are more
specific. There's great benefit in any common ground though. With AHFX to work
at its best, it should be similar.


## Why should anyone be interested in programming that?

Because it makes perfect sense.

Having meta+data as reliably stable anywhere-FS like fat32 but open and FOSS and for the people, by the people. Paid for a living.

Imagine your personal or business use-cases:
Your default filesystem *anywhere* may actually be a fully interoperable DAM out of the box.

Local, LAN and remote up to large-scale clusters.

Not all-size-fits-one, but rather:
Basic components that all behave the same and do their job.
Unix-philosophy applied to the filesystem.

With computing, processing and data-IO powers of the 21st century.
M.2, SSDs, Flash-whatever - including tons of RAM, several CPUs on one board, PCIe, Thunderstuff(tm) and all.

Just lego that filesystem paradigm and let the hardware crunch the numbers.


