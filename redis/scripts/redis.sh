#!/bin/bash
# redis
version=6.2.10
yum install wget -y
wget https://github.com/redis/redis/archive/$version.tar.gz -O /root/$version.tar.gz
tar zxvf /root/$version.tar.gz -C /opt/
yum install gcc -y
yum install make -y
cd /opt/redis-$version
make distclean
make install
useradd redis
mkdir /etc/redis
mkdir /var/log/redis
mkdir -p /var/lib/redis/redis
mkdir -p /var/lib/redis/sentinel

ports="6380 6381 6382"

for port in $ports

do
	cp /opt/redis-$version/redis.conf /etc/redis/redis.conf_$port
	sed -i 's/^\(bind.*\)$/#\1/' /etc/redis/redis.conf_$port
	sed -i 's/^\(logfile.*\)$/#\1/' /etc/redis/redis.conf_$port
	sed -i 's/^\(dir.*\)$/#\1/' /etc/redis/redis.conf_$port
	sed -i 's/^\(port.*\)$/#\1/' /etc/redis/redis.conf_$port
	echo bind $( ip a|grep 192.168|awk '{print $2}'|awk -F/ '{print $1}') 127.0.0.1 >> /etc/redis/redis.conf_$port
	echo port $port >> /etc/redis/redis.conf_$port
	echo requirepass oMSv8VnCSEjSQcb >> /etc/redis/redis.conf_$port
	echo masterauth oMSv8VnCSEjSQcb >> /etc/redis/redis.conf_$port
	echo logfile "/var/log/redis/redis.log" >> /etc/redis/redis.conf_$port
	echo dir \"/var/lib/redis/redis\" >> /etc/redis/redis.conf_$port
	#echo replicaof 192.168.88.161 6380 >> /etc/redis/redis.conf_6380

	echo supervised systemd >> /etc/redis/redis.conf_$port
	sed -i 's/^\(daemonize.*\)$/#\1/' /etc/redis/redis.conf_$port
	echo daemonize yes >> /etc/redis/redis.conf_$port


	chown -R redis. /etc/redis
	chown -R redis. /var/log/redis
	chown -R redis. /var/lib/redis

	if [ "$port" == "6381" ] || [ "$port" == "6382" ]; then
		echo "replicaof 192.168.88.162 6380" >> "/etc/redis/redis.conf_$port"
	fi

done

