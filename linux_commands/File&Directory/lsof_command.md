# Lsof command in Linux

Lệnh `lsof` là viết tắt của List Of Open File. Lệnh này cung cấp danh sách các tập tin được mở. Về cơ bản, nó cung cấp thông tin để tìm ra các tập tin được mở bằng tiến trình nào. 

Lệnh `lsof` liệt kê các tệp đang mở trong bảng điều khiển đầu ra (shell). Nó có thể được kết hợp với lệnh `grep` có thể được sử dụng để thực hiện tìm kiếm và liệt kê nâng cao

**Syntax:**

```sh
$lsof [option][user name]
```

**Options with Example:**

**1. Liệt kể tất cả các tệp đang mở: Lệnh này liệt kê tất cả các tệp được mở bởi bất kỳ quy trình nào trong hệ thống**

```sh
lsof
```

Output:

```sh
COMMAND     PID   TID TASKCMD              USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME
systemd       1                            root  cwd       DIR                8,1     4096          2 /
systemd       1                            root  rtd       DIR                8,1     4096          2 /
systemd       1                            root  txt       REG                8,1  1620224       3448 /usr/lib/systemd/systemd
systemd       1                            root  mem       REG                8,1  1369384       4766 /usr/lib/x86_64-linux-gnu/libm-2.31.so
systemd       1                            root  mem       REG                8,1   178528       4751 /usr/lib/x86_64-linux-gnu/libudev.so.1.6.17systemd       1                            root  mem       REG                8,1  1575112       4585 /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
systemd       1                            root  mem       REG                8,1   137584       3777 /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.28.0
systemd       1                            root  mem       REG                8,1    67912       4633 /usr/lib/x86_64-linux-gnu/libjson-c.so.4.0.0
systemd       1                            root  mem       REG                8,1    34872       3519 /usr/lib/x86_64-linux-gnu/libargon2.so.1
systemd       1                            root  mem       REG                8,1   431472       3788 /usr/lib/x86_64-linux-gnu/libdevmapper.so.1.02.1
systemd       1                            root  mem       REG                8,1    30936       3861 /usr/lib/x86_64-linux-gnu/libuuid.so.1.3.0
systemd       1                            root  mem       REG                8,1  2954080       4749 /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
systemd       1                            root  mem       REG                8,1   686160       4581 /usr/lib/x86_64-linux-gnu/libzstd.so.1.4.4
systemd       1                            root  mem       REG                8,1    27064       3498 /usr/lib/x86_64-linux-gnu/libcap-ng.so.0.0.0
systemd       1                            root  mem       REG                8,1    18848       4765 /usr/lib/x86_64-linux-gnu/libdl-2.31.so
systemd       1                            root  mem       REG                8,1   588488       3855 /usr/lib/x86_64-linux-gnu/libpcre2-8.so.0.9
```

Tại đây, bạn quan sát thấy thông tin chi tiết các tập tin được mở, id tiến trình, người dùng liên kết với tiến trình, FD (File descriptor), kích thước của tệp ...

- `FD` - (File descriptor): Đại diện dưới dạng mô tả tệp

- `cwd` - (Current working directory): Thư mục làm việc hiện tại

- `txt` - (Text file): Tệp văn bản

- `mem` - (Mem file): Tệp tin bộ nhớ

- `mmap` - (Memory mapped device): Thiết bị ánh xạ bộ nhớ

**2. Liệt kê các tệp được mở bởi người dùng: Để tìm danh sách các tệp được mở bởi 1 người dùng cụ thể ta chạy lệnh sau:**

Syntax:

```sh
lsof -u <user_name>
```

Output:

