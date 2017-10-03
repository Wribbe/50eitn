# TPM, Project 3 EITN50
## 3.1
### **Grading criterion**: Report describes the necessary steps to repeat the group's experimental setup, award 5 points.
Copied VMs from network drive S: to local hard drive on lab room computer.
Extracted them with 7-Zip. Added them to VirtualBox through Machine > Add...
and selecting respective extracted .vbox file (TPM1, TPM2, TSS).
In TPM1 VM: Checked IP address with ``ifconfig eth0``, was 10.0.2.14.
In TSS VM: Started FileZilla and connected to TPM1 VM by Quickconnect
functionality with values = { Host: 10.0.2.14, Username: pi, Password: tpm,
Port: 22}.
In TPM1 VM: No file in /home/pi/tpm/tpm4720/tpmstate on startup. Checked which
environment variables were already set with bash command ``set | sed -n
1,91p``. Found that env variables

    TPM_PATH=/home/pi/tpm/tpm4720/tpmstate
    TPM_PORT=6545
    TPM_SERVER_NAME=localhost
    TPM_SERVER_PORT=6545

were already set, meaning there was no need to ``export`` to those env var:s.

In TSS VM: Env variables

    TCSD_TCP_DEVICE_HOSTNAME=10.0.2.15
    TCSD_TCP_DEVICE_PORT=6545
    TCSD_USE_TCP_DEVICE=true

were set. Thus only needed to change ``TCSD_TCP_DEVICE_HOSTNAME``, did this
with ``export TCSD_TCP_DEVICE_HOSTNAME=10.0.2.14``.
Check if changed:

    tss@TSS ~ $ env | sort | grep HOSTNAME
    TCSD_TCP_DEVICE_HOSTNAME=10.0.2.14

Also had to change TPM hostname:

    tss@TSS ~ $ set | grep TPM
    TPM_SERVER_HOSTNAME=10.0.2.15
    ...
    export TPM_SERVER_NAME=10.0.2.14
    tss@TSS ~ $ set | grep TPM
    TPM_SERVER_HOSTNAME=10.0.2.14
    ...


## 3.2.2
### **Grading criterion**: report should contain a dump EK and description how
### it was obtained, 2 points.
TPM1:

    tpm_server

TSS:

    tpmbios
    sudo -E /usr/local/sbin/tcsd -e -f
		TCSD TDDL ioctl: (25) Inappropriate ioctl for device
		TCSD TDDL Falling back to Read/Write device support.
		TCSD trousers 0.3.13: TCSD up and running.
Opened new terminal window on TSS:

    createek

Here terminal window on TPM1 running ``tpm_server`` was searched by scrolling for keys, and the keys were copied and pasted here:

	...
    TPM_RSAGenerateKeyPair: length of n,p,q,d = 256 / 128 / 128 / 256
    TPM_Key_GenerateRSA: Public key n 9d c7 a2 12
    TPM_Key_GenerateRSA: Exponent length 3
    01 00 01 
    TPM_Key_GenerateRSA: Private prime p cc f1 86 7b
    TPM_Key_GenerateRSA: Private prime q c5 16 32 ff
    TPM_Key_GenerateRSA: Private key d 8d 80 b5 01
	...
    TPM_SymmetricKeyData_SetKeys:
    TPM_SymmetricKeyData_SetKeys: userKey 48 67 2f 01
	...
Thus,
* Public key = **9d c7 a2 12**
* Private key = **8d 80 b5 01**

### Memorize 'take ownership' passwords:
TSS:

	takeown -pwdo superhemligt_o -pwds superhemligt_s

### **Grading criterion**: report should contain a dump SRK pubkey and description how it was obtained, 2 points.

TSS (atm):

