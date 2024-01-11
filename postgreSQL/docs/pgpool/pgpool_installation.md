# PGPool-II + Watchdog Setup Example

Phần này sẽ trình bày việc cấu hình cụm Pgpool với 3 node để quản lý các máy chủ PostgreSQL

PostgreSQL 15 và Pgpool 4.3.0 được sử dụng trong phần này

# Cluster System Configuration

Sử dụng 3 máy chủ cài đặt CentOS 7.9. Đặt tên cho các máy chủ này lần lượt là `server1`, `server2`, `server3` (Thực hiện đặt tên bằng cách trỏ host trong `/etc/hosts`) và cài đặt đồng thời PostgreSQL và Pgpool-II trên mỗi máy chủ

![](/postgreSQL/images/pgpool.png)

## Table 1 - Hostname & IP address

|Hostname|IP Address|Virtual IP|
|---|---|---|
|server1|34.138.227.54|34.138.227.54|
|server2|35.237.152.250|34.138.227.54|
|server3|35.196.222.111|34.138.227.54|

## Table 2 - PostgreSQL version and Configuration

|Item|Value|Detail|
|---|---|---|
|PostgreSQL Version|15.0|-|
|port|5432|-|
|$PGDATA|/var/lib/pgsql/15/data|-|
|Archive mode|on|/var/lib/pgsql/archivedir|
|Replication Slots|Enable|-|

## Table 3 - Pgpool-II version and Configuration

|Item|Value|Detail|
|---|---|---|
|Pgpool-II Version|4.3.0|-|
|port|9999|Pgpool-II port|
|port|9898|PCP port|
|port|9000|WatchDog port|
|port|9694|port UDP nhận tín hiệu của WatchDog heartbeat signal|
|Config file|/etc/pgpool-II/pgpool.conf|Pgpool-II config file|
|Pgpool-II start user|postgres|-|
|Running mode|streaming replication mode|-|
|Watchdog|on|Life check method: heartbeat|

## Table 4 - Sample scripts

|Feature|Script|Detail|
|---|---|---|
|Failover|/etc/pgpool-II/sample_scripts/failover.sh.sample|Chạy bởi `failover_command` để thực hiện chuyển đổi dự phòng|
|Failover|/etc/pgpool-II/sample_scripts/follow_primary.sh.sample|Chạy bởi `follow_primary_command` để đồng bộ hóa node Standby với node Primary sau khi chuyển đổi dự phòng|
|Online Recovery|/etc/pgpool-II/sample_scripts/recovery_1st_stage.sample|Chạy bởi `recovery_1st_stage_command` để khôi phục node dự phòng|
|Online Recovery|/etc/pgpool-II/sample_scripts/pgpool_remote_start.sample|Chạy sau `recovery_1st_stage_command` để start node dự phòng|
|Watchdog|/etc/pgpool-II/sample_scripts/escalation.sh.sample|Chạy sau `wd_escalation_command` để chuyển đổi Active/Standby Pgpool-II một cách an toàn|

**NOTE: Các file scripts trên có sẵn khi cài Pgpool thông qua RPM package và có thể customize khi cần**

# Installation

Trong ví dụ này chúng ta sẽ cài đặt các gói RPM Pgpool-II và PostgreSQL thông qua trình quản lý gói YUM trên CentOS 7

Trước tiên, cài đặt PostgreSQL từ kho lưu trữ PostgreSQL YUM. Thao tác này thực hiện trên toàn bộ 3 node

```sh
[all servers]# yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
[all servers]# yum install -y postgresql15-server
```

Vì các gói liên quan đến PGPool-II cũng được bao gồm trong kho lưu trữ PostgreSQL YUM, chúng ta muốn cài đặt nó riêng biệt, vì thế hãy thêm phần `exclude` vào `/etc/yum.repos.d/pgdg-redhat-all.repo` để PGPool-II không được cài đặt từ kho lưu trữ PostgreSQL YUM. Thao tác này thực hiện trên toàn bộ 3 node

```sh
[all servers]# vi /etc/yum.repos.d/pgdg-redhat-all.repo
```

Thêm đoạn `exclude=pgpool*` vào mỗi phần trong file

```sh
[pgdg-common]
...
exclude=pgpool*

[pgdg15]
...
exclude=pgpool*

[pgdg14]
...
exclude=pgpool*

[pgdg13]
...
exclude=pgpool*

[pgdg12]
...
exclude=pgpool*

[pgdg11]
...
exclude=pgpool*

[pgdg10]
...
exclude=pgpool*
  
```

Cài đặt PGPool-II từ kho lưu trữ PGPool-II YUM

```sh
[all servers]# yum install -y https://www.pgpool.net/yum/rpms/4.4/redhat/rhel-7-x86_64/pgpool-II-release-4.4-1.noarch.rpm
[all servers]# yum install -y pgpool-II-pg15-*
```

<a name="beforestarting"></a>
# Thiết lập ban đầu

