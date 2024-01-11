# Highe Availability - Phần 1: Tổng quan về cluster

## Lời mở đầu

Cluster là kiến trúc nâng cao khả năng sẵn sàng cho các hệ thống dịch vụ. Hệ thống Cluster cho phép nhiều máy chủ chạy kết hợp, đồng bộ với nhau. Hệ thống Cluster nâng cao khả năng chịu lỗi của hệ thống, tăng cấp độ tin cậy, tăng tính đảm bảo, nâng cao khả năng mở rộng của hệ thống. Trong trường hợp có lỗi xảy ra, các dịch vụ bên trong Cluster sẽ tự động loại trừ lỗi, cố gắng khôi phục, duy trì tính ổn định, tính sẵn sàng của dịch vụ

## Tính chất quan trọng

- Cân bằng tải của cụm (Load Balancing): Các node bên trong cluster hoạt động song song, chia sẻ các tác vụ để nâng cao hệ thống

- Tính sẵn sàng cao (High availability): Các tài nguyên bên trong cluster luôn sẵn sàng xử lý yêu cầu, ngay cả khi có vấn đề xảy ra với các thành phần bên trong (hardware, software).

- Khả năng mở rộng (scalability): Khi tài nguyên có thể sử dụng của hệ thống tới giới hạn, ta có thể dễ dàng bổ sung thêm tài nguyên vào cluster bằng các bổ sung thêm các node.

- Độ tin cậy (reliability): Hệ thống Cluster giảm thiểu tần số lỗi có thể xảy ra, giảm thiểu các vấn đề dẫn tới ngừng hoạt động của hệ thống.

## Các thuật ngữ quan trọng 

- `Cluster`: Nhóm các server dành riêng để giải quyết 1 vấn đề, có khả năng kết nối, sản sẻ các tác vụ.

- `Node`: Server thuộc Cluster

- `Failover`: Khi 1 hoặc nhiều node trong Cluster xảy ra vấn đề, các tài nguyên (resource) tự động được chuyển tới các node sẵn sàng phục vụ

- `Failback`: Khi node lỗi phục hồi, sẵn sàng phục vụ, Cluster tự động trả lại tài nguyên cho node

- `Fault-tolerant cluster`: Để cập đến khả năng chịu lỗi của hệ thống trên các thành phần, cho phép dịch vụ hoạt động ngay cả khi một vài thành phần gặp sự cố

- `Heartbeat`: Tín hiệu xuất phát từ các node trong cụm với mục đích xác minh chúng còn sống và đang hoạt động. Nếu hearbeat tại một node ngừng hoạt động, cluster sẽ đánh dấu thành phần đó gặp sự cố 

- `Interconnect`: Kết nối giữa các node, thường là thông tin về trạng thái, heartbeat, dữ liệu chia sẻ 

- `Primary server, secondary server`: Trong cluster dạng `Active/Passive`, node đang đáp ứng giải quyết mọi yêu cầu gọi là Primary server, Node đang chờ hay dự phòng cho node Primary server gọi là secondary server

- `Quorum`: Trong cluster chứa nhiều tài nguyên nên dễ xảy ra hiện tượng phân mảnh (Tức là một cluster lớn bị tách ra thành nhiều cluster nhỏ). Điều này sẽ dẫn đến sự mất đồng bộ giữa các tài nguyên, ảnh hưởng đến sự toàn vẹn của hệ thống. Quorum được thiết kế để ngăn chặn hiện tượng phân mảnh

- `Resource`: Tài nguyên của cụm, cũng có thể hiểu là tài nguyên mà dịch vụ cung cấp

- `STONITH/ Fencing`: STONITH là viết tắt của cụm từ `Shoot Other Node In the Head`, đây là kỹ thuật dành cho fencing. Fencing là kỹ thuật cô lập tài nguyên cho từng node trong Cluster. Mục tiêu của STONITH là tắt hoặc khởi động lại node trong trường hợp dịch vụ không thể khôi phục

## Chế độ hoạt động

**Active - Active:** 

Active active cluster được tạo ra từ ít nhất 2 node, cả 2 node chạy đồng thời xử lý cùng 1 loại dịch vụ. Mục đích chính của Active Active Cluster là tối ưu hóa cho hoạt động cân bằng tải (Load Balancing). Hoạt động cân bằng tải (Load Balancing) sẽ phân phối tải, các tác vụ hệ thống tới tất cả các node bên trong cluster, tránh tình trạng các node xử lý các tác vụ không cân bằng dẫn tới tình trạng quá tải. Bên cạnh đó, Active active Cluster nâng cao thông lượng (throughput) và thời gian phản hồi

Khuyến cáo cho chế độ Active Active Cluster là các node trong cụm cần được giống nhau tránh tình trạng phân mảnh cụm 

![](/ha/images/activeactive.png)

**Active - Passive:**

Giống cấu hình Active - Active, Active - Passive Cluster cần ít nhất 2 node, tuy nhiên không phải tất cả các node đều sẵn sàng xử lý yêu cầu

VD: Nếu có 2 node thì 1 node sẽ chạy ở chế độ Active, node còn lại sẽ chạy ở chế độ passive hoặc stanby

Passive Node sẽ hoạt động như 1 bản backup của Active Node. Trong trường hợp Active Node xảy ra vấn đề, Passive Node sẽ chuyển trạng thái thành active, tiếp quản xử lý các yêu cầu 

![](/ha/images/activepassive.png)