```sh
root@buitu:~# lsof -u root
COMMAND     PID USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME
systemd       1 root  cwd       DIR                8,1     4096          2 /
systemd       1 root  rtd       DIR                8,1     4096          2 /
systemd       1 root  txt       REG                8,1  1620224       3448 /usr/lib/systemd/systemd
systemd       1 root  mem       REG                8,1  1369384       4766 /usr/lib/x86_64-linux-gnu/libm-2.31.so
systemd       1 root  mem       REG                8,1   178528       4751 /usr/lib/x86_64-linux-gnu/libudev.so.1.6.17
systemd       1 root  mem       REG                8,1  1575112       4585 /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
systemd       1 root  mem       REG                8,1   137584       3777 /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.28.0
systemd       1 root  mem       REG                8,1    67912       4633 /usr/lib/x86_64-linux-gnu/libjson-c.so.4.0.0
systemd       1 root  mem       REG                8,1    34872       3519 /usr/lib/x86_64-linux-gnu/libargon2.so.1
systemd       1 root  mem       REG                8,1   431472       3788 /usr/lib/x86_64-linux-gnu/libdevmapper.so.1.02.1
systemd       1 root  mem       REG                8,1    30936       3861 /usr/lib/x86_64-linux-gnu/libuuid.so.1.3.0
systemd       1 root  mem       REG                8,1  2954080       4749 /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
systemd       1 root  mem       REG                8,1   686160       4581 /usr/lib/x86_64-linux-gnu/libzstd.so.1.4.4
systemd       1 root  mem       REG                8,1    27064       3498 /usr/lib/x86_64-linux-gnu/libcap-ng.so.0.0.0
systemd       1 root  mem       REG                8,1    18848       4765 /usr/lib/x86_64-linux-gnu/libdl-2.31.so
systemd       1 root  mem       REG                8,1   588488       3855 /usr/lib/x86_64-linux-gnu/libpcre2-8.so.0.9.0
systemd       1 root  mem       REG                8,1   157224       4777 /usr/lib/x86_64-linux-gnu/libpthread-2.31.so
systemd       1 root  mem       REG                8,1   162264       3779 /usr/lib/x86_64-linux-gnu/liblzma.so.5.2.4
systemd       1 root  mem       REG                8,1   129248       3506 /usr/lib/x86_64-linux-gnu/liblz4.so.1.9.2
systemd       1 root  mem       REG                8,1    35440       3848 /usr/lib/x86_64-linux-gnu/libip4tc.so.2.0.0
systemd       1 root  mem       REG                8,1   129096       4566 /usr/lib/x86_64-linux-gnu/libidn2.so.0.3.6
systemd       1 root  mem       REG                8,1  1168056       3853 /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.2.5
systemd       1 root  mem       REG                8,1   417328       4574 /usr/lib/x86_64-linux-gnu/libcryptsetup.so.12.5.0
systemd       1 root  mem       REG                8,1   202760       3500 /usr/lib/x86_64-linux-gnu/libcrypt.so.1.1.0
systemd       1 root  mem       REG                8,1    31120       4599 /usr/lib/x86_64-linux-gnu/libcap.so.2.32
systemd       1 root  mem       REG                8,1   351352       3858 /usr/lib/x86_64-linux-gnu/libblkid.so.1.1.0
systemd       1 root  mem       REG                8,1    39088       3510 /usr/lib/x86_64-linux-gnu/libacl.so.1.1.2253
systemd       1 root  mem       REG                8,1    80736       4593 /usr/lib/x86_64-linux-gnu/libapparmor.so.1.6.1
systemd       1 root  mem       REG                8,1   112848       4691 /usr/lib/x86_64-linux-gnu/libkmod.so.2.3.5
systemd       1 root  mem       REG                8,1   133200       3514 /usr/lib/x86_64-linux-gnu/libaudit.so.1.0.0

. . .
. . .
```

Trong lệnh trên `lsof -u root` liệt kê tất cả các tệp được người dùng `root` mở. Cùng với đó, chúng ta có thể thấy loại tệp ở đây và chúng là:

- `DIR`: Directory

- `REG`: Regular file

- `CHR`: Character special file

**3. Liệt kê tất cả các tệp được mở bởi mọi người dùng ngoại trừ một người dùng cụ thể**

```sh
lsof -u ^<user_name>
```

Output:

```sh
root@buitu:~# lsof -u ^root
COMMAND     PID TID TASKCMD              USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME
systemd-n   439               systemd-network  cwd       DIR                8,1     4096          2 /
systemd-n   439               systemd-network  rtd       DIR                8,1     4096          2 /
systemd-n   439               systemd-network  txt       REG                8,1  2245632       3469 /usr/lib/systemd/systemd-networkd
systemd-n   439               systemd-network  mem       REG                8,1    27064       3498 /usr/lib/x86_64-linux-gnu/libcap-ng.so.0.0.0
systemd-n   439               systemd-network  mem       REG                8,1  1369384       4766 /usr/lib/x86_64-linux-gnu/libm-2.31.so
systemd-n   439               systemd-network  mem       REG                8,1   178528       4751 /usr/lib/x86_64-linux-gnu/libudev.so.1.6.17
systemd-n   439               systemd-network  mem       REG                8,1   133200       3514 /usr/lib/x86_64-linux-gnu/libaudit.so.1.0.0
systemd-n   439               systemd-network  mem       REG                8,1   686160       4581 /usr/lib/x86_64-linux-gnu/libzstd.so.1.4.4
systemd-n   439               systemd-network  mem       REG                8,1   137584       3777 /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.28.0
systemd-n   439               systemd-network  mem       REG                8,1    67912       4633 /usr/lib/x86_64-linux-gnu/libjson-c.so.4.0.0
systemd-n   439               systemd-network  mem       REG                8,1    34872       3519 /usr/lib/x86_64-linux-gnu/libargon2.so.1
systemd-n   439               systemd-network  mem       REG                8,1  2954080       4749 /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
systemd-n   439               systemd-network  mem       REG                8,1   431472       3788 /usr/lib/x86_64-linux-gnu/libdevmapper.so.1.02.1
systemd-n   439               systemd-network  mem       REG                8,1    30936       3861 /usr/lib/x86_64-linux-gnu/libuuid.so.1.3.0
systemd-n   439               systemd-network  mem       REG                8,1    18848       4765 /usr/lib/x86_64-linux-gnu/libdl-2.31.so
systemd-n   439               systemd-network  mem       REG                8,1   588488       3855 /usr/lib/x86_64-linux-gnu/libpcre2-8.so.0.9.0systemd-n   439               systemd-network  mem       REG                8,1  1575112       4585 /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
systemd-n   439               systemd-network  mem       REG                8,1   162264       3779 /usr/lib/x86_64-linux-gnu/liblzma.so.5.2.4
systemd-n   439               systemd-network  mem       REG                8,1   133568       3840 /usr/lib/x86_64-linux-gnu/libseccomp.so.2.5.1systemd-n   439               systemd-network  mem       REG                8,1    68320       4753 /usr/lib/x86_64-linux-gnu/libpam.so.0.84.2
systemd-n   439               systemd-network  mem       REG                8,1   387768       3868 /usr/lib/x86_64-linux-gnu/libmount.so.1.1.0

. . .
. . .
```

Trong ví dụ trên, chúng ta có thể quan sát thấy không có tệp nào được người dùng `root` mở

**4. Liệt kê tất cả các tệp đang mở theo một tiến trình cụ thể : Lệnh này có thể liệt kê tất cả các tệp được mở bởi một tiến trình cụ thể**

Syntax:

```sh
lsof -c <process_name>
```

Output:

```sh
root@buitu:~# lsof -c mysql
COMMAND   PID  USER   FD      TYPE             DEVICE SIZE/OFF   NODE NAME
mysqld  53969 mysql  cwd       DIR                8,1     4096 258359 /var/lib/mysql
mysqld  53969 mysql  rtd       DIR                8,1     4096      2 /
mysqld  53969 mysql  txt       REG                8,1 67241464  66558 /usr/sbin/mysqld
mysqld  53969 mysql  mem       REG                8,1    14672 258226 /usr/lib/mysql/plugin/auth_socket.so
mysqld  53969 mysql  DEL       REG               0,19          438588 /[aio]
mysqld  53969 mysql  DEL       REG               0,19          438587 /[aio]
mysqld  53969 mysql  DEL       REG               0,19          438586 /[aio]
mysqld  53969 mysql  DEL       REG               0,19          438585 /[aio]
mysqld  53969 mysql  DEL       REG               0,19          438584 /[aio]
mysqld  53969 mysql  DEL       REG               0,19          438583 /[aio]
mysqld  53969 mysql  DEL       REG               0,19          438582 /[aio]
mysqld  53969 mysql  DEL       REG               0,19          438581 /[aio]
mysqld  53969 mysql  mem       REG                8,1    35376 258234 /usr/lib/mysql/plugin/component_reference_cache.so
mysqld  53969 mysql  mem       REG                8,1    51856   4772 /usr/lib/x86_64-linux-gnu/libnss_files-2.31.so
mysqld  53969 mysql  mem       REG                8,1 28046896   4679 /usr/lib/x86_64-linux-gnu/libicudata.so.66.1
mysqld  53969 mysql  mem       REG                8,1  2029592   4761 /usr/lib/x86_64-linux-gnu/libc-2.31.so
mysqld  53969 mysql  mem       REG                8,1   104984   4763 /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
mysqld  53969 mysql  mem       REG                8,1  1369384   4766 /usr/lib/x86_64-linux-gnu/libm-2.31.so
mysqld  53969 mysql  mem       REG                8,1  1956992   4762 /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.28
mysqld  53969 mysql  mem       REG                8,1    18848   4765 /usr/lib/x86_64-linux-gnu/libdl-2.31.so
mysqld  53969 mysql  mem       REG                8,1   157224   4777 /usr/lib/x86_64-linux-gnu/libpthread-2.31.so
mysqld  53969 mysql  mem       REG                8,1    47960   4801 /usr/lib/x86_64-linux-gnu/libnuma.so.1.0.0
mysqld  53969 mysql  mem       REG                8,1    14336   4942 /usr/lib/x86_64-linux-gnu/libaio.so.1.0.1
mysqld  53969 mysql  mem       REG                8,1   129248   3506 /usr/lib/x86_64-linux-gnu/liblz4.so.1.9.2
mysqld  53969 mysql  mem       REG                8,1   629064 258256 /usr/lib/mysql/private/libprotobuf-lite.so.3.19.4
mysqld  53969 mysql  mem       REG                8,1  2954080   4749 /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
mysqld  53969 mysql  mem       REG                8,1   598104   4750 /usr/lib/x86_64-linux-gnu/libssl.so.1.1
mysqld  53969 mysql  mem       REG                8,1    35960   4779 /usr/lib/x86_64-linux-gnu/librt-2.31.so
mysqld  53969 mysql  mem       REG                8,1    14256  66530 /usr/lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7.0.0
mysqld  53969 mysql  mem       REG                8,1   223400  66524 /usr/lib/x86_64-linux-gnu/libevent_core-2.1.so.7.0.0
mysqld  53969 mysql  mem       REG                8,1  3132040   4680 /usr/lib/x86_64-linux-gnu/libicui18n.so.66.1
mysqld  53969 mysql  mem       REG                8,1  1976648   4684 /usr/lib/x86_64-linux-gnu/libicuuc.so.66.1
mysqld  53969 mysql  DEL       REG               0,19          438580 /[aio]
mysqld  53969 mysql  mem       REG                8,1   191504   4745 /usr/lib/x86_64-linux-gnu/ld-2.31.so
mysqld  53969 mysql  DEL       REG               0,19          438579 /[aio]

. . .
. . .
```

Tại đây ta có thể quan sát thấy các tệp và mô tả của chúng được mở bằng tiến trình `mysql`

**5. Liệt kê tất cả các tệp đang được mở bởi một tiến trình cụ thể bằng ID: Mỗi tệp được liên kết với một số ID tiến trình. Có thể có nhiều tệp được mở bằng một tiến trình. Bằng cách sử dụng `lsof -p <PID>`, các tệp được mở bởi một quy trình cụ thể có thể được kiểm tra**

Syntax:

```sh
lsof -p <PID>
```

Output:

```sh
root@buitu:~# lsof -p 17793
COMMAND   PID USER   FD   TYPE             DEVICE SIZE/OFF   NODE NAME
sshd    17793 root  cwd    DIR                8,1     4096      2 /
sshd    17793 root  rtd    DIR                8,1     4096      2 /
sshd    17793 root  txt    REG                8,1   884520   2880 /usr/sbin/sshd
sshd    17793 root  mem    REG                8,1   239896   4607 /usr/lib/x86_64-linux-gnu/libnss_systemd.so.2
sshd    17793 root  mem    REG                8,1    18720   3794 /usr/lib/x86_64-linux-gnu/security/pam_env.so
sshd    17793 root  mem    REG                8,1    27136   3806 /usr/lib/x86_64-linux-gnu/security/pam_limits.so
sshd    17793 root  mem    REG                8,1    14560   3810 /usr/lib/x86_64-linux-gnu/security/pam_mail.so
sshd    17793 root  mem    REG                8,1    14728   4754 /usr/lib/x86_64-linux-gnu/libpam_misc.so.0.82.1
sshd    17793 root  mem    REG                8,1    14656   3812 /usr/lib/x86_64-linux-gnu/security/pam_motd.so
sshd    17793 root  mem    REG                8,1   475944   3802 /usr/lib/x86_64-linux-gnu/security/pam_systemd.so
sshd    17793 root  mem    REG                8,1    14624   3831 /usr/lib/x86_64-linux-gnu/security/pam_umask.so
sshd    17793 root  mem    REG                8,1    14528   3804 /usr/lib/x86_64-linux-gnu/security/pam_keyinit.so
sshd    17793 root  mem    REG                8,1    14584   3809 /usr/lib/x86_64-linux-gnu/security/pam_loginuid.so
sshd    17793 root  mem    REG                8,1    27088   3821 /usr/lib/x86_64-linux-gnu/security/pam_selinux.so
sshd    17793 root  mem    REG                8,1    31120   4599 /usr/lib/x86_64-linux-gnu/libcap.so.2.32
sshd    17793 root  mem    REG                8,1    14512   3814 /usr/lib/x86_64-linux-gnu/security/pam_nologin.so
sshd    17793 root  mem    REG                8,1    18424   3820 /usr/lib/x86_64-linux-gnu/security/pam_cap.so
sshd    17793 root  mem    REG                8,1    14448   3815 /usr/lib/x86_64-linux-gnu/security/pam_permit.so
sshd    17793 root  mem    REG                8,1    64504   3832 /usr/lib/x86_64-linux-gnu/security/pam_unix.so
sshd    17793 root  mem    REG                8,1    51856   4772 /usr/lib/x86_64-linux-gnu/libnss_files-2.31.so
sshd    17793 root  mem    REG                8,1   137584   3777 /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.28.0
sshd    17793 root  mem    REG                8,1   101352   4778 /usr/lib/x86_64-linux-gnu/libresolv-2.31.so
sshd    17793 root  mem    REG                8,1    22600   4871 /usr/lib/x86_64-linux-gnu/libkeyutils.so.1.8
sshd    17793 root  mem    REG                8,1    56096   4865 /usr/lib/x86_64-linux-gnu/libkrb5support.so.0.1
sshd    17793 root  mem    REG                8,1   191040   4869 /usr/lib/x86_64-linux-gnu/libk5crypto.so.3.1
sshd    17793 root  mem    REG                8,1   157224   4777 /usr/lib/x86_64-linux-gnu/libpthread-2.31.so
```

**6. Liệt kê các tệp được mở bởi tất cả các PID khác. Theo cách tượng tự đối với user, ta cũng có thể sử dụng tùy chọn bên dưới để tìm ra danh sách các tệp được mở bởi tất cả PID khác trừ PID được chỉ định**

Syntax:

```sh
lsof -p ^<PID>
```

**7. Liệt kê cac tệp được mở bởi một thư mục cụ thể:**

Syntax:

```sh
lsof +D <directory_path>
```

Output:

```sh
root@buitu:~# lsof +D /var/log
COMMAND     PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
systemd-j   168   root  mem    REG    8,1 25165824  16200 /var/log/journal/4a0ad2c141c21ee8b8ccfd4c9567cdd7/system.journal
systemd-j   168   root  mem    REG    8,1  8388608  66312 /var/log/journal/4a0ad2c141c21ee8b8ccfd4c9567cdd7/user-1001.journal
systemd-j   168   root   22u   REG    8,1 25165824  16200 /var/log/journal/4a0ad2c141c21ee8b8ccfd4c9567cdd7/system.journal
systemd-j   168   root   31u   REG    8,1  8388608  66312 /var/log/journal/4a0ad2c141c21ee8b8ccfd4c9567cdd7/user-1001.journal
rsyslogd    603 syslog    7w   REG    8,1    13517    212 /var/log/syslog
rsyslogd    603 syslog    9w   REG    8,1  1826368  66280 /var/log/auth.log
rsyslogd    603 syslog   10w   REG    8,1    51790  66273 /var/log/kern.log
unattende   859   root    3w   REG    8,1        0  66281 /var/log/unattended-upgrades/unattended-upgrades-shutdown.log
zabbix_ag 29281 zabbix    1w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29281 zabbix    2w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29282 zabbix    1w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29282 zabbix    2w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29283 zabbix    1w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29283 zabbix    2w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29284 zabbix    1w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29284 zabbix    2w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29285 zabbix    1w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29285 zabbix    2w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29286 zabbix    1w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
zabbix_ag 29286 zabbix    2w   REG    8,1   112436 258134 /var/log/zabbix/zabbix_agentd.log
mysqld    53969  mysql    1w   REG    8,1     4292 258344 /var/log/mysql/error.log
mysqld    53969  mysql    2w   REG    8,1     4292 258344 /var/log/mysql/error.log
```

**8. Liệt kê các tệp được mở bởi kết nối mạng (Chỉ định giao thức kết nối)**

Syntax:

```sh
lsof -i <protocol>
```

Output:

```sh
root@buitu:~# lsof -i udp
COMMAND    PID            USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
systemd-n  439 systemd-network   15u  IPv4 383984      0t0  UDP buitu.us-west4-b.c.tubt-vtp.internal:bootpc
systemd-r  443 systemd-resolve   12u  IPv4  19821      0t0  UDP localhost:domain
chronyd   1376         _chrony    5u  IPv4  26550      0t0  UDP localhost:323
chronyd   1376         _chrony    6u  IPv6  26551      0t0  UDP ip6-localhost:323


root@buitu:~# lsof -i tcp
COMMAND     PID            USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
systemd-r   443 systemd-resolve   13u  IPv4  19822      0t0  TCP localhost:domain (LISTEN)
google_os   590            root    3u  IPv4  21977      0t0  TCP buitu.us-west4-b.c.tubt-vtp.internal:49298->metadata.google.internal:http (ESTABLISHED)
google_gu   754            root   10u  IPv4  26705      0t0  TCP buitu.us-west4-b.c.tubt-vtp.internal:33272->metadata.google.internal:http (ESTABLISHED)
sshd       1580            root    3u  IPv4  29687      0t0  TCP *:ssh (LISTEN)
sshd       1580            root    4u  IPv6  29698      0t0  TCP *:ssh (LISTEN)
sshd      17793            root    4u  IPv4 166833      0t0  TCP buitu.us-west4-b.c.tubt-vtp.internal:ssh->114.247.145.34.bc.googleusercontent.com:42352 (ESTABLISHED)
zabbix_ag 29281          zabbix    4u  IPv4 264731      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29281          zabbix    5u  IPv6 264732      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29282          zabbix    4u  IPv4 264731      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29282          zabbix    5u  IPv6 264732      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29283          zabbix    4u  IPv4 264731      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29283          zabbix    5u  IPv6 264732      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29284          zabbix    4u  IPv4 264731      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29284          zabbix    5u  IPv6 264732      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29285          zabbix    4u  IPv4 264731      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29285          zabbix    5u  IPv6 264732      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29286          zabbix    4u  IPv4 264731      0t0  TCP *:zabbix-agent (LISTEN)
zabbix_ag 29286          zabbix    5u  IPv6 264732      0t0  TCP *:zabbix-agent (LISTEN)
mysqld    53969           mysql   21u  IPv4 438590      0t0  TCP localhost:33060 (LISTEN)
mysqld    53969           mysql   23u  IPv4 438592      0t0  TCP localhost:mysql (LISTEN)
```

