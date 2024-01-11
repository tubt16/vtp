# Zip command in Linux

Zip là tiện ích nén và đóng gói tệp dành cho Linux. Mỗi tệp được lưu trữ trong một tệp `.zip` có phần mở rộng `.zip`

- Zip được sử dụng để nén các tập tin nhằm giảm kích thước tập tin đó và cũng được sử dụng như một tiện ích gói tập

**Cú pháp**

|Options|Description|Syntax|
|---|---|---|
|-d|(Xóa tập tin khỏi tập nén): Tùy chọn này cho phép bạn xóa các tệp cụ thể khởi kho lưu trữ zip. Sau khi tạo tệp zip, bạn có thể xóa tệp một cách có chọn lọc bằng tùy chọn -d|`zip -d [file_name.zip] [files_name]`|
|-u|(Cập nhật tập tin trong tập nén): Tùy chọn `-u` cho phép bạn cập nhật các tệp trong tệp nén zip hiện có. Bạn có thể chỉ định danh sách các tệp cần cập nhật hoặc thêm tệp mới vào tệp nén. Quá trình cập nhật chỉ diễn ra nếu phiên bản sửa đổi mới hơn phiên bản đã có trong tệp nén|`zip -u [file_name.zip] [files_name]`|
|-m|(Di chuyển tập tin vào tệp nén): Với tùy chọn `-m`, bạn có di chuyển các tệp được chỉ định vào tệp nén zip. Thao tác này cũng xóa các thư mục hoặc tệp đích sau khi tạo tệp zip. Hãy cẩn thận khi sử dụng tùy chọn này vì nó sẽ xóa vĩnh viễn các tệp đầu vào|`zip -m [file_name.zip] [files_name]`|
|-r|(Zip đệ quy một thư mục): Tùy chọn `-r` cho phép bạn nén đệ quy một thư mục và các tệp của nó. Nó bao gồm tất cả các tệp có trong thư mục được chỉ định và các thư mục con của nó|`zip -r [file_name.zip] [files_name]`|
|-x|(Loại trừ các tệp tin khỏi zip): Sử dụng tùy chọn `-x`, bạn có thể loại trừ các tệp cụ thể khỏi việc đưa vào kho lưu trữ zip. Điều này hữu ích khi bạn muốn nén tất cả các tệp trong một thư mục nhưng muốn loại trừ một số tệp không mong muốn|`zip -r [file_name.zip] -x [directory_name]`
|-v|(Chế độ verbose): Tùy chọn -v kích hoạt chế độ verbose, cung cấp thông tin trong quá trình nén. Khi được sử dụng một mình, nó sẽ in màn hình chi tiết về tệp thực thi zip và môi trường đích|`zip -v [file_name.zip] [file_name]`

# Các ví dụ

1. Lệnh `unzip`

Unzip sẽ liệt kê, kiểm tra hoặc giải nén các tệp từ `.zip`

```sh
[root@linux ~]# unzip tubt.zip 
Archive:  tubt.zip
  inflating: geekfile.txt            
  inflating: pattern.txt             
 extracting: tu.txt
```

2. Sử dụng tùy chọn `-d` trong lệnh zip



Cú pháp:

```sh
zip -d [file_name.zip] [files_name]
```

Ví dụ:

Thực hiện nén 3 file `geekfile.txt`, `pattern.txt` và `tu.txt` thành file zip `tubt.zip`

```sh
zip -r tubt.zip geekfile.txt pattern.txt tu.txt
```

Xóa tệp `geekfile.txt` từ file nén `tubt.zip`

```sh
zip -d tubt.zip geekfile.txt
```

Output:

```sh
[root@linux ~]# zip -d tubt.zip geekfile.txt
deleting: geekfile.txt

[root@linux ~]# unzip tubt.zip 
Archive:  tubt.zip
  inflating: pattern.txt             
 extracting: tu.txt 
```

Sau khi xóa bằng lệnh `zip -d` ta giải nén để kiểm tra và chỉ thấy 2 file `pattern.txt ` và `tu.txt` đượi giải nén, vậy lệnh trên đã hoạt động và xóa đi file `geekfile.txt` như chỉ định

3. Sử dụng tùy chọn `-u` trong lệnh zip

Cú pháp: 

```sh
zip -u [file_name.zip] [files_name]
```

Giả sử có một tệp `myfile.zip`. Ta muốn đưa thêm file này vào tệp zip đã nén trước đó, ta sử dụng option `-u` như sau:

```sh
zip -u tubt.zip myfile.zip
```

Output:

```sh
[root@linux ~]# zip -u tubt.zip myfile.txt 
  adding: myfile.txt (stored 0%)
```

4. Sử dụng tùy chọn `-m` trong lệnh zip

Cú pháp:

```sh
zip -m [file_name.zip] [files_name]
```

Để di chuyển các tập tin vào tập nén ta sử dụng option `-m` trong lệnh zip, thao tác này cũng sẽ xóa các tệp được di chuyển

```sh
zip -m tubt.zip geekfile.txt myfile.txt pattern.txt tu.txt
```

Output:

```sh
[root@linux ~]# zip -m tubt.zip geekfile.txt myfile.txt pattern.txt tu.txt
  adding: geekfile.txt (deflated 31%)
  adding: myfile.txt (stored 0%)
  adding: pattern.txt (deflated 32%)
  adding: tu.txt (stored 0%)
[root@linux ~]# ls
geeks  tubt.zip  tubui
```

5. Sử dụng tùy chọn `-r` trong lệnh zip

Cú pháp:

```sh
zip -r [file_name.zip] [directory_name]
```

Để nén đệ quy ta sử dụng option `-r`

```sh
zip -r tubt.zip /root/tubt
```

Output:

```sh
[root@linux ~]# zip -r tubt.zip /root/tubui/
  adding: root/tubui/ (stored 0%)
  adding: root/tubui/geekfile.txt (deflated 31%)
  adding: root/tubui/myfile.txt (stored 0%)
  adding: root/tubui/pattern.txt (deflated 32%)
  adding: root/tubui/tu.txt (stored 0%)
```

6. Sử dụng tùy chọn `-x` trong lệnh zip

Cú pháp:

```sh
zip -r [file_name.zip] -x [directory_name]
```

Ta sử dụng tùy chọn `-x` để loại trừ file được chỉ định ra khỏi tệp nén

```sh
zip -r tubt.zip . -x geekfile.txt 
```

Output:

```sh
[root@linux ~]# ls
geekfile.txt  geeks  myfile.txt  pattern.txt  root  tubui  tu.txt
[root@linux ~]# zip -r tubt.zip . -x geekfile.txt 
  adding: .bash_logout (stored 0%)
  adding: .bash_profile (deflated 19%)
  adding: .bashrc (deflated 29%)
  adding: .cshrc (deflated 24%)
  adding: .tcshrc (deflated 22%)
  adding: .bash_history (deflated 5%)
  adding: .pki/ (stored 0%)
  adding: .pki/nssdb/ (stored 0%)
  adding: geeks/ (stored 0%)
  adding: geeks/tu/ (stored 0%)
  adding: geeks/tu/geekfile.txt (deflated 31%)
  adding: tubui/ (stored 0%)
  adding: root/ (stored 0%)
  adding: root/tubui/ (stored 0%)
  adding: root/tubui/geekfile.txt (deflated 31%)
  adding: root/tubui/myfile.txt (stored 0%)
  adding: root/tubui/pattern.txt (deflated 32%)
  adding: root/tubui/tu.txt (stored 0%)
  adding: myfile.txt (stored 0%)
  adding: pattern.txt (deflated 32%)
  adding: tu.txt (stored 0%)
```

