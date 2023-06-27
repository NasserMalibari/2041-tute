#!/bin/sh

touch "template"


if [ $# -ne 2 ]
then
    echo "wrong num of args" >2
    exit 1
fi

title=$1
num_qs=$2

echo "# '$title'" > template

# should check num_qs is a num

i=1

while [ $i -le $num_qs ]
do
    echo "\n\n" >> template
    echo "# "$i"" >> template
    i=$(( i + 1))
done





# echo "hello world"