#!/bin/bash

read -p "Enter a number: " NUM
echo

if [ $NUM -gt 100 ]
then
    echo "We have entered in IF block"
    sleep 3
    echo "Your number is greater then 100"
    echo
else
    echo "We have entered in ELSE block"
    echo "Your number is less then 100"
fi

echo "Script execute complete successully"