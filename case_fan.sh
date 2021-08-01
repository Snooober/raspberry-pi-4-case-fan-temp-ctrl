#!/bin/bash

python3 -u case_fan.py | systemd-cat &

while :
do
	TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
	echo "case-fan.service: timestamp ${TIMESTAMP}" | systemd-cat
	sleep 60
done
