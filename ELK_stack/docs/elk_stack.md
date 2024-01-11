# ELK stack

ELK stack là một tập hợp phần mềm nguồn mở do Elastic sản xuất, cho phép tìm kiếm, phân tích và trực quan hóa nhật ký được tạo ra từ bất kỳ nguồn nào ở bất kỳ định dạng nào

ELK stack là tập hợp 3 phần mềm đi chung với nhau, phục vụ công việc logging. Ba phần mềm này lần lượt là:

- Elasticsearch: Cơ sở dữ liệu lưu trữ, tìm kiếm và query log

- Logstash: Tiếp nhận log từ nhiều nguồn, sau đó xử lý log và ghi dữ liệu vào Elasticsearch

- Kibana: Giao diện để quản lý, thống kê log. Đọc thông tin từ Elasticsearch

**Cơ chế hoạt động của ELK stack:**

![](/ELK_stack/images/elk.png)

1. Đầu tiên, log sẽ được đưa đến Logstash (Thông qua nhiều con đường, ví dụ server gửi request chứa log tới URL của Logstash, hoặc Beat đọc file log và gửi lên Logstash)

2. Logstash sẽ đọc những log này, thêm những thông tin như thời gian, IP, parse dữ liệu từ log ra sau đó ghi xuống database là Elasticsearch

3. Khi muốn xem log, người dùng vào URL của kibana. Kibana sẽ đọc thông tin log trong Elasticsearch, hiển thị lên giao diện cho người dùng query và xử lý 

# Tại sao phải dùng ELK stack?

Với các hệ thống hoặc ứng dụng nhỏ, ta không cần sử dụng ELK stack làm gì, cứ dùng thư viện ghi log sau đó ghi log ra file và đọc thôi

Tuy nhiên, với những hệ thống lớn hoặc nhiều người dùng, có nhiều service phân tán (microservice), có nhiều server chạy cùng lúc thì việc ghi log xuống file không còn hiệu quả nữa

Giả sử bạn có 10 con server chạy cùng lúc, bạn sẽ phải lục tung 10 con server này để đọc và tìm file log. Lúc này, người ta bắt đầu áp dụng centralized logging (ghi log tập trung) vào một chỗ

# Lợi ích khi sử dụng ELK

- Đọc log từ nhiều nguồn: Logstash có thể đọc được log từ rất nhiều nguồn, từ log file cho đến log database cho đến UDP hay REST request

- Dễ tích hợp: Dù bạn có dùng Nginx hay Apache, dùng MSSQL hay MongoDB, Logstash đều có thể đọc hiểu và xử lý log của bạn nên việc tích hợp rất dễ dàng

- Khả năng scale tốt: Logstash và Elasticsearch chạy trên nhiều node nên hệ thống ELK cực kì dễ scale. Khi có thêm service, thêm người dùng, muốn log nhiều hơn, bạn chỉ việc thêm node cho Logstash và Elasticsearch là xong

- Search và filter mạnh mẽ: Elasticsearch cho phép lưu trữ thông tin kiểu NoSQL, hỗ trợ luôn Full-Text Search nên việc query rất dễ dàng và mạnh mẽ.

- Mã nguồn mở: Lý do lớn nhất để sử dụng ELK có lẽ bởi vì đây là một tập hợp phần mềm mã nguồn mở và cộng đồng mạnh mẽ. Tuy nhiên ELK stack sẽ không còn là mã nguồn mở nữa kể từ phiên bản 7.11