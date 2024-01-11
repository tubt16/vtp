# Mô hình

Ta sử dụng 1 node master và 1 node client: node client cài centos7

Trên node master đã cài Ansible và đã copy SSH key sang node client

Khai báo file inventory

```sh
root@asb-control:/tubt_ansible/ansible/yamlfile# cat inventory.ini 
[centos7]
ansible-node01 ansible_host=34.139.117.216 ansible_port=22 ansible_user=root
```

# Các công việc cần làm và các module liên quan

### Các công việc cần làm

Để tự động hóa một việc gì đấy chúng ta cần phải làm việc đó bằng cách thủ công tốt trước đã. Bởi vậy trước tiên ta cần biết quy trình mình sẽ làm để cài đặt WordPress trên CentOS 7:

- Cài đặt LAMP
- Đảm bảo các service bật và port được thông
- Cài đặt WordPress
- Tạo cơ sở dũ liệu, người dùng cho cơ sở dữ liệu
- Update version PHP nhằm tránh lỗi version PHP cũ không được hỗ trợ ở WP phiên bản mới

### Các module liên quan

Quy trình đã nắm được, tiếp theo ta cần tìm các module liên quan đến những công việc nằm trong quy trình trên. Để từ những module này chúng ta xây dựng lên một Playbook hoàn chỉnh

Các module sẽ sử dụng:

- yum
- service
- firewalld
- get_url
- unarchive
- shell
- mysql_db
- mysql_user
- replace

# Viết Playbook

1. Khai báo

```sh
---
- host: centos7
  remote_user: root
```

2. Cài đặt LAMP

```sh
  tasks:
  - name: Install LAMP
  	yum:
  	  name: '{{item}}'
  	  state: present
  	with_items:
  	- httpd
  	- mariadb-server
    - mariadb
    - php
    - php-mysql
    - php-fpm
```

3. Đảm bảo các service được bật và các port được thông

```sh
  - name: Start and enable services
  	service:
  	  name: '{{item}}'
  	  state: started
  	  enabled: True
  	with_items:
  	- httpd
  	- mariadb
  - name: HTTP and HTTPS pass the firewalld
  	firewalld:
  	  service: '{{item}}'
  	  state: enabled
  	  permanent: True
  	  immediate: True
  	become: True
  	with_items:
  	- http
  	- https
```

4. Tải, giải nén Wordpress

```sh
	- name: Install php-gd,rsync
	  yum:
	    name: '{{item}}'
	    state: present
	  with_items:
	  - php-gd
	  - rsync
	- name: Restart httpd
	  service:
	    name: httpd
	    state: restarted
	- name: Download wordpress
	  get_url:
	    url: https://wordpress.org/wordpress-6.3.1.zip
	    dest: /root
	- name: Extract wordpress
	  unarchive:
	    src: /root/wordpress-6.3.1.zip
	    dest: /root
	    remote_src: yes
	- name: Rsync wordpress
	  shell: rsync -avP /root/wordpress /var/www/html/
	- name: Create folder uploads
	  shell: mkdir /var/www/html/wp-content/uploads
	- name: Set user:group
	  shell: chown -R apache:apache /var/www/html/*
```

5. Tạo database và user cho WordPress

```sh
	- name: Install MySQL-python
	  yum:
	    name: MySQL-python
	    state: present
	- name: Create database wordpress
	  mysql_db:
	    name: wordpress
	    state: present
	- name: Create user wordpressuser
	  mysql_user:
	    name: wordpressuser
	    host: localhost
	    password: wordpresspassword
	    priv: 'wordpress.*:ALL'
	    state: present
	- name: Backup file config wp
	  shell: cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
	- name: Config db name
	  replace:
	    path: /var/www/html/wp-config.php
	    regexp: 'database_name_here'
	    replace: 'wordpress'
	- name: Config username
	  replace:
	    path: /var/www/html/wp-config.php
	    regexp: 'username_here'
	    replace: 'wordpressuser'
	- name: Config password database
	  replace:
	    path: /var/www/html/wp-config.php
	    regexp: 'password_here'
	    replace: 'wordpresspassword'
```

