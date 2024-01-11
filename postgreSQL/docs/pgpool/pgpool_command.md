# Các lệnh PGPool-II

# PGPOOL SHOW

`PGPOOL SHOW` - Hiển thị giá trị của các tham số trong file config `/pgpool.conf`. Lệnh này tương tự như lệnh `SHOW` trong PostgreSQL với việc bổ sung từ khóa `PGPOOL` để phân biệt với lệnh SHOW của PostgreSQL

## Syntax

```sh
PGPOOL SHOW <configuration_parameter>
PGPOOL SHOW <configuration_parameter_group>
PGPOOL SHOW ALL
```

## Ví dụ

**Hiển thị port PGPool**

```sh
root@postgres-client:/proc# psql -h pgpool2 -U tubt -p 9990 information -c "PGPOOL SHOW port;"
Password for user tubt: 
 port 
------
 9990
(1 row)
```

**Hiển thị các tham số cấu hình của backend**

```sh
root@postgres-client:/proc# psql -h pgpool2 -U tubt -p 9990 information -c "PGPOOL SHOW backend;"
Password for user tubt: 
           item            |       value       |                  description                  
---------------------------+-------------------+-----------------------------------------------
 backend_hostname0         | 34.106.45.98      | hostname or IP address of PostgreSQL backend.
 backend_port0             | 5432              | port number of PostgreSQL backend.
 backend_weight0           | 1                 | load balance weight of backend.
 backend_data_directory0   |                   | data directory of the backend.
 backend_application_name0 |                   | application_name of the backend.
 backend_flag0             | ALLOW_TO_FAILOVER | Controls various backend behavior.
 backend_hostname1         | 34.106.29.46      | hostname or IP address of PostgreSQL backend.
 backend_port1             | 5432              | port number of PostgreSQL backend.
 backend_weight1           | 1                 | load balance weight of backend.
 backend_data_directory1   |                   | data directory of the backend.
 backend_application_name1 |                   | application_name of the backend.
 backend_flag1             | ALLOW_TO_FAILOVER | Controls various backend behavior.
(12 rows)
```

**Hiển thị tất cả cấu hình**

