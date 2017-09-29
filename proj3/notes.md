# TPM, Project 3 EITN50
## 3.1
### **Grading criterion**: Report describes the necessary steps to repeat the group's experimental setup, award 5 points.
Copied VMs from network drive S: to local hard drive on lab room computer. Extracted them with 7-Zip. Added them to VirtualBox through Machine > Add...  and selecting respective extracted .vbox file (TPM1, TPM2, TSS).
In TPM1 VM: Checked IP address with ``ifconfig eth0``, was 10.0.2.14.
In TSS VM: Started FileZilla and connected to TPM1 VM by Quickconnect functionality with values = { Host: 10.0.2.14, Username: pi, Password: tpm, Port: 22}.
In TPM1 VM: No file in /home/pi/tpm/tpm4720/tpmstate on startup. Checked which environment variables were already set with bash command ``set | sed -n 1,91p``. Found that env variables

    TPM_PATH=/home/pi/tpm/tpm4720/tpmstate
    TPM_PORT=6545
    TPM_SERVER_NAME=localhost
    TPM_SERVER_PORT=6545 

were already set, meaning there was no need to ``export`` to those env var:s.

In TSS VM: Env variables

    TCSD_TCP_DEVICE_HOSTNAME=10.0.2.15
    TCSD_TCP_DEVICE_PORT=6545 
    TCSD_USE_TCP_DEVICE=true

were set. Thus only needed to change ``TCSD_TCP_DEVICE_HOSTNAME``, did this with ``export TCSD_TCP_DEVICE_HOSTNAME=10.0.2.14``. 
Check if changed:
    
    ``tss@TSS ~ $ env | sort | grep HOSTNAME
    TCSD_TCP_DEVICE_HOSTNAME=10.0.2.14``

Also had to change TPM hostname:
    
    tss@TSS ~ $ set | grep TPM
    TPM_SERVER_HOSTNAME=10.0.2.15
    ...
    export TPM_SERVER_NAME=10.0.2.14
    tss@TSS ~ $ set | grep TPM
    TPM_SERVER_HOSTNAME=10.0.2.14
    ...


## 3.2.2
### **Grading criterion**: report should contain a dump EK and description how it was obtained, 2 points.
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
	
	tss@TSS ~ $ getpubkey
	Missing key handle.

	getpubkey -ha <key handle> -pwdk keypassword


	tss@TSS ~ $ getpubkey -ha 40000000 -pwdk superhemligt_s
	Error Invalid key handle from TPM_GetPubKey

Will have to try smth else, gotta leave now