<!--
Running the above command on a terminal that is opened on the Desktop folder
generates a ``srk.pem`` file with the following content:

    tss@TSS ~/Desktop $ cat srk.pem
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1pz0SF4rCVdTbw4ySPxW
    F2ZfAlw3LuTwE+F11eXGrZ/+ib7CRX7I+OT4/5LXnGvrH6PR5R1ajMUeE3Om1VZu
    tLxZ1Tikrizk8CECh0u1qb5LsNKoBBhW6COa6ge5gR8UqaXYhylP6NkBz9hBiLT3
    IHhgvvcecdlfpWR+/tsK1RYKjUfnWj5v5sZkEQ4y71PNBr+ZD+iw9XhzU0PqpuXC
    8y3zD4aoA/CVREzVe5GzKqd4ZzGoYfUhdbqYb9hHeRXYCKBpSc8kwjF4Qa1z/Fc2
    nfCyPOeb1asV9GbZL81W4VR+WJwK75cKGxuKbo+PUGOzekG1euIxtMUe83eJmRRB
    +wIDAQAB
    -----END PUBLIC KEY-----
-->

From the source of tmp_constants.h (the emulator definitions):

    /* 4.4.1 Reserved Key Handles rev 87

       The reserved key handles. These values specify specific keys or specific actions for the TPM.

       TPM_KH_TRANSPORT indicates to TPM_EstablishTransport that there is no encryption key, and that
       the "secret" wrapped parameters are actually passed unencrypted.
    */

    #define TPM_KH_SRK              0x40000000 /* The handle points to the SRK */
    #define TPM_KH_OWNER            0x40000001 /* The handle points to the TPM Owner */
    #define TPM_KH_REVOKE           0x40000002 /* The handle points to the RevokeTrust value */
    #define TPM_KH_TRANSPORT        0x40000003 /* The handle points to the TPM_EstablishTransport static
                                                  authorization */
    #define TPM_KH_OPERATOR         0x40000004 /* The handle points to the Operator auth */
    #define TPM_KH_ADMIN            0x40000005 /* The handle points to the delegation administration
                                                  auth */
    #define TPM_KH_EK               0x40000006 /* The handle points to the PUBEK, only usable with
                                                  TPM_OwnerReadInternalPub */

TSS

    ownerreadinternalpub -hk 40000000 -of srk.pub -pwdo superhemligt_o
TPM1

