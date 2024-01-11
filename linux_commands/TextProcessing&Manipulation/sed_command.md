Một lệnh sử dụng để chính sửa luồng rất mạnh mẽ có thể xử lý và thực hiện các hành động phức tạp trên luồng văn bản

File ví dụ:

```sh
[root@hanode1 ~]# cat geekfile.txt 
unix is great os. unix is opensource. unix is free os.
learn operating system.
unix linux which one you choose.
unix is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```

1. Thay thế hoặc thay thế chuỗi: Lệnh sed chủ yếu được sử dụng để thay thế văn bản trong mộ tệp. Lệnh `sed` dưới đây thay thế từ "unix" đầu tiên của 1 dòng thành "linux" trong tệp

```sh
[root@hanode1 ~]# sed 's/unix/linux/' geekfile.txt 
linux is great os. unix is opensource. unix is free os.
learn operating system.
linux linux which one you choose.
linux is easy to learn.unix is a multiuser os.Learn unix .unix is a powerful.
```

Ở đây `s` chỉ định thao tác thay thế `/` là dấu phân cách, `unix` là mẫu tìm kiếm và `linux` là chuỗi thay thế

Theo mặc định, lệnh `sed` thay thế lần xuất hiện đầu tiên của mẫu trong mỗi dòng và nó sẽ không thay thế lần xuất hiện thứ 2, thứ 3 ... trong dòng

2. Thay thế lần xuất hiện lần thứ n của mẫu trong một dòng. Sử dụng `/1`, `/2` để thay thế lần xuất hiện đầu tiên, thứ hai của mẫu trong một dòng. Lệnh dưới đây thay thế lần xuất hiện thứ hai của từ `unix` thành `linux` trong một dòng

```sh
[root@hanode1 ~]# sed 's/unix/linux/2' geekfile.txt 
unix is great os. linux is opensource. unix is free os.
learn operating system.
unix linux which one you choose.
unix is easy to learn.linux is a multiuser os.Learn unix .unix is a powerful.
```

3. Thay thế tất cả sự xuất hiện trong một dòng. Option thay thế `/g` (global) chỉ định lệnh `sed` để thay thế tất cả các lần xuất hiện của chuỗi trong dòng

```sh
[root@hanode1 ~]# sed 's/unix/linux/g' geekfile.txt 
linux is great os. linux is opensource. linux is free os.
learn operating system.
linux linux which one you choose.
linux is easy to learn.linux is a multiuser os.Learn linux .linux is a powerful.
```

4. Thêm dấu ngoặc đơn vào ký tự đầu tiên của mỗi từ. Ví dụ, lệnh `sed` này in ký tự đầu tiên của mỗi từ trong ngoặc đơn

```sh
[root@hanode1 ~]# echo "Welcome To The Geek Stuff" | sed 's/\(\b[A-Z]\)/\(\1\)/g'
(W)elcome (T)o (T)he (G)eek (S)tuff
```