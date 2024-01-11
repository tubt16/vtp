# Ps command in Linux

Linux là hệ thống đa nhiệm và nhiều người dùng. Vì vậy, nó cho phép nhiều tiến trình hoạt động đồng thời mà không can thiệp lẫn nhau. 

Tiến trình là một trong những khái niệm quan trọng của Linux. Một tiến trình là một phiên bản thực thi của một chương trình và thực hiện các tác vụ khác nhau trong hệ điều hành

Linux cung cấp cho chúng ta một tiện ích có tên `ps`(Process Status) để xem thông tin liên quan đến các tiến trình trên hệ thống

Lệnh `ps` dùng để liệt kê các tiến trình đang chạy và PID của chúng cùng với một số thông tin khác tùy thuộc vào các tùy chọn khác nhau. Nó đọc thông tin tiến trình từ các tệp ảo trong hệ thống tệp `/proc`. `/proc` chứa các tệp ảo, đây là lý do tại sao nó được gọi là hệ thống tệp ảo

**Cú pháp**

```sh
ps [options]
```

**Các tùy chọn cho lệnh `ps`**

Lệnh `ps` mà không có tùy chọn đi kèm. Hiển thị các tiến trình cho shell hiện tại

```sh
[root@linux ~]# ps
  PID TTY          TIME CMD
 1379 pts/1    00:00:01 bash
 7699 pts/1    00:00:00 ps
```

Kết quả chứa 4 trường thông tin

`PID` - Process ID

`TTY` - Loại thiết bị đầu cuối mà người dùng đã đăng nhập

`TIME` - Lượng CPU tính bằng phút và giây mà tiến trình đang chạy

`CMD` - Tên của lệnh khởi chạy tiến trình

Sau đây là một số tùy chọn đi kèm với lệnh `ps`

- `ps -ef` or `ps -aux` - Liệt kê các tiến trình hiện đang chạy ở định dạng đủ

- `ps -ax` - Liệt kê các tiến trình đang chạy

- `ps -u <username>` - Liệt kê các quy trình cho một người dùng cụ thể

- `ps -C <command>` - Liệt kê quy trình cho một lệnh nhất định

- `ps -p <PID>` - Liệt kê các quy trình với một PID nhất định

- `ps -p <PPID>` - Liệt kê các tiến trình có ID tiến trình gốc nhất (PPID)

- `pstree` - Hiển thị tiến trình theo thứ bậc

- `ps -L` - Liệt kê tất cả các thread cho một tiến trình cụ thể

- `ps --sort pmem` - Tìm rõ rỉ bộ nhớ

- `ps -eo` - Hiển thị thông tin bảo mật

- `ps -U root -u root u` - Hiển thị các tiến trình đang chạy bằng root

# Các trường hợp sử dụng lệnh `ps`

Chúng ta hãy xem các trường hợp sử dụng thực tế của lệnh `ps` rất hữu ích cho quản trị viên hệ thống 

1. Liệt kê tất cả các tiến trình đang chạy

Để xem tất cả các tiến trình hiện đang chạy trên hệ thống, hãy sử dụng lệnh sau

```sh
[root@linux ~]# ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Sep12 ?        00:00:05 /usr/lib/systemd/systemd --switched-root --system --deroot         2     0  0 Sep12 ?        00:00:00 [kthreadd]
root         4     2  0 Sep12 ?        00:00:00 [kworker/0:0H]
root         6     2  0 Sep12 ?        00:00:00 [ksoftirqd/0]
root         7     2  0 Sep12 ?        00:00:00 [migration/0]
root         8     2  0 Sep12 ?        00:00:00 [rcu_bh]
root         9     2  0 Sep12 ?        00:00:08 [rcu_sched]
root        10     2  0 Sep12 ?        00:00:00 [lru-add-drain]
root        11     2  0 Sep12 ?        00:00:01 [watchdog/0]
root        12     2  0 Sep12 ?        00:00:00 [watchdog/1]
root        13     2  0 Sep12 ?        00:00:00 [migration/1]
root        14     2  0 Sep12 ?        00:00:00 [ksoftirqd/1]
root        16     2  0 Sep12 ?        00:00:00 [kworker/1:0H]
...
```

