#!/bin/dash

#===========================

# testing pigs-init behaviour when .pig already exists

# author : nasser
#date
# for assignment1 for comp(2041|9044)

#======================================

PATH=$PATH":"$(pwd)

test_dir="$(mktemp -d)"
echo $test_dir
cd $test_dir

trap 'rm -drf "$testdir"' INT EXIT TERM QUIT

expected=$(mktemp)
actual=$(mktemp)


# touch "expected"
# touch "actual"

# expected
echo "Initialized empty pigs repository in .pig" 2>&1 $expected

# actual
pigs-init 2>&1 "actual"

if ! diff
then
    echo "your test failed"
    exit 1
fi

#expected

echo "pigs-init: error: .pig already exists" 2>&1 'expected'


# actual
pigs-init 2>&1 "actual"

if ! diff
then
    echo "your test failed"
    exit 1
fi


echo "your test passed!"
exit 0

