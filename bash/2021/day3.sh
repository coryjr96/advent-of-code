#DAY 3 2021

#!/bin/bash

data=()
while IFS= read -r line; do
    data+=("$line")
done </home/cory.j.mitchell.ctr/advent-of-code/day3input.txt

gamma=""
epsilon=""

for (( i=0; i<12; i++ ))
do
    :
    ones=0
    zeros=0
    for line in "${data[@]}"
    do
        :
        if [ "${line:$i:1}" == "1" ]
        then
            let "ones++"
        else
            let "zeros++"
        fi
    done
    if [ $ones -gt $zeros ]
    then
        gamma+="1"
        epsilon+="0"
    else
        gamma+="0"
        epsilon+="1"
    fi
done

gammadec="$(( 2#$gamma ))"
epsilondec="$(( 2#$epsilon ))"

echo Part One Answer: $(( $gammadec * $epsilondec ))

data2=(${data[*]})

for (( i=0; i<12; i++ ))
do
    :
    ones=0
    zeros=0
    oxygen=()
    common="0"
    for line in "${data2[@]}"
    do
        :
        if [ "${line:$i:1}" == "1" ]
        then
            let "ones++"
        else
            let "zeros++"
        fi
    done
    if [ $ones -ge $zeros ]
    then
        common="1"
    fi
    for line in "${data2[@]}"
    do
        :
        if [ ${line:$i:1} == $common ]
        then
            oxygen+=($line)
        fi
    done
    data2=(${oxygen[*]})
    len="${#data2[*]}"
    if [ $len -eq 1 ]
    then
        break
    fi
done

for (( i=0; i<12; i++ ))
do
    :
    ones=0
    zeros=0
    scrubber=()
    uncommon="1"
    for line in "${data[@]}"
    do
        :
        if [ "${line:$i:1}" == "1" ]
        then
            let "ones++"
        else
            let "zeros++"
        fi
    done
    if [ $ones -ge $zeros ]
    then
        uncommon="0"
    fi
    for line in "${data[@]}"
    do
        :
        if [ ${line:$i:1} == $uncommon ]
        then
            scrubber+=($line)
        fi
    done
    data=(${scrubber[*]})
    len="${#data[*]}"
    if [ $len -eq 1 ]
    then
        break
    fi
done

oxygendec="$(( 2#${oxygen[0]} ))"
scrubberdec="$(( 2#${scrubber[0]} ))"

echo Part Two Answer: $(( $oxygendec * $scrubberdec ))
