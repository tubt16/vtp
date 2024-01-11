#!/bin/bash

# Variable Declaration
PACKAGE="httpd wget unzip"
SVC="httpd"
#URL="https://www.tooplate.com/zip-templates/2135_mini_finance.zip"
#ART_NAME="2135_mini_finance"
TEMPDIR="/mnt/webfiles"

# Installing Depenencies
echo "#####################################"
echo "Installing package"
echo "#####################################"
sudo yum install $PACKAGE -y > /dev/null
echo

# Start & enable service
echo "#####################################"
echo "Start & enable HTTPD service"
echo "#####################################"
sudo systemctl start $SVC
sudo systemctl enable $SVC
echo

# Creating Temp Directory
echo "#####################################"
echo "Start Artifact Deployment"
echo "#####################################"
mkdir -p $TEMPDIR
cd $TEMPDIR
echo

wget $1 > /dev/null
unzip $2.zip > /dev/null
sudo cp -r $2/* /var/www/html/
echo 

# Restart service 
echo "#####################################"
echo "Restarting HTTPD service"
echo "#####################################"
sudo systemctl restart $SVC
echo

# Clean up
echo "#####################################"
echo "Removing Temporary File"
echo "#####################################"
rm -rf $TEMPDIR

## Run scrip voi 2 doi so
## ./section4_argsTooplateWebSetup.sh https://www.tooplate.com/zip-templates/2132_clean_work.zip 2132_clean_work