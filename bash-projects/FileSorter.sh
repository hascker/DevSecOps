#!/bin/bash

#Defining the directory path that needs to be sorted
BASE_FOLDER="/Users/yousufmohammad/Downloads/DevOps/Another"

#Going inside the directory and checking if its exist or not.
cd "$BASE_FOLDER" || { echo "Folder not found!"; exit 1; }

#Process all files with extensions taken into account brackets,parentheses & special characters.

find . -maxdepth 1 -type f -name "*.*" -print0 | sort -z | while IFS= read -r -d '' file; do
filename="$(basename "$file")"
ext="${filename##*.}"

#Using tr as the bash version is <4.
ext="$( echo "$ext" | tr '[:upper:]' '[:lower:]')" 

#Create folder if it doesnt exist
mkdir -p "$ext"

#Move the file
echo "Moving '$filename' to folder '$ext/'"
mv "$filename" "$ext/" 
done




