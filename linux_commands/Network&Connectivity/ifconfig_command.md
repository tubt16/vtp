# Ifconfig command in Linux

Lệnh `ifconfig` (Interface configuration) được sử dụng để cấu hình giao diện mạng trên kernel. Nó được sử dụng lúc khởi động để thiết lập các giao diện khi cần thiết 

Ngoài ra lệnh này còn được sử dụng để gán địa chỉ IP và mặt nạ mạng cho một giao diện hoặc để bật hoặc tắt một giao diện nhất định

**Cú pháp**

```sh
ifconfig [...OPTIONS] [INTERFACE]
```

Các phiên bản mới của một số bản phân phối Linux không có sẵn lệnh `ifconfig`. Vì vậy trong trường hợp xảy ra lỗi "ifconfig: command not found". Thì hãy thực hiện lệnh sau để cài đặt `ifconfig`

Đối với Debian, Ubuntu và một số bản phân phối liên quan

```sh
sudo apt-get install net-tools
```

Đối với CentOS hoặc RHEL 

```sh
yum install net-tools
```

Điều này sẽ cài đặt `ifconfig` cùng với một số lệnh network khác như `arp`, `route`, `ipmaddr`

# Các tùy chọn đi kèm với lệnh

1. `-a` - Tùy chọn này được sử dụng hiển thị tất cả các giao diện có sẵn, ngay cả khi chúng bị không hoạt động (down)

Syntax:

```sh
ifconfig -a
```

Output:

```sh
[root@linux ~]# ifconfig -a
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1460
        inet 10.150.0.6  netmask 255.255.255.255  broadcast 10.150.0.6
        inet6 fe80::e546:f325:b40f:ff61  prefixlen 64  scopeid 0x20<link>
        ether 42:01:0a:96:00:06  txqueuelen 1000  (Ethernet)
        RX packets 340238  bytes 574306231 (547.7 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 304826  bytes 29934156 (28.5 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

2. `-s` - Hiển thị danh sách ngắn thay vì chi tiết

Syntax:

```sh
ifconfig -s
```

Output:

```sh
[root@linux ~]# ifconfig -s
Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
eth0             1460   340968      0      0 0        305540      0      0      0 BMRU
lo              65536        0      0      0 0             0      0      0      0 LRU
```

3. `-v` - Chạy lệnh ở verbose mode (chế độ hiển thị đầy đủ) - ghi lại thông tin chi tiết hơn về việc thực thi 

Syntax:

```sh
ifconfig -v
```

Output:

```sh
[root@linux ~]# ifconfig -v
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1460
        inet 10.150.0.6  netmask 255.255.255.255  broadcast 10.150.0.6
        inet6 fe80::e546:f325:b40f:ff61  prefixlen 64  scopeid 0x20<link>
        ether 42:01:0a:96:00:06  txqueuelen 1000  (Ethernet)
        RX packets 341402  bytes 574495446 (547.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 305960  bytes 30121086 (28.7 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

4. `up` - Tùy chọn này được sử dụng để KÍCH HOẠT trình điều khiển cho interface được chỉ định

Syntax:

```sh
ifconfig interface up
```

5. `down` - Tùy chọn này được sử dụng để TẮT trình điều khiển cho interface được chỉ định

Syntax:

```sh
ifconfig interface down
```

6. `add addr/prefixlen` - Tùy chọn này được sử dụng để thêm địa chỉ IPv6 vào interface

Syntax:

```sh
ifconfig interface add addr/prefixlen
```

7. `del addr/prefixlen` - Tùy chọn này được sử dụng để xóa địa chỉ IPv6 khỏi interface

Syntax:

```sh
ifconfig interface del addr/prefixlen
```

8. `[-]/[+]arp` - Tùy chọn này được sử dụng để enable/disable việc sử dụng giao thức ARP trên một interface

Syntax:

```sh
ifconfig interface [-]arp
```

9. `[-][+]promisc` - Tùy chọn này được sử dụng để enable/disable chế độ promiscuous trên một interface. Nếu được chọn, tất cả các gói tin trên mạng sẽ được nhận bởi interface

Syntax:

```sh
ifconfig interface [-]promisc
```

10. `mtu N`: Sử dụng tham số này để thiết lập MTU (Maximum Transfer Unit - Đơn vị truyền tối đa)

Syntax:

```sh
ifconfig <interface_name> mtu <mtu_size> up
```

Output:

```sh
[root@linux ~]# ifconfig eth0 mtu 4000 up

[root@linux ~]# ifconfig -a
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 4000
        inet 10.150.0.6  netmask 255.255.255.255  broadcast 10.150.0.6
        inet6 fe80::e546:f325:b40f:ff61  prefixlen 64  scopeid 0x20<link>
        ether 42:01:0a:96:00:06  txqueuelen 1000  (Ethernet)
        RX packets 343814  bytes 574860024 (548.2 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 308197  bytes 30465484 (29.0 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```