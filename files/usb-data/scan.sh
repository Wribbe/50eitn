#!/bin/sh

flash_files=$(ls *.E01)
data_folder="DATA"


make_dir() {
    [ -d "$1" ] || mkdir "$1"
}

# Create data folder if not present.
make_dir $data_folder

remove_file_ending() {
    printf "%s" "${1%%.*}"
}

for file in $flash_files; do
    printf "Extracting information for file $file.\n"
    name="$(remove_file_ending $file)"
    # Make sure there is a folder for the data.
    dir_file="$data_folder/$name"
    make_dir $dir_file
    printf " * Extracting file system details.\n"
    fsstat $file > $dir_file/fsstat.txt 2>&1
    printf " * Extracting time data.\n"
    tsk_gettimes $file > $dir_file/timedata.txt
    printf "DONE with $file.\n\n"
done
