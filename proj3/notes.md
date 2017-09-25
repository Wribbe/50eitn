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
    createek

Here terminal window on TPM1 running ``tpm_server`` was searched by scrolling for keys.  

(Note: had to abort session due to f*ckin utrymningsövning.. Will copy keys next time..)

### Memorize 'take ownership' passwords:


### **Grading criterion**: report should contain a dump SRK pubkey and description how it was obtained, 2 points.