# APM - Application performance monitoring 

Elastic APM (Application performance monitoring) là một hệ thống giám sát hiệu suất ứng dụng được xây dựng trên Elastic Stack. Nó cho phép bạn giám sát các dịch vụ và ứng dụng trong thời gian thực bằng cách thu thập thông tin hiệu suất chi tiết, thời gian phản hồi của các request gửi đến, truy vấn database, HTTP request ... Điều này giúp dễ dàng xác định và khắc phục các vấn đề về hiệu suất một cách nhanh chóng

# Component

Elastic APM gồm 4 thành phần:

- APM agent

- Elastic APM integration

- Elasticsearch

- Kibana

Có 2 cách để 4 thành phần này hoạt động cùng nhau:

**1. Các APM agent trên các máy chủ NGOÀI gửi dữ liệu đến APM integration được lưu trữ tập trung:**

![](/ELK_stack/images/APM1.png)

**2. Các APM agent và APM integration hoạt động trên các máy chủ bên NGOÀI và gửi dữ liệu thông qua Elastic Agent được lưu trữ tập trung**

![](/ELK_stack/images/APM2.png)

### APM agents

APM agent là thư viện mã nguồn mở, bạn cần cài đặt chúng lên máy chủ của mình giống như cài một thư viện. APM agent sẽ thu thập dữ liệu về hiệu suất cũng như lỗi nó tìm được trên máy chủ của bạn trong thời gian nó chạy. Dữ liệu này được lưu vào bộ đệm trong một thời gian ngắn và sau đó APM agent sẽ gửi dữ liệu này tới APM server

### Elastic APM integration

APM intergration nhận dữ liệu từ các APM agent, xác thực và xử lý dữ liệu đó, sau đó chuyển đổi dữ liệu thành Elasticsearch documents

### Elasticsearch

Elasticsearch là một công cụ phân tích và tìm kiếm log mã nguồn mở có khả năng mở rộng cao. Nó cho phép bạn lưu trữ, tìm kiếm và phân tích khối lượng lớn dữ liệu một cách nhanh chóng và gần như theo thời gian thực. Elasticsearch được sử dụng để lưu trữ các số liệu hiệu suất APM

### Kibana APM app

Kibana là một nền tảng được thiết kế để hoạt động với Elasticsearch, Kibana cung cấp giao diện trực quan dễ tiếp cận, sử dụng để tìm kiếm, xem và tương tác với dữ liệu được lưu trữ trong Elasticsearch

# Install and run APM server

Bước 1: Download và giải nén file cài đặt APM server

```sh
curl -L -O https://artifacts.elastic.co/downloads/apm-server/apm-server-6.8.23-x86_64.rpm
sudo rpm -vi apm-server-6.8.23-x86_64.rpm
```

Bước 2: Chỉnh sửa config

Nếu bạn đang sử dụng phiên abrn bảo mật X-Pack của Elastic, bạn phải chỉ định thông tin xác thực trong cấu hình `apm-server.yml` (Nếu không sử dụng thì có thể bỏ qua)

```sh
output.elasticsearch:
    hosts: ["<es_url>"]
    username: <username>
    password: <password>
```

Bước 3: Start and Enable APM Server

```sh
systemctl start apm-server
systemctl enable apm-server 
```

Bước 4: Kiểm tra trạng thái của APM Server

```sh
[root@elk apm-server]# systemctl status apm-server 
● apm-server.service - Elastic APM Server
   Loaded: loaded (/usr/lib/systemd/system/apm-server.service; enabled; vendor preset: disabled)
   Active: active (running) since Sat 2023-11-11 04:22:52 UTC; 18min ago
     Docs: https://www.elastic.co/solutions/apm
 Main PID: 19261 (apm-server)
   CGroup: /system.slice/apm-server.service
           └─19261 /usr/share/apm-server/bin/apm-server -c /etc/apm-server/apm-server.yml -path.home /usr/share/apm-server -path.config /etc/a...
Nov 11 04:22:52 elk systemd[1]: Started Elastic APM Server.
```

# Install APM Agents

Trong bài viết này sẽ sử dụng Java Agent

Bước 1: Download APM Agent (Java Agent)

```sh
curl -o 'elastic-apm-agent.jar' -L 'https://oss.sonatype.org/service/local/artifact/maven/redirect?r=releases&g=co.elastic.apm&a=elastic-apm-agent&v=LATEST'
```

Bước 2: Khởi động ứng dụng với cờ `javaagent`

Thêm cờ `-javaagent` và định cấu hình agent

```sh
java -javaagent:/mnt/elastic-apm-agent.jar \
     -Delastic.apm.service_name=my-application \
     -Delastic.apm.server_url=http://localhost:8200 \
     -Delastic.apm.secret_token= \
     -Delastic.apm.application_packages=zabbix \
     -jar my-application.jar
```