<!--    TPM_IO_Write: length 335
     00 C5 00 00 01 4F 00 00 00 00 00 00 00 01 00 03 
     00 01 00 00 00 0C 00 00 08 00 00 00 00 02 00 00 
     00 00 00 00 01 00 DA C2 29 DA 76 18 F0 F7 15 30 
     1F 3D 66 E6 EC C5 01 71 80 95 95 AA 0E 31 5B 4D 
     13 9F 71 C9 88 6E 27 84 1C 0F 1C AD 56 B8 96 DF 
     F2 D0 BE 18 7B BD 9D EA 2E 5E 28 E5 48 BE 9A A8 
     8A 80 EB 5C 39 91 7C BC F2 CC DF 12 1D A1 40 B3 
     78 C2 98 16 9A AD 71 83 C5 1D 20 22 0C BA 1F 28 
     E1 67 80 7B 0E 13 6A 26 95 F5 E7 41 E2 8F 95 27 
     7D DF 63 EF 77 F3 EE 2F 1F E4 14 18 7C 3F 0F E6 
     21 D0 A5 99 98 22 0E C8 EE D5 BC A4 D7 17 2C 6F 
     56 B8 C8 F3 DF 77 71 B7 13 12 CB 91 C2 5B B3 05 
     7C 4B B4 85 9E 30 95 99 6A 2A 99 9B 69 2A 47 40 
     00 12 E3 FC 8B DA C9 1C 36 27 DC 5C AF 38 D1 03 
     3C FA 11 BA A9 68 7F 45 4F DA 1A D8 27 38 02 F6 
     FE 03 D9 46 9D CD FA 81 BD D9 23 F2 6A AB 87 9F 
     4D B0 2C BC 8F 49 F0 5A FE 6B 86 09 1F 7D 1D 57 
     94 5D 95 CE CB 96 39 06 9A 89 C6 85 7D 3F D6 A9 
     0D 68 69 80 96 B5 21 AC E8 38 39 EF EA 48 5D 20 
     DE 0C 05 72 AA 0B 07 44 2E BA 00 DF BC 34 71 6B 
     F5 8E DE 7F C0 15 82 05 AA 6B D8 61 AB AC 40 
    output from 1st iteration, see now on 2nd it that first 2 ½ lines are the same, prob means that that is some kind of preamble/overhead. Thus, part that changes between iterations but stay the same between cmd runs in same iterations should probs be the key part. -->

    TPM_IO_Write: length 335
     00 C5 00 00 01 4F 00 00 00 00 00 00 00 01 00 03 
     00 01 00 00 00 0C 00 00 08 00 00 00 00 02 00 00 
     00 00 00 00 01 00 BF E7 8E C3 A4 2E 0D D4 00 DE 
     C7 0F 97 EC D8 C2 55 92 E0 8A 59 1B 92 F8 27 60 
     69 58 6A 2A 69 08 67 6A 9D 05 CF 92 70 B7 FF B1 
     95 47 26 BC 1E D6 86 4F 5A 24 72 CA CE AE 6A 32 
     F7 11 53 88 25 42 45 CC D0 41 B5 98 B4 F3 67 D4 
     01 1B CE B1 3D B6 85 E8 1C 52 E9 71 2A 34 9E 09 
     ED D9 75 32 34 E2 00 E6 68 3D 61 7F C8 CA E9 27 
     0B 56 04 3B 5A 06 F0 CC 5D EA 07 BC 00 19 D7 A3 
     00 D8 DF 7F BC D7 59 E1 11 2F C8 53 C2 FD DA 8C 
     66 38 38 11 D4 8E 84 9E 02 65 C0 EA FB EB 39 08 
     AC 56 74 FF 3C 16 51 45 C1 49 34 64 6B F8 E1 63 
     D0 C0 0D 18 7E 64 E2 E5 18 8D AC 3E 02 89 10 33 
     A6 6A 20 9B D6 CB 87 D5 39 DB 53 4C BC F4 B6 C6 
     8D 6F 57 37 AD E6 B9 4E 40 4A 78 7B C5 7F BE CC 
     BD 30 2E 0E 4E 4F 74 50 34 B9 9F B1 CF 8D B8 E5 
     5A E6 4C 47 AB 3C 16 0B AB 55 9B C8 BB 23 1C 5E 
     3E 2C 27 DB 12 B7 C2 1E E5 FE 9A 06 E5 8D 75 89 
     51 5C CD 95 98 AE 86 9A BF E3 00 8E 52 1A A0 2B 
     2D F8 DA CC A2 E2 A9 77 CE A5 D6 F4 30 94 C3    

If adding flag -v on TSS:

    tss@TSS ~ $ ownerreadinternalpub -hk 40000000 -of srk.pub -pwdo superhemligt_o -v

