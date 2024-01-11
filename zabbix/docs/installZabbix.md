# Cài đặt Zabbix 5.0 và định cấu hình

1. Môi trường cài đặt 

- Zabbix version 5.0

- OS: CentOS 7

- Database: MySQL

- Webserver: Httpd

- Mô hình triển khai: All in one

2. Thực hiện tắt Firewalld và SElinux

```sh
systemctl disable firewalld
systemctl stop firewalld

sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
setenforce 0
```


3. Cài đặt Zabbix repository

```sh
rpm -Uvh https://repo.zabbix.com/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm
yum clean all
```

4. Cài đặt Zabbix server, agent, frontend

```sh
yum install zabbix-server-mysql zabbix-agent -y
```

5. Cài đặt Zabbix frontend

Enable Red Hat Software Collections

```sh
yum install centos-release-scl -y
```

Chỉnh sửa repo Zabbix `/etc/yum.repos.d/zabbix.repo` thành như sau:

```sh
[zabbix-frontend]
...
enabled=1
...
```

Cài đặt các gói Zabbix frontend

```sh
yum install zabbix-web-mysql-scl zabbix-apache-conf-scl -y
```

6. Cài đặt MariaDB

Cài đặt MariaDB

```sh
yum -y install MariaDB-server MariaDB-client
systemctl start mariadb
systemctl enable mariadb
systemctl status mariadb
```

Cấu hình MariaDB

```sh
mysql_secure_installation
```

Tạo database cho zabbix

```sh
mysql -u root -p

create database zabbix character set utf8 collate utf8_bin;
create user zabbix@localhost identified by 'tubt16a6@';
grant all privileges on zabbix.* to zabbix@localhost;
quit;
```

Import database

```sh
zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -uzabbix -p zabbix
```

Lưu ý: Nhập password cho user `zabbix` sau khi chạy xong câu lệnh

7. Cấu hình database cho Zabbix server

Chỉnh sửa file `/etc/zabbix/zabbix_server.conf`

```sh
...
DBHost=localhost
DBName=zabbix
DBUser=zabbix
DBPassword=tubt16a6@
...
```

Đây là các thông số vừa tạo trong database ở câu lệnh bên trên

Trong đó:

- DBHost: localhost (Cài trên cùng một host với zabbix-server)

- DBName: Tên của database

- DBUser: Tên của user databases tạo ở trên

- DBPassword: Password của user databases tạo ở trên

8. Định cấu hình PHP cho Zabbix frontend

Chỉnh sửa file `/etc/opt/rh/rh-php72/php-fpm.d/zabbix.conf`, bỏ comment và chỉnh sửa timezone phù hợp

```sh
php_value[date.timezone] = Asia/Ho_Chi_Minh
```

9. Start Zabbix server và Zabbix agent

```sh
systemctl restart zabbix-server zabbix-agent httpd rh-php72-php-fpm
systemctl enable zabbix-server zabbix-agent httpd rh-php72-php-fpm
```

Mở trình duyệt web và truy cập `http://IP-server/zabbix` bạn sẽ thấy như sau:

Thực hiện cấu hình zabbix-web

![](/zabbix/images/zabbix5.png)

Chọn `Next step`

![](/zabbix/images/zabbix_setup1.png)

Chọn `Next step`

![](/zabbix/images/zabbix_setup2.png)

Điền đúng thông tin và chọn `Next step`

![](/zabbix/images/zabbix_setup3.png)

Chọn `Next step`

![](/zabbix/images/zabbix_setup4.png)

Chọn `Finish`

![](/zabbix/images/zabbix_setup5.png)

Đăng nhập với account/password: Admin/zabbix

![](/zabbix/images/finish.png)


Như vậy ta đã cài đặt thành công Zabbix 5.0