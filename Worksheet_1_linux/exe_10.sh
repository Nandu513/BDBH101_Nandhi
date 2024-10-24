#!/bin/bash
#define a sequence
seq="AGTCCGTHNSKAGTCGTCGTAHAGTAGATNC"

# Define correct nucleotide bases
bases=("A" "G" "T" "C")

# Count each nucleotide
for base in "${bases[@]}"; do
    count=$(echo "$seq" | tr -cd "$base" | wc -c)
    echo "Count_${base}: $count"
done

# Extract and count non-nucleotide characters
# Remove valid nucleotides and then sort and count unique characters
non_nucleotides=$(echo "$seq" | tr -d "AGCT")
if [ -n "$non_nucleotides" ]; then
    echo "Non-nucleotide characters and counts:"
    echo "$non_nucleotides" | fold -w1 | sort | uniq -c | awk '{print "Character:", $2, "Count:", $1}'
else
    echo "All characters in the sequence are valid nucleotides."
fi