<!-- TPM_Send: OIAP
    TPM_TransmitSocket: To TPM [OIAP] length=10
    00 C1 00 00 00 0A 00 00 00 0A
    TPM_ReceiveSocket: From TPM length=34
    00 C4 00 00 00 22 00 00 00 00 F3 9D CD CC 15 91
    19 BE 65 29 2A 79 57 D6 4E CB 40 18 95 FA 2C EF
    18 D1

    TPM_Send: OwnerReadInternalPub
    TPM_TransmitSocket: To TPM [OwnerReadInternalPub] length=59
    00 C2 00 00 00 3B 00 00 00 81 40 00 00 00 F3 9D
    CD CC BE 7D AB 5D 9C 1C 6F C7 19 DE F9 B4 0A 2F
    2E 78 71 C4 D0 1C 00 D5 E8 4E C9 A4 11 A8 6A 69
    DC B7 25 16 0D 8A 53 91 D2 FE 31
    TPM_ReceiveSocket: From TPM length=335
    00 C5 00 00 01 4F 00 00 00 00 00 00 00 01 00 03 
    00 01 00 00 00 0C 00 00 08 00 00 00 00 02 00 00 
    00 00 00 00 01 00 DA C2 29 DA 76 18 F0 F7 15 30 
    1F 3D 66 E6 EC C5 01 71 80 95 95 AA 0E 31 5B 4D 
    13 9F 71 C9 88 6E 27 84 1C 0F 1C AD 56 B8 96 DF 
    F2 D0 BE 18 7B BD 9D EA 2E 5E 28 E5 48 BE 9A A8 
    8A 80 EB 5C 39 91 7C BC F2 CC DF 12 1D A1 40 B3 
    78 C2 98 16 9A AD 71 83 C5 1D 20 22 0C BA 1F 28 
    E1 67 80 7B 0E 13 6A 26 95 F5 E7 41 E2 8F 95 27 
    7D DF 63 EF 77 F3 EE 2F 1F E4 14 18 7C 3F 0F E6 
    21 D0 A5 99 98 22 0E C8 EE D5 BC A4 D7 17 2C 6F 
    56 B8 C8 F3 DF 77 71 B7 13 12 CB 91 C2 5B B3 05 
    7C 4B B4 85 9E 30 95 99 6A 2A 99 9B 69 2A 47 40 
    00 12 E3 FC 8B DA C9 1C 36 27 DC 5C AF 38 D1 03 
    3C FA 11 BA A9 68 7F 45 4F DA 1A D8 27 38 02 F6 
    FE 03 D9 46 9D CD FA 81 BD D9 23 F2 6A AB 87 9F 
    4D B0 2C BC 8F 49 F0 5A FE 6B 86 09 1F 7D 1D 57 
    94 5D 95 CE CB 96 39 06 9A 89 C6 85 7D 3F D6 A9 
    0D 68 69 80 96 B5 16 74 05 0E A8 6F 14 9F C0 1C 
    EE 60 E9 C4 BA 4C CB 72 CF 4E 00 F7 5F 0F 3C 49 
    E6 71 9A AF 4B 65 30 3A A3 15 61 E9 8F DD B8 -->

    TPM_IO_Write: length 335
     00 C5 00 00 01 4F 00 00 00 00 00 00 00 01 00 03 
     00 01 00 00 00 0C 00 00 08 00 00 00 00 02 00 00 
     00 00 00 00 01 00 BF E7 8E C3 A4 2E 0D D4 00 DE 
     C7 0F 97 EC D8 C2 55 92 E0 8A 59 1B 92 F8 27 60 
     69 58 6A 2A 69 08 67 6A 9D 05 CF 92 70 B7 FF B1 
     95 47 26 BC 1E D6 86 4F 5A 24 72 CA CE AE 6A 32 
     F7 11 53 88 25 42 45 CC D0 41 B5 98 B4 F3 67 D4 
     01 1B CE B1 3D B6 85 E8 1C 52 E9 71 2A 34 9E 09 
     ED D9 75 32 34 E2 00 E6 68 3D 61 7F C8 CA E9 27 
     0B 56 04 3B 5A 06 F0 CC 5D EA 07 BC 00 19 D7 A3 
     00 D8 DF 7F BC D7 59 E1 11 2F C8 53 C2 FD DA 8C 
     66 38 38 11 D4 8E 84 9E 02 65 C0 EA FB EB 39 08 
     AC 56 74 FF 3C 16 51 45 C1 49 34 64 6B F8 E1 63 
     D0 C0 0D 18 7E 64 E2 E5 18 8D AC 3E 02 89 10 33 
     A6 6A 20 9B D6 CB 87 D5 39 DB 53 4C BC F4 B6 C6 
     8D 6F 57 37 AD E6 B9 4E 40 4A 78 7B C5 7F BE CC 
     BD 30 2E 0E 4E 4F 74 50 34 B9 9F B1 CF 8D B8 E5 
     5A E6 4C 47 AB 3C 16 0B AB 55 9B C8 BB 23 1C 5E 
     3E 2C 27 DB 12 B7 F7 FB ED 39 C8 E0 AC D2 8A 72 
     A3 6D 34 E6 11 6F 47 1C 2F 12 00 CD C2 7C E1 FA 
     E0 A6 C1 80 80 50 82 C4 C2 1B BC 5A 98 15 56

