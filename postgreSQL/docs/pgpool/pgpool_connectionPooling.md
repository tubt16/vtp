# Connection Pooling

Pgpool-II duy trì các kết nối đã thiết lập với máy chủ PostgreSQL và sử dụng lại chúng bất cứ khi nào có kết nối mới cùng thuộc tính (tức là người dùng, cơ sở dữ liệu, phiên bản giao thức). Nó giúp giảm lượng kết nối và cải thiện thông lượng tổng thể của hệ thống

# Connection Pooling Settings

`connection_cache` (boolean)

Lưư các kết nối tới Backend vào bộ đệm (Mặc định `connection_cache = on` nếu không chỉ định). Tuy nhiên, các kết nối tới cơ sở dữ liệu `template0`, `template1` , `postgres` và `regression` không được lưu vào bộ đệm ngay cả khi bật `connection_cache`

`max_pool` (integer)

Số lượng kết nối được cho phép lưu trong bộ nhớ đệm tối đa trong mỗi tiến trình con Pgpool-II. Pgpool-II sử dụng lại kết nối được lưu trong bộ nhớ đệm nếu kết nối đến đang kết nối với cùng một cơ sở dữ liệu có cùng tên người dùng và cùng tham số run-time. Nếu không, Pgpool-II sẽ tạo kết nối mới tới các backend server. Nếu số lượng kết nối được lưu trong bộ nhớ cache vượt quá `max_pool`, kết nối cũ nhất định sẽ bị loại bỏ và sử dụng vị trí đó cho kết nối mới

Giá trị mặc định là 4

`listen_backlog_multiplier` (integer)

Chỉ định độ dài của hàng đợi kết nối từ giao diện người dùng đến Pgpool-II. Giá trị mặc định là 2

`serialize_accept` (boolean)

Tham số `serialize_accept` trong Pgpool là một cấu hình được sử dụng để kiểm soát việc xử lý song song của các kết nối client trong Pgpool-II. Khi Pgpool-II nhận được nhiều kết nối client đồng thời, mặc định nó sẽ xử lý chúng theo cách song song, có nghĩa là nó sẽ chấp nhận và xử lý các kết nối mà không cần cần chờ kết thúc xử lý của kết nối trước đó. Điều này có thể dẫn đến việc đọc ghi dữ liệu trong các kết nối xảy ra cùng một lúc, có thể gây ra xung đột và không đồng nhất dữ liệu

Tuy nhiên khi đặt tham số `serialize_accept` thành `on` trong tệp cấu hình của Pgpool-II, nó sẽ tắt chế độ xử lý song song và chỉ chấp nhận một kết nối client mới sau khi kết nối trước đó được xử lý hoàn toàn. Điều này đảm bảo rằng các truy vấn và thay đổi dữ liệu của các kết nối client sẽ được thực hiện theo tuyến tính, tránh xung đột

`child_life_time` (integer)

Chỉ định thời gian sống tối đa của một tiến trình con (child process) được tạo ra để xử lý các kết nối đến Pgpool-II. Khi một tiến trình đã tồn tại trong một thời gian vượt quá giá trị `child_life_time`, nó sẽ bị chấm dứt và thay thế bằng một tiến trình con mới. Điều này giúp giảm tài nguyên hệ thống được sử dụng bởi các tiến trình con và giữ cho Pgpool-II hoạt động ổn định trong thời gian dài

`child_max_connection` (integer)

Là một tham số chỉ định số lượng kết nối tối đa mà Pgpool-II có thể xử lý đồng thời. Mỗi kết nối từ ứng dụng sẽ được gửi tới một tiến trình con (child process) trong Pgpool-II để xử lý

Khi số lượng kết nối đến Pgpool-II vượt quá giá trị `child _max_connection`, Pgpool-II sẽ từ chối kết nối cho các yêu cầu mới cho đến khi một kết nối có sẵn được giải phóng. Điều này giúp đảm bảo rằng Pgpool-II không bị quá tải và giữ cho hệ thống hoạt động ổn định

`connection_life_time` (integer)

Chỉ định thời gian để chấm dứt các kết nối được lưu trong bộ nhớ đệm tới các backend server. Điều này đóng vai trò là thời gian hết hạn kết nối được lưu trong bộ nhớ cache. Giá trị mặc định là 0, có nghĩa là các kết nối được lưu trong bộ nhớ đệm sẽ không bị ngắt kết nối

`reset_query_list` (string)

Chỉ định các lệnh SQL sẽ được gửi để đặt lại kết nối phụ trợ khi thoát khỏi phiên người dùng. Nhiều lệnh có thể được chỉ định bằng cách phân cách từ lệnh bằng dấu ";"

Dưới đây là một số tùy chọn được đề xuất cho `reset_query_list` trên các phiên bản PostgreSQL khác nhau

|PostgreSQL version|reset_query_list|
|7.1 or earlier|'ABORT'|
|7.2 to 8.2|'ABORT; RESET ALL; SET SESSION AUTHORIZATION DEFAULT'|
|8.3 or later|'ABORT; DISCARD ALL'|

Ví dụ

```sh
reset_query_list = 'ABORT; DISCARD ALL'
```

> Tham khảo: https://www.pgpool.net/docs/44/en/html/runtime-config-connection-pooling.html