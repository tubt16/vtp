# Streaming Replication (Một tính năng tuyệt vời của Postgres)

PostgreSQL có một tính năng được gọi là Streaming Replication, cung cấp khả năng liên tục gửi và áp dụng các bản ghi XLOG cho một số standby server (máy chủ dự phòng) để cập nhật chúng 

Dưới đây sẽ trình bày một cách rất cơ bản và đơn giản để sao chép máy chủ PostgreSQL (chính) sang máy chủ dự phòng (standby server)

Đầu tiên, tạo người dùng sao chép (Replication user) trong máy chủ PostgreSQL để sử dụng từ máy chủ dự phòng:

```sh
sudo -u postgres createuser --replication -P -e replicator
```

Trong đó:

- `--replication`: Chỉ định `role` mới tạo sẽ được gán quyền sao chép (replication). Quyền này cho phép người dùng sao chép dữ liệu từ máy chủ PostgreSQL sang các máy chủ dự phòng `Standby Server`

- `-P`: Tùy chọn này yêu cầu nhập mật khẩu cho `role` mới tạo

- `-e`: Hiển thị đầu ra về thông tin của `role` sau khi tạo xong

NOTE: Replication user là user có quyền sao chép, cho phép người dùng này sao chép dự liệu từ máy chủ PostgreSQL sang các máy chủ dự phòng khác để đảm tính sẵn sàng cao cho hệ thống

Cấu hình máy chủ PostgreSQL để bật Streaming Replication. Mở tệp `/var/lib/pgsql/15/data/postgresql.conf` và đảm bảo bạn có các dòng sau:

```sh
listen_addresses = '*'
wal_level = replica
```

Đồng thời chỉnh sửa tệp `/var/lib/pgsql/15/pg_hba.conf` để thêm một số dòng bổ sung nhằm cho phép kết nối đến máy chủ dự phòng để sao chép bằng cách sử dụng user `replicator` vừa tạo

```sh
[root@postgres data]# cat /var/lib/pgsql/15/data/pg_hba.conf | grep replicator
host    replication     replicator      34.125.87.127/24        scram-sha-256
```

Khởi động lại dịch vụ để áp dụng các thay đổi

```sh
sudo systemctl restart postgresql-15
```

Stop service PostgreSQL trên standby server

```sh
sudo systemctl stop postgresql
```

Thiết lập cho standby server, Chỉnh sửa file `/var/lib/pgsql/15/data/postgresql.conf` và thêm vào dòng sau

```sh
[root@postgres-standby ~]# cat /var/lib/pgsql/15/data/postgresql.conf | grep "hot_standby"
hot_standby = on                        # "off" disallows queries during recovery
```

Sao lưu toàn bộ config của Standby server

```sh
cp -R /var/lib/pgsql/15/data /var/lib/pgsql/15/data_org
```

Sau khi đã sao lưu toàn bộ cấu hình, ta sẽ xóa toàn bộ tập tin đã được sao lưu trước đó trong `/var/lib/pgsql/15/data`

```sh
rm -rf /var/lib/pgsql/15/data/*
```

Tạo Replication Slots

Ta thực hiện tạo Replication Slots như sau

```sh
SELECT pg_create_physical_replication_slot('standby1');
```

Ta có thể kiểm tra lại Replication Slot đã tạo bằng lệnh sau:

```sh
select * from pg_replication_slots;
```

Và cũng có thể xóa Replication slot bằng lệnh

```sh
mydb=# select pg_drop_replication_slot('standby2');
 pg_drop_replication_slot 
--------------------------
 
(1 row)
```

Thực hiện copy toàn bộ cấu hình từ PostgreSQL server tới Standby server

Syntax:

```sh
pg_basebackup -h <IP address of the main server> -D /var/lib/pgsql/15/data -U replicator -P -v -R -S <replication_slot>
```

Câu lệnh trên sẽ thực hiện sao chép đầy đủ nội dung của cơ sở dữ liệu từ PostgreSQL server vào Standby server

Trong đó:

- `-h`: Tên máy chủ hoặc địa chỉ IP của PostgreSQL server

- `-D`: Thư mục chứa các tệp config

- `-U`: Người dùng được sử dụng để sao chép dữ liệu

- `-P`: Yêu cầu nhập mật khẩu cho role `replicator`

- `-v`: Enable verbose mode

- `-R`: Tạo tệp `standby.signal` và nối thêm cài đặt kết nối vào `postgresql.auto.conf`

- `-S`: Tên của Replication slot

Output:

Trước khi sao chép cơ sở dữ liệu ta cần chuyển đổi người dùng hiện tại sang người dùng `postgres`

```sh
sudo su - postgres
```

