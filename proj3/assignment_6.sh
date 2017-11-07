#!/bin/sh

. ./utils.sh # Load utility functions.

name_key_migratable_bind=6_key_binding_migratable
name_key_migrate=tpm2_migration_key
name_key_storage=tpm1_storage_key
name_key_legacy=tpm1_legacy_key

handle_tpm2_migrate_key=handle_tpm2_migrate_key

file_ass6_bound_file_orig=ass6_bound.txt
file_ass6_bound_file_bound=${file_ass6_bound_file_orig%%.*}.bound
file_ass6_bound_file_unbound=${file_ass6_bound_file_orig%%.*}.unbound
file_sealing_orig=ass6_sealfile.txt
file_sealing_sealed=ass6_sealfile.seal
file_sealing_unsealed=ass6_sealfile.unseal

type_migbind_key=bm
type_migrate_key=em
type_storage_key=e
type_legacy_key=l
password_migration=mmm
password_mig_key=kmmm

blob_tpm1_bind=blob_tpm1_bind
blob_tpm1_storage=blob_tpm1_storage

stored_tpm2_migration_handle=stored_tpm2_migration_handle.txt

if [ $1 -eq 1 ]; then

  heading "3.6.2 -- File encryption."

  comment "Create migratable bind key."
  run "createkey -kt $type_migbind_key -ok $name_key_migratable_bind -hp $handle_SRK -pwdp sss -pwdm $password_migration"

  comment "Load created key."
  run "loadkey -hp $handle_SRK -ik $name_key_migratable_bind.key -pwdp sss"
  key_handle_migratable_bind=${command_output##*' '}
  printf "Got key handle: $key_handle_migratable_bind\n"

  comment "Create a file that can be bound."
  echo "CONTENT OF BOUND FILE\n" > $file_ass6_bound_file_orig
  run "cat $file_ass6_bound_file_orig"

  comment "Bind file."
  run "bindfile -ik $name_key_migratable_bind.pem -if $file_ass6_bound_file_orig -of $file_ass6_bound_file_bound"

  comment "Unbinding file."
  run "unbindfile -hk $key_handle_migratable_bind -if $file_ass6_bound_file_bound -of $file_ass6_bound_file_unbound"

  comment "Check contents of unbound file."
  run "cat $file_ass6_bound_file_unbound"

  comment "Copy bound file to shared folder."
  run "sudo cp $file_ass6_bound_file_bound shared"

elif [ $1 -eq 2 ]; then

  heading "3.6.2 -- TPM2 -- creating migration key."

  comment "Create migration key."
  run "createkey -kt $type_migrate_key -ok $name_key_migrate -hp $handle_SRK -pwdp sss -pwdm $password_migration -pwdk $password_mig_key"

  comment "Load created key."
  run "loadkey -hp $handle_SRK -ik $name_key_migrate.key -pwdp sss"
  handle_tpm2_migrate_key=${command_output##*' '}
  printf "Got key handle: $handle_tpm2_migrate_key\n"

  comment "Store migration key handle for later use."
  printf $handle_tpm2_migrate_key > $stored_tpm2_migration_handle
  run "cat $stored_tpm2_migration_handle"

  comment "Store migration key in shared dir."
  run "sudo rm shared/$name_key_migrate.key shared/$name_key_migrate.pem"
  run "sudo cp $name_key_migrate.* shared"

elif [ $1 -eq 3 ]; then

  heading "3.6.2 -- TPM1 -- Using migration key from TPM2."

#  run "createkey -kt em -pwdk mig -pwdp sss -pwdm mmm -ok mig -hp $handle_SRK"
#  #run "createkey -kt em -pwdk bbb -pwdp sss -pwdm mmm -ok bind -hp $handle_SRK"
#  run "createkey -kt em -pwdp sss -pwdm mmm -ok bind -hp $handle_SRK"
#
#  run "migrate -hp $handle_SRK -pwdp sss -pwdo ooo -im mig.key -pwdm mmm -pwdk mig -ok migBlob -ik bind.key"

  comment "Grab TPM2 key from shared."
  run "rm -f $name_key_migrate.key $name_key_migrate.pem"
  run "cp shared/$name_key_migrate.* ."

  comment "Create migration blob for key."
  run "migrate -hp $handle_SRK -pwdp sss -pwdo ooo -im $name_key_migrate.key -pwdm $password_migration -pwdk $password_mig_key -ik $name_key_migratable_bind.key -ok $blob_tpm1_bind"

  comment "Copy migration blob to shared folder."
  run "sudo cp $blob_tpm1_bind shared"

elif [ $1 -eq 4 ]; then

  heading "3.6.2 -- TPM2 -- Using migration blob from TPM1."

  comment "Retrieve migration blob from shared folder."
  run "cp shared/$blob_tpm1_bind ."

  handle_tpm2_migrate_key=$(cat $stored_tpm2_migration_handle)
  comment "Load the migration blob into TMP2."
  run "loadmigrationblob -hp $handle_tpm2_migrate_key -if $blob_tpm1_bind -pwdp $password_mig_key"
  handle_tpm1_bind_key=${command_output##*' '}
  printf "Got key handle: $handle_tpm1_bind_key\n"

  comment "Grab encrypted file from shared."
  run "cp shared/$file_ass6_bound_file_bound ."

  comment "Unbind file with migrated bind key."
  run "unbindfile -hk $handle_tpm1_bind_key -if $file_ass6_bound_file_bound -of $file_ass6_bound_file_unbound"

  comment "Check contents of unbound file."
  run "cat $file_ass6_bound_file_unbound"

elif [ $1 -eq 5 ]; then

  ########################################
  heading "3.6.3 -- TPM1 -- Data sealing."
  ########################################

  comment "Create storage key."
  run "createkey -kt $type_storage_key -ok $name_key_storage -hp $handle_SRK -pwdp sss"

  comment "Load created storage key."
  run "loadkey -hp $handle_SRK -ik $name_key_storage.key -pwdp sss"
  handle_storage_key=${command_output##*' '}
  printf "Got key handle: $handle_storage_key\n"

  comment "Prepare file for sealing."
  printf "STRING IN SEALFILE\n" > $file_sealing_orig
  run "cat $file_sealing_orig"

  comment "Seal the file."
  run "sealfile -hk $handle_storage_key -if $file_sealing_orig -of $file_sealing_sealed"

  comment "Unseal the file."
  run "unsealfile -hk $handle_storage_key -if $file_sealing_sealed -of $file_sealing_unsealed"

  comment "Check contents of unsealed file."
  run "cat $file_sealing_unsealed"

  ########################################
  heading "3.6.3 -- TPM1 -- Data sealing, legacy."
  ########################################

  comment "Create and load legacy key."
  run "createkey -kt l -ok key_legacy -hp $handle_SRK -pwdp sss"
  run "loadkey -hp $handle_SRK -ik key_legacy.key -pwdp sss"
  current_handle=${command_output##*' '}

  comment "Use legacy key to seal."
  run "sealfile -hk $current_handle -if $file_sealing_orig -of $file_sealing_sealed"

  ########################################
  heading "3.6.3 -- TPM1 -- Data sealing, binding."
  ########################################

  comment "Create and load binding key."
  run "createkey -kt b -ok key_binding -hp $handle_SRK -pwdp sss"
  run "loadkey -hp $handle_SRK -ik key_binding.key -pwdp sss"
  current_handle=${command_output##*' '}

  comment "Use binding key to seal."
  run "sealfile -hk $current_handle -if $file_sealing_orig -of $file_sealing_sealed"

  ########################################
  heading "3.6.3 -- TPM1 -- Data sealing, sign."
  ########################################

  comment "Create and load sign key."
  run "createkey -kt d -ok key_sign -hp $handle_SRK -pwdp sss"
  run "loadkey -hp $handle_SRK -ik key_sign.key -pwdp sss"
  current_handle=${command_output##*' '}

  comment "Use sign key to seal."
  run "sealfile -hk $current_handle -if $file_sealing_orig -of $file_sealing_sealed"

  ########################################
  heading "3.6.3 -- TPM1 -- Sealing and storage key migration."
  ########################################

  comment "Migrate key that was used to seal the file earlier."

  run "migrate -hp $handle_SRK -pwdp sss -pwdo ooo -im $name_key_migrate.key -pwdm $password_migration -pwdk $password_mig_key -ik $name_key_storage.key -ok $blob_tpm1_storage"

  comment "Error means that the key is not migratable."

  comment "Create and load a migratable storage key."
  name_key_migstore=key_migratable_storage
  run "createkey -kt em -ok $name_key_migstore -hp $handle_SRK -pwdp sss -pwdm $password_migration"
  run "loadkey -hp $handle_SRK -ik $name_key_migstore.key -pwdp sss"
  current_handle=${command_output##*' '}

  comment "Use migratable storage key for sealing."
  run "sealfile -hk $current_handle -if $file_sealing_orig -of $file_sealing_sealed"

  comment "Can't use a migratable storage key for sealing, no use in trying to migrate it to TPM2"
fi
