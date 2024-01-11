# Create Database

Cho đến thời điểm hiện tại, chúng ta đã làm việc và thực hành với một Table rất nhỏ và đơn giản trong PostgreSQL database của mình

Bây giờ, chúng ta cần tạo nhiều Table hơn với nhiều nội dung hơn để export nó thành một file có đuôi `.pgsql`. Từ file này chúng ta có thể import DB đến nhiều máy chủ khác nhau mà chúng ta muốn hoặc đơn giản là muốn có một bản backup cho Database của mình để đề phòng trường hợp khẩn cấp.

Chúng ta sẽ tạo 4 Table

`categories`

`customers`

`products`

`testproducts`

## Tạo Table `categories`

```sh
CREATE TABLE categories (
  category_id SERIAL NOT NULL PRIMARY KEY,
  category_name VARCHAR(255),
  description VARCHAR(255)
);
```

Chèn nội dung vào Table `categories` với lệnh `INSERT INTO`

```sh
INSERT INTO categories (category_name, description)
VALUES
  ('Beverages', 'Soft drinks, coffees, teas, beers, and ales'),
  ('Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings'),
  ('Confections', 'Desserts, candies, and sweet breads'),
  ('Dairy Products', 'Cheeses'),
  ('Grains/Cereals', 'Breads, crackers, pasta, and cereal'),
  ('Meat/Poultry', 'Prepared meats'),
  ('Produce', 'Dried fruit and bean curd'),
  ('Seafood', 'Seaweed and fish');
```

## Tạo Table `customers`

```sh
CREATE TABLE customers (
  customer_id SERIAL NOT NULL PRIMARY KEY,
  customer_name VARCHAR(255),
  contact_name VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(255),
  postal_code VARCHAR(255),
  country VARCHAR(255)
);
```

Chèn nội dung vào Table `customers` với lệnh `INSERT INTO`

