# Failover & Failback

Failover có nghĩa là tự động detach node PostgreSQL backend mà Pgpool-II không thể truy cập được. Điều này xảy ra tự động

Quá trình failover, Pgpool-II xác nhận tính không thể truy cập của node backend PostgreSQL bằng cách sử dụng phương pháp health check, quá trình health check cố gắng kết nối từ node Pgpool-II đến node PostgreSQL để xác nhận tình trạng hoạt động của nó. Nếu không kết nối được có nghĩa là node PostgreSQL không khả dụng

Nếu `failover_command` được cấu hình và chuyển đổi dự phòng xảy ra thì `failover_command` sẽ được thực thi. `failover_command` do người dùng tự cung cấp

Vai trò chính của `failover_command` là chọn Primary server mới từ các Standby server và promote nó lên làm Primary server

# Failover & failback settings 

`failover_command` (string)

Trong Pgpool-II, Failover là quá trình tự động chuyển đổi các yêu cầu từ node Primary đang gặp sự cố sang một node khác trong cụm. Khi node Primary không khả dụng, Pgpool-II tự động chuyển hướng yêu cầu đến một node mới khác để duy trì tính khả dụng của hệ thống. Quá trình này xảy ra một cách tự động và không làm gián đoạn hoạt động của ứng dụng

Chỉ định lệnh sẽ chạy khi node PostgreSQL bị detach. Pgpool-II thay thế các ký tự sau bằng thông tin của thể về backend server

**Failover command options**

|Special character|Description|
|---|---|
|%d|ID của node backend bị detach|
|%h|Hostname của node bị detach|
|%p|Port của node bị detach
|%D|Thư mục chứa cơ sở dữ liệu của node bị detach|
|%m|ID của Node Primary mới|
|%H|Hostname của node Primaru mới|
|%M|ID của node Primary cũ|
|%P|ID của node Primary cũ|
|%r|Port của node Primary mới|
|%R|Thư mục chứa cơ sở dữ liệu của node Primary mới|
|%N|Hostname của node Primary cũ|
|%S|Port của node Primary cũ|

`failback_command` (string)

Trong Pgpool-II, Failback là quá trình khôi phục lại node chính sau khi node chính đã hoạt động bình thường trở lại, Pgpool-II sẽ thực hiện quá trình failback để đưa node chính trở lại vị trí ban đầu của nó trong cụm. Quá trình failback đảm bảo rằng node chính được sử dụng lại và hoạt động như trước khi gặp phải sự cố

Chỉ định lệnh sẽ chạy khi attach node PostgreSQL vào cụm Pgpool-II. PGpool-II thay thế các ký tự đặc biệt sau bằng thông tin cụ thể về backend server

**Failback command options**

|Special character|Description|
|---|---|
|%d|ID của node cần attach|
|%h|Hostname của node cần attach|
|%p|Port của node cần attach|
|%D|Thư mục chứa cơ sở dữ liệu của node cần attach|
|%m|ID của node Primary mới|
|%H|Hostname của node Primary mới|
|%M|ID của node Primary cũ|
|%P|ID của node Primary cũ|
|%r|Port của node Primary mới|
|%R|Thư mục chứa cơ sở dữ liệu của node Primary mới|
|%N|Hostname của node Primary cũ|
|%S|Port của node Primary cũ|

`follow_primary_command` (string)

Chỉ định một lệnh người dùng sẽ chạy sau khi chuyển đổi dự phòng trên node Primary

**Follow primary command options**

|Special character|Description|
|---|---|
|%d|ID của node đã bị detach|
|%h|Hostname của node bị detach|
|%p|Port của node bị detach|
|%D|Thư mục chứa cơ sở dữ liệu của node bị detach|
|%m|ID node Primary mới|
|%H|Hostname của node Primary mới|
|%M|ID của node Primary cũ|
|%P|ID của node Primary cũ|
|%r|Port của node Primary mới|
|%R|Thư mục chứa cơ sở dữ liệu của node Primary mới|
|%N|Hostname của node Primary cũ|
|%S|Port của node Primary cũ|

Thông thường lệnh `follow_primary_command` được sử dụng để khôi phục Standby node từ Primary node bằng cách gọi lệnh `pcp_recovery_node`.

`auto_failback` (boolean)

Khi tham số `auto_failback = on`, Pgpool-II sẽ tự động thực hiện quá trình failback một cách tự động sau khi node chính đã được khôi phục, có nghĩa là Pgpool-II sẽ tự động chuyển lại các yêu cầu từ node mới sang node Primary khi node Primary đã sẵn sàng và hoạt động bình thường.

