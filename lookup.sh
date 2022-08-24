#!/bin/bash
mac=${1}

if [[ -z "$mac" ]]
then
  echo "Please pass mac-address as argument."
else
  echo $(python macinfo/__init__.py --mac_address="${mac}")
fi
