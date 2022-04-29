#DAY 1 2021

#!/bin/bash

data=()
while IFS= read -r line; do
    data+=("$line")
done </home/cory.j.mitchell.ctr/advent-of-code/day1input.txt

len="${#data[*]}"
counter=0

for (( i=0; i<$len; i++ ))
do
    :
    if [ ${data[$i]} -gt ${data[$i-1]} ]
    then
        let "counter++"
    fi
done

echo Part One Answer: $counter

counter=0

for (( i=3; i<$len; i++ ))
do
    :
    group1=$(( ${data[$i-1]} + ${data[$i-2]} + ${data[$i-3]} ))
    group2=$(( ${data[$i]} + ${data[$i-1]} + ${data[$i-2]} ))
    if [ $group2 -gt $group1 ]
    then
        let "counter++"
    fi
done

echo Part Two Answer: $counter
