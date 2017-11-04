#!/bin/sh

. ./utils.sh # Load utility functions.

heading "3.8.1 Signature based attestation."

# Create an AIK using the command identity. Use it to quote a PCR value, like R
# with the hash digest of tmpbios. Verification of the quote will be done
# automatically.

tpm_quote="/home/tss/tpm/tpm4720/libtpm/utils/quote"
label="assignment8"
output="assignment_8_aik"
std_out="assignment8_stdout.txt"

printf "" > $std_out # Clear file.

rm -f "$output.key"
rm -f "$output.pem"

comment "Create AIK for attestation."
run "identity -pwdo ooo -la $label -pwds sss -pwdk kkk -ok $output"

comment "Load key into TPM."
run "loadkey -hp $handle_SRK -ik $output.key -pwdp $PWD_SRK"
# Get key handle (split at last ' ').
key_handle=${command_output##*' '}
printf "Got key handle: $key_handle\n"

comment "Create new PCR value @ register 11."
run "sha -if $(which tpmbios) -ix 11"
pcr_value=${command_output##*' '}
printf "New PCR value: $pcr_value\n"

comment "Quote the new PCR value."
tpm_quote=/home/tss/tpm/tpm4720/libtpm/utils/quote
run "$tpm_quote -v -hk $key_handle -bm $pcr_value -pwdk kkk"
printf "Output quote assignment 8: >>>>> \n%s\n <<<<<\n\n" "$command_output" >> $std_out


heading "3.8.2 Decryption based attestation."

comment "Create a file that will be encrypted."
file_trusted=trusted.txt
string_trusted="THIS IS A TRUSTED FILE!\n"
printf "$string_trusted" > $file_trusted
run "cat $file_trusted"

comment "Update and get PCR value."
PCR_reg=12
run "sha -if $file_trusted -ix $PCR_reg"
pcr_value=${command_output##*' '}
printf "New PCR value: $pcr_value\n"

comment "Create new key for performing the sealing/unsealing."
type_storage=e
name_storage_key=attestation_encryption_key

# Remove any key files that have already been created.
rm -rf $name_storage_key.key
rm -rf $name_storage_key.pem

run "createkey -hp $handle_SRK -kt $type_storage -pwdp sss -ok $name_storage_key -ix $PCR_reg $pcr_value"

comment "Load the created key."
run "loadkey -hp $handle_SRK -ik $name_storage_key.key -pwdp sss"
key_handle=${command_output##*' '}
printf "Got key handle: $key_handle\n"

comment "Seal and unseal the trusted file."
file_sealed=${file_trusted%%.*}.seal
file_unsealed=${file_trusted%%.*}.unseal

rm -f $file_sealed $file_unsealed

run "sealfile -hk $key_handle -if $file_trusted -of $file_sealed"
run "unsealfile -hk $key_handle -if $file_sealed -of $file_unsealed"

comment "Check file contents."
run "cat $file_trusted"
run "cat $file_unsealed"

comment "Tamper with the trusted file."
string_untrusted="THIS IS NO LONGER A TRUSTED FILE!\n"
printf "$string_untrusted" > $file_trusted
run "cat $file_trusted"

comment "Update the PCR value."
run "sha -if $file_trusted -ix $PCR_reg"
pcr_value=${command_output##*' '}
printf "New PCR value: $pcr_value\n"

comment "Try to unseal the sealed file again."
rm -f $file_unsealed
run "unsealfile -hk $key_handle -if $file_sealed -of $file_unsealed"
