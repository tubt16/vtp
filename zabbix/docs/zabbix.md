# Tổng quan về Zabbix

Zabbix là một công cụ mã nguồn mở giải quyết cho ta các vấn đề về giám sát. Zabbix là phần mềm sử dụng các tham số của một mạng, tình trạng và tính toàn vẹn của Server cũng như các thiết bị mạng

Zabbix sử dụng một cơ chế thông báo linh hoạt cho phép người dùng cấu hình email hoặc sms để cảnh báo dựa trên sự kiện được thiết lập sẵn. Ngoài ra Zabbix cung cấp báo cáo và dữ liệu chính xác dựa trên cơ sở dữ liệu

1. Ưu điểm của Zabbix

- Giám sát cả Server và thiết bị mạng

- Dễ dàng thao tác và cấu hình

- Hỗ trợ máy chủ Linux, Solaris, FreeBSD …

- Đáng tin cậy trong việc chứng thực người dùng

- Linh hoạt trong việc phân quyền người dùng

- Mã nguồn mở

2. Các thành phần của Zabbix

**Zabbix Server:** Đây là thành phần trung tâm của phần mềm Zabbix. Zabbix server có thể kiểm tra các máy chủ từ xa thông qua các báo cáo của Agent gửi về cho Zabbix Server và từ đó nó sẽ lưu trữ tất cả các cấu hình cũng như là các số liệu thống kê

**Database storage:** Tất cả thông tin cấu hình cũng như dữ liệu được Zabbix thu thập được lưu trữ trong cơ sở dữ liệu

**Zabbix Proxy:** Là phần tùy chọn của Zabbix. Nó có nhiệm vụ thu nhận dữ liệu, lưu trong bộ nhớ đệm và chuyển đến Zabbix Server

Zabbix Proxy là một giải pháp lý tưởng cho việc giám sát tập trung các máy chủ từ xa

Zabbix Proxy cũng được sử dụng để phân phối tải của một Zabbix Server

**Zabbix Agent:** Để giám sát chủ động các thiết bị cục bộ và các ứng dụng (ổ cứng, bộ nhớ ...) trên hệ thống mạng. Zabbix Agent sẽ được cài lên trên Server và từ đó Agent sẽ thu thập thông tin hoạt động từ Server mà nó đang chạy và báo cáo dữ liệu này đến Zabbix Server để xử lý

**Web interface:** Web interface được cung cấp để dễ dàng truy cập Zabbix từ mọi nơi và mọi nền tảng. Web interface thường chạy trên cùng một máy vật lý với Zabbix Server