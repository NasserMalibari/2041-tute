#!/bin/dash

if [ $# -lt 1 ]
then
    echo "args pls" 
    exit 1
fi

for program in "$@"
do
    directories=$( echo $PATH | tr ':' ' ' )
    # directories='dir1 dir2 dir3'
    # echo $directories
    for  directory in $directories
    do
        # try to find program
        file="$directory/$program"
        if test -x "$file"
        then
            ls -l "$file"
        fi
    done

done
