#!/bin/sh
rm -rf /home/pi/tpm/tpm4720/tpmstate
mkdir /home/pi/tpm/tpm4720/tpmstate
tpm_server
