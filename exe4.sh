#!/bin/bash

# Retrieve the percentage of disk space used on the home directory
# `df $HOME` outputs disk usage for the home directory
# `awk 'NR==2 {print $5}'` extracts the percentage used from the second row of the output
# `sed 's/%//'` removes the percentage sign from the result
x=$(df $HOME | awk 'NR==2 {print $5}' | sed 's/%//')

# Define a threshold value for disk usage percentage
threshold=70

# Compare the current disk usage percentage with the threshold
if [[ $x -gt $threshold ]]; then
    # If the used percentage is greater than the threshold, print a warning message
    echo "You have used more than 70% of disk space"
else
    # If the used percentage is less than or equal to the threshold, print the current usage percentage
    echo "You used only $x% of disk space"
fi

