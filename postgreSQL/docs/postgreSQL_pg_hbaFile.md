# Cấu hình kết nối trong PostgreSQL với `pg_hba.conf`

## Giới thiệu

Khi một máy khách (client) cố gắng két nối với PostgreSQL database cluster, đầu tiên nó phải qua được lớp xác thực ở mức hệ điều hành được cấu hình trong file `pg_hba.conf`. Các chính sách sẽ dựa trên các thông tin IP máy khách, tên người dùng database để quyết định xem có được đi tiếp hay không. 

File `pg_hba.conf` thường được lưu trữ trong cùng thư mục với `postgresql.conf`. Hoặc đường dẫn của nó có thể được tùy chỉnh bởi tham số `hba_file`

```sh
postgres=# show hba_file;
              hba_file              
------------------------------------
 /var/lib/pgsql/15/data/pg_hba.conf
(1 row)
```

## Cấu trúc của file `pg_hba.conf`

Đây là nội dung của 1 file `pg_hba.conf` tiêu chuẩn

```sh
# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     peer
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     peer
host    replication     all             127.0.0.1/32            scram-sha-256
host    replication     all             ::1/128                 scram-sha-256
host    template1       all             34.162.116.205/24       md5
host    replication     replicator      34.125.87.127/24        scram-sha-256
host    all             postgres        34.106.45.98/24         md5
```

## Ý nghĩa

- Cột `TYPE` có thể có các giá trị:

	+ `local`: Chỉ cho phép kết nối từ localhost vào database

	+ `host`: Cho phép tất cả các kết nối kể cả mã hóa hay không mã hóa

	+ `hostssl`: Chỉ cho phép kết nối có mã hóa SSL

	+ `hostnossql`: Chỉ cho phép kết nối không có mã hóa SSL

- Cột `DATABASE`: Chỉ ra database được phép kết nối trong chính sách

- Cột `USER`: Chỉ ra database user dược phép kết nối

- Cột `ADDRESS`: Chỉ ra dải IP được phép kết nối. Chú ý, giá trị của cột này là 1 dải mạng, do đó bạn cần phải chỉ ra cả subnet mask

- Cột `METHOD` Chỉ ra phương thức được sử dụng

	+ `trust`: Cho phép kết nối mà không yêu cầu thông tin xác thực

	+ `peer`: Cho phép kết nối nếu OS user máy khách trùng tên với Database user. Được dùng khi kết nối với database từ localhost

	+ `ident`: Tượng tự như `peer` nhưng nó hỗ trợ các kết nối từ bên ngoài

	+ `password`: Yêu cầu tên đăng nhập và mật khẩu. Tuy nhiên mật khẩu sẽ không được mã hóa khi truyền từ máy khách đến database server

	+ `md5`: Giống với password, tuy nhiên mật khẩu sẽ được mã hóa với thuật toán `md5`

	+ `scram-sha-256`: Giống với password, tuy nhiên mật khẩu sẽ được mã hóa với thuật toán `scram-sha-256`

## Hoạt động

Khi có 1 yêu cầu kết nối từ máy khách, PostgreSQL sẽ lấy thông tin máy khách này và đọc file `pg_hba.conf` từ trên xuống dưới

Nếu thông tin máy khách phù hợp với chính sách được quy định, kết nối sẽ được thiết lập. Ngược lại nếu không có chính sách nào phù hợp thì yêu cầu sẽ bị từ chối

Ví dụ, một dòng trong file `pg_hba.conf` như sau:

```sh
# TYPE  DATABASE        USER            ADDRESS                 METHOD
host    all             postgres        34.106.45.98/24         md5
```

Có nghĩa là: Máy khách có IP 34.106.45.98 có thể kết nối vào toàn bộ database (DATABASE=all), bằng user postgres (USER=postgres), sử dụng phương thức xác thực là nhập password (METHOD=md5)

Sau khi yêu cầu kết nối đã qua được chính sách của `pg_hba.conf`, tiến trình master của PostgreSQL sẽ tạo ra 1 tiến trình con và cho phép nó sử dụng shared buffer. Một kết nối được thiết lập

## Kết nối

Sau khi thêm cấu hình trong `pg_hba.conf` ta có thể kiểm tra kết nối từ máy khác 

Đầu tiên trên máy chủ khác cần cài `postgreSQL-client`

```sh
apt-get install postgresql-client -y
```

Kiểm tra kết nối

**Syntax:**

```sh
psql --port 5432 --host <your-servers-dns-or-ip> --username <user_name> --password --dbname <db_name>
```

hoặc

```sh
psql -p 5432 -h <your-servers-dns-or-ip> -U <user_name> <db_name>
```

**Output:**

```sh
root@test:~# psql -p 5432 -h 35.245.178.45 -U postgres information
Password for user postgres:
psql (12.16 (Ubuntu 12.16-0ubuntu0.20.04.1), server 15.4)
WARNING: psql major version 12, server major version 15.
         Some psql features might not work.
Type "help" for help.

information=# \dt
        List of relations
 Schema |  Name  | Type  | Owner
--------+--------+-------+-------
 public | myinfo | table | tubt
(1 row)

information=# SELECT * FROM myinfo;
 name | age | location
------+-----+----------
 TuBT |  24 | Dong Anh
(1 row)
```

NOTE: Chúng ta nên sử dụng PostgreSQL server với PostgreSQL client cùng phiên bản, ở đây 2 version của mình không giống nhau nên mới có dòng WARNING trên