#!/bin/bash
read -p "Enter a file name: " file
# Check if the specified file exists and is a regular file
if [ -f $file ]; then
    # 'uniq' filters out repeated lines in the file
	uniq $file
else
    # If the file does not exist or is not a regular file, print an error message
	echo "$file is not a file"
fi
