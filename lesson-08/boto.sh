#! /usr/bin/env bash

source secret.sh

function main()
{
  if ! ACCESS_KEY_ID=${access_key_id} SECRET_KEY_ID=${secret_key_id} \
       BUCKET_NAME=${bucket_name} \
       ./boto.py ; then
    echo "Failed to run boto.py"
    return 1
  fi
  echo "Success!"
}

main $@
