#!/usr/bin/sh

# check arguments are numbers
if [ "$1" -eq "$1" ]
then
    echo "first is a number!"
else
    echo "first arg isnt a number :("
    exit
fi

#TODO: check the others are numbers too!


# check we have correct num of args
if [ "$#" -eq 1 ] 
then
    last=$1
    first=1
    increment=1
elif [ "$#" -eq 2 ]
then
    first=$1
    last=$2
    increment=$1

#TODO 3 args is possible

else
    # echo "Usage: sh seq.sh <first> <increment> <last>"
    echo "incorrect num of args"
    exit
fi


# current=$first
current=$first
#print numbers
# while test "$current" -le "$last"
while [ "$current" -le "$last" ]
do
    # print
    echo "$current"

    # increment
    current=$(( current + increment ))

done