```sh
INSERT INTO customers (customer_name, contact_name, address, city, postal_code, country)
VALUES
  ('Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany'),
  ('Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Avda. de la Constitucion 2222', 'Mexico D.F.', '05021', 'Mexico'),
  ('Antonio Moreno Taquera', 'Antonio Moreno', 'Mataderos 2312', 'Mexico D.F.', '05023', 'Mexico'),
  ('Around the Horn', 'Thomas Hardy', '120 Hanover Sq.', 'London', 'WA1 1DP', 'UK'),
  ('Berglunds snabbkoep', 'Christina Berglund', 'Berguvsvegen 8', 'Lulea', 'S-958 22', 'Sweden'),
  ('Blauer See Delikatessen', 'Hanna Moos', 'Forsterstr. 57', 'Mannheim', '68306', 'Germany'),
  ('Blondel pere et fils', 'Frederique Citeaux', '24, place Kleber', 'Strasbourg', '67000', 'France'),
  ('Bolido Comidas preparadas', 'Martin Sommer', 'C/ Araquil, 67', 'Madrid', '28023', 'Spain'),
  ('Bon app', 'Laurence Lebihans', '12, rue des Bouchers', 'Marseille', '13008', 'France'),
  ('Bottom-Dollar Marketse', 'Elizabeth Lincoln', '23 Tsawassen Blvd.', 'Tsawassen', 'T2F 8M4', 'Canada'),
  ('Bs Beverages', 'Victoria Ashworth', 'Fauntleroy Circus', 'London', 'EC2 5NT', 'UK'),
  ('Cactus Comidas para llevar', 'Patricio Simpson', 'Cerrito 333', 'Buenos Aires', '1010', 'Argentina'),
  ('Centro comercial Moctezuma', 'Francisco Chang', 'Sierras de Granada 9993', 'Mexico D.F.', '05022', 'Mexico'),
  ('Chop-suey Chinese', 'Yang Wang', 'Hauptstr. 29', 'Bern', '3012', 'Switzerland'),
  ('Comercio Mineiro', 'Pedro Afonso', 'Av. dos Lusiadas, 23', 'Sao Paulo', '05432-043', 'Brazil'),
  ('Consolidated Holdings', 'Elizabeth Brown', 'Berkeley Gardens 12 Brewery ', 'London', 'WX1 6LT', 'UK'),
  ('Drachenblut Delikatessend', 'Sven Ottlieb', 'Walserweg 21', 'Aachen', '52066', 'Germany'),
  ('Du monde entier', 'Janine Labrune', '67, rue des Cinquante Otages', 'Nantes', '44000', 'France'),
  ('Eastern Connection', 'Ann Devon', '35 King George', 'London', 'WX3 6FW', 'UK'),
  ('Ernst Handel', 'Roland Mendel', 'Kirchgasse 6', 'Graz', '8010', 'Austria'),
  ('Familia Arquibaldo', 'Aria Cruz', 'Rua Oros, 92', 'Sao Paulo', '05442-030', 'Brazil'),
  ('FISSA Fabrica Inter. Salchichas S.A.', 'Diego Roel', 'C/ Moralzarzal, 86', 'Madrid', '28034', 'Spain'),
  ('Folies gourmandes', 'Martine Rance', '184, chaussee de Tournai', 'Lille', '59000', 'France'),
  ('Folk och fe HB', 'Maria Larsson', 'Akergatan 24', 'Brecke', 'S-844 67', 'Sweden'),
  ('Frankenversand', 'Peter Franken', 'Berliner Platz 43', 'Munchen', '80805', 'Germany'),
  ('France restauration', 'Carine Schmitt', '54, rue Royale', 'Nantes', '44000', 'France'),
  ('Franchi S.p.A.', 'Paolo Accorti', 'Via Monte Bianco 34', 'Torino', '10100', 'Italy'),
  ('Furia Bacalhau e Frutos do Mar', 'Lino Rodriguez ', 'Jardim das rosas n. 32', 'Lisboa', '1675', 'Portugal'),
  ('Galeria del gastronomo', 'Eduardo Saavedra', 'Rambla de Cataluna, 23', 'Barcelona', '08022', 'Spain'),
  ('Godos Cocina Tipica', 'Jose Pedro Freyre', 'C/ Romero, 33', 'Sevilla', '41101', 'Spain'),
  ('Gourmet Lanchonetes', 'Andre Fonseca', 'Av. Brasil, 442', 'Campinas', '04876-786', 'Brazil'),
  ('Great Lakes Food Market', 'Howard Snyder', '2732 Baker Blvd.', 'Eugene', '97403', 'USA'),
  ('GROSELLA-Restaurante', 'Manuel Pereira', '5th Ave. Los Palos Grandes', 'Caracas', '1081', 'Venezuela'),
  ('Hanari Carnes', 'Mario Pontes', 'Rua do Paco, 67', 'Rio de Janeiro', '05454-876', 'Brazil'),
  ('HILARION-Abastos', 'Carlos Hernandez', 'Carrera 22 con Ave. Carlos Soublette #8-35', 'San Cristobal', '5022', 'Venezuela'),
  ('Hungry Coyote Import Store', 'Yoshi Latimer', 'City Center Plaza 516 Main St.', 'Elgin', '97827', 'USA'),
  ('Hungry Owl All-Night Grocers', 'Patricia McKenna', '8 Johnstown Road', 'Cork', '', 'Ireland'),
  ('Island Trading', 'Helen Bennett', 'Garden House Crowther Way', 'Cowes', 'PO31 7PJ', 'UK'),
  ('Koniglich Essen', 'Philip Cramer', 'Maubelstr. 90', 'Brandenburg', '14776', 'Germany'),
  ('La corne d abondance', 'Daniel Tonini', '67, avenue de l Europe', 'Versailles', '78000', 'France'),
  ('La maison d Asie', 'Annette Roulet', '1 rue Alsace-Lorraine', 'Toulouse', '31000', 'France'),
  ('Laughing Bacchus Wine Cellars', 'Yoshi Tannamuri', '1900 Oak St.', 'Vancouver', 'V3F 2K1', 'Canada'),
  ('Lazy K Kountry Store', 'John Steel', '12 Orchestra Terrace', 'Walla Walla', '99362', 'USA'),
  ('Lehmanns Marktstand', 'Renate Messner', 'Magazinweg 7', 'Frankfurt a.M. ', '60528', 'Germany'),
  ('Lets Stop N Shop', 'Jaime Yorres', '87 Polk St. Suite 5', 'San Francisco', '94117', 'USA'),
  ('LILA-Supermercado', 'Carlos Gonzalez', 'Carrera 52 con Ave. Bolivar #65-98 Llano Largo', 'Barquisimeto', '3508', 'Venezuela'),
  ('LINO-Delicateses', 'Felipe Izquierdo', 'Ave. 5 de Mayo Porlamar', 'I. de Margarita', '4980', 'Venezuela'),
  ('Lonesome Pine Restaurant', 'Fran Wilson', '89 Chiaroscuro Rd.', 'Portland', '97219', 'USA'),
  ('Magazzini Alimentari Riuniti', 'Giovanni Rovelli', 'Via Ludovico il Moro 22', 'Bergamo', '24100', 'Italy'),
  ('Maison Dewey', 'Catherine Dewey', 'Rue Joseph-Bens 532', 'Bruxelles', 'B-1180', 'Belgium'),
  ('Mere Paillarde', 'Jean Fresniere', '43 rue St. Laurent', 'Montreal', 'H1J 1C3', 'Canada'),
  ('Morgenstern Gesundkost', 'Alexander Feuer', 'Heerstr. 22', 'Leipzig', '04179', 'Germany'),
  ('North/South', 'Simon Crowther', 'South House 300 Queensbridge', 'London', 'SW7 1RZ', 'UK'),
  ('Oceano Atlantico Ltda.', 'Yvonne Moncada', 'Ing. Gustavo Moncada 8585 Piso 20-A', 'Buenos Aires', '1010', 'Argentina'),
  ('Old World Delicatessen', 'Rene Phillips', '2743 Bering St.', 'Anchorage', '99508', 'USA'),
  ('Ottilies Keseladen', 'Henriette Pfalzheim', 'Mehrheimerstr. 369', 'Koln', '50739', 'Germany'),
  ('Paris specialites', 'Marie Bertrand', '265, boulevard Charonne', 'Paris', '75012', 'France'),
  ('Pericles Comidas clasicas', 'Guillermo Fernandez', 'Calle Dr. Jorge Cash 321', 'Mexico D.F.', '05033', 'Mexico'),
  ('Piccolo und mehr', 'Georg Pipps', 'Geislweg 14', 'Salzburg', '5020', 'Austria'),
  ('Princesa Isabel Vinhoss', 'Isabel de Castro', 'Estrada da saude n. 58', 'Lisboa', '1756', 'Portugal'),
  ('Que Delicia', 'Bernardo Batista', 'Rua da Panificadora, 12', 'Rio de Janeiro', '02389-673', 'Brazil'),
  ('Queen Cozinha', 'Lucia Carvalho', 'Alameda dos Canarios, 891', 'Sao Paulo', '05487-020', 'Brazil'),
  ('QUICK-Stop', 'Horst Kloss', 'Taucherstrasse 10', 'Cunewalde', '01307', 'Germany'),
  ('Rancho grande', 'Sergio Gutiarrez', 'Av. del Libertador 900', 'Buenos Aires', '1010', 'Argentina'),
  ('Rattlesnake Canyon Grocery', 'Paula Wilson', '2817 Milton Dr.', 'Albuquerque', '87110', 'USA'),
  ('Reggiani Caseifici', 'Maurizio Moroni', 'Strada Provinciale 124', 'Reggio Emilia', '42100', 'Italy'),
  ('Ricardo Adocicados', 'Janete Limeira', 'Av. Copacabana, 267', 'Rio de Janeiro', '02389-890', 'Brazil'),
  ('Richter Supermarkt', 'Michael Holz', 'Grenzacherweg 237', 'Genève', '1203', 'Switzerland'),
  ('Romero y tomillo', 'Alejandra Camino', 'Gran Via, 1', 'Madrid', '28001', 'Spain'),
  ('Santa Gourmet', 'Jonas Bergulfsen', 'Erling Skakkes gate 78', 'Stavern', '4110', 'Norway'),
  ('Save-a-lot Markets', 'Jose Pavarotti', '187 Suffolk Ln.', 'Boise', '83720', 'USA'),
  ('Seven Seas Imports', 'Hari Kumar', '90 Wadhurst Rd.', 'London', 'OX15 4NB', 'UK'),
  ('Simons bistro', 'Jytte Petersen', 'Vinbeltet 34', 'Kobenhavn', '1734', 'Denmark'),
  ('Specialites du monde', 'Dominique Perrier', '25, rue Lauriston', 'Paris', '75016', 'France'),
  ('Split Rail Beer & Ale', 'Art Braunschweiger', 'P.O. Box 555', 'Lander', '82520', 'USA'),
  ('Supremes delices', 'Pascale Cartrain', 'Boulevard Tirou, 255', 'Charleroi', 'B-6000', 'Belgium'),
  ('The Big Cheese', 'Liz Nixon', '89 Jefferson Way Suite 2', 'Portland', '97201', 'USA'),
  ('The Cracker Box', 'Liu Wong', '55 Grizzly Peak Rd.', 'Butte', '59801', 'USA'),
  ('Toms Spezialiteten', 'Karin Josephs', 'Luisenstr. 48', 'Manster', '44087', 'Germany'),
  ('Tortuga Restaurante', 'Miguel Angel Paolino', 'Avda. Azteca 123', 'Mexico D.F.', '05033', 'Mexico'),
  ('Tradicao Hipermercados', 'Anabela Domingues', 'Av. Ines de Castro, 414', 'Sao Paulo', '05634-030', 'Brazil'),
  ('Trails Head Gourmet Provisioners', 'Helvetius Nagy', '722 DaVinci Blvd.', 'Kirkland', '98034', 'USA'),
  ('Vaffeljernet', 'Palle Ibsen', 'Smagsloget 45', 'Arhus', '8200', 'Denmark'),
  ('Victuailles en stock', 'Mary Saveley', '2, rue du Commerce', 'Lyon', '69004', 'France'),
  ('Vins et alcools Chevalier', 'Paul Henriot', '59 rue de l Abbaye', 'Reims', '51100', 'France'),
  ('Die Wandernde Kuh', 'Rita Moller', 'Adenauerallee 900', 'Stuttgart', '70563', 'Germany'),
  ('Wartian Herkku', 'Pirkko Koskitalo', 'Torikatu 38', 'Oulu', '90110', 'Finland'),
  ('Wellington Importadora', 'Paula Parente', 'Rua do Mercado, 12', 'Resende', '08737-363', 'Brazil'),
  ('White Clover Markets', 'Karl Jablonski', '305 - 14th Ave. S. Suite 3B', 'Seattle', '98128', 'USA'),
  ('Wilman Kala', 'Matti Karttunen', 'Keskuskatu 45', 'Helsinki', '21240', 'Finland'),
  ('Wolski', 'Zbyszek', 'ul. Filtrowa 68', 'Walla', '01-012', 'Poland');
```

