# Giới thiệu

Zabbix Agent là một phần mềm được cài đặt và chạy trên máy khách (clients) để thu thập dữ liệu từ hệ thống và gửi đến Zabbix Server hoặc các máy proxy để giám sát. Nó là một phần quan trọng trong hệ thống Zabbix Monitoring

### Cách thức hoạt động của Zabbix Agent

Zabbix Agent: Có thể thực hiện cả kiểm tra thụ động (polling) và kiểm tra chủ động (trapping). Việc kiểm tra có thể được thực hiện theo khoảng thời gian hoặc dựa trên lịch trình có thời gian cụ thể. Đây chính là sự khác biệt giữa kiểm tra thụ động và chủ động

- Kiểm tra thụ động (Polling): Zabbix Server sẽ gửi yêu cầu cho Zabbix Agent. Zabbix Agent sẽ xử lý yêu cầu và trả về cho Zabbix Server

- Kiểm tra chủ động (Trapping): Với loại này thì yêu cầu xử lý sẽ phức tạp hơn. Zabbix Agent sẽ phải truy xuất danh sách các hạng mục cần xử lý để xử lý độc lập. Sau đó, sẽ trả kết quả định kỳ về Zabbix Server

Hình ảnh dưới đây mô tả chi tiết Zabbix Agent để ta có thể hình dung các hoạt động kiểm tra thụ động và chủ động

![](/zabbix/images/zabbix_agent.png)

# Cài đặt Zabbix Agent trên Ubuntu 20.04

Ta có thể tham khảo tài liệu sau từ nhà phát triển Zabbix:

https://www.zabbix.com/download?zabbix=5.0&os_distribution=ubuntu&os_version=20.04&components=agent&db=&ws=

Truy cập vào server cần giám sát (Ubuntu 20.04)

1. Download Package từ Repo của Zabbix:

```sh
wget https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+focal_all.deb
```

Cài đặt gói đã tải xuống bằng `dpkg`

```sh
dpkg -i zabbix-release_5.0-1+focal_all.deb
apt update
```

2. Cài đặt Zabbix-agent

```sh
apt install zabbix-agent
```

3. Chỉnh sửa cấu hình

Mở file `/etc/zabbix/zabbix_agentd.conf` và chỉnh sửa cấu hình 

```sh
Server=35.221.52.191			# Địa chỉ IP hoặc hostname của Zabbix server
ServerActive=35.221.52.191		# Địa chỉ IP hoặc hostname của Zabbix server
Hostname=gitlab.monest.sbs		# Địa chỉ IP hoặc hostname của Zabbix agent
```

4. Khởi động lại Zabbix-agent

Sau khi chỉnh sửa cấu hình ta cần khởi động lại Zabbix-agent để apply cấu hình mới nhất đồng thời cho phép Zabbix-agent khởi động cùng hệ thống

```sh
systemctl restart zabbix-agent
systemctl enable zabbix-agent
```