```sh
                    item                    |                              value                              |                                                       description                                                        
--------------------------------------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------
 backend_hostname0                          | 34.106.45.98                                                    | hostname or IP address of PostgreSQL backend.
 backend_port0                              | 5432                                                            | port number of PostgreSQL backend.
 backend_weight0                            | 1                                                               | load balance weight of backend.
 backend_data_directory0                    |                                                                 | data directory of the backend.
 backend_application_name0                  |                                                                 | application_name of the backend.
 backend_flag0                              | ALLOW_TO_FAILOVER                                               | Controls various backend behavior.
 backend_hostname1                          | 34.106.29.46                                                    | hostname or IP address of PostgreSQL backend.
 backend_port1                              | 5432                                                            | port number of PostgreSQL backend.
 backend_weight1                            | 1                                                               | load balance weight of backend.
 backend_data_directory1                    |                                                                 | data directory of the backend.
 backend_application_name1                  |                                                                 | application_name of the backend.
 backend_flag1                              | ALLOW_TO_FAILOVER                                               | Controls various backend behavior.
 health_check_period                        | 0                                                               | Time interval in seconds between the health checks.
 health_check_timeout                       | 20                                                              | Backend node health check timeout value in seconds.
 health_check_user                          | nobody                                                          | User name for PostgreSQL backend health check.
 health_check_password                      | *****                                                           | Password for PostgreSQL backend health check database user.
 health_check_database                      | postgres                                                        | The database name to be used to perform PostgreSQL backend health check.
 health_check_max_retries                   | 0                                                               | The maximum number of times to retry a failed health check before giving up and initiating failover.
 health_check_retry_delay                   | 1                                                               | The amount of time in seconds to wait between failed health check retries.
 connect_timeout                            | 10000                                                           | Timeout in milliseconds before giving up connecting to backend.
 health_check_period0                       | 0                                                               | Time interval in seconds between the health checks.
 health_check_timeout0                      | 20                                                              | Backend node health check timeout value in seconds.
 health_check_user0                         | nobody                                                          | User name for PostgreSQL backend health check.
 health_check_password0                     | *****                                                           | Password for PostgreSQL backend health check database user.
 health_check_database0                     | postgres                                                        | The database name to be used to perform PostgreSQL backend health check.
 health_check_max_retries0                  | 0                                                               | The maximum number of times to retry a failed health check before giving up and initiating failover.
 health_check_retry_delay0                  | 1                                                               | The amount of time in seconds to wait between failed health check retries.
 connect_timeout0                           | 10000                                                           | Timeout in milliseconds before giving up connecting to backend.
 health_check_period1                       | 0                                                               | Time interval in seconds between the health checks.
 health_check_timeout1                      | 20                                                              | Backend node health check timeout value in seconds.
 health_check_user1                         | nobody                                                          | User name for PostgreSQL backend health check.
 health_check_password1                     | *****                                                           | Password for PostgreSQL backend health check database user.
 health_check_database1                     | postgres                                                        | The database name to be used to perform PostgreSQL backend health check.
 health_check_max_retries1                  | 0                                                               | The maximum number of times to retry a failed health check before giving up and initiating failover.
 health_check_retry_delay1                  | 1                                                               | The amount of time in seconds to wait between failed health check retries.
 connect_timeout1                           | 10000                                                           | Timeout in milliseconds before giving up connecting to backend.
 allow_multiple_failover_requests_from_node | off                                                             | A Pgpool-II node can send multiple failover requests to build consensus.
 dml_adaptive_object_relationship_list      |                                                                 | list of relationships between objects.
 failover_if_affected_tuples_mismatch       | off                                                             | Starts degeneration, If there's a data mismatch between primary and secondary.
 primary_routing_query_pattern_list         |                                                                 | list of query patterns that should be sent to primary node.
 app_name_redirect_preference_list          |                                                                 | redirect by application name.
 memqcache_auto_cache_invalidation          | on                                                              | Automatically deletes the cache related to the updated tables.
 cache_unsafe_memqcache_table_list          |                                                                 | list of tables should not be cached.
 database_redirect_preference_list          |                                                                 | redirect by database name.
 enable_consensus_with_half_votes           | off                                                             | apply majority rule for consensus and quorum computation at 50% of votes in a cluster with an even number of nodes.
 wd_no_show_node_removal_timeout            | 0                                                               | Timeout in seconds to revoke the cluster membership of NO-SHOW watchdog nodes.
 cache_safe_memqcache_table_list            |                                                                 | list of tables to be cached.
 allow_clear_text_frontend_auth             | on                                                              | allow to use clear text password authentication with clients, when pool_passwd does not contain the user password.
 clear_memqcache_on_escalation              | on                                                              | Clears the query cache in the shared memory when pgpool-II escalates to leader watchdog node.
```

# PGPOOL SET

Lệnh `PGPOOL SET` sẽ thay đổi giá trị của các tham số cấu hình PGPool-II cho phiên bản hiện tại. Lệnh này tương tự như lệnh `SET` trong PostgreSQL 

## Syntax

```sh
PGPOOL SET  configuration_parameter { TO | = } { value | 'value' | DEFAULT }
```

## Ví dụ

Thay đổi giá trị của tham số `client_idle_limit`

```sh
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "PGPOOL SET client_idle_limit = 350;"
Password for user tubt: 
SET
```

Thay đổi giá trị của tham số `client_idle_limit` về mặc định

```sh
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "PGPOOL SET client_idle_limit TO DEFAULT;"
Password for user tubt: 
SET
```

Thay đổi giá trị của tham số `log_min_messages`

```sh
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "PGPOOL SET log_min_messages TO INFO;"
Password for user tubt: 
SET
```

# PGPOOL RESET

Lệnh `PGPOOL RESET` sẽ khôi phục giá trị của tham số cấu hình PGPool-II về giá trị mặc định

## Syntax

```sh
PGPOOL RESET configuration_parameter
PGPOOL RESET ALL
```

