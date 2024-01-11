#!/bin/bash
# sentinel
ports="6380 6381 6382"

for port in $ports
do
	
	cat << EOF > /etc/redis/sentinel.conf_$port
port 2$port
daemonize yes				
logfile "/var/log/redis/sentinel.log"
dir "/var/lib/redis"
sentinel monitor mymaster 192.168.88.162 6380 2
sentinel down-after-milliseconds mymaster 10000
sentinel failover-timeout mymaster 20000
sentinel auth-pass mymaster oMSv8VnCSEjSQcb
sentinel parallel-syncs mymaster 1
EOF

chown -R redis. /etc/redis

cat << EOF > /etc/systemd/system/redis-sentinel_$port.service
[Unit]
Description=Advanced key-value store
After=network.target
Documentation=http://redis.io/documentation, man:redis-sentinel_$port(1)

[Service]
Type=forking
ExecStart=/usr/local/bin/redis-sentinel /etc/redis/sentinel.conf_$port
ExecStop=/bin/kill -s TERM $MAINPID
#PIDFile=/run/redis-sentinel_$port.pid
TimeoutStopSec=0
Restart=always
User=redis
Group=redis
RuntimeDirectory=sentinel
RuntimeDirectoryMode=2755

UMask=007
PrivateTmp=yes
LimitNOFILE=65535
PrivateDevices=yes
ProtectHome=yes
ReadOnlyDirectories=/
ReadWriteDirectories=-/var/lib/redis/sentinel_$port
ReadWriteDirectories=-/var/log/redis
ReadWriteDirectories=-/run/sentinel_$port

NoNewPrivileges=true
CapabilityBoundingSet=CAP_SETGID CAP_SETUID CAP_SYS_RESOURCE
RestrictAddressFamilies=AF_INET AF_INET6 AF_UNIX

ProtectSystem=true
ReadWriteDirectories=-/etc/redis

[Install]
WantedBy=multi-user.target
Alias=sentinel_$port.service
EOF


cat << EOF > /etc/systemd/system/redis_$port.service
[Unit]
Description=Redis persistent key-value database
After=network.target
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf_$port --supervised systemd
#ExecStop=/usr/libexec/redis_$port-shutdown
ExecStop=/usr/local/bin/redis-cli -h localhost -p $port SHUTDOWN
Type=forking
User=redis
LimitNOFILE=65536
Group=redis
RuntimeDirectory=redis
RuntimeDirectoryMode=0755

[Install]
WantedBy=multi-user.target
EOF

systemctl enable redis_$port
systemctl enable redis-sentinel_$port
systemctl start redis_$port
systemctl start redis-sentinel_$port
systemctl status redis_$port
systemctl status redis-sentinel_$port

done