Ở đây chúng ta thực hiện tạo 

```sh
database: wordpress
username: wordpressuser
password: wordpresspassword
```

7. Update version PHP

```sh
	- name: Config version PHP
	  yum:
	    name: '{{item}}'
	    state: present
	  with_items:
	  - epel-release
	  - yum-utils
	  - http://rpms.remirepo.net/enterprise/remi-release-7.rpm
	- name: Config version PHP
	  shell: yum-config-manager --enable remi-php72
	- name: Config version PHP
	  yum:
	    name: '{{item}}'
	    state: present
	  with_items:
	  - php
	  - php-common
	  - php-opcache
	  - php-mcrypt
	  - php-cli
	  - php-gd
	  - php-curl
	  - php-mysqlnd
	- name: Restart Apache
	  service:
	    - name: httpd
	    - state: restarted
```

8. Chạy Playbook

```sh
---
- hosts: centos7
  remote_user: root
  tasks:
  - name: Install LAMP
    yum:
      name: '{{item}}'
      state: present
    with_items:
    - httpd
    - mariadb-server
    - mariadb
    - php
    - php-mysql
    - php-fpm

  - name: Ensure service enabled and started
    service:
      name: '{{item}}'
      state: started
      enabled: True
    with_items:
    - mariadb
    - httpd
  - name: Collect facts about system services
    service_facts:
    register: service_status

  - name: Install php-gd,rsync
    yum:
      name: '{{item}}'
      state: present
    with_items:
    - php-gd
    - rsync
  - name: Restart httpd
    service:
      name: httpd
      state: restarted
  - name: Down wordpress
    get_url:
      url: http://wordpress.org/wordpress-6.3.1.tar.gz
      dest: /root
  - name: extract wordpress
    unarchive:
      src: /root/wordpress-6.3.1.tar.gz
      dest: /root
      remote_src: yes
  - name: rsync wordpress
    shell: rsync -avP /root/wordpress/ /var/www/html/
  - name: Create folder uploads
    shell: mkdir /var/www/html/wp-content/uploads
  - name: Set user:group
    shell: chown -R apache:apache /var/www/html/*

  - name: Install MySQL-python
    yum:
      name: MySQL-python
      state: present
  - name: Create database wordpress
    mysql_db:
      name: wordpress
      state: present
  - name: Create user wordpressuser
    mysql_user:
      name: wordpressuser
      host: localhost
      password: wordpresspassword
      priv: 'wordpress.*:ALL'
      state: present

  - name: Backup file config wp
    shell: cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
  - name: Config db name
    replace:
      path: /var/www/html/wp-config.php
      regexp: 'database_name_here'
      replace: 'wordpress'
  - name: Config username
    replace:
      path: /var/www/html/wp-config.php
      regexp: 'username_here'
      replace: 'wordpressuser'
  - name: Config password
    replace:
      path: /var/www/html/wp-config.php
      regexp: 'password_here'
      replace: 'wordpresspassword'

  - name: Config version PHP
    yum:
      name: '{{item}}'
      state: present
    with_items:
    - epel-release
    - yum-utils
    - http://rpms.remirepo.net/enterprise/remi-release-7.rpm
  - name: Config version PHP
    shell: yum-config-manager --enable remi-php72
  - name: Config version PHP
    yum:
      name: '{{item}}'
      state: present
    with_items:
    - php
    - php-common
    - php-opcache
    - php-mcrypt
    - php-cli
    - php-gd
    - php-curl
    - php-mysqlnd
  - name: Restart Apache
    service:
      name: httpd
      state: restarted
```

Lưu ý file với tên `playbook.yaml`

Chạy Playbook 

```sh
ansible -i /tubt_ansible/ansible/yamlfile/inventory.ini playbook.yaml
```

Kết quả

![](/ansible/images/wp1.png)

![](/ansible/images/wp2.png)

![](/ansible/images/wp3.png)