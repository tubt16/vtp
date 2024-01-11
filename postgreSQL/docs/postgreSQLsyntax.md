# Mục lục

[1. PostgreSQL Operator](#postgresqlOperator)

[2. PostgreSQL SELECT](#postgresqlSeclect)

[3. PostgreSQL SELECT](#postgresqlSeclect)

[4. PostgreSQL SELECT DISTINCT](#postgresqlSeclectDistinct)

[5. PostgreSQL WHERE - Filter Data](#postgresqlWhere)

[6. PostgreSQL ORDER BY](#postgresqlORDERBY)

[7. PostgreSQL LIMIT](#postgresqlLIMIT)

[8. PostgreSQL MIN and MAX](#postgresqlMINMAX)

[9. PostgreSQL COUNT](#postgresqlCOUNT)

[10. PostgreSQL SUM](#postgresqlSUM)

[11. PostgreSQL AVG](#postgresqlAVG)

[12. PostgreSQL LIKE](#postgresqlLIKE)

[13. PostgreSQL IN](#postgresqlIN)

[14. PostgreSQL BETWEEN](#postgresqlBETWEEN)

[15. PostgreSQL AS](#postgresqlAS)

[16. PostgreSQL JOIN](#postgresqlJOIN)

[17. PostgreSQL INNER JOIN](#postgresqlINNER_JOIN)

[18. PostgreSQL LEFT JOIN](#postgresqlLEFT_JOIN)

[19. PostgreSQL RIGHT JOIN](#postgresqlRIGHT_JOIN)

[20. PostgreSQL FULL JOIN](#postgresqlFULL_JOIN)

[21. PostgreSQL CROSS JOIN](#postgresqlCROSS_JOIN)

[22. PostgreSQL UNION](#postgresqlUNION)

[23. PostgreSQL GROUP BY](#postgresqlGROUP_BY)

[24. PostgreSQL HAVING](#postgresqlHAVING)

[25. PostgreSQL ANY](#postgresqlANY)

[26. PostgreSQL CASE](#postgresqlCASE)

<a name="postgresqlOperator"></a>
# PostgreSQL Operator

## Các toán tử trong mệnh đề WHERE

- `=`: Equal to

- `<`: Less than

- `>`: Greater than

- `<=`:	Less than or equal to

- `>=`:	Greater than or equal to

- `<>`:	Not equal to

- `!=`:	Not equal to

- `LIKE`: Check if a value matches a pattern (case sensitive)

- `ILIKE`: Check if a value matches a pattern (case insensitive)

- `AND`: Logical AND

- `OR`:	Logical OR

- `IN`:	Check if a value is between a range of values

- `BETWEEN`: Check if a value is between a range of values

- `IS NULL`: Check if a value is NULL

- `NOT`: Makes a negative result e.g. NOT LIKE, NOT IN, NOT BETWEEN

## Create & Insert Table

**Create Table**

```sh
CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
);
```

**Insert Table**

```sh
INSERT INTO cars (brand, model, year)
VALUES
  ('Volvo', 'p1800', 1968),
  ('BMW', 'M1', 1978),
  ('Toyota', 'Celica', 1975);
```

**Select Table**

```sh
mydb=# SELECT * FROM cars;
 brand  | model  | year 
--------+--------+------
 Volvo  | p1800  | 1968
 BMW    | M1     | 1978
 Toyota | Celica | 1975
(3 rows)
```

## Equal To

Toán tử `=` được sử dụng khi bạn muốn trả về tất các các bản ghi trong đó có một cột bằng một giá trị được chỉ định:

**Ví dụ:**

Trả về tất cả các bản ghi có cột `brand` là Volvo

```sh
SELECT * FROM cars WHERE brand = 'Volvo';
```

## Less Than

Toán tử `<` được sử dụng khi bạn muốn trả về tất cả các bản ghi trong đó có một cột nhỏ hơn một giá trị được chỉ định

**Ví dụ:**

Trả về tất cả bản ghi có giá trị nhỏ hơn 1975 trong cột `year`

```sh
SELECT * FROM cars WHERE year < 1975;
```

## Greater Than

Toán tử `>` được sử dụng khi bạn muón trả về tất cả các bản ghi có cột lớn hơn giá trị được chỉ định

**Ví dụ:**

Trả về tất cả bản ghi có giá trị lớn hơn 1975 trong cột `year`

```sh
SELECT * FROM cars WHERE year > 1975;
```

## Less Than or Equal To

Toán tử `<=` được sử dụng khi bạn muốn trả về tất cả các bản ghi trong đó có cột nhỏ hơn hoặc bằng một giá trị được chỉ định

**Ví dụ:**

Trả về tất cả các bản ghi có giá trị nhở hơn hoặc bằng 1975 trong cột `year`

```sh
SELECT * FROM cars WHERE year <= 1975;
```

## Greater Than or Equal to

Toán tử `>=` được sử dụng khi bạn muốn trả về tất các các bản ghi có cột lớn hơn hoặc bằng một giá trị được chỉ định

**Ví dụ:**

Trả về tất cả các bản ghi có giá trị lớn hơn hoặc bằng 1975 trong cột `year`

```sh
SELECT* FROM cars WHERE year >= 1975;
```

## Not Equal To

Toán tử `<>` và `!=` được sử dụng khi bạn muốn trả về tất cả các bản ghi trong đó một cột KHÔNG bằng một giá trị được chỉ định

**Ví dụ:**

Trả về tất cả các bản ghi trong đó cột `brand` không phải là `Volvo`

```sh
SELECT * FROM cars WHERE brand <> 'Volvo';
```

hoặc 

```sh
SELECT * FROM cars WHERE brand != 'Volvo';
```

## LIKE 

Toán tử `LIKE` được sử dụng khi bạn muốn trả về tất cả các bản ghi trong đó một cột bằng một mẫu đã chỉ định

Mẫu có thể là một giá trị tuyệt đối như 'Volvo' hoặc với KÝ TỰ ĐẠI DIỆN có ý nghĩa đặc biệt

Có 2 ký tự đại diện thường được sủ dụng cùng với toán tử `LIKE`:

- Ký hiệu phần trăm `%`, đại diện cho 0, một hoặc nhiều ký tự

- Dấu gạch dưới `_`, đại diện cho một ký tự đơn

**Ví dụ:**

Trả về tất cả các bản ghi trong đó cột `model` bắt đầu với chữ `M` viết HOA

```sh
SELECT * FROM cars WHERE model LIKE 'M%';
```

**Out put**

```sh
mydb=# SELECT * FROM cars WHERE model LIKE 'M%';
 brand | model | year 
-------+-------+------
 BMW   | M1    | 1978
(1 row)
```

Toán tử `LIKE` sẽ phân biệt chữ hoa và chữ thường 

## ILIKE

Tương tự như toán tử LIKE, nhưng ILIKE không phân biệt chữ hoa và chữ thường

**Ví dụ:**

Trả về tất cả các bản ghi trong đó cột `model` bắt đầu với chữ `m` (không phân biệt chữ hoa hay thường)

```sh
SELECT * FROM cars WHERE model ILIKE 'm%';
```

**Output**

```sh
mydb=# SELECT * FROM cars WHERE model ILIKE 'm%';
 brand | model | year 
-------+-------+------
 BMW   | M1    | 1978
(1 row)
```

## AND

Toán tử logic AND được sử dụng khi bạn muốn kiểm tra thêm điều kiện:

Ví dụ:

Trả về tất cả các bản ghi có cột `brand` là `Volvo` và cột `year` là 1968

```sh
mydb=# SELECT * FROM cars WHERE brand = 'Volvo' and year = 1968;
 brand | model | year 
-------+-------+------
 Volvo | p1800 | 1968
(1 row)
```

## OR

Toán tử logic OR được sử dụng khi bạn chỉ cần 1 điều kiện đúng trong nhiều điều kiện được đưa ra

Ví dụ:

Trả về tất crả các bản ghi có cột `brand` là `Volvo` và cột `year` là 1975

```sh
mydb=# SELECT * FROM cars WHERE brand = 'Volvo' or year = 1975;
 brand  | model  | year 
--------+--------+------
 Volvo  | p1800  | 1968
 Toyota | Celica | 1975
(2 rows)
```

## IN

Toán tử `IN` được sử dụng khi giá trị của cột khớp bất kỳ giá trị nào trong danh sách:

Ví dụ: 

Trả về tất cả các bản ghi có cột `brand` chứa các giá trị trong danh sách này (`Volvo`, `Mercedes`, `Ford`)

```sh
mydb=# SELECT * FROM cars WHERE brand IN ('Volvo', 'Mercedes', 'BMW');
 brand | model | year 
-------+-------+------
 Volvo | p1800 | 1968
 BMW   | M1    | 1978
(2 rows)
```

## BETWEEN

Toán tử `BETWEEN` được sử dụng để kiểm tra xem giá trị của cột có nằm trong phạm vị được chỉ định hay không

Ví dụ:

Trả về tất cả các bản ghi có cột `year` nằm trong khoảng từ 1970 đến 1980

```sh
mydb=# SELECT * FROM cars WHERE year BETWEEN 1970 AND 1980;
 brand  | model  | year 
--------+--------+------
 BMW    | M1     | 1978
 Toyota | Celica | 1975
(2 rows)
```

Toán tử `BETWEEN` bao gồm các giá trị `from` và `to`, nghĩa là trong ví dụ trên kết quả cũng sẽ bao gồm cả những cột `year` có giá trị 1970 và 1980

## IS NULL

Toán tử `IS NULL` được sử dụng để kiểm tra xem giá trị của cột có phải là `NULL` hay không

Ví dụ:

Trả về tất cả cac bản ghi cột `model` là NULL

```sh
mydb=# SELECT * FROM cars WHERE model IS NULL;
 brand | model | year 
-------+-------+------
(0 rows)
```

## NOT

Toán tử `NOT` có thể được sử dụng cùng với các toán tử `LIKE`, `ILIKE`, `IN`, `BETWEEN` và `NULL` để đảo ngược giá trị của toán tử

**Ví dụ: `NOT LIKE`**

Trả về tất các các bản ghi trong đó cột `brand` không bắt đầu bằng chữ cái `B` viết HOA 

```sh
mydb=# SELECT * FROM cars WHERE brand NOT LIKE 'B%';
 brand  | model  | year 
--------+--------+------
 Volvo  | p1800  | 1968
 Toyota | Celica | 1975
(2 rows)
```

**Ví dụ: `NOT ILIKE`**

Trả về tất cả các bản ghi trong đó cột `brand` không bắt đầu bằng chữ cái `b` (Cả viết thường lẫn viết hoa)

```sh
mydb=# SELECT * FROM cars WHERE brand NOT ILIKE 'b%';
 brand  | model  | year 
--------+--------+------
 Volvo  | p1800  | 1968
 Toyota | Celica | 1975
(2 rows)
```

**Ví dụ: `NOT IN`**

Trả về tất cả các bản ghi mà cột `brand` KHÔNG CÓ trong danh sách này (`Volvo`, `Mercedes`, `BMW`)

```sh
mydb=# SELECT * FROM cars WHERE brand NOT IN ('Volvo', 'Mercedes', 'BMW');
 brand  | model  | year 
--------+--------+------
 Toyota | Celica | 1975
(1 row)
```

**Ví dụ: `NOT BETWEEN`**

Trả về tất cả các bản ghi trong đó cột `year` KHÔNG nằm trong khoảng từ 1970 đến 1980

```sh
mydb=# SELECT * FROM cars WHERE year NOT BETWEEN 1970 AND 1980;
 brand | model | year 
-------+-------+------
 Volvo | p1800 | 1968
(1 row)
```

Lưu ý: Toán tử `NOT BETWEEN` loại trừ các giá trị from và to, nghĩa là trong ví dụ trên, kết quả sẽ không bao gồm giá trị 1970 và 1980 trong cột `year`

**Ví dụ: `IS NOT NULL`**

Trả về tất cả các bản ghi trong đó cột `model` không rỗng

```sh
mydb=# SELECT * FROM cars WHERE model IS NOT NULL;
 brand  | model  | year 
--------+--------+------
 Volvo  | p1800  | 1968
 BMW    | M1     | 1978
 Toyota | Celica | 1975
(3 rows)
```

<a name="postgresqlSeclect"></a>
# PostgreSQL SELECT

Nhắc lại kiến thức cũ

## Select Data

Để lấy dữ liệu từ cơ sở dữ liệu, chúng ta sử dụng SELECT

## Specify Columns

Bằng cách chỉ định tên cột , chúng ta có thể SELECT cột cần truy xuất:

Ví dụ: Chỉ SELECT cột `brand` và `model` trong Table `cars`

```sh
mydb=# SELECT brand, model FROM cars;
 brand  | model  
--------+--------
 Volvo  | p1800
 BMW    | M1
 Toyota | Celica
(3 rows)
```

## Return All Columns

Chỉ định `*` thay vì tên cột để trả về giá trị của tất cả các cột

Ví dụ: 

```sh
mydb=# SELECT * FROM cars;
 brand  | model  | year 
--------+--------+------
 Volvo  | p1800  | 1968
 BMW    | M1     | 1978
 Toyota | Celica | 1975
(3 rows)
```

<a name="postgresqlSeclectDistinct"></a>
# PostgreSQL SELECT DISTINCT

## SELECT DISTINCT Statement

Câu lệnh SELECT DISTINCT được sử dụng để CHỈ trả về các giá trị RIÊNG BIỆT KHÁC NHAU

Bên trong một Table, một cột thường chứa nhiều giá trị trùng lặp và đôi khi bạn chỉ muốn liệt kê các giá trị RIÊNG BIỆT KHÁC NHAU

Ví dụ:

Chỉ chọn các giá trị DISTINCT từ cột `country` trong Table `customer`. Table này đã được tạo từ phần trước, có thể xem phần đó ở [đây](./import&exportPostgresDB.md)

```sh
testdb=# SELECT DISTINCT country FROM customers;
   country   
-------------
 Argentina
 Spain
 Switzerland
 Italy
 Venezuela
 Belgium
 Norway
 Sweden
 USA
 France
 Mexico
 Brazil
 Austria
 Poland
 UK
 Ireland
 Germany
 Denmark
 Canada
 Finland
 Portugal
(21 rows)
```

Mặc dù Table `customers` có 91 record nhưng nó chỉ có 21 quốc gia khác nhau tồn tại trong Table và đó là kết quả bạn nhận được khi thực hiện câu lệnh trên (Output: `21 rows`)

## SELECT COUNT (DISTINCT)

Chúng ta cũng có thể sử dụng từ khóa DISTINCT kết hợp với câu lệnh COUNT, trong ví dụ bên dưới sẽ trả về SỐ LƯỢNG quốc gia khác nhau có trong Table `customers` 

Trả về SỐ LƯỢNG quốc gia khác nhau có trong Table `customers`

```sh
testdb=# SELECT COUNT(DISTINCT country) FROM customers;
 count 
-------
    21
(1 row)
```

<a name="postgresqlWhere"></a>
# PostgreSQL WHERE - Filter Data

## Filter Records

Mệnh đề `WHERE` được sử dụng để lọc các record

Nó được sử dụng để trích xuất một bản ghi đáp ứng một điều kiện cụ thể

Ví dụ:

Nếu chúng ta chỉ muốn trả về những bản ghi có cột `city` là `London`, chúng ta có thể chỉ định điều đó trong mệnh đề `WHERE`

```sh
testdb=# SELECT * FROM customers WHERE city = 'London';
 customer_id |     customer_name     |   contact_name    |           address            |  city  | postal_code | country 
-------------+-----------------------+-------------------+------------------------------+--------+-------------+---------           4 | Around the Horn       | Thomas Hardy      | 120 Hanover Sq.              | London | WA1 1DP     | UK
          11 | Bs Beverages          | Victoria Ashworth | Fauntleroy Circus            | London | EC2 5NT     | UK
          16 | Consolidated Holdings | Elizabeth Brown   | Berkeley Gardens 12 Brewery  | London | WX1 6LT     | UK
          19 | Eastern Connection    | Ann Devon         | 35 King George               | London | WX3 6FW     | UK
          53 | North/South           | Simon Crowther    | South House 300 Queensbridge | London | SW7 1RZ     | UK
          72 | Seven Seas Imports    | Hari Kumar        | 90 Wadhurst Rd.              | London | OX15 4NB    | UK
(6 rows)
```

## Text Fields so với Numberic Fields

PostgreSQL yêu cầu dấu nháy đơn xung quanh các giá trị văn bản

Tuy nhiên các trường số sẽ không đặt trong dấu nháy đơn

Ví dụ:

```sh
testdb=# SELECT * FROM customers WHERE customer_id = 19;
 customer_id |   customer_name    | contact_name |    address     |  city  | postal_code | country 
-------------+--------------------+--------------+----------------+--------+-------------+---------
          19 | Eastern Connection | Ann Devon    | 35 King George | London | WX3 6FW     | UK
(1 row)
```

## Greater than

Sử dụng toán tử `>` để lấy tất cả các records có `custom_id` lớn hơn 80

```sh
testdb=# SELECT * FROM customers WHERE customer_id > 80;
 customer_id |          customer_name           |   contact_name    |           address           |   city    | postal_code | country 
-------------+----------------------------------+-------------------+-----------------------------+-----------+-------------+---------
          81 | Tradicao Hipermercados           | Anabela Domingues | Av. Ines de Castro, 414     | Sao Paulo | 05634-030   | Brazil
          82 | Trails Head Gourmet Provisioners | Helvetius Nagy    | 722 DaVinci Blvd.           | Kirkland  | 98034    
   | USA
          83 | Vaffeljernet                     | Palle Ibsen       | Smagsloget 45               | Arhus     | 8200     
   | Denmark
          84 | Victuailles en stock             | Mary Saveley      | 2, rue du Commerce          | Lyon      | 69004    
   | France
          85 | Vins et alcools Chevalier        | Paul Henriot      | 59 rue de l Abbaye          | Reims     | 51100    
   | France
          86 | Die Wandernde Kuh                | Rita Moller       | Adenauerallee 900           | Stuttgart | 70563    
   | Germany
          87 | Wartian Herkku                   | Pirkko Koskitalo  | Torikatu 38                 | Oulu      | 90110    
   | Finland
          88 | Wellington Importadora           | Paula Parente     | Rua do Mercado, 12          | Resende   | 08737-363   | Brazil
          89 | White Clover Markets             | Karl Jablonski    | 305 - 14th Ave. S. Suite 3B | Seattle   | 98128    
   | USA
          90 | Wilman Kala                      | Matti Karttunen   | Keskuskatu 45               | Helsinki  | 21240    
   | Finland
          91 | Wolski                           | Zbyszek           | ul. Filtrowa 68             | Walla     | 01-012   
   | Poland
(11 rows)
```

<a name="postgresqlORDERBY"></a>
# PostgreSQL ORDER BY

## Sort Data

Từ khóa `ORDER BY` được sử dụng để sắp xếp kết quả theo thứ tự tăng dần hoặc giảm dần

Từ khóa `ORDER BY` sắp xếp các record theo thứ tự tăng dần (mặc định). Để sắp xếp theo thứ tự giảm dần, hãy sử dụng từ khóa `DESC`

Ví dụ:

Sắp xếp Table theo cột `price`

```sh
testdb=# SELECT * FROM products ORDER BY price;
 product_id |           product_name           | category_id |         unit         | price  
------------+----------------------------------+-------------+----------------------+--------
         33 | Geitost                          |           4 | 500 g                |   2.50
         24 | Guarani Fantastica               |           1 | 12 - 355 ml cans     |   4.50
         13 | Konbu                            |           8 | 2 kg box             |   6.00
         52 | Filo Mix                         |           5 | 16 - 2 kg boxes      |   7.00
         54 | Tourtiare                        |           6 | 16 pies              |   7.45
         75 | Rhenbreu Klosterbier             |           1 | 24 - 0.5 l bottles   |   7.75
         23 | Tunnbrod                         |           5 | 12 - 250 g pkgs.     |   9.00
         19 | Teatime Chocolate Biscuits       |           3 | 10 boxes x 12 pieces |   9.20
         47 | Zaanse koeken                    |           3 | 10 - 4 oz boxes      |   9.50
         45 | Rogede sild                      |           8 | 1k pkg.              |   9.50
         41 | Jacks New England Clam Chowder   |           8 | 12 - 12 oz cans      |   9.65
         74 | Longlife Tofu                    |           7 | 5 kg pkg.            |  10.00
          3 | Aniseed Syrup                    |           2 | 12 - 550 ml bottles  |  10.00
         21 | Sir Rodneys Scones               |           3 | 24 pkgs. x 4 pieces  |  10.00
         46 | Spegesild                        |           8 | 4 - 450 g glasses    |  12.00
         31 | Gorgonzola Telino                |           4 | 12 - 100 g pkgs      |  12.50
         68 | Scottish Longbreads              |           3 | 10 boxes x 8 pieces  |  12.50
         48 | Chocolade                        |           3 | 10 pkgs.             |  12.75
         77 | Original Frankfurter gr�ne Soae  |           2 | 12 boxes             |  13.00
         58 | Escargots de Bourgogne           |           8 | 24 pieces            |  13.25
         42 | Singaporean Hokkien Fried Mee    |           5 | 32 - 1 kg pkgs.      |  14.00
         34 | Sasquatch Ale                    |           1 | 24 - 12 oz bottles   |  14.00
         67 | Laughing Lumberjack Lager        |           1 | 24 - 12 oz bottles   |  14.00
         25 | NuNuCa Nui-Nougat-Creme          |           3 | 20 - 450 g glasses   |  14.00
         73 | Red Kaviar                       |           8 | 24 - 150 g jars      |  15.00
         70 | Outback Lager                    |           1 | 24 - 355 ml bottles  |  15.00
         15 | Genen Shouyu                     |           2 | 24 - 250 ml bottles  |  15.50
         50 | Valkoinen suklaa                 |           3 | 12 - 100 g bars      |  16.25
         66 | Louisiana Hot Spiced Okra        |           2 | 24 - 8 oz jars       |  17.00
         16 | Pavlova                          |           3 | 32 - 500 g boxes     |  17.45
         39 | Chartreuse verte                 |           1 | 750 cc per bottle    |  18.00
         35 | Steeleye Stout                   |           1 | 24 - 12 oz bottles   |  18.00
          1 | Chais                            |           1 | 10 boxes x 20 bags   |  18.00
         76 | Lakkalikeeri                     |           1 | 500 ml               |  18.00
         40 | Boston Crab Meat                 |           8 | 24 - 4 oz tins       |  18.40
         36 | Inlagd Sill                      |           8 | 24 - 250 g jars      |  19.00
          2 | Chang                            |           1 | 24 - 12 oz bottles   |  19.00
         44 | Gula Malacca                     |           2 | 20 - 2 kg bags       |  19.45
         57 | Ravioli Angelo                   |           5 | 24 - 250 g pkgs.     |  19.50
         49 | Maxilaku                         |           3 | 24 - 50 g pkgs.      |  20.00
         11 | Queso Cabrales                   |           4 | 1 kg pkg.            |  21.00
         22 | Gustafs Kneckebrod               |           5 | 24 - 500 g pkgs.     |  21.00
         65 | Louisiana Fiery Hot Pepper Sauce |           2 | 32 - 8 oz bottles    |  21.05
          5 | Chef Antons Gumbo Mix            |           2 | 36 boxes             |  21.35
         71 | Flotemysost                      |           4 | 10 - 500 g pkgs.     |  21.50
          4 | Chef Antons Cajun Seasoning      |           2 | 48 - 6 oz jars       |  22.00
         14 | Tofu                             |           7 | 40 - 100 g pkgs.     |  23.25
         55 | Pate chinois                     |           6 | 24 boxes x 2 pies    |  24.00
          6 | Grandmas Boysenberry Spread      |           2 | 12 - 8 oz jars       |  25.00
         30 | Nord-Ost Matjeshering            |           8 | 10 - 200 g glasses   |  25.89
         37 | Gravad lax                       |           8 | 12 - 500 g pkgs.     |  26.00
         61 | Sirop d arable                   |           2 | 24 - 500 ml bottles  |  28.50
          7 | Uncle Bobs Organic Dried Pears   |           7 | 12 - 1 lb pkgs.      |  30.00
         10 | Ikura                            |           8 | 12 - 200 ml jars     |  31.00
         26 | Gumber Gummiberchen              |           3 | 100 - 250 g bags     |  31.23
         32 | Mascarpone Fabioli               |           4 | 24 - 200 g pkgs.     |  32.00
         53 | Perth Pasties                    |           6 | 48 pieces            |  32.80
         64 | Wimmers gute Semmelknadel        |           5 | 20 bags x 4 pieces   |  33.25
         60 | Camembert Pierrot                |           4 | 15 - 300 g rounds    |  34.00
         72 | Mozzarella di Giovanni           |           4 | 24 - 200 g pkgs.     |  34.80
         69 | Gudbrandsdalsost                 |           4 | 10 kg pkg.           |  36.00
         56 | Gnocchi di nonna Alice           |           5 | 24 - 250 g pkgs.     |  38.00
         12 | Queso Manchego La Pastora        |           4 | 10 - 500 g pkgs.     |  38.00
         17 | Alice Mutton                     |           6 | 20 - 1 kg tins       |  39.00
          8 | Northwoods Cranberry Sauce       |           2 | 12 - 12 oz jars      |  40.00
         27 | Schoggi Schokolade               |           3 | 100 - 100 g pieces   |  43.90
         63 | Vegie-spread                     |           2 | 15 - 625 g jars      |  43.90
         28 | Rassle Sauerkraut                |           7 | 25 - 825 g cans      |  45.60
         43 | Ipoh Coffee                      |           1 | 16 - 500 g tins      |  46.00
         62 | Tarte au sucre                   |           3 | 48 pies              |  49.30
         51 | Manjimup Dried Apples            |           7 | 50 - 300 g pkgs.     |  53.00
         59 | Raclette Courdavault             |           4 | 5 kg pkg.            |  55.00
         18 | Carnarvon Tigers                 |           8 | 16 kg pkg.           |  62.50
         20 | Sir Rodneys Marmalade            |           3 | 30 gift boxes        |  81.00
          9 | Mishi Kobe Niku                  |           6 | 18 - 500 g pkgs.     |  97.00
         29 | Thoringer Rostbratwurst          |           6 | 50 bags x 30 sausgs. | 123.79
         38 | Cote de Blaye                    |           1 | 12 - 75 cl bottles   | 263.50
(77 rows)
```

## DESC

Ngược lại với `ORDER BY`. Để sắp xếp các bản ghi theo thứ tự giảm dần, hãy sử dụng từ khóa `DESC`

Ví dụ:

Sắp xếp cột `price` trong Table `products` theo thứ tự giảm dần

```sh
SELECT * FROM products ORDER BY price DESC;
```

## Sort Alphabetically

Đối với các giá trị là string thì `ORDER BY` sẽ sắp xếp theo thứ tự bảng chữ cái:

Sắp xếp cột `description`

```sh
testdb=# SELECT * FROM categories ORDER BY description;
 category_id | category_name  |                        description                         
-------------+----------------+------------------------------------------------------------
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
           4 | Dairy Products | Cheeses
           3 | Confections    | Desserts, candies, and sweet breads
           7 | Produce        | Dried fruit and bean curd
           6 | Meat/Poultry   | Prepared meats
           8 | Seafood        | Seaweed and fish
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
(8 rows)
```

## Alphabetically DESC

Sắp xếp ngược cột `description`

```sh
testdb=# SELECT * FROM categories ORDER BY description DESC;
 category_id | category_name  |                        description                         
-------------+----------------+------------------------------------------------------------
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           8 | Seafood        | Seaweed and fish
           6 | Meat/Poultry   | Prepared meats
           7 | Produce        | Dried fruit and bean curd
           3 | Confections    | Desserts, candies, and sweet breads
           4 | Dairy Products | Cheeses
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
(8 rows)
```

<a name="postgresqlLIMIT"></a>
# PostgreSQL LIMIT

## LIMIT Clause

Mệnh đề LIMIT được sử dụng để giới hạn số lượng bản ghi tối đa được trả về

Ví dụ:

Chỉ trả về 10 bản ghi đầu tiên từ Table `products`:

```sh
testdb=# SELECT * FROM products LIMIT 10;
 product_id |          product_name          | category_id |        unit         | price 
------------+--------------------------------+-------------+---------------------+-------
          1 | Chais                          |           1 | 10 boxes x 20 bags  | 18.00
          2 | Chang                          |           1 | 24 - 12 oz bottles  | 19.00
          3 | Aniseed Syrup                  |           2 | 12 - 550 ml bottles | 10.00
          4 | Chef Antons Cajun Seasoning    |           2 | 48 - 6 oz jars      | 22.00
          5 | Chef Antons Gumbo Mix          |           2 | 36 boxes            | 21.35
          6 | Grandmas Boysenberry Spread    |           2 | 12 - 8 oz jars      | 25.00
          7 | Uncle Bobs Organic Dried Pears |           7 | 12 - 1 lb pkgs.     | 30.00
          8 | Northwoods Cranberry Sauce     |           2 | 12 - 12 oz jars     | 40.00
          9 | Mishi Kobe Niku                |           6 | 18 - 500 g pkgs.    | 97.00
         10 | Ikura                          |           8 | 12 - 200 ml jars    | 31.00
(10 rows)
```

## OFFSET Clause

Mệnh đề `OFFSET` được sử dụng để chỉ định nơi bắt đầu chọn các bản ghi để trả về

Nếu bạn muốn trả về 10 bản ghi nhưng bắt đầu ở bản ghi thứ 40, bạn có thể sử dụng cả LIMIT và OFFSET để thực hiện điều đó:

```sh
testdb=# SELECT * FROM products LIMIT 10 OFFSET 40;
 product_id |          product_name          | category_id |       unit        | price 
------------+--------------------------------+-------------+-------------------+-------
         41 | Jacks New England Clam Chowder |           8 | 12 - 12 oz cans   |  9.65
         42 | Singaporean Hokkien Fried Mee  |           5 | 32 - 1 kg pkgs.   | 14.00
         43 | Ipoh Coffee                    |           1 | 16 - 500 g tins   | 46.00
         44 | Gula Malacca                   |           2 | 20 - 2 kg bags    | 19.45
         45 | Rogede sild                    |           8 | 1k pkg.           |  9.50
         46 | Spegesild                      |           8 | 4 - 450 g glasses | 12.00
         47 | Zaanse koeken                  |           3 | 10 - 4 oz boxes   |  9.50
         48 | Chocolade                      |           3 | 10 pkgs.          | 12.75
         49 | Maxilaku                       |           3 | 24 - 50 g pkgs.   | 20.00
         50 | Valkoinen suklaa               |           3 | 12 - 100 g bars   | 16.25
(10 rows)
```

<a name="postgresqlMINMAX"></a>
# PostgreSQL MIN and MAX

## MIN

Hàm MIN() trả về giá trị nhỏ nhất trong cột chỉ định

Ví dụ:

Trả về giá trị thấp nhất của cột `prince` trong Table `products`

```sh
testdb=# SELECT MIN(price) FROM products;
 min  
------
 2.50
(1 row)
```

## MAX

Ngược lại với hàm MIN() hàm MAX() trả về giá trị lớn nhất trong cột chỉ định

Ví dụ:

Trả về giá trị lớn nhất của cột `prince` trong Table `products`

```sh
testdb=# SELECT MAX(price) FROM products;
  max   
--------
 263.50
(1 row)
```

## Set Column Name

Khi bạn sử dụng `MIN()` hoặc `MAX()` cột trả về sẽ được đặt tên là `min` hoặc `max` theo mặc định. Để đặt tên mới cho cột, hãy sử dụng từ khóa `AS`

Ví dụ:

Trả về giá trị thấp nhất và đặt tên cột `lowest_price`

```sh
testdb=# SELECT MIN(price) AS lowest_price FROM products;
 lowest_price 
--------------
         2.50
(1 row)
```

<a name="postgresqlCOUNT"></a>
# PostgreSQL COUNT

## COUNT

Hàm COUNT() trả về số hàng khớp tiêu chí đã chỉ định

Nếu tiêu chí trả về là tên cột thì hàm COUNT() trả về cột có tên đó:

Ví dụ:

Trả về số lượng khách hàng từ Table khách hàng

```sh
testdb=# SELECT COUNT(customer_id) FROM customers;
 count 
-------
    91
(1 row)
```

Note: Giá trị NULL không được đếm

Bằng cách sử dụng mệnh đề `WHERE`, bạn có thể lấy được giá trị mong muốn từ cột trong Table

Ví dụ:

Tìm kiếm trong cột `city` các giá trị `Lodon` và trả về số lượng tìm thấy (Những khách hàng đến từ Lodon được lưu trong Table)

```sh
testdb=# SELECT COUNT(customer_id) FROM customers WHERE city = 'London';
 count 
-------
     6
(1 row)
```

<a name="postgresqlSUM"></a>
# PostgreSQL SUM

## SUM

Hàm SUM() trả về tổng của một cột có giá trị số (numberic)

Câu lệnh SQL sau đầy tìm tổng của các trường `price` trong Table `products`

```sh
testdb=# SELECT SUM(price) FROM products;
   sum   
---------
 2222.71
(1 row)
```

NOTE: Giá trị NULL bị bỏ qua

<a name="postgresqlAVG"></a>
# PostgreSQL AVG

## AVG

Hàm AVG() trả về giá trị trung bình của một cột số (numberic)

Ví dụ:

Trả về giá trị trung bình của cột `price` trong Table `products`

```sh
testdb=# SELECT AVG(price) FROM products;
         avg         
---------------------
 28.8663636363636364
(1 row)
```

NOTE: Các giá trị NULL bị bỏ qua

## WITH 2 Decimals

Ví dụ trên trả về giá trị trung bình của tất cả các sản phẩm, kết quả là `28.8663636363636364`

Chúng ta có thể sử dụng toán tử `::NUMERIC` để làm tròn giá trị trung bình thành một số có 2 số thập phân

Ví dụ:

Trả về giá trị trung bình của cột `price` trong Table `products` làm tròn đến 2 số thập phân

```sh
testdb=# SELECT AVG(price)::NUMERIC(10,2) FROM products;
  avg  
-------
 28.87
(1 row)
```

<a name="postgresqlLIKE"></a>
# PostgreSQl LIKE

## LIKE

**Nhắc lại**

Toán tử LIKE được sử dụng trong mệnh đề WHERE để tìm kiếm mẫu được chỉ định trong một cột

Có 2 ký tự đại diện thường được sử dụng cùng với toán tử LIKE

- `%`: Dấu `%` đại diện cho 0, 1 hoặc nhiều ký tự

- `_`: Dấu gạch dưới đại diện cho một kí tự đơn

Để trả về các bản ghi bắt đầu bằng một chữ cái hoặc cụm từ cụ thể, hãy thêm % vào cuối chữ cái hoặc cụm từ đó

Trả về cột `customer_name` có giá trị bắt đầu bằng chữ cái `A`

```sh
testdb=# SELECT * FROM customers WHERE customer_name LIKE 'A%';
 customer_id |           customer_name            |  contact_name  |            address            |    city     | postal_code | country 
-------------+------------------------------------+----------------+-------------------------------+-------------+-------------+---------
           1 | Alfreds Futterkiste                | Maria Anders   | Obere Str. 57                 | Berlin      | 12209       | Germany
           2 | Ana Trujillo Emparedados y helados | Ana Trujillo   | Avda. de la Constitucion 2222 | Mexico D.F. | 05021       | Mexico
           3 | Antonio Moreno Taquera             | Antonio Moreno | Mataderos 2312                | Mexico D.F. | 05023       | Mexico
           4 | Around the Horn                    | Thomas Hardy   | 120 Hanover Sq.               | London      | WA1 1DP     | UK
(4 rows)
```

## Contains

Để trả về bẳn ghi có chứa một chữ cái hoặc cụm từ cụ thể, hãy thêm % cả trước và sau chữ cái hoặc cụm từ đó

Ví dụ:

Trả về cột `customer_name` có giá trị chứa chữ `Al`

```sh
testdb=# SELECT * FROM customers WHERE customer_name LIKE '%Al%';
 customer_id |        customer_name         |    contact_name    |         address         |  city   | postal_code | country 
-------------+------------------------------+--------------------+-------------------------+---------+-------------+---------
           1 | Alfreds Futterkiste          | Maria Anders       | Obere Str. 57           | Berlin  | 12209       | Germany
          37 | Hungry Owl All-Night Grocers | Patricia McKenna   | 8 Johnstown Road        | Cork    |             | Ireland
          49 | Magazzini Alimentari Riuniti | Giovanni Rovelli   | Via Ludovico il Moro 22 | Bergamo | 24100       | Italy
          75 | Split Rail Beer & Ale        | Art Braunschweiger | P.O. Box 555            | Lander  | 82520       | USA
(4 rows)
```

## ILIKE

Cung giống như `LIKE` tuy nhiên `ILIKE` sẽ không phân biệt chữ hoa chữ thường

Ví dụ: 

Trả về cột `customer_name` có giá trị chứa chữ cái `AL`, `aL`, `Al` hoặc `al`

```sh
testdb=# SELECT * FROM customers WHERE customer_name LIKE '%al%';
 customer_id |            customer_name             |   contact_name    |         address         |    city     | postal_code | country  
-------------+--------------------------------------+-------------------+-------------------------+-------------+-------------+----------
          13 | Centro comercial Moctezuma           | Francisco Chang   | Sierras de Granada 9993 | Mexico D.F. | 05022       | Mexico          21 | Familia Arquibaldo                   | Aria Cruz         | Rua Oros, 92            | Sao Paulo   | 05442-030   | Brazil          22 | FISSA Fabrica Inter. Salchichas S.A. | Diego Roel        | C/ Moralzarzal, 86      | Madrid      | 28034       | Spain
          28 | Furia Bacalhau e Frutos do Mar       | Lino Rodriguez    | Jardim das rosas n. 32  | Lisboa      | 1675        | Portugal
          29 | Galeria del gastronomo               | Eduardo Saavedra  | Rambla de Cataluna, 23  | Barcelona   | 08022       | Spain
          57 | Paris specialites                    | Marie Bertrand    | 265, boulevard Charonne | Paris       | 75012       | France          74 | Specialites du monde                 | Dominique Perrier | 25, rue Lauriston       | Paris       | 75016       | France          79 | Toms Spezialiteten                   | Karin Josephs     | Luisenstr. 48           | Manster     | 44087       | Germany
          85 | Vins et alcools Chevalier            | Paul Henriot      | 59 rue de l Abbaye      | Reims       | 51100       | France          90 | Wilman Kala                          | Matti Karttunen   | Keskuskatu 45           | Helsinki    | 21240       | Finland
(10 rows)
```

## Ends with

Để trả về các bản ghi kết thúc bằng một chữ cái hoặc cụm từ cụ thể, hãy thêm % trước chữ cái hoặc cụm từ đó

Ví dụ

```sh
testdb=# SELECT * FROM customers WHERE customer_name LIKE '%en';
 customer_id |      customer_name      |    contact_name     |      address       |    city     | postal_code | country 
-------------+-------------------------+---------------------+--------------------+-------------+-------------+---------
           6 | Blauer See Delikatessen | Hanna Moos          | Forsterstr. 57     | Mannheim    | 68306       | Germany
          39 | Koniglich Essen         | Philip Cramer       | Maubelstr. 90      | Brandenburg | 14776       | Germany
          55 | Old World Delicatessen  | Rene Phillips       | 2743 Bering St.    | Anchorage   | 99508       | USA
          56 | Ottilies Keseladen      | Henriette Pfalzheim | Mehrheimerstr. 369 | Koln        | 50739       | Germany
          79 | Toms Spezialiteten      | Karin Josephs       | Luisenstr. 48      | Manster     | 44087       | Germany
(5 rows)
```

## The Undescore `_` Wildcard

Ký tự `_` đại diện cho một ký tự đơn

Nó có thể là bất kỳ ký tự hoặc số nào, nhưng mỗi `_` đại diện cho MỘT và chỉ MỘT ký tự

Ví dụ:

Trả về kết quả là giá trị bắt đầu bằng chữ `L` tiếp đó là một ký tự đại diện `_`, sau đó là chữ `nd` và cuối cùng là 2 ký tự đại diện `__`

```sh
testdb-# SELECT * FROM customers WHERE city LIKE 'L_nd__';
 customer_id |     customer_name     |    contact_name    |           address            |  city  | postal_code | country 
-------------+-----------------------+--------------------+------------------------------+--------+-------------+---------
           4 | Around the Horn       | Thomas Hardy       | 120 Hanover Sq.              | London | WA1 1DP     | UK
          11 | Bs Beverages          | Victoria Ashworth  | Fauntleroy Circus            | London | EC2 5NT     | UK
          16 | Consolidated Holdings | Elizabeth Brown    | Berkeley Gardens 12 Brewery  | London | WX1 6LT     | UK
          19 | Eastern Connection    | Ann Devon          | 35 King George               | London | WX3 6FW     | UK
          53 | North/South           | Simon Crowther     | South House 300 Queensbridge | London | SW7 1RZ     | UK
          72 | Seven Seas Imports    | Hari Kumar         | 90 Wadhurst Rd.              | London | OX15 4NB    | UK
          75 | Split Rail Beer & Ale | Art Braunschweiger | P.O. Box 555                 | Lander | 82520       | USA
(7 rows)
```

<a name="postgresqlIN"></a>
# PostgreSQL IN

## IN

Toán tử IN cho phép bạn chỉ định danh sách các giá trị có thể có trong mệnh đề WHERE

**Toán tử IN là cách viết tắt của nhiều điều kiện OR**

Ví dụ:

Trả về tất cả giá trị `France` và `UK` trong cột `country` của Table `customers`

```sh
testdb=#  SELECT * FROM customers WHERE country IN ('France', 'UK');
 customer_id |       customer_name       |    contact_name    |           address            |    city    | postal_code | country 
-------------+---------------------------+--------------------+------------------------------+------------+-------------+---------
           4 | Around the Horn           | Thomas Hardy       | 120 Hanover Sq.              | London     | WA1 1DP     | UK
           7 | Blondel pere et fils      | Frederique Citeaux | 24, place Kleber             | Strasbourg | 67000       | France
           9 | Bon app                   | Laurence Lebihans  | 12, rue des Bouchers         | Marseille  | 13008       | France
          11 | Bs Beverages              | Victoria Ashworth  | Fauntleroy Circus            | London     | EC2 5NT     | UK
          16 | Consolidated Holdings     | Elizabeth Brown    | Berkeley Gardens 12 Brewery  | London     | WX1 6LT     | UK
          18 | Du monde entier           | Janine Labrune     | 67, rue des Cinquante Otages | Nantes     | 44000       | France
          19 | Eastern Connection        | Ann Devon          | 35 King George               | London     | WX3 6FW     | UK
          23 | Folies gourmandes         | Martine Rance      | 184, chaussee de Tournai     | Lille      | 59000       | France
          26 | France restauration       | Carine Schmitt     | 54, rue Royale               | Nantes     | 44000       | France
          38 | Island Trading            | Helen Bennett      | Garden House Crowther Way    | Cowes      | PO31 7PJ    | UK
          40 | La corne d abondance      | Daniel Tonini      | 67, avenue de l Europe       | Versailles | 78000       | France
          41 | La maison d Asie          | Annette Roulet     | 1 rue Alsace-Lorraine        | Toulouse   | 31000       | France
          53 | North/South               | Simon Crowther     | South House 300 Queensbridge | London     | SW7 1RZ     | UK
          57 | Paris specialites         | Marie Bertrand     | 265, boulevard Charonne      | Paris      | 75012       | France
          72 | Seven Seas Imports        | Hari Kumar         | 90 Wadhurst Rd.              | London     | OX15 4NB    | UK
          74 | Specialites du monde      | Dominique Perrier  | 25, rue Lauriston            | Paris      | 75016       | France
          84 | Victuailles en stock      | Mary Saveley       | 2, rue du Commerce           | Lyon       | 69004       | France
          85 | Vins et alcools Chevalier | Paul Henriot       | 59 rue de l Abbaye           | Reims      | 51100       | France
(18 rows)
```

## NOT IN

Bằng cách sử dụng từ khóa NOT phía trước toán tử IN, bạn có thể trả về tất cả các bản ghi KHÔNG có bất cứ giá trị nào trong danh sách

Ví dụ:

Trả về tất cả giá trị trong cột `country` ngoại trừ các giá trị `France`, `Germany` và `UK`

```sh
SELECT * FROM customers WHERE country NOT IN ('France', 'Germany', 'UK');
```

## IN (SELECT)

Bạn cũng có thể sử dụng câu lệnh SELECT bên trong dấu ngoặc đơn để trả về tất cả các bản ghi nằm trong kết quả của câu lệnh SELECT

Ví dụ:

```sh
testdb=# SELECT * FROM categories WHERE category_id IN (SELECT customer_id FROM customers);
 category_id | category_name  |                        description                         
-------------+----------------+------------------------------------------------------------
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
           3 | Confections    | Desserts, candies, and sweet breads
           4 | Dairy Products | Cheeses
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
           6 | Meat/Poultry   | Prepared meats
           7 | Produce        | Dried fruit and bean curd
           8 | Seafood        | Seaweed and fish
(8 rows)
```

## NOT IN (SELECT)

Kết quả ở trên trả về 8 record vì OUTPUT của lệnh SELECT thứ 2 chạy từ 0 đến 91, nếu chúng ta sử dụng NOT IN thì tất cả giá trị sẽ từ record 0 đến 91 sẽ không được in ra

Ví dụ:

```sh
testdb=# SELECT * FROM categories WHERE category_id NOT IN (SELECT customer_id FROM customers);
 category_id | category_name | description 
-------------+---------------+-------------
(0 rows)
```

<a name="postgresqlBETWEEN"></a>
# PostgreSQL BETWEEN

## BETWEEN

Toán tử `BETWEEN` chọn các giá trị trong một phạm vi nhất định. Các giá trị có thể là số, văn bản hoặc ngày tháng

Toán tử `BETWEEN` mang tính bao gồm: Giá trị bắt đầu và kết thúc được bao gồm

Ví dụ:

Tìm trong Table `products` cột `price` giá trị từ 10 đến 15

```sh
testdb=# SELECT * FROM products WHERE price BETWEEN 10 and 15;
 product_id |          product_name           | category_id |        unit         | price 
------------+---------------------------------+-------------+---------------------+-------
          3 | Aniseed Syrup                   |           2 | 12 - 550 ml bottles | 10.00
         21 | Sir Rodneys Scones              |           3 | 24 pkgs. x 4 pieces | 10.00
         25 | NuNuCa Nui-Nougat-Creme         |           3 | 20 - 450 g glasses  | 14.00
         31 | Gorgonzola Telino               |           4 | 12 - 100 g pkgs     | 12.50
         34 | Sasquatch Ale                   |           1 | 24 - 12 oz bottles  | 14.00
         42 | Singaporean Hokkien Fried Mee   |           5 | 32 - 1 kg pkgs.     | 14.00
         46 | Spegesild                       |           8 | 4 - 450 g glasses   | 12.00
         48 | Chocolade                       |           3 | 10 pkgs.            | 12.75
         58 | Escargots de Bourgogne          |           8 | 24 pieces           | 13.25
         67 | Laughing Lumberjack Lager       |           1 | 24 - 12 oz bottles  | 14.00
         68 | Scottish Longbreads             |           3 | 10 boxes x 8 pieces | 12.50
         70 | Outback Lager                   |           1 | 24 - 355 ml bottles | 15.00
         73 | Red Kaviar                      |           8 | 24 - 150 g jars     | 15.00
         74 | Longlife Tofu                   |           7 | 5 kg pkg.           | 10.00
         77 | Original Frankfurter gr�ne Soae |           2 | 12 boxes            | 13.00
(15 rows)
```

## BETWEEN Text Values

Toán tử `BETWEEN` cũng có thể được sử dụng trên các giá trị văn bản

Kết qủa trả về tất cả các record được sắp xếp theo thứ tự bảng chữ cái giữa các giá trị được chỉ định

Ví dụ:

Chọn tất cả các giá trị nằm giữa `Pavlova` và `Tofu` trong cột `product_name` của Table `products`

```sh
testdb=# SELECT * FROM products WHERE product_name BETWEEN 'Pavlova' AND 'Tofu';
 product_id |         product_name          | category_id |         unit         | price  
------------+-------------------------------+-------------+----------------------+--------
         11 | Queso Cabrales                |           4 | 1 kg pkg.            |  21.00
         12 | Queso Manchego La Pastora     |           4 | 10 - 500 g pkgs.     |  38.00
         14 | Tofu                          |           7 | 40 - 100 g pkgs.     |  23.25
         16 | Pavlova                       |           3 | 32 - 500 g boxes     |  17.45
         19 | Teatime Chocolate Biscuits    |           3 | 10 boxes x 12 pieces |   9.20
         20 | Sir Rodneys Marmalade         |           3 | 30 gift boxes        |  81.00
         21 | Sir Rodneys Scones            |           3 | 24 pkgs. x 4 pieces  |  10.00
         27 | Schoggi Schokolade            |           3 | 100 - 100 g pieces   |  43.90
         28 | Rassle Sauerkraut             |           7 | 25 - 825 g cans      |  45.60
         29 | Thoringer Rostbratwurst       |           6 | 50 bags x 30 sausgs. | 123.79
         34 | Sasquatch Ale                 |           1 | 24 - 12 oz bottles   |  14.00
         35 | Steeleye Stout                |           1 | 24 - 12 oz bottles   |  18.00
         42 | Singaporean Hokkien Fried Mee |           5 | 32 - 1 kg pkgs.      |  14.00
         45 | Rogede sild                   |           8 | 1k pkg.              |   9.50
         46 | Spegesild                     |           8 | 4 - 450 g glasses    |  12.00
         53 | Perth Pasties                 |           6 | 48 pieces            |  32.80
         57 | Ravioli Angelo                |           5 | 24 - 250 g pkgs.     |  19.50
         59 | Raclette Courdavault          |           4 | 5 kg pkg.            |  55.00
         61 | Sirop d arable                |           2 | 24 - 500 ml bottles  |  28.50
         62 | Tarte au sucre                |           3 | 48 pies              |  49.30
         68 | Scottish Longbreads           |           3 | 10 boxes x 8 pieces  |  12.50
         73 | Red Kaviar                    |           8 | 24 - 150 g jars      |  15.00
         75 | Rhenbreu Klosterbier          |           1 | 24 - 0.5 l bottles   |   7.75
(23 rows)
```

Nếu chúng ta thêm mệnh đề `ORDER BY` nó sẽ như sau

Ví dụ: 

Tương tự như trên nhưng chúng ta sẽ sắp xếp cột `product_name`

```sh
testdb=# SELECT * FROM products WHERE product_name BETWEEN 'Pavlova' AND 'Tofu' ORDER BY product_name;
 product_id |         product_name          | category_id |         unit         | price  
------------+-------------------------------+-------------+----------------------+--------
         16 | Pavlova                       |           3 | 32 - 500 g boxes     |  17.45
         53 | Perth Pasties                 |           6 | 48 pieces            |  32.80
         11 | Queso Cabrales                |           4 | 1 kg pkg.            |  21.00
         12 | Queso Manchego La Pastora     |           4 | 10 - 500 g pkgs.     |  38.00
         59 | Raclette Courdavault          |           4 | 5 kg pkg.            |  55.00
         28 | Rassle Sauerkraut             |           7 | 25 - 825 g cans      |  45.60
         57 | Ravioli Angelo                |           5 | 24 - 250 g pkgs.     |  19.50
         73 | Red Kaviar                    |           8 | 24 - 150 g jars      |  15.00
         75 | Rhenbreu Klosterbier          |           1 | 24 - 0.5 l bottles   |   7.75
         45 | Rogede sild                   |           8 | 1k pkg.              |   9.50
         34 | Sasquatch Ale                 |           1 | 24 - 12 oz bottles   |  14.00
         27 | Schoggi Schokolade            |           3 | 100 - 100 g pieces   |  43.90
         68 | Scottish Longbreads           |           3 | 10 boxes x 8 pieces  |  12.50
         42 | Singaporean Hokkien Fried Mee |           5 | 32 - 1 kg pkgs.      |  14.00
         61 | Sirop d arable                |           2 | 24 - 500 ml bottles  |  28.50
         20 | Sir Rodneys Marmalade         |           3 | 30 gift boxes        |  81.00
         21 | Sir Rodneys Scones            |           3 | 24 pkgs. x 4 pieces  |  10.00
         46 | Spegesild                     |           8 | 4 - 450 g glasses    |  12.00
         35 | Steeleye Stout                |           1 | 24 - 12 oz bottles   |  18.00
         62 | Tarte au sucre                |           3 | 48 pies              |  49.30
         19 | Teatime Chocolate Biscuits    |           3 | 10 boxes x 12 pieces |   9.20
         29 | Thoringer Rostbratwurst       |           6 | 50 bags x 30 sausgs. | 123.79
         14 | Tofu                          |           7 | 40 - 100 g pkgs.     |  23.25
(23 rows)
```

## BETWEEN Date Values

Toán tử BETWEEN cũng có thể được sử dụng trên các giá trị `date`

Ví dụ:

Chọn tất cả các giá trị trong cột `order_date` từ `2023-04-12` đến `2023-05-05` trong Table `orders`

```sh
SELECT * FROM orders
WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05';
```

Các bạn có thể tạo Table `orders` và Insert các giá trị để kiểm tra thử

<a name="postgresqlAS"></a>
# PostgreSQL AS

## Aliases

Bí danh SQL được sử dụng để đặt tên tạm thời cho một Table hoặc một cột trong Table 

Bí danh thường được sử dụng cho tên cột dễ đọc hơn

Bí danh tồn tại trong suốt thời gian truy vấn

Bí danh được tạo bằng từ khóa `AS`

Ví dụ

Sử dụng bí danh cho các cột đổi tên tạm thời cột `category_id` thành `id`

```sh
testdb=# SELECT category_id AS id FROM categories;
 id 
----
  1
  2
  3
  4
  5
  6
  7
  8
(8 rows)
```

## Concatenate Columns

Từ khóa `AS` thường được sử dụng khi hai hoặc nhiều trường được ghép thành một

Để nối 2 trường hãy sử dụng `||`

Ví dụ:

Nối 2 trường và gọi chúng là `prod` đồng thời `LIMIT` 10 dòng

```sh
testdb=# SELECT product_name || unit AS prod FROM products LIMIT 10;
                     prod                      
-----------------------------------------------
 Chais10 boxes x 20 bags
 Chang24 - 12 oz bottles
 Aniseed Syrup12 - 550 ml bottles
 Chef Antons Cajun Seasoning48 - 6 oz jars
 Chef Antons Gumbo Mix36 boxes
 Grandmas Boysenberry Spread12 - 8 oz jars
 Uncle Bobs Organic Dried Pears12 - 1 lb pkgs.
 Northwoods Cranberry Sauce12 - 12 oz jars
 Mishi Kobe Niku18 - 500 g pkgs.
 Ikura12 - 200 ml jars
(10 rows)
```

NOTE: Trong ví dụ trên, chúng ta thiếu khoảng trắng giữa 2 cột `product_name` và `unit`, Để thêm khoảng trắng khi nối, hãy sử dụng `|| ' ' ||`

```sh
testdb=# SELECT product_name || ' ' || unit AS prod FROM products LIMIT 10;
                      prod                      
------------------------------------------------
 Chais 10 boxes x 20 bags
 Chang 24 - 12 oz bottles
 Aniseed Syrup 12 - 550 ml bottles
 Chef Antons Cajun Seasoning 48 - 6 oz jars
 Chef Antons Gumbo Mix 36 boxes
 Grandmas Boysenberry Spread 12 - 8 oz jars
 Uncle Bobs Organic Dried Pears 12 - 1 lb pkgs.
 Northwoods Cranberry Sauce 12 - 12 oz jars
 Mishi Kobe Niku 18 - 500 g pkgs.
 Ikura 12 - 200 ml jars
(10 rows)
```

<a name="postgresqlJOIN"></a>
# PostgreSQL Joins

## JOIN

Mệnh đề JOIN được sử dụng để kết hợp các hàng từ hai hoặc nhiều Table, dựa trên một cột có liên quan giữa chúng

Chúng ta hãy cùng xem 8 dòng đầu Table `products`

```sh
testdb=# SELECT * FROM products LIMIT 8;
 product_id |          product_name          | category_id |        unit         | price 
------------+--------------------------------+-------------+---------------------+-------
          1 | Chais                          |           1 | 10 boxes x 20 bags  | 18.00
          2 | Chang                          |           1 | 24 - 12 oz bottles  | 19.00
          3 | Aniseed Syrup                  |           2 | 12 - 550 ml bottles | 10.00
          4 | Chef Antons Cajun Seasoning    |           2 | 48 - 6 oz jars      | 22.00
          5 | Chef Antons Gumbo Mix          |           2 | 36 boxes            | 21.35
          6 | Grandmas Boysenberry Spread    |           2 | 12 - 8 oz jars      | 25.00
          7 | Uncle Bobs Organic Dried Pears |           7 | 12 - 1 lb pkgs.     | 30.00
          8 | Northwoods Cranberry Sauce     |           2 | 12 - 12 oz jars     | 40.00
(8 rows)
```

Sau đó, hãy xem Table `categories `

```sh
testdb=# SELECT * FROM categories;
 category_id | category_name  |                        description                         
-------------+----------------+------------------------------------------------------------
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
           3 | Confections    | Desserts, candies, and sweet breads
           4 | Dairy Products | Cheeses
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
           6 | Meat/Poultry   | Prepared meats
           7 | Produce        | Dried fruit and bean curd
           8 | Seafood        | Seaweed and fish
(8 rows)
```

Lưu ý rằng cột `category_id` trong Table `product` đề cập đến `category_id` trong Table `catagories`. Mối quan hệ giữa 2 Table trên là cột `category_id`

Sau đó, chúng ta có thể thực hiện câu lệnh SQL sau (với JOIN), để chọn các record có giá trị khớp nhau trong cả 2 TABLE

Ví dụ:

Nối 8 dòng đầu Table `products` vào `table` bằng cột `category_id`

```sh
testdb=# SELECT product_id, product_name, category_name FROM products INNER JOIN categories ON products.category_id = categories.category_id LIMIT 8;
 product_id |          product_name          | category_name 
------------+--------------------------------+---------------
          1 | Chais                          | Beverages
          2 | Chang                          | Beverages
          3 | Aniseed Syrup                  | Condiments
          4 | Chef Antons Cajun Seasoning    | Condiments
          5 | Chef Antons Gumbo Mix          | Condiments
          6 | Grandmas Boysenberry Spread    | Condiments
          7 | Uncle Bobs Organic Dried Pears | Produce
          8 | Northwoods Cranberry Sauce     | Condiments
(8 rows)
```

## Different Types of Joins

Dưới đấy là các loại JOIN khác nhau:

- `INNER JOIN`: Trả về các bản ghi có giá trị trùng khớp trong cả 2 Table

- `LEFT JOIN`: Trả về tất cả các bản ghi từ Table bên trái và các bản ghi trùng khớp từ Table bên phải

- `RIGHT JOIN`: Trả về tất cả các bản ghi từ Table bên phải và các bản ghi trùng khớp từ Table bên Trái

- `FULL JOIN`: Trả về tất cả các bản ghi khi có kết quả khớp ở Table bên trái hoặc bên phải

<a name="postgresqlINNER_JOIN"></a>
# PostgreSQL INNER JOIN

## INNER JOIN

Từ khóa INNER JOIN chọn các bản ghi có giá trị trùng khớp trong cả hai Table

Hãy xem ví dụ sử dụng Table `testproducts`

```sh
testdb=# SELECT * FROM testproducts;
 testproduct_id |      product_name      | category_id 
----------------+------------------------+-------------
              1 | Johns Fruit Cake       |           3
              2 | Marys Healthy Mix      |           9
              3 | Peters Scary Stuff     |          10
              4 | Jims Secret Recipe     |          11
              5 | Elisabeths Best Apples |          12
              6 | Janes Favorite Cheese  |           4
              7 | Billys Home Made Pizza |          13
              8 | Ellas Special Salmon   |           8
              9 | Roberts Rich Spaghetti |           5
             10 | Mias Popular Ice       |          14
(10 rows)
```

Xem Table `categories`

```sh
testdb=# SELECT * FROM categories;
 category_id | category_name  |                        description                         
-------------+----------------+------------------------------------------------------------
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
           3 | Confections    | Desserts, candies, and sweet breads
           4 | Dairy Products | Cheeses
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
           6 | Meat/Poultry   | Prepared meats
           7 | Produce        | Dried fruit and bean curd
           8 | Seafood        | Seaweed and fish
(8 rows)
```

Chúng ta sẽ thử nối Table `testproducts` với Table `categories`:

Lưu ý rằng nhiều giá trị trong Table `testproducts` có `category_id` không khớp với bất kỳ `category_id` nào trong Table `categories`

Bằng cách sử dụng INNER JOIN, chúng ta sẽ chỉ nhận được các record khớp với cả 2 Table:

Ví dụ:

Kết hợp Table `testproducts` với `categories` sử dụng cột `category_id`

```sh
testdb=# SELECT testproduct_id, product_name, category_name FROM testproducts INNER JOIN categories ON testproducts.category_id = categories.category_id;
 testproduct_id |      product_name      | category_name  
----------------+------------------------+----------------
              1 | Johns Fruit Cake       | Confections
              6 | Janes Favorite Cheese  | Dairy Products
              8 | Ellas Special Salmon   | Seafood
              9 | Roberts Rich Spaghetti | Grains/Cereals
(4 rows)
```

<a name="postgresqlLEFT_JOIN"></a>
# PostgreSQL LEFT JOIN

## LEFT JOIN

Từ khóa LEFT JOIN chọn TẤT CẢ bản ghi từ Table TRÁI và các bản ghi phù hợp từ Table PHẢI. Kết quả là 0 record từ phía bên phải nếu không có kết quả trùng khớp

Hãy Table `testproducts`:

```sh
testdb=# SELECT * FROM testproducts;
 testproduct_id |      product_name      | category_id 
----------------+------------------------+-------------
              1 | Johns Fruit Cake       |           3
              2 | Marys Healthy Mix      |           9
              3 | Peters Scary Stuff     |          10
              4 | Jims Secret Recipe     |          11
              5 | Elisabeths Best Apples |          12
              6 | Janes Favorite Cheese  |           4
              7 | Billys Home Made Pizza |          13
              8 | Ellas Special Salmon   |           8
              9 | Roberts Rich Spaghetti |           5
             10 | Mias Popular Ice       |          14
(10 rows)
```

Xem Table `categories`

```sh
testdb=# SELECT * FROM categories;
 category_id | category_name  |                        description                         
-------------+----------------+------------------------------------------------------------
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
           3 | Confections    | Desserts, candies, and sweet breads
           4 | Dairy Products | Cheeses
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
           6 | Meat/Poultry   | Prepared meats
           7 | Produce        | Dried fruit and bean curd
           8 | Seafood        | Seaweed and fish
(8 rows)
```

Ví dụ:

Sử dụng JOIN LEFT kết hợp Table `testproducts` với Table `categories` bằng cột `category_id`

```sh
testdb=# SELECT testproduct_id, product_name, category_name FROM testproducts LEFT JOIN categories ON testproducts.category_id = categories.category_id;
 testproduct_id |      product_name      | category_name  
----------------+------------------------+----------------
              1 | Johns Fruit Cake       | Confections
              2 | Marys Healthy Mix      | 
              3 | Peters Scary Stuff     | 
              4 | Jims Secret Recipe     | 
              5 | Elisabeths Best Apples | 
              6 | Janes Favorite Cheese  | Dairy Products
              7 | Billys Home Made Pizza | 
              8 | Ellas Special Salmon   | Seafood
              9 | Roberts Rich Spaghetti | Grains/Cereals
             10 | Mias Popular Ice       | 
(10 rows)
```

Kết quả chúng ta nhận được tất cả record đến từ Table bên TRÁI (`testproducts`) và chỉ các record trùng khớp từ Table bên PHẢI (`categories`)

<a name="postgresqlRIGHT_JOIN"></a>
# PostgreSQL RIGHT JOIN

## RIGHT JOIN

Từ khóa RIGHT JOIN chọn TẤT CẢ bản ghi từ Table bên PHẢI và các bản ghi phù hợp từ Table TRÁI

Chúng ta có 2 bảng `testproducts` và `categories`

```sh
testdb=# SELECT * FROM testproducts;
 testproduct_id |      product_name      | category_id 
----------------+------------------------+-------------
              1 | Johns Fruit Cake       |           3
              2 | Marys Healthy Mix      |           9
              3 | Peters Scary Stuff     |          10
              4 | Jims Secret Recipe     |          11
              5 | Elisabeths Best Apples |          12
              6 | Janes Favorite Cheese  |           4
              7 | Billys Home Made Pizza |          13
              8 | Ellas Special Salmon   |           8
              9 | Roberts Rich Spaghetti |           5
             10 | Mias Popular Ice       |          14
(10 rows)
```

```sh
testdb=# SELECT * FROM categories;
 category_id | category_name  |                        description                         
-------------+----------------+------------------------------------------------------------
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
           3 | Confections    | Desserts, candies, and sweet breads
           4 | Dairy Products | Cheeses
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
           6 | Meat/Poultry   | Prepared meats
           7 | Produce        | Dried fruit and bean curd
           8 | Seafood        | Seaweed and fish
(8 rows)
```

Bằng cách sử dụng RIGHT JOIN, chúng ta sẽ nhận được tất cả các record từ Table `categories` ngay cả những record không khớp trong Table `testproducts`

Ví dụ

Sử dụng RIGHT JOIN kết hợp Table `testproducts` với `categories` bằng cột `category_id`

```sh
testdb=# SELECT testproduct_id, product_name, category_name FROM testproducts RIGHT JOIN categories ON testproducts.category_id = categories.category_id;
 testproduct_id |      product_name      | category_name  
----------------+------------------------+----------------
              1 | Johns Fruit Cake       | Confections
              6 | Janes Favorite Cheese  | Dairy Products
              8 | Ellas Special Salmon   | Seafood
              9 | Roberts Rich Spaghetti | Grains/Cereals
                |                        | Condiments
                |                        | Meat/Poultry
                |                        | Beverages
                |                        | Produce
(8 rows)
```

<a name="postgresqlFULL_JOIN"></a>
# PostgreSQL FULL JOIN

## FULL JOIN

Từ khóa FULL JOIN chọn TẤT CẢ các record từ cả hai Table, ngay cả khi không có record nào khớp, các giá trị từ cả 2 Table đều có sẵn, nếu không khớp, các trường trốn sẽ nhận NULL

Chúng ta có 2 bảng `testproducts` và `categories`

```sh
testdb=# SELECT * FROM testproducts;
 testproduct_id |      product_name      | category_id 
----------------+------------------------+-------------
              1 | Johns Fruit Cake       |           3
              2 | Marys Healthy Mix      |           9
              3 | Peters Scary Stuff     |          10
              4 | Jims Secret Recipe     |          11
              5 | Elisabeths Best Apples |          12
              6 | Janes Favorite Cheese  |           4
              7 | Billys Home Made Pizza |          13
              8 | Ellas Special Salmon   |           8
              9 | Roberts Rich Spaghetti |           5
             10 | Mias Popular Ice       |          14
(10 rows)
```

```sh
testdb=# SELECT * FROM categories;
 category_id | category_name  |                        description                         
-------------+----------------+------------------------------------------------------------
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
           3 | Confections    | Desserts, candies, and sweet breads
           4 | Dairy Products | Cheeses
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
           6 | Meat/Poultry   | Prepared meats
           7 | Produce        | Dried fruit and bean curd
           8 | Seafood        | Seaweed and fish
(8 rows)
```

Bằng cách sử dụng FULL JOIN chúng ta sẽ nhận được tất cả các bản ghi từ cả Table `categories` và Table `testproducts`:

Ví dụ: 

Sử dụng FULL JOIN kết hợp 2 Table `testproducts` và `categories` bằng cột `category_id`

```sh
testdb=# SELECT testproduct_id, product_name, category_name FROM testproducts FULL JOIN categories ON testproducts.category_id = categories.category_id;
 testproduct_id |      product_name      | category_name  
----------------+------------------------+----------------
              1 | Johns Fruit Cake       | Confections
              2 | Marys Healthy Mix      | 
              3 | Peters Scary Stuff     | 
              4 | Jims Secret Recipe     | 
              5 | Elisabeths Best Apples | 
              6 | Janes Favorite Cheese  | Dairy Products
              7 | Billys Home Made Pizza | 
              8 | Ellas Special Salmon   | Seafood
              9 | Roberts Rich Spaghetti | Grains/Cereals
             10 | Mias Popular Ice       | 
                |                        | Condiments
                |                        | Meat/Poultry
                |                        | Beverages
                |                        | Produce
(14 rows)
```

<a name="postgresqlCROSS_JOIN"></a>
# PostgreSQL CROSS JOIN

## CROSS JOIN

Từ khóa CROSS JOIN khớp TẤT CẢ bản ghi Table TRÁI với MỖI bản ghi từ Table PHẢI

Điều đó có nghĩa là tất cả các bản ghi từ Table PHẢI sẽ được trả về cho MỖI bản ghi trong Table TRÁI

Cách nối này có khả năng trả về một Table rất LỚN và bạn không nên sử dụng nó nếu không cần thiết

Chúng ta có 2 Table `testproducts` và `categories`

```sh
testdb=# SELECT * FROM testproducts;
 testproduct_id |      product_name      | category_id 
----------------+------------------------+-------------
              1 | Johns Fruit Cake       |           3
              2 | Marys Healthy Mix      |           9
              3 | Peters Scary Stuff     |          10
              4 | Jims Secret Recipe     |          11
              5 | Elisabeths Best Apples |          12
              6 | Janes Favorite Cheese  |           4
              7 | Billys Home Made Pizza |          13
              8 | Ellas Special Salmon   |           8
              9 | Roberts Rich Spaghetti |           5
             10 | Mias Popular Ice       |          14
(10 rows)
```

```sh
testdb=# SELECT * FROM categories;
 category_id | category_name  |                        description                         
-------------+----------------+------------------------------------------------------------
           1 | Beverages      | Soft drinks, coffees, teas, beers, and ales
           2 | Condiments     | Sweet and savory sauces, relishes, spreads, and seasonings
           3 | Confections    | Desserts, candies, and sweet breads
           4 | Dairy Products | Cheeses
           5 | Grains/Cereals | Breads, crackers, pasta, and cereal
           6 | Meat/Poultry   | Prepared meats
           7 | Produce        | Dried fruit and bean curd
           8 | Seafood        | Seaweed and fish
(8 rows)
```

NOTE: Phương thức CROSS JOIN sẽ trả về TẤT CẢ Table `categories` cho mỗi bản ghi trong Table `testproducts`, nghĩa là nó sẽ trả về 80 hàng (10 * 8)

Ví dụ:

```sh
testdb=# SELECT testproduct_id, product_name, category_name FROM testproducts CROSS JOIN categories;
 testproduct_id |      product_name      | category_name  
----------------+------------------------+----------------
              1 | Johns Fruit Cake       | Beverages
              1 | Johns Fruit Cake       | Condiments
              1 | Johns Fruit Cake       | Confections
              1 | Johns Fruit Cake       | Dairy Products
              1 | Johns Fruit Cake       | Grains/Cereals
              1 | Johns Fruit Cake       | Meat/Poultry
              1 | Johns Fruit Cake       | Produce
              1 | Johns Fruit Cake       | Seafood
              2 | Marys Healthy Mix      | Beverages
              2 | Marys Healthy Mix      | Condiments
              2 | Marys Healthy Mix      | Confections
              2 | Marys Healthy Mix      | Dairy Products
              2 | Marys Healthy Mix      | Grains/Cereals
              2 | Marys Healthy Mix      | Meat/Poultry
              2 | Marys Healthy Mix      | Produce
              2 | Marys Healthy Mix      | Seafood
              3 | Peters Scary Stuff     | Beverages
              3 | Peters Scary Stuff     | Condiments
              3 | Peters Scary Stuff     | Confections
              3 | Peters Scary Stuff     | Dairy Products
              3 | Peters Scary Stuff     | Grains/Cereals
              3 | Peters Scary Stuff     | Meat/Poultry
              3 | Peters Scary Stuff     | Produce
              3 | Peters Scary Stuff     | Seafood
              4 | Jims Secret Recipe     | Beverages
              4 | Jims Secret Recipe     | Condiments
              4 | Jims Secret Recipe     | Confections
              4 | Jims Secret Recipe     | Dairy Products
              4 | Jims Secret Recipe     | Grains/Cereals
              4 | Jims Secret Recipe     | Meat/Poultry
              4 | Jims Secret Recipe     | Produce
              4 | Jims Secret Recipe     | Seafood
              5 | Elisabeths Best Apples | Beverages
              5 | Elisabeths Best Apples | Condiments
              5 | Elisabeths Best Apples | Confections
              5 | Elisabeths Best Apples | Dairy Products
              5 | Elisabeths Best Apples | Grains/Cereals
              5 | Elisabeths Best Apples | Meat/Poultry
              5 | Elisabeths Best Apples | Produce
              5 | Elisabeths Best Apples | Seafood
              6 | Janes Favorite Cheese  | Beverages
              6 | Janes Favorite Cheese  | Condiments
              6 | Janes Favorite Cheese  | Confections
              6 | Janes Favorite Cheese  | Dairy Products
              6 | Janes Favorite Cheese  | Grains/Cereals
              6 | Janes Favorite Cheese  | Meat/Poultry
              6 | Janes Favorite Cheese  | Produce
              6 | Janes Favorite Cheese  | Seafood
              7 | Billys Home Made Pizza | Beverages
              7 | Billys Home Made Pizza | Condiments
              7 | Billys Home Made Pizza | Confections
              7 | Billys Home Made Pizza | Dairy Products
              7 | Billys Home Made Pizza | Grains/Cereals
              7 | Billys Home Made Pizza | Meat/Poultry
              7 | Billys Home Made Pizza | Produce
              7 | Billys Home Made Pizza | Seafood
              8 | Ellas Special Salmon   | Beverages
              8 | Ellas Special Salmon   | Condiments
              8 | Ellas Special Salmon   | Confections
              8 | Ellas Special Salmon   | Dairy Products
              8 | Ellas Special Salmon   | Grains/Cereals
              8 | Ellas Special Salmon   | Meat/Poultry
              8 | Ellas Special Salmon   | Produce
              8 | Ellas Special Salmon   | Seafood
              9 | Roberts Rich Spaghetti | Beverages
              9 | Roberts Rich Spaghetti | Condiments
              9 | Roberts Rich Spaghetti | Confections
              9 | Roberts Rich Spaghetti | Dairy Products
              9 | Roberts Rich Spaghetti | Grains/Cereals
              9 | Roberts Rich Spaghetti | Meat/Poultry
              9 | Roberts Rich Spaghetti | Produce
              9 | Roberts Rich Spaghetti | Seafood
             10 | Mias Popular Ice       | Beverages
             10 | Mias Popular Ice       | Condiments
             10 | Mias Popular Ice       | Confections
             10 | Mias Popular Ice       | Dairy Products
             10 | Mias Popular Ice       | Grains/Cereals
             10 | Mias Popular Ice       | Meat/Poultry
             10 | Mias Popular Ice       | Produce
             10 | Mias Popular Ice       | Seafood
(80 rows)
```

<a name="postgresqlUNION"></a>
# PostgreSQL UNION

## UNION

Toán tử UNION được sử dụng để KẾT HỢP tập kết quả của hai hay nhiều truy vấn

Các truy vấn trong UNION phải tuân thủ các quy tắc sau:

- Chúng phải có cùng số cột

- Các cột phải có cùng kiểu dữ liệu

- Các cột phải có cùng thứ tự

Ví dụ:

Kết hợp Table `products` và `testproducts` bằng UNION

Chúng ta sẽ chỉ hiển thị 15 dòng đầu để Table trả về không quá dài

```sh
testdb=# SELECT product_id, product_name FROM products UNION SELECT testproduct_id, product_name FROM testproducts ORDER BY product_id LIMIT 15;
 product_id |          product_name          
------------+--------------------------------
          1 | Chais
          1 | Johns Fruit Cake
          2 | Chang
          2 | Marys Healthy Mix
          3 | Peters Scary Stuff
          3 | Aniseed Syrup
          4 | Chef Antons Cajun Seasoning
          4 | Jims Secret Recipe
          5 | Chef Antons Gumbo Mix
          5 | Elisabeths Best Apples
          6 | Janes Favorite Cheese
          6 | Grandmas Boysenberry Spread
          7 | Billys Home Made Pizza
          7 | Uncle Bobs Organic Dried Pears
          8 | Ellas Special Salmon
(15 rows)
. . .
. . .
```

Kết quả trả về thực chất có 87 row gồm 77 row của Table `product` và 10 row của Table `testproduct`

## UNION vs UNION ALL

Với toán tử UNION, nếu một số hàng trong hai truy vấn trả về cùng một kết quả thì chỉ một hàng được liệt kê vì UNION chỉ chọn các giá trị riêng biệt

Sử dụng UNION ALL để trả về các giá trị trùng lặp

Ví dụ - UNION

```sh
SELECT product_id
FROM products
UNION
SELECT testproduct_id
FROM testproducts
ORDER BY product_id;
```

**UNION trả về 77 row**

Ví dụ - UNION ALL

```sh
SELECT product_id
FROM products
UNION ALL
SELECT testproduct_id
FROM testproducts
ORDER BY product_id;
```

**UNION ALL trả về 87 row**

<a name="postgresqlGROUP_BY"></a>
# PostgreSQL GROUP BY

## GROUP BY

Mệnh đề GROUP BY nhóm các hàng có cùng giá trị thành các hàng tóm tắt

Mệnh đề GROUP BY thường được sử dụng với các hàm tổng hợp như COUNT(), MAX(), MIN(), SUM(), AVG() để nhóm tập kết quả theo một hoặc nhiều cột

Ví dụ:

Đếm số lượng xuất hiện của các giá trị trong cột `country` của Table `customers`

```sh
testdb=# SELECT COUNT(customer_id), country FROM customers GROUP BY country;
 count |   country   
-------+-------------
     3 | Argentina
     5 | Spain
     2 | Switzerland
     3 | Italy
     4 | Venezuela
     2 | Belgium
     1 | Norway
     2 | Sweden
    13 | USA
    11 | France
     5 | Mexico
     9 | Brazil
     2 | Austria
     1 | Poland
     7 | UK
     1 | Ireland
    11 | Germany
     2 | Denmark
     3 | Canada
     2 | Finland
     2 | Portugal
(21 rows)
```

Ta sẽ nhận được kết quả giá trị `Argentina` xuất hiện 3 lần, `Spain` xuất hiện 5 lần ...

<a name="postgresqlHAVING"></a>
# PostgreSQL HAVING

## HAVING

Mệnh đề HAVING đã được thêm vào SQL vì mệnh đề WHERE không thể sử dụng được trong những hàm tổng hợp

Các hàm tổng hợp thường được sử dụng với mệnh đề GROUP BY và bằng cách thêm HAVING chúng ta có thể viết điều kiện giống như chúng ta làm với mệnh đề WHERE

Ví dụ:

Chỉ liệt kê giá trị xuất hiện nhiều hơn 5 lần trong cột `country` của Table `customers`

```sh
testdb=# SELECT COUNT(customer_id), country FROM customers GROUP BY country HAVING COUNT(customer_id) > 5;
 count | country 
-------+---------
    13 | USA
    11 | France
     9 | Brazil
     7 | UK
    11 | Germany
(5 rows)
```

Tổng cộng có 5 record xuất hiện nhiều hơn 5 lần trong cột `country` của Table `customers`

<a name="postgresqlANY"></a>
# PostgreSQL ANY

## ANY

Toán tử ANY cho phép bạn thực hiện so sánh giữa một giá trị cột đơn và một phạm vi giá trị khác

Toán tử ANY:

- Kết quả trả về là giá trị Boolean

- Trả về TRUE nếu bất kỳ giá trị truy vấn nào đáp ứng điều kiện

ANY có nghĩa là điều kiện sẽ đúng nếu thao tác đúng với bất kỳ giá trị nào trong phạm vi

Ví dụ:

Liệt kê cột `product_name` trong Table `product` có giá trị `product_id` tương ứng lớn hơn 10 trong cột `category_id` của Table `testproducts` (Chỗ này hơi rối một chút :D )

```sh
SELECT product_name
FROM products
WHERE product_id = ANY (
  SELECT testproduct_id
  FROM testproducts
  WHERE category_id > 10
);
```

Output: 

```sh
testdb(# );
          product_name          
--------------------------------
 Chef Antons Cajun Seasoning
 Chef Antons Gumbo Mix
 Uncle Bobs Organic Dried Pears
 Ikura
(4 rows)
```

<a name="postgresqlCASE"></a>
# PostgreSQL CASE

## CASE

Biểu thức CASE xem xét các điều kiện và trả về một giá trị khi điều kiện đầu tiên được đáp ứng (như câu lệnh if-then-else)

Khi một điều kiện là đúng, nó sẽ ngừng đọc và trả về kết quả. Nếu không có điều kiện nào đúng, nó sẽ trả về giá trị trong mệnh đề ELSE

Nếu không có phần ELSE và không có phần nào đúng thì nó sẽ trả về NULL

Ví dụ:

Trả về các giá trị cụ thể nếu giá trị từ cột `price` trong Table `products` đáp ứng một điều kiện cụ thể (Chỉ trả về 20 dòng vì Table này dài)

```sh
testdb-# FROM products LIMIT 20;
          product_name          |        case        
--------------------------------+--------------------
 Chais                          | Normal product
 Chang                          | Normal product
 Aniseed Syrup                  | Normal product
 Chef Antons Cajun Seasoning    | Normal product
 Chef Antons Gumbo Mix          | Normal product
 Grandmas Boysenberry Spread    | Normal product
 Uncle Bobs Organic Dried Pears | Normal product
 Northwoods Cranberry Sauce     | Normal product
 Mishi Kobe Niku                | High price product
 Ikura                          | Normal product
 Queso Cabrales                 | Normal product
 Queso Manchego La Pastora      | Normal product
 Konbu                          | Low price product
 Tofu                           | Normal product
 Genen Shouyu                   | Normal product
 Pavlova                        | Normal product
 Alice Mutton                   | Normal product
 Carnarvon Tigers               | High price product
 Teatime Chocolate Biscuits     | Low price product
 Sir Rodneys Marmalade          | High price product
(20 rows)
```

## With an Alias

Khi tên cột không được chỉ định cho trường "case", trình phân tích cú pháp sẽ sử dụng `case` làm tên cột

Để thêm bí danh cho tên cột hay thêm từ khóa `AS` đằng sau `END`

```sh
testdb=# SELECT product_name,
CASE
  WHEN price < 10 THEN 'Low price product'
  WHEN price > 50 THEN 'High price product'
ELSE
  'Normal product'
END AS "price category"
FROM products LIMIT 20;
          product_name          |   price category   
--------------------------------+--------------------
 Chais                          | Normal product
 Chang                          | Normal product
 Aniseed Syrup                  | Normal product
 Chef Antons Cajun Seasoning    | Normal product
 Chef Antons Gumbo Mix          | Normal product
 Grandmas Boysenberry Spread    | Normal product
 Uncle Bobs Organic Dried Pears | Normal product
 Northwoods Cranberry Sauce     | Normal product
 Mishi Kobe Niku                | High price product
 Ikura                          | Normal product
 Queso Cabrales                 | Normal product
 Queso Manchego La Pastora      | Normal product
 Konbu                          | Low price product
 Tofu                           | Normal product
 Genen Shouyu                   | Normal product
 Pavlova                        | Normal product
 Alice Mutton                   | Normal product
 Carnarvon Tigers               | High price product
 Teatime Chocolate Biscuits     | Low price product
 Sir Rodneys Marmalade          | High price product
(20 rows)
```

