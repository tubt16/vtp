# Cài đặt Iptables

`Iptables` thường được cài đặt mặc định trong hệ thống. Nếu chưa cài đặt, ta sử dụng lệnh sau

- Centos 7

```sh
yum install -y iptables-services
```

- Ubuntu

```sh
apt-get install iptables
```

Centos 7 sử dụng `Firewalld` làm tường lửa mặc định thay vì `Firewalld`. Nếu muốn sử dụng Iptables thì cần chạy lệnh sau

```sh
systemctl mask firewalld
systemctl stop firewalld
systemctl enable iptables
systemctl enable ip6tables
systemctl start iptables
systemctl start ip6tables
```

Hoặc nếu cần thiết thì xóa luôn firewalld khỏi Centos 7

```sh
yum remove -y firewalld
```

- Kiểm tra Iptables đã được cài trong hệ thống

```sh
iptables --version
```

- Check tình trạng của Iptables cũng như cách bật tắt services trên Centos 7

```sh
service iptables status
service iptables start
service iptables stop
service iptables restart
```

- Khởi động Iptables cùng hệ thống 

```sh
chkconfig iptables on
```

Trên Ubuntu, Iptables là chuỗi lệnh không phải là 1 service nên không thể start, stop hay restart. Một cách đơn giản để vô hiệu hóa là xóa hết toàn bộ các quy tắc đã thiết lập bằng lệnh flush

```sh
iptables -F
```

# Các nguyên tắc áp dụng trong Iptables

- Liệt kê các quy tắc hiện tại

```sh
iptables -L
```

# Sử dụng iptables để mở port VPS

1. Mở port 22 trên `iptables`

```sh
iptables -I INPUT -p tcp -m tcp --dport 22 -j ACCEPT
```

Mặc định iptables sẽ hiển thị ssh cho cổng 22, nếu đổi port ssh thì iptables sẽ hiển thị số cổng

```sh
ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:22
```

2. Xem danh sách rule 

```sh
iptables -L -n --line-numbers
```

3. Xóa rule ở dòng thứ 2

```sh
iptables -D input 2
```

3. Chặn 1 IP truy cập 

```sh
iptables -I IPPUT -s IP_ADDRESS -j DROP
```

4. Chặn 1 IP truy cập 1 port (ví dụ port 22) cụ thể

```sh
iptables -I INPUT -p tcp -s IP_ADDRESS -dport 22 -j DROP
```

# Lưu thiết lập

Sau khi thiết lập các rule trên Iptables ta cần lưu lại nếu không các thiết lập sẽ bị mất khi reboot hệ thống

```sh
service iptables save
```

