# PostgreSQL

PostgreSQL là một hệ thống cơ sở dữ liệu quan hệ đối tượng mã nguồn mở, sử dụng và mở rộng ngôn ngữ SQL kết hợp với nhiều tính năng lưu trữ cho workloads phức tạp

# Cài đặt PostgreSQL

Tải xuống và cài đặt kho lưu trữ RPM:

```sh
sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```

Cài đặt PostgreSQL 15:

```sh
sudo yum install -y postgresql15-server
```

Khởi tạo cơ sở dữ liệu

```sh
sudo /usr/pgsql-16/bin/postgresql-16-setup initdb
```

Start PostgreSQL 15 và cho phép khởi động cùng hệ thống

```sh
sudo systemctl start postgresql-15
sudo systemctl enable postgresql-15
```

# Quản trị PostgreSQL databases

Theo mặc định, Postgres sử dụng một khái niệm gọi là `roles` để xử lý việc xác thực và ủy quyền

Sau khi cài đặt Postgres được thiết lập để sử dụng danh tính, nghĩa là nó liên kết các `role` của Postgres với tài khoản hệ thống Unix/Linux phù hợp. Nếu một `role` tồn tại trong Postgres, tên người dùng trên Linux có cùng tên có thể đăng nhập với `role` đó

Quy trình cài đặt sẽ tạo một tài khoản người dùng có tên `postgres` được liên kết với `role` Postgres mặc định. Để sử dụng Postgres, bạn có thể đăng nhập vào tài khoản đó

**Chuyển sang tài khoản postgres**

Chuyển sang tài khoản postgres trên máy chủ bằng cách nhập:

```sh
[root@postgres ~]# sudo -i -u postgres
-bash-4.2$ 
```

Bây giờ bạn có thể truy cập Postgres ngay lập tức bằng cách gõ

```sh
-bash-4.2$ psql
psql (15.4)
Type "help" for help.

postgres=# 
```

Thao tác này sẽ đăng nhập và đưa shell vào dấu nhắc PostgreSQL và từ đây ta có thể tự do tương tác với hệ thống quản lý cơ sở dữ liệu ngay lập tức

Thoát khỏi PostgreSQL bằng cách gõ:

```sh
postgres=# \q
```

**Truy cập lời nhắc Postgres mà không cần chuyển đổi tài khoản**

Chúng ta cũng có thể chạy thẳng tới Postgres prompt bằng lệnh sau

```sh
[root@postgres ~]# sudo -u postgres psql
could not change directory to "/root": Permission denied
psql (15.4)
Type "help" for help.

postgres=# 
```

Điều này sẽ đăng nhập bận trực tiếp vào Postgres mà không cần bash trung gian 

**Tạo role mới**

Ta có thể tạo `role` mới từ dòng lệnh bằng lệnh `createrole`. Option `--interactive` sẽ nhắc bạn tên của `role` mới và cũng hỏi liệu `role` đó có cần quyền superuser hay không 

Nếu ta đang đăng nhập bằng user `postgres` trên server, ta có thể tạo người dùng mới bằng cách nhập:

```sh
bash-4.2$ createuser --interactive
```

Hoặc ta sử dụng sudo cho mỗi lệnh và không cần chuyển qua lại giữa các user để tạo `role`

```sh
sudo -u postgres createuser --interactive
```

Sau khi chạy lệnh, hệ thống sẽ nhắc bạn với một số lựa chọn và dựa trên phản hồi, hệ thống sẽ thực thì các lệnh Postgres chính xác để tạo người dùng theo thông số kỹ thuật của bạn. Ở đây ta tạo một người dùng `tubt` có cấp cho nó các đặc quyền của superuser

```sh
Enter name of role to add: tubt
Shall the new role be a superuser? (y/n) y
```

**Tạo DB**

Theo mặc định đối với bất kỳ `role` nào được sử dụng để đăng nhập, `role` đó sẽ có cơ sở dữ liệu có CÙNG TÊN mà nó có thể truy cập

Điều này có nghĩa là nếu người dùng chúng ta tạo ở phần trước là `tubt` thì `role` đó sẽ cố gắng kết nối với cơ sở dữ liệu cũng có tên là `tubt` theo mặc định. Bạn cũng có thể tạo db thích hợp bằng lệnh `createdb`

```sh
sudo -u postgres createdb tubt
```

Bây giờ sau khi đã tạo db mới, bạn sẽ đăng nhập vào db đó với `role` của mình

**Truy cập Posgres với role mới tạo**

Để đăng nhập bằng xác thực dựa trên danh tính, bạn sẽ cần một người dùng Linux có cùng tên với `role` và db Postgres của bạn

Tạo user phù hợp 

```sh
[root@postgres ~]# sudo useradd tubt
```

