#!/bin/bash
# https://stackoverflow.com/a/15679298
filein="002-branches.txt"
fileout="003-hashes.txt"
echo "" > $fileout
while read line ; do
  echo $line
  echo $line >> $fileout
  echo git log -n 1 --pretty=format:\"%H\" $line
  git log -n 1 --pretty=format:"%H" $line >> $fileout
  echo "" >> $fileout
  echo "" >> $fileout
done < $filein
