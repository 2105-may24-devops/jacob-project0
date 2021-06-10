#!/bin/bash

SUCCESS=0
ERROR=1

echo 'Testing AssetManagement.py write command...'
cd ..
python3.9 ./AssetManagement.py write ./test test_input ./test write_results

generated="./test/write_results.txt"
correct="./test/write_test.txt"

if cmp -s "$generated" "$correct"; then
    echo "SUCCESS!"
    printf 'The generated file "%s" is the same as the correct file "%s".\n' "$generated" "$correct"
    RESULT=$SUCCESS
else
    >&2 echo "FAILURE!!"
    >&2 printf 'The generated file "%s" is different from the correct file "%s".\n' "$generated" "$correct"
    RESULT=$ERROR
fi

echo 'Removing the generated file...'
rm $generated
echo 'Removed.'
exit $RESULT