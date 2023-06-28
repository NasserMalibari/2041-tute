#!/bin/dash

print_message() {
    if [ $# -eq 2 ]
    then 
        exit_status=$1
        msg=$2
        echo "$0: $msg" 2>>
        exit $exit_status
    else
        msg=$1
        echo "$0: warning: $msg"
    fi

}


# print_message "this should give warning"
print_message 42 "should exit with 42"


exit 0


