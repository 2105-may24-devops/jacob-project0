#!/bin/bash

echo 'Testing AssetManagement.py write command...'
sudo python3.9 AssetManagement.py write . test_input . write_results
echo 'Complete.'

generated="./write_results.txt"
correct="./write_test.txt"

if cmp -s "$generated" "$correct"; then
    echo "SUCCESS!"
    printf 'The generated file ["%s"] is the same as the correct file ["%s"].\n' "$generated" "$correct"
else
    echo "FAILURE!!"
    printf 'The generated file ["%s"] is different from the correct file ["%s"]\n' "$generated" "$correct"
fi

echo 'Removing the test file...'
rm write_results.txt
echo 'Removed.'
