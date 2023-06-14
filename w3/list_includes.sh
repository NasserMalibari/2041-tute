#!/usr/bin/sh

# globbing
for file in *.c # --> for file in a.c b.c wc.c uniq.c
do
    echo "$file includes:"
    
    grep -E '^#include' $file | # finding #includes's
    sed -E 's/[>"][^>"]*$//' | # removing last " or >
    sed -E -e 's/^#include([[:space:]])*[<"]/    /' # remove starting rubbish
    
done