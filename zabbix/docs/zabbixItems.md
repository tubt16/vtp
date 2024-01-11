# Items

Các `Items` được sử dụng để thu thập dữ liệu như CPU, Ram, disk, network... Sau khi đã thêm Host, bạn cần phải thêm các `Items` để thu thập dữ liệu thực tế từ Host đã thêm đó. Một cách để thêm nhanh nhiều `Items` là đính kèm một trong các `Templates` được xác định trước vào Host

Tuy nhiên, để tối ưu hóa hiệu suất hệ thống, bạn có thể cần tinh chỉnh các `Templates` để có nhiều `Items` và theo dõi thường xuyên nếu cần

Để chỉ định loại dữ liệu cần thu thập từ máy chủ, ta sử dụng `Item key`. 

**Ví dụ:**

- `Item key` có tên `system.cpu.load` sẽ thu thập dữ liệu tải CPU của máy chủ

- `Item key` có tên `net.if.in` sẽ thu thập thông tin lưu lượng truy cập đến máy chủ

Các tham số bổ sung có thể được chỉ định trong dấu ngoặc vuông sau `Item key`

**Ví dụ:**

- `system.cpu.load[avg5]` sẽ trả về mức tải trung bình của CPU trong vòng 5 phút gần nhất

- `net.if.in[eth0]` sẽ hiển thị lưu lượng truy cập đến interface "eth0"

# Tạo Item

Thực hiện tạo mới một `Item` với `Item key` là `net.tcp.listen[80]` để kiểm tra port 80 của server còn hoạt động hay không

Để tạo mới một `Item` trên Zabbix frontend ta làm như sau

- Đi đến `Configuration` -> `Hosts`

- Click vào `Item` thuộc Host cần tạo

![](/zabbix/images/create_item.png)

- Nhấn vào `Create item` ở bên góc phải màn hình

![](/zabbix/images/create_item1.png)

![](/zabbix/images/create_item2.png)

- Nhập thông số vào form và click `Add`

Như vậy là chúng ta đã tạo xong `Item` check port 80 của Gitlab server

Để đặt cảnh báo ta cần phải tạo `Triggers` (Sẽ giới thiệu kỹ hơn trong phần sau)

Thực hiện tạo `Triggers` như sau:

- Đi tới `Configuration` -> `Hosts` click `Triggers`

![](/zabbix/images/create_triggers.png)

- Chọn `Create triggers` ở trên góc phải màn hình 

![](/zabbix/images/create_triggers1.png)

![](/zabbix/images/create_triggers2.png)

Đặt tên cho `Triggers`, chọn mức độ cho cảnh báo sau đó chọn `Select` tại tab `Expression`

![](/zabbix/images/create_triggers3.png)

Tìm đến `Item` vừa tạo và chọn `Item` đó rồi nhấn `Insert`

![](/zabbix/images/create_triggers4.png)

Sau khi `Insert` ta nhận được giá trị `Expression` như trên. Click `Add` để hoàn thành tạo `Triggers`

Sau khi tạo `Item` và `Triggers` xong ta thực hiện stop service Gitlab(Gitlab trong bài viết này chạy trên port 80) để kiểm tra xem Zabbix có hiện cảnh báo không

```sh
root@gitlab:/etc/zabbix# gitlab-ctl stop
ok: down: alertmanager: 1s, normally up
ok: down: gitaly: 1s, normally up
ok: down: gitlab-exporter: 1s, normally up
ok: down: gitlab-kas: 0s, normally up
ok: down: gitlab-workhorse: 0s, normally up
ok: down: logrotate: 0s, normally up
ok: down: nginx: 1s, normally up
ok: down: node-exporter: 0s, normally up
ok: down: postgres-exporter: 1s, normally up
ok: down: postgresql: 0s, normally up
ok: down: prometheus: 1s, normally up
ok: down: puma: 0s, normally up
ok: down: redis: 0s, normally up
ok: down: redis-exporter: 0s, normally up
ok: down: sidekiq: 0s, normally up
```

![](/zabbix/images/monitor_gitlab1.png)

Sau khi stop Gitlab Zabbix đã hiển thị cảnh báo, tiếp theo chúng ta sẽ start Gitlab để xem trạng thái của cảnh báo có chuyển từ `PROBLEM` về `RESOLVED` hay không

![](/zabbix/images/gitlab_resolved.png)

Như vậy trạng thái của cảnh báo đã chuyển về `RESOLVED` sau khi chúng ta start Gitlab, như vậy `Item` và `Triggers` ta vừa tạo đã hoạt động