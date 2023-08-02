#!/usr/bin/dash

directory=$1

for file in *
do
    if [ -f "$file" ] 
    then
        echo "rm $file"
    fi
done

for dir in "$directory"/*
do
    echo $dir
    if  [ -d "$dir" ] && [ "$dir" != "." ] && [ "$dir" != ".." ]
    then
        echo "delete $dir" ?
        read answer
        if [ $answer = "yes" ]
        then
            ./rmall.sh $dir
        fi
    fi

done
