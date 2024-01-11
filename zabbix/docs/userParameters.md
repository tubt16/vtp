# Zabbix Agent

Zabbix Agent là một tiện ích được sử dụng rộng rãi để giám sát các tài nguyên và ứng dụng cục bộ trong bất kỳ cơ sở hạ tầng Zabbix nào

Zabbix Agent có rất nhiều số liệu. Điều này có nghĩa là không cần thiết phải phát triển cái gì đó mới, không phải code hay tùy chỉnh các kịch bản giám sát phức tạp

# User parameters

Tham số người dùng là gì? Đôi khi chúng ta cần giám sát thứ gì đó không phổ biến trên máy Windows hoặc Linux, không phải dung lượng ổ đĩa hay tải CPU mà là một ứng dụng cụ thể. Vì vậy `User parameters` được đưa ra để giải quyết cho điều đó

Bạn có thể viết tập lệnh truy xuất dữ liệu bạn cần và đưa dữ liệu đó vào tham số người dùng trong tệp config Zabbix Agent

Một `User Parameters` có cú pháp như sau:

```sh
UserParameter=<key>,<command>
```

`UserParameter` chứa `key` và `command`, `key` sẽ cần thiết khi định cấu hình một `item`

Sau khi chỉnh sửa `UserParameter` trong tệp config của Zabbix Agent, ta cần khởi động lại Zabbix Agent hoặc sử dụng tùy chọn `-R` để Zabbix nhận tham số mới

```sh
zabbix_agentd -R userparameter_reload
```

# User Parameter exsamples

Mở tệp config Zabbix Agent

```sh
vim /etc/zabbix/zabbix_agentd.conf
```

Tìm đến dòng sau

```sh
### Option: UserParameter
#       User-defined parameter to monitor. There can be several user-defined parameters.
#       Format: UserParameter=<key>,<shell command>
#       See 'zabbix_agentd' directory for examples.
#
# Mandatory: no
# Default:
# UserParameter=
```

Ta có thể thêm `User Parameter` tại đây

**Các ví dụ**

Ví dụ 1:

```sh
UserParameter=ping,echo 1
```

Agent sẽ luôn trả về `1` cho một `item` có `key` là ping

Ví dụ 2:

```sh
UserParameter=mysql.ping,mysqladmin -uroot ping | grep -c alive
```

Agent sẽ trả về `1` nếu máy chủ MySQL còn hoạt động, `0` nếu không

# Flexible User Parameters

Tham số người dùng linh hoạt (Flexible User Parameters) chấp nhận tham số bằng `key`. Bằng cách này, tham số người dùng linh hoạt có thể là cơ sở để tạo một số `item`

Tham số người dùng linh hoạt có cú pháp như sau:

```sh
UserParameter=key[*],command
```

Ví dụ 1:

```sh
UserParameter=ping[*],echo $1
```

Ta có thể xác định số lượng `item` không giới hạn để theo dõi tất cả các `item` có định dạng `ping[something]`

- `ping[0]`: Sẽ luôn trả về `0`

- `ping[aaa]`: Sẽ luôn trả về `aaa`

Ví dụ 2:

```sh
UserParameter=mysql.ping[*],mysqladmin -u$1 -p$2 ping | grep -c alive
```

Tham số này có thể được sử dụng để theo dõi tính khả dụng của cơ sở dữ liệu MySQL. Chúng ta có thể thay đổi `$1` `$2` thành `username` và `password`

```sh
mysql.ping[zabbix,our_password]
```

# Tạo `User Parameter`

Thực hiện thu thập số liệu tùy chỉnh với Zabbix agent bằng cách sử dụng `Flexible User parameter`

**Thực hiện tạo `Flexible User parameter` trên server `Mysql` đã cài Zabbix agent để kiểm tra Mysql có hoạt động hay không**

1. Kiểm tra lệnh check Mysql trên máy chủ Mysql nơi ta sẽ tạo `Flexible User parameter`.

```sh
mysqladmin -uadmin -pTubui16a6@ ping | grep -c alive
```

Output:

```sh
[root@db ~]# mysqladmin -uadmin -pTubui16a6@ ping | grep -c alive
1
```

2. Mở tệp cấu hình Zabbix agent (`/etc/zabbix/zabbix_agentd.conf`) và thêm đoạn sau để tạo `User parameter`

```sh
UserParameter=mysql.ping[*],mysqladmin -u$1 -p$2 ping 2>/dev/null|grep -c alive
```

```sh
[root@db ~]# cat /etc/zabbix/zabbix_agentd.conf | grep UserParam
#       Does not support UserParameters or aliases.
### Option: UnsafeUserParameters
# UnsafeUserParameters=0
### Option: UserParameter
#       Format: UserParameter=<key>,<shell command>
# UserParameter=
UserParameter=mysql.ping[*],mysqladmin -u$1 -p$2 ping 2>/dev/null|grep -c alive
```

Trong đó:

- `mysql.ping[*]`: đóng vai trò là `key`

- `mysqladmin -u$1 -p$2 ping 2>/dev/null|grep -c alive`: Đóng vai trò là `command`

- Đối với tham số người dùng linh hoạt ta sử dụng tham chiếu vị trí $1 ... $9 để tham chiếu tới các tham số tùy chỉnh trên Zabbix frontend

3. Tải lại `User parameter` bằng cách Restart Zabbix Agent 

```sh
systemctl restart zabbix-agent
```

4. Tạo `Item` trên Zabbix Frontend

Đi tới `Configuration` -> `Hosts` -> `Items`

![](/zabbix/images/usp.png)

Chọn `Create item` ở góc phải màn hình

![](/zabbix/images/usp2.png)

Thiết lập thông số như trong ảnh

Trong đó:

- `Name`: Mysql status

- `Type`: Zabbix agent

- `Key`: `mysql.ping["admin","Tubui16a6@"]` - Với `admin` và `Tubui16a6@` là 2 tham số được tham chiếu từ `$1` và `$2` trong `User Parameter`

Click add để tạo `Item`

5. Tạo Triggers cảnh báo

Chuyển sang tab `Triggers` chọn `Create triggers`

![](/zabbix/images/triggers.png)

Tại phần `Expression` add `Item` vừa tạo

![](/zabbix/images/usp3.png)

Sau khi insert `Item` vừa tạo, ta nhận được giá trị `Expression` như ảnh trên

6. Thực hiện stop service Mysql để kiểm tra xem có cảnh báo hay không

```sh
systemctl stop mysql
```

![](/zabbix/images/testusp.png)

Sau khi có cảnh báo, ta thử start `Mysql` xem trạng thái có trở về `Resolved` hay không

```sh
systemctl start mysql
```

![](/zabbix/images/testusp1.png)

Cảnh báo đã tự động `Resolved` khi chúng ta start `Mysql`. Vậy là `User parameter` vừa tạo đã hoạt động