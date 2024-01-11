# Scp command in Linux

Lệnh scp (secure copy) trong hệ thống Linux được sử dụng để sao chép tệp giữa các máy chủ một cách an toàn. Lệnh SCP hoặc bản sao an toàn cho phép truyền tệp an toàn giữa máy chủ cục bộ và máy chủ từ xa hoặc giữa hai máy chủ từ xa

Nó sử dụng xác thực và bảo mật tương tự như được sử dụng trong giao thức Secure Shell (SSH). SCP được biết đến nhờ tính đơn giản, bảo mật và tính khả dụng được cài đặt sẵn

**Syntax:**

```sh
scp [-i identity_file] [-l limit] [-o ssh_option] [-P port] [-S program] [[user@]host1:]file1 … [[user@]host2:]file2
```

**Các ví dụ**

1. Sao chép một tệp tin từ máy chủ cục bộ đến máy chủ từ xa

Syntax:

```sh
scp [file_name] remote_user@remote_host:/path/to/remote/directory
```

Trong đó:

- `file_name`: Tên file cần sao chép

- `remote_user`: Tên người dùng của máy chủ từ xa

- `remote_host`: Địa chỉ IP hoặc tên máy chủ từ xa

- `/path/to/remote/directory`: Thư mục nơi tập tin sẽ được sao chép trên máy chủ từ xa

*Ví dụ:* Chúng ta muốn sao chép tệp `myfile.txt` từ cục bộ sang máy chủ từ xa có địa chỉ IP 34.23.114.235

Trong trường hợp này các tham số sẽ là

- `file_name` = `myfile.txt`

- `remote_user` = `root`

- `remote_host` = `34.23.114.235`

- `/path/to/remote/directory` = `/home/root`

Syntax:

```sh
scp myfile.txt root@34.23.114.235:/root
```

Output:

```sh
[root@linux mnt]# ls
myfile.txt

[root@linux mnt]# scp myfile.txt root@34.23.114.235:/root/
The authenticity of host '34.23.114.235 (34.23.114.235)' can't be established.
ECDSA key fingerprint is SHA256:02eXUS4Erwj6Na/PZchRhdMyRiU6mh27WKtMlKvMlUw.
ECDSA key fingerprint is MD5:ef:46:1f:d3:f7:f1:a1:98:5a:71:a9:59:75:08:83:33.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '34.23.114.235' (ECDSA) to the list of known hosts.
root@34.23.114.235's password: 
myfile.txt                                                     100%    5     0.4KB/s   00:00
```

2. Sao chép một tệp tin từ máy chủ từ xa tới máy chủ cục bộ

```sh
scp user@remote_host:/path_to_file .
```

Trong đó:

- `user`: Tên người dùng của hệ thống từ xa

- `remote_host`: Địa chỉ IP của hệ thống từ xa

- `/path_to_file`: Đường dẫn chứa file cần sao chép

- `.`: Điều này có nghĩa là chúng ta muốn sao chép file đó từ máy chủ từ xa về máy chủ cục bộ tại thư mục hiện tại đang chạy câu lệnh

**Ví dụ:**

- `user` = root

- `remote_host` = 34.23.114.235

- `/path_to_file` = `/tmp/tubt.txt`

Syntax:

```sh
scp root@34.23.114.235:/tmp/tubt.txt .
```

Output:

```sh
[root@linux opt]# ls

[root@linux opt]# scp root@34.23.114.235:/tmp/tubt.txt .
root@34.23.114.235's password: 
tubt.txt                                                       100%   13     0.9KB/s   00:00    

[root@linux opt]# ls
tubt.txt
```

# Các tùy chọn đối với lệnh `scp`

|options|Description|
|---|---|
|-P|`port:` Chỉ định cổng để kết nối tới máy chủ từ xa (Mặc định nếu không cung cấp thì sẽ là port 22)|
|-p|Giữ nguyên gốc thời gian sửa đổi, thời gian truy cập và chế độ tệp gốc|
|-q|Tùy chọn này ẩn tiến trình truyền tệp trên thiết bị đầu cuối|
|-r|Sao chép đệ quy toàn bộ thư mục|
|-s|Tên chương trình được sử dụng cho kết nối được mã hóa|

**Các ví dụ:**

1. `-P`: Nó được sử dụng để chỉ định cổng kết nối trên máy chủ từ xa

Syntax:

```sh
scp -P port source_file user@hostname:/destination_dir
```

Ví dụ: Nếu chúng ta muốn sao chép tệp `test1.txt` từ máy chủ cục bộ sang máy chủ từ xa có địa chỉ IP 34.23.114.235 trên port 2222 với user là `root` và location = `/tmp`

Syntax: 

```sh
scp -P 2222 test1.txt root@34.23.114.235:/tmp
```

2. `-p`: Tùy chọn này được sử dụng khi chúng ta muốn giữ nguyên dữ liệu gốc của tệp. Về cơ bản, nó giữ nguyên thời gian sửa đổi, thời gian truy cập và các quyền đối với tệp gốc

Syntax:

```sh
scp -p source_file user@hostname:/destination_dir
```

Ví dụ:

```sh
scp -p test2.txt root@34.23.114.235:/tmp
```

3. `-q`: Tùy chọn này ẩn tiến trình truyền tệp trên thiết bị đầu cuối

Syntax: 

```sh
scp -q source_file user@hostname:/destination_dir
```

Ví dụ:

```sh
scp -q test3.txt root@34.23.114.235:/tmp
```

4. `-r`: Tùy chọn này khi chúng ta muốn sao chép toàn bộ thư mục và nội dung của nó. Về cơ bản có nghĩa là sao chép toàn bộ thư mục theo cách đệ quy

```sh
scp -r directory_name user@hostname:/destination_dir
```

Ví dụ:

```sh
scp -r tubt root@34.23.114.235:/tmp
```

Output:

```sh
[root@linux opt]# scp -r tubt/ root@34.23.114.235:/tmp
root@34.23.114.235's password: 
tubt1.txt                                                      100%    0     0.0KB/s   00:00    
tubt2.txt                                                      100%    0     0.0KB/s   00:00    
tubt3.txt                                                      100%    0     0.0KB/s   00:00    
tubt4.txt                                                      100%    0     0.0KB/s   00:00    
tubt5.txt                                                      100%    0     0.0KB/s   00:00 
```