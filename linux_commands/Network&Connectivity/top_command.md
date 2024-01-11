# Top command in Linux

Lệnh `top` được sử dụng hiển thị các tiến trình Linux. Nó cung cấp thông tin theo thời gian thực. Thông thường, lệnh này hiển thị thông tin tóm tắt của hệ thống và danh sách các tiến trình hoặc luồng hiện được Linux Kernel quản lý

Ngay sau khi bạn chạy lệnh này, nó sẽ mở ra một chế độ tương tác trong đó phần nửa trên sẽ chứa số liệu thống kê về các quy trình và việc sử dụng tài nguyên. Nửa dưới chứa danh sách các tiến trình đang chạy

```sh
top - 09:08:46 up 2 days,  2:37,  2 users,  load average: 0.00, 0.01, 0.05
Tasks:  87 total,   2 running,  85 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  3876756 total,  2798440 free,   249484 used,   828832 buff/cache
KiB Swap:        0 total,        0 free,        0 used.  3379244 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                      
 8132 root      20   0  159868   2128   1504 R   0.3  0.1   0:00.03 top                          
    1 root      20   0  193528   6672   4160 S   0.0  0.2   0:05.35 systemd                      
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.04 kthreadd                     
    4 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0:0H                 
    6 root      20   0       0      0      0 S   0.0  0.0   0:00.20 ksoftirqd/0                  
    7 root      rt   0       0      0      0 S   0.0  0.0   0:00.02 migration/0                  
    8 root      20   0       0      0      0 S   0.0  0.0   0:00.00 rcu_bh                       
    9 root      20   0       0      0      0 S   0.0  0.0   0:08.27 rcu_sched                    
   10 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 lru-add-drain                
   11 root      rt   0       0      0      0 S   0.0  0.0   0:01.07 watchdog/0                   
   12 root      rt   0       0      0      0 S   0.0  0.0   0:00.87 watchdog/1                   
   13 root      rt   0       0      0      0 S   0.0  0.0   0:00.02 migration/1                  
   14 root      20   0       0      0      0 S   0.0  0.0   0:00.19 ksoftirqd/1                  
   16 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/1:0H                 
   18 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kdevtmpfs                    
   19 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 netns                        
   20 root      20   0       0      0      0 S   0.0  0.0   0:00.09 khungtaskd                   
   21 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 writeback                    
   22 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kintegrityd                  
   23 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 bioset                       
   24 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 bioset                       
   25 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 bioset                       
   26 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kblockd                      
   27 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 md                           
   28 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 edac-poller                  
   29 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 watchdogd                    
   30 root      20   0       0      0      0 S   0.0  0.0   0:20.91 kworker/0:1                  
   39 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kswapd0                      
   40 root      25   5       0      0      0 S   0.0  0.0   0:00.00 ksmd
```

Các tham số cần quan tâm:

- `PID`: Hiển thị process ID của các tiến trình

- `PR`: Mức độ ưu tiên của tiến trình, Giá trị càng thấp thì mức độ ưu tiên càng cao (nằm trong khoảng từ 0-20)

- NI: Giá trị `nice` của task. Giá trị `âm` tương đương với độ ưu tiên cao hơn và giá trị `dương` nghĩa là mức độ ưu tiên thấp hơn

- `VIRT`:Tổng bộ nhớ ảo được tác vụ sử dụng

- `USER`: Tên người dùng sở hữu của tác vụ

- `$CPU`: Mức độ sử dụng CPU

- `TIME+`: Lượng CPU tính bằng phút, giây mà tiến trình đang chạy

- `SHR`: Thể hiện kích thước Bộ nhớ dùng chung (kb) được tác vụ sử dụng

- `%MEM`: Hiển thị mức độ sử dụng bộ nhớ của tác vụ

- `RES`: Quá trình đang sử dụng bao nhiêu RAM vật lý, tính bằng kilobytes

- `COMMAND`: Tên của lệnh bắt đầu quá trình

**Trong quá trình chạy, ta có thể sử dụng các phím tắt sau:**

- `spacebar`: Cập nhật ngay lập tức

- `z`: Đổi màu cho các tiến trình đang chạy, giúp xác định dễ dàng hơn

- `c`: Hiển thị đường dẫn tuyệt đối của các tiến trình

- `h`: Hiển thị màn hình trợ giúp

- `k`: Kill tiến trình, yêu cầu PID để kết thúc

- `p`: Sắp xếp theo mức sử dụng CPU

- `i`: Hiển thị hoặc bỏ qua các tiến trình không hoạt động /ru idle /zombie

- `n`: Yêu cầu số tiến trình để hiển thị trên màn hình

- `r`: Yêu cầu PID để áp dụng `renice` và ưu tiên mới (số càng cao, ưu tiên càng thấp)

- `R`: Sắp xếp các PID của tiến trình từ cao đến thấp (ngược lại so với mặc định)

- `q`: Thoát

Các tùy chọn đi kèm với lệnh `top`

1. Hiển thị tiến trình với người dùng cụ thể

```sh
top -u tubt
```

2. Hiển thị thông tin phiên bản và cú pháp lệnh

```sh
[root@linux ~]# top -h
  procps-ng version 3.3.10
Usage:
  top -hv | -bcHiOSs -d secs -n max -u|U user -p pid(s) -o field -w [cols]
```

3. Batch mode: Gửi đầu ra liên tục trên màn hình

```sh
top -b
```

4. Secure mode: Sử dụng `top` trong chế độ bảo mật

```sh
top -s
```

5. Command line: Lệnh dưới đây bắt đầu từ trên cùng với trạng thái cuối cùng được cập nhật sẽ hiển thị ở trên đầu

```sh
top -c
```

6. Delay time: Nó cho biết thời gian trễ giữa các lần cập nhật trên màn hình

```sh
top -d 5
```

Mỗi 5 giây trạng thái sẽ được cập nhật 1 lần