## Tạo Table `products`

```sh
CREATE TABLE products (
  product_id SERIAL NOT NULL PRIMARY KEY,
  product_name VARCHAR(255),
  category_id INT,
  unit VARCHAR(255),
  price DECIMAL(10, 2)
);
```

Chèn nội dung vào Table `products` với lệnh `INSERT INTO`

```sh
INSERT INTO products (product_id, product_name, category_id, unit, price)
VALUES
  (1, 'Chais', 1, '10 boxes x 20 bags', 18),
  (2, 'Chang', 1, '24 - 12 oz bottles', 19),
  (3, 'Aniseed Syrup', 2, '12 - 550 ml bottles', 10),
  (4, 'Chef Antons Cajun Seasoning', 2, '48 - 6 oz jars', 22),
  (5, 'Chef Antons Gumbo Mix', 2, '36 boxes', 21.35),
  (6, 'Grandmas Boysenberry Spread', 2, '12 - 8 oz jars', 25),
  (7, 'Uncle Bobs Organic Dried Pears', 7, '12 - 1 lb pkgs.', 30),
  (8, 'Northwoods Cranberry Sauce', 2, '12 - 12 oz jars', 40),
  (9, 'Mishi Kobe Niku', 6, '18 - 500 g pkgs.', 97),
  (10, 'Ikura', 8, '12 - 200 ml jars', 31),
  (11, 'Queso Cabrales', 4, '1 kg pkg.', 21),
  (12, 'Queso Manchego La Pastora', 4, '10 - 500 g pkgs.', 38),
  (13, 'Konbu', 8, '2 kg box', 6),
  (14, 'Tofu', 7, '40 - 100 g pkgs.', 23.25),
  (15, 'Genen Shouyu', 2, '24 - 250 ml bottles', 15.5),
  (16, 'Pavlova', 3, '32 - 500 g boxes', 17.45),
  (17, 'Alice Mutton', 6, '20 - 1 kg tins', 39),
  (18, 'Carnarvon Tigers', 8, '16 kg pkg.', 62.5),
  (19, 'Teatime Chocolate Biscuits', 3, '10 boxes x 12 pieces', 9.2),
  (20, 'Sir Rodneys Marmalade', 3, '30 gift boxes', 81),
  (21, 'Sir Rodneys Scones', 3, '24 pkgs. x 4 pieces', 10),
  (22, 'Gustafs Kneckebrod', 5, '24 - 500 g pkgs.', 21),
  (23, 'Tunnbrod', 5, '12 - 250 g pkgs.', 9),
  (24, 'Guarani Fantastica', 1, '12 - 355 ml cans', 4.5),
  (25, 'NuNuCa Nui-Nougat-Creme', 3, '20 - 450 g glasses', 14),
  (26, 'Gumber Gummiberchen', 3, '100 - 250 g bags', 31.23),
  (27, 'Schoggi Schokolade', 3, '100 - 100 g pieces', 43.9),
  (28, 'Rassle Sauerkraut', 7, '25 - 825 g cans', 45.6),
  (29, 'Thoringer Rostbratwurst', 6, '50 bags x 30 sausgs.', 123.79),
  (30, 'Nord-Ost Matjeshering', 8, '10 - 200 g glasses', 25.89),
  (31, 'Gorgonzola Telino', 4, '12 - 100 g pkgs', 12.5),
  (32, 'Mascarpone Fabioli', 4, '24 - 200 g pkgs.', 32),
  (33, 'Geitost', 4, '500 g', 2.5),
  (34, 'Sasquatch Ale', 1, '24 - 12 oz bottles', 14),
  (35, 'Steeleye Stout', 1, '24 - 12 oz bottles', 18),
  (36, 'Inlagd Sill', 8, '24 - 250 g jars', 19),
  (37, 'Gravad lax', 8, '12 - 500 g pkgs.', 26),
  (38, 'Cote de Blaye', 1, '12 - 75 cl bottles', 263.5),
  (39, 'Chartreuse verte', 1, '750 cc per bottle', 18),
  (40, 'Boston Crab Meat', 8, '24 - 4 oz tins', 18.4),
  (41, 'Jacks New England Clam Chowder', 8, '12 - 12 oz cans', 9.65),
  (42, 'Singaporean Hokkien Fried Mee', 5, '32 - 1 kg pkgs.', 14),
  (43, 'Ipoh Coffee', 1, '16 - 500 g tins', 46),
  (44, 'Gula Malacca', 2, '20 - 2 kg bags', 19.45),
  (45, 'Rogede sild', 8, '1k pkg.', 9.5),
  (46, 'Spegesild', 8, '4 - 450 g glasses', 12),
  (47, 'Zaanse koeken', 3, '10 - 4 oz boxes', 9.5),
  (48, 'Chocolade', 3, '10 pkgs.', 12.75),
  (49, 'Maxilaku', 3, '24 - 50 g pkgs.', 20),
  (50, 'Valkoinen suklaa', 3, '12 - 100 g bars', 16.25),
  (51, 'Manjimup Dried Apples', 7, '50 - 300 g pkgs.', 53),
  (52, 'Filo Mix', 5, '16 - 2 kg boxes', 7),
  (53, 'Perth Pasties', 6, '48 pieces', 32.8),
  (54, 'Tourtiare', 6, '16 pies', 7.45),
  (55, 'Pate chinois', 6, '24 boxes x 2 pies', 24),
  (56, 'Gnocchi di nonna Alice', 5, '24 - 250 g pkgs.', 38),
  (57, 'Ravioli Angelo', 5, '24 - 250 g pkgs.', 19.5),
  (58, 'Escargots de Bourgogne', 8, '24 pieces', 13.25),
  (59, 'Raclette Courdavault', 4, '5 kg pkg.', 55),
  (60, 'Camembert Pierrot', 4, '15 - 300 g rounds', 34),
  (61, 'Sirop d arable', 2, '24 - 500 ml bottles', 28.5),
  (62, 'Tarte au sucre', 3, '48 pies', 49.3),
  (63, 'Vegie-spread', 2, '15 - 625 g jars', 43.9),
  (64, 'Wimmers gute Semmelknadel', 5, '20 bags x 4 pieces', 33.25),
  (65, 'Louisiana Fiery Hot Pepper Sauce', 2, '32 - 8 oz bottles', 21.05),
  (66, 'Louisiana Hot Spiced Okra', 2, '24 - 8 oz jars', 17),
  (67, 'Laughing Lumberjack Lager', 1, '24 - 12 oz bottles', 14),
  (68, 'Scottish Longbreads', 3, '10 boxes x 8 pieces', 12.5),
  (69, 'Gudbrandsdalsost', 4, '10 kg pkg.', 36),
  (70, 'Outback Lager', 1, '24 - 355 ml bottles', 15),
  (71, 'Flotemysost', 4, '10 - 500 g pkgs.', 21.5),
  (72, 'Mozzarella di Giovanni', 4, '24 - 200 g pkgs.', 34.8),
  (73, 'Red Kaviar', 8, '24 - 150 g jars', 15),
  (74, 'Longlife Tofu', 7, '5 kg pkg.', 10),
  (75, 'Rhenbreu Klosterbier', 1, '24 - 0.5 l bottles', 7.75),
  (76, 'Lakkalikeeri', 1, '500 ml ', 18),
  (77, 'Original Frankfurter gr�ne Soae', 2, '12 boxes', 13);
```