Last two lines differ between output on TSS and TPM1. Ubiqutious in different instances of command execution (and between iterations of TPM taking ownership iterations) is the string

<!--    00 C5 00 00 01 4F 00 00 00 00 00 00 00 01 00 03 
    00 01 00 00 00 0C 00 00 08 00 00 00 00 02 00 00 
    00 00 00 00 01 00 DA C2 29 DA 76 18 F0 F7 15 30 
    1F 3D 66 E6 EC C5 01 71 80 95 95 AA 0E 31 5B 4D 
    13 9F 71 C9 88 6E 27 84 1C 0F 1C AD 56 B8 96 DF 
    F2 D0 BE 18 7B BD 9D EA 2E 5E 28 E5 48 BE 9A A8 
    8A 80 EB 5C 39 91 7C BC F2 CC DF 12 1D A1 40 B3 
    78 C2 98 16 9A AD 71 83 C5 1D 20 22 0C BA 1F 28 
    E1 67 80 7B 0E 13 6A 26 95 F5 E7 41 E2 8F 95 27 
    7D DF 63 EF 77 F3 EE 2F 1F E4 14 18 7C 3F 0F E6 
    21 D0 A5 99 98 22 0E C8 EE D5 BC A4 D7 17 2C 6F 
    56 B8 C8 F3 DF 77 71 B7 13 12 CB 91 C2 5B B3 05 
    7C 4B B4 85 9E 30 95 99 6A 2A 99 9B 69 2A 47 40 
    00 12 E3 FC 8B DA C9 1C 36 27 DC 5C AF 38 D1 03 
    3C FA 11 BA A9 68 7F 45 4F DA 1A D8 27 38 02 F6 
    FE 03 D9 46 9D CD FA 81 BD D9 23 F2 6A AB 87 9F 
    4D B0 2C BC 8F 49 F0 5A FE 6B 86 09 1F 7D 1D 57 
    94 5D 95 CE CB 96 39 06 9A 89 C6 85 7D 3F D6 A9 
    0D 68 69 80 96 B5 -->

                       BF E7 8E C3 A4 2E 0D D4 00 DE 
     C7 0F 97 EC D8 C2 55 92 E0 8A 59 1B 92 F8 27 60 
     69 58 6A 2A 69 08 67 6A 9D 05 CF 92 70 B7 FF B1 
     95 47 26 BC 1E D6 86 4F 5A 24 72 CA CE AE 6A 32 
     F7 11 53 88 25 42 45 CC D0 41 B5 98 B4 F3 67 D4 
     01 1B CE B1 3D B6 85 E8 1C 52 E9 71 2A 34 9E 09 
     ED D9 75 32 34 E2 00 E6 68 3D 61 7F C8 CA E9 27 
     0B 56 04 3B 5A 06 F0 CC 5D EA 07 BC 00 19 D7 A3 
     00 D8 DF 7F BC D7 59 E1 11 2F C8 53 C2 FD DA 8C 
     66 38 38 11 D4 8E 84 9E 02 65 C0 EA FB EB 39 08 
     AC 56 74 FF 3C 16 51 45 C1 49 34 64 6B F8 E1 63 
     D0 C0 0D 18 7E 64 E2 E5 18 8D AC 3E 02 89 10 33 
     A6 6A 20 9B D6 CB 87 D5 39 DB 53 4C BC F4 B6 C6 
     8D 6F 57 37 AD E6 B9 4E 40 4A 78 7B C5 7F BE CC 
     BD 30 2E 0E 4E 4F 74 50 34 B9 9F B1 CF 8D B8 E5 
     5A E6 4C 47 AB 3C 16 0B AB 55 9B C8 BB 23 1C 5E 
     3E 2C 27 DB 12 B7

Guess that means this is SRK.pub part..? Moving on.

## 3.3 Assignment 3: Key hierarchy

