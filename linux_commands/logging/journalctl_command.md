# Journalctl command in Linux

Lệnh `journalctl` là một phần của bộ tiện ích `systemd` và được sử dụng để TRUY VẤN và HIỂN THỊ thông báo tường trình TỪ NHẬT KÝ `systemd`. Nhật ký `systemd` là một hệ thống ghi log tập trung, thu thập và lưu trữ dữ liệu từ nhật ký từ nhiều nguồn khác nhau, bao gồm các dịch vụ hệ thống, sự kiện kernel và ứng dụng người dùng. 

Lệnh `journalctl` giúp người dùng giám sát hoạt động của hệ thống và chẩn đoán sự cố một cách hiệu quả 

**Syntax:**

Cú pháp cơ bản của lệnh `journalctl` như sau:

```sh
journalctl [options] [unit]
```

Trong đó:

- `options`: Các tùy chọn dòng lệnh khác nhau có sẵn để tùy chỉnh đầu ra

- `unit`: Đơn vị hệ thống hoặc nguồn nhật ký cụ thể để truy vấn. Nếu không có đơn vị nào được chỉ định `journalctl` sẽ hiển thị thông báo từ tất cả các đơn vị có sẵn

# Working with `journalctl` command

**1. Để hiển thị tất cả logs**

Syntax:

```sh
journalctl
```

Output:

```sh
root@buitu:~# journalctl
-- Logs begin at Thu 2023-09-21 22:23:14 UTC, end at Sat 2023-09-23 04:25:57 UTC. --
Sep 21 22:23:14 ubuntu kernel: Linux version 5.15.0-1042-gcp (buildd@bos03-amd64-005) (gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0, GNU ld (GNU Bi>Sep 21 22:23:14 ubuntu kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-1042-gcp root=PARTUUID=573945d9-0dfa-4263-a38a-ec6fc48d27a5 ro cons>Sep 21 22:23:14 ubuntu kernel: KERNEL supported cpus:
Sep 21 22:23:14 ubuntu kernel:   Intel GenuineIntel
Sep 21 22:23:14 ubuntu kernel:   AMD AuthenticAMD
Sep 21 22:23:14 ubuntu kernel:   Hygon HygonGenuine
Sep 21 22:23:14 ubuntu kernel:   Centaur CentaurHauls
Sep 21 22:23:14 ubuntu kernel:   zhaoxin   Shanghai
Sep 21 22:23:14 ubuntu kernel: BIOS-provided physical RAM map:
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x0000000000000000-0x0000000000000fff] reserved
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x0000000000001000-0x0000000000054fff] usable
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x0000000000055000-0x000000000005ffff] reserved
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x0000000000060000-0x0000000000097fff] usable
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x0000000000098000-0x000000000009ffff] reserved
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x0000000000100000-0x000000007f8ecfff] usable
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x000000007f8ed000-0x000000007fb6cfff] reserved
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x000000007fb6d000-0x000000007fb7efff] ACPI data
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x000000007fb7f000-0x000000007fbfefff] ACPI NVS
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x000000007fbff000-0x000000007ffdffff] usable
Sep 21 22:23:14 ubuntu kernel: BIOS-e820: [mem 0x000000007ffe0000-0x000000007fffffff] reserved
. . .
. . .
```

Lệnh này sẽ hiển thị các thông điệp nhật ký từ tất cả các đơn vị theo thứ tự cũ nhất đến mới nhất

**2. Đảo ngược thứ tự hiển thị nhật ký**

Để hiển thị nhật ký mới trước ta sử dụng option `-r`

Syntax:

```sh
journalctl -r
```

Output:

