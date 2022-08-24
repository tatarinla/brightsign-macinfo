#!/bin/bash
mac=${1}

cd ../../
chmod 755 lookup.sh
./lookup.sh ${mac}
