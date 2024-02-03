# Mô hình TCP/IP

TCP/IP là viết tắt của cụm từ Transmission Control Protocol/Internet Protocol, là một tập hợp các giao thức (protocol) trao đổi thông tin được sử dụng để truyền tải và kết nối các thiết bị trong mạng Internet. Cụ thể hơn, TCP/IP chỉ rõ cho chúng ta cách thức đóng gói thông tin (còn được gọi là gói tin), được gửi và nhận bởi các máy tính có kết nối với nhau 

![](/images/tcp_ip.png)

Mô hình TCP/IP tiêu chuẩn gồm 4 tầng được chồng lên nhau là:

- Tầng 1: Tầng vật lý

- Tầng 2: Tầng mạng 

- Tầng 3: Tầng giao vận

- Tầng 4: Tầng ứng dụng

# Mô hình phần tầng trong TCP/IP

**Tầng ứng dụng (Application)**

- Nó cung cấp giao tiếp đến người dùng 

- Nó cung cấp các ứng dụng cho phép người dùng trao đổi dữ liệu ứng dụng thông qua các dịch vụ mạng khác nhau (như duyệt web, chat, gửi mail...)

- Dữ liệu khi đến đây sẽ được định dạng theo kiểu byte nối byte, cùng với đó là các thông tin định tuyến giúp xác định đường đi đúng của một gói tin

**Một số giao thức trao đổi dữ liệu**

- FTP (File Transfer Protocol): Giao thức chạy trên nền TCP cho phép truyền các file ASCII hoặc nhị phân theo 2 chiều

- TFTP (Trival File Transfer Protocol): Giao thức truyền file chạy trên nền UDP

- SMTP (Simple Mail Transfer Protocol): Giao thức dùng để phân phối thư điện tử

- Telnet: Cho phép truy cập từ xa để cấu hình thiết bị 

- SNMP (Simple Network Managerment Protocol): Là ứng dụng chạy trên nền UDP, cho phép quản lý và giám sát các thiết bị mạng từ xa

- Domain Name System (DNS): Là giao thức phân giải tên miền, đước sử dụng trong hỗ trợ truy nhập Internet

**Tầng giao vận (Transport)**

- Chịu trách nhiệm duy trì liên lạc đầu cuối trên toàn mạng

- Tầng này có 2 giao thức chính là TCP (Transmission Control Protocol) và UDP (User Datagram Protocol)

	+ TCP sẽ đảm bảo chất lượng truyền gửi gói tin, nhưng tốn khá nhiều thời gian để kiểm tra đầy đủ thông tin từ thứ tự dữ liệu cho đến việc kiểm soát vấn đề tắc nghẽn lưu lượng dữ liệu

	+ Trái với TCP, UDP có thấy tốc độ truyền tải nhanh hơn nhưng lại không đảm bảo được chất lượng dữ liệu được gửi đi (tức là nó không quan tâm dữ liệu có đến được đích hay không).

**Tầng mạng (Internet)**

- Xử lý quá trình truyền gói tin trên mạng 

- Định tuyến: Tìm đường qua các nút trung gian để gửi từ nguồn tới đích

- Chuyển tiếp: Chuyển tiếp gói tin từ cổng nguồn tới cổng đích theo tuyến đường

- Định địa chỉ: Định danh cho các nút mạng

- Đóng gói dữ liệu: Nhận dữ liệu từ giao thức ở trên, chèn thêm phần Header chứa thông tin của tầng mạng và tiếp tục được chuyển đến tầng tiếp theo

- Đảm bảo chất lượng dịch vụ (QoS): Đảm bảo các thông số phù hợp của đường truyền theo từng dịch vụ 

> QoS (Quality of Service) là tập hợp các kỹ thuật cho phép cấp phát các tài nguyên một cách thích hợp cho các loại dữ liệu khác nhau, từ đó có thể đảm bảo chất lượng dịch vụ mạng cho các loại dữ liệu này

**Tầng vật lý**

- Nó là sự kết hợp của tầng Data Link và Physical trong mô hình OSI

- Là tầng thấp nhất trong mô hình TCP/IP

- Chịu trách nhiệm truyền dữ liệu giữa các thiết bị trong cùng một mạng. Tại đây, các gói dữ liệu được đóng vào khung (Frame) và được định tuyến đi đến đích được chỉ định ban đầu

# Cách thức hoạt động của TCP/IP

![](/images/tcp_ip1.png)

Khi truyền dữ liệu, quá trình tiến hành từ tầng trên xuống dưới, qua mỗi tầng dữ liệu được thêm vào thông tin điều khiển gọi là Header. Khi nhận dữ liệu thì quá trình xảy ra ngược lại, dữ liệu được truyền từ tầng dưới lên và qua mỗi tầng thì phần header tương ứng sẽ được lấy đi và khi đến tầng trên cùng thì dữ liệu không còn header nữa

- Ở đây, IP có vai trò quan trọng, nó cho phép các gói tin được gửi đến đích đã định sẵn, bằng cách thêm các thông tin dẫn đường (chính là Header) vào các gói tin để các gói tin được đến đúng đích sẵn ban đầu

- Giao thức TCP đóng vai trò kiểm tra và đảm bảo sự an toàn cho mỗi gói tin khi đi qua mỗi trạm. Trong quá trình này, nếu giao thức TCP nhận thấy gói tin bị lỗi, một tín hiệu sẽ được truyền đi va yêu cầu hệ thống gửi lại một gói tin khác

![](/images/tcp_ip2.png)

Hình trên là cấu trúc dữ liệu qua các tầng. Trong hình ta sẽ thấy ở mỗi tầng khac nhau dữ liệu được truyền vào là khác nhau 

- Tầng ứng dụng: Dữ liệu là các luồng được gọi là Stream 

- Tầng giao vận: Đơn vị dữ liệu mà TCP gửi xuống gọi là TCP segment 

- Tầng mạng: Dữ liệu mà IP gửi xuống tầng dưới gọi là IP Datagram 

- Tầng liên kết: Dữ liệu được truyền đi gọi là frame

# Ưu điểm của mô hình TCP/IP 

- Không chịu sự kiểm soát của bất kỳ tổ chức nào => chúng ta có thể tự do trong việc sử dụng

- Có khả năng tương thích cao với tất cả các hệ điều hành, phần cứng máy tính và mạng => hoạt động hiệu quả với nhiều hệ thống khác nhau

- Có khả năng mở rộng cao, có thể định tuyến => có thể xác định đường dẫn hiệu quả nhất

