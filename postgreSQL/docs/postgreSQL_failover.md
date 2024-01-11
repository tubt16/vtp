# Thủ tục Failover Streaming Replication trên PostgreSQL

## Failover

Đây là tình huống khi database Master găp phải trục trặc, không thể hoạt động tiếp được. Chúng ta cần phải kích hoạt database Slave (dự phòng) lên thành database master mới

**1. Mô hình**

|Role|IP|OS|PosgreSQL version|
|---|---|---|---|
|Master|34.106.45.98|CentOS 7|version 13|
|Slave|34.106.29.46|CentOS 7|version 13|

**2. Quy trình Failover**

- Bài toán: Giả sử server Master bị trực trặc và hiện không thể khởi động lên được. Như chúng ta được biết server Slave giống hệt như server Master, tuy nhiên Slave chỉ cho phép đọc dữ liệu thôi, không ghi được. Ta cần phải cấu hình sao cho server Slave có thể đọc/ghi dữ liệu được, để cho ứng dụng kết nối vào Slave thay thế cho Master

**3. Thực hiện trên Master**

Để thực hiện bài toán trên ta cần phải stop service Postgresql trên Master đi

```sh
[root@postgresql13 data]# sudo -u postgres /usr/pgsql-13/bin/pg_ctl stop -D /var/lib/pgsql/13/data/
waiting for server to shut down.... done
server stopped
```

hoặc

```sh
systemctl stop postgresql-13
```

**4. Thực hiện trên Slave**

Đầu tiên ta thử tạo một cột trên Table để kiểm tra xem Slave có đúng là đang ở chế độ `read only` hay không

```sh
information=# SELECT * FROM myinfo;
 name | age | location | color | gender
------+-----+----------+-------+--------
 TuBT |  24 | Dong Anh | red   |
(1 row)

information=# ALTER TABLE myinfo ADD test INT;
ERROR:  cannot execute ALTER TABLE in a read-only transaction
```

Kết quả trả về thông báo rằng lệnh trên không thể thực hiện do Slave đang ở chế độ `read-only`

Thực hiện promote Slave server thành Master

```sh
[root@standby-postgres13 mnt]# sudo -u postgres /usr/pgsql-13/bin/pg_ctl promote -D /var/lib/pgsql/13/data/
waiting for server to promote.... done
server promoted
```

Hoặc 

```sh
SELECT pg_promote();
```

Kiểm tra lại log sau khi thực hiện lệnh trên

```sh
2023-10-03 15:38:36.670 UTC [1819] LOG:  received promote request
2023-10-03 15:38:36.670 UTC [1819] LOG:  redo done at 0/5000060
2023-10-03 15:38:36.674 UTC [1819] LOG:  selected new timeline ID: 2
2023-10-03 15:38:36.944 UTC [1819] LOG:  archive recovery complete
2023-10-03 15:38:36.957 UTC [1816] LOG:  database system is ready to accept connections
```

**5. Kiểm tra lại bằng cách UPDATE Table**

```sh
information=# SELECT * FROM myinfo;
 name | age | location | color | gender
------+-----+----------+-------+--------
 TuBT |  24 | Dong Anh | red   |
(1 row)
```

Thực hiện UPDATE cột `gender` của Table `myinfo`

```sh
information=# UPDATE myinfo SET gender = 'male' WHERE name = 'TuBT';
UPDATE 1
information=# SELECT * FROM myinfo;
 name | age | location | color | gender
------+-----+----------+-------+--------
 TuBT |  24 | Dong Anh | red   | male
(1 row)
```

Vậy là Server Slave đã có thể đọc-ghi bình thường