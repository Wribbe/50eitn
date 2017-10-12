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
**OoB**: Out of Bound, not created inside entity but in other place

**Ephemeral keys** contra **master keys**

### Simmons’ Bound. Key entropy loss as result of protection (probability of impersonation).

## Crypto and Quantum computing:
### How is key size affected for symmetric crypto algorithms? What happens with public-key crypto algorithms?

## Authentication:
### What does AAA stands for?
* **Authentication** - Is this the right person/entity?
* **Authorization** - What is this person allowed to do?
* **Accounting** - Logging of user activity
### What is a challenge-response scheme and what is it used for.

### What can be used for authentication? What is two or three and multi factor authentication?

### What is CHAP and how does it work?
**Challenge Handshake Authentication Protocol**

Both CHAP and PAP protocols were created to manage remote access
users.

### Radius: how do the two Radius alternatives work? Where is the key stored used during the authentication? Compare here the two alternatives. Pros and cons to use alternative 2?

(CHAP and RADIUS can be used together, then Radius as the database lookup part of CHAP)

### What is Diameter?

### Give some examples of features that make Diameter better than Radius.

### What is EAP and what is its purpose?
(PAP and CHAP) => **EAP**!

* Is a framework to support different authentication methods
* has certain predefined auth methods

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

# TPM

Right now only notes

### **SGX** = Software Guard eXtensions. Intel
Reduced attack surface (App + processor)

**Enclaves** - isolated memory regions of code and data. Also encrypted

*Enclave Page Cache (EPC)* -a part of physical memory (RAM) is reserved for enclaves

If looks at enclave from outside 0xFFFFF.., from inside: data

**Intel TXT** - Intel Trusted eXecution Technology. Intel's implementation of the dynamic RTM model (see further down + slides lect 4)

## Trusted Platform Module
"An international standard for a cryptoprocessor, which is a dedicated microprocessor designed to secure hardware by integrating cryptographic keys into devices."
"providing asymmetric key generation and storage."
TPM is a passive device, only answers to commands from the outside.
"TPM has non-volatile RAM."

**Root of Trust (RoT)** - the start of a trust chain. Aka the part of a system we consider trustworthy.

    RTS (RoT for Storage) 
        A computing engine that protects use and access to data/keys
    RTM (RoT for Measurement) 
        A computing engine capable of making reliable integrity measurements

        CRTM (Core RoT for Measurements)
            Static and dynamic RTM
    RTR (RoT for Reporting) 
        A computing engine capable of reliably reporting information held by the RTS

**TCG** = Trusted Computing Group. "Founded in 1999 by Compaq, HP, IBM, Intel and Microsoft" 
TCG:s take on it is:

    -----------------------------
    |           TPM             |
    |                           |
    |  -------      -------     |
    |  | RTS |      | RTR |     |
    |  -------      -------     |
    -----------------------------

"On a high level TCG wants to foster technology that promotes and defines and promote hardware-based root of trust, an RoT."

**Platform and TPM vendor certificates** - platform: I put the TPM so-and-so on my motherboard with this firmware. Signed ASUS ; TPM vendor: I put this pubKey in this genuine TPM that I made. Signed Infineon

TPM certificate "actually called" the Endorsement credential

**Protected Capabilities** - Protected capabilities is a set of commands that grant the user issuing the command access to protected locations, memory
(storage), registers, etc.

**Attestation** - Attestation is the process of verifying the accuracy of information and the characteristics of the TPM chip current state.

**Integrity (Measurement and Reporting )** - Integrity measurement is the process of obtaining metrics of the platform characteristics and storing the information digest in a protected locations (registers) in the TPM chip. Integrity
reporting is to attest the integrity measurements that are recorded in these locations.

**Opt-in policy of TPM** - The user decides if they want to use the TPM module or not. If they want to use it, they need to **take ownership** of it.

**UEFi** - 

**OEM** - Original Equipment Manufacturer
### Keys
#### Main keys, always remains inside TPM
* **EK** - Endorsement Key. Created at manufacturing time, cannot be changed, used for attestation. Only used for encryption, not signing.
* **AIK** - Attestation Identity Key(s)
* **SRK** = Storage Root Key.
    The root of the key tree structure in a TPM. To get any other key in the tree, one has to go through this parent of parents.
    Used for implementing encrypted storage. Created after running.
    *  TPM_TakeOwnership ( OwnerPassword, ..)

