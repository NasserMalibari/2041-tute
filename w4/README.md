# WEEK 4

# Admin

- Week 3 weekly test is due Thursday 21:00

- Next week we will talk about the assignment, git and testing with shell


# Q1

COMP2041 student wrote this script, named start_lab04.sh, to run before the Week 4 lab. 

```
cat start_lab04.sh
#! /bin/dash

cd ~/labs/04

ex1=jpg2png
ex2=email_image
ex3=date_image
ex4=tag_music`
```

```
$ pwd
/home/z1234567
$ ./start_lab04.sh
pwd
/home/z1234567
$ echo $ex1 $ex2 $ex3 $ex4

```

Why not? How can the sctipy be fixed? 


# Q2

Write a shell script, is_business_hours which exits with a status of 0 if the current time is between 9am - 5pm, and otherwise exits with a status of 1. 

Hint: The `date` command prints the current time in a format like this

# Q3

 COMP2041 student Shruti has a 'friends' subdirectory in her home directory that contains images of her many friends.
Shruti likes to view these images often and would like to have them appear in other directories within her CSE account so she has written a shell script to symlink them to the current directory:

```
for image_file in $(ls ~/friends); do
    ln -s "~/friends/$image_file" .
done
```

The links created by Shruti's script are broken.

Why? How can she fix her script? 


# Q4

The course code for COMP2041 has been changed to COMP2042 and the course code for COMP9044 has been changed to COMP9042.

Write a shell script, update_course_code.sh which appropriately changes the course code in all the files it is given as arguments. 

# Q5

Modify update_course_code.sh so if given a directory as an argument it updates the course codes in files found in that directory and its sub-directories. 

 CSE systems have a command, mlalias, which prints information about a specified mail alias.
For example:
```
$ mlalias cs2041.23T2.tutors
        Alias: cs2041.23T2.tutors
  Description: Maling List For COMP(2041|9044) 2023 T2 Tutors
        Flags: personal, public, unprivileged, members_can_post, closed
    Addresses:
               andrewt
               z9300162
               dylanb
               z5115658
               ...
               z5316004
               z5363586
               z5360319
               z3540752
       Owners: cs2041
      Senders: @COMP2041_Lecturer, @COMP2041_Supervisor
```
Convert the output of the mlalias command into a new line separated list of UNSW zIDs,
like this:
```
z9300162
z5115658
...
z5316004
z5363586
z5360319
z3540752
```