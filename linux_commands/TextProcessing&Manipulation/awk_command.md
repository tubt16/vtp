# Awk command in Linux

Awk là một tiện ích để quét và xử lý mẫu. Nó tìm kiếm một hoặc nhiều tệp để xem liệu chúng có chứa các dòng khớp với các đã chỉ định hay không

**Hoạt động của Awk**

- Quét từng dòng từng tệp

- Chia mỗi dòng đầu thành các trường

- So sánh dòng/trường đầu vào với mẫu

- Thực hiện các hành động trên các dòng phù hợp

**Syntax:**

```sh
awk options 'selection _criteria {action }' input-file > output-file
```

**Options**

- `-f` - (program-file): Đọc nguồn chương trình AWK từ tệp thay vì từ đối số dòng đầu tiên

- `-F` - fs: Sử dụng fs cho dấu phần cách trường đầu vào

**Các ví dụ**

```sh
[root@tubt ~]# cat employee.txt 
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000
```

**1. Hành vi mặc định của `awk`: Theo mặc định, `awk` in mọi dòng dữ liệu từ tệp được chỉ định**

```sh
awk '{print}' employee.txt
```

Output: 

```sh
[root@tubt ~]# awk '{print}' employee.txt
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000 
```

Trong ví dụ trên, không có mẫu nào được đưa ra. Vì vậy, các hành động có thể áp dụng cho tất cả các dòng. Hành động `print` không có bất kỳ đối số nào sẽ in toàn bộ dòng theo mặc định

**2. In các dòng phù hợp với mẫu đã cho**

```sh
awk '/manager/ {print}' employee.txt 
```

Output:

```sh
[root@tubt ~]# awk '/manager/ {print}' employee.txt 
ajay manager account 45000
varun manager sales 50000
amit manager account 47000
```

Trong ví dụ này, lệnh `awk` in tất cả các dòng có từ khóa `manager`

**3. Tách một dòng thành các trường:**

Đối với mỗi bản ghi, tức là dòng, lệnh `awk` sẽ CHIA TÁCH bản ghi được phân cách bằng ký tự KHOẢNG TRẮNG theo mặc định và lưu trữ nó trong các biến `$n`, Nếu dòng có 4 từ, nó sẽ được lưu lần lượt trong `$1`, `$2`, `$3`, `$4`. Ngoài ra `$0` đại diện cho toàn bộ dòng 

```sh
awk '{print $1,$4}' employee.txt 
```

Outout:

```sh
[root@tubt ~]# awk '{print $1,$4}' employee.txt 
ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000
```

Trong ví dụ trên `$1` và `$4` lần lượt đại diện cho các trường `Tên` và `Lương`

**Các biến tích hợp trong `awk`**

Các biến tích hợp của Awk bao gồm các biến trường `$1` `$2` `$3` ... (`$0` là toàn bộ dòng) - Chia một dòng văn bản thành các từ hoặc phần riêng lẻ được gọi là TRƯỜNG

- `NR`: Lệnh `NR` giữ số lượng bản ghi đầu vào hiện tại và hiển thị số thứ tự của dòng cho mỗi dòng. Hãy nhớ rằng các bản ghi thường là dòng. Lệnh Awk thực hiện các câu lệnh mẫu/hành động một lần cho mỗi bản ghi trong một tệp.

- `NF`: Lệnh `NF` giữ số lượng trường trong bản ghi đầu vào hiện tại. Và in trường cuối cùng

- `FS`: Lệnh `FS` chứa ký tự phân cách trường dùng để PHÂN CHIA các trường trên dòng đầu vào. Mặc định là “KHOẢNG TRẮNG”, nghĩa là ký tự DẤU CÁCH và TAB. `FS` có thể được gán lại cho một ký tự khác (thường là trong BEGIN) để thay đổi dấu phân cách trường

- `RS`: Lệnh `RS` lưu trữ ký tự phân tách bản ghi hiện tại. Vì theo mặc định, dòng đầu vào là bản ghi đầu vào nên ký tự phân tách bản ghi mặc định là dòng mới.