Trước khi bắt đầu quá trình cấu hình, vui lòng kiểm tra các điều kiện tiên quyết sau

**Thiết lập PostgreSQL streaming replication trên Primary Server. Trong phần này sẽ sử dụng tính năng lưu trữ WAL**

Đầu tiên chúng ta tạo thư mục `/var/lib/pgsql/archivedir` để lưu trữ các file WAL trên tất cả các máy chủ. Trong phần này chỉ node chính mới lưu trữ các file WAL cục bộ, thực hiện trên toàn bộ 3 node, node nào đóng vài trò là Primary thì node đó sẽ sinh ra các file WAL khi có sự thay đổi trong cơ sở dữ liệu

```sh
[all servers]# su - postgres
[all servers]$ mkdir /var/lib/pgsql/archivedir
```

Khởi tạo PostgreSQL trên Primary Server

```sh
[server1]# su - postgres
[server1]$ /usr/pgsql-15/bin/initdb -D $PGDATA
```

Sau đó chúng ta chỉnh sửa file cấu hình của PostgreSQL (`/var/lib/pgsql/15/data/postgresql.conf`) trên server1 (Primary server) như sau:

```sh
listen_addresses = '*'
archive_mode = on
archive_command = 'cp "%p" "/var/lib/pgsql/archivedir/%f"'
max_wal_senders = 10
max_replication_slots = 10
wal_level = replica
hot_standby = on
wal_log_hints = on
```

**NOTE: Chúng ta sẽ sử dụng chức năng online recovery của PGPool-II để thiết lập các Standby server sau, hiện tại chỉ cần khởi tạo PostgreSQL trên Primary Server**

**Tạo các user `repl` và `pgpool` sử dụng cho mục đích Replication, kiểm tra độ trễ Streaming Replication và Health check tình trạng của PGPool-II**

## Table 5 - Users

|User Name|Password|Detail|
|---|---|---|
|repl|tubt160999|PostgreSQL replication user|
|pgpool|tubt160999|PGPool health check & Replication delay check user|
|postgres|tubt160999|User running online recovery|

Thao tác sau thực hiện trên `server1`

```sh
[server1]# psql -U postgres -p 5432
postgres=# SET password_encryption = 'scram-sha-256';
postgres=# CREATE ROLE pgpool WITH LOGIN;
postgres=# CREATE ROLE repl WITH REPLICATION LOGIN;
postgres=# \password pgpool
postgres=# \password repl
postgres=# \password postgres
GRANT pg_monitor TO pgpool;
```

Chỉnh sửa file `pg_hba.conf` để cho phép cũng như chỉnh sửa phương thức xác thực với các node

```sh
host    all             all             34.138.227.54/24        scram-sha-256
host    all             all             35.237.152.250/24       scram-sha-256
host    all             all             35.196.222.111/24       scram-sha-256

host    replication     all             34.138.227.54/24        scram-sha-256
host    replication     all             35.237.152.250/24       scram-sha-256
host    replication     all             35.196.222.111/24       scram-sha-256
```

**Để sử dụng tính năng Automated Failover và Online Recovery của PGPool-II, bắt buộc phải cho phép SSH public key authentication (Passwordless SSH login) tới tất cả các Backend Server với tư cách là người dùng `postgres` (`postgres` mặc định là người dùng khởi động PGPool và PostgreSQL)**

Đầu tiên, đặt mật khẩu cho người dùng `postgres`

```sh
[all servers]# passwd postgres
```

Thực hiện các lệnh sau trên toàn bộ máy chủ để thiết lập passwordless SSH. Thực hiện trên toàn bộ 3 node

```sh
[all servers]# mkdir ~/.ssh
[all servers]# chmod 700 ~/.ssh
[all servers]# cd ~/.ssh
[all servers]# ssh-keygen -t rsa -f id_rsa_pgpool
[all servers]# ssh-copy-id -i id_rsa_pgpool.pub postgres@server1
[all servers]# ssh-copy-id -i id_rsa_pgpool.pub postgres@server2
[all servers]# ssh-copy-id -i id_rsa_pgpool.pub postgres@server3

[all servers]# su - postgres
[all servers]$ mkdir ~/.ssh
[all servers]$ chmod 700 ~/.ssh
[all servers]$ cd ~/.ssh
[all servers]$ ssh-keygen -t rsa -f id_rsa_pgpool
[all servers]$ ssh-copy-id -i id_rsa_pgpool.pub postgres@server1
[all servers]$ ssh-copy-id -i id_rsa_pgpool.pub postgres@server2
[all servers]$ ssh-copy-id -i id_rsa_pgpool.pub postgres@server3
```

Sau khi cài đặt SSH, hãy đảm bảo rằng bạn có thể chạy lệnh `ssh@postgres[X] -i ~/.ssh/id_rsa pgpool` để đăng nhập mà không cần mật khẩu

**NOTE: Nếu bạn đăng nhập được bằng SSH public key, hãy kiểm tra phần sau:**