## Tạo Table `testproducts`

```sh
CREATE TABLE testproducts (
  testproduct_id SERIAL NOT NULL PRIMARY KEY,
  product_name VARCHAR(255),
  category_id INT
);
```

Chèn nội dung vào Table `testproducts` với lệnh `INSERT INTO`

```sh
INSERT INTO testproducts (product_name, category_id)
VALUES
  ('Johns Fruit Cake', 3),
  ('Marys Healthy Mix', 9),
  ('Peters Scary Stuff', 10),
  ('Jims Secret Recipe', 11),
  ('Elisabeths Best Apples', 12),
  ('Janes Favorite Cheese', 4),
  ('Billys Home Made Pizza', 13),
  ('Ellas Special Salmon', 8),
  ('Roberts Rich Spaghetti', 5),
  ('Mias Popular Ice', 14);
```

Sau khi tạo xong các Table trên ta kiểm tra lại các Table trong Database như sau:

```sh
mydb=# \dt
           List of relations
 Schema |     Name     | Type  | Owner 
--------+--------------+-------+-------
 public | categories   | table | tubt
 public | customers    | table | tubt
 public | products     | table | tubt
 public | testproducts | table | tubt
(4 rows)
```

# Export Database

Để export database PostgreSQL ta sử dụng `pg_dump`. Truy cập SSH vào user có quyền thao tác với DB và chạy lệnh sau:

