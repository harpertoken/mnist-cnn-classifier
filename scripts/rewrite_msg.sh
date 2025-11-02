#!/bin/bash

# Script to rewrite commit messages for conventional commits
# Makes first line lowercase and truncates to 60 chars

while IFS= read -r line; do
    if [ -z "$first_line_done" ]; then
        # Process first line
        # Make lowercase
        line=$(echo "$line" | tr '[:upper:]' '[:lower:]')
        # Truncate to 60 chars
        line=$(echo "$line" | cut -c1-60)
        first_line_done=1
    fi
    echo "$line"
done
