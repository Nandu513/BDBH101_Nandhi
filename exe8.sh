#!/bin/bash

# Define a threshold value for comparison
threshold=85

# Loop through numbers from 1 to 100
for i in {1..100}; do
    # Print the current number
    echo "$i"

    # Check if the current number is greater than or equal to the threshold
    if [ $i -ge $threshold ]; then
        # If the number meets the condition, print a message indicating it is greater than or equal to the threshold
        echo "$i is greater than or equal to threshold: $threshold"
    fi
done

