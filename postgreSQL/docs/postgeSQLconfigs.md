# Configuration File

Trước tiên cùng xem status của PostgreSQL

```sh
[root@postgres var]# systemctl status postgresql-15
● postgresql-15.service - PostgreSQL 15 database server
   Loaded: loaded (/usr/lib/systemd/system/postgresql-15.service; enabled; vendor preset: disabled)
   Active: active (running) since Mon 2023-09-25 08:33:09 UTC; 4 days ago
     Docs: https://www.postgresql.org/docs/15/static/
 Main PID: 4730 (postmaster)
   CGroup: /system.slice/postgresql-15.service
           ├─ 4730 /usr/pgsql-15/bin/postmaster -D /var/lib/pgsql/15/data/
           ├─ 4732 postgres: logger 
           ├─ 4733 postgres: checkpointer 
           ├─ 4734 postgres: background writer 
           ├─ 4736 postgres: walwriter 
           ├─ 4737 postgres: autovacuum launcher 
           ├─ 4738 postgres: logical replication launcher 
           └─23299 postgres: tubt testdb [local] idle

Sep 25 08:33:09 postgres systemd[1]: Starting PostgreSQL 15 database server...
Sep 25 08:33:09 postgres postmaster[4730]: 2023-09-25 08:33:09.344 UTC [4730] LOG:  redirecting l...essSep 25 08:33:09 postgres postmaster[4730]: 2023-09-25 08:33:09.344 UTC [4730] HINT:  Future log o...g".Sep 25 08:33:09 postgres systemd[1]: Started PostgreSQL 15 database server.
Hint: Some lines were ellipsized, use -l to show in full.
```

Từ output trên ta thấy cái file config của PostgreSQL-15 nằm ở `/var/lib/pgsql/15/data`

Liệt kê các file và thư mục trong `/var/lib/pgsql/15/data`

```sh
[root@postgres var]# ls /var/lib/pgsql/15/data
base              pg_dynshmem    pg_notify     pg_stat_tmp  pg_wal                postmaster.pid
current_logfiles  pg_hba.conf    pg_replslot   pg_subtrans  pg_xact
global            pg_ident.conf  pg_serial     pg_tblspc    postgresql.auto.conf
log               pg_logical     pg_snapshots  pg_twophase  postgresql.conf
pg_commit_ts      pg_multixact   pg_stat       PG_VERSION   postmaster.opts
```

Trong đó tệp `postgresql.conf` là tệp chứa các config mặc định của PostgreSQL

# Connection Settings

Theo mặc định máy chủ PostgreSQL chỉ cho phép các kết nối cục bộ

```sh
[root@postgres data]# cat /var/lib/pgsql/15/data/postgresql.conf | grep "listen_addresses"
#listen_addresses = 'localhost'         # what IP address(es) to listen on;
```

Để cho phép tất cả các máy tính khác kết nối với máy chủ PostgreSQL của bạn, hãy chỉnh sửa tệp `postgresql.conf` như sau:

```sh
[root@postgres data]# cat /var/lib/pgsql/15/data/postgresql.conf | grep "listen_addresses"
listen_addresses = '*'          # what IP address(es) to listen on;
```

Tìm đến dòng `listen_addresses = 'localhost` và sửa thành `listen_addresses = '*'`

NOTE: `*` sẽ cho phép tất cả các địa chỉ IP kết nối đến máy chủ PostgreSQL, bạn cũng có thể chỉ định IP cụ thể thay vì để toàn bộ

Sau khi chỉnh sửa cấu hình chúng ta cần restart lại service PostgreSQL để nhận cấu hình mới nhất

```sh
systemctl restart postgresql-15
```

**Thay đổi port cho service postgresql (Mặc định cổng TCP cho dịch vụ PostgreSQL là 5432)**

```sh
[root@postgres data]# cat postgresql.conf | grep "port = 5432"
#port = 5432                            # (change requires restart)
```

**Chỉ định số lượng kết nối đến máy chủ PostgreSQL**

Xác định số lượng kết nối đồng thời tối đa đến PostgreSQL server, mặc định thường là 100 kết nối

```sh
[root@postgres data]# cat postgresql.conf | grep "max_connections"
max_connections = 100                   # (change requires restart)
```

**Còn rất nhiều tham số chúng ta có thể chỉ định trong file `postgresql.conf`, chúng ta hoàn toàn có thể customize được nó**

# File Locations

