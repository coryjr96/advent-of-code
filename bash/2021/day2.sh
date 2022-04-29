#DAY 2 2021

#!/bin/bash

data=()
while IFS= read -r line; do
    data+=("$line")
done </home/cory.j.mitchell.ctr/advent-of-code/day2input.txt

len="${#data[*]}"
IFS=' '
operators=()
values=()

for line in "${data[@]}"
do
    :
    holder=()
    read -a holder <<< "$line"
    operators+=(${holder[0]})
    values+=(${holder[1]})
done

horizontal=0
depth=0 

for (( i=0; i<$len; i++ ))
do
    :
    if [ ${operators[$i]} == "forward" ]
    then
        horizontal=$(( $horizontal + ${values[$i]} ))
    elif [ ${operators[$i]} == "down" ]
    then
        depth=$(( $depth + ${values[$i]} ))
    else
        depth=$(( $depth - ${values[$i]} ))
    fi
done

answer=$(( $depth * $horizontal ))

echo Part One Answer: $(( $depth * $horizontal ))

horizontal=0
depth=0
aim=0

for (( i=0; i<$len; i++ ))
do
    :
    if [ ${operators[$i]} == "forward" ]
    then
        horizontal=$(( $horizontal + ${values[$i]} ))
        depth=$(( $depth + $aim * ${values[$i]} )) 
    elif [ ${operators[$i]} == "down" ]
    then
        aim=$(( $aim + ${values[$i]} ))
    else
        aim=$(( $aim - ${values[$i]} ))
    fi
done

answer=$(( $depth * $horizontal ))

echo Part One Answer: $(( $depth * $horizontal ))
