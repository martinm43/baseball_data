#!/bin/bash

# Basic script to iterate through years in reverse order
# Here I chose the introduction of free agency as my limit


start_year = 2004
end_year = 1977

for i in {$start_year..$end_year..-1}
do 
	
	echo "Processing year $i"
	python gameData.py --year $i

done

