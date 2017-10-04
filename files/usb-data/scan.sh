#!/bin/sh

flash_files=$(ls *.E01)
dir_data="DATA"
dir_extracted="extracted"

make_dir() {
    [ -d "$1" ] || mkdir -p "$1"
}

# Create data folder if not present.
make_dir $dir_data

remove_file_ending() {
    printf "%s" "${1%%.*}"
}

step() {
    printf " * $1\n"
}

interesting_files="\
.zip
.jpeg
.jpg
.doc
.docx
.txt
.bmp
.pdf"

get() {
#    printf "%s <--->" $*
    # Grab the image filename.
    file=$1
    shift
    # Grab the file-folder.
    folder=$1
    shift
    # Shift the input variables according to second input.
    shift $1
    # $1 = filename, $2 = inum.
    output_file=$folder/$dir_extracted/$1
    # Make sure folder exists.
    make_dir ${output_file%/*}
    icat $file $2 > $output_file
}

extract_file() {
    IFS_old=$IFS
    IFS='|'
    get $1 $2 2 $3
    IFS=$IFS_old
}

for file in $flash_files; do
    printf "Extracting information for file $file.\n"
    name="$(remove_file_ending $file)"

    # Make sure there is a folder for the data.
    dir_file="$dir_data/$name"
    make_dir $dir_file

    step "Extracting file system details."
    fsstat $file > $dir_file/fsstat.txt 2>&1

    step "Extracting time data."
    tsk_gettimes $file > $dir_file/timedata.txt

    #step "Dumping all files with sorter."
    #make_dir "$dir_file/sorter"
    #sorter -h -d $dir_file/sorter $file

    step "Sorting out interesting files."
    interesting="$(grep -Fri "$interesting_files" $dir_file/timedata.txt)"
    # Dump to file.
    printf "%s\n" "$interesting" > $dir_file/interesting.txt
    old_IFS=$IFS
    IFS='
'
    for interesting_line in $interesting; do
        #printf "%s\n" "$interesting_line"
        extract_file $file $dir_file "$interesting_line"
    done
    IFS=$old_IFS

    printf "DONE with $file.\n\n"
done