- Đảm bảo dòng sau được allow trong `/etc/ssh/sshd_config`

```sh
PubkeyAuthentication yes
...
PasswordAuthentication yes
```

- Nếu SELinux được bật, xác thực SSH thông qua Public key có thể sẽ không thành công, Bạn cần chạy các lệnh sau trên toàn bộ máy chủ

```sh
[all servers]# su - postgres
[all servers]$ restorecon -Rv ~/.ssh
```

**Để cho phép người dùng `repl` không hỏi mật khẩu khi Streaming Replication và Online Recovery chúng ta cần tạo tệp `.pgpass` trong thư mục gốc của người dùng `postgres` và thay đổi permision thành 600 trên toàn bộ máy chủ PostgreSQL**

```sh
[all servers]# su - postgres
[all servers]$ vi /var/lib/pgsql/.pgpass
server1:5432:replication:repl:tubt160999
server2:5432:replication:repl:tubt160999
server3:5432:replication:repl:tubt160999
server1:5432:postgres:postgres:tubt160999
server2:5432:postgres:postgres:tubt160999
server3:5432:postgres:postgres:tubt160999
[all servers]$ chmod 600  /var/lib/pgsql/.pgpass
```

# Đặt ID cho các node trong cụm

Nếu tính năng `watchdog` được enable trong file config, để phân biệt các máy chủ với nhau, ta cần phải có id cho mỗi máy chủ bằng cách thêm vào file `pgpool_node_id`

- Thực hiện trên `server1`

```sh
echo 0 > /etc/pgpool-II/pgpool_node_id
```

- Thực hiện trên `server2`

```sh
echo 1 > /etc/pgpool-II/pgpool_node_id
```

- Thực hiện trên `server3`

```sh
echo 2 > /etc/pgpool-II/pgpool_node_id
```

# PGPool-II Configuration

Chỉnh sửa trên toàn bộ node, chúng ta sẽ đi từng phần sau đó sẽ tổng hợp tất cả các nội dung thành một file `pgpool.conf` hoàn chỉnh và thực hiện trên cả 3 node

### Clustering mode

Trong Pgpool-II có một số chế độ phân cụm, để đặt chế độ phân cụm, ta có thể sử dụng `backend_clustering_mode`. Trong phần này chế độ Streaming Replication được sử dụng:

```sh
backend_clustering_mode = 'streaming_replication'
```

### listen_addresses

Để cho phép PGPool-II chấp nhận tất cả các kết nối đến, chúng ta đặt tham số `listen_addresses = '*'`

```sh
listen_addresses = '*'
```

### Port

Chỉ định port PGPool-II lắng nghe

```sh
port = 9999
```

### Streaming Replication Check

Chỉ định người dùng và mật khẩu để replication delay check trong `sr_check_user` và `sr_check_password`. Chúng ta để trống phần `sr_check_password` và tạo mục chứa password trong `pool_passwd`. Nếu `sr_check_password` được để trống thì trước tiên Pgpool-II sẽ cố gắng lấy mật khẩu cho người dùng cụ thể đó từ tệp `pool_password` (Tệp này chúng ta sẽ tạo ở phần dưới) trước khi sử dụng empty password

```sh
sr_check_user = 'pgpool'
sr_check_password = ''
```

### Health Check

Kích hoạt tính năng health check để PGPool-II thực hiện chuyển đổi dự phòng một cách tự động (Automated Failover), Ngoài ra nếu mạng không ổn định, quá trình health check không thành công ngay các khi các backend server vẫn đang hoạt động bình thường, điều này dẫn đến việc chuyển đổi dự phòng không mong muốn. Đê ngăn chặn tình trạng không chính xác như vậy, chúng ta cần đặt tham số `health_check_max_retries = 3` để chỉ định số lần thử lại trước khi chuyển đổi dự phòng

```sh
health_check_period = 5
health_check_timeout = 30
health_check_user = 'pgpool'
health_check_password = ''
health_check_max_retries = 3
```

### Backend Settings

Chỉ định thông tin cho Backend server PostgreSQL

```sh
# - Backend Connection Settings -

backend_hostname0 = 'server1'
backend_port0 = 5432
backend_weight0 = 1
backend_data_directory0 = '/var/lib/pgsql/15/data'
backend_flag0 = 'ALLOW_TO_FAILOVER'
backend_application_name0 = 'server1'

backend_hostname1 = 'server2'
backend_port1 = 5432
backend_weight1 = 1
backend_data_directory1 = '/var/lib/pgsql/15/data'
backend_flag1 = 'ALLOW_TO_FAILOVER'
backend_application_name0 = 'server2'

backend_hostname2 = 'server3'
backend_port2 = 5432
backend_weight2 = 1
backend_data_directory2 = '/var/lib/pgsql/15/data'
backend_flag2 = 'ALLOW_TO_FAILOVER'
backend_application_name0 = 'server3'
```

### Failover Configuration