Nếu bạn không muốn Pgpool-II thực hiện tự động failback, bạn có thể đặt lại `auto_failback = off`, Khi đó Pgpool-II sẽ không tự động thực hiện quá trình failback và yêu cầu sẽ được chuyển đến node Primary hiện tại cho đến khi bạn thực hiện failback thủ công

`auto_failback_interval` (integer)

Chỉ định khoảng thời gian giữa các lần kiểm tra `auto_failback`, khi `auto_failback_interval` được đặt, Pgpool-II sẽ kiểm tra xem node Primary đã được khôi phục chưa sau mỗi khoảng thời gian được xác định bởi `auto_failback_interval`


# Demo failover

Trước tiên kiểm tra các node backend trong cụm Pgpool-II

```sh
[root@postgres2 ~]# psql -h localhost -p 9999 -U pgpool postgres -c "show pool_nodes"
 node_id | hostname | port | status | pg_status | lb_weight |  role   | pg_role | select_cnt | load_balance_node | replication_delay | replication_state | replication_sync_state | last_status_change  
---------+----------+------+--------+-----------+-----------+---------+---------+------------+-------------------+-------------------+-------------------+------------------------+---------------------
 0       | server1  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | true              | 0                 | streaming         | async                  | 2023-10-18 05:40:22
 1       | server2  | 5432 | up     | up        | 0.333333  | primary | primary | 0          | false             | 0                 |                   |                        | 2023-10-18 05:40:22
 2       | server3  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | false             | 0                 | streaming         | async                  | 2023-10-18 05:40:22
(3 rows)
```

Hiện tại `server2` đang đóng vai trò là Primary server

Tiếp theo, Stop service PostgreSQL trên `server2` và xác minh automated failover

```sh
[root@postgres2 ~]# su postgres

bash-4.2$ /usr/pgsql-15/bin/pg_ctl -D /var/lib/pgsql/15/data/ stop
waiting for server to shut down.... done
server stopped
```

Sau khi stop PostgreSQL trên `server2`, quá trình failover xảy ra và PostgreSQL trên `server1` trở thành Primary node, sở dĩ `server1` trở thành Primary node vì ID của `server1` đang là thấp nhất (ID = 0)

```sh
bash-4.2$ psql -h localhost -p 9999 -U pgpool postgres -c "show pool_nodes"
 node_id | hostname | port | status | pg_status | lb_weight |  role   | pg_role | select_cnt | load_balance_node | replication_delay | replication_state | replication_sync_state | last_status_change  
---------+----------+------+--------+-----------+-----------+---------+---------+------------+-------------------+-------------------+-------------------+------------------------+---------------------
 0       | server1  | 5432 | up     | up        | 0.333333  | primary | primary | 0          | true              | 0                 |                   |                        | 2023-10-18 06:41:39
 1       | server2  | 5432 | down   | down      | 0.333333  | standby | unknown | 0          | false             | 0                 |                   |                        | 2023-10-18 06:39:59
 2       | server3  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | false             | 0                 | streaming         | async                  | 2023-10-18 06:41:39
(3 rows)
```

Sau khi stop service status chuyển về down, ta cần chạy lệnh sau để join node vào cụm

```sh
[root@postgres1 ~]# pcp_recovery_node -h localhost -p 9898 -U pgpool -n 1
Password: 
pcp_recovery_node -- Command Successful
```

Kết quả `server1` đã trở thành Primary server sau khi stop service PostgreSQL trên `server2`, vậy quá trình failover đã hoạt động trên cụm:

```sh
[root@postgres1 ~]# psql -h localhost -p 9999 -U pgpool postgres -c "show pool_nodes"
 node_id | hostname | port | status | pg_status | lb_weight |  role   | pg_role | select_cnt | load_balance_node | replication_delay | replication_state | replication_sync_state | last_status_change  
---------+----------+------+--------+-----------+-----------+---------+---------+------------+-------------------+-------------------+-------------------+------------------------+---------------------
 0       | server1  | 5432 | up     | up        | 0.333333  | primary | primary | 0          | true              | 0                 |                   |                        | 2023-10-18 06:39:59
 1       | server2  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | false             | 0                 | streaming         | async                  | 2023-10-18 06:43:06
 2       | server3  | 5432 | up     | up        | 0.333333  | standby | standby | 0          | false             | 0                 | streaming         | async                  | 2023-10-18 06:43:06
(3 rows)
```

Xem bài viết [sau](./pgpool_installation.md) để cài đặt cụm Pgpool với 3 server như trên

> Tham khảo: https://www.pgpool.net/docs/44/en/html/runtime-config-failover.html