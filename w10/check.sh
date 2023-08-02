#!/bin/dash

cut -d' ' -f1 < Marks |
sort  |
uniq -c |
grep -E -v '^ *1 ' |
sed -E 's/^ *([0-9]+) //'
# sed -e 's/^.* //'

# alternatively use this instead of uniq -c
# uniq -d