## Ví dụ

Đặt lại giá trị của tham số `client_idle_limit`

```sh
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "PGPOOL RESET client_idle_limit;"
Password for user tubt: 
SET
```

Đặt lại tất cả tham số về mặc định

```sh
PGPOOL RESET ALL;
```

# SHOW POOL STATUS

Hiển thị POOL status, liệt kê danh sách các tham số cấu hình cùng với tên, giá trị và mô tả của chúng

```sh
SHOW POOL_STATUS
```

# SHOW POOL_NODES

Lệnh này trả về danh sách tất cả các node trong file cấu hình

```sh
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "SHOW pool_nodes"
Password for user tubt: 
 node_id |   hostname   | port | status | pg_status | lb_weight |  role   | pg_role | select_cnt | load_balance_node | replication_delay | replication_state | replication_sync_state | last_status_change  
---------+--------------+------+--------+-----------+-----------+---------+---------+------------+-------------------+-------------------+-------------------+------------------------+---------------------
 0       | 34.106.45.98 | 5432 | up     | unknown   | 0.500000  | primary | unknown | 9          | false             | 0                 |                   |                        | 2023-10-05 02:26:10
 1       | 34.106.29.46 | 5432 | up     | unknown   | 0.500000  | standby | unknown | 3          | true              | 0                 |                   |                        | 2023-10-05 02:26:10
(2 rows)
```

Trong đó:

- `node_id`: Mỗi node sẽ được thêm vào pgpool sẽ có một id riêng biệt

- `hostname`: IP hoặc hostname của các node

- `port`: Port kết nối đến service PostgreSQL của các node

- `status`: Trạng thái của node

- `lb_weight`: Tỉ lệ cân bằng tải, ở đây là 50:50, tức là tải được chia đều cho 2 node

- `role`: Vai trò của node, Ở đây 1 node đóng vai trò là node chính (primary), node còn lại đóng vai trò dự phòng (standby)

- `select_cnt`: Số truy vấn trên mỗi node

- `load_balance_mode`: Node cân bằng tải

# SHOW POOL_PROCESSES

Lệnh này gửi lại danh sách tất cả các quy trình PGPool-II đang chờ kết nối và xử lý kết nối

## Ví dụ

```sh
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "SHOW pool_processes"
Password for user tubt: 
 pool_pid |     start_time      | client_connection_count |  database   | username | backend_connection_time | pool_counter |       status        
----------+---------------------+-------------------------+-------------+----------+-------------------------+--------------+---------------------
 1797     | 2023-10-05 12:41:59 | 0                       |             |          |                         |              | Wait for connection
 1703     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1704     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1705     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1706     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1707     | 2023-10-05 12:35:32 | 1                       |             |          |                         |              | Wait for connection
 1708     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1822     | 2023-10-05 12:44:02 | 0                       |             |          |                         |              | Wait for connection
 1710     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1711     | 2023-10-05 12:35:32 | 2                       |             |          |                         |              | Wait for connection
 1802     | 2023-10-05 12:42:27 | 0                       |             |          |                         |              | Wait for connection
 1796     | 2023-10-05 12:41:33 | 0                       |             |          |                         |              | Wait for connection
 1714     | 2023-10-05 12:35:32 | 1                       |             |          |                         |              | Wait for connection
 1715     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1716     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1717     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1718     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1827     | 2023-10-05 12:44:34 | 0                       |             |          |                         |              | Wait for connection
 1830     | 2023-10-05 12:45:09 | 0                       |             |          |                         |              | Wait for connection
 1721     | 2023-10-05 12:35:32 | 0                       | information | tubt     | 2023-10-05 13:35:15     | 1            | Execute command
 1722     | 2023-10-05 12:35:32 | 1                       |             |          |                         |              | Wait for connection
 1723     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1795     | 2023-10-05 12:41:23 | 0                       |             |          |                         |              | Wait for connection
 1828     | 2023-10-05 12:44:44 | 0                       |             |          |                         |              | Wait for connection
 1829     | 2023-10-05 12:44:55 | 0                       |             |          |                         |              | Wait for connection
 1727     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1728     | 2023-10-05 12:35:32 | 1                       |             |          |                         |              | Wait for connection
 1729     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1730     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1731     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
 1732     | 2023-10-05 12:35:32 | 2                       |             |          |                         |              | Wait for connection
 1733     | 2023-10-05 12:35:32 | 0                       |             |          |                         |              | Wait for connection
(32 rows)
```

