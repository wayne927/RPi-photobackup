#!/bin/bash

source=$1
target=$2
dryrun=$3

arg=""
if [ $dryrun -eq "1" ]; then
    arg="--dry-run"
fi

rm -f ../output.txt

rsync -rzvh --update --size-only $arg "/media/pi/$source/" "/media/pi/$target/$source/" > ../output.txt
#rsync -rzvh  $arg "/media/pi/$source/" "/media/pi/$target/$source/" > ../output.txt