```sh
root@buitu:~# journalctl -r
-- Logs begin at Thu 2023-09-21 22:23:14 UTC, end at Sat 2023-09-23 04:30:57 UTC. --
Sep 23 04:30:57 buitu sshd[55269]: Disconnected from invalid user sshadmin 141.98.11.90 port 34638 [preauth]
Sep 23 04:30:57 buitu sshd[55269]: Received disconnect from 141.98.11.90 port 34638:11: Bye Bye [preauth]
Sep 23 04:30:55 buitu sshd[55269]: Failed password for invalid user sshadmin from 141.98.11.90 port 34638 ssh2
Sep 23 04:30:52 buitu sshd[55269]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=141.98.11.90
Sep 23 04:30:52 buitu sshd[55269]: pam_unix(sshd:auth): check pass; user unknown
Sep 23 04:30:52 buitu sshd[55269]: Invalid user sshadmin from 141.98.11.90 port 34638
Sep 23 04:27:51 buitu systemd[1]: Finished GCE Workload Certificate refresh.
Sep 23 04:27:51 buitu systemd[1]: gce-workload-cert-refresh.service: Succeeded.
Sep 23 04:27:51 buitu gce_workload_cert_refresh[55233]: 2023/09/23 04:27:51: Done
Sep 23 04:27:51 buitu gce_workload_cert_refresh[55233]: 2023/09/23 04:27:51: Error getting config status, workload certificates may not be confi>Sep 23 04:27:51 buitu systemd[1]: Starting GCE Workload Certificate refresh...
Sep 23 04:27:51 buitu sshd[55231]: Connection closed by authenticating user root 196.202.215.213 port 37943 [preauth]
Sep 23 04:27:49 buitu sshd[55231]: Failed password for root from 196.202.215.213 port 37943 ssh2
Sep 23 04:27:47 buitu sshd[55231]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=196.202.215.213  user>Sep 23 04:25:57 buitu systemd[1]: Finished NSS cache refresh.
Sep 23 04:25:57 buitu systemd[1]: google-oslogin-cache.service: Succeeded.
```

Lệnh này hiển thị nhật ký theo thứ tự ngược lại, hiển thị các log gần đây nhất ở trên cùng

**3. Giới hạn số lượng dòng muốn hiển thị**

Nếu ta chỉ hiển thị một số dòng nhật ký cụ thể, ta có thể sử dụng tùy chọn `-n` theo sau đó là số dòng mong muốn

```sh
journalctl -n 5
```

```sh
root@buitu:~# journalctl -n 5
-- Logs begin at Thu 2023-09-21 22:23:14 UTC, end at Sat 2023-09-23 04:38:26 UTC. --
Sep 23 04:38:26 buitu systemd[1]: Starting GCE Workload Certificate refresh...
Sep 23 04:38:26 buitu gce_workload_cert_refresh[55331]: 2023/09/23 04:38:26: Error getting config status, workload certificates may not be confi>Sep 23 04:38:26 buitu gce_workload_cert_refresh[55331]: 2023/09/23 04:38:26: Done
Sep 23 04:38:26 buitu systemd[1]: gce-workload-cert-refresh.service: Succeeded.
Sep 23 04:38:26 buitu systemd[1]: Finished GCE Workload Certificate refresh.
```

**4. Lọc nhật ký theo từ khóa**

Để truy xuất các mục nhật ký chứa một từ khóa, ta kết hợp với `grep`

Ở đây mình sẽ `grep "Failed password"` để xem có ai truy cập máy chủ của mình không