Chỉ định tập lệnh `failover.sh` sẽ được thực thi sau khi chuyển đổi dự phòng bằng tham số `failover_command`. Nếu sử dụng 3 máy chủ PostgreSQL, chúng ta cần chỉ định `follow_primary_command` để chạy sau khi chuyển đổi dự phòng

```sh
failover_command = '/etc/pgpool-II/failover.sh %d %h %p %D %m %H %M %P %r %R %N %S'
follow_primary_command = '/etc/pgpool-II/follow_primary.sh %d %h %p %D %m %H %M %P %r %R'
```

Các tập lệnh mẫu `failover.sh` và `follow_primary.sh` được có sẵn trong `/etc/pgpool-II/sample_scripts`. Chúng ta sẽ sử dụng các file scripts này vì thế hãy copy đến nơi chứa file config của `pgpool` để `failover_command` và `follow_primary_command` gọi tới. Thực hiện trên cả 3 node

```sh
[all servers]# cp -p /etc/pgpool-II/sample_scripts/failover.sh.sample /etc/pgpool-II/failover.sh
[all servers]# cp -p /etc/pgpool-II/sample_scripts/follow_primary.sh.sample /etc/pgpool-II/follow_primary.sh
[all servers]# chown postgres:postgres /etc/pgpool-II/{failover.sh,follow_primary.sh}
```

Chúng ta cần phải xác thực người dùng để sử dụng `pcp_command` trong tập lệnh `follow_primary_command` nên chúng ta cần chỉ định tên người dùng và mật khẩu được mã hóa md5 trong `pcp.conf` ở định dạng "username:encrypted password"

Chúng ta sử dụng `pg_md5` để tạo mật khẩu mã hóa cho user `pgpool` và điền vào file `pcp.conf` như sau. Thực hiện trên cả 3 node:

```sh
[all servers]# echo 'pgpool:'`pg_md5 tubt160999` >> /etc/pgpool-II/pcp.conf
```

Vì tập lệnh `follow_primary.sh` phải thực thi pcp command mà không cần nhập mật khẩu, nên chúng ta cần tạo `.pcppass` trong thư mục chính của người dùng khởi động PGPool-II (người dùng `postgres`) trên mỗi máy chủ

```sh
[all servers]# su - postgres
[all servers]$ echo 'localhost:9898:pgpool:tubt160999' > ~/.pcppass
[all servers]$ chmod 600 ~/.pcppass
```

### Pgpool-II Online Recovery Configurations

Tiếp theo, để thực hiện khôi phục trực tuyến (Online recovery) Pgpool-II, chúng ta chỉ định tên người dùng PostgreSQL và lệnh khôi phục trực tuyến `recovery_1st_stage`. Vì đặc quyền Superuser trong PostgreSQL là cần thiết để thực hiện khôi phục trực tuyến nên chúng ta chỉ định người dùng `postgres` trong tham số `recovery_user` (Vì người dùng này có sẵn đặc quyền supperuser). Sau đó chúng ta tạo `recovery_1st_stage` và `pgpool_remote_start` bằng cách lấy từ file `/etc/pgpool-II/sample_scripts` và thêm quyền thực thi

Thêm dòng sau vào file config `pgpool.conf`

```sh
recovery_user = 'postgres'
recovery_password = ''
recovery_1st_stage_command = 'recovery_1st_stage'
```

Các tệp mẫu `recovery_1st_stage` và `pgpool_remote_start` được cài đặt trong `/etc/pgpool-II/sample_scripts`. Sao chép tất cả các tệp này vào thư mục chứa dữ liệu của Pgpool-II trên Primary Server. Thao tác này thực hiện trên `server1`

```sh
[server1]# cp -p /etc/pgpool-II/sample_scripts/recovery_1st_stage.sample /var/lib/pgsql/15/data/recovery_1st_stage
[server1]# cp -p /etc/pgpool-II/sample_scripts/pgpool_remote_start.sample /var/lib/pgsql/15/data/pgpool_remote_start
[server1]# chown postgres:postgres /var/lib/pgsql/15/data/{recovery_1st_stage,pgpool_remote_start}
```

Để sử dụng chức năng khôi phục trực tuyến (Online recovery), cần có các chức năng của `pgpool_recovery`, `pgpool_remote_start`, `pgpool_switch_xlog` và muốn có các chức năng này ta cần phải cài đặt một Extension có tên là `pgpool_recovery` trên Table `template1` của máy chủ PostgreSQL server1

```sh
[server1]# su - postgres
[server1]$ psql template1 -c "CREATE EXTENSION pgpool_recovery"
```

### Client Authentication Configuration

