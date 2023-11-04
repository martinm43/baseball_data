#!/bin/bash

# Basic script to iterate through years in reverse order
# Here I chose the introduction of free agency as my limit

start_year=1976
end_year=1947

for ((i = $start_year; i >= $end_year; i--))
do
    echo "Processing year $i"
    python gameData.py --year $i
done

