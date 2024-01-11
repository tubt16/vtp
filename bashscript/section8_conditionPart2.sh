#!/bin/bash

value=$(ip a | grep -v LOOPBACK | grep -ic mtu)

if [ $value -eq 1 ]
then
	echo "1 Active network interface found"
elif [ $value -gt 1 ]
then
	echo "Found multiple active interface"
else
	echo "No active interface found"
fi