#!/bin/bash
# https://stackoverflow.com/a/15679298
#filein="002-branches.txt"
filein="002-branches-manually-sorted.txt"
fileout="003-hashes.txt"
echo "" > $fileout
while read line ; do
  [[ -z $line ]] && continue
  echo $line
  echo $line >> $fileout
  echo git log -n 1 --pretty=format:\"%H\" $line
  git log -n 1 --pretty=format:"%H" $line >> $fileout
  echo "" >> $fileout
  echo "" >> $fileout
done < $filein
