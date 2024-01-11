# Pgpool-II

Pgpool-II là phần mềm trung gian hoạt động giữa các PostgreSQL server và các PostgreSQL client.

Bài toán: Giả sử Database PostgreSQL của bạn đang gặp vấn đề nghiêm trọng về mặt hiệu năng do có quá nhiều connection kết nối đến

Trong trường hợp này một giải pháp `Connection Pooling` như `Pgpool-II` có thể là 1 giải pháp phù hợp

Ý tưởng của `Connection Pool` cở bản là mở sẵn 1 loạt các connection, các ứng dụng khi muốn kết nối vào sẽ đấu nối vào các connection đã mở sẵn đó, nếu kết nối nào vào sau mà không còn connection đã mở sẵn thì sẽ phải đợi các kết nối trước đó kết thúc

**Pgpool-II là một phần mềm Connection Pooling đứng giữa PostgreSQL Server và PostgreSQL Client, nó đóng vai trò là một proxy server, đứng trước các PostgreSQL server và PostgreSQL Standby server, nó nhận các request đến từ client sau đó forward lại cho các node tương ứng**

Nói đơn giản hơn nó là lớp TRUNG GIAN giữa người sử dụng và PostgreSQL server

# Các tính năng của PGPool

PGPool có rất nhiều tính năng hữu ích:

**1. Connection Pooling:**

Pgpool-II quản lý các connection đã được kết nối đến PostgreSQL Server và nó sẽ TÁI SỬ DỤNG lại các connection cũ mỗi khi có connection mới có cùng các thuộc tính với connect đã kết nối (như username, database, version protocol ...). Nó giúp **giảm tổng lượng thông tin overhead** trên tất cả connection, từ đó cải thiện hiệu năng tổng thể

**2. Load Balancing**

Nếu bạn đã cấu hình tính năng `Streaming Replication` bao gồm 1 server master với 1 hoặc nhiều server slave, Pgpool-II có thể giúp giảm tải cho server master bằng cách đẩy các câu lệnh SELECT sang các server slave. Chức năng Load Balancing rất hữu ích trong tình huống có rất nhiều user thực hiện các câu lệnh SELECT xuống database

Đọc thêm về `Streaming Replication` tại [đây](./postgreSQL_streamingReplication.md)

**3. Automated fail over**

Nếu database server master bị shutdown và không thể hoạt động, Pgpool-II sẽ gỡ nó ra khỏi cấu hình và đưa database server slave lên thành master. Đây gọi là cơ chế `Automated fail over`

**4. Online Recovery**

Sau khi database server master bị gỡ ra khỏi cấu hình đồng bộ theo cơ chế `Automated fail over`, Pgpool-II có thể đưa nó trở lại cấu hình cũ với một câu lệnh. Cơ chế này gọi là Online Recovery

**5. Replication**

Cũng giống như Streaming Replication, Pgpool-II cũng có 1 chức năng tương tự. Nó cho phép tạo ra 1 database cluster khác đồng bộ liên tục theo thời gian thực với database cluster chính

**6. Max connection**

Trong PostgreSQL, bạn có thể cấu hình tham số `max_connection` để giới hạn số connection tối đa được phép kết nối vào hệ thống. Tuy nhiên, nếu hệ thống đạt max connection thì những connection kết nối vào sau sẽ nhận được một thông báo lỗi và bị ngắt luôn. Pgpool-II cũng cung cấp 1 cơ chế giới hạn connection như vậy nhưng **mềm mại** hơn, những connection bị vượt ra ngoài pham vị max connection, sẽ được đưa vào 1 hàng đợi, chờ đến lượt thay vì bị văng ra ngoài kèm theo 1 thông báo lỗi

**7. Watchdog**

Pgpool là nơi phân tải đến các database server ở đằng sau, vì thể khi Pgpool có trục trặc, sẽ không thể kết nối đến database được nữa. Tính năng Watchdog cho phép bạn xây dựng nhiều Pgpool dự phòng. Nó sẽ kiểm tra trạng thái của Pgpool chính, nếu phát hiện Pgpool chính bị down, nó sẽ đưa Pgpool dự phòng lên thành Pgpool chính dựa trên cơ chế bình bầu (voting)

Nếu số lượng Pgpool là số chẵn thì sẽ không thể bình bầu để quyết định được Pgpool nào là chính, do đó, số lượng Pgpool nên là số lẻ

**8. In Memory Query Cache**

Chức năng này cho phép lưu giữ câu lệnh và kết quả thực hiện của nó trên Memory. Nếu có 1 câu lệnh SELECT giống hệt câu lệnh câu lệnh đã có trên Memory, Pgpool sẽ trả kết quả lấy từ Memory xuống luôn mà không cần truy vấn xuống đĩa để xử lý nữa