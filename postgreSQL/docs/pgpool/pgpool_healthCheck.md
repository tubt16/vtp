# Health Check

Pgpool-II kết nối định kỳ với các backend server PostgreSQL đã được định cấu hình để phát hiện bất kỳ lỗi nào trên các máy chủ đó. Quy trình kiểm tra lỗi này được gọi là `Health check`

Nếu SSL được bật, quá trình kiểm tra tình trạng có thể sử dụng kết nối SSL

Nếu phát hiện ra node bị lỗi, Pgpool-II sẽ thực hiện chuyển đổi dự phòng (failover) để đưa node Standby có id thấp nhất đang hoạt động lên làm Primary server

`health_check_timeout` (integer)

- Chỉ định thời gian chờ tính bằng giây để từ bỏ kết nối với PostgreSQL backend nếu kết nối TCP không thành công trong thời gian này

- Nếu Pgpool-II không nhận được phản hồi từ một node trong khoảng thời gian `health_check_timeout`, nó sẽ coi node đó là không khả dụng và loại node đó ra khỏi danh sách các node có sẵn. Giá trị mặc định là 20

`health_check_period` (integer)

- Chỉ định khoảng thời gian giữa các lần health check

`health_check_user` (string)

- Chỉ định người dùng PostgreSQL để thực hiện health check. Cùng một người dùng phải tồn tại trong tất cả các backend server của PostgreSQL, nếu không quá trình health check sẽ gây ra lỗi

`health_check_password` (string)

- Chỉ định mật khẩu cho người dùng PostgreSQL được định cấu hình trong `health_check_user` để thực hiện health check. Người dùng và mật khẩu phải giống nhau trong tất cả các backend server của PostgreSQL

- Nếu `health_check_password` được để trống, Pgpool-II trước tiên sẽ cố lấy mật khẩu cho `health_check_user` từ tệp `pool_passwd` trước khi sử dụng mật khẩu trống

- Pgpool-II chấp nhận các dạng mật khẩu sau trong tệp `pool_passwd`:

	+ AES256-CBC encrypted password
	+ MD5 hashed password
	+ Plain text password (không khuyến khích vì mật khẩu được lưu ở dạng clear text nên rất dễ bị khai thác)

`health_check_database` (string)

- Chỉ định tên cơ sở dữ liệu PostgreSQL để thực hiện health check. Giá trị mặc định là `empty`, đầu tiên sẽ thử với database `postgres` trước, sau đó sẽ thử với database `template1` cho đến khi thành công

`health_check_max_retries` (integer)

- Chỉ định số lần thử lại tối đa cần thực hiện trước khi loại bỏ node và bắt đầu chuyển đổi dự phòng khi kiểm tra không thành công

`health_check_retry_delay` (integer)

- Chỉ định khoảng thời gian chờ (delay) giữa các lần thử lại khi health check không thành công. Tham số này không được chỉ định trừ khi `health_check_max_retries` > 0 

`connect_timeout` (integer)

- Chỉ định thời gian tối đa mà Pgpool-II sẽ chờ đợi để thiết lập kết nối với một node backend

- Nếu Pgpool-II không nhận được phản hồi từ một node trong khoảng thời gian `connect_timeout`, nó sẽ coi node đó là không khả dụng và loại node đó khỏi danh sách các node sẵn có để chịu trách nhiệm xử lý các yêu cầu. Giá trị mặc định là 10000ms