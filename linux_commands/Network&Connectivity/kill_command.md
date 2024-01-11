# Kill command in Linux

Lệnh `kill` trong Linux (nằm trong `/bin/kill`) là một lệnh tích hợp được sử dụng để chấm dứt các tiến trình theo cách thủ công, lệnh `kill` gửi tín hiệu đến một tiến trình để kết thúc tiến trình đó. Nếu người dùng không chỉ định bất kỳ tín hiệu (signal) nào đi kèm với lệnh `kill` thì mặc định tin hiệu `TERM` sẽ được gửi để chấm dứt tiến trình

**Cú pháp**

```sh
kill [signal] PID
```

Trong đó:

`PID`: Lệnh kill yêu cầu ID của tiến trình (PID) làm tham số để thực hiện chấm dứt một tiến trình cụ thể nào đó do ta chỉ định

`[signal]`: Chúng ta phải chỉ định tín hiệu làm đối số cho lệnh `kill` và nếu chúng ta không chỉ định tín hiệu. Tín hiệu mặc định `TERM` sẽ được áp dụng

**Tín hiệu có thể được chỉ định theo 3 cách sau**

1. By number:

Chúng ta có thể chỉ định một tín hiệu bằng cách sử dụng một số. Ví dụ, chúng ta có một tiến trình với PID 1212 và chúng ta muốn sử dụng tín hiệu `SIGKILL` để chấm dứt tiến trình này. `SIGKILL` có số tín hiệu là `9` (Để tìm giá trị của các tín hiệu chạy lệnh `kill -l`)

```sh
kill -9 1212
```

2. Kết hợp với tiền tố `SIG`

Chúng ta cũng có thể chỉ định tín hiệu bằng tiền tố `SIG`. Ví dụ: chúng ta cần gửi tín hiệu `SIGTERM` và PID là `1234`

```sh
kill -SIGTERM 1234
```

3. Không kết hợp với tiền tố

Chúng ta cũng có thể chỉ định tín hiệu mà không cần sử dụng tiền tố `SIG`. Ví dụ: nếu muốn gửi tín hiệu `TERM` và `PID` `4321`

```sh
kill -TERM 4321
```

# Một số tín hiệu phổ biến được sử dụng cùng với lệnh `kill`

Bảng dưới đây cho thấy một số tín hiệu phổ biến và số hiệu tương ứng của chúng

|Signal Name|Signal Number|Description|
|---|---|---|
|SIGHUP|1|Tắt và khởi động lại tiến trình đang hang up|
|SIGINT|2|Gián đoạn một tiến trình|
|SIGKILL|9|Chấm dứt một tiến trình|
|SIGTERM|15|Kết thúc một tiến trình|

**Các tùy chọn và ví dụ về lệnh `kill` trong Linux**

1. `kill -l`

Để hiển thị tất cả các tín hiệu có sẵn, bạn có sử dụng tùy chọn lệnh bên dưới

```sh
[root@linux ~]# kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

Note: 

- Để hiển thị danh sách các tiến trình đang chạy, hãy sử dụng lệnh `ps` và lệnh này sẽ hiển thị các tiến trình đang chạy với PID của chúng. Để chỉ định quy trình nào sẽ bị `kill`, chúng ta cần cung cấp PID

- PID 1 rất đặc biệt vì nó biểu thị tất cả các tiến trình ngoại trừ `kill` và `init`, đây là tiến trình gốc của tất cả các tiến trình trên hệ thống

2. `kill PID`

Tùy chọn này chỉ định ID của tiến trình bị kill. Sử dụng tín hiệu `SIGTERM` làm mặc định nếu chúng ta không cung cấp

```sh
[root@linux ~]# ps -aux | grep sshd
root      1374  0.0  0.1 113000  4344 ?        Ss   Sep12   0:02 /usr/sbin/sshd -D
root      8112  0.0  0.1 152820  5704 ?        Ss   09:07   0:00 sshd: root@pts/0
root      8258  0.0  0.0 112808   976 pts/0    S+   10:40   0:00 grep --color=auto sshd

[root@linux ~]# kill 8112Connection to linux closed by remote host.
Connection to linux closed.
```

Ví dụ trên mình đã tìm kiếm tiến trình `sshd` và `kill` tiến trình đó, kết quả session hiện tại đã bị kill và chúng ta bị đẩy ra khỏi phiên ssh

3. `kill -s`

Chỉ định tín hiệu để `kill` tiến trình

```sh
kill {-signal | -s signal} pid
```

4. `kill all`

Chỉ định các tiến trình cần `kill`

```sh
kill all firefox
```

Thực hiện `kill` tất cả các tiến trình có tên `firefox`


**Sự khác biệt giữa SIGTERM(15) và SIGKILL(9) trong lệnh kill**

SIGTERM yêu cầu tiến trình dừng hoạt động còn SIGKILL thì chấm dứt hoạt động của tiến trình ngay lập tức

SIGTERM có thể từ chối xử lý quá trình dừng hoạt động của tiến trình. Còn SIGKILL thì không cho tiến trình có cơ hội ngăn chặn hay từ chối

Một bức ảnh vui miêu tả sự khác nhau giữa `SIGTERM` và `SIGKILL`

![](/linux_commands/images/sigterm_sigkill.png)