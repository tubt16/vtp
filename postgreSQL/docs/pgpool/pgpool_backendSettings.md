# Backend Settings

## Backend Connection Settings

`backend_hostname` (string)

- `backend_hostname` chỉ định PostgreSQL backend sẽ được kết nối (Có thể là IP hoặc hostname của máy chủ). Nó được Pgpool-II sử dụng để liên lạc với máy chủ

Nếu có nhiều backend server, thì ta có thể chỉ định bằng cách thêm một số vào cuối tên tham số (ví dụ `backend_hostname0`). Số này được gọi là "ID". Backend được cấp ID là 0 sẽ được gọi là node chính (Primary). Khi xác định nhiều backend server, dịch vụ có thể được tiếp tục ngay cả khi node chính không hoạt động (Chỉ đúng với một vài chế độ trong Pgpool). Trong trường hợp này node có ID thấp nhất sẽ được lên làm Primary (Ví dụ cụm có 3 node và ID lần lượt là 0 1 và 2, khi node 0 bị down thì node có ID = 1 sẽ lên làm Primary)

`backend_port` (interger)

- `backend_port` chỉ định port của backend. nếu có nhiều backend server, ta có thể chỉ định bằng cách thêm ID vào cuối tham số (ví dụ `backend_port0`)

`backend_weight` (float)

- `backend_weight` chỉ định tỷ lệ cân bằng tải của backend. Nó có thể được đặt giá trị là bất kỳ số nguyên nào lớn hơn hoặc bằng 0. Có thể chỉ định nhiều `backend_weight` bằng cách thêm ID vào cuối tham số (Ví dụ `backend_weight0`)

- Ví dụ: Có 3 backend server và tỉ lệ như sau `backend_weight0 = 2`, `backend_weight1 = 1`, `backend_weight2 = 1`. Tỉ lệ cân bằng tải cho node 0 sẽ là 50%, node 1 và 2 mỗi node sẽ chiếm 25%

## Backend Data Settings

`backend_data_directory` (string)

- `backend_data_directory` chỉ định thư mục chứa cơ sở dữ liệu của backend server. Nếu bạn không sử dụng chức năng Online Recovery thì không cần thiết lập tham số này

`backend_flag` (string)

- `backend_flag` kiểm tra các tùy chọn của các backend server. Các tùy chọn sẽ được liệt kê ở bảng bên dưới

**Backend flags**

|Flag|Description|
|---|---|
|ALLOW_TO_FAILOVER|Cho phép chuyển đổi dự phòng (failover). Đây là giá trị mặc định nếu bạn để trống tham số `backend_flag`|
|DISALLOW_TO_FAILOVER|Không cho phép chuyển đổi dự phòng|
|ALWAYS_PRIMARY|Tùy chọn này chỉ hữu ích trong chế độ Streaming Replication. Nếu tùy này được đặt thành một trong các node backend, Pgpool-II sẽ không tìm thấy node chính bằng cách kiểm tra node backend, thay vào đó, node được khai báo trong tùy chọn sẽ luôn được coi là node chính|

`backend_application_name` (string)

- `backend_application_name` chỉ định tên ứng dụng nhận nhật ký WAL từ node Primary. Do đó tham số này không nhất thiết phải đặt ngoại trừ khi sử dụng chế độ Streaming Replication, Ngoài ra tham số này là bắt buộc nếu bạn muốn hiển thị cột `replication_state` và `replication_sync_state` trong lệnh `SHOW POOL_NODES` và `pcp_node_info`

- Ví dụ:

```sh
backend_application_name2 = '192.168.10.1'
```

> Tham khảo: https://www.pgpool.net/docs/44/en/html/runtime-config-backend-settings.html