```sh
root@buitu:~# journalctl | grep "Failed password"
Sep 21 22:33:07 buitu sshd[2669]: Failed password for invalid user user1 from 141.98.11.11 port 40256 ssh2
Sep 21 22:35:01 buitu sshd[4287]: Failed password for invalid user user from 116.48.142.227 port 57909 ssh2
Sep 21 22:51:34 buitu sshd[8231]: Failed password for invalid user a from 141.98.11.11 port 35908 ssh2
Sep 21 23:01:48 buitu sshd[11020]: Failed password for invalid user ubnt from 121.178.15.232 port 37601 ssh2
Sep 21 23:02:02 buitu sshd[11020]: Failed password for invalid user ubnt from 121.178.15.232 port 37601 ssh2
Sep 21 23:02:10 buitu sshd[11020]: Failed password for invalid user ubnt from 121.178.15.232 port 37601 ssh2
Sep 21 23:02:19 buitu sshd[11020]: Failed password for invalid user ubnt from 121.178.15.232 port 37601 ssh2
Sep 21 23:02:29 buitu sshd[11020]: Failed password for invalid user ubnt from 121.178.15.232 port 37601 ssh2
Sep 21 23:02:47 buitu sshd[11020]: Failed password for invalid user ubnt from 121.178.15.232 port 37601 ssh2
Sep 21 23:03:11 buitu sshd[11882]: Failed password for invalid user ubnt from 121.178.15.232 port 38060 ssh2
Sep 21 23:03:24 buitu sshd[11882]: Failed password for invalid user ubnt from 121.178.15.232 port 38060 ssh2
Sep 21 23:11:38 buitu sshd[14794]: Failed password for invalid user support from 141.98.11.11 port 22474 ssh2
Sep 21 23:28:51 buitu sshd[16908]: Failed password for root from 31.41.244.61 port 56966 ssh2
Sep 21 23:31:26 buitu sshd[16935]: Failed password for invalid user pi from 151.25.244.37 port 51610 ssh2
Sep 21 23:31:26 buitu sshd[16936]: Failed password for invalid user pi from 151.25.244.37 port 51618 ssh2
Sep 21 23:50:38 buitu sshd[17092]: Failed password for invalid user admin from 141.98.11.11 port 54448 ssh2
Sep 22 00:08:25 buitu sshd[17234]: Failed password for root from 141.98.11.90 port 22534 ssh2
Sep 22 00:10:12 buitu sshd[17254]: Failed password for root from 121.178.15.232 port 58911 ssh2
Sep 22 00:10:25 buitu sshd[17254]: Failed password for root from 121.178.15.232 port 58911 ssh2
Sep 22 00:10:37 buitu sshd[17254]: Failed password for root from 121.178.15.232 port 58911 ssh2
Sep 22 00:10:51 buitu sshd[17254]: Failed password for root from 121.178.15.232 port 58911 ssh2
```

Từ output trên ta thấy được có rất nhiều `user` được LOGIN trên rất nhiều `port` và chúng đều `Fail`, qua đó chúng ta cần thận trọng trong việc bảo mật hệ thống, tránh để quét được dẫn đến việc bị chiếm quyền điều khiển hệ thống

# Các tùy chọn bổ sung của journalctl

Lệnh `journalctl` cung cấp các tùy chọn và tính năng bổ sung để tinh chỉnh thêm các truy vấn và truy xuất thông tin cụ thể. Dưới đây là một vài ví dụ:

**1. Lọc nhật ký theo mức độ ưu tiên**

Để hiển thị các mục nhật ký theo mức độ ưu tiên của chúng, ta sử dụng tùy chọn `-p` theo sau đó là cấp độ mong muốn (ví dụ: emerg, alert, crit, err, warning, notice, info hoặc debug)

Ví dụ:

```sh
journalctl -p warning
```

Output:

```sh
root@buitu:~# journalctl -p warning
-- Logs begin at Thu 2023-09-21 22:23:14 UTC, end at Sun 2023-09-24 15:28:26 UTC. --
Sep 21 22:23:14 ubuntu kernel: MDS CPU bug present and SMT on, data leak possible. See https://www.kernel.org/doc/html/latest/admin-gu>Sep 21 22:23:14 ubuntu kernel: TAA CPU bug present and SMT on, data leak possible. See https://www.kernel.org/doc/html/latest/admin-gu>Sep 21 22:23:14 ubuntu kernel: MMIO Stale Data CPU bug present and SMT on, data leak possible. See https://www.kernel.org/doc/html/lat>Sep 21 22:23:14 ubuntu kernel: acpi PNP0A03:00: fail to add MMCONFIG information, can't access extended PCI configuration space under >Sep 21 22:23:14 ubuntu kernel: i8042: Warning: Keylock active
Sep 21 22:23:14 ubuntu kernel: device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be reco>Sep 21 22:23:14 ubuntu kernel: platform eisa.0: EISA: Cannot allocate resource for mainboard
Sep 21 22:23:14 ubuntu kernel: platform eisa.0: Cannot allocate resource for EISA slot 1
Sep 21 22:23:14 ubuntu kernel: platform eisa.0: Cannot allocate resource for EISA slot 2
Sep 21 22:23:14 ubuntu kernel: platform eisa.0: Cannot allocate resource for EISA slot 3
Sep 21 22:23:14 ubuntu kernel: platform eisa.0: Cannot allocate resource for EISA slot 4
Sep 21 22:23:14 ubuntu kernel: platform eisa.0: Cannot allocate resource for EISA slot 5
Sep 21 22:23:14 ubuntu kernel: platform eisa.0: Cannot allocate resource for EISA slot 6
Sep 21 22:23:14 ubuntu kernel: platform eisa.0: Cannot allocate resource for EISA slot 7
Sep 21 22:23:14 ubuntu kernel: platform eisa.0: Cannot allocate resource for EISA slot 8
Sep 21 22:23:14 ubuntu kernel: GPT:Primary header thinks Alt. header is not at the end of the disk.
Sep 21 22:23:14 ubuntu kernel: GPT:6291455 != 41943039
Sep 21 22:23:14 ubuntu kernel: GPT:Alternate GPT header not at the end of the disk.
Sep 21 22:23:14 ubuntu kernel: GPT:6291455 != 41943039
Sep 21 22:23:14 ubuntu kernel: GPT: Use GNU Parted to correct GPT errors.
. . . 
. . .
```

