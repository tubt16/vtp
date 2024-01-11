#!/bin/bash

echo "Welcome to bash script"
echo
echo "##############################"

## This script print system uptime ##

echo "The uptime of the system is: "
uptime

## Mempry utilization ##

echo "##############################"

echo "Memory Utilization"
free -m

## Disk utilization ##

echo "##############################"

echo "Disk Utilization"
df -h