**Migratable vs. non-migratable** keys = indicates whether the private portion of the key can be moved between TPMs.

Key creation

Key migration - between TPMs

File encryption

Authentication

**Attestation** = "Attestation is a mechanism used to obtain a proof that the right software was loaded (by recording its hash in a PCR)."

**PCRs** = Platform Configuration Registers - a register that contains a SHA1 hash and is used to accumulate “measurements”

**Binding** - (may be wrong? prob sealing) binds data to a certain value of the PCR. Then the TPM can only decrypt (unseal) if the PCR value(s) is the same as when encryption happened (seal)

Binding is encrypting data using a the public key of a bind key. If the bind key is non-migratable the encrypted data is binded to the TPM where the secret portion of the bind key resides.

**Key blob** - (EK+SRK)*. Only EK+SRK stored inside TPM, others stored outside using the public key of storage parent key and loaded internally as needed during processing. The encrypted object is called a key blob. When a key € (EK+SRK)\* is generated we get a key blob.

**SHIM** - 

**Hypervisors** - hardware w/ OS on top. Hypervisor is virtual instance of hardware. Aka virtual machine manager. Basically VM? Yeah, probs. Cmp Hyper-V as virtualization in Windows. **(!) Hypervisor = VMM = Virtual Machine Manager**

**Geo-fencing** - prove that computing is performed inside a geographical area. E. g. policy in certain countries w/ medical computations that should be done inside of the country.

**ARM Trustzone** - "poor man's enclave". Uses a REE and a TEE, the TEE is like an enclave but unencrypted. REE & TEE also here (a)ka 'normal world' and 'secure world'. Difference cmp to SGX: only one 'enclave'(-ish).