### 3.3.2 Questions
1. The identity key is one type of signature key. Describe some differences between an identity and a signature key.
    * An identity key is an alias for the Endorsement Key, used instead of the EK in order to mitigate privacy issues (Single EK can easily be linked to a single user) and security issues (each use of a key 'waters down' its security, i. e. the entropy is theoretically lowered each time it is used). An AIK can also only be used for two operations: ``TPM_Quote`` and ``TPM_CertifyKey``, and not in e. g. ``TPM_Sign``. ``TPM_Quote``, however, can not be performed by/with a signing key. Signing keys to sign arbitrary data, identity keys for remote attestation.
<!-- https://security.stackexchange.com/questions/83269/tpm-signing-key-or-attestation-identity-key -->
2. Which keys can be used for file encryption?
   * Storage keys.
3. There is one type of key that exists, but its use is not recommended. Which key is that, and why does it exist?
    * EK? If so, see reasoning in answer to question 1 above here.

**Grading criterion: each correct answer to the above 3 questions is 2 points.**

<!--
"This features generates a sub-SRK (called a Migratable Root Key or MRK) that
all applications that wish to preserve the ability to migrate keys can use as
the parent key. This new Migratable Root Key can then be migrated if necessary and
automatically enables all of the descendent keys to be migrated" - https://blogs.oracle.com/danx/tpm-key-migration-in-solaris
-->

<!-- Do they just mean that one must create key tree structure top-down? If so: -->
The tree key structure must be created top-down, i. e. a key must always have a parent key/treenode, thus one cannot create e. g. E before its parent B. Also, if a parent key is migratable its children will automatically need to be migratable as well, even if they are specified as non-migratable, e. g. non-migratable C as child to migratable B will be migratable C.

**Are all combinations possible? If not, why? Grading criterion: correct answer 2 points.**



            SRK
            /  \
           H    A
               / | \
              B  F  G
            / | \
           C  D  E

**Grading criterion: drawing of correct hierarchy 2 points.**

**on TSS**

Created a directory for TPM1, named ``TPM1``

H: SRK, an identity key. 

    identity -la H -pwdk superhemligt_H -pwds superhemligt_s -v12 -ok H -pwdo superhemligt_o -v

A: SRK, non migratable storage key. 

    createkey -kt e -pwdk superhemligt_A -pwdp superhemligt_s -ok A -hp 40000000 
    loadkey -hp 40000000 -ik A.key -pwdp superhemligt_s
    New Key Handle = 9B84E1AD

B: A, migratable storage key. 
    
    createkey -kt e/m -pwdk superhemligt_B -pwdp superhemligt_A -pwdm superhemligt_m -ok B -hp 9B84E1AD
    loadkey -hp 9B84E1AD -ik B.key -pwdp superhemligt_A
    New Key Handle = C410EC05

C: B, a non migratable sign key. Must, however, be a migratable key since parent key B is migratable.

    createkey -v -kt s/m -pwdk superhemligt_C -pwdp superhemligt_B -pwdm superhemligt_m -ok C -hp C410EC05

D: B, a migratable sign key. 

    createkey -v -kt s/m -pwdk superhemligt_D -pwdp superhemligt_B -pwdm superhemligt_m -ok D -hp C410EC05

E: B, a migratable bind key. 

    createkey -v -kt b/m -pwdk superhemligt_E -pwdp superhemligt_B -pwdm superhemligt_m -ok E -hp C410EC05

F: A, a non migratable sign key. 

    createkey -v -kt s -pwdk superhemligt_F -pwdp superhemligt_A -ok F -hp 9B84E1AD

G: A, a migratable sign key. 

    createkey -v -kt s/m -pwdk superhemligt_G -pwdp superhemligt_A -pwdm superhemligt_m -ok G -hp 9B84E1AD

