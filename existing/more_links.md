The ANSI T10 object-based storage standard and current implementations

D. Nagle; M. E. Factor; S. Iren; D. Naor; E. Riedel; O. Rodeh; J. Satran
Date of Publication: July 2008

(Download behind login-wall)
https://ieeexplore.ieee.org/document/5388616/authors#authors


Object-based Storage
Devices (OSD)
T10 Standard
Erik Riedel
Seagate Research
November 2003

https://www.t10.org/ftp/t10/document.03/03-394r0.pdf


# The Oasis

(referring to Ready player One?)

https://ieeexplore.ieee.org/abstract/document/5937220


 Abstract:
In this paper, we present the design and performance evaluation of Oasis, an active storage framework for object-based storage systems that complies with the current T10 OSD standard. In contrast with previous work, Oasis has the following advantages. First, Oasis enables users to transparently process the OSD object and supports different processing granularity (from the single object to all the objects in the OSD) by extending the OSD object attribute page defined in the T10 OSD standard. Second, Oasis provides an easy and efficient way for users to manage the application functions in the OSD by using the existing OSD commands. Third, Oasis can authorize the execution of the application function in the OSD by enhancing the T10 OSD security protocol, allowing only authorized users to use the system. We evaluate the performance and scalability of our system implementation on Oasis by running three typical applications. The results indicate that active storage far outperforms the traditional object-based storage system in applications that filter data on the OSD. We also experiment with Java based applications and C based applications. Our experiments indicate that Java based applications may be bottlenecked for I/O-intensive applications, while for applications that do not heavily rely on the I/O operations, both Java based applications and C based applications achieve comparable performance. Our microbenchmarks indicate that Oasis implementation overhead is minimal compared to the Intel OSD reference implementation, between 1.2% to 5.9% for Read commands and 0.6% to 9.9% for Write commands.
Published in: 2011 IEEE 27th Symposium on Mass Storage Systems and Technologies (MSST)
Date of Conference: 23-27 May 2011
Date Added to IEEE Xplore: 04 July 2011
ISBN Information:
ISSN Information:
DOI: 10.1109/MSST.2011.5937220
Publisher: IEEE


# Blog.x.com: Twitter's in-house photo storage system

https://blog.x.com/engineering/en_us/a/2012/blobstore-twitter-s-in-house-photo-storage-system

Quote:

```
Millions of people turn to Twitter to share and discover photos. To make it possible to upload a photo and attach it to your Tweet directly from Twitter, we partnered with Photobucket in 2011. As soon as photos became a more native part of the Twitter experience, more and more people began using this feature to share photos.
 
In order to introduce new features and functionality, such as filters, and continue to improve the photos experience, Twitter’s Core Storage team began building an in-house photo storage system. In September, we began to use this new system, called Blobstore.

What is Blobstore?

Blobstore is Twitter’s low-cost and scalable storage system built to store photos and other binary large objects, also known as blobs. When we set out to build Blobstore, we had three design goals in mind:

  * Low Cost: Reduce the amount of money and time Twitter spent on storing Tweets with photos.

  * High Performance: Serve images in the low tens of milliseconds, while maintaining a throughput of hundreds of thousands of requests per second.

  * Easy to Operate: Be able to scale operational overhead with Twitter’s continuously growing infrastructure.
```
