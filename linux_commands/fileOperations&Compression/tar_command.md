# Tar command in Linux

Linux `tar`là viết tắt của `tape archive`, được sử dụng để tạo lưu trữ và giải nén các tệp lưu trữ. Chúng ta có thể sử dụng lệnh `tar` để tạo các tệp lưu trữ nén hoặc không nén, đồng thời duy trì và sửa đổi chúng

**Cú pháp**

```sh
tar [options] [archive-file] [file or directory to be archived]
```

|options|Description|
|---|---|
|-c|Tạo một kho lưu trữ bằng cách gộp các tập tin và thư mục lại với nhau|
|-x|Trích xuất các tập tin và thư mục từ một kho lưu trữ hiện có|
|-f|Chỉ định tên tệp của kho lưu trữ sẽ được tạo hoặc trích xuất|
|-t|Hiển thị hoặc liệt kê các tập tin và thư mục có trong kho lưu trữ|
|-u|Lưu trữ và thêm các tập tin hoặc thư mục mới vào kho lưu trữ hiện có|
|-v|Hiển thị thông tin chi tiết, cung cấp đẩu ra chi tiết trong quá trình lưu trữ hoặc trích xuất|
|-A|Ghép nhiều tệp lưu trữ vào một kho lưu trữ duy nhất|
|-z|Sử dụng tính năng nén gzip khi tạo tệp từ `tar`, tạo ra tệp lưu trữ nén có phần đuôi mở rộng `.tar.gz`|
|-j|Sử dụng tính năng nén bzip2 khi tạo tệp từ `tar`, tạo ra tệp lưu trữ nén có phần đuôi mở rộng `.tar.bz2`|
|-W|Xác minh tình toàn vẹn của tệp lưu trữ, đảm bảo nội dung của nó không bị hỏng|
|-r|Cập nhật hoặc thêm tệp hoặc thư mục vào kho lưu trữ đã có sẵn mà không tạo lại toàn bộ kho lưu trữ|

**Tệp lưu trữ là gì?**

Tệp lưu trữ là tệp bao gồm một hoặc nhiều tệp cùng metadata. Các tệp lưu trữ được sử dụng để gom nhiều tệp dữ liệu lại với nhau thành một tệp duy nhất để dễ di chuyển và lưu trữ hoặc đơn giản là nén các tệp để sử dụng ít dung lượng lưu trữ hơn

# Các ví dụ

1. Tạo một tệp lưu trữ tar bằng tùy chọn `-cvf`

```sh
tar cvf tubt.tar *.tubt
```

- `-c`: Tạo một file nén mới

- `-v`: Hiển thị đầu ra chi tiết, hiển thị quá trình nén file

- `-f`: Chỉ định tên tệp sau khi nén

Lệnh này tạo một tệp có tên `tubt.tar`, đây là lưu trữ của tất cả các tệp có đuôi `.txt` trong thư mục hiện tại

Output:

```sh
[root@linux ~]# ls
geekfile.txt  geeks  pattern.txt  tubt  tu.txt

[root@linux ~]# tar cvf tubt.tar *.txt
geekfile.txt
pattern.txt
tu.txt

[root@linux ~]# ls
geekfile.txt  geeks  pattern.txt  tubt  tubt.tar  tu.txt
```

2. Giải nén tệp bằng tùy chọn `-xvf`

```sh
tar xvf tubt.tar
```

- `-x`: Giải nén tập tin từ một file đã được nén

- `-v`: Hiển thị đầu ra chi tiết, hiển thị quá trình nén file

- `-f`: Chỉ định tên tệp sau khi nén

Lệnh này sẽ giải nén file `tubt.tar`

Output:

```sh
[root@linux ~]# tar xvf tubt.tar 
geekfile.txt
pattern.txt
tu.txt
```

3. Nén file sang định dạng gzip, sử dụng tùy chọn `-cvzf`

```sh
tar -cvzf tubt.tar.gz *.txt
```

Ngoài ra ta có thể sử dụng các option khác

- `-z`: Sử dụng nén gzip

- `-j`: Sử dụng nén bzip2

- `-J`: Sử dụng nén xz

4. Giải nén file gzip `*.tar.gz`, sử dụng tùy chọn `xvzf`

```sh
tar -xvzf tubt.tar.gz
```

5. Liệt kê nội dung được nén từ file chỉ định bằng tùy chọn `-tf` hoặc `-tvf`

```sh
tar tf tubt.tar
```

Output:

```sh
[root@linux ~]# tar tf tubt.tar 
geekfile.txt
pattern.txt
tu.txt
```