- `OFS`: Lệnh `OFS` lưu trữ dấu phân cách trường đầu ra, phân tách các trường khi `awk` in chúng. Mặc định là một khoảng trống. Bất cứ khi nào bản in có một số tham số được phân tách bằng dấu phẩy, nó sẽ in giá trị `OFS` ở giữa mỗi tham số.

- `ORS`: Lệnh `ORS` lưu trữ dấu tách bản ghi đầu ra, ngăn cách các dòng đầu ra khi `awk` in chúng. Mặc định là ký tự dòng mới. print tự động xuất nội dung của `ORS` ở cuối nội dung được in.

**Các ví dụ với các biến trong `awk`**

**1. Sử dụng biến tích hợp `NR` (Số dòng hiển thị)**

```sh
awk '{print NR,$0}' employee.txt 
```

Output:

```sh
[root@tubt ~]# awk '{print NR,$0}' employee.txt 
1 ajay manager account 45000
2 sunil clerk account 25000
3 varun manager sales 50000
4 amit manager account 47000
5 tarun peon sales 15000
6 deepak clerk sales 23000
7 sunil peon sales 13000
8 satvik director purchase 80000 
```

Trong ví dụ trên, lệnh `awk` với `NR` in tất cả các dòng cùng với số dòng

Một cách sử dụng khác của biến `NR` (Hiển thị từ dòng 3 đến 6)

```sh
awk 'NR==3, NR==6 {print NR,$0}' employee.txt 
```

Output:

```sh
[root@tubt ~]# awk 'NR==3, NR==6 {print NR,$0}' employee.txt 
3 varun manager sales 50000
4 amit manager account 47000
5 tarun peon sales 15000
6 deepak clerk sales 23000
```

**2. Sử dụng biến tích hợp `NF` (Hiển thị trường cuối cùng)**

```sh
awk '{print $1,$NF}' employee.txt
```

Output:

```sh
[root@tubt ~]# awk '{print $1,$NF}' employee.txt
ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000
```

Trong ví dụ trên `$1` đại diện cho `Tên` và `$NF` đại diện cho `Mức lương`. Chúng ta có thể lấy giá trị `Mức lương` bằng cách sử dụng `$NF`, trong đó `$NF` đại diện cho trường cuối cùng

**Thêm ví dụ**

Tạo một tệp khác có tên `myfile.txt`

```sh
[root@tubt ~]# cat myfile.txt 
A    B    C
Tarun    A12    1
Man    B6    2
Praveen    M42    3
```

**1. Để in trường thứ 2 cùng với số hàng (NR) được phân tách bằng dấu "-" từ mỗi dòng trong `myfile.txt`**

```sh
awk '{print NR " - " $2 }' myfile.txt
```

Output:

```sh
[root@tubt ~]# awk '{print NR " - " $2 }' myfile.txt
1 - B
2 - A12
3 - B6
4 - M42
```

**2. Để trả về cột/trường thứ 2 từ `myfile.txt`**

```sh
awk '{print $2}' myfile.txt
```

Output:

```sh
[root@tubt ~]# awk '{print $2}' myfile.txt
B
A12
B6
M42
```

**3. Tìm độ dài của dòng dài nhất có trong tệp**

```sh
awk '{ if (length($0) > max) max = length($0) } END { print max }' myfile.txt
```

Output:

```sh
[root@tubt ~]# awk '{ if (length($0) > max) max = length($0) } END { print max }' myfile.txt
19
```

**4. Đếm các dòng trong một tập tin**

```sh
awk 'END { print NR }' myfile.txt
```

Output:

```sh
[root@tubt ~]# awk 'END { print NR }' myfile.txt
4
```

**5. In các dòng có hơn 15 ký tự**

```sh
awk 'length($0) > 15' myfile.txt
```

Output:

```sh
[root@tubt ~]# awk 'length($0) > 15' myfile.txt
Tarun    A12    1
Praveen    M42    3
```