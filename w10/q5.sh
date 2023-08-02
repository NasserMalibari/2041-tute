#!/bin/sh

directory=/usr

for c_file in $(find $directory -name "*.c" -type f -maxdepth n)
do
    echo "send $c_file as an email"
done


















# # depends on pathnames not containing white-space

# for c_file in $(find  "$directory" -type f -name '*.c' )
# do
#     echo $c_file
#     # echo mutt -s "C for you"  -a "$c_file" -- andrewt@unsw.edu.au
# done
