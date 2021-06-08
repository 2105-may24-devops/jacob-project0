#!/bin/bash

SUCCESS=0
ERROR=1

echo 'Testing AssetManagement.py write command...'
sudo python3.9 AssetManagement.py write . test_input . write_results

generated="./write_results.txt"
correct="./write_test.txt"

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
rm write_results.txt
echo 'Removed.'
exit $RESULT