# Host

**Host là gì?**

Máy chủ Zabbix điển hình là các thiết bị bạn muốn giám sát (Máy chủ từ xa, máy trạm, thiết bị chuyển mạch...)

Tạo host là một trong những nhiệm vụ đầu tiên cần thực hiện để giám sát với Zabbix. Ví dụ: nếu muốn giám sát một số tham số trên máy chủ "X", trước tiên bạn phải tạo một host có tên là `Server X` và sau đó bạn sẽ thêm các giám sát vào nó

Các máy chủ được tổ chức thành các nhóm máy chủ

Ta tiến hành tạo và cấu hình máy chủ

### Thêm Host

Để định cấu hình máy chủ trong Zabbix frontend, ta làm như sau:

- Đi tới `Configuraion` -> `Hosts`

- Click vào `Create host` ở góc bên phải (hoặc click vào tên máy chủ để chỉnh sửa máy chủ hiện có)

![](/zabbix/images/zabbix_configHost.png)

- Nhập thông số của máy chủ theo mẫu

![](/zabbix/images/add_agent.png)

- Chuyển qua tab `Templates` -> `Link new templates` -> chọn `Select`

![](/zabbix/images/add_agent2.png)

- Tiếp theo click `Select` trong `Host group`

![](/zabbix/images/add_agent3.png)

- Tiếp theo chọn `Templates`

![](/zabbix/images/add_agent4.png)

- Chọn `Template OS Linux by Zabbix agent`

![](/zabbix/images/add_agent5.png)

- Click `Add` để hoàn tất

![](/zabbix/images/add_agent6.png)

Sau khi thêm thành công ta kiểm tra lại phần `Availability` 

![](/zabbix/images/add_agent7.png)

Phần `ZBX` đã chuyển sang màu xanh tức là ta đã thêm thành công

Quay lại phần `Monitoring` -> `Problems` để xem cảnh báo hiện tại của Server `gitlab.monest.sbs` vừa thêm

![](/zabbix/images/monitor_gitlab.png)