Khi tài khoản mới này có sẵn, bạn có thể chuyển đổi và kết nối db bằng cách nhập:

```sh
sudo -u tubt psql
```

Nếu muốn người dùng của mình kết nối với cơ sở dữ liệu khác, bạn có thể làm như vậy bằng cách chỉ định cơ sở dữ liệu như sau

```sh
[tubt@postgres ~]$ psql -d postgres
psql (15.4)
Type "help" for help.

postgres=#
```

Sau khi đăng nhập, bạn có thể kiểm tra thông tin kết nối hiện tại của mình bằng cách nhập

```sh
postgres=# \conninfo
You are connected to database "postgres" as user "tubt" via socket in "/var/run/postgresql" at port "5432".
```

Điều này hữu ích nếu bạn đang kết nối với cơ sở dữ liệu không mặc định hoặc người dùng không mặc định 

Sau khi kết nối với db, bây giờ ta có thể thử tạo và xóa table

**Tạo và xóa Tables**

Bây giờ ta đã biết cách kết nối với hệ thống cơ sở dữ liệu PostgreSQL, ta có thể tìm hiểu một số tác vụ quản lý PostgreSQL cơ bản

Đầu tiên, tạo một bảng để lưu trữ dữ liệu.

Ví dụ: bạn sẽ lập một bảng mô tả một số trường

Cú pháp cơ bản của lệnh này như sau:

```sh
CREATE TABLE table_name (
    column_name1 col_type (field_length) column_constraints,
    column_name2 col_type (field_length),
    column_name3 col_type (field_length)
);
```

Các lệnh này đặt tên cho bảng, sau đó xác định các cột cũng như loại cột và độ dài tối đa của dữ liệu trường. 

Hãy tạo 1 bảng đơn giản như sau:

```sh
CREATE TABLE form (
	equip_id serial PRIMARY KEY,
	name varchar (50) NOT NULL,
	age varchar (10) NOT NULL,
	location varchar (20) NOT NULL,
	gender varchar (25) check (gender in ('male', 'female')),
	install_date date
);
```

Bảng trên chứa các trường `name`, `age`, `locate`, `gender`, `install_date`

Trong đó:

- `varchar`: Số ký tự tối đa được chỉ định cho trường

- `NOT NULL`: Các trường không được bỏ trống (phải có giá trị nếu không sẽ trả về lỗi)

- `check (gender in ('male', 'female'))`: Chỉ định 1 trong 2 giá trị cho trường, bắt buộc trường đỏ chỉ cho phép nhận 2 giá trị `male` và `female` nếu không sẽ trả về lỗi

- `date`: Định dạng giá trị cho trường theo date (Năm - Tháng - Ngày)

**Output:**

```sh
tubt=# CREATE TABLE form (
tubt(# equip_id serial PRIMARY KEY,
tubt(# name varchar (50) NOT NULL,
tubt(# age varchar (10) NOT NULL,
tubt(# location varchar (20) NOT NULL,
tubt(# gender varchar (25) check (gender in ('male', 'female')),
tubt(# install_date date
tubt(# );
CREATE TABLE
```

Ta có thể xem table mới tạo bằng cách gõ:

```sh
tubt=# \d
               List of relations
 Schema |       Name        |   Type   | Owner 
--------+-------------------+----------+-------
 public | form              | table    | tubt
 public | form_equip_id_seq | sequence | tubt
(2 rows)
```

Table `form` mà chúng ta vừa tạo đã được hiển thị, những có một hàng khác là `form_equip_id_seq` thuộc loại `sequence`. Đây là loại `serial PRIMARY KEY` mà chúng ta vừa cùng cấp cho `equip_id`. Điều này sẽ đánh số thứ tự cho các hàng trong bảng, được tạo tự động

Nếu chỉ muốn xem table mà không có `sequence`, ta có thể gõ:

```sh
tubt=# \dt
       List of relations
 Schema | Name | Type  | Owner 
--------+------+-------+-------
 public | form | table | tubt
(1 row)
```

Nếu muốn xóa table ta sử dụng lệnh 

```sh
DROP TABLE <table_name>;
```

Truy xuất toàn bộ thông tin của table bằng cách sau:

```sh
tubt=# SELECT * FROM form;
 equip_id | name | age | location | gender | install_date 
----------+------+-----+----------+--------+--------------
(0 rows)
```

Ở bước này chúng ta đã tạo 1 table mẫu. Trong bước tiếp theo, ta sẽ thử thêm, truy vấn và xóa các mục trong table đó

**Thêm, truy vấn và xóa dữ liệu trong Table**

Bây giờ chúng ta đã có Table, ta có thể chèn một số dữ liệu vào đó

Lưu ý: Chúng ta không cần nhập giá trị cho cột `equip_id` do cột này được tạo tự động khi có bất kỳ hàng mới nào trong Table được tạo