**Syntax:**

```sh
pg_dump -U db_username db_name > db_export.pgsql
```

Trong đó:

- `db_username`: Username có quyền thao tác với database cần export

- `db_name`: Tên database cần export

- `db_export.pgsql`: Tên file export muốn lưu. Ta cũng có thể đưa đường dẫn tuyệt đối để thực hiện lưu file tại đường dẫn đó, ở đây mình thực hiện lưu file export tại nơi chạy câu lệnh `pg_dump`

**Output:**

```sh
[tubt@postgres ~]$ pg_dump -U tubt mydb > myfirstdb.pgsql

[tubt@postgres ~]$ ls -lah myfirstdb.pgsql 
-rw-rw-r--. 1 tubt tubt 18K Sep 26 09:46 myfirstdb.pgsql
```

Sau khi chạy lệnh trên ta kiểm tra thấy file export `myfirstdb.pgsql` đã được tạo và hiện có dung lượng `18KB`, trong thực tế dung lượng của một file DB có kích thước lớn hơn rất nhiều

# Xóa DB hiện tại và thực hiện import DB bằng file `myfirstdb.pgsql` vừa mới export

Tiếp theo chúng ta thực hiện xóa DB `mydb`, tạo một DB mới có tên là `testdb` và thực hiện import DB từ file `myfirstdb.pgsql`

