# Wget command in Linux

`Wget` là trình tải xuống không tương tác, được sử dụng để tải xuống từ máy chủ ngay cả khi người dùng chưa đăng nhập vào hệ thống và nó có thể hoạt động ở chế độ nền mà không cản trở quá trình hiện tại

- `wget` không tương tác, nghĩa là nó có thể hoạt động ở chế độ nền trong khi người dùng chưa đăng nhập. Điều này cho phép bạn bắt đầu ngắt kết nối khỏi hệ thống mà `wget` vẫn hoàn thành công việc. Ngược lại, hầu hết các trình duyệt Web đều yêu cầu sự hiện diện thường xuyên của người dùng, điều này có thể là trở ngại lớn khi truyền nhiều dữ liệu

- `wget` đã được thiết kế để hoạt động mạnh mẽ khi kết nối mạng chậm hoặc không ổn định; nếu quá trình tải xuống không thành công do sự cố mạng, quá trình tải xuống sẽ tiếp tục thử lại cho đến khi toàn bộ tệp được truy xuất. Nếu máy chủ hoạt động trở lại, nó sẽ hướng dẫn máy chủ tiếp tục tải xuống từ nơi nó dừng lại

**Cài đặt wget**

Đối với Ubuntu, Debian

```sh
apt-get install wget
```

Đối với CentOS, RHEL

```sh
yum install wget
```

**Syntax:**

```sh
wget [option] [URL]
```

**Ví dụ:**

1. Tải xuống một file đơn giản từ trang web

```sh
wget http://example.com/sample.php
```

2. Download tệp dưới dạng background

```sh
wget -b http://example.com/sample.php
```

3. Chuyển hướng thông báo tới tệp nhật ký được chỉ định

```sh
wget http://example.com/filename.txt -o /path/filename.txt
```

4. Để tiếp tục tải xuống tập tin

```sh
wget -c http://example.com/sample.tar.gz
```

5. Thử một số lần nhất định

```sh
wget --tries=10 http://example.com/sample.tar.gz
```

**Các ví dụ thực tế**

1. Sử dụng `wget` command để tải từng file

Một trong các lệnh wget cơ bản nhất là tải file và lưu nó vào thư mục hiện hành. Ví dụ muốn tải wordpress phiên bản mới nhất, ta làm như sau:

```sh
wget https://wordpress.org/latest.zip
```

Output:

```sh
[root@linux mnt]# wget https://wordpress.org/latest.zip
--2023-09-15 02:39:05--  https://wordpress.org/latest.zip
Resolving wordpress.org (wordpress.org)... 198.143.164.253
Connecting to wordpress.org (wordpress.org)|198.143.164.253|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 24938800 (24M) [application/zip]
Saving to: ‘latest.zip’

100%[=======================================================>] 24,938,800  96.2MB/s   in 0.2s   

2023-09-15 02:39:05 (96.2 MB/s) - ‘latest.zip’ saved [24938800/24938800]

[root@linux mnt]# ls
latest.zip
```

Trong ví dụ này ta sẽ có một file có tên `latest.zip` sẽ được tải vào thư mục đang sử dụng

Chúng ta sẽ tháy thêm các thông tin khác như: tiến trình tải, tốc độ tải, kích thước file, thời gian và ngày ...

2. Sử dụng Wget command để tải nhiều file

Chúng ta có thể sử dụng wget vào việc tải nhiều file cùng một lúc. Để làm vậy, bạn cần tạo một file text và đặt các đường dẫn URLs tải file vào đó. Trong ví dụ này, chúng ta sẽ tải các bản mới nhất cả Wordpress, Joomla và Drupal

Thêm các đường dẫn URLs vào file sau

```sh
vi example.txt
```

Dán các đường dẫn sau vằo file

```sh
https://wordpress.org/latest.zip

https://downloads.joomla.org/cms/joomla3/3-8-5/Joomla_3-8-5-Stable-Full_Package.zip

https://ftp.drupal.org/files/projects/drupal-8.4.5.zip
```

