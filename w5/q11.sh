#!/bin/dash

top_and_bottom() {

    file=$1
    echo "==================="
    echo "$file"
    echo "----------"
    # head -1 $file
    # tail -1 $file
    sed -E -n '1p;$p' "$file"

    echo ""
}

for filename in "$@"
do
    top_and_bottom $filename

done

# top_and_bottom $1