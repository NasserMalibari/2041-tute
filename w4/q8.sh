#!/bin/dash

# ./q6.sh
cat list | 
while read zid 
do
    # better
    # q7.sh $zid
    acc $zid |
    sed -E -n '/^$/,/^$/p' |
    cut -d':' -f2 |
    tr ',' '\n' |
    tr -d ' ' |
    grep -E '^[A-Z]{4}[0-9]{4}t[1-3]_Student' |
    cut -c1-8
done |
sort |
uniq -c



# acc 'z5373462' |
# sed -E -n '/^$/,/^$/p' |
# cut -d':' -f2 |
# tr ',' '\n' |
# tr -d ' ' |
# grep -E '^[A-Z]{4}[0-9]{4}t[1-3]_Student' |
# cut -c1-8vx12 % 