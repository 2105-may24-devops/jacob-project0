#!/bin/bash

echo 'Testing AssetManagement.py copy command...'
sudo python3.9 AssetManagement.py copy . test_input . copy_results
echo 'Complete.'

generated="./copy_results.txt"
correct="./test_input.txt"

if cmp -s "$generated" "$correct"; then
    echo "SUCCESS!"
    printf 'The generated file ["%s"] is the same as the correct file ["%s"].\n' "$generated" "$correct"
else
    echo "FAILURE!!"
    printf 'The generated file ["%s"] is different from the correct file ["%s"]\n' "$generated" "$correct"
fi

#echo 'Removing the test file...'
#rm copy_results.txt
#echo 'Removed.'