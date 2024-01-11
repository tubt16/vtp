# Install ELK stack on CentOS 7

# Điều kiện tiên quyết

Một máy chủ CentOS 7 với

- 4 GB RAM

- 2 CPU

# Cài đặt

Bước 1: Cài đặt Java 8

```sh
yum install java -y
```

Kiểm tra lại 

```sh
[root@elk conf.d]# java -version
openjdk version "1.8.0_382"
OpenJDK Runtime Environment (build 1.8.0_382-b05)
OpenJDK 64-Bit Server VM (build 25.382-b05, mixed mode)
```

Bước 2: Cài đặt Nginx

Thêm Epel repository

```sh
yum install epel-release -y
```

Cài đặt nginx và khởi động service

```sh
yum install nginx -y

systemctl start nginx
systemctl enable nginx
```

Bước 3: Cài đặt và cấu hình Elasticsearch

Các thành phần ELK thông qua trình quản lý gói YUM theo mặc định, nhưng bạn hoàn toàn có thể cài chúng bằng yum bằng cách add Elastic package repository

Đầu tiên ta cần import GPG-KEY của Elasticsearch

```sh
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

Tiếp theo, thêm Elastic repository 

```sh
cat <<EOF>> /etc/yum.repos.d/elasticsearch.repo
[elasticsearch-6.x]
name=Elasticsearch repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
EOF
```

Với repo đã được thêm vào, bây giờ ta có thể cài đặt ELK stack, theo tài liệu chính thức, ta nên cài đặt Elasticsearch trước các thành phần khác

Cài đặt Elasticsearch bằng lệnh sau:

```sh
yum install elasticsearch -y
```

Sau khi Elasticsearch cài đặt xong, hãy mở tệp cấu hình của nó và chỉnh sửa như sau

```sh
vi /etc/elasticsearch/elasticsearch.yml
```

Elasticsearch lắng nghe lưu lượng truy cập từ mọi nơi trên port 9200. Bạn sẽ cần phải hạn chế quyền truy cập từ bên ngoài vào phiên bản Elasticsearch của mình để ngăn chặn người ngoài đọc dữ liệu của bạn. Tìm dòng chỉ định `network.host`, bỏ comment và thay thế giá trị của nó thành `localhost`

```sh
. . .
network.host: localhost
. . .
```

Khởi động và enable service Elasticsearch với systemctl:

```sh
systemctl start elasticsearch
systemctl enable elasticsearch
```

Bạn có thể kiểm tra xem dịch vụ Elasticsearch có đang chạy hay không bằng cách gửi yêu cầu HTTP:

```sh
curl -X GET "localhost:9200"
```

Bạn sẽ thấy phản hồi như sau:

```sh
Output
{
  "name" : "OQtHP2R",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "qyvn0vh3TBu9oDoJG_kV9w",
  "version" : {
    "number" : "6.8.23",
    "build_flavor" : "default",
    "build_type" : "rpm",
    "build_hash" : "4f67856",
    "build_date" : "2022-01-06T21:30:50.087716Z",
    "build_snapshot" : false,
    "lucene_version" : "7.7.3",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

Bây giờ Elasticsearch đã hoạt động, hãy cài đặt Kibana, thành phần tiếp theo của ELK

Bước 4: Cài đặt và định cấu hình Kibana Dashboard

Theo thứ tự cài đặt trong tài liệu chính thức, bạn nên cài đặt Kibana làm thành phần tiếp theo sau Elasticsearch. Sau khi thiết lập Kibana, chúng ta sẽ có thể sử dụng giao diện của nó để tìm kiếm trực quan hóa dữ liệu mà Elasticsearch lưu trữ

Vì bạn đã thêm Elastic repo ở bước trước nên bạn chỉ có thể cài đặt các thành phần còn lại của ELK bằng yum:

```sh
yum install kibana -y
```

Sau đó kích hoạt và khởi động dịch vụ kibana

```sh
systemctl enable kibana
systemctl start kibana
```

Vì Kibana được cấu hình để chỉ lắng nghe trên localhost nên chúng ta phải thiết lập proxy ngược để cho phép truy cập từ bên ngoài vào nó. Chúng ta sẽ sử dụng Nginx cho mục đích này

Đầu tiên, sử dụng lệnh openssl để tạo người dùng `kibanaadmin` mà bạn sẽ sử dụng để truy cập Kibana dashboard. Ở ví dụ này tôi sẽ đặt tên tài khoản này là `kibanaadmin`, nhưng để đảm bảo tính bảo mật, bạn nên đặt tên tài khoản khác

Lệnh sau sẽ tạo người dùng và mật khẩu cho `kibanaadmin` và lưu trữ trong tệp `htpasswd.users`. Bạn sẽ cấu hình nginx để yêu cầu username và password khi truy cập kibana dashboard

```sh
echo "kibanaadmin:`openssl passwd -apr1`" | sudo tee -a /etc/nginx/htpasswd.users
```

Nhập và xác nhận mật khẩu tại dấu nhắc. Hãy lưu lại thông tin này, vì bạn sẽ cần nó để truy cập vào Kibana dashboard

Tiếp theo, ta sẽ tạo một tệp config nginx. Ở đây tôi sẽ đặt tên tệp này là `kibana.monest.sbs.conf`

```sh
vi /etc/nginx/conf.d/kibana.monest.sbs.conf
```

Thêm đoạn sau vào file 

```sh
server {
    listen 80;

    server_name kibana.monest.sbs;

    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/htpasswd.users;

    location / {
        proxy_pass http://localhost:5601;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Kiểm tra syntax của nginx trước khi thực hiện restart

```sh
[root@elk conf.d]# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Nếu không có lỗi, ta thực hiện restart nginx

```sh
systemctl restart nginx
```

Theo mặc định, SElinux security được đặt thành thực thi. Chạy lệnh sau để cho phép Nginx truy cập proxy

```sh
setsebool httpd_can_network_connect 1 -P
```

Truy cập kibana trên trình duyệt

```sh
http://your_server_ip/status
```

![](/ELK_stack/images/kibana.png)

Bước 5: Cài đặt và cấu hình Logstach

Mặc dù Beats có thể xử lý dữ liệu trực tiếp đến cơ sở dữ liệu Elasticsearch nhưng ta nên sử dụng Logstash để xử lý dữ liệu trước. Điều này sẽ cho phép bạn thu thập dữ liệu từ các nguồn khác nhau và xuất dữ liệu sang cở sở dữ liệu

Cài đặt Logstash bằng lệnh sau:

```sh
yum install logstash -y
```

Tạo tệp cấu hình có tên `02-beats-input.conf` và chèn vào đoạn sau

```sh
vi /etc/logstash/conf.d/02-beats-input.conf

# Nôi dung cần chèn
input {
  beats {
    port => 5044
  }
}
```

Tạo tệp cấu hình có tên là `10-syslog-filter.conf` 

```sh
vi /etc/logstash/conf.d/10-syslog-filter.conf

# Chèn vào nội dung sau

filter {
  if [fileset][module] == "system" {
    if [fileset][name] == "auth" {
      grok {
        match => { "message" => ["%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} sshd(?:\[%{POSINT:[system][auth][pid]}\])?: %{DATA:[system][auth][ssh][event]} %{DATA:[system][auth][ssh][method]} for (invalid user )?%{DATA:[system][auth][user]} from %{IPORHOST:[system][auth][ssh][ip]} port %{NUMBER:[system][auth][ssh][port]} ssh2(: %{GREEDYDATA:[system][auth][ssh][signature]})?",
                  "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} sshd(?:\[%{POSINT:[system][auth][pid]}\])?: %{DATA:[system][auth][ssh][event]} user %{DATA:[system][auth][user]} from %{IPORHOST:[system][auth][ssh][ip]}",
                  "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} sshd(?:\[%{POSINT:[system][auth][pid]}\])?: Did not receive identification string from %{IPORHOST:[system][auth][ssh][dropped_ip]}",
                  "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} sudo(?:\[%{POSINT:[system][auth][pid]}\])?: \s*%{DATA:[system][auth][user]} :( %{DATA:[system][auth][sudo][error]} ;)? TTY=%{DATA:[system][auth][sudo][tty]} ; PWD=%{DATA:[system][auth][sudo][pwd]} ; USER=%{DATA:[system][auth][sudo][user]} ; COMMAND=%{GREEDYDATA:[system][auth][sudo][command]}",
                  "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} groupadd(?:\[%{POSINT:[system][auth][pid]}\])?: new group: name=%{DATA:system.auth.groupadd.name}, GID=%{NUMBER:system.auth.groupadd.gid}",
                  "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} useradd(?:\[%{POSINT:[system][auth][pid]}\])?: new user: name=%{DATA:[system][auth][user][add][name]}, UID=%{NUMBER:[system][auth][user][add][uid]}, GID=%{NUMBER:[system][auth][user][add][gid]}, home=%{DATA:[system][auth][user][add][home]}, shell=%{DATA:[system][auth][user][add][shell]}$",
                  "%{SYSLOGTIMESTAMP:[system][auth][timestamp]} %{SYSLOGHOST:[system][auth][hostname]} %{DATA:[system][auth][program]}(?:\[%{POSINT:[system][auth][pid]}\])?: %{GREEDYMULTILINE:[system][auth][message]}"] }
        pattern_definitions => {
          "GREEDYMULTILINE"=> "(.|\n)*"
        }
        remove_field => "message"
      }
      date {
        match => [ "[system][auth][timestamp]", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
      }
      geoip {
        source => "[system][auth][ssh][ip]"
        target => "[system][auth][ssh][geoip]"
      }
    }
    else if [fileset][name] == "syslog" {
      grok {
        match => { "message" => ["%{SYSLOGTIMESTAMP:[system][syslog][timestamp]} %{SYSLOGHOST:[system][syslog][hostname]} %{DATA:[system][syslog][program]}(?:\[%{POSINT:[system][syslog][pid]}\])?: %{GREEDYMULTILINE:[system][syslog][message]}"] }
        pattern_definitions => { "GREEDYMULTILINE" => "(.|\n)*" }
        remove_field => "message"
      }
      date {
        match => [ "[system][syslog][timestamp]", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
      }
    }
  }
}
```

Cuối cùng tạo tệp có tên `30-elasticsearch-output.conf`

```sh
vi /etc/logstash/conf.d/30-elasticsearch-output.conf
```

Chèn đoạn cấu hình `output` sau. Kết quả đầu ra này định cấu hình Logstash để lưu trữ dữ liệu Beats trong Elasticsearch đang chạy ở localhost:9200. Beat được sử dụng trong bài viết này là `Filebeat`

```sh
output {
  elasticsearch {
    hosts => ["localhost:9200"]
    manage_template => false
    index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
  }
}
```

Kiểm tra cấu hình Logstash của bạn bằng lệnh sau:

```sh
sudo -u logstash /usr/share/logstash/bin/logstash --path.settings /etc/logstash -t
```

Nếu không có lỗi cú pháp, Output sẽ hiển thị `Configruation OK`

Sau đó hãy khởi động lại logstash để các cấu hình có hiệu lực

```sh
systemctl start logstash
systemctl enable logstash
```

Bước 6: Cài đặt và cấu hình filebeat 

ELK stack sử dụng một số công cụ nhẹ có tên Beats để thu thập dữ liệu từ nhiều nguồn khác nhau và vận chuyển chúng đến Logstash hoặc Elasticsearch. Dưới đây là các Beats hiện có sẵn từ Elastic

- Filebeat
- Metricbeat
- Packetbeat
- Winlogbeat
- Auditbeat
- Heartbeat

Trong bài viết này sử dụng Filebeat

Cài đặt Filebeat

```sh
yum install filebeat -y
```

Tiếp theo ta sẽ cấu hình Filebeat kết nối với Logstash

```sh
vi /etc/filebeat/filebeat.yml
```

Tìm đến phần `out.elasticsearch` và comment các dòng sau

```sh
...
#output.elasticsearch:
  # Array of hosts to connect to.
  #hosts: ["localhost:9200"]
...
```

Sau đó cấu hình phần `out.logstash`. Bỏ comment các dòng sau

```sh
output.logstash:
  # The Logstash hosts
  hosts: ["localhost:5044"]
```

Sau đó, kích hoạt module filebeat

```sh
filebeat modules enable system
```

Bạn có thể xem danh sách các module được enable hoặc disable bằng cách chạy

```sh
filebeat modules list
```

Tiếp đến ta cần load index template Elasticsearch

```sh
filebeat setup --template -E output.logstash.enabled=false -E 'output.elasticsearch.hosts=["localhost:9200"]'
```

Output sau khi chạy lệnh trên sẽ như sau

```sh
Output
Loaded index template
```

Tắt Logstash output và bật Elasticsearch output:

```sh
filebeat setup -e -E output.logstash.enabled=false -E output.elasticsearch.hosts=['localhost:9200'] -E setup.kibana.host=localhost:5601
```

Sau khi chạy lệnh trên sẽ có output trông như sau:

```sh
Output
. . .
2018-12-05T21:23:33.806Z        INFO    elasticsearch/client.go:163     Elasticsearch url: http://localhost:9200
2018-12-05T21:23:33.811Z        INFO    elasticsearch/client.go:712     Connected to Elasticsearch version 6.5.2
2018-12-05T21:23:33.815Z        INFO    template/load.go:129    Template already exists and will not be overwritten.
Loaded index template
Loading dashboards (Kibana must be running and reachable)
2018-12-05T21:23:33.816Z        INFO    elasticsearch/client.go:163     Elasticsearch url: http://localhost:9200
2018-12-05T21:23:33.819Z        INFO    elasticsearch/client.go:712     Connected to Elasticsearch version 6.5.2
2018-12-05T21:23:33.819Z        INFO    kibana/client.go:118    Kibana url: http://localhost:5601
2018-12-05T21:24:03.981Z        INFO    instance/beat.go:717    Kibana dashboards successfully loaded.
Loaded dashboards
2018-12-05T21:24:03.982Z        INFO    elasticsearch/client.go:163     Elasticsearch url: http://localhost:9200
2018-12-05T21:24:03.984Z        INFO    elasticsearch/client.go:712     Connected to Elasticsearch version 6.5.2
2018-12-05T21:24:03.984Z        INFO    kibana/client.go:118    Kibana url: http://localhost:5601
2018-12-05T21:24:04.043Z        WARN    fileset/modules.go:388  X-Pack Machine Learning is not enabled
2018-12-05T21:24:04.080Z        WARN    fileset/modules.go:388  X-Pack Machine Learning is not enabled
Loaded machine learning job configurations
```

Bây giờ, ta có thể start và enable Filebeat

```sh
systemctl start filebeat
systemctl enable filebeat
```

Để xác minh rằng Elasticsearch đang thực sự nhận dữ liệu, hãy truy vấn chỉ mục Filebeat bằng lệnh này:

```sh
curl -X GET 'http://localhost:9200/filebeat-*/_search?pretty'
```

Khi chạy lệnh trên Output trông sẽ như sau:

```sh
Output
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 3,
    "successful" : 3,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 3225,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "filebeat-6.5.2-2018.12.05",
        "_type" : "doc",
        "_id" : "vf5GgGcB_g3p-PRo_QOw",
        "_score" : 1.0,
        "_source" : {
          "@timestamp" : "2018-12-05T19:00:34.000Z",
          "source" : "/var/log/secure",
          "meta" : {
            "cloud" : {
. . .
```

Một lần nữa kiểm tra Kibana và xem dữ liệu mà Filebeat thu thập trong `Discover` -> `filebeat-*`

![](/ELK_stack/images/filebeat.png)