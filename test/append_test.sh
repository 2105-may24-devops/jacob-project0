#!/bin/bash

SUCCESS=0
ERROR=1

cp test_input.txt append_test.txt

echo 'Testing AssetManagement.py append command...'
cd ..
python3.9 ./AssetManagement.py append ./test append_test ./test test_input

generated="./test/append_test.txt"
correct="./test/append_expected.txt"

if cmp -s "$generated" "$correct"; then
    echo "SUCCESS!"
    printf 'The generated file "%s" is the same as the correct file "%s".\n' "$generated" "$correct"
    RESULT=$SUCCESS
else
    >&2 echo "FAILURE!!"
    >&2 printf 'The generated file "%s" is different from the correct file "%s".\n' "$generated" "$correct"
    RESULT=$ERROR
fi

echo 'Removing the generated files...'
rm $generated
echo 'Removed.'
exit $RESULT