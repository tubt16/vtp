# Tail command in Linux

Lệnh `tail` in N số dữ liệu cuối cùng của đầu vào đã cho. Theo mặc định, nó in 10 dòng cuối cùng của tệp được chỉ định. Nếu có nhiều hơn một tệp được cung cấp thì dữ liệu từ mỗi tệp sẽ được đặt trước	tên tệp của nó

Cú pháp:

```sh
tail [OPTION]... [FILE]...
```

Ví dụ: Chúng ta có 2 file `state.txt` và `capital.txt`

```sh
[root@tubt ~]# cat state.txt 
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
Goa
Gujarat
Haryana
Himachal Pradesh
Jammu and Kashmir
Jharkhand
Karnataka
Kerala
Madhya Pradesh
Maharashtra
Manipur
Meghalaya
Mizoram
Nagaland
Odisha
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal
```

```sh
[root@tubt ~]# cat capital.txt 
Dispur
Patna
Raipur
Panaji
Gandhinagar
Chandigarh
Shimla
Srinagar
Ranchi
```

Nếu chúng ta không đưa bất kỳ tùy chọn nào, nó sẽ hiển thị 10 dòng cuối cùng của file `state.txt`

Ví dụ:

```sh
[root@tubt ~]# tail state.txt 
Odisha
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal
```

**Các tùy chọn khi sử dụng với lệnh `tail`**

|Short Options|Long Options|
|---|---|
|-n|--lines|
|-c|--bytes|
|-q|--quiet|
|-v|--verbose|
|-f|--follow|

1. `-n` (Num): In `n` dòng cuối cùng

```sh
[root@tubt ~]# tail -n 3 state.txt
Uttar Pradesh
Uttarakhand
West Bengal
```

2. `-c` (Num): In `n` byte cuối cùng

```sh
[root@tubt ~]# tail -c 6 state.txt 
engal
```

3. `-q`: Option này được sử dụng khi có nhiều hơn một file được đưa ra

```sh
[root@tubt ~]# tail state.txt capital.txt 
==> state.txt <==
Odisha
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal

==> capital.txt <==
Dispur
Patna
Raipur
Panaji
Gandhinagar
Chandigarh
Shimla
Srinagar
Ranchi
```

```sh
[root@tubt ~]# tail -q state.txt capital.txt 
Odisha
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal
Dispur
Patna
Raipur
Panaji
Gandhinagar
Chandigarh
Shimla
Srinagar
Ranchi
```

Khi sử dụng option `-q`, dữ liệu của 2 file sẽ được nối nhau mà không hiển thị tên của file trước dữ liệu

4. `-f`: Tùy chọn được sử dụng nhiều nhất đối với lệnh tail có lẽ là `-f`. Tùy chọn này chủ yếu được quẳn trị hệ thống sử dụng để theo dõi các tệp log. Tùy chọn này hiển thị 10 dòng cuối cùng của tệp theo thời gian thực và sẽ cập nhật khi có thêm dòng mới. Khi các dòng mới được thêm vào file log, bảng điều khiển sẽ cập nhật các dòng mới

```sh
[root@tubt log]# tail -f yum.log
Sep 12 15:47:54 Installed: gdisk-0.8.10-3.el7.x86_64
Sep 12 15:47:55 Installed: libicu-50.2-4.el7_7.x86_64
Sep 12 15:47:55 Installed: boost-regex-1.53.0-28.el7.x86_64
Sep 12 15:48:06 Installed: 1:google-compute-engine-oslogin-20221110.00-g1.el7.x86_64
Sep 12 15:48:06 Installed: nvme-cli-1.8.1-3.el7.x86_64
Sep 12 15:48:20 Installed: 1:google-compute-engine-20230801.00-g1.el7.noarch
Sep 12 15:48:35 Installed: 1:gce-disk-expand-20221110.00-g1.el7.noarch
Sep 12 15:48:36 Installed: 1:google-osconfig-agent-20230504.00-g1.el7.x86_64
Sep 12 15:49:59 Installed: google-cloud-sdk-446.0.0-1.x86_64
Sep 12 15:50:02 Installed: yum-cron-3.4.3-168.el7.centos.noarch
```

5. `-v`: Bằng cách sử dụng tùy chọn này, dữ liệu từ tệp chỉ định luôn được đặt sau tên tệp của nó

```sh
[root@tubt ~]# tail -v state.txt
==> state.txt <==
Odisha
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal
```

**Sử dụng lệnh `Tail` kết hợp với đường ống (Pipes `|`)**

Lệnh tail có thể được kết hợp với nhiều lệnh khác của Linux

Ví dụ 1:

Trong ví dụ sau, đầu ra của lệnh `tail` được cung cấp làm đầu vào cho lệnh `sort` với tùy chọn `-r` để sắp xếp 7 dòng cuối của tệp `state.txt` theo thứ tự ngược lại

```sh
[root@tubt ~]# tail -n 7 state.txt 
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal
[root@tubt ~]# tail -n 7 state.txt | sort -r
West Bengal
Uttar Pradesh
Uttarakhand
Tripura
Telangana
Tamil Nadu
Sikkim
```

Ví dụ 2:

Lệnh `tail` cũng có thể được kết hợp với một hoặc nhiều bộ lọc để xử lý bổ sung. Trong ví dụ sau, chúng ta lệnh `cat`, `head`, `tail` và đầu ra của lệnh này được lưu vào file `list.txt`

```sh
[root@tubt ~]# cat state.txt | head -n 20 | tail -n 5  > list.txt
[root@tubt ~]# cat list.txt 
Manipur
Meghalaya
Mizoram
Nagaland
Odisha
```

Lệnh `cat` đầu tiên cung cấp tất cả dữ liệu có trong tệp `state.txt` và sau đó, lệnh `pipe` (|) sẽ chuyển tất cả output từ lệnh `cat` sang lệnh `head`

Sau đó lệnh `head` cung cấp tất cả dữ liệu từ dòng số 1 đến dòng số 20 và chuyển hướng đầu ra từ lệnh `head` sang lệnh `tail`. Bây giờ lệnh `tail` sẽ lấy ra 5 dòng cuối cùng (từ 15 đến 20) và đầu ra sẽ chuyển đến tệp `list.txt`