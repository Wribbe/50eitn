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

# QUIZ SECNET
## Crypto:
### Recall how RSA and Diffie-Helman (DH) work. RSA can be faster than elliptic curve variant. Note the bit size in the tables for getting RSA and ECC of equal strength. Why is RSA with public key much faster than with RSA cloud and private key? The computational complexity of RSA: a^e mode N can be described as ``` O(n2) (#one bits in exponent e) ``` where n is the number of bits of the number N. Recall that DH uses the same type of arithmetic as RSA. 

### In which cases is ECC better than RSA?

### In a DH protocol how small can you make the exponents? Why does this differ from the situation where we use RSA for a key agreement (such as in slide 69/Lect2)

## Key handling:
### What is OoB? Key type: session, short –lived, master keys?


### Simmons’ Bound. Key entropy loss as result of protection (probability of impersonation).

## Crypto and Quantum computing:
### How is key size affected for symmetric crypto algorithms? What happens with public-key crypto algorithms?

## Authentication:
### What does AAA stands for?

### What is a challenge-response scheme and what is it used for.

### What can be used for authentication? What is two or three and multi factor authentication?

### What is CHAP and how does it work?

### Radius: how do the two Radius alternatives work? Where is the key stored used during the authentication? Compare here the two alternatives. Pros and cons to use alternative 2?

### What is Diameter?

### Give some examples of features that make Diameter better than Radius.

### What is EAP and what is its purpose?

### What is EAP-AKA?

### Explain how EAP-AKA can be used to give seamless WiFi network access (no need for entering WiFi network password).

### Explain token types.

### Kerberos scenarios. Understand how they work (no need to memorize how they work)

### Recall how authentication works in GSM, slide 4-5/Lect3. Role of A3.

### What is GBA and what is it used for? Understand the diagram of the GBA solution

## Secure Connections:
### Explain why we use session keys? In a secure transport protocol what are the roles of the subprotocols on Slide 64/Lect2?

### Consider difference of RSA and DH based key agreement. Difference in performance. How hard has NSA to work to get at the agreed key in either scheme?

### TLS 1.3 and QUIC; what are their round trip improvements over TLS1.2

### DTLS vs TLS.

### IPsec: what protection do the AH and ESP protocols give you? What is tunnel and what is transport mode. See also for example your computer security book.

### Can we do manual key insertion in IPsec? What is IKE? Which key agreement is at the core of IKEv2? Why do we use certificates in the Main mode?

### What are the problems with IPsec and NAT. Which IPsec (sub)protocol is blocked by NAT? Explain why?

### Use of UDP to get IPsec ESP through NAT device, how? Two problems with NAT-T

### What is opportunistic encryption?

### What is object encryption and when it is a good choice to use it?

### GSM authentication (understand how it works, where are they keys) and the 8 encryption algorithms

### What is a false base station attack and why is it possible?

### Understand principle of 3G authentication and why it helps against false base station attacks. Why we XOR the AK to the sequence number SQN? What is the role of this sequence number?

### Explain trust relations in the LTE architecture show in Slide15-16/lect3. Explain what is backward and forward security and which threats these solutions provide a counter measure for? X2 and S1 handover: what is the difference with respect to forward/backward security?

### What is key derivation and what is a key derivation function?

### Why do we have so many keys in the LTE key hierarchy, Slide17/Lect3?

### IoT: For small IoT devices what is more critical energy spent on processing or on transmission? What is the consequence of this?

## Botnet:
### What is botnet and how are they organized?

## DDOS:
### What is the role of the command centre?

### What is C2?

### Understand the role of two evasive techniques (no need to remember details).

### Countermeasure against (D)DOS attacks.

### What is black hole routing?

### DNSEC and DDOS: Why is DNSSEC not so good from DDOS perspective?

### DNS amplification attack, how does it basically work?

### Reflection attack, how does it basically work?

### Mirai botnet: what is it and how is it established (increase it’s attack power)?

### Mirai botnet: what are its main phases?

### Mirai botnet: what is attacked and by how many?