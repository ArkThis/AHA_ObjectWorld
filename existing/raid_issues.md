# https://qumulo.com/blog/erasure-coding-vs-raid-explained/

Authored by: Qumulo Team 
December 28, 2021


# RAID, flash and erasure coding: What works best with solid state?

By Stephen Pritchard
Published: 04 Dec 2020 

https://www.computerweekly.com/feature/RAID-flash-and-erasure-coding-What-works-best-with-solid-state

## Abstract

We look at RAID and flash to highlight key choices when it comes to drive data
protection. What RAID levels work best with solid state and when is erasure
coding a good choice?



# Does RAID 6 stop working in 2019?

https://storagemojo.com/2010/02/27/does-raid-6-stops-working-in-2019/

by Robin Harris
Saturday, February 27, 2010 

Refers to Adam Leventhal's article from 2009

## Quotes

> "The crux of the problem:
SATA drives are commonly specified with an unrecoverable read error rate (URE)
of 10^14. Which means that once every 200,000,000 sectors, the disk will not be
able to read a sector.

2 hundred million sectors is about 12 terabytes. When a drive fails in a 7
drive, 2 TB SATA disk RAID 5, you'll have 6 remaining 2 TB drives. As the
RAID controller is reconstructing the data it is very likely it will see an
URE. At that point the RAID reconstruction stops.

> Here’s the math: `(1 – 1 /(2.4 x 10^10)) ^ (2.3 x 10^10) = 0.3835`

> **You have a 62% chance of data loss due to an uncorrectable read error on a 7
> drive (2 TB each) RAID 5 with one failed disk, assuming a 10^14 read error
> rate and ~23 billion sectors in 12 TB. Feeling lucky?**
>
> When 4 TB drives ship later this year only 3 drives will equal 12 TB. If they
> don’t up the spec, this will be a mess.


## Comments (2018)

User: "beloncfy"
on Monday, 1 October, 2018 at 7:26 am

> SSD and ZFS solved all of these. Even RAIDz (which is RAID5 equivalent) is
> still working as reliably as before.


User: Robin Harris    
on Monday, 1 October, 2018 at 3:38 pm

> And there’s a reason for that, in the ZFS case at least. Adam Leventhal,
> whose research my piece was based on, was also one of the ZFS developers.
> Fixing the RAID problem was definitely on the ZFS developer’s minds.  
>
> As for the claim that SSDs have fixed this: it’s hard to know, as not all
> SSDs have a URE spec. Seagate’s Nytro series does, and it’s 10 to the
> negative 16, which supports your claim. Disk drives have also tended to up
> their spec as well, so the issue is less relevant today.
>
> And, of course, much of today’s new storage capacity doesn’t use RAID at all,
> preferring either triple replication or advanced erasure codes that offer
> greater capacity efficiency and greater failure tolerance.
 


# https://www.datamation.com/storage/raids-era-may-be-fading/

By Henry Newman
September 25, 2009



## Math (62% chance) challenged by User comment (Davis, 2010-03-03)

Please check your math on this section:
Here's the math:
(1 - 1 /(2.4 x 10^10)) ^ (2.3 x 10^10) = 0.3835.
I’ve recalculated it several times and did it different ways, it comes out to
0.28947 which would make the percentage = 71% and not 62% which is quite a
difference.

Result: Original Formula and number seem to be correct, see:
http://www.wolframalpha.com/input/?i=(1+%E2%80%93+1+/(2.4+x+10^10))+^+(2.3+x+10^10)



## Abstract

> "The bottom line is this: Disk density has increased far more than
> performance and hard error rates haven’t changed much, creating much greater
> RAID rebuild times and a much higher risk of data loss. In short, it’s a
> scenario that will eventually require a solution, if not a whole new way of
> storing and protecting data."


## Interesting quote:

> Think about it: Only 8.88 PB of data has to move before you hit the hard
> error rate, and remember that these types of values are numbers that vendors
> say you cannot likely exceed. Consumer-grade SATA drives are pretty scary and
> must be a consideration when talking to low-end RAID vendors who might use
> these drives. A single 8+2 rebuild with 1.5 TB drives reads and writes about
> 28.5 TB (read 1.5 TB*9 drives, write 1.5 TB*10 drives). That means that in a
> perfect world using vendor specifications, we can expect one out of every 312
> rebuilds to fail today with data loss. Moving to the next-generation 2 TB
> drives, this value drops to every 234 rebuilds, and with 4 TB drives it drops
> to every 117 rebuilds.



# Triple-Parity RAID and Beyond: As hard-drive capacities continue to outpace their throughput, the time has come for a new level of RAID.

Author: [Adam Leventhal](https://en.wikipedia.org/wiki/Adam_Leventhal_(programmer))
Published: 01 December 2009

https://dl.acm.org/doi/10.1145/1661785.1670144
https://doi.org/10.1145/1661785.1670144


## Abstract

How much longer will current RAID techniques persevere? The RAID levels were codified in the late 1980s; double-parity RAID, known as RAID-6, is the current standard for high-availability, space-efficient storage. The incredible growth of hard-drive capacities, however, could impose serious limitations on the reliability even of RAID-6 systems. Recent trends in hard drives show that triple-parity RAID must soon become pervasive. In 2005, Scientific American reported on Kryder’s law, which predicts that hard-drive density will double annually. While the rate of doubling has not quite maintained that pace, it has been close.

## Author

Adam Leventhal (born 1979 in the United States) is an American software engineer, and one of the three authors of DTrace, a dynamic tracing facility in Solaris 10 which allows users to observe, debug and tune system behavior in real time.[1] Available to the public since November 2003, DTrace has since been used to find opportunities for performance improvements in production environments.[2] Adam joined the Solaris kernel development team after graduating cum laude from Brown University in 2001 with his B.Sc. in Math and Computer Science. In 2006, Adam and his DTrace colleagues were chosen Gold winners in The Wall Street Journal's Technology Innovation Awards contest by a panel of judges representing industry as well as research and academic institutions.[3] A year after Sun Microsystems was acquired by Oracle Corp, Leventhal announced he was leaving the company.[4] He served as Chief Technology Officer at Delphix from 2010 to 2016.[5] 


--------------------------------------------------------

# Why RAID 6 stops working in 2019

Written by [Robin Harris](https://www.zdnet.com/meet-the-team/robin-harris/)
Feb. 21, 2010 at 10:50 p.m. PT

https://www.zdnet.com/article/why-raid-6-stops-working-in-2019/

More from Robin Harris (Caution! One author = one opinion)

  * https://www.zdnet.com/article/the-end-of-the-raid-era/ (Aug. 16, 2012 at 6:21 a.m.)


## Abstract

"Three years ago I warned that RAID 5 would stop working in 2009. Sure enough, no enterprise storage vendor now recommends RAID 5. Now it's RAID 6, which protects against 2 drive failures. But in 2019 even RAID 6 won't protect your data. Here's why."

## Author

Robin Harris is Chief Analyst at TechnoQWAN LLC, a storage research and consulting firm he founded in 2005. Based in Sedona, Arizona, TechnoQWAN focuses on emerging technologies, products, companies and markets. Robin has over 35 years experience in the IT industry and earned degrees from Yale and the University of Pennsylvania's Wharton School.


--------------------------------------------------------

# Why RAID 6 Stops Working in 2019

Written by John Macy (Technical Solutions Expert, Healthcare Data Management)
Mar 20, 2013


https://www.bridgeheadsoftware.com/2013/03/healthcare_data_growth_tests_the_limits_of_raid_storage_protection/