<!-- *Interesting. Running* ``listkeys`` *returns handles for only H and B,* ``Key handle 00 84f9ec60 \n Key handle 01 3092f35a`` *Can still read public part of keys w/* ``getpubkey``*, though* -->

## 3.4 Assignment 4: Key Migration
### 3.4.2 Questions
1. Is it possible for a migratable key to be the parent of a non-migratable key?
    * Yes, but then the non-migratable key becomes a migratable key.
    <!-- Okay, this explains why I couldn't create C before (from TPM commands pdf)
    " If parentHandle -> keyFlags -> migratable is TRUE and keyInfo -> keyFlags -> migratable is FALSE then return TPM_INVALID_KEYUSAGE"
    -->
2. Which command is the first to be executed when performing a key migration?
    * ``TPM_AuthorizeMigrationKey`` -> ``TPM_CreateMigrationBlob`` (i. e., authorize migation key cmd)
3. Give a short description of the command TPM_ConvertMigrationBlob.
    * This command enables a migration-blob to be loaded into a TPM as a 'normal', wrapped blob. 
    * From TPM part 3 pdf: "Loading one of these wrapped blobs does not require authorization, since correct blobs were created by the TPM under Owner authorization, and unwrapped blobs cannot be used without Owner authorisation."
    * So: unwrapped blobs cannot be used w/o owner auth, wrapped w/o, guess this command makes a blob usable for the "new" TPM, so that it can use the keys in the blob w/o prompting user.
4. Which TPM command loads the migrated keys into the TPM?
    * TPM_LoadKey
5. Is it the TPM or the TSS that handles the transfer of the migration blob?
    * The TPM, if judged from the commands in the appendix. 

**Grading criterion: correct answers to be above 5 questions is 2 points each.**

### 3.4.3 Instructions: Key migration in the TPM emulator
**First create a migration key blob on TPM1 for B that can be saved and then reloaded on TPM2.**

TPM2: moved existing TPM state (00.permall) to other directory. checked IP address w/ ``ifconfig``, was 10.0.2.15. Ran ``tpm_server``

TSS: Made a new directory for TPM2, ``TPM2``

    (in dir TPM1:) cd ../TPM2
    export TPM_SERVER_NAME=10.0.2.15
    export TCSD_TCP_DEVICE_HOSTNAME=10.0.2.15
    tpmbios
    (in other terminal window, TSS#2)sudo -E /usr/local/sbin/tcsd -e -f

    createek
    takeown -pwdo tpm2_o -pwds tpm2_s

tpm2_sk: SRK, migratable storage key

    createkey \
        -kt e \
        -pwdp tpm2_s \
        -pwdk tpm2_sk \
        -pwdm tpm_m \
        -ok tpm2_sk \
        -hp 40000000
    
    loadkey \
        -hp 40000000 \
        -ik tpm2_sk.key \
        -pwdp tpm2_s
    New Key Handle = 12AACB57

    cp tpm2_sk.key ../TPM1/tpm2_sk.key
    cd ../TPM1

Shut down daemon in TSS#2.
    
TPM1: ``tpm_server``

TSS

    export TPM_SERVER_NAME=10.0.2.14
    export TCSD_TCP_DEVICE_HOSTNAME=10.0.2.14
    tpmbios
    (TSS#2) sudo -E /usr/local/sbin/tcsd -e -f
    
    (TSS#1) export TPM_SERVER_NAME=10.0.2.14
    export TCSD_TCP_DEVICE_HOSTNAME=10.0.2.14

    migrate -hp <parent handle in hex> -pwdp <parent password>
        -pwdo <TPM owner password>
        -hm <handle of migration key> or -im TPM2_STORAGEKEY_FILENAME.key
        -pwdk <TPM2_STORAGEKEY_PASSWORD>
        -pwdm <MIGRATION_PASSWORD of STORAGEKEY>
        -ik STORAGEKEY_FILENAME.key
        -ok migrationblob.bin
        
    migrate -hp 9B84E1AD -pwdp superhemligt_A -pwdo superhemligt_o -im tpm2_sk.key -pwdk tpm2_sk -pwdm superhemligt_m -ik B.key -ok migrationblob.bin 
    migrate -hp 9B84E1AD -pwdp superhemligt_A -pwdo superhemligt_o -hm 12AACB57 -pwdk tpm2_sk -pwdm superhemligt_m -ik B.key -ok migrationblob.bin 


    createkey \
        -kt m \
        -pwdp superhemligt_s \
        -pwdk superhemligt_m \
        -pwdm superhemligt_m \
        -ok migrateKey \
        -hp 40000000
    loadkey \
        -hp 40000000 \
        -ik migrateKey.key \
        -pwdp superhemligt_s
    New Key Handle = 12C71D9F

**Migrate the keys using the utility migrate.**

    migrate \
        -hp 40000000 \
        -pwdp superhemligt_s \
        -pwdo superhemligt_o \
        -hm 12C71D9F \
        -pwdk superhemligt_m \
        -pwdm superhemligt_m \
        -ik migrateKey.key  \
        -ok migrationblob.bin
    Wrote migration blob and associated data to file.
    ls | grep blob
    migrationblob.bin

    migrate \
        -hp 9B84E1AD \
        -pwdp superhemligt_A \
        -pwdo superhemligt_o \
        -hm 12C71D9F \
        -pwdk superhemligt_m \
        -pwdm superhemligt_m \
        -ik B.key  \
        -ok migrationblob.bin
    CreateMigrationBlob returned 'File error' (-2147479545). 
<!-- grr -->
    migrate \
        -hp 9B84E1AD \
        -pwdp superhemligt_A \
        -pwdo superhemligt_o \
        -im migrateKey.key \
        -pwdk superhemligt_m \
        -pwdm superhemligt_m \
        -ik B.key  \
        -ok migrationblob.bin
    CreateMigrationBlob returned 'File error' (-2147479545). 
<!-- :'( -->

    migrate \
        -hp 12C71D9F \
        -pwdp superhemligt_m \
        -pwdo superhemligt_o \
        -hm 12C71D9F \
        -pwdk superhemligt_m \
        -pwdm superhemligt_m \
        -ik B.key  \
        -ok migrationblob.bin
    CreateMigrationBlob returned 'Invalid key usage' (36).

-kt e
A-F
migkey tpm2
-> tpm1
mig m tpm2key

**Change both environment variables to the TPM2 machine and reload the key on TPM2 using the utility loadmigrationblob.**

loadmigrationblob -hp TPM2_STORAGEKEY_HANDLE -pwdp TPM2_STORAGEKEY_PASSWORD -if migrationblob.bin

**After we migrated key B to TPM2 try to load key C, D, and E into TPM2. Explain what happens (why does it work or not work?).**

### 3.4.4 Questions
1. Do the above migration and document in your report.
2. There are other ways to migrate keys. When do you use a key of type TPM_KEY_USAGE =
TPM_Migrate (Hint: look in [8])
3. What is the rewrap option of the migrate command used for?
    * To directly transfer a key to another TPM.

### 3.6.1 Questions
1. Why is TSS_Bind a TSS command, and not a TPM command?
    * Because binding is done outside of a TPM.
2. Give some differences between Data binding and Data sealing.
3. Can a key used for data sealing be migrated to another TPM?

**Grading criterion: correct answers to the above three questions is 2 points each.**

<!--
https://blogs.oracle.com/danx/tpm-key-migration-in-solaris
http://courses.cs.vt.edu/cs5204/fall10-kafura-BB/Papers/TPM/Intro-TPM.pdf
https://trustedcomputinggroup.org/wp-content/uploads/Kazmierczak20Greg20-20TPM_Key_Management_KMS2008_v003.pdf
-->

### Running the TPM program:

With emulator running on other instance, print following in two separate
terminals:

First terminal (Tss#1):

    sudo -E /usr/local/sbin/tcsd -e -f

Second terminal (Tss#2):
(If the first command does not work, try the additional commands below.)

    tpm_takeownership -z -y

Additional commands if taking ownership does not work.

    forceclear
    tmp_setenable -e -f
    tpm_takeownership -z -y

Compile and run program (Tss#2):

    gcc -o tmpcode tmpcode.c -ltspi -std=c99 -Wall
    ./tmpcode

Which will generate and print 32 random bytes and print contents of first 3
PCR-registers.
