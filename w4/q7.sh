#!/bin/dash

cat alias |
sed -E -n '/Addresses/,/Owners/p' |
grep -E '^\s+z[0-9]{7}' |
tr -d ' ' 