Sau đó ta sử dụng option `-i` để khai báo file chứa URLs và thực hiện tải WordPess, Joomla và Drupal từ đó

```sh
wget -i example.txt
```

Đợi sau khi quá trình tải về hoàn tất, ta kiểm tra 

```sh
[root@linux mnt]# ls
drupal-8.4.5.zip  example.txt  Joomla_3-8-5-Stable-Full_Package.zip  latest.zip  latest.zip.1
```

3. Sử dụng wget command để tải file dưới một tên khác

Trong ví dụ này chúng ta sẽ lưu file bằng một tên khác với option `-O`:

```sh
wget -O wordpress-install.zip https://wordpress.org/latest.zip
```

Trong trường hợp này tên file sau khi được tải về là `wordpres-install.zip` thay vì tên gốc `latest.zip`

4. Sử dụng wget command để lưu file trong một thư mục được chỉ định

Bạn có thể sử dụng wget để đặt file vào một thư mục được chỉ định bằng tùy chọn `-P`

```sh
wget -P /mnt/tubt /https://wordpress.org/latest.zip
```

File bạn tải về sẽ xuất hiện trong thư mục `/mnt/tubt`

5. Sử dụng wget command để giới hạn tốc độ tải về

Với wget bạn có thể giới hạn tốc độ tải. Việc này hữu dụng khi bạn tải một file lớn và tránh trường hợp nó dùng hết băng thông của bạn. 

Ví dụ dưới đây sẽ giới hạn tốc độ tải còn 500 KB

```sh
wget --limit-rate=500k https://wordpress.org/latest.zip
```

6. Sử dụng wget command để đặt số lần thử tải lại

Kết nối internet có thể gây lỗi gián đoạn. Để xử lý, chúng ta có thể tăng số lần thử lại bằng cách dùng option `-tries`

```sh
wget -tries=100 https://wordpress.org/latest.zip
```

7. Sử dụng wget command để tải file trong Background

Đối với file lớn, bạn có thể sử dụng option `-b`. Nó sẽ chạy ẩn dưới nền 

```sh
wget -b https://wordpress.org/latest.zip
```

Một file `wget-log` sẽ xuất hiện trong thư mục hiện hành, bạn có thể sử dụng `tail` để xem tình trạng tải xuống. Lệnh `tail` như sau:

```sh
tail -f wget-log
```

8. Sử dụng wget command để tiếp tục file tải bị gián đoạn

Việc download có thể bị gián đoạn nếu kết nối gặp vấn đề. Việc này thường xảy ra khi bạn đang tải file lớn. Thay vì tải lại từ đầu, bạn có thể tiếp tục bằng option `-c`

```sh
wget -c https://wordpress.org/latest.zip
```

Nếu bạn tải cùng một file đã bị gián đoạn trước đó mà không có option `-c` thì mặc định wget sẽ tải lại từ đầu và file mới sẽ có tên `latest.zip.1`

9. Sử dụng wget command để xác định link lỗi

Hãy sử dụng lệnh một cách cao cấp hơn. Chúng ta có thể dùng wget command để xác định broken URL mà hiện lỗi 404 error trên website của bạn. Bằng cách thực thi lệnh sau:

```sh
wget -o wget-log -r -l 5 --spider https://wordpress.org/latest.zip
```

Trong đó: 

- `-o`: Nhóm tất cả các output vào một file log `wget-log` để kiểm tra sau

- `-r`: Tải file đệ quy

- `-l`: Xác định cấp độ đệ quy

Chúng ta sẽ tiếp túc kiểm tra thêm file `wget-log` để xác định link lỗi. Đây là lệnh để kiểm tra việc này

```sh
grep -B 2 '404' wget-log | grep "http" | cut -d " " -f 4 | sort -u
```

10. Sử dụng wget command để tải file theo số 

Nếu bạn có hình ảnh hoặc file bị đánh số theo một danh sách nhất định, bạn có thể tải toàn bộ chứng bằng cấu trúc sau:

```sh
wget http://example.com/images/{1..50}.jpg
```