Đăng nhập vào Postgres với user có quyền xóa DB. Ở đây user `tubt` có quyền xóa DB `mydb` nên mình sẽ đăng nhập vào nó và thực hiện chạy lệnh dưới

Để xóa DB `mydb`, ta chạy lệnh sau:

```sh
DROP DATABASE mydb;
```

Hoặc ta có thể xóa DB từ Shell của Linux mà không cần đăng nhập vào Postgres với lệnh sau:

```sh
[tubt@postgres ~]$ dropdb -h localhost -p 5432 -U tubt mydb
Password: 
```

Nhập password để thực hiện xóa DB `mydb`

**Thực hiện tạo mới DB `testdb`:**

Đăng nhập vào Postgres và chạy lệnh

```sh
CREATE DATABASE testdb
```

Hoặc tạo DB từ Shell Linux với lệnh sau:

```sh
[tubt@postgres ~]$ createdb -h localhost -p 5432 -U tubt testdb
Password:
```

Nhập password để thực hiện tạo mới DB `testdb`

Truy cập vào Postgres và chạy lệnh `\l` (list) để kiểm tra db đã được tạo chưa

```sh
tubt=# \l
                                                 List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    | ICU Locale | Locale Provider |   Access privileges   
-----------+----------+----------+-------------+-------------+------------+-----------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | =c/postgres          +
           |          |          |             |             |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | =c/postgres          +
           |          |          |             |             |            |                 | postgres=CTc/postgres
 testdb    | tubt     | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | 
 tubt      | tubt     | UTF8     | en_US.UTF-8 | en_US.UTF-8 |            | libc            | 
(5 rows)
```

