#!/bin/bash

# Installing Depenencies
echo "#####################################"
echo "Installing package"
echo "#####################################"
sudo yum install wget unzip httpd -y > /dev/null
echo

# Start & enable service
echo "#####################################"
echo "Start & enable HTTPD service"
echo "#####################################"
sudo systemctl start httpd
sudo systemctl enable httpd
echo

# Creating Temp Directory
echo "#####################################"
echo "Start Artifact Deployment"
echo "#####################################"
mkdir -p /mnt/webfiles
cd /mnt/webfiles
echo

wget https://www.tooplate.com/zip-templates/2135_mini_finance.zip > /dev/null
unzip 2135_mini_finance.zip > /dev/null
sudo cp -r 2135_mini_finance/* /var/www/html/
echo 

# Restart service 
echo "#####################################"
echo "Restarting HTTPD service"
echo "#####################################"
sudo systemctl restart httpd
echo

# Clean up
echo "#####################################"
echo "Removing Temporary File"
echo "#####################################"
rm -rf /mnt/webfiles/
