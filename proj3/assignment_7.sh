#!/bin/sh

. ./utils.sh # Load utility functions.

{ [ $# -eq 1 ] && { [ $1 = TSS_p1 ] || [ $1 = TPM2 ] || [ $1 = TSS_p2 ] ; };} || { printf "Usage: $0 TSS_p1|TSS_p2|TPM2\n" && exit; }

# Set up common filenames for all the different runs.
file_orig_bound=3_7_3_file_bound.txt
file_bound=${file_orig_bound%%.*}.bound
file_unbound=${file_orig_bound%%.*}.unbound

file_orig_sign=3_7_3_file_sign.txt
file_sign=${file_orig_sign%%.*}.signature

# Common names and types.
name_sign_key=3_7_2_sign_key
keytype_sign=s

name_bind_key=3_7_2_bind_key
keytype_bind=b

stored_handle_bind=${name_sign_key}_stored_handle.txt

if [ $1 = TSS_p1 ]; then # First run on the TSS.

  heading "3.7.2 TPM Authentication -- Questions."

  Q "Could the verifyfile command be done by another TPM?"
  A "Yes, it only uses the public part of the key to verify the signature."

  Q "Which TPM command is used to decrypt the file?"
  A "TPM_UnBind is used to decrypt files."

  Q "Can sealing be used in decryption based authentication instead of verifyfile?"
  A "Not really, the PCR-values will not match from one TPM to another, so only
the original TPM can do the unsealing."

  heading "3.7.3 TPM Authentication -- First pass on TSS."

  comment "Preparing files for signing and binding."

  comment "Create file for binding."
  string_bound="STRING IN BOUND FILE!\n"
  printf "" > $file_orig_bound # Reset/create file.
  printf "$string_bound" > $file_orig_bound
  run "cat $file_orig_bound"

  comment "Prepare file to sign."
  string_sign="THIS IS THE STRING IN THE SIGN FILE!\n"
  printf "" > $file_orig_sign # Reset/create file.
  printf "$string_sign" > $file_orig_sign
  run "cat $file_orig_sign"

  # Remove any key files that have already been created.
  rm -rf $name_storage_key.key
  rm -rf $name_storage_key.pem

  comment "Creating a signing key."
  run "createkey -hp $handle_SRK -pwdp sss -ok $name_sign_key -kt $keytype_sign"

  comment "Load created key."
  run "loadkey -hp $handle_SRK -ik $name_sign_key.key -pwdp sss"
  key_handle_sign=${command_output##*' '}
  printf "Got key handle: $key_handle_sign\n"

  comment "Sign the file."
  run "signfile -hk $key_handle_sign -if $file_orig_sign -os $file_sign"

  comment "Store the signing key-file in the shared folder."
  run "sudo cp $name_sign_key.pem shared"

  comment "Store the original file in  the shared folder."
  run "sudo cp $file_orig_sign shared"

  comment "Store the sign file in the shared folder."
  run "sudo cp $file_sign shared"

  comment "Create the binding key."
  run "createkey -hp $handle_SRK -pwdp sss -ok $name_bind_key -kt $keytype_bind"

  comment "Load created bind key."
  run "loadkey -hp $handle_SRK -ik $name_bind_key.key -pwdp sss"
  key_handle_bind=${command_output##*' '}
  printf "Got key handle: $key_handle_bind\n"

  comment "Store key-handle for bind key."
  printf "%s\n" "$key_handle_bind" > $stored_handle_bind
  run "cat $stored_handle_bind"

  comment "Store public part of binding key in shared folder."
  run "sudo cp $name_bind_key.pem shared"

  comment "Store original binding file in shared folder."
  run "sudo cp $file_orig_bound shared"

elif [ $1 = TPM2 ]; then # Intermediate run on TPM2 for verifying and binding.
  heading "3.7.3 TPM Authentication -- pass on TPM2."

  comment "Verify signature from TPM1, (No output == Verified..)"
  run "verifyfile -v -is shared/$file_sign -if shared/$file_orig_sign -ik shared/$name_sign_key.pem"

  comment "Bind file from shared."
  run "bindfile -ik shared/$name_bind_key.pem -if shared/$file_orig_bound -of $file_bound"

  comment "Store the bound file in shared."
  run "sudo cp $file_bound shared"
elif [ $1 = TSS_p2 ]; then # Last run on TSS, unbind/decrypt file.
  heading "3.7.3 TPM Authentication -- Second pass on TSS."

  comment "Decrypt bound file."
  run "unbindfile -hk $(cat $stored_handle_bind) -if shared/$file_bound -of $file_unbound"

  run "cat $file_unbound"
fi
