#!/bin/bash

cd temp

# for each .ts file in temp, sort and add it to a text file
for i in `ls *.ts | sort -V`; do echo "file $i"; done > mylist.txt

# prompt final file name
read -p 'Output file name: ' file_name

# Use ffmpeg to concat all the files and move them into base directory
ffmpeg -f concat -i mylist.txt -c copy -bsf:a aac_adtstoasc "${file_name}.mp4"
mv "${file_name}.mp4" "../${file_name}.mp4"
