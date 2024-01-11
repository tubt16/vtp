# rm command in Linux 

Lệnh `rm` là viết tắt của remove. Lệnh rm được sử dụng để xóa các đối tượng như tệp, thư mục liên kết tượng trưng... khỏi hệ thống. Nói chính xác hơn, `rm` loại bỏ các tham chiếu đến các đối tượng khỏi hệ thống tệp, trong đó các đối tượng đó có thể có nhiều tham chiếu(Ví dụ: một tệp có hai tên khác nhau)

**Cú pháp**

```sh
rm [OPTION]... FILE...
```

Chúng ta cùng xem xét 5 tệp `a.txt`, `b.txt`, `c.txt`, `d.txt`, `e.txt`

```sh
[root@linux mnt]# ls
a.txt  b.txt  c.txt  d.txt  e.txt
```

```sh
[root@linux mnt]# rm a.txt b.txt 
rm: remove regular empty file ‘a.txt’? y
rm: remove regular empty file ‘b.txt’? y
[root@linux mnt]# ls
c.txt  d.txt  e.txt
```

**Force deletetion**

Khi xóa một file, hệ thống sẽ nhắc nhở trước khi xóa. Ta sử dụng option `-f` để bỏ qua và xóa luôn mà không cần hỏi trước

```sh
[root@linux mnt]# ls
c.txt  d.txt  e.txt
[root@linux mnt]# rm -f c.txt d.txt 
[root@linux mnt]# ls
e.txt
```

**Recursive Deletion**

Xóa đệ quy, Với tùy chọn `-r`, lệnh `rm` thực hiện xóa tất cả các tệp và thư mục con theo cách đệ quy của thư mục cha. 

```sh
[root@linux mnt]# ls
tubt
[root@linux mnt]# cd tubt/
[root@linux tubt]# ls
tubui
[root@linux tubt]# cd tubui/
[root@linux tubui]# ls
tubt1.txt  tubt2.txt  tubt3.txt  tubt4.txt
[root@linux tubui]# cd /mnt/
[root@linux mnt]# rm tubt/
rm: cannot remove ‘tubt/’: Is a directory
[root@linux mnt]# rm -rf tubt/
[root@linux mnt]# ls
```