Trong đầu ra ở trên, PID biểu thị ID tiến trình của lệnh đang chạy, TTY là loại thiết bị đầu cuối nơi lệnh hiện tại đang được thực thi, TIME là thời gian cần thiết để CPU thực thi quy trình và CMD là lệnh hiện tại

2. Liệt kê tất cả các tiến trình đang được lọc theo mức sử dụng CPU hoặc bộ nhớ

Để xem tất cả các tiến trình hiện đang được lọc theo mức sử dụng CPU hoặc bộ nhớ, hãy sử dụng lệnh sau

```sh
[root@linux ~]# ps -aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 193528  6672 ?        Ss   Sep12   0:05 /usr/lib/systemd/systemd --switched-rroot         2  0.0  0.0      0     0 ?        S    Sep12   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        S<   Sep12   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        S    Sep12   0:00 [ksoftirqd/0]
root         7  0.0  0.0      0     0 ?        S    Sep12   0:00 [migration/0]
root         8  0.0  0.0      0     0 ?        S    Sep12   0:00 [rcu_bh]
root         9  0.0  0.0      0     0 ?        S    Sep12   0:08 [rcu_sched]
root        10  0.0  0.0      0     0 ?        S<   Sep12   0:00 [lru-add-drain]
root        11  0.0  0.0      0     0 ?        S    Sep12   0:01 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    Sep12   0:00 [watchdog/1]
root        13  0.0  0.0      0     0 ?        S    Sep12   0:00 [migration/1]
root        14  0.0  0.0      0     0 ?        S    Sep12   0:00 [ksoftirqd/1]
root        16  0.0  0.0      0     0 ?        S<   Sep12   0:00 [kworker/1:0H]
...
```

Trong kết quả đầu ra ở trên, %CPU hiển thị mức sử dụng CPU hiện tại theo quy trình, %MEM hiển thị mức sử dụng bộ nhớ theo quy trình, VSZ là kích thước của bộ nhớ và RSS là kích thước của nhóm thường trú

3. Liệt kê các quy trình cho một người dùng cụ thể

Để xem tất cả các tiến trình đang chạy cho một người dùng cụ thể, hãy sử dụng lệnh sau

```sh
ps -u <username>
```

```sh
[root@linux ~]# ps -u root
  PID TTY          TIME CMD
    1 ?        00:00:05 systemd
    2 ?        00:00:00 kthreadd
    4 ?        00:00:00 kworker/0:0H
    6 ?        00:00:00 ksoftirqd/0
    7 ?        00:00:00 migration/0
    8 ?        00:00:00 rcu_bh
    9 ?        00:00:08 rcu_sched
   10 ?        00:00:00 lru-add-drain
   11 ?        00:00:01 watchdog/0
   12 ?        00:00:00 watchdog/1
   13 ?        00:00:00 migration/1
   14 ?        00:00:00 ksoftirqd/1
   16 ?        00:00:00 kworker/1:0H
   18 ?        00:00:00 kdevtmpfs
   19 ?        00:00:00 netns
```

4. Danh sách các quy trình cho một lệnh cụ thể

Để xem tất cả các tiến trình đang chạy cho một lệnh cụ thể, ta sử dụng lệnh sau:

```sh
ps -C <command>
```

```sh
[root@linux ~]# ps -C sshd
  PID TTY          TIME CMD
 1374 ?        00:00:01 sshd
 1375 ?        00:00:02 sshd
```

5. Liệt kê quy trình với một PID cụ thể

Để xem quy trình với một PID chỉ định, ta sử dụng lệnh sau:

```sh
ps -p <PID>
```

```sh
[root@linux ~]# ps -p 1157
  PID TTY          TIME CMD
 1157 ?        00:00:00 crond
```

6. Xem tất cả các quy trình được liên kết với thiết bị đầu cuối

Để xem tất cả các quy trình liên kết với thiết bị đầu cuối, ta sử dụng lệnh sau:

```sh
ps -T
```

```sh
[root@linux ~]# ps -T
  PID  SPID TTY          TIME CMD
 1379  1379 pts/1    00:00:01 bash
 8009  8009 pts/1    00:00:00 ps
```

7. Liệt kê tất cả các tiến trình đang chạy

```sh
[root@linux ~]# ps -r
  PID TTY      STAT   TIME COMMAND
 8045 pts/1    R+     0:00 ps -r
```