Bởi vì ở phần [Thiết lập ban đầu](#beforestarting). Chúng ta đã đặt phương thức xác thực PostgreSQL thành `scram-sha-256` nên cần phải đặt xác thực Pgpool-II client để kết nối các node Backend. Tệp cấu hình `pool_hba.conf` nằm trong `/etc/pgpool-II/pool_hba.conf`. Theo mặc định, xác thực `pool_hba` bị tắt, hãy bật nó lên bằng cách thêm dòng sau vào file `pgpool.conf`

```sh
enable_pool_hba = on
```

Định dạng của tệp `pool_hba.conf` rất giống định dạng `pg_hba.conf` của PostgreSQL (Đều là định dạng `.ini`). Đặt phương thức xác thực của người dùng `pgpool` và `postgres` thành `scram-sha-256`

```sh
host    all         pgpool      34.138.227.54/24      scram-sha-256
host    all         pgpool      35.237.152.250/24     scram-sha-256
host    all         pgpool      35.196.222.111/24     scram-sha-256

host    all         postgres    34.138.227.54/24      scram-sha-256
host    all         postgres    35.237.152.250/24     scram-sha-256
host    all         postgres    35.196.222.111/24     scram-sha-256
```

Tên tệp mật khẩu mặc định để xác thực là `pool_passwd`. Để sử dụng xác thực `scram-sha-256`, cần có khóa giải mã mật khẩu. Chúng ta cần tạo tệp `.pgpoolkey` trong thư mục chính của người dùng `postgres`. Thực hiện trên toàn bộ 3 node

```sh
[all servers]# su - postgres
[all servers]$ echo 'tubtabxxyz' > ~/.pgpoolkey
[all servers]$ chmod 600 ~/.pgpoolkey
```

Thực hiện lệnh `pg_enc -m -k /path/to/.pgpoolkey -u username -p` để đăng ký tên người dùng và mật khẩu được mã hóa AES trong tệp `pool_passwd`. Nếu `pool_password` chưa tồn tại, nó sẽ được tạo trong cùng thư mục với `pgpool.conf`

```sh
[all servers]# su - postgres
[all servers]$ pg_enc -m -k ~/.pgpoolkey -u pgpool -p
db password: [pgpool user's password]
[all servers]$ pg_enc -m -k ~/.pgpoolkey -u postgres -p
db password: [postgres user's password]

bash-4.2$ cat /etc/pgpool-II/pool_passwd 
pgpool:AES8UyCRLE2L0np3h+th+CtxA==
postgres:AES8UyCRLE2L0np3h+th+CtxA==
```

### Watchdog Configuration

Kích hoạt chức năng giám sát trên `server1`, `server2`, `server3` bằng cách thêm dòng sau vào file `pgpool.conf`

```sh
use_watchdog = on
```

Chỉ định IP ảo chấp nhận tất cả các kết nối từ `server1`, `server2`, `server3`. Ở đây mình sử dụng luôn địa chỉ IP của `server1` làm VIP 

```sh
delegate_ip = '34.138.227.54'
```

Chỉ định tất cả thông tin các node Pgpool-II để định cấu hình Watchdog

```sh
hostname0 = 'server1'
wd_port0 = 9000
pgpool_port0 = 9999

hostname1 = 'server2'
wd_port1 = 9000
pgpool_port1 = 9999

hostname2 = 'server3'
wd_port2 = 9000
pgpool_port2 = 9999
```

Chỉ định phương pháp lifecheck `wd_lifecheck_method` và khoảng thời gian `lifecheck_wd_interval`. Ở đây chúng ta sử dụng method `heartbeat` để thực hiện watchdog lifecheck

```sh
wd_lifecheck_method = 'heartbeat'
wd_interval = 10
```

Chỉ định tất cả thông tin node Pgpool-II để gửi và nhận `heartbeat` signal

```sh
heartbeat_hostname0 = 'server1'
heartbeat_port0 = 9694
heartbeat_device0 = ''
heartbeat_hostname1 = 'server2'
heartbeat_port1 = 9694
heartbeat_device1 = ''
heartbeat_hostname2 = 'server3'
heartbeat_port2 = 9694
heartbeat_device2 = ''
```

Nếu `wd_lifecheck_method` được đặt thành `heartbeat`, hãy chỉ định thời gian đánh dấu node là failed/dead trong tham số `wd_heartbeat_deadtime` và khoảng thời gian gửi `heartbeat` signal trong tham số `wd_heartbeat_keepalive`

```sh
wd_heartbeat_keepalive = 2
wd_heartbeat_deadtime = 30
```

Khi quá trình Watchdog bị chấm dứt một cách bất thường, IP ảo có thể "up" trên các node pgpool hoạt động cũ và mới. Để ngăn chặn điều này hãy định cấu hình `wd_escalation_command` để hạ IP ảo trên các node pgpool khác trước khi hiển thị IP ảo trên các node pgpool đang hoạt động mới

```sh
wd_escalation_command = '/etc/pgpool-II/escalation.sh'
```

Tệp config mẫu `escalation.sh` có sẵn trong file `/etc/pgpool-II/sample_scripts`

```sh
[all servers]# cp -p /etc/pgpool-II/sample_scripts/escalation.sh.sample /etc/pgpool-II/escalation.sh
[all servers]# chown postgres:postgres /etc/pgpool-II/escalation.sh
```

Sau đó sửa tệp `escalation.sh` như sau:

```sh
[all servers]# vi /etc/pgpool-II/escalation.sh
...
PGPOOLS=(34.138.227.54 35.237.152.250 35.196.222.111)

VIP=34.138.227.54
DEVICE=eth0
...
```

**NOTE: Nếu tham số `use_watchdog = on`, ta cần đảm bảo các node được chỉ định ID trong tệp `pgpool_node_id`**

### Logging

Kích hoạt các tham số để cho phép lưu lại log trong quá trình chạy Pgpool-II

```sh
log_destination = 'stderr'
logging_collector = on
log_directory = '/var/log/pgpool_log'
log_filename = 'pgpool-%Y-%m-%d_%H%M%S.log'
log_truncate_on_rotation = on
log_rotation_age = 1d
log_rotation_size = 10MB
```

Tạo các thư mục lưu trữ log trên toàn bộ máy chủ

```sh
[all servers]# mkdir /var/log/pgpool_log/
[all servers]# chown postgres:postgres /var/log/pgpool_log/
```

Tới đây chúng ta đã hoàn tất cấu hình file `pgpool.conf`. Tổng hợp các mục trên lại ta được một file `pgpool.conf` hoàn chỉnh như sau:

```sh
# Pgpool configuration

backend_clustering_mode = 'streaming_replication'

listen_addresses = '*'

port = 9999

# Streaming replication check

sr_check_user = 'pgpool'
sr_check_password = ''

# Health check

health_check_period = 5
health_check_timeout = 30
health_check_user = 'pgpool'
health_check_password = ''
health_check_max_retries = 3

# - Backend Connection Settings -

backend_hostname0 = 'server1'
backend_port0 = 5432
backend_weight0 = 1
backend_data_directory0 = '/var/lib/pgsql/15/data'
backend_flag0 = 'ALLOW_TO_FAILOVER'
backend_application_name0 = 'server1'

backend_hostname1 = 'server2'
backend_port1 = 5432
backend_weight1 = 1
backend_data_directory1 = '/var/lib/pgsql/15/data'
backend_flag1 = 'ALLOW_TO_FAILOVER'
backend_application_name1 = 'server2'

backend_hostname2 = 'server3'
backend_port2 = 5432
backend_weight2 = 1
backend_data_directory2 = '/var/lib/pgsql/15/data'
backend_flag2 = 'ALLOW_TO_FAILOVER'
backend_application_name2 = 'server3'

# Failover config

failover_command = '/etc/pgpool-II/failover.sh %d %h %p %D %m %H %M %P %r %R %N %S'
follow_primary_command = '/etc/pgpool-II/follow_primary.sh %d %h %p %D %m %H %M %P %r %R'

# Recovery config

recovery_user = 'postgres'
recovery_password = ''
recovery_1st_stage_command = 'recovery_1st_stage'

# Authentication config

enable_pool_hba = on

# WatchDog config

use_watchdog = on

delegate_ip = '34.138.227.54'

#if_up_cmd = '/usr/bin/sudo /sbin/ip addr add $_IP_$/24 dev eth0 label eth0:0'
#if_down_cmd = '/usr/bin/sudo /sbin/ip addr del $_IP_$/24 dev eth0'
#arping_cmd = '/usr/bin/sudo /usr/sbin/arping -U $_IP_$ -w 1 -I eth0'
#if_cmd_path = '/sbin'
#arping_path = '/usr/sbin'

hostname0 = 'server1'
wd_port0 = 9000
pgpool_port0 = 9999

hostname1 = 'server2'
wd_port1 = 9000
pgpool_port1 = 9999

hostname2 = 'server3'
wd_port2 = 9000
pgpool_port2 = 9999

wd_lifecheck_method = 'heartbeat'
wd_interval = 10

heartbeat_hostname0 = 'server1'
heartbeat_port0 = 9694
heartbeat_device0 = ''
heartbeat_hostname1 = 'server2'
heartbeat_port1 = 9694
heartbeat_device1 = ''
heartbeat_hostname2 = 'server3'
heartbeat_port2 = 9694
heartbeat_device2 = ''

wd_escalation_command = '/etc/pgpool-II/escalation.sh'

# Logging

log_destination = 'stderr'
logging_collector = on
log_directory = '/var/log/pgpool_log'
log_filename = 'pgpool-%Y-%m-%d_%H%M%S.log'
log_truncate_on_rotation = on
log_rotation_age = 1d
log_rotation_size = 10MB
```

Ta sẽ sử dụng file này trên cả 3 node

# Khởi động lại Service để nhận cấu hình mới

Tiếp theo, chúng ta khởi động Pgpool-II. Trước khi khởi động Pgpool-II, vui lòng khởi động máy chủ PostgreSQL trước. Thực hiện trên toàn bộ 3 node

```sh
# systemctl restart postgresql-15
# systemctl restart pgpool
```

# Setup PostgreSQL standby server

Chúng ta thực hiện thiết lập Standby server PostgreSQL bằng cách sử dụng chức năng Online Recovery Pgpool-II. Cần đảm bảo rằng các tập lệnh `recovery_1st_stage` và `pgpool_remote_start` được lệnh `pcp_recovery_node` sử dụng nằm trong thư mục chứa dữ liệu của PostgreSQL trên Primary Server (server1)

```sh
# pcp_recovery_node -h 34.138.227.54 -p 9898 -U pgpool -n 1
Password:
pcp_recovery_node -- Command Successful

# pcp_recovery_node -h 34.138.227.54 -p 9898 -U pgpool -n 2
Password:
pcp_recovery_node -- Command Successful
```

Sau khi thực thi lệnh `pcp_recovery_node`, hãy xác minh rằng `server2` và `server3` đã được khởi động làm Standby server PostgreSQL bằng lệnh sau:

```sh
# psql -h 34.138.227.54 -p 9999 -U pgpool postgres -c "show pool_nodes"
Password for user pgpool: 
 node_id | hostname | port | status | pg_status | lb_weight |  role   | pg_role | select_cnt | load_balance_node | replication_delay | replication_state | replication_sync_state | last_status_change  
---------+----------+------+--------+-----------+-----------+---------+---------+------------+-------------------+-------------------+-------------------+------------------------+---------------------
 0       | server1  | 5432 | up     | up        | 0.333333  | primary | primary | 0          | false             | 0                 |                   |                        | 2023-10-16 04:08:08
 1       | server2  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | false             | 0                 | streaming         | async                  | 2023-10-16 04:17:00
 2       | server3  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | true              | 0                 | streaming         | async                  | 2023-10-16 04:09:56
(3 rows)
```

# Check Streaming Replication 

Kiểm tra hoạt động bằng cách truy vấn tới Table `pg_stat_replication`

```sh
[root@postgres1 ~]# sudo -u postgres psql tubt -c "SELECT * FROM pg_stat_replication" -x
-[ RECORD 1 ]----+------------------------------
pid              | 9236
usesysid         | 16385
usename          | repl
application_name | server2
client_addr      | 35.237.152.250
client_hostname  | 
client_port      | 34646
backend_start    | 2023-10-17 00:32:39.066122+00
backend_xmin     | 
state            | streaming
sent_lsn         | 0/1B45E3D8
write_lsn        | 0/1B45E3D8
flush_lsn        | 0/1B45E3D8
replay_lsn       | 0/1B45E3D8
write_lag        | 
flush_lag        | 
replay_lag       | 
sync_priority    | 0
sync_state       | async
reply_time       | 2023-10-17 00:57:33.337211+00
-[ RECORD 2 ]----+------------------------------
pid              | 9342
usesysid         | 16385
usename          | repl
application_name | server3
client_addr      | 35.196.222.111
client_hostname  | 
client_port      | 39556
backend_start    | 2023-10-17 00:32:56.069333+00
backend_xmin     | 
state            | streaming
sent_lsn         | 0/1B45E3D8
write_lsn        | 0/1B45E3D8
flush_lsn        | 0/1B45E3D8
replay_lsn       | 0/1B45E3D8
write_lag        | 
flush_lag        | 
replay_lag       | 
sync_priority    | 0
sync_state       | async
reply_time       | 2023-10-17 00:57:33.223074+00
```

Kiểm tra Replication Slot đã được tạo 

```sh
[root@postgres1 ~]# sudo -u postgres psql tubt -c "SELECT * FROM pg_replication_slots"   
 slot_name | plugin | slot_type | datoid | database | temporary | active | active_pid | xmin | catalog_xmin | restart_lsn | confirmed_flush_lsn | wal_status | safe_wal_size | two_phase 
-----------+--------+-----------+--------+----------+-----------+--------+------------+------+--------------+-------------+---------------------+------------+---------------+-----------
 server2   |        | physical  |        |          | f         | t      |       9236 |      |              | 0/1B45E3D8  |                     | reserved   |               | f
 server3   |        | physical  |        |          | f         | t      |       9342 |      |              | 0/1B45E3D8  |                     | reserved   |               | f
```

Để xác minh một lần nữa chúng ta hãy thực hiện kiểm tra quá trình Replication từ server Primary (server1) tới các Standby server (server2 và server3) bằng cách tạo 1 Table đơn giản và INSERT lên Table đó trên Primary Server

Trước tiên chúng ta cần tạo mới database trên Primary Server

```sh
[root@postgres1 ~]# su postgres -c psql

postgres=# CREATE DATABASE tubt;
CREATE DATABASE
```

Sau khi tạo xong, ta cần connect tới database đó để tạo Table và INSERT Table

```sh
postgres=# \c tubt  
You are now connected to database "tubt" as user "postgres".

tubt=# CREATE TABLE myinfo (
tubt(# name varchar(20),
tubt(# age int,
tubt(# locate varchar(20),
tubt(# gender varchar(10)
tubt(# );
CREATE TABLE

tubt=# INSERT INTO myinfo (name, age, locate, gender)
tubt-# VALUES ('TuBT', 24, 'Dong Anh', 'male');
INSERT 0 1

tubt=# SELECT * FROM myinfo;
 name | age |  locate  | gender 
------+-----+----------+--------
 TuBT |  24 | Dong Anh | male
(1 row)
```

Loggin `server2` truy vấn tới Table `myinfo` vừa tạo

```sh
[root@postgres2 ~]# sudo -u postgres psql tubt -c "SELECT * FROM myinfo;"
 name | age |  locate  | gender 
------+-----+----------+--------
 TuBT |  24 | Dong Anh | male
(1 row)
```

Làm tương tự đối với `server3`

```sh
[root@postgres3 ~]# sudo -u postgres psql tubt -c "SELECT * FROM myinfo;"
 name | age |  locate  | gender 
------+-----+----------+--------
 TuBT |  24 | Dong Anh | male
(1 row)
```

# Failover

Trước tiên kiểm tra các node Backend với `psql`

```sh
[root@postgres1 ~]# psql -h 34.138.227.54 -p 9999 -U pgpool postgres -c "show pool_nodes"
Password for user pgpool: 
 node_id | hostname | port | status | pg_status | lb_weight |  role   | pg_role | select_cnt | load_balance_node | replication_delay | replication_state | replication_sync_state | last_status_change  
---------+----------+------+--------+-----------+-----------+---------+---------+------------+-------------------+-------------------+-------------------+------------------------+---------------------
 0       | server1  | 5432 | up     | up        | 0.333333  | primary | primary | 0          | false             | 0                 |                   |                        | 2023-10-16 23:30:26
 1       | server2  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | false             | 0                 | streaming         | async                  | 2023-10-17 00:32:45
 2       | server3  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | true              | 0                 | streaming         | async                  | 2023-10-17 00:33:02
(3 rows)
```

Tiếp theo, Stop Primary PostgreSQL (server1) và xác minh automated failover

```sh
[server1]$ pg_ctl -D /var/lib/pgsql/15/data -m immediate stop
```

Sau khi stop PostgreSQL trên `server1`, qua trình failover xảy ra và PostgreSQL trên `server2` trở thành Primary node

```sh
bash-4.2$ psql -h 34.138.227.54 -p 9999 -U pgpool postgres -c "show pool_nodes"
Password for user pgpool: 
 node_id | hostname | port | status | pg_status | lb_weight |  role   | pg_role | select_cnt | load_balance_node | replication_delay | replication_state | replication_sync_state | last_status_change  
---------+----------+------+--------+-----------+-----------+---------+---------+------------+-------------------+-------------------+-------------------+------------------------+---------------------
 0       | server1  | 5432 | down   | down      | 0.333333  | standby | unknown | 0          | false             | 0                 |                   |                        | 2023-10-17 01:14:35
 1       | server2  | 5432 | up     | up        | 0.333333  | primary | primary | 0          | true              | 0                 |                   |                        | 2023-10-17 01:14:35
 2       | server3  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | false             | 0                 | streaming         | async                  | 2023-10-17 01:14:58
(3 rows)
```

# Online Recovery

Ở đây chúng ta sử dụng chức năng Online Recovery Pgpool-II để khôi phục `server1` (Primary server cũ) làm Standby server. Trước khi khôi phục `server1`, cần đảm bảo rằng các tệp lệnh `recovery_1st_stage` và `pgpool_remote_start` tồn tại trong thư mục chứa các file config PostgreSQL trong Primary server hiện tại (`server2`)

```sh
[root@postgres2 ~]# pcp_recovery_node -h localhost -p 9898 -U pgpool -n 0
Password: 
pcp_recovery_node -- Command Successful
```

Sau đó kiểm tra để xác minh rằng `server1` hiện tại được chạy với tư cách là Standby server

```sh
[root@postgres2 ~]# psql -h 34.138.227.54 -p 9999 -U pgpool postgres -c "show pool_nodes"
Password for user pgpool: 
 node_id | hostname | port | status | pg_status | lb_weight |  role   | pg_role | select_cnt | load_balance_node | replication_delay | replication_state | replication_sync_state | last_status_change  
---------+----------+------+--------+-----------+-----------+---------+---------+------------+-------------------+-------------------+-------------------+------------------------+---------------------
 0       | server1  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | true              | 0                 | streaming         | async                  | 2023-10-17 01:22:02
 1       | server2  | 5432 | up     | up        | 0.333333  | primary | primary | 2          | false             | 0                 |                   |                        | 2023-10-17 01:14:35
 2       | server3  | 5432 | up     | up        | 0.333333  | standby | standby | 1          | false             | 0                 | streaming         | async                  | 2023-10-17 01:14:58
(3 rows)
```




> Tham khảo: https://www.pgpool.net/docs/44/en/html/example-cluster.html