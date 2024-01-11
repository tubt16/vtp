#!/bin/bash

echo "###################################"
date

ls /var/run/httpd/httpd.pid &> /dev/null

if [ $? -eq 0 ]
then
	echo "Httpd process is running"
else
	echo "Httpd process is NOT running"
	echo
	echo "Starting httpd process"
	sudo systemctl start httpd
	if [ $? -eq 0 ]
	then
		echo "Httpd started successfully"
	else
		echo "Httpd started failed"
	fi
fi
echo "###################################"
echo

## * * * * * /opt/scripts/section9_monitoring.sh &>> /var/log/monitorHttpd.log 
## lap lich chay script moi phut va luu log vao file /var/log/monitorHttpd.log