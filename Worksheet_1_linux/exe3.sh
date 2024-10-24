#!/bin/bash

# Define the list of FASTA files
file_list=$(ls *.fasta)

# Define the motifs to search for
motifs=("YVDRHPDDTINDYLNSI" "MGNHTWDHPDIFEILTTK")

# Process each FASTA file
for file in $file_list
do
    if [ -f "$file" ]; then
        echo "Processing file: $file"

        # Read the file, removing FASTA headers and concatenating lines
        sequence=$(grep -v ">" "$file" )

        # Search for each motif
        for motif in "${motifs[@]}"; do
            echo "Searching for motif: $motif"
            pos=$(echo "$sequence" | grep -b -o "$motif" )
            
             # Check if any positions were found
            if [ -n "$pos" ]; then
                echo "Motif '$motif' found in file '$file' at character positions: $pos"
            else
                echo "Motif '$motif' not found in file '$file'"
            fi
        done
    else 
        echo "$file is not a file"
    fi
done

