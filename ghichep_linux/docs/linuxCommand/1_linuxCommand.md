# Làm việc trên dòng lệnh (Shell sourcing và các ký tự đặc biệt)

**Bash** 

Shell linux mặc định được sử dụng diễn giải các lệnh và kịch bản (script) trong hệ thống Linux

Các shell khác: ash, c-shell, ksh, zsh

Các shell đặc biệt 

- /bin/false, /etc/nologin (cảnh báo - Điều quan trọng cần nhớ là /bin/false và /etc/nologin không tồn tại theo mặc định trong hệ thống Linux) Tuy nhiên bạn có thể tạo file này và cấu hình hệ thống để ngăn người dùng thường đăng nhập vào Linux

Thực thi kịch bản (script)

- Bash đọc nội dung của file kịch bản được chỉ định và nếu các quyền thích hợp được thiết lập, các lệnh bên trong nó được thực thi một cách tuần tự (giống như bạn gõ trên dòng lệnh bash shell) nhưng trong một shell mới

- Bất kỳ biến nào được thiết lập trong không gian của shell trong quá trình thực thi kịch bản sẽ bị mất (gọi là `ra khỏi phạm vi`) sau khi kịch bản hoàn tất và trở lại dấu nhắc lệnh

Ví dụ `./myscript.sh`

- Sẽ thực thi kịch bản `myscript.sh` từ thư mục làm việc hiện tại

**Sourcing kịch bản (script)**

- Bash đọc nội dung của file kịch bản được chỉ định và nếu các quyền thích hợp được thiết lập, các lệnh bên trong nó được thực thi một cách tuần tự (giống như bạn gõ các câu lệnh trên dòng lệnh), nhưng trong môi trường shell `hiện tại`

- Cho phép giữ nguyên tất cả các thiết lập trong shell đó (ví dụ: biến môi trường) sau khi kịch bản hoàn thành 

**/etc/profile**

- Tập lệnh cho toàn bộ hệ thống Linux, có tác động ảnh hưởng đến môi trường của mỗi người dùng (miễn là họ sử dụng bash shell)

- Đó là tập lệnh `được source` và được thực thi mỗi khi người dùng đăng nhập (login) thông qua một shell

**/etc/bashrc**

- Đây là một tập lệnh cấu hình cho toàn bộ hệ thống Linux, ảnh hưởng đến môi trường của mỗi người dùng (miễn là họ sử dụng shell bash)

- Đây là một tập lệnh `được source` và thực thi mỗi khi người dùng đăng nhập thông qua một shell đăng nhập HOẶC khi họ thực thi một phiên không đăng nhập (xem bên dưới)

**/.bash_profile**

- Đây là một tập lệnh `được source` khác được thực thi khi người dùng đăng nhập thông qua một shell đăng nhập, nhưng chỉ ảnh hưởng đến môi trường của người dùng đăng nhập (nó nằm trong thư mục `/home` của mỗi người dùng, được chỉ định bằng ký tự viết tắt `~` trong đường dẫn)

**/.bashrc**

- Đây là một tập lệnh `được source` khác, thường được gọi bởi tập lệnh `/.bash_profile`

- Nếu có, nó sẽ được sử dụng để `source` tập lệnh `/etc/bashrc`

- Thông thường được sử dụng để tùy chỉnh giao diện dòng lệnh, bí danh (alias)...

**~/.bash_logout**

- Đây là một tập lệnh 'được source' khác, được thực thi khi lệnh logout hoặc exit được thực hiện

## Ví dụ về thứ tự đăng nhập vào Linux của user

1. Người dùng đăng nhập.
2. /etc/profile (được source).
3. ~/.bash_profile của người dùng (được source).
4. ~/.bashrc của người dùng (được source từ ~/.bash_profile).
5. Người dùng thực hiện công việc của họ theo nhu cầu sử dụng.
6. Người dùng đăng xuất bằng lệnh logout hoặc exit.
7. ~/.bash_logout của người dùng (được source)

Phiên `không đăng nhập`(Non-login session)

- Khi người dùng root hoặc người dùng khác root sử dụng su để trở thành người dùng khác (hoặc người dùng root), mặc định không tải toàn bộ biến môi trường của người dùng đó

## Thực hiện các thiết đặt môi trường 

Các ký tự đặc biệt 

- `~` Thư mục gốc của người dùng (ví dụ `/home/user`)

