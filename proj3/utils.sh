#!/bin/sh

handle_SRK=40000000

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

Q() {
  printf "    Question:\n"
  prev_IFS=$IFS
  IFS='
' # Split on newlines.
  printf "        %s\n" $1
  # Restore old IFS.
  IFS=$prev_IFS
}

A() {
  printf "    Answer:\n"
  prev_IFS=$IFS
  IFS='
' # Split on newlines.
  printf "        %s\n" $1
  # Restore old IFS.
  IFS=$prev_IFS
  printf "\n"
}
