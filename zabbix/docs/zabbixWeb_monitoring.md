# Web monitoring 

## Tổng quan

Web scenarios trong Zabbix là một tính năng cho phép kiểm tra và giám sát các trang web hoặc ứng dụng web bằng cách mô phỏng các hoạt động của người dùng thực tế. Bằng cách tạo và cấu hình các Web Scenarios, ta có thể kiểm tra tính khả dụng, thời gian phản hồi và nội dung của các trang web hoặc ứng dụng web đã cấu hình

> Để thực hiện giám sát máy chủ web, máy chủ Zabbix ban đầu phải được cấu hình với sự hỗ trợ curl

Để active web monitoring, ta cần định nghĩa ra các web scenarios. Một Web scenarios bao gồm một hoặc một số yêu cầu HTTP hoặc các "steps". Các step này được máy chủ Zabbix thực hiện định kỳ theo thứ tự được xác định trước. Nếu máy chủ được giám sát bởi proxy thì các bước sẽ được proxy thực hiện

Các Web scenarios được gắn vào Server/Templates như các Items, Triggers. Điều này có nghĩa là các Web scenarios cũng có thể được tạo trên các Templates và sau đó áp dụng Templates này cho nhiều Host

Thông tin sau được thu thập trong một Web scenarios:

- Tốc độ tải xuống trung bình mỗi giây cho tất cả các Step của toàn bộ scenarios

- Số bước không thành công

- Thông báo lỗi cuối cùng

Thông tin sau được thu thập trong bất kỳ Step nào của Web scenarios

- Tốc độ tải xuống mỗi giây

- Thời gian đáp ứng

- Mã phản hồi (response code)

## Config a Web Scenario

Để cấu hình một Web scenarios

- Đi tới `Data collection` -> Hosts (or Templates)

- Click `Web` ở hàng Host/Template

- Nhấp vào `Create web scenario` ở bên phải hoặc nhấn vào scenario hiện có để chính sửa kịch bản hiện có

- Nhập các tham số của kịch bản vào biểu mẫu

Tạo Scenario cho phép bạn định cấu hình các tham số chung của kịch bản web

![](/zabbix/images/scenario.png)

Tất cả các trường Input có dấu hoa thị màu đỏ là các trường buộc phải có Input

Thông số

|Parameter|Description|
|---|---|
|Name|Tên của Scenarios. Có hỗ trợ User Macros, khi sử dụng macro, các macro này sẽ không được giải quyết trong Web monitoring item|
|Update interval|Tần suất Scenario sẽ được thực hiện, có hỗ trợ User Macros|
|Attempts|Số lần thực hiện các Scenario steps, Có thể chỉ định tối đa 10 lần thử, giá trị mặc định là 1. Lưu ý: Zabbix sẽ không lặp lại một bước do mã phản hồi sai hoặc chuỗi bắt buộc không khớp|
|Agent|Chọn một client agent, User macros có thể được sử dụng trong trường này|
|HTTP proxy|Ta có thể sử dụng proxy HTTP để sử dụng bằng cách sử dụng định dạng [protocol://][username[:password]@]proxy.example.com[:port], User macros có thể được sử dụng trong trường này|
|Variables|Các biến có thể được sử dụng trong các Scenario steps (URL, post variables). 
Chúng ta có các định dạng sau: {macro1}=value1, {macro2}=value2, {macro3}=regex:<regular expression>. Ví dụ: For example: {username}=Alexei, {password}=kj3h5kJ34bd, {hostid}=regex:hostid is ([0-9]+)|
|Headers|Tiêu đề|