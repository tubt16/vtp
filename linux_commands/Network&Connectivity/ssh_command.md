# SSH command in Linux

SSH là viết tắt của (Secure shell). Nó là giao thức được sử dụng để kết nối an toàn với máy chủ/hệ thống từ xa. SSH an toàn vì nó truyền dữ liệu được mã hóa giữa máy chủ và máy khách. Nó chuyển đầu vào từ máy khách đến máy chủ và chuyển tiếp đầu ra. SSH chạy mặc định ở cổng TCP/IP 22 

**Syntax:**

```sh
ssh user_name*host(IP/Domain_name)
```

**Thực hiện ssh**

Ví dụ: SSH tới máy chỉ có IP là 35.245.165.142 và username là `root`

Syntax:

```sh
ssh root@35.245.165.142
```

Output:

```sh
C:\Users\Tu>ssh root@35.245.165.142
The authenticity of host '35.245.165.142 (35.245.165.142)' can't be established.
ECDSA key fingerprint is SHA256:Io1PXCLN/PDrTVecAeXK/PFQjS68loHC8AN3EU1Qf/o.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '35.245.165.142' (ECDSA) to the list of known hosts.
root@35.245.165.142's password:
Last failed login: Thu Sep 14 22:57:09 UTC 2023 from 175.178.122.148 on ssh:notty
There were 154 failed login attempts since the last successful login.
Last login: Thu Sep 14 21:20:44 2023 from 42.118.79.228
[root@linux ~]#
```

Lệnh trên gồm 3 thành phần

- `ssh comand`: Thiết lập kết nối an toàn được mã hóa với máy chủ

- `user_name`: Đại diện cho tài khoản đang được truy cập trên máy chủ

- `host`: Đề cập đến máy, có thể là máy tính hoặc bộ định tuyến đang được truy cập. Nó có thể là địa chỉ IP hoặc tên miền

**Tạo ssh key**

Để tạo ssh key ta chạy lệnh

```sh
ssh key-gen
```

Output:

```sh
C:\Users\Tu>ssh root@35.245.165.142
The authenticity of host '35.245.165.142 (35.245.165.142)' can't be established.
ECDSA key fingerprint is SHA256:Io1PXCLN/PDrTVecAeXK/PFQjS68loHC8AN3EU1Qf/o.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '35.245.165.142' (ECDSA) to the list of known hosts.
root@35.245.165.142's password:
Last failed login: Thu Sep 14 22:57:09 UTC 2023 from 175.178.122.148 on ssh:notty
There were 154 failed login attempts since the last successful login.
Last login: Thu Sep 14 21:20:44 2023 from 42.118.79.228

[root@linux .ssh]# ls
id_rsa  id_rsa.pub
```

Private key phải là khóa ẩn trong khi public key là khóa được sao chép tới máy chủ từ xa. Sau khi đưa Public key tới máy chủ từ xa, kết nối sẽ được thiết lập bằng khóa SSH chứ không phải mật khẩu

Private key và Public key đóng vai trò như CHÌA KHÓA và Ổ KHÓA vậy, chìa khóa cần được giữ bí mật và để mở được ổ khóa ta cần đến chìa khóa

**Các tùy chọn có sẵn trong ssh**

|Options|Description|Syntax|
|---|---|---|
|-1|Buộc ssh chỉ sử dụng giao thức SSH -1|`ssh -1 user@host`|
|-2|Buộc ssh chỉ sử dụng giao thức SSH -2|`ssh -2 user@host`|
|-4|Chỉ cho phép địa chỉ IPv4|`ssh -4 user@host`|
|-6|Chỉ cho phép địa chỉ IPv6|`ssh -6 user@host`|
|-A|Bật chuyển xác thực tiếp các tác nhân kết nối|`ssh -A user@host`|
|-a|Vô hiệu hóa xác thực chuyển tiếp các tác nhân kết nối|`ssh -a user@host`
|-C|Nến tất cả dữ liệu (bao gồm stdin, stdout, stderr và dữ liệu cho các kết nối x11 và TCP) để truyền dữ liệu nhanh hơn|`ssh -C user@host`