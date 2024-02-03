# Mô hình OSI là gì?

Mô hình kết nối các hệ thống mở (OSI) là một mô hình tham chiếu dùng để mô tả cách các hệ thống mạng tương tác với nhau. Mô hình này được phát triển bởi ISO. Mô hình OSI chia quá trình truyền thông mạng thành 7 lớp, mỗi lớp có chức năng riêng biệt và các lớp này tương tác với nhau để thực hiện truyền thông dữ liệu

Dưới đây là danh sách các lớp trong mô hình OSI:

1. Physical Layer (Lớp vật lý):

- Lớp Vật lý xác định các yếu tố cơ bản của việc truyền dẫn dữ liệu như điện áp, tần số, kết nối vật lý, các đặc điểm về cáp, sóng vô tuyến hoặc quang 

- Nhiệm vụ chính của lớp này là chuyển đổi các bit thành các tín hiệu vật lý để truyền qua các phương tiện truyền dẫn và đảm bảo truyền dẫn đúng các bit từ nguồn tới đích

2. Data Link Layer (Lớp liên kết dữ liệu):

- Lớp liên kết dữ liệu quản lý việc truyền dữ liệu giữa các thiết bị trên cùng một mạng vật lý 

- Nhiệm vụ chính của lớp này là đóng gói các bit dữ liệu thành các khung (frames) và thực hiện kiểm tra lỗi để đảm bảo truyền dữ liệu một cách tin cậy 

- Lớp này cũng thực hiện các chức năng như điều khiển truy cập vào phương tiện truyền dẫn, địa chỉ hóa (MAC addressing), phát sinh và sửa lỗi truyền thông

3. Network Layer (Lớp Mạng)

- Lớp Mạng quản lý việc định tuyến (routing) các gói tin từ nguồn tới đích qua một mạng lớn

- Lớp này sử dụng các giao thức định tuyến như IP để xác định đường đi tối ưu cho dữ liệu và kiểm soát luồng giao thông

- Nhiệm vụ chính của lớp này là chia nhỏ dữ liệu thành các gói tin, gắn địa chỉ IP và xác định địa chỉ đích

4. Transport Layer (Lớp vận chuyển)

- Lớp Vận chuyển đảm bảo truyền dẫn đáng tin cậy giữa các tiến tình ứng dụng trên các máy tính khác nhau

- Nhiệm vụ của lớp này là chia nhỏ dữ liệu thành các segments, thêm các thông tin điều khiền và nhận dạng cho mỗi đoạn

- Lớp này đảm bảo dữ liệu được gửi và nhận theo đúng thứ tự và có khả năng phục hồi lỗi trong quá trình truyền thông

5. Session Layer (Lớp Phiên):

- Lớp Phiên thiết lập, duy trì và đóng các phiên truyền thông giữa các ứng dụng trên các máy tính khác nhau 

- Lớp này quản lý việc đồng bộ hóa và phục hồi của các phiên truyền thông

- Nhiệm vụ chính của lớp này là điều khiển việc thiết lập, duy trì và chấm dứt phiên truyền thông

6. Presentation Layer (Lớp trình diễn)

- Lớp trình diễn đảm bảo sự tương thích giữa các định dạng dữ liệu khác nhau trên các hệ thống khác nhau

- Lớp này mã hóa, nén và định dạng dữ liệu để truyền và giải mã, giải nén và định dạng dữ liệu khi nhận

- Nhiệm vụ chính của lớp này là đảm bảo các ứng dụng trên các hệ thống khác nhau có thể hiểu và xử lý dữ liệu một cách chính xác 

7. Application Layer (Lớp ứng dụng)

- Lớp Ứng dụng cung cấp các dịch vụ trực tiếp cho người dùng cuối

- Lớp này chứa các giao thức ứng dụng như HTTP, FTP, SMTP và nhiều giao thức khác 

- Nhiệm vụ chính của lớp này là cung cấp các giao diện và dịch vụ để người dùng có thể truy cập và sử dụng các ứng dụng mạng như truyền tệp, gửi email duyệt web...

> Mỗi lớp trong mô hình OSI có chức năng riêng biệt nhưng cũng tương tác với nhau để thực hiện quá trình truyền thông mạng. Các lớp cung cấp một cấu trúc tổ chức cho việc phân chia và quản lý các nhiệm vụ và chức năng trong một máy tính

# Tại sao mô hình OSI lại quan trọng ?

Các lớp của mô hình OSI tóm lược mọi loại hình giao tiếp mạng trên cả thành phần phần mềm và phần cứng. Mô hình này được thiết kế để cho phép 2 hệ thống độc lập giao tiếp với nhau thông qua các giao diện hoặc giao thức được chuẩn hóa dựa trên lớp hoạt động hiện tại

Tiếp theo là những lợi ích của mô hình OSI

### Hiểu biết chung về những hệ thống phức tạp 

Các kỹ sư có thể sử dụng mô hình OSI 