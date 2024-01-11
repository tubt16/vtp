# PostgreSQL Create Table

## Connect to DB

Để tạo Table mới, hãy đảm bảo rằng chúng ta đã kết nối với DB

Khi kết nối đã sẵn sàng, chúng ta sẽ thực hiện tạp Table

## Create Table

```sh
CREATE TABLE cars (
	brand VARCHAR(255),
	model VARCHAR(255),
	year INT
);
```

Khi bạn thực hiện câu lệnh trên một Table mới có tên là `cars` sẽ được tạo và output sẽ như sau:

Output:

```sh
tubt=# CREATE TABLE cars (
tubt(# brand VARCHAR(255),
tubt(# model VARCHAR(255),
tubt(# year INT
tubt(# );
CREATE TABLE
```

**Giải thích về câu lệnh trên**:

- Câu lệnh SQL ở trên đã tạo một Table có ba trường: `brand`, `model` và `year`

- Khi tạo các trường trong Table, chúng ta phải chỉ định kiểu dữ liệu của từng trường

- Đối với `brand` và `model` các giá trị sẽ là `string values` và để chỉ định đầu ra cho 2 trường trên là `string values` thì ta sử dụng `VARCHAR`, chúng ta cũng phải chỉ định số lượng ký tự tối đã cho các trường, ở đây là 255

- Đối với `year`, chúng ta chỉ định các giá trị phải là số nguyên (interger) vì thế ta chỉ định bằng từ khóa `INT`

## Display Table 

Bạn có thể hiển thị Table "trống" bạn vừa tạo bằng một câu lệnh SQL

```sh
tubt=# SELECT * FROM cars;
 brand | model | year 
-------+-------+------
(0 rows)
```

# PostgreSQL INSERT INTO

## Insert Into

Để chèn dữ liệu vào một Table trong PostgreSQL, chúng ta sử dụng câu lệnh `INSERT INTO`:

```sh
tubt=# INSERT INTO cars (brand, model, year) VALUES ('Ford', 'Mustang', '1964');
INSERT 0 1
```

Số `1` đã diện cho một hàng đã được chèn vào, số `0` sẽ được giải thích ở phần sau

**Giải thích câu lệnh trên**

Như bạn đã thấy trong câu lệnh SQL ở trên, các giá trị chuỗi phải được viết bằng dấu nháy đơn

Các giá trị số có thể được viết mà không cần có dấu nháy đơn, nhưng bạn có thể đưa chúng vào nếu muốn

## Display Table 

Để kiểm tra kết quả, chúng ta có thể hiển thị Table bằng câu lệnh SQL sau:

```sh
tubt=# SELECT * FROM cars;
 brand |  model  | year 
-------+---------+------
 Ford  | Mustang | 1964
(1 row)
```

## Insert Multiple Rows
Trước khi đi vào ví dụ chính chúng ta cùng xem một ví dụ về SQL syntax mà các bạn nên biết

Ví dụ 1:

```sh
tubt=# SELECT version();
                                                 version                                               
  
---------------------------------------------------------------------------------------------------------
 PostgreSQL 15.4 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44), 64-bit
(1 row)
```

Ví dụ 2:

```sh
tubt=# SELECT
tubt-# version();
                                                 version                                               
  
---------------------------------------------------------------------------------------------------------
 PostgreSQL 15.4 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44), 64-bit
(1 row)
```

Sau khi xem xong ví dụ 1 và ví dụ 2 chúng ta có thể kết luận

Đối với SQL shell, nó sẽ đợi dấu `;` và thực thi tất cả các dòng dưới dạng một câu lệnh SQL. Câu lệnh SQL nhiều dòng không được thực thi khi chúng ta đưa dấu `;` vào cuối

Trở lại với ví dụ chính

Để chèn nhiều hàng dữ liệu, chúng ta sử dụng cùng một câu lệnh `INSERT INTO` nhưng có nhiều giá trị:

```sh
INSERT INTO cars (brand, model, year)
VALUES
  ('Volvo', 'p1800', 1968),
  ('BMW', 'M1', 1978),
  ('Toyota', 'Celica', 1975);
```

Output:

```sh
tubt=# INSERT INTO cars (brand, model, year)
tubt-# VALUES
tubt-#   ('Volvo', 'p1800', 1968),
tubt-#   ('BMW', 'M1', 1978),
tubt-#   ('Toyota', 'Celica', 1975);
INSERT 0 3
```

Số `3` trong đầu ra có nghĩa là 3 hàng mới đã được chèn vào

## Display Table

Kiểm tra Table sau khi chèn 

```sh
tubt=# SELECT * FROM cars;
 brand  |  model  | year 
--------+---------+------
 Ford   | Mustang | 1964
 Volvo  | p1800   | 1968
 BMW    | M1      | 1978
 Toyota | Celica  | 1975
(4 rows)
```

# PostgreSQL Select Data

## Select Data

Để lấy dữ liệu từ cơ sở liệu, chúng ta sử dụng lệnh SELECT

## Specify Columns

Bằng cách chỉ định tên cột, chúng ta có thể chọn cột nào chọn

```sh
tubt=# SELECT brand, year FROM cars;
 brand  | year 
--------+------
 Ford   | 1964
 Volvo  | 1968
 BMW    | 1978
 Toyota | 1975
(4 rows)
```

## Return All Columns

Chỉ định `*` thay vì tên cột để chọn tất cả các cột (Ta đã nhìn thấy lệnh này nhiều lần từ các phần trước): 

```sh
tubt=# SELECT * FROM cars;
 brand  |  model  | year 
--------+---------+------
 Ford   | Mustang | 1964
 Volvo  | p1800   | 1968
 BMW    | M1      | 1978
 Toyota | Celica  | 1975
(4 rows)
```

# PostgreSQL Add Column

## ALTER TABLE Statement

Để thêm một cột vào Table hiện có, chúng ta sử dụng câu lệnh `ALTER TABLE`

Câu lệnh `ALTER TABLE` được sử dụng để thêm, xóa hoặc sửa đổi cột trong Table hiện có

Câu lệnh `ALTER TABLE` cũng được sử dụng để thêm và xóa các ràng buộc khác nhau trên một Table hiện có

## ADD COLUMN

Thêm một cột có tên `color` vào Table `cars`

Khi thêm cột chúng ta cũng phải xác định kiểu dữ liệu của cột đó. Cột `color` của chúng ta sẽ là một `value string` và chúng ta chỉ định nó bằng cách sử dụng từ khóa `VARCHAR`, chúng ta cũng muốn giới hạn số lượng ký tự ở mức 255:

```sh
tubt=# ALTER TABLE cars ADD color VARCHAR(255);
ALTER TABLE
```

## Display Table 

Kiểm tra Table sau khi đã tạo cột

```sh
tubt=# SELECT * FROM cars;
 brand  |  model  | year | color 
--------+---------+------+-------
 Ford   | Mustang | 1964 | 
 Volvo  | p1800   | 1968 | 
 BMW    | M1      | 1978 | 
 Toyota | Celica  | 1975 | 
(4 rows)
```

# PostgreSQL UPDATE

## UPDATE Statement

Câu lệnh UPDATE được sử dụng để sửa đổi các giá trị trong các bản ghi hiện có trong Table

```sh
tubt=# UPDATE cars SET color = 'red' WHERE brand = 'Volvo';
UPDATE 1
```

`UPDATE 1` có nghĩa là 1 hàng chịu ảnh hưởng bởi lệnh `UPDATE`

## Display Table

```sh
tubt=# SELECT * FROM cars;
 brand  |  model  | year | color 
--------+---------+------+-------
 Ford   | Mustang | 1964 | 
 BMW    | M1      | 1978 | 
 Toyota | Celica  | 1975 | 
 Volvo  | p1800   | 1968 | red
(4 rows)
```

Lưu ý khi sử dụng `WHERE`: Hãy cẩn thận khi cập nhật Table. Nếu bạn bỏ qua lệnh `WHERE`, tất cả các hàng sẽ được cật nhật

Ví dụ:

```sh
tubt=# UPDATE cars SET color = 'red';
UPDATE 4
```

`UPDATE 4` nghĩa là 4 hàng chịu ảnh hưởng bởi lệnh `UPDATE` trên

## Display Table

Kiểm tra kết quả

