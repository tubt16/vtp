# Ping command in Linux

Lệnh Ping (Packet Internet Groper) được sử dụng để kiểm tra kết nối mạng giữa host tới server/host. 

Lệnh này lấy địa chỉ IP hoăc URL đầu vào và gửi gói dữ liệu đến địa chỉ được chỉ định với thông báo `PING` và nhận được phần hồi từ server/host với giá trị được gọi là `ĐỘ TRỄ`

Độ trễ ping nhanh thấp hay cao thấp tương đương với kết nối nhanh hay chậm

Ping sử dụng ICMP để gửi đoạn message `ICMP echo` đến máy chủ chỉ định, néu máy chủ đó khả dụng thì nó sẽ gửi tin nhắn trả lời ICMP với thông điệp `ICMP reply`. Ping thường được do bằng mili giây. Mọi hệ điều hành hiện đại đều có sẵn lệnh `ping`



# Using ping

1. Ping version

```sh
ping -v
```

Output

```sh
[root@linux ~]# ping -V
ping utility, iputils-s20160308
```

2. Thực hiện ping

```sh
ping google.com
```

Output:

```sh
[root@linux ~]# ping google.com
PING google.com (172.253.62.102) 56(84) bytes of data.
64 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=1 ttl=116 time=2.25 ms
64 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=2 ttl=116 time=1.45 ms
64 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=3 ttl=116 time=1.40 ms
64 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=4 ttl=116 time=1.39 ms
64 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=5 ttl=116 time=1.37 ms
64 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=6 ttl=116 time=1.37 ms
64 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=7 ttl=116 time=1.54 ms
64 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=8 ttl=116 time=1.42 ms
64 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=9 ttl=116 time=1.39 ms
^C
--- google.com ping statistics ---
9 packets transmitted, 9 received, 0% packet loss, time 8012ms
rtt min/avg/max/mdev = 1.376/1.515/2.255/0.270 ms
```

Để đừng `ping`, chúng ta nên sử dụng tổ hợp phím `Ctrl + C` nếu không nó sẽ tiếp tục gửi các gói tin

Trong đó:

- `min`: Thời gian tối thiểu để nhận được phản hồi

- `avg`: Thời gian trung bình để nhận dược phản hồi

- `max`: Thời gian tối đa để nhận được phản hồi 

3. Kiểm soát số lượng gói tin Ping

Để đưa ra số gói cụ thể muốn gửi đến server/host ta sử dụng option `-c`

```sh
ping -c 5 google.com
```

```sh
[root@linux ~]# ping -c 5 google.com
PING google.com (172.253.63.101) 56(84) bytes of data.
64 bytes from bi-in-f101.1e100.net (172.253.63.101): icmp_seq=1 ttl=115 time=1.31 ms
64 bytes from bi-in-f101.1e100.net (172.253.63.101): icmp_seq=2 ttl=115 time=0.762 ms
64 bytes from bi-in-f101.1e100.net (172.253.63.101): icmp_seq=3 ttl=115 time=0.793 ms
64 bytes from bi-in-f101.1e100.net (172.253.63.101): icmp_seq=4 ttl=115 time=0.858 ms
64 bytes from bi-in-f101.1e100.net (172.253.63.101): icmp_seq=5 ttl=115 time=0.878 ms

--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4002ms
rtt min/avg/max/mdev = 0.762/0.920/1.311/0.201 ms
```

4. Kiểm soát kích thước của gói gửi

Trước đó mình đã giới hạn số lượng gói về 5 nhưng chúng ta còn có thể giảm kích thước của gói khi gửi với option `-s` (Thay vì gửi 56 byte theo mặc định)

```sh
ping -s 40 -c 5 google.com
```

Output:

```sh
[root@linux ~]# ping -s 20 -c 5 google.com
PING google.com (172.253.62.102) 20(48) bytes of data.
28 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=1 ttl=113 time=1.71 ms
28 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=2 ttl=113 time=1.10 ms
28 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=3 ttl=113 time=1.10 ms
28 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=4 ttl=113 time=1.22 ms
28 bytes from bc-in-f102.1e100.net (172.253.62.102): icmp_seq=5 ttl=113 time=1.16 ms

--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 1.104/1.263/1.716/0.230 ms
```

5. Thay đổi khoảng thời gian gửi

Theo mặc định, ping đợi 1 giây để gửi gói tiếp theo, tuy nhiên chúng ta hoàn toàn có thể customize nó với option `-i`

```sh
ping -i 2 google.com
```

Bây giờ, ping sẽ đợi 2 giây để gửi một gói tin server/host chỉ định

6. Chỉ lấy thông tin tóm tắt khi ping

Nếu ta chỉ muốn nhận được thông tin tóm tắt khi thực hiện ping, ta sử dụng option `-q`

```sh
ping -c 5 -q google.com
```

Output:

```sh
[root@linux ~]# ping -c 5 -q google.com
PING google.com (142.251.167.101) 56(84) bytes of data.

--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4003ms
rtt min/avg/max/mdev = 1.311/1.450/1.804/0.184 ms
```

7. Ngừng ping sau một thời gian chỉ định trước

Dể ngừng ping sau một thời gian, ta sử dụng option `-w`

```sh
ping -w 3 google.com
```

Lệnh trên sẽ ngừng ping sau 3 giây

8. Thêm mốc thời gian vào lệnh ping

Sử dụng tùy chọn TS (Time stamp) của gói IP ghi lại thời điểm hiện tại của sự kiện được ghi lại bởi một máy qua mạng

Chúng ta có 3 tùy chọn sau:

`tsonly` - Time stamp only

`tsandaddr` - Time and address

`tsprespec` - Timestamp pre-specified for multiple hosts

```sh
ping -T tsonly -c 2 127.0.0.1
ping -T tsandaddr -c 2 127.0.0.1
ping -T tsprespec -c 2 127.0.0.1
```

9. Đưa dữ liệu và gói tin

Chúng ta có thể điền dữ liệu vào gói bằng tùy chọn `-p`. Lưu ý dữ liệu đưa vào phải là dạng thập lục phân (hex)

```sh
ping -c 5 -p ff google.com
```

Output:

```sh
[root@linux ~]# ping -c 5 -p ff google.com
PATTERN: 0xff
PING google.com (172.253.63.102) 56(84) bytes of data.
64 bytes from bi-in-f102.1e100.net (172.253.63.102): icmp_seq=1 ttl=115 time=2.30 ms
64 bytes from bi-in-f102.1e100.net (172.253.63.102): icmp_seq=2 ttl=115 time=1.40 ms
64 bytes from bi-in-f102.1e100.net (172.253.63.102): icmp_seq=3 ttl=115 time=1.37 ms
64 bytes from bi-in-f102.1e100.net (172.253.63.102): icmp_seq=4 ttl=115 time=1.49 ms
64 bytes from bi-in-f102.1e100.net (172.253.63.102): icmp_seq=5 ttl=115 time=1.43 ms

--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 1.377/1.603/2.308/0.357 ms
```

10. Chỉ định TTL (Time to live)

Mỗi khi gói tin đi qua một bộ định tuyến trên mạng giá trị TTL sẽ giảm đi 1. Nếu giá trị TTL bằng 0, gói sẽ bị xóa khỏi mạng và trả về cho người gửi với thông báo "Lifetime expired". Điều này ngăn chặn sự lưu thông vô hạn của các gói trên mạng không thể đến được đích

Giá trị TTL mặc định thường là 64, ta có thể điều chỉnh được giá trị TTL với option `-t`

```sh
ping -c 5 -t 128 google.com
```