- `\` Ký tự thoát

- `$` Xác định một biến

- `?` Ký tự đại diện cho một ký tự duy nhất

- `*` Ký tự đại diện cho 0 đến n ký tự

- `&` Chuyển một tiến trình vào chế độ chạy nền background

- `&&` Thực thi lệnh thứ hai chỉ khi lệnh đầu tiên thành công (Ví dụ - `/bin/true && echo 'It Works'`)

- `|` Đường ống (pipeline), dùng để chuyển đầu ra của lệnh sang lệnh khác

- `||` Thực thi lệnh thứ hai chỉ khi lệnh đầu tiên không thành công (Ví dụ - `/bin/false && echo 'Got here'`)

- `;` Thực thi nhiều lệnh trên cùng một dòng

- `[]` Xác định một phạm vi ký tự (số hoặc chữ)

- `>` Chuyển hướng đầu ra chuẩn (redirect standard) vào một tập file

- `<` Chuyển hướng đầu vào chuẩn (standard input) từ một chương trình

Mã thoát lệnh 

- Mỗi lần thực thi thành công hoặc thất bại và cung cấp một mã thoát lệnh bạn có thể xem sau đó

- `echo $?` (0 cho thành công, 1 cho thất bại)

# Các biến môi trường, hiển thị, thiết lập và sử dụng

**env**

Lệnh để liệt kê tất cả các biến môi trường được thiết lập cho phiên làm việc hiện tại TRỪ các thiết lập của shell

**set**

Dùng để xem các thiết lập của shell hoặc biến shell nào cho phiên làm việc 

Có thể dùng để bật tắt các tùy chọn shell

- `-o` - ON (bật) tùy chọn

- `+o` - OFF (tắt) tùy chọn

Các tùy chọn có sẵn:

- vi hoặc emacs - kiểu bàn phím cho dòng lệnh

- hashall - mặc định BẬT, cho phép bảng băm lệnh và vị trí được sử dụng lặp lại

- history - mặc định BẬT, cho phép đọc HISFILE đê tìm file lịch sử (xem bên dưới)

- monitor - chạy các tiến trình nền trong một nhóm khác và thông báo cho console khi chúng hoàn thành

- noclobber - mặc định TẮT, không cho phép chuyển hướng `>` ghi đè lên một file đã tồn tại

- noexec - mặc định TẮT, các files kịch bản (script) sẽ chạy kiểm tra cú pháp khi bật trên tất cả các lệnh khi chạy

- notify - công việc kết thúc thông báo ngay lập tức trên console thay vì trong lần thực thi tiếp theo của lệnh `job`

- verbose - hiển thị lệnh ra terminal/màn hình trước khi chúng được thực thi

**shopt** 

Dùng để xem bất kỳ thiết lập của shell hoặc biến shell nào cho phiên làm việc

**PATH**

Mọi biên môi trường chứa danh sách các thư mục được phân tách bằng dấu `:` được tìm kiếm (theo thứ tự) để tìm các file thực thi lệnh (nghĩa là các file có quyền thực thi)

**HISTFILE**

Lệnh `history` sử dụng giá trị này để hiển thị danh sách các lệnh đã chạy trước đó

Theo mặc định, giá trị của nó cho bất kỳ người dùng nào sẽ là `/home/user/.bash_history`

Các biến điều khiển việc sử dụng lịch sử của bash shell là:

- HISTCMD - chỉ mục của lệnh hiện tại

- HISTCONTROL - khi được thiết lập thành `ignorespace`, bất kỳ lệnh nào đi trước bởi một khoảng trắng sẽ KHÔNG được ghi lại trong file lịch sử, khi được thiết lập thành `ignoredups`, hai dòng liên tiếp giống nhau sẽ có một dòng bị bỏ qua

- HISTFILESIZE - số dòng có thể chứa các lệnh trước đó (mặc định là 500)

**Thay đổi biến môi trường**

Tất cả các biến có thể được thay đổi theo hai cách

1. Ghi đè (export VARIABLE=newValue)

2. Thêm vào (export VARIABLE=$VARIABLE:newValue)

- `echo [$ + ten_bien]` - sẽ hiển thị giá trị hiện tại

Ví dụ: 

```sh
echo $HOME		#Sẽ hiển thị thư mục gốc của người dùng hiện tại 
```

Ví dụ:

```sh
cd $HOME		# Sẽ đổi thư mục hiện tại của shell thành thư mục gốc của người dùng hiện tại
```

# Xử lý luồng văn bản bằng cách lệnh bộ lọc (Sort, nl, wc, expand, cut, paste, join, uniq, head và tail)

**sort**

Sẽ sắp xếp (theo thứ tự số hoặc chữ cái, mặc định bắt đầu từ cột 0) mỗi dòng trong file sẽ được chỉ định

`sort [ten_file]` - hiển thị một sắp xếp mặc định của mỗi dòng (từ trên xuống dưới) lên trên màn hình

Ví dụ:

```sh
[root@hanode1 ~]# cat tubt.txt 
a
n
c
b
t
q
u
[root@hanode1 ~]# sort tubt.txt 
a
b
c
n
q
t
u
```

`sort -r [ten_file]` - sắp xếp theo thứ tự ngược

Ví dụ:

```sh
[root@hanode1 ~]# cat tubt.txt 
a
n
c
b
t
q
u
[root@hanode1 ~]# sort -r tubt.txt 
u
t
q
n
c
b
a
```

`sort -n [ten-file]`: Săpx xếp file theo thứ tự số

Ví dụ:

```sh
[root@hanode1 ~]# cat file1.txt 
50
39
15
89
200
[root@hanode1 ~]# sort -n file1.txt 
15
39
50
89
200
```

`sort -k[#] [ten_file]`: Thực hiện sắp xếp cột bất kỳ được cung cấp trong option `#`

Ví dụ: 

```sh
[root@hanode1 ~]# cat employ.txt 
manager  5000
clerk    4000
employee  6000
peon     4500
director 9000
guard     3000
[root@hanode1 ~]# sort -k 2 employ.txt 
guard     3000
clerk    4000
peon     4500
manager  5000
employee  6000
director 9000
[root@hanode1 ~]# sort -k 1 employ.txt 
clerk    4000
director 9000
employee  6000
guard     3000
manager  5000
peon     4500
```

**nl**

Đánh số dòng trong một file (hoặc luồng đầu vào), có thể là tất cả các dòng hoặc các dòng có dữ liệu

`nl [ten_file]` - sẽ đánh số tất cả các dòng có dữ liệu (mặc định)

`nl -ba [ten_file]` - sẽ đánh số tất cả các dòng kể cả có dòng trống

Ví dụ: 

```sh
[root@hanode1 ~]# cat file2.txt 


r

t

a

n

t
[root@hanode1 ~]# nl file2.txt 
       
       
     1  r
       
     2  t
       
     3  a
       
     4  n
       
     5  t
[root@hanode1 ~]# nl -ba file2.txt 
     1
     2
     3  r
     4
     5  t
     6
     7  a
     8
     9  n
    10
    11  t
```

**wc**

Từ viết tắt của `word count`, nhưng có thể làm nhiều hơn thế

`-l` -số dòng 

`-w` - số từ

`-c` - số ký tự (byte)

Ví dụ: 

```sh
[root@hanode1 ~]# cat employ.txt 
manager  5000
clerk    4000
employee  6000
peon     4500
director 9000
guard     3000
[root@hanode1 ~]# wc -l employ.txt 
6 employ.txt
[root@hanode1 ~]# wc -w employ.txt 
12 employ.txt
[root@hanode1 ~]# wc -c employ.txt 
86 employ.txt
```

Được sử dụng như một bổ sung đầu ra cho lệnh khác

Ví dụ:

```sh
cat /etc/hosts | wc -l
```

Lệnh này sẽ hiển thị nội dung của file `/etc/hosts`, lọc nó qua lệnh `wc` và hiển thị số dòng trong file

output:

```sh
[root@hanode1 ~]# cat /etc/hosts | wc -l
7
```

**expand**

Chuyển đổi các tab trong một file thành một số ký tự dấu cách cụ thể

`-t [#]` - chuyển đổi các tab thành # số dấu cách đã bị chỉ định

```sh
[root@hanode1 ~]# cat expand.txt 
        2
6
                3

4
  0
[root@hanode1 ~]# expand -t 2 expand.txt 
  2
6
    3

4
  0
```

**cut**

Lệnh cho phép trích xuất dữ liệu trường hoặc cột từ một vị trí cụ thể trong file được chỉ định

File ví dụ: 

```sh
[root@hanode1 ~]# cat state.txt 
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
```

`cut -b [#],[#],[#] [file_name]`: Trích xuất các byte cụ thể với danh sách các số byte được phân tách bằng dấu `,`

Ví dụ: 

```sh
# List without ranges

[root@hanode1 ~]# cut -b 1,2,3 state.txt
And
Aru
Ass
Bih
Chh

# List with ranges

[root@hanode1 ~]# cut -b 1-3,5-7 state.txt
Andra 
Aruach
Assm
Bihr
Chhtti

# '1-' bieu thi tu byte thu 1 den cuoi dong

[root@hanode1 ~]# cut -b 1- state.txt
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh

# '-3' bieu thi tu byte thu 1 den byte thu 3 cua dong

[root@hanode1 ~]# cut -b -3 state.txt
And
Aru
Ass
Bih
Chh
```


`cut -c [#],[#] [file_name]` - Để cắt theo ký tự, hãy sử dụng tùy chọn `-c`. Đây có thể là danh sách các số được phân tách bằng dấu phẩy hoặc một dãy số được phân cách bằng dấu `-` 

Ví dụ: 

```sh
# Lay ky tu thu 2, thu 5 va thu 7 tu moi dong cua tep

[root@hanode1 ~]# cut -c 2,5,7 state.txt
nr 
rah
sm
ir
hti

# In 7 ky tu dau tien cua moi dong trong tep

[root@hanode1 ~]# cut -c 1-7 state.txt
Andhra 
Arunach
Assam
Bihar
Chhatti

# Cat cac ky tu tu` dau den cuoi file

[root@hanode1 ~]# cut -c 1- state.txt 
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh

# Cat cac ky tu tu` dau den ky tu thu 5

[root@hanode1 ~]# cut -c -5 state.txt 
Andhr
Aruna
Assam
Bihar
Chhat
```

`cut -f (field_number) [file_name]`: Xác định số trường (được xác định bằng ký tự phân cách) dể hiển thị từ file được chỉ định

Ví dụ:

```sh
# Giống như trong tệp 'state.txt', các trường được phân tách bằng dấu cách nếu tùy chọn '-d' không được sử dụng thì nó sẽ in toàn bộ dòng

[root@hanode1 ~]# cut -f 2 state.txt 
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh

# Nếu tùy chọn '-d' được sử dụng thì nó sẽ coi khoảng trắng là dấu phân tách trường hoặc dấu phân cách

[root@hanode1 ~]# cut -d " " -f 2 state.txt 
Pradesh
Pradesh
Assam
Bihar
Chhattisgarh

# In ra trường đâu tiên đến trường cuối cùng của mỗi dòng

[root@hanode1 ~]# cut -d " " -f 1-3 state.txt
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
```

**paste**

Kết hợp hai files lại với nhau mà không loại bỏ bất kỳ dữ liệu nào (phong cách nối tiếp)

**join**

Kết hợp hai file lại với nhau nhưng loại bỏ các trường lặp lại (giống với cơ sở dữ liệu) - dựa trên trường đầu tiên (trường khóa)

`join -t[character]` - sử dụng ký tự được chỉ định làm bộ phân cách trường (ký tự phân cách)

**head**

Tương tự như lệnh `cat` vì nó sẽ hiển thị nội dung của một file nhưng chỉ hiển thị một số dòng nhất định từ đầu của file đó (mặc định là 10 dòng đầu)

`head -n [#] [file_name]`: Hiển thị 'n' dòng, bắt đầu từ dòng đầu của tệp được chỉ định

```sh
[root@hanode1 ~]# head -n 2 state.txt 
Andhra Pradesh
Arunachal Pradesh
```

**tail**

Đối lập với lệnh `head`, chỉ hiện thị một số dòng nhất định từ cuối file (mặc định là 10)

`tail -n [#] [file_name]`: Hiển thị 'n' dòng, bắt đầu từ dòng cuối của tệp được chỉ định

`tail -f [file_name]`: Hiển thị 10 dòng cuối file được chỉ định và sau đó sẽ `theo dõi` đầu ra của file theo `thời gian thực`, giúp có thể theo dõi xem các giá trị bổ sung được ghi vào file

`tail` thường được sử dụng thường xuyên để kiểm tra log

# Xử lý luồng văn bản bằng các bộ lọc part 2 (split, cat, od, fmt, tr, sed)

**split**

Cho phép bạn chia một file thành nhiều file khác có chứa `phần` dữ liệu của file gốc

`split -l [#] [file_name]`: Chia một file thành 2 file mới, 2 file mới ngăn cách bởi số dòng được chỉ định

Ví dụ: 

```sh
[root@hanode1 ~]# split -l 4 state.txt split_file.txt

[root@hanode1 ~]# cat split_file.txtaa 
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar

[root@hanode1 ~]# cat split_file.txtab 
Chhattisgarh
```

**cat**

Hiển thị nội dung của một file từ đầu đến cuối trên đầu ra tiêu chuẩn

**od**

Cho phép hiển thị nội dung của một file nhị phân trên `đầu ra/terminal` tiêu chuẩn 

- `-a` - hiển thị file nhị phân 

- `-d` - định dạng thập phân

- `-f` - định dạng số chấm động

- `-o` - định dạng bát phân 

- `-x` - định dạng thập lục phân

**sed**

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

# Quản lý file cơ bản (ls, cd, pwd, mkdir, file, globbing, touch, stat, cp và mv)

**ls**

Liệt kê thư mục, files hoặc cả hai

- `-l`: Liệt kê chi tiết, bao gồm quyền truy cập, chủ sở hữu, kích cỡ và ngày/giờ tạo và sửa file

- `-a`: Liệt kê file, bao gồm cả file 'ẩn' (file bắt đầu bằng dấu `.` Ví dụ `.bashrc`)

- `-d`: Chỉ liệt kê số inode cho file hoặc thư mục

- `-i`: Hiển thị số inode cho file hoặc thư mục

- `-h`: Thêm định dạng dễ đọc cho kích thước và chi tiết của file

**cd**

Thay đổi thư mục làm việc

Có thể sử dụng đường dẫn tuyệt đối, đường dẫn tương đối hoặc giá trị trong biến làm phần của đường dẫn

- `cd .`: Một tham chiếu đến thư mục hiện tại

- `cd ..`: Di chuyển lên một thư mục

- `cd ../../mydir`: Di chuyển lên hai thư mục trong cây thư mục và vào thư mục `mydir` (nếu tồn tại)

**pwd**

Hiện thị thư mục hiện tại mà bạn đang ở trong đó

**mkdir**

Tạo một thư mục (nếu chưa tồn tại)

- `mkdir -p /mnt/mydir/tubt`: Tạo tất cả các thư mục trong đường dẫn chỉ định nếu chúng chưa tồn tại

**file**

Có thể xác định loại file của file được chỉ định

Ví dụ:

```sh
[root@hanode1 ~]# file geekfile.txt 
geekfile.txt: ASCII text
```

**touch**

Tạo một file (nếu chưa tồn tại)

Có thể sử dụng với tên đường dẫn tuyệt đối

```sh
touch /mnt/tubt.txt
```

**stat**

Hiển thị trạng thái file (hoặc file system)

`-f` - Hiển thị trạng thái file system thay vì trạng thái file

`-t` - Hiển thị thông tin dưới dạng ngắn gọn

**cp**

Sao chép file hoặc thư mục từ một vị trí này đến vị trí khác

`-d`: Khổng copy các liên kết tượng trưng (symbolic links), chỉ sao chép liên kết (link)

`-f`: Ghi đè mà không hỏi (nếu file đã tồn tại ở điểm đến)

`-i`: Hỏi trước khi ghi đè lên một file đã tồn tại

`-l`: Tạo một liên kết tượng cứng đến file gốc

`-s`: Tạo một liên kết tượng trưng đến file gốc

`-r`(Hoặc `-R`): Áp dụng đê quy cho các tùy chọn cho các thư mục và các thư mục con trong đường dẫn được chỉ định 

`-u`: Chỉ cập nhật copy khi file cũ mới hơn file đích hiện có (hoặc tạo file đích nếu chưa tồn tại)

NOTE: Việc sao chép có thể được thực hiện với đường dẫn tuyệt đối hoặc tương đối

**mv**

Di chuyển một file hoặc thư mục từ vị trí này sang vị trí khác

Có thể sử dụng với đường dẫn tuyệt đối hoặc tương đối

`-i`: Kiểm tra xem đích đã tồn tại hay chưa, sẽ hỏi có ghi đè không

`-u`: Không ghi đè file hoặc thư mục đích nếu nó mới hơn file hoặc thư mục gốc

`-f`: Không hỏi về thay đổi mục là nhập tên thư mục

# Quản lý file cơ bản part 2 (dd, rmdir, rm và find)

**dd**

Được sử dụng để tạo bản sao lưu image, các files định dạng đặc biệt cho dung lượng swap, file ISO CD/DVD và các file khác

Ví dụ 1:

```sh
dd if=/dev/sda of=/dev/sdb
```

Lệnh trên sẽ sao lưu toàn bộ ổ cứng /dev/sda vào ổ cứng backup /dev/sdb (giả sử /dev/sdb có cùng hoặc nhiều dung lượng hơn)

Ví dụ 2:

```sh
dd if=/dev/sr0 of=/tmp/cdimage.iso
```

Sẽ lấy một bản sao image từ thiết bị CDROM tại `/dev/sr0` và tạo một file hình ảnh ISO từ nó tại `/tmp/cdimage.iso`

**rmdir**

Xóa một thư mục, nhưng chỉ khi nó RỖNG

`-p`: Xóa tất cả các thư mục trong một đường dẫn, miễn là TẤT CẢ chúng đều RỖNG 

**rm**

Xóa file hoặc thư mục

- `-r`: Xóa đệ quy file (và các thư mục con nếu mục tiêu là một thư mục)

- `-f`: Không yêu cầu xác nhận chỉ thị xóa

- `-i`: Yêu cầu xác nhận ĐỐI VỚI MỖI file/thư mục sẽ bị xóa

**find**

Phương pháp tốt nhất để `tìm` các file dựa trên tên, loại hoặc các đặc điểm khác trên hệ thống Linux (Có thể tốn kém về hiệu suất CPU và I/O)

Ví dụ:

```sh
find / -name "messaages"
```

Lệnh trên sẽ trên filesystem bắt đầu từ thư mục `/`, đệ quy cố gắng tìm bất kỳ file hoặc thư mục nào có tên `messages`

Các option có thể tìm thấy:

- `group`: Các tệp tin/thư mục thuộc nhóm được chỉ định

- `user`: Các files/thư mục thuộc về người dùng được chỉ định

- `newer`: Các files/thư mục mới hơn file được chỉ định

- `name`: Các files/thư mục có tên khớp với chỉ định (bao gồm cả chữ hoa và chữ thường)

- `iname`: Các files/thư mục có tên khớp (không phân biệt chữ hoa chữ thường) với tên được chỉ định

- `mtime`: Các files/thư mục phù hợp với thời gian sửa đổi được chỉ định 

- `atime`: Các files/thư mục phù hợp với số ngày kể từ lần truy cập cuối cùng được chỉ định

- `ctime`: Các files/thư mục phù hợp với số ngày kể từ lần thay đổi cuối cùng được chỉ định

- `-exec [cmd] {} [output];`: Cho phép thực thi `cmd` trên tất cả các giá trị tìm thấy, được chuyển vào lệnh đó (`{}` là đại diện cho mỗi giá trị), với bất kỳ đầu ra liên quan nào

Ví dụ: 

```sh
find /home/usr/bin -name ".sh" -exec cp -f {} /home/user/backup/bin
```

Lệnh trên sẽ tìm kiếm đệ quy thư mục `/home/user/bin` để tìm các tệp tin kết thúc bằng `.sh` và sao chép chúng, ghi đè mà không cần xác nhận nếu chúng đã tồn tại vào thư mục `/home/user/backup/bin`

# Quản lý file cơ bản (Công cụ lưu trữ vào nén)

**tar**

Dùng để tạo các lưu trữ dữ liệu (nén file/thư mục)

Là một trong những tiện ích phổ biến nhất để sao lưu (qua các đuôi file mở rộng) và nén các files và thư mục

Có thể sử dụng các loại nén khác nhau (gzip và bzip)

- `-c`: Nén lưu trữ

- `-t`: Hiển thị nội dung của lưu trữ

- `-x`: Giải nén nội dung của lưu trữ

NOTE: Luôn cần một trong ba tùy chọn trên

- `-f`: Tên của file cần tạo

- `-j`: Nén/giải nén với bzip2

- `-z`: Nén/giải nén với gzip (sẵn có mặc định và là phương pháp phổ biến nhất)

- `-v`: Thông báo chi tiết (đầu ra này gần giống với lệnh ls -al khi tạo/giải nén/xem lưu trữ)

NOTE: Nhiều tùy chọn có thể được kết hợp trong một danh sách tùy chọn duy nhất

Ví dụ: 

```sh
tar -cvfz mybackup.tar.gz /home/user
```

Sẽ tạo một file có tên `mybackup.tar.gz` trong thư mục hiện tại, chứa tất cả các file trong thư mục người dùng, được nén bằng công cụ gzip

# Sử dụng Luồng (Streams), Ống (Pipes) và Chuyển hướng (Redirects)

Luồng đầu vào tiêu chuẩn (Standard input stream)

- Một luồng cung cấp đầu vào cho các thiết bị đầu cuối, files, các ứng dụng hoặc tiện ích (phương thức mà tất cả các chương trình được cho là có thể chấp nhận trong một số hình thức)

Luồng đầu ra tiêu chuẩn (Standard input stream)

Một luồng cung cấp đầu ra cho các thiết bị đầu cuối, file, ứng dụng hoặc tiện ích

Luồng lỗi tiêu chuẩn (Standard error stream): Một luồng chứa các thông báo lỗi được đưa đến các thiết bị đầu cuối, file, ứng dụng hoặc tiện ích (được coi là tập hợp con của luồng đầu ra tiêu chuẩn)

Chuyển hướng (Redirection): Quá trình lấy một luồng và gửi nó `đến nới khác`, không phải là mặc định

Các thiết bị:

- Đầu vào tiêu chuẩn (Standard Input) - `/dev/stdin`

- Đầu ra tiêu chuẩn (Standard Output) - `/dev/stdout`

- Luồng lỗi tiêu chuẩn (Standard error) - `/dev/stderr`

Trình chuyển hướng (Redirectors)

- `|`: Đường ống, để gửi đầu ra đến lệnh khác

Ví dụ: `cat /var/log/messages | more`

- `>`: Chuyển hướng đầu ra tiêu chuẩn đến một file hoặc thiết bị (tạo hoặc ghi đè file đích nếu là một file)

Ví dụ: `find /mnt -name "*.sh" > output.txt`: Đầu ra của lệnh `find /mnt -name "*.sh"` sẽ được lưu vào file `output.txt`

```sh
[root@hanode1 ~]# cat output.txt 
/mnt/tubt.sh
```

- `>>`: Chuyển hướng đầu ra tiêu chuẩn đến một file hoặc thiết bị (nối thêm vào đích nếu là một file)

Ví dụ: `find /mnt -name "*.txt" >> output.txt`: Đầu ra của lệnh `find /mnt -name "*.txt"` sẽ được ghi thêm vào file `output.txt` mà không ghi đè lên file nếu file đó đã tồn tại

```sh
[root@hanode1 ~]# cat output.txt 
/mnt/tubt.sh
/mnt/tubt.txt
```

- `<`: Chuyển hướng đầu vào tiêu chuẩn đến một chương trình

Ví dụ: `sort < /home/user/listfile.txt` hành vi tương tụ như sử dụng `cat /home/user/listfile.txt | sort`

Chuyển hướng luồng lỗi (Redirecting standard error)

- Thông thường, `stderr` được chuyển hướng đến một file (ghi nhật ký log) hoặc một đầu ra đặc biệt gọi là `/dev/null`

- Việc này cho phép bạn xóa các lỗi từ đâu ra tiêu chuẩn bình thường

Ví dụ: `find / -iname "*.sh" 2> /dev/null`: Lệnh này sẽ hiển thị kết quả tìm thấy mà không hiển thị các thông báo lỗi liên quan

Kết hợp chuyển hướng

Ví dụ: `find / -iname "*.sh* 2> /dev/null > output.txt`

Tương tự như ví dụ trên, nhưng các kết quả sẽ được chuyển hướng đến file output.txt thay vì hiển thị lên màn hình

Ví dụ: `sort < listfile.txt | nl`

Chuyển hướng listfile.txt như một luồng đầu vào đến lệnh sort, đẩy đầu ra sau khi được sort vào lệnh nl để thêm số dòng, hiển thị lên màn hình

Kết hợp đặc biệt `2>&1`

- Thường được sử dụng để loại bỏ toàn bộ đầu ra cho một công việc (job) hoặc tiến trình process (như một công việc cron), để đảm không gây ra lỗi trong hiển thị dữ liệu 

Ví dụ: `find /mnt -iname ".sh" > /dev/nul 2>&1`: Chuyển hướng lỗi tiêu chuẩn thành đầu ra tiêu chuẩn (2>&1) và toàn bộ luồng đầu ra được chuyển hướng vào `/dev/null` (bị loại bỏ)

**tee**

Nhận một luồng đầu vào tiêu chuẩn và gửi một luồng đầu ra (giống nhau) đến một file được chỉ định

Thường được sử dụng khi bạn muốn thu thập đầu ra của một ứng dụng nhưng cũng cần nhìn thấy kết quả trên màn hình

Ví dụ: `find / -name "*.sh" | tee tubt.txt`: Sẽ tìm tất cả file có đuôi mở rộng `.sh` từ phân vùng gốc `/`. Đẩy kết quả đó như một luồng đầu vào cho `tee`, sau đó mở 2 luồng đầu ra tiêu chuẩn, gửi một luồng đến console và một luồng tới file được chỉ định `tubt.txt`

**xargs**

Nhận một luồng đầu vào (kết quả của lệnh khác - thường là lệnh `find`), sau đó đẩy chúng vào một lệnh khác theo yêu cầu

Ví dụ: `find /mnt -name "*.sh" | xagrs ls -al > myresults.txt`: Sẽ tìm tất cả các files có đuôi mở rộng .sh, sau đó xagrs sẽ lấy kết quả đó cung cấp cho lệnh `ls -al` để hiển thị chi tiết của mỗi file và chuyển hướng đầu ra vào file `myresults.txt`

Output:

```sh
[root@hanode1 ~]# find /mnt -name "*.sh" | xargs ls -al > myresults.txt
[root@hanode1 ~]# cat myresults.txt 
-rwxr-xr-x. 1 root root 13 Sep 11 08:36 /mnt/tubt.sh
```

# Tạo, giám sát và hủy (kill) tiến trình (PID, ps, pstree, uptime, kill, killall, pkill, pgrep)

**PID**

Mã xác định tiến trình - một số duy nhất (trên hệ thống Linux) có thể được sử dụng để tham chiếu đến một tiến trình đang chạy 

**ps**

Hiển thị các tiến trình đã được khởi động và đang chạy với quyền người dùng được chỉ định

- `-a`: Hiển thị tất cả các tiến trình đang chạy trên hệ thống, cho bất kỳ người dùng nào

- `-u`: Hiển thị thông tin người dùng cho các tiến trình được hiển thị

- `-x`: Hiển thị tiến trình không có tty (terminal) kết nối

Ví dụ: 

```sh
ps -aux
```

Sẽ hiển thị tất cả các tiến trình đang chạy, bởi bất kỳ người dùng nào, hiển thị chủ sở hữu  tiến trình và bao gồm các tiến trình không liên kết với một terminal

Theo tính chất chuyển hóa, mặc dù có sự khác biệt về định dạng `ps -aux = ps -ef`

**pstree**

Hiển thị cây tiến trình đang chạy theo dang cây (hiển thị ASCII phân cấp hoặc ncurses)

- `-A`: Hiển thị cây sử dụng ký tự ASCII

- `-a`: Hiển thị các tiến trình bao gồm các tham số sử dụng

- `-p`: Hiển thị PID

**free**

Cung cấp thông tin về bộ nhớ RAM hệ thống Linux (bao gồm tổng cộng, đang sử dụng, được chia sẻ, bộ đệm và bộ nhớ cache ...)

`-b` (hoặc --bytes): Hiển thị bộ nhớ theo byte

`-k` (hoặc --kilo): Hiển thị bộ nhớ theo kilobyte (mặc định)

`-m` (hoặc --mega): Hiển thị bộ nhớ theo megabyte

`-g` (hoặc --giga): Hiển thị bộ nhớ theo gigabyte

`-h` (hoặc --human): Hiển thị bộ nhớ theo dạng dễ đọc cho con người

`-c` (hoặc --count): Số lần hiển thị kết quả (phải được sử dụng với tùy chọn `-s`)

`-s` (hoặc --seconds): Thời gian chờ giữa mỗi lần hiển thị kết quả (sử dụng vơi tùy chọn `-c`)

`-t` (hoặc --total): Hiển thị dòng chỉ số tổng của từng cột

`-l` (hoặc --lohi): Hiển thị thống kê bộ nhớ thấp và cao

**uptime**

Hiển thị thời gian hệ thống Linux đã chạy kể từ lần khởi động (boot)/khởi động lại (reboot) cuối cùng

Cung cấp thông tin về số lượng người dùng hiện đang có trên hệ thống Linux và tải trung bình trên hệ thống trong 1, 5 và 15 phút (ba giá trị)

**Signals**

Là những gi được gửi đến tiến trình và tiến trình sau đó phản ứng tương ứng, tùy thuộc vào loại tín hiệu

- SIGHUP - Tín hiệu 1 - tắt và khởi động lại tiến trình (hangup)

- SIGINT - Tín hiệu 2 - gián đoạn một tiến trình (CTRL + C)

- SIGKILL - Tín hiệu 9 - kill tiến trình (không thể bị bỏ qua hoặc bắt được)

- SIGTERM - Tín hiệu 15 - kết thúc tiến trình (tiến trình có thể bỏ qua hoặc bắt được tín hiệu)

- SIGSTOP - Tín hiệu 19 - dừng tiến trình (không thể bị bỏ qua hoặc bắt được)

- SIGTSTP - Tín hiệu 20 - dừng terminal (CTRL + Z)

**Kill**

Gửi một lệnh kill 'nice' đến PID chỉ định (mặc định lệnh kill là tín hiệu SIGTERM signal 15)

Phương pháp này cho phép tiến trình dừng lại 1 cách 'sạch sẽ' (kết thúc, giải phóng bộ nhớ, đóng file đang mở ...)

`-1` (-HUP) - Tham chiếu đặc biệt để yêu cầu tiến trình khởi động lại (để đọc lại file cấu hình hoặc thực hiện thay đổi)

`-9` (-KILL) - kill/stop/end/dump ngay lập tức (thường dùng để kill ngay cả một tiến trình zombie hoặc đang treo)

**killall**

Tiêu diệt (kill) tất cả các tiến trình dựa trên tên, ID, người dùng, phiên hoặc thiết bị đầu cuối (tty)

LƯU Ý: Nếu có nhiều tiêu chí được sử dụng. TẤT CẢ các tùy chọn phải khớp để áp dụng cho một tiến trình

**pgrep**

Cho phép kiểm tra (debug) lệnh pkill (Hiển thị những gì sẽ xảy ra)

Hiển thị ID quá trình sẽ bị ảnh hưởng

Chấp nhận TẤT CẢ các tùy chọn pkill để xác định PID sẽ bị ảnh hưởng 

LƯU Ý: Nếu cung cấp nhiều tùy chọn, cách liệt kê sẽ xác định cách chúng được hiểu

Ví dụ: `pgrep -u root,apache httpd`: Sẽ hiển thị bất kỳ tiến trình httpd nào thuộc sở hữu của `root` 'HOẶC' `apache`

Ví dụ: `pgrep -u root apache`: Chỉ hiển thị các tiến trình thuộc sở hữu của `root` 'VÀ' `apache`

# Tạo, giám sát và tiêu diệt quá trình (jobs, bg, fg, priority, nohup và screen)

**jobs**

Sẽ hiển thị trạng thái của các công việc (jobs) đã bị tạm dừng

Hiển thị:

- `[#]- Stopped [cmd]` - cho biết công việc trước đó hoặc công việc trước đó sẽ được thao tác 

- `[#]- Stopped [cmd]` - cho biết công việc hiện tại với bất kỳ lệnh (bg hoặc fg) nào sẽ tác động vào nó

**bg**
Gửi tiến trình đã chỉ định vào chế độ nền background (thường được sử dụng sau lệnh jobs để đưa một tiến trình tạm dừng vào nền để nó tiếp tục chạy)

**fg**
Gửi tiến trình đã chỉ ra chế độ phía trước `foreground` (dùng để đưa một tiến trình đang chạy nền ra phía trước để sử dụng)

**&**

Đặt một chương trình vào chế độ nền phía trước background khi chạy sau một lệnh

Ví dụ: `vim &`: Sẽ chạy và đưa trình soạn thảo vim vào chế độ nền

**priority**

Lập lịch và ưu tiên là cách Linux sử dụng để chạy nhiều ứng dụng/dịch vụ/tiến trình trên một máy tính duy nhất một cách đa nhiệm

Ưu tiên tiến trình mặc định là `0`

Dải ưu tiên là từ `0` đến `19` và từ `0` đến `-20` (điểm ưu tiên càng thấp, tiến trình càng nhận được nhiều tài nguyên hơn `-20` là điểm ưu tiên cao nhất)

- Mọi người dùng có thể bắt đầu tiến trình với điểm ưu tiên từ 0 đến 19

- Chỉ root mới có thể bắt đầu tiến trình với điểm ưu tiên từ 0 đến -20

**nohup**

Cho phép bạn khởi chạy một ứng dụng hoặc tiến trình từ dòng lệnh /terminal và sau đó `stop/exit/logout` khởi terminal hoặc phiên làm việc, trong khi vẫn giữ ứng dụng hoặc tiến trình đang chạy

Ví dụ: `nohup find / -name <ten_file> > output.txt `

Lệnh tìm file này có thể chạy trong thời gian dài (giả sử trên một hệ thống file lớn) và dừng khi chúng ta đăng xuất khỏi máy tính, đóng terminal - `nohup` cho phép lệnh đó tiếp tục chạy nếu chúng ta thoát/đóng phiên

**screen**

Là một trình quản lý phiên (session) văn bản cho phép chạy nhiều phiên shell độc lập với nhau trong cùng một cửa sổ

Có thể sử dụng phiên để kết nối cục bộ hoặc từ xa (tương tự như sử dụng nhiều terminal)

Hỗ trợ chức năng sao chép/dán giữa các phiên làm việc

Hỗ trợ ghi log đầu ra nếu được cấu hình

Có khả năng tách rời (thường được gọi là "bỏ lại") một cửa sổ, cho phép các chương trình được khởi chạy bên trong tiếp tục chạy

Các tùy chọn khi `screen` được khởi động:

- ctrl + a + c: Mở một phiên làm việc mới

- ctrl + a + p: Di chuyển quay lại phiên làm việc trước đó

- ctrl + a + n: Di chuyển đến phiên làm việc tiếp theo 

- ctrl + a + ": Hiển thị danh sách các phiên làm việc có sẵn (được định danh bằng số)

- screen -ls: Hiển thị danh sách các màn hình

- screen -r: Kết nối lại với màn hình

# Sửa đổi ưu tiên thực thi tiến trình (Sử dụng nice, renice và top)

**nice**

Cho phép người dùng khởi chạy một tiến trình với ưu tiên thấp hơn mặc định (mặc định là `0`, nice sẽ khởi chạy với `10`)

Ví dụ: `nice myscript.sh`

Sẽ khởi chạy myscript.sh với ưu tiên thấp hơn đó là `10`

`nice -n [#] myscript.sh`: Cho phép bạn thay đổi ưu tiên mặc định của chương trình đã chỉ định

**renice**

Thay đổi ưu tiên của một tiến trình

Thường được sử dụng để giảm ưu tiên của một tiến trình mà có thể tiêu thụ quá nhiều tài nguyên hoặc tăng ưu tiên của một tiến trình để nó hoàn thành nhanh hơn

`renice +[#] [PID]`: Thay đổi ưu tiên thành một số cao hơn (tương ứng với ưu tiên thấp hơn)

Chỉ có người dùng root mới có thể tăng ưu tiên của một tiến trình đang chạy

`renice -[#] [PID]`: Thay đổi ưu tiên thành một số thấp hơn (tương ứng với ưu tiên cao hơn)

**top**

Cấu hình được đọc từ `/etc/toprc` (hoặc /home/user/.toprc cục bộ cho cấu hình người dùng)

Có thể được sử dụng để hiển thị các tiến trình `top` đang hoạt động 

Cũng có thể được sử dụng để thay đổi độ ưu tiên của các tiến trình đang chạy

- `d [#]`: Chạy và cập nhật hiển thị tiến trình mỗi '#' giây

- `i`: Chỉ hiện thị các tiến trình hoạt động

- `b`: Chạy ở chế độ batch 

- `c [#]`: Chạy # lần cập nhật và thoát

Ví dụ: `top -b -n 5 > output.txt`: Sẽ chạy ở chế độ batch và cập nhật 5 lần, ghi kết quả vào file `output.txt` và thoát

Trong quá trình chạy, ta có thể sử dụng các phím tắt sau:

- `spacebar`: Cập nhật ngay lập tức

- `h`: Hiển thị màn hình trợ giúp

- `k`: Yêu cầu PID để kết thúc

- `i`: Hiển thị hoặc bỏ qua các tiến trình không hoạt động /ru idle /zombie

- `n`: Yêu cầu số tiến trình để hiển thị trên màn hình

- `r`: Yêu cầu PID để áp dụng `renice` và ưu tiên mới (số càng cao, ưu tiên càng thấp)

- `R`: Sắp xếp các PID của tiến trình từ cao đến thấp (ngược lại so với mặc định)

# Tìm kiếm file văn bản bằng biểu thức chính quy (grep, egrep, fgrep, sed và regex)

**grep**

Một tiện ích để tìm chuỗi và cụm từ trong tập tin, luồng hoặc thư mục 

- `-c`: Chỉ hiển thị số lượng tìm thấy

- `-C [#]`: Bao quanh kết quả tìm kiếm với '#' dòng liên quan (trước và sau dữ liệu)

- `-E [ext. regex]`: Sử dụng biểu thức chính quy mở rộng chỉ định để tìm kiếm 

- `-F [fixed regex`: Sử dụng biểu thức chính quy cố định chỉ định để tìm kiếm

- `-H`: Hiển thị tên file của mỗi chuỗi hoặc cụm từ khớp

- `-h`: Ngăn không hiển thị tên file

- `-i`: Không phân biệt chữ hoa, chữ thường 

- `-l`: Chỉ hiển thị tên file, không hiển thị chuỗi/cụm từ khớp

- `-L`: Chỉ hiển thị tên file, không chưa chuỗi/cụm từ khớp

- `-w`: Chỉ khớp các dòng chứa toàn bộ chuỗi và cụm từ

- `-x`: Chỉ hiển thị các dòng khớp chính xác toàn bộ chuỗi hoặc cụm từ

- `-v`: Chỉ hiển thị các dòng trong file không khớp với chuỗi hoặc cụm từ (ngược lại với mặc định)

Ví dụ: `find / -name "*.sh" -exec grep -iH "modprobe" {} ;`

Lệnh này sẽ tìm file, đệ quy, bắt đầu từ thư mục root và kết thúc bằng `.sh`, truyển file đó cho lệnh grep, lệnh này sẽ không phân biệt chữ hoa thường và hiển thị tên file và nội dung khớp của bất kỳ file nào chứa từ khóa "modprobe"

Ví dụ: `grep -v "/bin/bash" /etc/passwd`

Sẽ chỉ hiển thị các dòng KHÔNG chứa giá trị `/bin/bash`