Ví dụ: Gọi bảng muốn thêm, đặt tên cho các cột và cung cấp dữ liệu cho từng cột như sau:

```sh
INSERT INTO form (name, age, location, gender, install_date) VALUES ('tubt', '24', 'Dong Anh', 'male', '2023-09-26');
```

```sh
INSERT INTO form (name, age, location, gender, install_date) VALUES ('tubt1', '20', 'Ha Noi', 'male', '2022-09-26');
```

```sh
INSERT INTO form (name, age, location, gender, install_date) VALUES ('tubt2', '22', 'Mai Lam', 'female', '2021-09-26;
```

```sh
tubt=# INSERT INTO form (name, age, location, gender, install_date) VALUES ('tubt', '24', 'Dong Anh', 'male', '2023-09-26');
INSERT 0 1
tubt=# INSERT INTO form (name, age, location, gender, install_date) VALUES ('tubt1', '20', 'Ha Noi', 'male', '2022-09-26');
INSERT 0 1
tubt=# INSERT INTO form (name, age, location, gender, install_date) VALUES ('tubt2', '22', 'Mai Lam', 'female', '2021-09-26');
INSERT 0 1
```

Truy xuất toàn bộ thông tin của table để xem dữ liệu vừa được thêm

```sh
tubt=# SELECT * FROM form;
 equip_id | name  | age | location | gender | install_date 
----------+-------+-----+----------+--------+--------------
        1 | tubt  | 24  | Dong Anh | male   | 2023-09-26
        2 | tubt1 | 20  | Ha Noi   | male   | 2022-09-26
        3 | tubt2 | 22  | Mai Lam  | female | 2021-09-26
(3 rows)
```

Từ Output của lệnh trên chúng ta thấy được `equip_id` đã tự động đánh số thứ tự từ từ hàng 1 đến hàng 3 và tất cả dữ liệu đã được `INSERT` theo thứ tự chính xác

Nếu muốn xóa một HÀNG trong một table ta sử dụng lệnh sau:

```sh
tubt=# DELETE FROM form WHERE name = 'tubt1';
```

Truy vấn lại vào table, ta thấy HÀNG có `name` = `tubt1` đã bị xóa

```sh
tubt=# SELECT * FROM form;
 equip_id | name  | age | location | gender | install_date 
----------+-------+-----+----------+--------+--------------
        1 | tubt  | 24  | Dong Anh | male   | 2023-09-26
        3 | tubt2 | 22  | Mai Lam  | female | 2021-09-26
(2 rows)
```

**Thêm và xóa cột khỏi Table**

Sau khi tạo Table, bạn có thể sửa đổi Table bằng cách thêm hoặc xóa cột. Thêm cột bằng cách sau:

```sh
tubt=# ALTER TABLE form ADD color varchar(10);
ALTER TABLE

tubt=# SELECT * FROM form;
 equip_id | name  | age | location | gender | install_date | color 
----------+-------+-----+----------+--------+--------------+-------
        1 | tubt  | 24  | Dong Anh | male   | 2023-09-26   | 
        3 | tubt2 | 22  | Mai Lam  | female | 2021-09-26   | 
(2 rows)
```

Xóa cột bằng cách sau:

```sh
tubt=# ALTER TABLE form DROP color;
ALTER TABLE

tubt=# SELECT * FROM form;
 equip_id | name  | age | location | gender | install_date 
----------+-------+-----+----------+--------+--------------
        1 | tubt  | 24  | Dong Anh | male   | 2023-09-26
        3 | tubt2 | 22  | Mai Lam  | female | 2021-09-26
(2 rows)
```

Thao tác này sẽ xóa cột `color` và mọi giá trị trong cột đó nhưng giữ nguyên tất cả các dữ liệu khác

**Update dữ liệu trong Table**

Để sửa đổi các dữ liệu có sẵn trong Table ta làm như sau:

```sh
tubt=# UPDATE form SET location = 'Ha Noi' WHERE name = 'tubt';
UPDATE 1

tubt=# SELECT * FROM form;
 equip_id | name  | age | location | gender | install_date 
----------+-------+-----+----------+--------+--------------
        3 | tubt2 | 22  | Mai Lam  | female | 2021-09-26
        1 | tubt  | 24  | Ha Noi   | male   | 2023-09-26
(2 rows)
```

Ta có thể thấy `location` đã thay đổi từ `Dong Anh` sang `Ha Noi`

Ngoài ra ta có thể truy vấn đến từng cột hoặc nhiều cột thay vì truy vấn đến tất cả các cột trong Table

```sh
tubt=# SELECT name, age FROM form;
 name  | age 
-------+-----
 tubt2 | 22
 tubt  | 24
(2 rows)
```

