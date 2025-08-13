#!/bin/bash

STARTING_FOLDER="/Volumes/Untitled/DCIM/100MSDCF"

inputFileNames="$HOME/Desktop/listeMitDateinamen.txt"
inputFolderImages=""
outputPath="$HOME/Desktop"
outputFolderName="copied_images"

while IFS= read line
do
  fileSearch="_MB06$line.ARW"
  
  echo "🥉 Dateiname.. $line"
  echo "🥈 wird zu '$fileSearch'"
  echo "    🆗 $fileSearch wird nun in '/Volumes/Untitled/DCIM/100MSDCF' gesucht"

  search_solution=$(find "$STARTING_FOLDER" -name "$fileSearch" -print -quit)

  if [ -n "$search_solution" ]; then
      echo "    ✅ Datei gefunden"
      echo "🥇 $fileSearch wird nun in $outputPath/$outputFolderName kopiert"
      cp $STARTING_FOLDER/$fileSearch $outputPath/$outputFolderName

  else
      echo "❌ Die Datei wurde unter '$STARTING_FOLDER' nicht gefunden."
  fi
  
  echo ""
done < "$inputFileNames"
