# QUIZ FORENSICS
## General: 
### Computer vs Digital forensics: same or not? 
No. Digital forensics eclipses computer forensics, it refers to ‘digitally stored data’. Data-driven vs device-driven. 
### Computer/Digital forensics results are used by? 
Criminal justice agencies, prosecutor’s office/DA attorneys judges, corporate councils, company legal resources, HR, auditors, ‘individuals’, crackers/hackers.
### Computer/Digital forensics is about? 
Using scientifically derived and proven methods in order to acquire, handle and draw conclusions from data, to be able to have evidence or to predict unwanted actions.
### Which are the 4 main steps in Digital forensics? 
1.	Seizure
2.	Acquisition
3.	Analysis
4.	Reporting

### Digital forensics is not? 
Proactive (reactive), about finding the bad guy (find evidence, not bad guys), something you do for fun (legal limitations on seizing data), or quick (lots of data, encrypted/hidden data).
### Use of hashes to detect changes of seized data, why? 
It’s a one-way and quick operation.
### Types of Digital forensics? 
Network, memory, computer, cloud 
### What is CERT? CERT in Sweden. 
Computer Emergency Response Team. www.cert.se is part of Myndigheten för samhällsskydd och beredskap. Skyldiga to report about incidents and threats.
## Incident handling: 
### Incident handling terms (4) 
Event

Incident

Vulnerability { technical, administrative }

Lots of other terms, attribution, alibis and statements, intent, evaluation of source, document authentication
### Incident Handling is a process 
*-> Prepare -> identify -> contain -> eradicate -> recover -> follow-up (-> report) -> *
### Event correlation, what is it? 
Correlation between events? Not clear from slides
But, prob to draw what conclusions one can. One slide about User <=> platform <=> OS <=> logon <=> application <=> data
### Chain of custody, what is it? 
How evidence is retrieved. Notably, legally / illegally. US vs. Sweden. Sv. Spårbarhetskedja.
### “If it is on, leave it on – if it is off, leave it off.” Why? 
Several reasons. On: data in RAM, unable to authenticate once out, example with filesharing computer on university where OS was loaded from USB drive (which was removed after loading) and running in memory, processes running, yada yada yada. Off: self-wiping discs, logging, sending alerts to other cronies yada yada.
Note: may not be true w/ mobile phones, because of garbage collector / memory manager could rearrange files and/or delete parts of obsolete files.
## File systems 
### File allocation: basic, deletion, slack space: (see also Altheide video 23:50-26:50)
Deleted files: only removes pointer to file, not actual file (will be part of / transformed into slack space). Slack space: elephant grave yard for files.  
### Allocation in Flash (SSD). Pages, : (see Altheide video 27:50-32:40) 
Can only write one page at a time, can only delete one block at a time, no slack space.
### Problems with flash: wear leveling (see Altheide video 28:50), deletion(30:00) 
Wear levelling: flash can only be written to a finite number of times (typically 100k or smth), to mitigate this flash memory writes ‘here and there’, or “randomly remaps” blocks.
Deletion: see above.
Garbage collector and TRIM, wipe freed blocks in background (grbg) or on demand (TRIM). Clears unallocated space. Eliminate slack space (does not even/often exist in flash? Maybe done by this feature 😊 )
### Basics of how FAT is organized, sectors, heads, cluster, FAT table, 
### Analyzing Volatile and non-volatile memories. 
### Cooling down of RAM, why? 
He means spray-cooling RAM? If so, can ‘freeze’ (hehe) the state of the RAM, this allows one to connect it some other place/time/etc and analyse it, won’t lose data in RAM like if seized computer would just be turned off.
### Slack and wasted space of non-volatile storage 
## Analyzing documents/pictures: 
### Importance of metadata 
Not always deleted, can say more about a file than one thinks
### Where can data be found: allocated space, slack space, or both? 
Both. ‘Alive’ or ‘existing’ files in alloc, ‘dead’ or deleted files in slack space
### Cloud systems and computers/devices: storage is in cloud. Consequence for forensics, cloud forensics (see Altheide video 57:00-1:15:00) 
## Mobile phone memory analysis 
### Forensics of devices/phones (see Altheide video 51:40-57:00) and Willassen paper. 
### Storage data on SIM vs storage on device own memory (sec 2.1, 2.2) 
### How to prevent memory contamination? 
### How to obtain an image: desoldering, jtag reading 
Like in Norwegian article, removing BGA ICs, resoldering solder balls and debugging the IC.
### What is jtag (Google , for example http://www.corelis.com/education/JTAG_Tutorial.htm or first pages of http://www2.lauterbach.com/pdf/training_jtag.pdf ) 
A standardised interface for debugging hardware

First, a task action group, i. e. a committee.  Secondly, IEEE-1149.1 aka JTAG aka boundary-scan (?) aka In-system programming aka XBOX hacking aka embedded instrumentation. 
### What is boundary scan? 
Test physical connections of electronic product (through using JTAG interface), make sure no faults due to loosened pad, cold solder joint, mechanical stress etc.
## Data hiding 
### Steganography: meaning? 
Hiding data within other data. E. g. hiding a msg (hidden_data) within an img (cover_medium) file by replacing first bit of each pixel value with one bit from msg. 

```
cover_medium + hidden_data + stego_key = stego_medium 
```
### Use of encryption as part of hiding.
Encrypt first, then hide. 
### Watermarking: meaning? 
e. g. printers, printing small yellow dots w/ date and time info etc. Copy protection and deterrence. Protect material from malicious use. 

Visible / invisible watermarking. 
### Use of spread spectrum technology. 
Sort of the same as with fileception, but don’t know the mechanics of it. 

Mechanics: add a noise-like signal and detection “via correlation”.
“Add a noise-like signal and detection via correlation.”
### Data hiding terms: embedding, robustness 
Embedding: The actual hiding of data. Which algorithm used (e. g. first bit, n:th word of every sentence etc.) 

Robustness: the ability of the hidden msg to remain undamaged even if stego_medium undergoes transformation, etc.

Tamper-resistance: Even if attacker is successful in destroying the steganographic technique then tamper-resistance makes it hard to alter or damage hidden_data.
### Magic triangle: tradeoffs 
                    Capacity
    Undetectability		Robustness 
Cap: “Naive steganography”. Better, how much information can be hidden in cover_medium.

Undet: secure steganographic techniques

Rob: Digital watermarking
### Detecting of hidden data vs extraction of hidden data: why is extraction not possible even if it is detected?
Because hidden_data may also be encrypted?
