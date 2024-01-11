# mkdir command in Linux

Lệnh `mkdir` trong Linux cho phép người dùng tạo thư mục. Lệnh này có thể tạo nhiều thư mục cùng một lúc cũng như đặt quyền cho các thư mục

Điều quan trọng cần lưu ý là người dùng thực hiện lệnh này phải có đủ quyền để tạo một thư mục trong thư mục cha, nếu không sẽ nhận được lỗi 'permission denied'

**Cú pháp**

```sh
mkdir [options] [directories...]
```

**Các tùy chọn có sẵn trong mkdir**

1. `--help`:

Nó hiển thị thông tin liên quan đến trợ giúp

```sh
mkdir --help
```

2. `--version`:

Nó hiển thị số phiên bản, một số thông tin liên quan đến phiên bản

```sh
mkdir --version
```

3. `-v` (-verbose)

Tạo và hiển thị thông báo cho mọi thư mục được tạo

```sh
[root@linux ~]# mkdir -v tubt tubt1
mkdir: created directory ‘tubt’
mkdir: created directory ‘tubt1’
```

4. `-p`

Cho phép tạo thư mục cha nếu cần, nếu thư mục đã cha đã tồn tại thì sẽ bỏ qua và không có lỗi nào được chỉ định

```sh
[root@linux ~]# mkdir -p /mnt/first/second/third
[root@linux ~]# cd /mnt/first/second/third/
[root@linux third]# pwd
/mnt/first/second/third
```

Nếu thư mục `first` và `second` không tồn tại thì do tùy chọn `-p` nên mkdir sẽ tạo các thư mục này cho chúng ta

5. `-m`

Tùy chọn này được sử dụng để đặt các chế độ cho folder, tức là quyền, v.v cho các thư mục đã tạo. Cú pháp của chế độ này giống như lệnh `chmod`

```sh
[root@linux ~]# mkdir -m a=rwx tubui
[root@linux ~]# ls -lah | grep tubui
drwxrwxrwx.  2 root root   6 Sep 12 08:56 tubui
```

Cú pháp trên chỉ định rằng các thư mục được tạo sẽ cấp quyền truy cập cho tất cả người dùng để đọc, ghi và thực thi nội dung của các thư mục đã tạo. Bạn có thể sử dụng `a=r` để chỉ cho phép tất cả người dùng chỉ đọc từ thư mục `tubui`

