#!/bin/bash

# Retrieve the percentage of disk space used on the root directory
# `df /` outputs disk usage for the root directory
# `awk 'NR==2 {print $5}'` extracts the percentage used from the second row of the output
# `sed 's/%//'` removes the percentage sign from the result
root_usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

# Retrieve the percentage of disk space used on the home directory
# `df $HOME` outputs disk usage for the home directory
# `awk 'NR==2 {print $5}'` extracts the percentage used from the second row of the output
# `sed 's/%//'` removes the percentage sign from the result
Home_usage=$(df $HOME | awk 'NR==2 {print $5}' | sed 's/%//')

# Check if the root directory usage percentage is not zero
if [[ $root_usage -ne 0 ]]; then
    # Calculate the percentage of home directory usage relative to the root directory usage
    # The formula used is: (Home_usage * 100) / root_usage
    percentage=$(( Home_usage * 100 / root_usage ))
    
    # Output the calculated percentage
    echo "Percentage of home directory usage relative to the root directory: $percentage%"
else
    # If the root directory usage percentage is zero, print an error message
    echo "Root directory usage is zero, can't calculate percentage"
fi

