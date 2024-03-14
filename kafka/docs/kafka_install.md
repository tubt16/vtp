# Install Kafka Cluster on CentOS 7

Thực hiện cài trên 3 node 10.206.0.9, 10.206.0.8, 10.206.0.10

Mô hình

|ID|Node|OS|
|---|---|---|
|1|10.206.0.9|CentOS 7|
|2|10.206.0.8|CentOS 7|
|3|10.206.0.10|CentOS 7|

Bước 1: Update OS Packages

```sh
yum clean all
yum update
```

Bước 2: Install Java

Apache kafka yêu cầu môi trường Java, vì vậy để chạy được Kafka trên máy chủ thì trước tiên ta cần cài đặt Java

Cài đặt Java như sau

```sh
yum install java-1.8.0-openjdk.x86_64
```

Check version Java

```sh
java -version

[root@kafka1 ~]# java -version
openjdk version "1.8.0_382"
OpenJDK Runtime Environment (build 1.8.0_382-b05)
OpenJDK 64-Bit Server VM (build 25.382-b05, mixed mode)
```

Thêm các biến môi trường `JAVA_HOME` và `JRE_HOME` vào cuối tệp `/etc/bashrc`

```sh
sudo vi /etc/bashrc
```

Thêm các dòng sau vào cuối file

```sh
export JRE_HOME=/usr/lib/jvm/jre
export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk
PATH=$PATH:$JRE_HOME:$JAVA_HOME
```

Chạy lệnh sau để export biến

```sh
source /etc/bashrc
```

Bước 3: Install Apache Kafka

Tạo user Kafka

```sh
useradd kafka
```

Tải xuống phiên bản Kafka 3.6.1 từ trang chủ và giải nén

```sh
cd ~
wget https://archive.apache.org/dist/kafka/3.6.1/kafka_2.12-3.6.1.tgz
tar xzf kafka_2.12-3.6.1.tgz
```

Tạo thư mục lưu trữ source Kafka và di chuyển source đã tải về vao thư mục vừa tạo

```sh
mkdir -p /opt/kafka
mv kafka_2.12-3.6.1/* /opt/kafka
```

Tạo thư mục cho log message Kafka và snapshot cho Zookeeper

```sh
mkdir -p /data/kafka

mkdir -p /data/zookeeper
```

Tạo tệp `myid` trong `/data/zookeeper` và điền node id tương đương với các node trong cụm

```sh
cd /data/zookeeper
echo 1 > myid
```

Đối với các node 2 và node 3

```sh
echo 2 > myid
echo 3 > myid
```

Sửa config của Kafka (file `server.properties`) trên node 1

```sh
mv /opt/kafka/config/server.properties /opt/kafka/config/server.properties.old

vi /opt/kafka/config/server.properties

broker.id=1
advertised.listeners=PLAINTEXT://10.206.0.9:9092
delete.topic.enable=true
log.dirs=/data/kafka
num.partitions=8
default.replication.factor=3
min.insync.replicas=2
log.retention.hours=168
log.segment.bytes=1073741824
log.retention.check.interval.ms=300000
zookeeper.connect=10.206.0.9:2181,10.206.0.8:2181,10.206.0.10:2181
zookeeper.connection.timeout.ms=6000
auto.create.topics.enable=true
```

Làm tương tự với node 2 và node 3, lưu ý sửa `broker.id` và `advertised.listeners` phù hợp với từng node

Sửa config của Zookeeper (file `zookeeper.properties`) trên toàn bộ các node

```sh
mv /opt/kafka/config/zookeeper.properties /opt/kafka/config/zookeeper.properties.old
vi /opt/kafka/config/zookeeper.properties

# the directory where the snapshot is stored.
dataDir=/data/zookeeper
# the port at which the clients will connect
clientPort=2181
# setting number of connections to unlimited
maxClientCnxns=0
# keeps a heartbeat of zookeeper in milliseconds
tickTime=2000
# time for initial synchronization
initLimit=10
# how many ticks can pass before timeout
syncLimit=5
# define servers ip and internal ports to zookeeper
server.1=10.206.0.9:2888:3888
server.2=10.206.0.8:2888:3888
server.3=10.206.0.10:2888:3888
```

Tạo tệp `zookeeper.service` trong systemd để chạy Zookeeper dưới dạng service (Thực hiện trên cả 3 node)

```sh
vi /etc/systemd/system/zookeeper.service

[Unit]
Description=Apache Zookeeper server (Kafka)
Documentation=http://zookeeper.apache.org
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
User=kafka
Group=kafka
Environment=JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk
ExecStart=/opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties
ExecStop=/opt/kafka/bin/zookeeper-server-stop.sh

[Install]
WantedBy=multi-user.target
```

Tạo tệp `kafka.service` trong systemd để chạy Kafka dưới dạng service (Thực hiện trên cả 3 node)

```sh
vi /etc/systemd/system/kafka.service

[Unit]
Description=Apache Kafka server (broker)
Documentation=http://kafka.apache.org/documentation.html
Requires=network.target remote-fs.target
After=network.target remote-fs.target kafka-zookeeper.service

[Service]
Type=simple
User=kafka
Group=kafka
Environment=JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk
ExecStart=/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties
ExecStop=/opt/kafka/bin/kafka-server-stop.sh

[Install]
WantedBy=multi-user.target
```

Sau khi thực hiện tạo các file trong systemd, ta cần chạy lệnh sau để các file mới tạo có hiệu lực

```sh
systemctl daemon-reload
```

Phân quyền lại cho Source Kafka để chạy service với User `kafka`

```sh
chown -R kafka. /opt/kafka
chown -R kafka. /data
```

Khi đã xong, hãy khởi động dịch vụ trên toằn bộ node

```sh
systemctl start kafka
systemctl start zookeeper
```

# Kiểm tra Cluster hoạt động

Đứng tại node 1 chạy lệnh sau trên shell và chạy câu lệnh `create /tubt "test"`

```sh
[root@kafka1 opt]# /opt/kafka/bin/zookeeper-shell.sh 10.206.0.9
Connecting to 10.206.0.9
Welcome to ZooKeeper!
JLine support is disabled

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
ls /
[cluster, controller_epoch, controller, brokers, zookeeper, admin, isr_change_notification, consumers, log_dir_event_notification, latest_producer_id_block, config]
create /tubt "test"
Created /tubt
```

Sau đó Ctrl + C để thoát và connect đến các node 2 và 3 để kiểm tra xem folder đã được tạo chưa

```sh
[root@kafka1 opt]# /opt/kafka/bin/zookeeper-shell.sh 10.206.0.8
Connecting to 10.206.0.8
Welcome to ZooKeeper!
JLine support is disabled

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
ls /
[cluster, controller_epoch, controller, brokers, zookeeper, tubt, admin, isr_change_notification, consumers, log_dir_event_notification, latest_producer_id_block, config]


[root@kafka1 opt]# /opt/kafka/bin/zookeeper-shell.sh 10.206.0.10
Connecting to 10.206.0.10
Welcome to ZooKeeper!
JLine support is disabled

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
ls /
[cluster, controller_epoch, controller, brokers, zookeeper, tubt, admin, isr_change_notification, consumers, log_dir_event_notification, latest_producer_id_block, config]
```

Sau khi connect đến node 2 và 3 ta kiểm tra thấy folder `tubt` đã được tạo, vậy cluster đã hoạt động