Nó hiển thị tất cả các mục nhật ký có độ ưu tiên là `warning`

**2. Tùy chọn định dạng đầu ra**

Bạn có thể sửa đổi định dạng hiển thị các mục nhật ký bằng tùy chọn `-o`. Ví dụ: để hiển thị đầu ra dài dòng (verbose), hãy sử dụng

```sh
journalctl -o verbose
```

Output:

```sh
root@buitu:~# journalctl -o verbose
-- Logs begin at Thu 2023-09-21 22:23:14 UTC, end at Sun 2023-09-24 15:42:14 UTC. --
Thu 2023-09-21 22:23:14.003447 UTC [s=8f281179162e4073b56f798442a30840;i=1;b=c23c6d317d044a6c80ef6b4aac5ecf8d;m=259395;t=605e5f017c5f7>    _SOURCE_MONOTONIC_TIMESTAMP=0
    _TRANSPORT=kernel
    PRIORITY=5
    SYSLOG_FACILITY=0
    SYSLOG_IDENTIFIER=kernel
    MESSAGE=Linux version 5.15.0-1042-gcp (buildd@bos03-amd64-005) (gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0, GNU ld (GNU Binutils fo>    _BOOT_ID=c23c6d317d044a6c80ef6b4aac5ecf8d
    _MACHINE_ID=4a0ad2c141c21ee8b8ccfd4c9567cdd7
    _HOSTNAME=ubuntu
Thu 2023-09-21 22:23:14.003484 UTC [s=8f281179162e4073b56f798442a30840;i=2;b=c23c6d317d044a6c80ef6b4aac5ecf8d;m=2593b9;t=605e5f017c61c>    _SOURCE_MONOTONIC_TIMESTAMP=0
    _TRANSPORT=kernel
    SYSLOG_FACILITY=0
    SYSLOG_IDENTIFIER=kernel
    _BOOT_ID=c23c6d317d044a6c80ef6b4aac5ecf8d
    _MACHINE_ID=4a0ad2c141c21ee8b8ccfd4c9567cdd7
    _HOSTNAME=ubuntu
    PRIORITY=6
    MESSAGE=Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-1042-gcp root=PARTUUID=573945d9-0dfa-4263-a38a-ec6fc48d27a5 ro console=ttyS0>
. . .
. . .
```

Điều này sẽ hiển thị đầu ra được định dạng ở verbose mode

**3. Liệt kê những lần khởi động hệ thống**

Để xem thông tin chi tiết về các lần khởi động hệ thống trước đó, ta có thể sử dụng tùy chọn `--list-boots`

```sh
journalctl --list-boots
```

Output:

```sh
root@buitu:~# journalctl --list-boots
 0 c23c6d317d044a6c80ef6b4aac5ecf8d Thu 2023-09-21 22:23:14 UTC—Sun 2023-09-24 15:42:14 UTC
```

Lệnh này cung cấp danh sách các lần khởi động hệ thống cùng với ID khởi động và timestamp của chúng