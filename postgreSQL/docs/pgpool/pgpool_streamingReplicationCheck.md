# Streaming Replication Check

Pgpool-II có thể hoạt động với PostgreSQL Streaming Replication. Để định cấu hình Pgpool-II với Streaming Replication, hãy đặt `backend_clustering_mode = 'streaming_replication'`

`sr_check_period` (integer)

- Chỉ định khoảng thời gian tính bằng giây để check độ trễ Streaming Replication. Mặc định là 10s

`sr_check_user` (string)

- Chỉ định tên người dùng PostgreSQL để thực hiện check Streaming replication. Người dùng phải có đặc quyền ĐĂNG NHẬP và tồn tại trên tất cả các backend server của PostgreSQL

`sr_check_password` (string)

- Chỉ định mật khẩu của người dùng `sr_check_user` PostgreSQL để thực hiện check Streaming replication. Sử dụng empty string nếu người dùng không yêu cầu mật khẩu

- Nếu `sr_check_password` được để trống, Pgpool-II trước tiên sẽ lấy mất khẩu từ tệp `pool_password` trước khi sử dụng mật khẩu trống

- Các dạng mật khẩu `sr_check_password` chấp nhận:

	+ AES256-CBC encrypted password

	+ MD5 hashed password

	+ Plain text password (không khuyến khích sử dụng vì mật khẩu sẽ ở dạng clear text rất dễ bị khai thác)

`sr_check_database` (string)

- Chỉ định cơ sở dữ liệu để thực hiện kiểm tra độ trễ Streaming replication. Mặc định là `postgres`

`delay_threshold` (integer)

- Là một tùy chọn cấu hình để xác định ngưỡng thời gian chễ (delay) giữa các node trong cụm. Nếu thời gian trễ vượt qua ngưỡng này, Pgpool-II có thể xem node đó là không khả dụng và chuyển hướng các truy vấn SELECT đến một node khác

- Khi delay_threshold được đặt, Pgpool-II sẽ so sánh thời gian trễ giữa node chính (primary node) và các node dự phòng (standby nodes). Nếu thời gian trễ của node chính vượt qua giá trị `delay_threshold`, Pgpool-II có thể đánh giá node chính là không khả dụng và chuyển hướng các truy vấn SELECT đến một node dự phòng

> Tham khảo: https://www.pgpool.net/docs/44/en/html/runtime-streaming-replication-check.html