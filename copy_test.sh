#!/bin/bash

SUCCESS=0
ERROR=1

echo 'Testing AssetManagement.py copy command...'
python3.9 AssetManagement.py copy . test_input . copy_results

generated="./copy_results.txt"
correct="./test_input.txt"

if cmp -s "$generated" "$correct"; then
    echo "SUCCESS!"
    printf 'The generated file "%s" is the same as the correct file "%s".\n' "$generated" "$correct"
    RESULT=$SUCCESS
else
    >&2 echo "FAILURE!!"
    >&2 printf 'The generated file "%s" is different from the correct file "%s".\n' "$generated" "$correct"
    RESULT=$ERROR
fi

echo 'Removing the test file...'
rm copy_results.txt
echo 'Removed.'
exit $RESULT