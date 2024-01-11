# Tạo Template theo yêu cầu

Thực hiện tạo Template kiểm tra số lượng file đang mở của một Process động

**1. Thực hiện tạo Template**

Trong Zabbix frontend đi tới `Configuration` -> `Templates` -> chọn `Create template`

![](/zabbix/images/checkprocess.png)


![](/zabbix/images/checkprocess1.png)

Điền `Template name` và chọn `Groups` cho Template như hình trên sau đó chọn `Add` để tạo Template

**2. Thực hiện chạy lệnh trên server cài Zabbix Agent để kiểm tra số lượng file đang mở của một Process động**

Syntax:

```sh
ls /proc/$pid/fd/ | wc -l
```

Thực hiện check đối với process có PID là `1`

Output:

```sh
root@db:~# ls /proc/1/fd | wc -l
72
```

Vậy lệnh trên đã trả về giá trị 72 là số file đang được mở bởi process có PID là `1`

**3. Thực hiện tạo `Flexible User Parameter`**

Mở file cấu hình của Zabbix Agent (`/etc/zabbix/zabbix_agentd.conf`)

Sau đó ta thêm dòng sau để tạo `User Parameter`

```sh
UserParameter=computer.linux.usercount[*],sudo ls /proc/$1/fd|wc -l
```

Lưu, thoát và kiểm tra lại

```sh
root@db:/proc/1/fd# cat /etc/zabbix/zabbix_agentd.conf | grep UserParameter
#       Does not support UserParameters or aliases.
### Option: UnsafeUserParameters
# UnsafeUserParameters=0
UnsafeUserParameters=1
### Option: UserParameter
#       Format: UserParameter=<key>,<shell command>
# UserParameter=
#UserParameter=mysql.ping[*],mysqladmin -u$1 -p$2 ping 2>/dev/null|grep -c alive
UserParameter=computer.linux.usercount[*],sudo ls /proc/$1/fd|wc -l
```

**4. Thực hiện cấp quyền `root` cho user `zabbix` và không hỏi mật khẩu khi sử dụng `sudo`**

```sh
visudo
```

Thêm dòng sau

```sh
zabbix    ALL=(ALL:ALL) NOPASSWD: /usr/bin/ls
```

**5. Tạo `Item` cho Template mới**

Đi tới `Configuration` -> `Templates`

![](/zabbix/images/checkprocess2.png)

Tìm đến Template `Tubt_Template` vừa tạo và nhấn vào `Items`

![](/zabbix/images/checkprocess3.png)

Chọn `Create item` để tạo mới `Item`

![](/zabbix/images/checkprocess4.png)

Điền các giá trị như hình trên với giá trị

- `Name`: `Counting open file per process`

- `Type`: `Zabbix agent`

- `Key`: `computer.linux.usercount[1]`, ở đây ta sử dụng `key item` là `computer.linux.usercount` và truyền vào tham số `1` tương ứng với `$1` trong `User Parameter` để kiểm tra số file đang được mở bởi tiến trình có PID là `1`

- `Type of infomation`: Chọn `Text`

Sau khi điền các giá trị trên chọn `Test` để kiểm tra và lấy giá trị số file đang được mở bởi tiến trình `1` xem có đúng bằng `72` như đã kiểm tra ở trên không

Chọn `Test` sau đó nhập IP của host cần kiểm tra và port (Port ở đây là port chạy Zabbix Agent 10050)

![](/zabbix/images/checkprocess5.png)

Sau khi điền các giá trị chọn `Get value and test` để lấy giá trị 

![](/zabbix/images/checkprocess6.png)

Kết quả cho thấy có 72 file đang được mở bởi process có PID `1`

Thử lại với process có PID `169`

![](/zabbix/images/checkprocess7.png)

![](/zabbix/images/checkprocess8.png)

Kết quả trả về 34, vậy có 34 file đang được mở bởi process PID `169`

Kiểm tra thử bằng command line

```sh
root@db:~# ls /proc/169/fd | wc -l
34
```

Kết quả trả về tương tự, vậy `User Parameter` đã hoạt động. Ta có thể sử dụng `Template` này cho nhiều server khác