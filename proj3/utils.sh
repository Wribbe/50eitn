#!/bin/sh

run() {
  printf "\n%s\n" ">>>>"
  printf "Running command:\n    %s\n" "$1"
  command_output="$($1)"
  printf "Got output:\n"
  prev_IFS=$IFS
  IFS='
' # Split on newlines.
  printf "    %s\n" $command_output
  # Restore old IFS.
  IFS=$prev_IFS
  printf "%s\n\n" "<<<<"
}

comment() {
  printf "\n### %s ###\n" "$1"
}

heading() {
  printf "\n"
  printf "######################################################\n"
  printf "#### $1\n"
  printf "######################################################\n"
  printf "\n"
}
