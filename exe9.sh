#!/bin/bash

# Get the current hour in 24-hour format (0-23) using the 'date' command
date=$(date +%H)

# Check if the hour is less than or equal to 12 (i.e., morning)
if [ $date -le 12 ]; then
    # If it is morning, print "Good Morning"
    echo "Good Morning"
else
    # If the hour is greater than 12, check if it is less than or equal to 18 (i.e., afternoon)
    if [ $date -gt 12 ] && [ $date -le 18 ]; then
        # If it is afternoon, print "Good Afternoon"
        echo "Good Afternoon"
    else
        # If the hour is greater than 18 (i.e., evening or night), print "Good Night"
        echo "Good Night"
    fi
fi

