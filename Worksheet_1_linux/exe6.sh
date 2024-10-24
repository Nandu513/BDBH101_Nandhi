#!/bin/bash
#set -x
read -p "Enter a directory name: " dir
cd $dir
# Iterate over each item in the directory
for directory in *; do
    # Check if the item is a directory
    if [ -d $directory ]; then
        # If it's a directory, append the information to 'sub_dir_list.txt'
        echo "$directory is a sub_directory" >> sub_dir_list.txt
    else 
        # If it's not a directory, print a message
        echo "$directory is not a directory"
    fi
done

# List all items in the directory, excluding 'sub_dir_list.txt', and append their names and sizes to 'sub_dir_list.txt'
ls -lh | grep -v "sub_dir_list.txt" | awk '{print $9, $5}' >> sub_dir_list.txt

# Display the content of 'sub_dir_list.txt' to the terminal
cat sub_dir_list.txt

#set +x


