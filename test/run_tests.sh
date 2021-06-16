#!/bin/bash

ERROR_STATE=0


ERROR_STATE+=bash ./append_test.sh
ERROR_STATE+=bash ./copy_test.sh
ERROR_STATE+=bash ./write_test.sh

>&2 echo "Tests completed with " $ERROR_STATE " failures."

exit $ERROR_STATE
