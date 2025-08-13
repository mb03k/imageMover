#!/bin/bash

input="~/Desktop/imageMover/imageMover/listeMitDateinamen.txt"

while IFS= read line
do
  echo "$line"
  echo "- jetzt mit der 6 und .RAW davor/danach"
  
  changedLine="6$line.RAW"
  echo $changedLine
  echo ""
done < "$input"
