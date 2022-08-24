#!/bin/bash
mac=${1:-"95-A1-4E-40-9D-36"}

if [[ -z "$mac" ]]
then
  echo "Please pass mac-address as argument"
else
  python tool/__init__.py --mac-address=${mac}
fi
