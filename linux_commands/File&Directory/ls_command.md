# ls command in Linux

`ls` là lệnh shell Linux liệt kê nội dung thư mục của các tệp thư mục. Nó cung cấp thông tin có giá trị về các tập tin, thư mục và thuộc tính của chúng

**Cú pháp của lệnh `ls` trong Linux**

```sh
ls [option] [file/directory]
```

`ls` sẽ hiển thị nội dung của thư mục hiện tại. Theo mặc định `ls` liệt kê các tập tin và thư mục theo thứ tự bảng chữ cái

|Options|Description|
|---|---|
|-l|Được biết đến như một định dạng dài hiển thị thông tin chi tiết về các tập tin và thư mục|
|-a|Đại diện cho tất cả tập tin bao gồm các tập tin và thư mục ẩn trong danh sách|
|-t|Sắp xếp các tập tin và thư mục theo thời gian sửa đổi lần cuối, hiển thị những tập tin và thư mục được sửa đổi gần đây nhất trước tiên
|-r|Đảo ngược thư tự được niêm yết nhất định|
|-S|Sắp xếp các tập tin và thư mục theo kích thước của chúng, liệt kê những tập tin lớn nhất trước tiên
|-R|Liệt kê các tập tin và thư mục theo cách đệ quy, bao gồm cả các thư mục con|
|-i|Hiển thị số chỉ mục (inode) của mỗi tệp và thư mục|
|-g|Hiển thị quyền sở hữu nhóm các tệp và thư mục thay vì chủ sở hữu|
|-h|In kích thước tệp ở định dạng con người có thể đọc được (ví dụ 1K, 234M, 2G)
|-d|Liệt kê chính các thư mục chứ không phải nội dung của chúng|

# Ví dụ thực tế về lệnh `ls`

1. Liệt kê tệp chỉnh sửa lần cuối bằng lệnh `ls -t`

Nó sắp xếp theo thời gian sửa đổi, hiển thị tệp được chỉnh sửa cuối cùng trước tiên. `head -1` chọn tập tin đầu tiên này. Để liệt kê tập tin đã chỉnh sửa gần nhất trong thư mục hiện tại, hãy sử dụng kết hợp lệnh `ls` và `head` như hình bên dưới

```sh
[root@linux ~]# vi first.txt 
[root@linux ~]# vi second.txt 
[root@linux ~]# ls -t | head -1
second.txt
```

Thao tác này sẽ liệt kê tệp cuối cùng bạn đã chỉnh sửa (tức là liệt kê tệp `second.txt`)

2. Liệt kê một tệp trên mỗi dòng `ls -1`

```sh
[root@linux ~]# ls -1
first.txt
second.txt
```

3. Liệt kê tất cả thông tin về tệp/thư mục bằng `ls -l`

```sh
[root@linux ~]# ls -l
total 8
-rw-r--r--. 1 root root 10 Sep 12 06:54 first.txt
-rw-r--r--. 1 root root  5 Sep 12 06:54 second.txt
```

`-rw-r--r--. 1 root root 10 Sep 12 06:54 first.txt`

Giải thích

- Ký tự `-` ở đầu cho biết đây là một file bình thường. Sau đây là các tùy chọn loại tệp có thể có trong ký tự đầu tiên của đầu ra `ls -l`

- Trường 1 - File permissions: Các ký tự tiếp theo chỉ định quyền của tập tin. Cứ mỗi 3 ký tự chỉ định quyền đọc, ghi và thực thi cho người dùng (root), cho nhóm(group) và cho người dùng khác (other user) theo thứ tự. Lấy ví dụ trên, `-rw-r--r--` biểu thị quyền đọc-ghi cho người dùng (root), quyền đọc cho nhóm(group) và quyền đọc cho người dùng khác(other user). Nếu cả 3 quyền được cấp cho người dùng (root), nhóm và người dùng khác thì định dạng sẽ giống như (-rwxrwxrwx)

- Trường 2 - Number of links: Trường thứ hai chỉ định số lượng liên kết cho tệp đó. Trong ví dụ này, `1` chỉ ra một liên kết đến tệp này

- Trường 3 - Owner: Trường thứ ba chỉ định chủ sở hữu của tệp. Trong ví dụ này, tệp thuộc sở hữu của tên người dùng `root`

- Trường 4 - Group: Trường thứ tư chỉ định nhóm của tệp. Trong ví dụ này, tệp thuộc nhóm `root`

- Trường 5 - Size: Trường thứ năm chỉ định kích thước của tệp tính bằng byte. Trong ví dụ này, `10` cho biết kích thước tệp tính bằng byte

- Trường 6 - Last modified date and time: Trường thứ sau chỉ định ngày và giờ sửa đổi tệp cuối cùng. Trong ví dụ này `Sep 12 06:54` chỉ định thời gian sửa đổi cuối cùng của tệp

- Trường 7 - File name: Trường cuối cùng là tên của tập tin, trong ví dụ này, tên tệp là `first.txt`

4. Hiển thị kích thước tệp ở định dạng mà gần với con người được bằng cách sử dụng `ls -lh`

```sh
[root@linux ~]# ls -lh
total 8.0K
-rw-r--r--. 1 root root 10 Sep 12 06:54 first.txt
-rw-r--r--. 1 root root  5 Sep 12 06:54 second.txt
```

5. Hiển thị thông tin thư mục bằng `ls -ld`

Khi sử dụng `ls -ld`, bạn sẽ nhận được thông tin chi tiết về nội dung thư mục. Ví dụ: nếu bạn sử dụng `ls -l /var` sẽ hiển thị tất cả các tệp trong thư mục `/var`. Tuy nhiên , nếu bạn muốn hiển thị thông tin về thư mục `/var`, hãy sử dụng tùy chọn `-ld` như hiển thị bên dưới:

