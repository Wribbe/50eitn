#!/bin/sh

## Important; source this file, as in: < source setup.sh >, don't run it.

# Setting up global user and srk password.
export PWD_OWNER=ooo
export PWD_SRK=sss

TPM_PORT=6545
IP_TPM_HOST=10.0.2.14

# Setting up ports and address.
export TPM_PATH=/home/pi/tpm/tpm4720/tpmstate
export TPM_PORT=$TPM_PORT
export TPM_SERVER_NAME=localhost
export TPM_SERVER_PORT=$TPM_PORT

if [ "$(echo $USER)" = "tss" ]; then
  # TSS specific variables, fine if both have them exported.
  export TPM_SERVER_NAME=$IP_TPM_HOST
  export TCSD_USE_TCP_DEVICE=true
  export TCSD_TCP_DEVICE_PORT=$TPM_PORT
  export TCSD_TCP_DEVICE_HOSTNAME=$IP_TPM_HOST
fi