```sh
tubt=# SELECT * FROM cars;
 brand  |  model  | year | color 
--------+---------+------+-------
 Ford   | Mustang | 1964 | red
 BMW    | M1      | 1978 | red
 Toyota | Celica  | 1975 | red
 Volvo  | p1800   | 1968 | red
(4 rows)
```

Ta thấy tất cả các hàng để được set color là `red` nếu chúng ta quên không sử dụng `WHERE`

## UPDATE Multiple Columns

Để cập nhật nhiều cột, hãy phân tách các cặp name/value bằng dấu phẩy `,`:

```sh
tubt=# UPDATE cars SET color = 'white', year = '1970' WHERE brand = 'Toyota';
UPDATE 1
```

## Display Table 

Kiểm tra kết quả

```sh
tubt=# SELECT * FROM cars;
 brand  |  model  | year | color 
--------+---------+------+-------
 Ford   | Mustang | 1964 | red
 BMW    | M1      | 1978 | red
 Volvo  | p1800   | 1968 | red
 Toyota | Celica  | 1970 | white
(4 rows)
```

# PostgreSQL ALTER COLUMN

## ALTER COLUMN Statement 

Để thay đổi kiểu dữ liệu hoặc kích thước của cột trong Table, chúng ta sử dụng câu lệnh ALTER TABLE

Câu lệnh ALTER TABLE được sử dụng để thêm, xóa hoặc sửa đổi các cột trong Table hiện có

Câu lệnh ALTER TABLE cũng được sử dụng để thêm và xóa các ràng buộc khác nhau trên một Table hiện có

## ALTER COLUMN

Chúng ta muốn thay đổi kiểu dữ liệu của cột `year` của Table `cars` từ `INT` thành `VARCHAR(4)`

Để sửa đổi một cột, hãy sử dụng câu lệnh `ALTER COLUMN` và từ khóa `TYPE` theo sau là kiểu dữ liệu mới:

```sh
tubt=# ALTER TABLE cars ALTER COLUMN year TYPE VARCHAR(4);
ALTER TABLE
```

**Note: Một số loại dữ liệu không thể chuyển đổi được nếu cột có giá trị. Ví dụ: Số luôn có thể được chuyển đổi thành text nhưng text không phải lúc nào cũng có thể chuyển đổi được thành số**

Bây giờ kiểu dữ liệu của cột `year` sẽ không chỉ còn là kiểu số nguyên nữa nên chúng ta có thể sử dụng thay đổi dữ liệu của cột này thành text để kiểm tra thử

```sh
UPDATE cars SET year = 'abcd' WHERE brand = 'Ford';
```

## Display Table

Kiểm tra lại Table sau khi thay đổi

```sh
tubt=# SELECT * FROM cars;
 brand  |  model  | year | color 
--------+---------+------+-------
 BMW    | M1      | 1978 | red
 Volvo  | p1800   | 1968 | red
 Toyota | Celica  | 1970 | white
 Ford   | Mustang | abcd | red
(4 rows)
```

## Change Maximum Allowed Characters

Chúng ta cũng có thể thay đổi số lượng ký tự tối đa được phép trong cột `color` của Table `cars`

Sử dụng cú pháp tương tự như trên, sử dụng câu lệnh ALTER COLUMN và từ khóa TYPE theo sao là kiểu dữ liệu muốn thay đổi:

Thay đổi cột `color` từ `VARCHAR(255)` thành `VARCHAR(30)`

```sh
tubt=# ALTER TABLE cars ALTER COLUMN color TYPE VARCHAR(30);
ALTER TABLE
```

# PostgreSQL DROP COLUMN

## ALTER TABLE Statement

Để xóa một cột khỏi Table , chúng ta phải sử dụng câu lệnh ALTER TABLE

Nhắc lại:

Câu lệnh ALTER TABLE được sử dụng để thêm, xóa hoặc sửa đổi các cột trong Table hiện có

Câu lệnh ALTER TABLE cũng được sử dụng để thêm và xóa các ràng buộc khác nhau trên một Table hiện có

## DROP COLUMN

Để xóa cột `color` khỏi Table `cars` hãy sử dụng câu lệnh `DROP COLUMN`:

```sh
tubt=# ALTER TABLE cars DROP COLUMN color;
ALTER TABLE
```

