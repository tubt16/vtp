# Find command in Linux

Lệnh `find` trong Linux là một tiện ích dòng lệnh để duyệt hệ thống phân cấp tệp. Nó có thể được sử dụng để tìm các tập tin và thư mục và thực hiện các thao tác tiếp theo trên chúng

Nó hỗ trợ tìm kiếm theo tập tin, ngày tạo, ngày sửa đổi, chủ sở hữu và phân quyền. Bằng cách sử dụng `-exec`, các lệnh Linux khác có thể được thực thi trên các tệp hoặc thư mục được tìm thấy

**Cú pháp**

```sh
find [where to start searching from] [expression determines what to find] [-options] [what to find]
```

**Các tùy chọn**

- `exec CMD`: Tệp đang được tìm kiếm đáp ứng các tiêu chí trên và trả về 0 làm exit code để thực thi lệnh thành công

- `ok CMD`: Nó hoạt động tương tự như `-exec` ngoại trừ việc người dùng được nhắc trước

- `-inum N`: Tìm kiếm các file có số lượng inode `N`

- `-links N`: Tìm kiếm các file có liên kết `N`

- `-name demo`: Tìm kiếm các file có tên `demo`

- `-newer tubt`: Tìm kiếm các tệp được sửa đổi/tạo sau tệp có tên là `tubt`

- `-perm octal`: Tìm kiếm tệp nếu quyền là `bát phân`

- `-print`: Hiển thị tên đường dẫn của các tệp được tìm thấy bằng cách sử dụng các tiêu chí còn lại

- `-empty`: Tìm kiếm các tập tin và thư mục trống

- `-user name`: Tìm kiếm các tập tin thuộc sở hữu của tên người dùng hoặc ID

- `\(expr)\`: Đúng nếu `expr` là ĐÚNG được sử dụng để nhóm các tiêu chí kết hợp với OR hoặc AND

- `!expr`: Đúng nếu `expr` là SAI

# Ví dụ

1. Tìm kiếm một tập tin cụ thể

```sh
[root@linux ~]# find /root/ -name geekfile.txt
/root/geekfile.txt
/root/geeks/geekfile.txt
```

2. Tìm kiếm tệp có đuôi `.txt`

```sh
[root@linux ~]# find /root/ -name "*.txt"
/root/geekfile.txt
/root/tubt.txt
/root/pattern.txt
/root/geeks/tu/geekfile.txt
```

3. Tìm và xóa một tập tin có xác nhận

```sh
find /root/ -name tubt.txt -exec rm -i {} \;
```

Khi lệnh này được nhập, một dấu nhắc sẽ xuất hiện để xác nhận xem bạn có muốn xóa file `tubt.txt` hay không. Nếu bạn nhập `y/yes` nó sẽ xóa tập tin

Output:

```sh
[root@linux ~]# ls
geekfile.txt  geeks  pattern.txt  tubt.txt

[root@linux ~]# find /root/ -name tubt.txt -exec rm -i {} \;
rm: remove regular empty file ‘/root/tubt.txt’? yes

[root@linux ~]# ls
geekfile.txt  geeks  pattern.txt
```

4. Tìm kiếm các tập tin và thư mục trống

```sh
find /root -empty
```

Output:

```sh
[root@linux ~]# find /root/ -empty
/root/.pki/nssdb
/root/tu.txt
/root/tubt
```

5. Tìm kiếm tập tin với quyền đã chỉ định

```sh
find /root -perm 644
```

Output:

```sh
[root@linux ~]# find /root/ -perm 644
/root/.bash_logout
/root/.bash_profile
/root/.bashrc
/root/.cshrc
/root/.tcshrc
/root/geekfile.txt
/root/pattern.txt
/root/geeks/tu/geekfile.txt
/root/tu.txt
```

6. Tìm kiếm tất cả các thư mục và thư mục con

```sh
find /root/ -type d
```

Output:

```sh
[root@linux ~]# find /root/ -type d
/root/
/root/.pki
/root/.pki/nssdb
/root/geeks
/root/geeks/tu
/root/tubt
```

7. Tìm kiếm văn bản trong nhiều tập tin

```sh
find /root/ -type f -name "*.txt" -exec grep -in 'unix' {} \;
```

Output:

```sh
[root@linux ~]# find /root/ -type f -name "*.txt" -exec grep -in 'unix' {} \;
1:unix is great os. unix was developed in Bell labs.
3:Unix linux which one you choose.
4:uNix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
1:unix is great os. unix was developed in Bell labs.
3:Unix linux which one you choose.
4:uNix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```