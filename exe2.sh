#!/bin/bash

# Prompt the user to enter the CSV file name and store it in the variable 'file'
read -p "Enter the csv file name: " file

# Check if the specified file exists and is a regular file
if [ -f "$file" ]; then
    # If the file exists, read its content, replace commas with newlines, and save it to 'file.txt'
    cat "$file" | tr "," "\n" > file.txt
    
    # Replace colons with newlines in the 'file.txt' file and output the result to the terminal
    cat file.txt | tr ":" "\n"
else 
    # If the file does not exist, print an error message
    echo "$file is not a file"
fi