```sh
-bash-4.2$ pg_basebackup -h 35.245.178.45 -D /var/lib/pgsql/15/data -U replicator -P -v -R -S standby1
Password: 
pg_basebackup: initiating base backup, waiting for checkpoint to complete
pg_basebackup: checkpoint completed
pg_basebackup: write-ahead log start point: 0/6000060 on timeline 1
pg_basebackup: starting background WAL receiver
pg_basebackup: created temporary replication slot "pg_basebackup_2854"
47364/47364 kB (100%), 1/1 tablespace                                         
pg_basebackup: write-ahead log end point: 0/6000138
pg_basebackup: waiting for background process to finish streaming ...
pg_basebackup: syncing data to disk ...
pg_basebackup: renaming backup_manifest.tmp to backup_manifest
pg_basebackup: base backup completed
```

Cuối cùng hãy khởi động PostgreSQL trên Standby server

```sh
sudo systemctl start postgresql-15
```

List Database trên Standby Server

```sh
[root@postgres-standby data]# sudo -u postgres psql -c "\l"
                                                 List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    | ICU Locale | Locale Provider |   Access privileges   
-----------+----------+----------+-------------+-------------+------------+-----------------+-----------------------
 mydb      | tubt     | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | 
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | =c/postgres          +
           |          |          |             |             |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | =c/postgres          +
           |          |          |             |             |            |                 | postgres=CTc/postgres
 testdb    | tubt     | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | 
 tubt      | tubt     | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | 
(6 rows)
```

Kiểm tra Replica Slot

```sh
mydb=# select * from pg_replication_slots;
 slot_name | plugin | slot_type | datoid | database | temporary | active | active_pid | xmin | catalog_xmin | restart_lsn | confirmed_flush_lsn | wal_status | safe_wal_size | two_phase 
-----------+--------+-----------+--------+----------+-----------+--------+------------+------+--------------+-------------+---------------------+------------+---------------+-----------
 standby1  |        | physical  |        |          | f         | f      |            |      |              | 0/3A0001C0  |            
         | reserved   |               | f
(1 row)
```

Như vậy database trên PostgreSQL server đã được copy sang Standby Server thành công. Để kiểm tra hoạt động của nó hãy chạy lệnh sau trên PostgreSQL server (Server chính)

```sh
[root@postgres data]# sudo -u postgres psql -c "select * from pg_stat_replication;"
 pid  | usesysid |  usename   | application_name |  client_addr  | client_hostname | client_port |         backend_start         | backend_xmin |   state   | sent_lsn  | write_lsn | flush_lsn | replay_lsn | write_lag | flush_lag | replay_lag | sync_priority | sync_state |          reply_time           
------+----------+------------+------------------+---------------+-----------------+-------------+-------------------------------+--------------+-----------+-----------+-----------+-----------+------------+-----------+-----------+------------+---------------+------------+-------------------------------
 3279 |    16630 | replicator | walreceiver      | 34.125.87.127 |                 |       38660 | 2023-10-01 03:21:12.883816+00 |              | streaming | 0/F000060 | 0/F000060 | 0/F000060 | 0/F000060  |         
  |           |            |             0 | async      | 2023-10-01 03:24:34.037146+00
(1 row)
```

Thực hiện tạo mới database trên server chính và kiểm tra xem nó có được sao chép sang Standby server hay không

```sh
CREATE DATABASE infomation;
```

```sh
CREATE TABLE myinfo (
    name VARCHAR(25),
    age INT,
    location VARCHAR(25)
);
```

Insert Table

```sh
INSERT INTO myinfo (name, age, location)
VALUES ('TuBT', '24', 'Dong Anh');
```

Output:

```sh
tubt=# CREATE DATABASE infomation;
CREATE DATABASE

tubt=# \c infomation 
You are now connected to database "infomation" as user "tubt".

infomation=# CREATE TABLE myinfo (
infomation(#     name VARCHAR(25),
infomation(#     age INT,
infomation(#     location VARCHAR(25)
infomation(# );
CREATE TABLE

infomation=# INSERT INTO myinfo (name, age, location)
infomation-# VALUES ('TuBT', '24', 'Dong Anh');
INSERT 0 1

infomation=# SELECT * FROM myinfo;
 name | age | location 
------+-----+----------
 TuBT |  24 | Dong Anh
(1 row)
```

Đứng tại Standby Server kiểm tra DB vừa tạo tại server chính đã được copy sang hay chưa như sau:

```sh
[root@postgres-standby data]# sudo -u postgres psql infomation -c "SELECT * FROM myinfo;"
 name | age | location 
------+-----+----------
 TuBT |  24 | Dong Anh
(1 row)
```

Thực hiện truy vấn và kết quả trả về giống hệt với khi truy vấn tại server chính, vậy luồng `Streaming Relication` của chúng ta đã hoạt động