Ngoài tệp `postgresql.conf` đã được đề cập, PostgreSQL còn sử dụng các tệp cấu hình được chỉnh sửa thủ công khác:

- `pg_hba.conf`: Chỉ định tệp cấu hình để xác thực dựa trên máy chủ

- `pg_ident.conf`: Chỉ định tệp cấu hình để ánh xạ tên người dùng

- `PG_VERSION`: Thông tin phiên bản của PostgreSQL

# Authentication connect DB PostgreSQL

Bây giờ chúng ta có thể kết nối với máy chủ PostgreSQL của mình, bước tiếp theo là đặt mật khẩu cho người dùng postgres. Chạy lệnh sau tại Shell Linux để kết nối với cơ sở dữ liệu `template1` mặc định 

```sh
[root@postgres mnt]# sudo -u postgres psql template1
psql (15.4)
Type "help" for help.

template1=#
```

Lệnh trên kết nối đến database `template1` dưới user `postgres`. Bạn có thể sử dụng lệnh sau để kiểm tra kết nối

```sh
template1=# \conninfo
You are connected to database "template1" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
```

Sau khi kết nối với máy chủ PostgreSQL, bạn có thể chạy lệnh sau tại Shell để định cấu hình mật khẩu cho người dùng `postgres`

```sh
[root@postgres mnt]# sudo -u postgres psql template1 -c "ALTER USER postgres with encrypted password 'tubt160999'"
ALTER ROLE
```

Sau khi đặt mật khẩu, hãy chỉnh sửa tệp `/var/lib/pgsql/15/data/pg_hba.conf` để sử dụng xác thực `scram-sha-256` với người dùng postgres được phép đối với database `template1` từ host chỉ định (Ví dụ 34.162.116.205/24)

Thêm vào file `pg_hba.conf` dòng sau:

```sh
[root@postgres data]# cat pg_hba.conf | grep template1
host template1       all             34.162.116.205/24        scram-sha-256
```

Trong đó:

- `host`: Được sử dụng ở đây chỉ định kết nối TCP 

- `template1`: Chỉ định cơ sở dữ liệu cần xác thực để có thể connect

- `all`: User

- `34.162.116.205/24`: Host

- `scram-sha-256`: Một phương thức xác thực cho mật khẩu, ngoài ra còn có `md5`, `peer` ...

Chúng ta có thể thay trường `host` bằng một trong các giá trị sau:

```sh
# The first field is the connection type:
- "local" is a Unix-domain socket
- "host" is a TCP/IP socket (encrypted or not)
- "hostssl" is a TCP/IP socket that is SSL-encrypted
- "hostnossl" is a TCP/IP socket that is not SSL-encrypted
- "hostgssenc" is a TCP/IP socket that is GSSAPI-encrypted
- "hostnogssenc" is a TCP/IP socket that is not GSSAPI-encrypted
```

Dòng trên chỉ định host có IP 34.162.116.205 cần phải sử dụng phương thức xác thực mật khẩu `scram-sha-256` để kết nối đến db `template1`

Sau khi chỉnh sửa cấu hình chúng ta cần restart lại service PostgreSQL để nhận cấu hình mới nhất

```sh
systemctl restart postgresql-15
```

Sau khi restart postgres service, chúng ta có thể kiểm tra kết nối từ các máy khác bằng cách sử dụng `postgresql-client` như sau:

Đầu tiên trên máy chủ khác, cài `postgresql-client` (Ở đây mình sử dụng máy chủ ubuntu)

```sh
sudo apt install postgresql-client -y
```

Kiểm tra kết nối:

Syntax:

```sh
psql --port 5432 --host <your-servers-dns-or-ip> --username postgres --password --dbname template1
```

Hoặc rút gọn hơn

```sh
psql -p 5432 -h <your-servers-dns-or-ip> -U postgres template1
```

Output:

```sh
root@master:~# psql --host 35.245.178.45 --username postgres --password --dbname template1
Password: 
psql (12.16 (Ubuntu 12.16-0ubuntu0.20.04.1), server 15.4)
WARNING: psql major version 12, server major version 15.
         Some psql features might not work.
Type "help" for help.

template1=#
```

Dấu nhắc trên Shell đã đưa bạn đến db `template1=#`, vậy chúng ta đã từ một server khác (Server cài postgre-client) kết nối đến db `template1` trên máy chủ PostgreSQL thành công

NOTE: Chúng ta nên sử dụng `postgres-client` version cùng với version của PostgreSQL server

