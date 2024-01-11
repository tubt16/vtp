# Watchdog

Các tham số cấu hình Watchdog được mô tả trong file `pgpool.conf`. Các tùy chọn sau đây được sử dụng cho watchdog

# Options

`use_watchdog` (boolean): Mặc định là off

Nếu Watchdog được bật, để phân biệt các backend server với nhau trong cụm Pgpool-II ta cần phải đặt ID cho các backend server đó bằng cách tạo tệp `pgpool_node_id` và chỉ định ID cho node

Ví dụ: Nếu cụm Pgpool-II có 3 node `server1` `server2` và `server3`, hãy tạo tệp `pgpool_node_id` trên mỗi máy chủ với nội dung như sau:

```sh
[root@postgres1 ~]# cat /etc/pgpool-II/pgpool_node_id 
0

[root@postgres2 ~]# cat /etc/pgpool-II/pgpool_node_id
1

[root@postgres3 ~]# cat /etc/pgpool-II/pgpool_node_id
2
```

`hostnameX` (string): Chỉ định tên máy chủ hoặc địa chỉ IP của máy chủ Pgpool-II. Số ở cuối tên tham số được gọi là node ID và bắt đầu từ 0

`wd_portX` (integer): Chỉ định port được sử dụng bởi watchdog để lắng nghe các kết nối. Mặc định là 9000

`pgpool_portX` (integer): Chỉ định port Pgpool-II được backend node sử dụng

Ví dụ: Nếu cụm Pgpool-II có 3 node `server1` `server2` và `server3` thì ta cần cấu hình `hostname`, `wd_port` và `pgpool_port` như sau:

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

# Virtual IP control

`delegate_ip` (string)

Chỉ định IP ảo (VIP) của Pgpool-II được kết nối từ client.

`if_cmd_path` (string)

Chỉ định đường dẫn đến lệnh mà Pgpool-II sẽ sử dụng để chuyển đổi IP ảo trên hệ thống. Chỉ đặt đường dẫn của thư mục chứa tệp nhị phân, chẳng hạn như `/sbin`

`if_up_cmd` (string)

Chỉ định lệnh bring up VIP dùng để chuyển đổi IP ảo. Đặt lệnh và tham số như sau `if_up_cmd = '/usr/bin/sudo /sbin/ip addr add $_IP_$/24 dev eth0 label eth0:0'`

`if_down_cmd` (string)

Chỉ định lệnh bring down VIP dùng để xóa IP ảo cũ sau khi đã chuyển đổi IP ảo. Đặt lệnh và tham số như sau `if_down_cmd = '/usr/bin/sudo /sbin/ip addr del $_IP_$/24 dev eth0'`

`arping_path` (string)

Chỉ định đường đẫn đến Pgpool-II sẽ sử dụng để gửi các yêu cầu ARP sau khi chuyển đổi IP ảo. Chỉ đặt đường dẫn của thư mục chứa tệp nhị phân như sau: `/usr/sbin`

`arping_cmd` (string)

Chỉ định lệnh sử dụng để gửi yêu cầu ARP sau khi chuyển đổi IP ảo. Đặt lệnh và tham số như sau: `/usr/bin/sudo /usr/sbin/arping -U $_IP_$ -w 1 -I eth0`

`ping_path` (string)

Chỉ định đường dẫn của lệnh ping để kiểm tra quá trình khởi động của IP ảo khi chuyển đổi. Đường dẫn là đường dẫn chứa lệnh ping ở dạng file nhị phân `/bin`

# Life checking Pgpool-II

Watchdog kiểm tra status của Pgpool-II định kỳ gọi là life check

`wd_lifecheck_method` (string)

Chỉ định method để life check. Có thể là một trong 3 tùy chọn `heartbeat` (default), `query` hoặc `external`

- `heartbeat`: Ở chế độ này, watchdog sẽ gửi tín hiệu heartbeat (gói UDP) theo định kỳ đến các node Pgpool-II, Watchdog cũng nhận được tín hiệu từ các node Pgpool-II. Nếu không có tín hiệu trong một khoảng thời gian nhất định. Watchdog coi node Pgpool-II đó là lỗi

- `query`: Ở chế độ này, watchdog sẽ gửi các truy vấn đến các node Pgpool-II và kiểm tra phản hồi. Khi network giữa các máy chủ Pgpool-II chậm điều này có thể hữu ích vì việc gửi đi một truy vấn nhanh hơn so với việc gửi đi một tín hiệu như `heartbeat`

- `external`: Chế độ này vô hiệu hóa tính năng life check của watchdog và dựa vào hệ thống bên ngoài để cung cấp khả năng kiểm tra tình trạng node của

`wd_interval` (integer)

Chỉ định khoảng thời gian giữa các lần life check của Pgpool-II. Mặc định là 10s

`wd_priority` (integer)

Tham số này được sử dụng để nâng mức độ ưu tiên của node watchdog để chọn ra một node Leader

Ví dụ:

```sh
[root@postgres1 ~]# pcp_watchdog_info -h localhost -p 9898 -U pgpool
Password: 
3 3 YES server1:9999 Linux postgres1 server1

server1:9999 Linux postgres1 server1 9999 9000 4 LEADER 0 MEMBER
server2:9999 Linux postgres2 server2 9999 9000 7 STANDBY 0 MEMBER
server3:9999 Linux postgres3 server3 9999 9000 7 STANDBY 0 MEMBER
```

# Lifecheck Heartbeat mode config

`heartbeat_hostnameX` (string)

Chỉ định địa chỉ IP hoặc tên máy chủ để gửi và nhận tín hiệu heartbeat. 

`heartbeat_portX` (integer)

Chỉ định port nhận tín hiệu heartbeat. Mặc định là 9694

`heartbeat_deviceX` (string)

Chỉ định tên thiết bị network nhận tín hiệu heartbeat. `heartbeat_deviceX` được khởi động với quyền `root`, nếu không hãy để trống tham số này

Ví dụ: Nếu cụm Pgpool-II có 3 node `server1` `server2` và `server3`, ta cần cấu hình `heartbeat_hostname`, `heartbeat_port` và `heartbeat_device` như sau:

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

`wd_heartbeat_keepalive` (integer)

Chỉ định thời gian giữa việc gửi tín hiệu `heartbeat`. Mặc định là 2s

`wd_heartbeat_deadtime` (integer)

Chỉ định thời gian trước khi coi node backend là `fail/dead` node nếu không nhận được tín hiệu heartbeat trong khoảng thời gian đó. Mặc định là 30s

> Tham khảo: https://www.pgpool.net/docs/44/en/html/runtime-watchdog-config.html