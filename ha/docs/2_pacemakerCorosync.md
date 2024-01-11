# High Availability - Phần 2: Tổng quan về Pacemaker Corosync

## Tổng quan

`Pacemaker` Là trình quản lý tài nguyên trong cluster

Kiến trúc triển khai bởi Pacemaker cho phép tùy biến, hỗ trợ tối đa để các tài nguyên (resource) thuộc cluster luôn sẵn sàng. Đồng thời pacemaker có khả năng phát hiện phục hồi các tài nguyên, các node đang xảy ra sự cố thông qua các engine hỗ trợ (Corosync, Heartbeat), cho phép tùy biến tùy theo các kiến trúc khác nhau

Các tính năng chính của Pacemaker: 

- Tự động phát hiện, khôi phục các node, các tài nguyên dịch vụ trên node 

- Không yêu cầu chia sẻ không gian lưu trữ (shared storage)

- Tất cả tài nguyên có thể quản lý bằng script đều có thể quản lý bằng Pacemaker 

- Hỗ trợ kỹ thuật `fencing`, kỹ thuật cô lập tài nguyên trên mỗi node 

- Hỗ trợ các cluster từ nhỏ tới lớn

- Hỗ trợ kỹ thuật `Resource-driven cluster` - Kỹ thuật phân cấp, nhóm tài nguyên để quản lý độc lập

- Hỗ trợ kỹ thuật `Quorate Clusters` - Kỹ thuật tính điểm trên các node thuộc cluster, ý tưởng của kỹ thuật là khi cụm lớn bị phân mảnh thành 2 phần, cluster sẽ đánh giá so sánh số điểm của 2 cụm để quyết định cụm nào sẽ tiếp tục chạy, cụm nào sẽ bị đóng băng hoặc tắt hẳn

- Hỗ trợ các thiết bị dự phòng 

- Tự động nhân bản cấu hình tới các node thuộc cluster

- Có khả năng nhận thức sự thay đổi trên tài nguyên 

- Hỗ trợ các kiểu dịch vụ nâng cao:

	+ Nhân bản (Clone): Dịch vụ được nhân bản tới nhiều node để tăng tính sẵn sàng

	+ Đa trang thái (Multi-state): Các dịch vụ có nhiều trạng thái (Master/Slave, Primary/Secondary)

- Quản trị cluster qua các công cụ hỗ trợ

## Kiến trúc Pacemaker

Theo kiến trúc Pacemaker, Cluster được tạo từ 3 thành phần:

- Các thành phần cluster không thể nhận biết (Non-cluster aware components): Các thành phần được script hóa để có thể tắt bật, giám sát

- Quản lý tài nguyên (Resource management): Pacemaker cung cấp trung tâm giám sát, phản ứng với các event xảy ra trong cluster. Các event có thể là các node bị loại bỏ, các node tham gia vào cluster, các hoạt động bảo trì... Pacemaker sẽ nhận thức, tự động đánh giá trạng thái lý tưởng cho cluster ra chỉ thị cho cluster trở lại trạng thái lý tưởng (tự động di chuyển tài nguyên, loại bỏ thành phần lỗi bằng cách tắt dịch vụ hoặc tắt hẳn node)

- Low-level infrastructure: Các project như Corosync, CMAN, Heartbeat cung cấp các tin nhắn tin cậy về thông tin, về tài nguyên node, quorum của cụm 

Kết hợp Corosync + Pacemaker cho phép cluster quản trị các cluster Filesystem tiêu chuẩn. Tính năng này được phát triển từ tiêu chuẩn `distributed lock manager` trên các hệ thống Cluster Filesystem mã nguồn mở, từ đó cho phép corosync thu thập event về tình trạng các node thuộc cluster filesystem và cho phép Pacemaker ra lệnh cô lập dịch vụ tại các node

![](/ha/images/pacemaker.png)

## Các thành phần nội tại

Pacemaker chia thành 5 phần chính:

- Cluster Infomation Base (CIB): CIB sử dụng XML để thể hiện cấu hình cluster cũng như trạng thái hiện tại của các tài nguyên bên trong cluster. Nội dung của CIB tự đồng bộ tới tất cả các node trên toàn cluster, đồng thời sử dụng PEngine để đánh giá trạng thái lý tưởng của Cluster và cách để đạt được trạng thái lý tưởng

- Cluster Resource Management daemon (CRMd): Các thao tác tới tài nguyên thuộc Cluster được định tuyến thông qua tiến trình này. Tiến trình cho phép truy vấn thông tin, di chuyển, khởi tạo, thay đổi trạng thái khi cần

- Local Resource Management daemon (LRMd): Mỗi node thuộc cluster chạy tiến trình `local resource manager daemon` (LRMd), tiến trình này như giao diện giữa CRMd với các tài nguyên nội tại của node. Tiến trình LRMd sẽ chuyển chỉ thị từ CRMd tới các thành phần tài nguyên nó quản lý

- Policy engine (PEngine): Chịu trách nhiệm tính toán trạng thái lý tưởng của cụm, ra chỉ thị, kịch bản cho CRMd để hiện thực hóa trạng thái mong muón

- STONITH: Giải pháp cho các node không phản hồi, không nhận chỉ thị mềm CRMd sẽ chỉ thị cho STONITH tắt nóng, hoặc khởi động lại trực tiếp thông qua phần cứng (IPMI, IDRAC, ILO ...)