## Display Table

Kiểm tra lại Table sau khi đã xóa cột `color`

```sh
tubt=# SELECT * FROM cars;
 brand  |  model  | year 
--------+---------+------
 BMW    | M1      | 1978
 Volvo  | p1800   | 1968
 Toyota | Celica  | 1970
 Ford   | Mustang | 1964
(4 rows)
```

Như bạn thấy cột `color` đã bị xóa khỏi Table

# PostgreSQL DELETE

## DELETE Statement

Câu lệnh DELETE được sử dụng để xóa các bản ghi hiện có trong Table

NOTE: Hãy cẩn thận khi xóa bản ghi trong Table. Lưu ý mệnh đề WHERE trong câu lệnh DELETE. Mệnh đề WHERE chỉ định các bản ghi nào sẽ bị xóa. Nếu bạn bỏ qua mệnh đề WHERE thì **tất cả các bản ghi trong Table sẽ bị xóa toàn bộ**

Để xóa bản ghi trong đó có `brand` là `Volvo`, hãy sử dụng lệnh sau:

```sh
tubt=# DELETE FROM cars WHERE brand = 'Volvo';
DELETE 1
```

`DELETE 1` ở đây nghĩa là 1 hàng đã bị xóa

## Display Table

Kiểm tra Table sau khi xóa hàng 

```sh
tubt=# SELECT * FROM cars;
 brand  |  model  | year 
--------+---------+------
 BMW    | M1      | 1978
 Toyota | Celica  | 1970
 Ford   | Mustang | 1964
```

Chúng ta thấy hàng có `brand` là `Volvo` đã biến mất sau khi xóa

## Delete All Records

Có thể xóa tất cả các hàng trong Table mà không xóa Table. Điều này có nghĩa là cấu trúc Table, thuộc tính và chỉ mục sẽ được giữ nguyên

Câu lệnh SQL sau đây xoá tất cả các hàng trong Table `cars` mà không xóa Table

```sh
tubt=# DELETE FROM cars;
DELETE 3
```

`DELETE 3`: 3 hàng bị xóa khỏi bảng sau khi chạy lệnh trên

## Display Table

Kiểm tra lại Table sau khi đã xóa tất cả các hàng

```sh
tubt=# SELECT * FROM cars;
 brand | model | year 
-------+-------+------
(0 rows)
```

## TRUNCATE TABLE

Vì chúng ta bỏ qua mệnh đề `WHERE` trong câu lệnh DELETE ở trên nên tất cả các bản ghi sẽ bị xóa khỏi Table `cars`

Ta cũng có thể xóa tương tự với câu lệnh `TRUNCATE TABLE`

Trước tiên chúng ta nên thêm một record cho Table vì hiện tại Table đang trống

```sh
tubt=# INSERT INTO cars (brand, model, year) VALUES ('Ford', 'Mustang', 1964);
```

Thực hiện xóa tất cả record với `TRUNCATE TABLE`

```sh
tubt=# TRUNCATE TABLE cars;
TRUNCATE TABLE
```

## Display Table 

Kiểm tra Table sau khi truncate

```sh
tubt=# SELECT * FROM cars;
 brand | model | year 
-------+-------+------
(0 rows)
```

Record vừa mới tạo đã bị xóa sau khi sử dụng `TRUNCATE TABLE`

# PostgreSQL DROP TABLE

## DROP TABLE Statement 

Câu lệnh `DROP TABLE` để xóa một Table trong Database

Note: Hãy cẩn thận với lệnh này, khi xóa một Table đồng nghĩa với việc dữ liệu được lưu trong đó cũng mất hết

Câu lệnh sau đây sẽ xóa bỏ Table `cars` khỏi cơ sở dữ liệu:

```sh
tubt=# DROP TABLE cars;
DROP TABLE
```

## Display Table

Thử truy vấn vào Table `cars` để xem kết qua trả về

```sh
tubt=# SELECT * FROM cars;
ERROR:  relation "cars" does not exist
LINE 1: SELECT * FROM cars;
                      ^
```

Kết quả trả về cho biết trong cơ sở dữ liệu không có Table nào có tên `cars` vì Table này đã bị xóa bởi `TRUNCATE`