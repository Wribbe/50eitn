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
	TPM_Key_GenerateRSA: Public key n cf c5 c3 b9
	TPM_Key_GenerateRSA: Exponent length 3
	01 00 01
	TPM_Key_GenerateRSA: Private prime p fb 20 5d 01
	TPM_Key_GenerateRSA: Private prime q d3 ce 03 15
	TPM_Key_GenerateRSA: Private key d c5 e9 b1 0d
	...
	TPM_SymmetricKeyData_SetKeys:
	TPM_SymmetricKeyData_SetKeys: userKey af 41 64 4c
	...
Thus,
* Public key = **cf c5 c3 b**
* Private key = **c5 e9 b1 0d**

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

<!-- 
    tss@TSS ~ $ getpubkey
	Missing key handle.

	getpubkey -ha <key handle> -pwdk keypassword


	tss@TSS ~ $ getpubkey -ha 40000000 -pwdk superhemligt_s
	Error Invalid key handle from TPM_GetPubKey

Will have to try smth else, gotta leave now 
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

    TPM_IO_Write: length 335
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
<!-- I guess the above is the SRK.pub file output. -->

If adding flag -v on TSS:

    tss@TSS ~ $ ownerreadinternalpub -hk 40000000 -of srk.pub -pwdo superhemligt_o -v

    TPM_Send: OIAP
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
    E6 71 9A AF 4B 65 30 3A A3 15 61 E9 8F DD B8 

Last two lines differ between output on TSS and TPM1. Ubiqutious in different instances of command execution is the string

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
    0D 68 69 80 96 B5

Guess that means this is SRK.pub part..? Moving on.