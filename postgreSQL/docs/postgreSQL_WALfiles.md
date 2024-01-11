# PostgreSQL WAL là gì ?

## Giới thiệu WAL

Một trong các thành phần QUAN TRỌNG NHẤT trong PostgreSQL đó là Write-ahead Log (WAL). WAL phục vụ cho mục đích khôi phục lại database khi PostgreSQL bị shutdown đột ngột

`WAL` trong PostgreSQL là những file lưu trữ thông tin **mô tả sự thay đổi** trong database

## Sự cần thiết của WAL

**Ví dụ:**

Khi bạn cần Update 1 giá trị A thành B, thì giá trị mới (B) **chưa được ghi thẳng xuống ổ đĩa**

Nguyên nhân là bởi: Trong 1 hệ thống có rất nhiều thay đổi, nếu mỗi lần thay đổi đã ghi xuống đĩa luôn như thế, thì hệ thống không thể đủ khả năng xử lý hết được

Cách làm tốt hơn là khi có thay đổi thì các thay đổi đó chỉ được ghi lại trên memory thôi, ví dụ thay đổi giá trị A thành B ở trên memory và chưa ghi xuống đĩa ngay

Sau khi có nhiều thay đổi thì mới **gom các thay đổi này rồi mới ghi xuống đĩa**. Như vậy sẽ giảm số lượng request xuống đĩa hơn

Tuy nhiên, điều này dẫn đến nảy sinh một vấn đề khác là giá trị B mà chúng ta thay đổi đang ở trên memory chưa kịp lưu xuống đĩa thì chẳng may server bị mất điện thì sao??

Như chúng ta đều biết Memory là bộ nhớ **lưu trữ tạm thời** và sẽ được giải phóng khi shutdown hoặc reboot server... Nếu mất điện thì dữ liệu trên Memory sẽ bị xóa hết, **Vậy giá trị B của tôi cũng mất luôn**

Vậy nên `WAL` được ra đời để khắc phục vấn đề đó

**Cơ chế**

Cơ chế lúc này như sau: Khi bạn thay đổi A thành B, B sẽ thay thế A nằm ở trên Memory, tuy nhiên PostgreSQL sẽ tạo ra một mẩu thông tin mô tả về sự thay đổi (Lưu ý, đây chỉ là thông tin về sự thay đổi của giá trị) đó và nó sẽ được lưu vào 1 file nằm trên đĩa, đó là file `WAL`

Dữ liệu A được B có thể lớn, nhưng thông tin mô tả về thay đổi sẽ rất NHỎ, nên lựa chọn lưu file xuống `WAL` sẽ nhanh hơn rất nhiều so với lưu dữ liệu đầy đủ (như A hoặc B)

Vậy, khi máy chủ bị mất điện thì dữ liệu trên Memory bị xóa sạch. Khi database khởi động trở lại, dữ liệu ở dưới đĩa vẫn là dữ liệu cũ (dữ liệu A). Tuy nhiên, nó sẽ đọc các thông tin thay đổi ở trong WAL file và phát hiện thấy **A đã được thay đổi thành B**. Như vậy nó sẽ biết cần phải thực hiện recover để **khôi phục lại dữ liệu B**

## Đặc điểm của WAL file

Như đã nói ở trên, WAL file là 1 file nằm trên đĩa cứng. Nó nằm trong data directory (hay thư mục lưu dữ liệu của PostgreSQL) `/var/lib/pgsql/15/data/pg_wal`

```sh
[root@postgres ~]# ls -lah /var/lib/pgsql/15/data/pg_wal/
total 81M
drwx--x--x.  3 postgres postgres 4.0K Oct  2 06:01 .
drwx------. 20 postgres postgres 4.0K Oct  2 00:00 ..
-rw-------.  1 postgres postgres  16M Oct  2 06:01 000000050000000000000027
-rw-------.  1 postgres postgres  16M Oct  2 01:55 000000050000000000000028
-rw-------.  1 postgres postgres  16M Oct  2 05:54 000000050000000000000029
-rw-------.  1 postgres postgres  16M Oct  2 05:56 00000005000000000000002A
-rw-------.  1 postgres postgres  16M Oct  2 05:56 00000005000000000000002B
```

Kích thước mặc định của `WAL` file là 16MB. Bạn hoàn toàn có thể điều chỉnh kích thước của `WAL` file thông qua tham số `max_wal_size`

Kiểm tra kích thước của `WAL` file hiện tại bằng câu lệnh

```sh
show max_wal_size;

 max_wal_size
--------------
 16M
(1 row)
```

Sau khi sử dụng hết 16MB, hệ thống sẽ tự sinh ra một `WAL` file mới, và cứ tiếp tục như thế

Mỗi khi có thay đổi trong database, một bản ghi mô tả thay đổi sẽ được sinh ra và nối vào `WAL` file hiện tại. Mỗi bản ghi này sẽ được ghi cùng với số thứ tự của nó hay còn gọi là `Log Sequence Number (LSN)`. Số LSN được lưu trong control file

Khi cần sử dụng `WAL` file để khôi phục, hệ thống sẽ so sánh LSN hiện tại (VD: LSN_n) với LSN được lưu trong control file (VD: LSN_1). Nếu LSN_n > LSN_1 thì hệ thống sẽ hiểu rằng nó sẽ cần phải recover bằng cách lấy bản ghi trong WAL file từ LSN_1 trước rồi mới đến LSN_n

## Tham số cấu hình wal_level

Tham số `wal_level` quy định **bao nhiêu thông tin sẽ được ghi lại vào WAL**. Nó có thể nhận các giá trị `minimum`, `replica`, `logical` sắp xếp mức độ chi tiết **tăng dần**

- Ở mức độ `minimum`, WAL chỉ chứa thông tin tối thiểu đủ để khôi phục database cluster trong trường hợp bị crash đột ngột

- Ở mức độ `replica`, WAL bao gồm các thông tin ở mức độ minimum, kèm theo đó là các thông tin đủ để hỗ trợ cho các tính năng như archive log mode, streaming replication

- Ở mức độ `logical`, WAL bao gồm các thông tin ở mức độ repica, kèm theo đó là các thông tin để hỗ trợ tính năng logical replication

Mặc định `wal_level = replica`

```sh
postgres=# show wal_level;
 wal_level 
-----------
 replica
(1 row)
```

`wal_level` càng cao thì càng hỗ trợ nhiều tính năng hơn, tuy nhiên tài nguyên sử dụng cũng nhiều hơn. Chúng ta cần cân nhắc điều này khi đặt giá trị cho tham số `wal_level`
