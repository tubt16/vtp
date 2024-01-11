# Sort command in Linux

Lệnh SORT dùng để sắp xếp một file, sắp xếp dữ liệu theo một thứ tự cụ thể. Theo mặc định, lệnh `sort` sẽ sắp xếp nội dung theo ASCII. Việc sử dụng các tùy chọn trong lệnh sắp xếp cũng có thể được sử dụng để sắp xếp theo số

- Lệnh `sort` sắp xếp nội dung của tệp văn bản theo từng dòng 

- Lệnh `Sort` là một tiện ích dòng lệnh để sắp xếp các dòng của tệp văn bản. Nó hỗ trợ sắp xếp theo thứ tự bảng chữ cái, theo thứ tự ngược lại, theo số, theo tháng...

**Lệnh sort tuân theo quy tắc dưới đây**

1. Dòng bắt đầu bằng số sẽ xuất hiện trước dòng bắt đầu bằng chữ

2. Các dòng bắt đầu bằng một chữ cái xuất hiện trước trong bảng chữ cái sẽ xuất hiện trước các dòng bắt đầu bằng một chữ cái xuất hiện sau trong bảng chữ cái.

3. Các dòng bắt đầu bằng chữ in hoa sẽ xuất hiện trước các dòng bắt đầu bằng chữ cái tương tự đối với chữ thường

Ví du:

Tạo một tệp `file.txt` có dữ liệu như sau

```sh
[root@tubt ~]# cat file.txt 
abhishek
chitransh
satish
rajan
naveen
divyam
harsh
```

1. Sử dụng lệnh sắp xếp

Syntax:

```sh
[root@tubt ~]# sort file.txt 
abhishek
chitransh
divyam
harsh
naveen
rajan
satish
```

2. Sẵp xếp với tệp trộn, tức là chữ hoa và chữ thường. Khi chúng ta có một tệp trộn có cả chữ hoa và thường thì trước tiên các chữ viết thường sẽ được sắp xếp trước chữ viết hoa

```sh
[root@tubt ~]# cat mix.txt 
abc
apple
BALL
Abc
bat
[root@tubt ~]# sort mix.txt 
abc
Abc
apple
BALL
bat
```

**Các tùy chọn sử dụng với lệnh `sort`**

1. `-o`: Linux cũng cung cấp cho chúng ta các tiện ích đặc biệt, như nếu bạn muốn ghi đầu ra vào một tệp mới `out.txt`, bạn có thể sử dụng tùy chọn `-o`

Ví dụ:

```sh
[root@tubt ~]# sort file.txt > out.txt
[root@tubt ~]# cat out.txt 
abhishek
chitransh
divyam
harsh
naveen
rajan
satish
```

2. `-r`: Tùy chọn này sẽ đảo ngược thứ tự sắp xếp 

```sh
[root@tubt ~]# sort -r file.txt 
satish
rajan
naveen
harsh
divyam
chitransh
abhishek
```

3. `-n`: Tùy chọn này để sắp xếp tệp có dữ liệu số bên trong

```sh
[root@tubt ~]# cat file1.txt 
50
39
15
89
200
[root@tubt ~]# sort -n file1.txt 
15
39
50
89
200
```

4. `-k`: Tùy chọn này cung cấp tính năng sắp xếp trên số cột bất kỳ 

Ví dụ: Sử dụng `-k 2` để sắp xếp cột thứ hai

Hãy tạo một file có 2 cột

```sh
[root@tubt ~]# cat employee.txt 
manager  5000
clerk    4000
employee  6000
peon     4500
director 9000
guard     3000

[root@tubt ~]# sort -k 2 employee.txt 
guard     3000
clerk    4000
peon     4500
manager  5000
employee  6000
director 9000
```

5. `-c`: Tùy chọn này được sử dụng để kiểm tra xem tệp đã được sắp xếp hay chưa 

Ví dụ: 

Tạo một tệp mới

```sh
[root@tubt ~]# cat car.txt 
Audi
Cadillac
BMW
Dodge

[root@tubt ~]# sort -c car.txt 
sort: car.txt:3: disorder: BMW
```

6. `-u`: Sẵp xếp và loại bỏ các bản sao

```sh
[root@tubt ~]# cat car1.txt 
Audi
BMW
Cadillac
BMW
Dodge
Audi

[root@tubt ~]# sort -u car1.txt 
Audi
BMW
Cadillac
Dodge
```

