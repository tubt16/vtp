# Một số Ansible module mà bạn nên biết

Một trong những khái niệm quan trọng trong Ansible là `modules`

Modules là một thành phần cốt lõi của Ansible, nó là một khối/đơn vị xử lý một task. Thông qua quá trình tìm hiểu về Ansible, mình sẽ tổng hợp lại một số modules Ansible cơ bản và thường xuyên được sử dụng 

### Module 1: Package Management

Đây là module được thiết kế cho hầu hết các trình quản lý gói (package management) phổ biến, chẳng hạn như apt, dnf, yum ... cho phép bạn cài đặt các package trên hệ thống. Ngoài các chức năng cụ thể của từng trình quản lý gói thì hầu hết các trình quản lý gói đều có thể install, update, upgrade, downgrade, remove và list các packages

Ví dụ: Cài đặt gói `httpd` trên CentOS 9 sử dụng trình quản lý gói `yum`

```sh
---
- host: centos9
  become: True
  become_user: root
  tasks:
  - name: Install httpd
  	yum:
  	  name: httpd
  	  state: present
```

### Module 2: File

Trong Ansible, có rất nhiều các module làm việc với tập tin, thư mục, links trên các node đích (node client) như copy, template, file... Trước tiên chúng ta hãy cùng tìm hiểu về file module. File module giúp quản lý tập tin và các thuộc tính của nó (Ví dụ như quyền hay symlinks cho tệp tin)

Ví dụ:

```sh
---
- hosts: centos9
  become: True
  become_user: root
  tasks:
  - name: Change file owner, group and permissions
    file:
      path: /var/www/html
      owner: tubt
      group: root
      mode: '0644'

  - name: Create an insecure file
    file:
      path: /tubt/insecureFile
      owner: root
      group: root
      mode: '0755'
  
  - name: Create symlinks
    file:
      src: /var/www/html
      dest: /tubt/insecureFile
      owner: root
      group: root
      state: link
```

### Module 3: Template

Có nhiều cách khác nhau với Ansible giúp bạn có thể thao tác với nội dung của tệp, tuy nhiên module thường được sử dụng nhất là `template`

Template trong Ansible là một tệp chứa tất cả các tham số cấu hình. Trong quá trình thực thi playbook, các biến có thể được thay thế bằng các giá trị bạn cần. Ngoài ra bạn có thể thay thế bằng các giá trị bạn cần. Các tệp template thường sẽ có phần đuôi mở rộng là `.j2`. Các biến trong tệp template sẽ được ký hiệu bằng dấu ngoặc nhọn kép `{{var}}`

Ví dụ:

```sh
- hosts: centos9
  become: True
  become_user: root
  vars:
    first_var: 'Tubt'
    inline_var: 'Tubui'
  tasks:
    - name: Ansible Template test
    template:
      src: index.j2
      dest: /tubt/testTemplate.txt
```

Nội dung của file `index.j2`

```sh
Hello {{first_var}}

Hello {{inline_var}}
```

Sau khi chạy playbook trên output của file `testTemplate.txt` tại node client thuộc group centos9 sẽ như sau

```sh
[root@asb-node01 tubt]# cat testTemplate.txt 
Hello Tubt

Hello Tubui
```

### Module 4: Copy

Copy module là module thường được sử dụng khi chúng ta muốn sao chép một tập tin từ Ansible server (Management node) đến các node đích (client node)

Ví dụ:

```sh
---
- hosts: centos9
  become: True
  become_user: root
  tasks:
  - name: Copy file from Ansible server to Ansible node with user root, group and file permissions
  copy: 
    src: /test.txt
    dest: /root/test.txt
    owner: root
    group: root
    mode: '0644'
```

### Module 5: Service

Service module là một module rất hữu ích giúp kiểm soát các service chạy trên các server Linux. Giống như các module khác, `service` cũng đi kèm với một số tham số và các tham số này có các tùy chọn riêng hoặc giá trị phù hợp

Sử dụng các tham số này và các giá trị bắt buộc, các bạn có thể quản lý các service với các chức năng như stop, start, reload trên các node client

Ví dụ:

```sh
---
- hosts: centos9
  become: True
  become_user: root
  tasks:
  - name: Start service httpd if NOT running
    service:
      name: httpd
      state: started

  - name: Stop service httpd if running
    service:
      name: httpd
      state: stopped

  - name: Restart service httpd
    service:
      name: httpd
      state: restarted

  - name: Reload service httpd
    service:
      name: httpd
      state: reloaded

  - name: Enable service httpd
    service:
      name: httpd
      enable: yes
```
