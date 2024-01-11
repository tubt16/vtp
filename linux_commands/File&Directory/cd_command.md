# cd command in Linux

Lệnh `cd` trong Linux được gọi là thay đổi thư mục. Nó được dùng để di chuyển hiệu quả từ thư mục làm việc hiện tại sang các thư mục khác trong hệ thống

**Cú pháp của lệnh `cd` trong Linux**

```sh
`cd [directory]`
```

Tại đây, thay thế [directory] bằng đường dẫn của thư mục đích mà bạn muốn điều hướng đến

# Ví dụ thực tế về lệnh `cd`

1. Di chuyển bên trong thư mục con trong Linux

Để di chuyển vào bên trong thư mục con trong Linux, chúng ta sử dụng lệnh `cd`

```sh
cd [directory_name]
```

Nếu chúng ta muốn chuyển đến thư mục con `tubt`

```sh
first.txt  second.txt  tubt
[root@linux ~]# cd tubt/
[root@linux tubt]# pwd
/root/tubt
```

2. Sử dụng `/` làm đối số trong lệnh `cd`

Bằng cách sử dụng `/` làm đối số trong `cd`, chúng ta có thể thay đổi thư mục thành thư mục gốc. Thư mục gốc là thư mục đầu tiên trong hệ thống phân cấp tập tin Linux

```sh
[root@linux tubt]# pwd
/root/tubt
[root@linux tubt]# cd /
[root@linux /]# pwd
/
```

3. Di chuyển bên trong thư mục từ một thư mục 

Lệnh này được sử dụng để di chuyển bên trong một thư mục từ một thư mục

```sh
cd dir_1/dir_2/dir_3
```

4. Cách di chuyển thư mục chính từ bất kỳ vị trị nào trong hệ thống Linux

`~` Đối số này được sử dụng trong lệnh `cd` để thay đổi thư mục thành thư mục chính từ bất kỳ vị trí nào trong hệ thống Linux

```sh
cd ~
```

Chúng ta cũng có thể truyền lệnh `cd` mà không có đối số, điều này cuối cùng sẽ đưa chúng ta vào thư mục chính

```sh
cd
```

5. Cách chuyển sang cấp độ gốc hoặc tăng một cấp độ từ thư mục hiện tại trong Linux

Chúng tôi sử dụng `..` làm đối số trong lệnh `cd` được sử dụng để di chuyển đến thư mục cha của thư mục hiện tại hoặc tăng 1 cấp so với thư mục hiện tại

```sh
cd ..
```