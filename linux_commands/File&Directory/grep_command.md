# Grep command in Linux

Bộ lọc grep tìm kiếm một mẫu ký tự cụ thể trong tệp và hiển thị tất cả các dòng có chứa mẫu đó. Mẫu được tìm kiếm trong tệp được gọi là biểu thức chính quy (grep là viết tắt của global search for regular expression and print out)

**Cú pháp**

```sh
grep [options] pattern [files]
```

**Tùy chọn mô tả**

- `-c`: Chỉ in số dòng khớp với mẫu

- `-h`: Hiển thị các dòng phù hợp nhưng không hiển thị tên tệp

- `-i`: Bỏ qua các trường hợp trùng khớp

- `-l`: Chỉ hiện thị danh sách tên tệp

- `-n`: Hiển thị số dòng phù hợp với mẫu được đưa ra

- `-v`: In tất cả các dòng khớp với mẫu

- `-e`: Chỉ định biểu thức với tùy chọn này. Có thể sử dụng nhiều lần

- `-f`: Lấy các mẫu từ tập tin, mỗi mẫu một dòng

- `-E`: Xử lý mẫu dưới dạng biểu thức chính quy mở rộng (ERE)

- `-w`: Nối cả từ

- `-o`: Chỉ in các phần phù hợp của một dòng phù hợp với mỗi phần như vậy trên một dòng đầu ra riêng biệt

- `-A n`: In dòng tìm kiếm và n dòng sau kết quả

- `-B n`: In dòng tìm kiếm và n dòng trước kết quả

- `-C n`: In dòng tìm kiếm và n dòng sau và trước kết quả

**Ví dụ mẫu**

```sh
[root@linux ~]# cat geekfile.txt 
unix is great os. unix was developed in Bell labs.
learn operating system.
Unix linux which one you choose.
uNix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```

1. Tìm kiếm không phân biệt chữ hoa thường: Tùy chọn `-i` cho phép tìm kiếm chuỗi không phân biệt chữ hoa, chữ thường trong tệp đã cho

```sh
grep -i "UNix" geekfile.txt 
```

Output:

![](/linux_commands/images/grep1.png)

2. Hiển thị số dòng chưa kết quả khớp: Chúng ta có thể tìm thấy số dòng khớp với chuỗi/mẫu đã cho với `-c`

```sh
grep -c "unix" geekfile.txt
```

Output:

```sh
[root@linux ~]# grep -c "unix" geekfile.txt 
2
```

3. Hiển thị tên tệp phù hợp với mẫu: Chúng ta có thể hiển thị các tệp có chứa chuỗi/mẫu đã cho với `-l`

```sh
grep -l "unix" *
```

Output: 

```sh
[root@linux ~]# grep -l "unix" *
geekfile.txt
tubt.txt
```

4. Kiểm tra toàn bộ các từ trong một tệp: Theo mặc định, grep khớp với chuỗi/mẫu đã cho ngay cả khi nó được tìm thấy dưới dạng chuỗi con trong một tệp. Tùy chọn `-w` cho grep làm cho nó chỉ khớp với toàn bộ từ

```sh
grep -w "unix" geekfile.txt
```

Output:

![](/linux_commands/images/grep2.png)


5. Chỉ hiển thị mẫu phù hợp: Theo mặc định, grep chỉ hiển thị toàn bộ `dòng` có chuỗi khớp. Chúng ta có làm cho grep hiển thị chuỗi phù hợp bằng cách sử dụng tùy chọn `-o`

```sh
grep -o "unix" geekfile.txt
```

Output:

```sh
[root@linux ~]# grep -o "unix" geekfile.txt
unix
unix
unix
unix
unix
```

6. Hiển thi số dòng trong khi hiển thị đầu ra bằng `grep -n`: Để hiển thị số dòng của tệp có dòng khớp

```sh
grep -n "unix" geekfile.txt
```

Output:

```sh
[root@linux ~]# grep -n "unix" geekfile.txt
1:unix is great os. unix was developed in Bell labs.
4:uNix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```

7. Đảo ngược mẫu khớp: Bạn có thể hiển thị các dòng không khớp với mẫu chuỗi tìm kiếm đã chỉ định bằng tùy chọn `-v`

```sh
grep -v "unix" geekfile.txt
```

Output:

```sh
[root@linux ~]# grep -v "unix" geekfile.txt 
learn operating system.
Unix linux which one you choose
```

8. Hiển thị các dòng khớp bắt đầu bằng một chuỗi: Mẫu biểu thức chính quy `^` chỉ định phần BẮT ĐẦU của một dòng. Điều này có thể được sử dụng trong grep để khớp với với các dòng BẮT ĐẦU bằng chuỗi hoặc mẫu đã cho

```sh
grep "^unix" geekfile.txt 
```

Output:

```sh
[root@linux ~]# grep "^unix" geekfile.txt 
unix is great os. unix was developed in Bell labs.
```

9. Hiển thị các dòng khớp kết thúc bằng một chuỗi: Mẫu biểu thức chính quy `$` chỉ định phần CUỐI CÙNG của một dòng. Điều này có thể được sử dụng trong grep để khớp với các dòng KẾT THÚC bằng chuỗi hoặc mẫu đã cho

```sh
grep "abs.$" geekfile.txt 
```

Output:

```sh
[root@linux ~]# grep "abs.$" geekfile.txt 
unix is great os. unix was developed in Bell labs.
```

10. Xử lý mẫu với biểu thức chính quy mở rộng (ERE)

```sh
grep -E '(unix|Unix) geekfile.txt'
```

Lệnh trên sẽ hiển thị các dòng chứa từ khóa `unix` hoặc `Unix` trong file `geekfile.txt`

Output:

```sh
[root@linux ~]# grep -E '(unix|Unix)' geekfile.txt
unix is great os. unix was developed in Bell labs.
Unix linux which one you choose.
uNix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```

11. In `n` dòng cụ thể từ một tệp

`-A`: In dòng tìm kiếm và n dòng sau kết quả

`-B`: In dòng tìm kiếm và n dòng trước kết quả

`-C`: In dòng tìm kiếm và n dòng sau và trước kết quả

**Cú pháp**

```sh
$grep -A[NumberOfLines(n)] [search] [file]  

$grep -B[NumberOfLines(n)] [search] [file]  

$grep -C[NumberOfLines(n)] [search] [file]  
```

**Ví dụ**

```sh
grep -A1 learn geekfile.txt
```

Output: 

```sh
[root@linux ~]# grep -A1 learn geekfile.txt
learn operating system.
Unix linux which one you choose.
uNix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```

12. Tìm kiếm đệ quy trong thư mục: `-R` in mẫu được tìm kiếm trong thư mục đã cho theo cách đệ quy trong tất cả các tệp

```sh
grep -iR unix /root/
```

Output:

```sh
[root@linux ~]# grep -iR unix /root/geeks/
/root/geeks/geekfile.txt:unix is great os. unix was developed in Bell labs.
/root/geeks/geekfile.txt:Unix linux which one you choose.
/root/geeks/geekfile.txt:uNix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```

