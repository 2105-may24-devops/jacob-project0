#!/bin/bash

SUCCESS=0
ERROR=1

cp test_input.txt append_test.txt

echo 'Testing AssetManagement.py append command...'
sudo python3.9 AssetManagement.py append . append_test . test_input

generated="./append_test.txt"
correct="./append_expected.txt"

if cmp -s "$generated" "$correct"; then
    echo "SUCCESS!"
    printf 'The generated file "%s" is the same as the correct file "%s".\n' "$generated" "$correct"
    RESULT=$SUCCESS
else
    >&2 echo "FAILURE!!"
    >&2 printf 'The generated file "%s" is different from the correct file "%s".\n' "$generated" "$correct"
    RESULT=$ERROR
fi

echo 'Removing the test files...'
rm append_test.txt
echo 'Removed.'
exit $RESULT