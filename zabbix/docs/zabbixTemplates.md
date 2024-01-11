# Tổng quan

Templates là tập hợp các thực thể có thể áp dụng được cho nhiều máy chủ

Các thực thể có thể là:

- Items

- Triggers

- Graphs

- Applications

- Screens

- Low-level discovery rules

- Web scenarios

Trong thực tế, có nhiều máy chủ cài đặt những ứng dụng giống hệt nhau hoặc khá giống nhau nên đương nhiên tập hợp các thực thể (Items, Triggers, Graphs...) mà ta đã tạo cho một máy chủ có thể sẽ hữu ích cho NHIỀU máy chủ. Tất nhiên ta có thể sao chép từng thành phần trong các thực thể đó sang máy chủ mới nhưng việc đó sẽ gây tốn công sức. Thay vào đó, với các Template, ta có thể sao chép chúng vào một Template rồi áp dụng Template đó lên nhiều máy chủ nếu cần

Khi Template được liên kết với máy chủ, tất cả các thực thể (Items, Triggers ...) của Template sẽ được thêm vào máy chủ. Các Template được gán trực tiếp cho từng máy chủ riêng lẻ (chứ không phải cho một nhóm máy chủ)

Các Template thường được sử dụng để nhóm các thực thể cho các dịch vụ hoặc ứng dụng cụ thể như (Apache, MySQL, PostgreSQL, Postfix...) và sau đó áp dụng cho các máy chủ chạy các dịch vụ đó

Một lợi ích khác của việc sử dụng Template là khi cần phải thay đổi điều gì đó với tất cả các máy chủ. Thay đổi nội dung nào đó ở cấp độ Template một lần sẽ đồng thời thay đổi trên tất cả các máy chủ được liên kết

Do đó, việc sử dụng Template là một cách tuyệt vời để giảm tẳi khối lượng công việc và hợp lý hóa cấu hình Zabbix

# Template

Việc định cấu hình Template yêu cầu trước tiên phải xác định các thông số chung của Template đó, sau đó thêm các thực thể (Items, Triggers...) vào Template đó

**Tạo mới một Template**

![](/zabbix/images/temp.png)

Để tạo mới một template ta đi đến `Configuration` -> `Templates` chọn `Create template`

![](/zabbix/images/temp1.png)

Tại tab `Template` điền nội dung vào form như ảnh trên

Các trường trong form

|Parameter|Description|
|---|---|
|Template name|Tên của Template|
|Visible name|Tên này sẽ hiểu thị trong phần maps, etc ...|
|Group|Nhóm Host/template mà Template thuộc về|
|Description|Mô tả về Template|

Tab `Linked templates` cho phép liên kết một hoặc nhiều Template LỒNG NHAU với Template đang tạo này. Tất nhiên các thực thể (Items, Triggers...) sẽ được kế thừa từ các Template được liên kết

Để liên kết một Template mới, hãy bắt đầu nhập tên Template vào trường `Link new templates` hoặc chọn `Select`, danh sách các Template phù hợp sẽ xuất hiện. Các Template được chọn trong trường `Link new template` sẽ được liên kết với Template khi biểu Template cấu hình được lưu hoăc cập nhật

![](/zabbix/images/temp2.png)

Để hủy liên kết một Template, hãy sử dụng một trong hai tùy chọn trong `Linked templates block`

- `Unlink` - Hủy liên kết nhưng vẫn giữ nguyên các `Items`, `Triggers`, `Graphs`

- `Unlink and clear` - Hủy liên kết Template và xóa tất cả `Items`, `Triggers` và `Graphs`

Tab `Tags` cho phép thẻ cho Template. Tất cả các vấn đề của máy chủ được liên kết với Template này sẽ được gắn thẻ với các giá trị được nhập ở đây

![](/zabbix/images/temp3.png)

# Thêm Item, Triggers, Graphs vào Template

Để thêm các `Item` hiện có vào Template ta làm như sau

1. Đi tới `Configuration` -> Host (hoặc Template)

2. Chọn `Items`

![](/zabbix/images/temp4.png)

3. Chọn lấy một `Item` cần thêm vào Template và chọn `Copy` ở cuối màn hình

![](/zabbix/images/temp5.png)

4. Chuyển sang tab `Templates` và chọn `Template` cần thêm `Item` mới này

![](/zabbix/images/temp6.png)

![](/zabbix/images/temp7.png)

5. Nhấn `Copy` để thực hiện copy `Item` đã chọn sang `Template` đã chỉ định