~~(Sidenote: Ben Smeets favours AMD solution over Intel's SGX)~~

Future for TPMs: Safeguarding keys for application may become obsolete.
Testing that the platform itself functions properly may still live on. That TPM is a separate module may also disappear, instead integrated into CPUs. 

In last project: use idea of trusted computing to shield camera from all kinds of attacks -> apply what we learned in this part of the course.

*Philosophical five minutes w/ Ben*: Security always comes at a price. "Nature wants chaos, to bring order in that chaos cost energy" -> making a device trustworthy costs time and money. "Convince people that achieving trustworthiness in the cloud is feasible -> make money!"

# TPM Quiz prep
## TCG goals and impact:
### What are the functions the TCG RoT should provide?
* verification of data authenticity and integrity;
* provision and protection of secure storage for secret keys; 
* secure reporting of specific machine states; and secure activation.
* Protected capabilities
    * Protected capabilities is a set of commands that grant the user issuing the command access to protected locations, memory (storage), registers, etc.
* Attestation
    * Attestation is the process of verifying the accuracy of information and the characteristics of the TPM chip current state.
* Integrity (Measurement and Reporting)
    - Integrity measurement is the process of obtaining metrics of the platform characteristics and storing the information digest in a protected locations (registers) in the TPM chip. Integrity reporting is to attest the integrity measurements that are recorded in these locations.
* *etc.*
### How is the TPM integrated in a traditional PC/Server system?
As a microchip, attached to the PC's/server's motherboard. Part of the boot mechanism.
### What components in a traditional PC system are at least affected by adding TPM support?
BIOS, CPU, Southbridge(?) = *"The southbridge is one of the two chips in the core logic chipset on a personal computer (PC) motherboard, the other being the northbridge. The southbridge typically implements the slower capabilities of the motherboard in a northbridge/southbridge chipset computer architecture"* - Wikipedia
## TPM Internal
### How many PCR registers does a TPM at least have?
$\geq 16$ 
### How many PCR registers is Intel TXT using in a TPM?
$\geq 24$
### What is the purpose of the OPT-IN function of a TPM?
TCG policy: *The TPM should be shipped in the state the customer requires.* Users are
not forced to use trusted computing, they opt-in if they choose to do so by taking ownership of the device.
### Why do we need a GUI in the Bios when adding TPM support?
Because of the OPT-IN functions. *(Wait, but why?)*
### What is meant by physical presence?
Certain operations on the TPM should only be allowed by an operator that has physical access to the device with the TPM. That is, a remote SW process cannot run such an operation. These operations are said to be allowed under Physical Presence (PP).

Examples of commands that should be implemented to
function only under PP regime
* TakeOwnership
* ForceClear
### Where (in a system) is the physical presence enforced?
(Perhaps the CRTM?) *"Note: at startup the CRTM will check for physical presence of the TPM"*
### What are the monotonic counters in a TPM and explain one use case of them?
TPM has monotonic counters (at least 4). Increment rate: Every 5 secs for at least 7 years (so at least 26 bit counter needed).

Use case: Can be used to implement anti-roll back protection (old SW version in system can be blocked from loading after newSW has been loaded once)
### What is meant by a PCR, what is the size of a PCR, and extending a PCR ?
**Platform Configuration Register**. *"A PCR is a register that contains a SHA1 hash and is used to accumulate “measurements”"*

* Accumulation of new data in the PCR is called extending a PCR
* PCRs can be read from the outside
* Are reset to zero at power up
* Some PCR can be setup to be resettable when in use, be warned!
* At least 16. In Intel TXT use of TPM there are at least 24 PCRs

**Size = ???**
### Why is resetting of PCRs restricted?
Because of possibility of a Reset Attack?
### Why is it not possible to set a PCR to a user provided value?
???
### The TPM exists in different versions. Which ones?
1.2 and 2.0
## TPM in a system
### What is a platform certificate and what is its role?
*"I put the TPM so-and-so on my motherboard with this firmware. Signed ASUS"*
### What is a TPM certificate and what is its role?
*"TPM (vendor) Certificate: I put this pubKey in this genuine TPM that I made. Signed Infineon"*
### What is an endorsement credential?
Aka TPM certificate. 

It is a Digital certificate stating that EK has been properly created and embedded into a TPM. Issued by the entity who generated the EK e.g., the TPM manufacturer. It Includes
* TPM manufacturer name
* TPM model number
* TPM version
* Public EK (Note this maybe privacy sensitive data)
### Who issues a TPM certificate?
The TPM vendor.
### Who issues a Platform certificate?
The OEM (Original Equipment Manufacturer)
### What part of EK is stored in the endorsement credential?
Public EK.

( http://trousers.sourceforge.net/man/tpm_createek.8.html )
### Explain the trust chain, Lect4/slide 42.
[-]
## Roots of trust and their use
### See also http://www.ericsson.com/res/thecompany/docs/publications/ericsson_review/2014/ertrusted-computing.pdf
### What is the CRTM, the SRTM and the DRTM?
*RTM = Root of Trust for Measurement*
* CRTM: Core RTM
    * the a priori trusted code that is refered by the platform credential.
* SRTM: Static RTM
    * In the Static RTM Model, this MUST be the very first piece of code executed on power on or upon reset of the server or complete physical hardware environment.
        * Note: at startup the CRTM will check for physical presence of the TPM 
        * REMEMBER: TPM is not the root-of-trust but trust starts with the CRTM
* DRTM: Dynamic RTM
    * In the Dynamic RTM model the hardware is designed to support that while running a trusted execution thread can be started:
        * Intel call their implementation (Intel) Trusted eXecution Technology
        * AMD: DRTM instruction, SKINIT
### Explain the secure boot use of a RoT Lect1/slide 47 and 48
Measure->Report->Execute
### What is UEFI secure boot?
Lect5, slide 37
### Is the TPM needed in UEFI boot?
*"Observe that actually the TPM is not needed for secure boot if one skips the requirement to support attestation. (one basically has no secrets to protect then)."*
### What is ACM in the context of Intel TXT?
Other HW in the PC/server
* ACM modules (firmware) - Special signed sw modules by HW manufacturer that execute at highest security level and execute in special separate secure memory
    * BIOS ACM: code that measures BIOS +init
    * SINT ACM: code that is part of the DRTM for the secure init/launch
### Intel TXT mitigation of reset attacks.
Lect5, slide 52.
### What is meant by a locality and what are localities used for?
Locality is a concept that allows various trusted processes on the platform to communicate with the TPM such that the TPM is aware of which trusted process is sending commands.

This is implemented using dedicated ranges of LPC bus addresses and thus requires proper support in the chipset HW (e.g. Southbridge).

There are 6 Localities given numbers 0 – 4 and None.

"For TPM, *locality* is defined to be the privilege level of a command." - Platform Embedded Security Technology Revealed: Safeguarding the Future of ...
### Explain how localities and PCRs are linked.
Lect4, slide 19.
## TPM keys and TPM commands
#### Look through TPM main specification for TPM ver 1.2, Part 3, commands.
#### Study the commands: TPM\_TakeOwership, TPM\_Unbind, TPM\_Seal, TPM\_Quote, TPM\_LoadKey2, TPM\_Init. Not needed you understand all the fields but study the pseudo code following in the description of the commands. This code explains the behavior in more detail than the text.
### What is a legacy key?
Legacy: signing or encryption (compatible with TPM v1)
### What is a binding key?
*Lect4:* Binding: decrypt data (usually from remote platforms)

*Lect5:* Binding is encrypting data using a the public key of a bind key. If the
bind key is non-migratable the encrypted data is binded to the TPM
where the secret portion of the bind key resides.

* “Sealing”: binds data to a certain value of the PCR and a key that is not migratable. Then the TPM can only decrypt (unseal) if the PCR value(s) is the same as when encryption happened (seal)

### Who is doing the binding operation, the TPM or some other entity?
*"Binding is done outside the TPM (so there is no TPM_Bind command)"*
### What is (TPM) ownership?
Creating Storage Root Key (SRK)

When taking ownership an owner(ship) secret is set that is needed later for certain TPM commands.

The TakeOwnership results in
* a (re)computation of the SRK private and public key
* The usage secret for SRK is set
* The owner secret is set
* A new tpmProof value is set which is a random value kept secret inside the tpm
* Future reading of pubEK will require knowledge of owner secret
### Which keys do always stay in a TPM (version 1.2)?
* **EK** - Endorsement Key. Created at manufacturing time, cannot be changed, used for attestation. Only used for encryption, not signing.
* **AIK** - Attestation Identity Key(s)
* **SRK** = Storage Root Key.
    The root of the key tree structure in a TPM. To get any other key in the tree, one has to go through this parent of parents.
    Used for implementing encrypted storage. Created after running.
    *  TPM_TakeOwnership ( OwnerPassword, ..)
### Explain the role of EK and SRK?
#### EK
Is a very special key since it stays the same during the TPM lifetime. This gives privacy concern due to linkability to the user when the EK is used. To reduce the risk of EK being used in an improper way even the use of EK is limited Basically it allows only EK for encryption. So signing type of operations are not allowed.

#### SRK
The root of the key structure in a TPM.
### If we have a key hierarchy and then take ownership, can we still use the keys in that hierarchy? Explain!
If we migrate the keys as a/several key blobs, and then immigrate them?
### Why is EK privacy sensitive?
Because it is only generated once and associated with specific TPM (naturally, since it resides in one and never leaves that). See **EK** entry in second question above.
### Why is SRK not (or at least less) privacy sensitive? Think what happens when we takeownership.
At takeownership event, user selects a new password for SRK, and old SRK (and subsequent key tree) is deleted.
### What happened during Takeownership?
See **What is (TPM) ownership?** question above.
### What is the function of the passwords and secrets associated with the keys?
Each key except EK has a usage secret which must be presented when certain operations with the key is to be performed. (one could regard the owner secret as the usage secret of EK). To each secret is connected a password from which it could be derived.
### Where do we store the non-permanent TPM keys?
Outside the TPM, in key blobs.
### What is a migratable key?
Not specified in slides, guess it means a key that you can move/migrate to other TPMs. An example of a non-migratable key should then be SRK. But hey, who knows.
### Which TPM keys we have in a TPM version 1.2? Explain.
Lect4, slide 59.
### Can we have an AIK stored under a migratable storage key?
AIK = Attestation Identity Key(s). sign data from the TPM. A TPM can have many identities!

???

"An Attestation Identity Key (AIK) is an alias for the Endorsement Key (EK). The EK cannot
perform signatures for security reasons and due to privacy concerns." TPM Part 1
### If we have a TPM key blob why then do I have to remember also all keys that were used in the process of creating this key even if these keys are not used for any application?
SRK is inside the TPM, blobs are built from this => the Root of Trust principle (?)
### When loading a key into the TPM why do we have to know the parent secret/password?
Because it will be integrated into key tree / a new key blob with this as a 'new' child will be constructed? And a tree is built from the SRK. *Not really explained in slides.*
### Explain the key hierarchy Lect5: slides 2
[-]
### What is sealing? Can you seal data to a TPM from outside the TPM (using the public portion of the seal key)?
Sealing”: binds data to a certain value of the PCR and a key that is not migratable. Then the TPM can only decrypt (unseal) if the PCR value(s) is the same as when encryption happened (seal)

Second thing not explained in slides
### How many key hierarchies does a TPM v 2.0 have?
Three
### What is the purpose of the primary seeds in a TPM v 2.0?
Three primary seeds
* Platform primary seed: PPS
* Endorsement primary seed: EPS
* Storage primary seed: SPS

**Seeds are used to derive symmetric keys**

## EOQP3
**Zero-knowledge proof** - Prove you know x w/o revealing x

Leakage attacks most common today

"know the environment your software will run on"
    E. g. PIN, false attempt will write to EEPROM and add to a counter counting false attempts, 3 = blocked. To write to this EEPROM, a 'charger' must be supplied with power to be able to write to EEPROM, make a false attempt and notice 'charger' charging => cut power. Make new attempt w/ counter still on 0.

Hopper-Blum authentication, send challenge "a couple of hundred times"

# Trusted Computing -Notes
**PUF** - Physically Unclonable Function


# Quiz prep Trusted Computing
## Trusted Computing:
### What is TEE and REE. Why is a TEE usually smaller than a REE?
Trusted Execution Environment(?)
### Trusted execution in a TEE is obtained by two crucial capabilities/functions?
### What is TCB and what are the two important components of a TCB of a mobile?
Trusted Computing Base. 
### What is the role of the TCB?
"'RoT' of OS"
### To build a secure storage solution one needs at least in a mobile to have what ? (think security here)
### What is a root of trust of integrity? (as compared to RTM, RTS and RTR)
### What is provisioning?
### Understand difference between trusted and trustworthy.
### Understand when a system is trusted and when it is trustworthy. See above. “Trusted” can be just an assumption
### Recall from compute security course Common Criteria and EAL levels.
### Arguments pro’s and con’s using hardware of only software for trusted computing.
### What is trust chain for trusted computing when applied to a server with hardware and services?
### What is RTM, RTS, and RTR?
### Secure boot using RTS and RTM, explain the roles of RTS and RTM
### Which RoTs are in the TPM? Do we need TPM for secure boot?
### What is UEFI boot (ignore use of TPM)?
### Primary objective of OS in trusted platform is to create isolation. Explain role of MMU and why this solution is effective in keeping user applications apart. Understand the importance of privileged (super user) mode and Non-privileged (user) mode.
### Isolation by abstraction: virtualization and (later) containers.
See slide 83 (also article about Docker security! Interesting)
### By able to describe differences between the execution environment alternative on Slide19/Lect5.
### Virtualization: what is type 1 and type 2 virtualization. What is Full/pure and impure/para virtualization?
**Type 1:** Runs on 'bare metal', **Type 2:** Runs on host.

**Pure:** Ensure that sensitive instructions
are not executable within the virtual machine, but instead
invoke the hypervisor: needs hardware support 

**Impure:** remove sensitive instructions from
the virtual machine and replace them with virtualization
code.

Also **para-virtualization**.

## Java
### Java as example of trusted execution environment. Evolution of the sandbox model. Role of signed software.
### Role of components to java security on Slide 30, 40/Lect8.
### What is STIP?

## SELinux
### MAC added to Linux DAC (recall MAC and DAC from your basic computer security course). Understand this via Slide 61/Lect8. Understand what this means for the access control to, for example, a file where we give permissions via the Linux DAC system and also have the MAC policies in place.
**DAC: Discreationary Acces Control**

**MAC: Mandatory Access Control**
### What is the purpose of a SELinux policy?
?

### What are the differences between the three reference policies? Slide 68/lect8
* **Strict**
* **Targeted**
* **MLS**
### What happens when SELinux is operating in permissive or in enforcing mode?
SELinux modes = {Enabled = { Enforcing, Permissive }, Disabled }

**Enforcing:** fully functional

**Permissive:** not blocking anything, but logging
### What is MLS? Example of MLS in basic computer security book.
**MLS:** Multi-Level Security

### Why does SELinux have problems with Text Relocation?
A text relocation is a memory address in the "LOAD
READ-EXECUTE" text segment of a shared library where
text segment means the segment that contains the
program code. Such a non-PIC text segment often
contains large amounts of memory addresses that need
to be "patched" (manipulated, modified, corrected) with
the runtime location of functions and data. This is
performed by the dynamic loader (ld.so in glibc) during
startup of the dynamically linked executable and
invocation of these libraries in the process space.

BUT many existing shared libraries are non-PIC compiled!

So relocating the “TEXT” means changing the executable
code segment so that the absolute addresses (of both
functions and data — variables and constants) are correct
for the base address the segment was loaded at. Doing
this, causes a Copy-on-Write for the executable area.
SELinux will normally (in enforcing mode) not allow this.
But can be allowed by applying special rules on the code
file (often a shared library).
## ARM TrustZone
### ARM Architecture: modes Privileged (super user) and non-Privileged (user).

### Role of NS bit and which parts of the HW carry the NS bit. What is the role of the monitor? A secure mode process can access normal world objects if it has the same or higher privilege. A normal world process can never get access to any object marked as belonging to the secure world.
### What is the benefit from the NX bit?
## HSM
### What is an HSM? See Link to SANS: An Overview of Hardware Security Modules in literature list.
### What is PKCS#11?
### How can people trust a HSM product?

## Smartcard
### How can you interact with the functions in a smartcard: APDUs. Command and response APDUs. When does the card itself send data, which is not as a result of command. The smartcard is essentially a server.
### Existence of the T=0 protocol and T=1 protocol. What is T=1 especially designed for? You do not have to know the details by heart of these protocols. Such will be given if needed.
### What is the role of the NPU unit on a smartcard?
### Slide 50/Lect7: Purpose of the sensor and filters are for defense. Give three types of defensive mechanisms? Why is over and under voltage a condition that should cause the smartcard to shutdown?
### What is the purpose of the personalization stage in a cards lifecycle?
### What is the message passing model in a Java card?
### How can we attack a card? Describe at least two types of attacks.
### What is DPA?
### What caused that DPA succeeded in finding the secret RSA key? How can that be remedied?
### Distinction between RFID and NFC?
### Mifare and Felica: what are these?
### Why is crypto considered to be problematic for contactless cards? Think here about power and allowed
### time to interact with the reading device.
### How does the Hopper-Blum scheme work and why is it secure?
### Why is the blinding vector needed on slide 108/ Lect7
### What is the importance of the presence of noise problem for the Hopper-Blum scheme?
### What is SGX?
### What is an enclave and what protection one has for data and code in an enclave?
### Is SGX a pure SW solution?
### Is SGX also using a TPM?
### Where is the key stored for encrypting the enclave code and data.
### Can the kernel of an OS read data from an enclave?
### How is the enclave created (see the Innovative Instructions and Software Model for Isolated Execution, watch the SGX video on youtube)
### Life-cycle of an enclave. Slides 17,18/Lect6
### EPID identity role in remote attestation
## Identities
### Identity as a link
## Identifiers
### Role of credential.
### What are PUFs and what can they used for?
Physical Unclonable Functions. E. g. ASICs, no two are alike physically, due to random process variations in manufacturing process. Use this in order to identify one. E. g. a challenge-response scheme w/ two paths through the circuit, excite them simultaneously and output a boolean value based on a comparison of the path delays.
### Zero-knowledge proof: what is the basic idea of it and why is it useful in connection with identities.
### EPID, what is it?
### EPID: Roles of issuer, member and verifier, who gets what (think keys, revocation lists)
### EPID: Unlikability of private keys.
### EPID: Join operation
### EPID: Revocation lists
## Android and iOS
### Explain difference in the use of signatures on applications.

### Explain DM-verity.

### How is the root hash value protected in DM-verity?

### How are apps isolated in Android? Slide 101-107/Lect8

### How are apps isolated in iOS? Slide 129/Lect8

### What is BYOD?
Bring Your Own Device

KNOX concept?
### Why is isolation important in BYOD?


"In Android, signatures have nothing to do w/ trustworthiness" "Only thing it says is that it has been signed by somebody else, separation of applications(?), nothing more" "Virus checkers are useless here, they cannot access other aplications' code, only if OS allows them. They can ask for the name of another app, nothing more."

**$Z_N$** 

* the set of elements in $Z$ That are relatively prime to $N$.
* E. g. $Z_4 = {1,3}$
* $a^2mod N$, squares
* $(a/N)=(p/N)(q / N)$

# SW security
**static/dynamic analysis**
* låt kvalificerade personer använda dessa (ex om errors från en sådan checker som inte eg är fel, men okvalificerad/klantig person gick in och ändrade koden för att 'programmet skulle bli nöjt' och introducerade då fel i huvudprogrammet)
* Fr o m (Lect10, slide 59) 

**Taint analysis** - som magoperation med kontrastvätska