Trong đó:

- `pool_pid`: Là PID của tiến trình Pgpool-II

- `start_time`: Thời điểm tiến trình này được khởi chạy

- `client_connection_count`: Đếm số lần tiến trình được client kết nối

- `database`: Tên cơ sở dũ liệu được sử dụng cho tiến trình này

- `username`: Tên người dùng được sử dụng để kết nối đến database

- `backend_connection_time`: Là thời gian và ngày tạo kết nối

- `pool_counter`: Đếm số lần tiến trình được client sử dụng

- `status`: Là trạng thái hiện tại của quá trình. Các giá trị có thể là:

	+ `Execute command`: Thực hiện 1 lệnh

	+ `Idle`: Tiến trình đang chờ lệnh từ client

	+ `Wait for connection`: Tiến trình đang chờ kết nối từ client

# SHOW POOL_VERSION

Lệnh này hiển thị phiên bản của Pgpool

```sh
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "SHOW pool_version"
Password for user tubt: 
    pool_version     
---------------------
 4.4.4 (nurikoboshi)
(1 row)
```

# SHOW POOL_BACKEND_STATS

Lệnh `SHOW pool_backend_stats` thống kê các truy vấn đến các node backend

```sh
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "SHOW pool_backend_stats"
Password for user tubt: 
 node_id |   hostname   | port | status |  role   | select_cnt | insert_cnt | update_cnt | delete_cnt | ddl_cnt | other_cnt | panic_cnt | fatal_cnt | error_cnt 
---------+--------------+------+--------+---------+------------+------------+------------+------------+---------+-----------+-----------+-----------+-----------
 0       | 34.106.45.98 | 5432 | up     | primary | 2          | 0          | 1          | 1          | 1       | 27        | 0         | 0         | 1
 1       | 34.106.29.46 | 5432 | up     | standby | 3          | 0          | 0          | 0          | 0       | 14        | 0         | 0         | 1
(2 rows)
```

Trong đó

- `node_id`: ID của node

- `hostname`: Tên hoặc địa chỉ IP của node

- `port`: Port chạy service PostgreSQL trên node backend

- `status`: Trạng thái của node

- `role`: Vai trò của node

- `select_cnt`: Số lượng truy vấn `SELECT` đến node

- `insert_cnt`: Số lượng truy vấn `INSERT` đến node

- `update_cnt`: Số lượng truy vấn `UPDATE` đến node

- `delete_cnt`: Số lượng truy vấn `DELETE` đến node

- `ddl_cnt`: Số lượng truy vấn `DDL` đến node

Thực hiện `UPDATE` giá trị một cột trong Table để kiểm tra xem giá trị `update_cnt` có tăng hay không ?

```sh
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "UPDATE myinfo SET color = 'green' WHERE name = 'TuBT';"
Password for user tubt: 
UPDATE 1
root@postgres-client:~# psql -h pgpool2 -U tubt -p 9990 information -c "SHOW pool_backend_stats"
Password for user tubt: 
 node_id |   hostname   | port | status |  role   | select_cnt | insert_cnt | update_cnt | delete_cnt | ddl_cnt | other_cnt | panic_cnt | fatal_cnt | error_cnt 
---------+--------------+------+--------+---------+------------+------------+------------+------------+---------+-----------+-----------+-----------+-----------
 0       | 34.106.45.98 | 5432 | up     | primary | 2          | 0          | 2          | 2          | 1       | 30        | 0         | 0         | 2
 1       | 34.106.29.46 | 5432 | up     | standby | 3          | 0          | 0          | 0          | 0       | 15        | 0         | 0         | 1
(2 rows)
```