```sh
[root@linux ~]# ls -l /var
total 4
drwxr-xr-x.  2 root root    6 Apr 11  2018 adm
drwxr-xr-x.  5 root root   44 Aug  9 16:56 cache
drwxr-xr-x.  3 root root   34 Aug  9 16:56 db
drwxr-xr-x.  3 root root   18 Aug  9 16:56 empty
drwxr-xr-x.  2 root root    6 Apr 11  2018 games
drwxr-xr-x.  2 root root    6 Apr 11  2018 gopher
drwxr-xr-x.  3 root root   18 Aug  9 16:56 kerberos
drwxr-xr-x. 25 root root 4096 Sep 12 06:31 lib
drwxr-xr-x.  2 root root    6 Apr 11  2018 local
lrwxrwxrwx.  1 root root   11 Aug  9 16:55 lock -> ../run/lock
drwxr-xr-x.  6 root root  275 Sep 12 06:31 log
lrwxrwxrwx.  1 root root   10 Aug  9 16:55 mail -> spool/mail
drwxr-xr-x.  2 root root    6 Apr 11  2018 nis
drwxr-xr-x.  2 root root    6 Apr 11  2018 opt
drwxr-xr-x.  2 root root    6 Apr 11  2018 preserve
lrwxrwxrwx.  1 root root    6 Aug  9 16:55 run -> ../run
drwxr-xr-x.  8 root root   87 Aug  9 16:56 spool
drwxrwxrwt.  3 root root   85 Sep 12 07:12 tmp
drwxr-xr-x.  2 root root    6 Apr 11  2018 yp
```

```sh
[root@linux ~]# ls -ld /var
drwxr-xr-x. 18 root root 254 Sep 12 06:31 /var
```

6. Sắp xếp các tệp dựa trên thời gian sửa đổi lần cuối bằng cách sử dụng `ls -lt`

```sh
ls -lt
```

Để sắp xếp tên tập tin hiển thị theo thứ tự thời gian sửa đổi lần cuối, ta nên kết hợp với tùy chọn `-l`

```sh
[root@linux ~]# ls -lt
total 8
-rw-r--r--. 1 root root  5 Sep 12 06:54 second.txt
-rw-r--r--. 1 root root 10 Sep 12 06:54 first.txt
```

7. Sắp xếp các dựa trên thời gian sửa đổi lần cuối (Theo thứ tự ngược lại) bằng cách sử dụng `ls -ltr`

```sh
ls -ltr
```

Để sắp xếp tên tệp trong lần sửa đổi gần nhất theo thứ tự ngược lại. Điều này sẽ hiển thị tệp được chỉnh sửa cuối cùng ở dòng cuối cùng, điều này sẽ rất hữu ích khi danh sách quá dài, vượt ra ngoài 1 trang

8. Hiển thị các tập tin ẩn bằng cách sử dụng `ls -a`

```sh
[root@linux ~]# ls -a
.   .bash_history  .bash_profile  .cshrc     .pki        .tcshrc
..  .bash_logout   .bashrc        first.txt  second.txt
```

Để hiển thị các tệp ẩn trong thư mục hãy sử dụng tùy chọn `-a`. Các tệp ẩn trong Linux bắt đầu bằng dấu `.` trong tên tệp của nó. Nó sẽ hiển thị tất cả các tệp bao gồm `.`(thư mục hiện tại) và `..`(thư mục mẹ)

Để hiển thị các tập tin ẩn nhưng không hiển thị `.`(thư mục hiện tại) và `..`(thư mục mẹ) ta sử dụng `ls -A`

```sh
[root@linux ~]# ls -A
.bash_history  .bash_logout  .bash_profile  .bashrc  .cshrc  first.txt  .pki  second.txt  .tcshrc
```

9. Hiển thị file tệp đệ quy bằng `ls -R`

```sh
[root@linux ~]# ls /etc/yum
fssnap.d  pluginconf.d  protected.d  vars  version-groups.conf  yum-cron.conf  yum-cron-hourly.conf
```

Để hiển thị tất cả các tập tin đệ quy. Khi bạn thực hiện việc này từ `/`, nó sẽ hiển thị đệ quy tất cả các tệp không bị ẩn trong toàn bộ hệ thống tệp

```sh
[root@linux ~]# ls -R /etc/yum
/etc/yum:
fssnap.d  pluginconf.d  protected.d  vars  version-groups.conf  yum-cron.conf  yum-cron-hourly.conf

/etc/yum/fssnap.d:

/etc/yum/pluginconf.d:
fastestmirror.conf  langpacks.conf

/etc/yum/protected.d:
systemd.conf

/etc/yum/vars:
contentdir  infra
```

10. Hiển thị số Inode của tệp bằng `ls -i`

Đôi khi bạn có thể muốn biết số lượng duy nhất của một tập tin. Sử dụng tùy chọn `-i` để hiển thị số inode của một tập tin


```sh
[root@linux ~]# ls -i
50512191 first.txt  51773514 second.txt
```

11. Hiển thị UID và GID bằng `ls -n`

```sh
[root@linux ~]# ls -n
total 8
-rw-r--r--. 1 0 0 10 Sep 12 06:54 first.txt
-rw-r--r--. 1 0 0  5 Sep 12 06:54 second.txt
```

Liệt kê đầu ra giống như `-l` nhưng hiển thị `uid` và `gid` ở định dạng số thay vì tên