**Thực hiện import DB từ file `myfirstdb.pgsql`**

Để thực import DB ta chạy lệnh như sau:

Syntax:

```sh
psql -U user_name db_name < db_export.pgsql
```

Output:

```sh
[tubt@postgres ~]$ psql -U tubt testdb < myfirstdb.pgsql 
SET
SET
SET
SET
SET
 set_config 
------------
 
(1 row)

SET
SET
SET
SET
SET
SET
CREATE TABLE
ALTER TABLE
CREATE SEQUENCE
ALTER TABLE
ALTER SEQUENCE
CREATE TABLE
ALTER TABLE
CREATE SEQUENCE
ALTER TABLE
ALTER SEQUENCE
CREATE TABLE
ALTER TABLE
CREATE SEQUENCE
ALTER TABLE
ALTER SEQUENCE
CREATE TABLE
ALTER TABLE
CREATE SEQUENCE
ALTER TABLE
ALTER SEQUENCE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
COPY 8
COPY 91
COPY 77
COPY 10
 setval 
--------
      8
(1 row)

 setval 
--------
     91
(1 row)

 setval 
--------
      1
(1 row)

 setval 
--------
     10
(1 row)

ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
```

Sau khi import DB, truy cập vào Postgres, select đến DB `testdb` để kiểm tra dữ liệu đã được restore hay chưa:

```sh
[tubt@postgres ~]$ psql
psql (15.4)
Type "help" for help.

tubt=# \c testdb 
You are now connected to database "testdb" as user "tubt".

testdb=# \dt
           List of relations
 Schema |     Name     | Type  | Owner 
--------+--------------+-------+-------
 public | categories   | table | tubt
 public | customers    | table | tubt
 public | products     | table | tubt
 public | testproducts | table | tubt
(4 rows)

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

Sau khi kiểm tra ta thấy 4 Table (`categories`, `customers`, `products`, `testproducts`) đã được khôi phục như ban đầu, vậy là việc export và import đã thành công.