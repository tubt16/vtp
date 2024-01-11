Trước khi bắt tay vào viết 1 playbook ta cần điểm lại một số thuật ngữ và khái niệm quan trọng của Ansible

# Thuật ngữ

- Control Node/Management Control: Server cài đặt Ansible, chịu trách nhiệm cho việc đưa các công việc bạn cung cấp đến các server từ xa. Nói một cách khác thì đây là server mà bạn đứng trên đó và lệnh cho các server khác thực hiện các việc bạn muốn mà không cần phải trực tiếp đăng nhập vào chúng

- Inventory: Một file INI hoặc YAML chứa các thông tin về các server từ xa mà bạn quản lý

- Playbook: Một file YAML chứa một tập các công việc cần tự động hóa

- Task: Một task sẽ xác định một công việc đơn lẻ sẽ được thực hiện

- Module: Một Module sẽ trưu tượng hóa một tác vụ hệ thống. Ansible cũng cấp rất nhiều module tích hợp để ta sử dụng nhưng nếu bạn muốn cũng có thể tự tạo module. Nói cách khác ta giao tiếp với Ansible thông qua các Module

- Role: Một tập hợp các Playbook, các template và các file khác, được tổ chức để tạo điều kiện tái sử dụng và chia sẻ

- Play: Một lần thực thi suôn sẻ từ đầu đến cuối được gọi là một `play`

- Facts: Các biến toàn cục chứa các thông tin về hệ thống, như các `network interface` hay `operating system`

- Handlers: Sử dụng để kích hoạt thay đổi trạng thái các service như việc ta restart hay reload một service

# Bất cập khi chỉ sử dụng Ad-hoc command

Giả sử bạn đứng trên một Node control và ra lệnh cho các server khác mà bạn quản lý. Tuy nhiên vấn đề đặt ra là số lượng thao tác cần thực hiện trên các server kia thì nhiều, nhiều server có tác dụng, nhiệm vụ giống nhau nên cần thực hiện các thao tác giống nhau. 

Vậy không lẽ ta cần phải gõ tay cả trăm lệnh Ad-hoc. Để rồi khi có 1 server mới ta lại gõ tay, chưa kể việc sai sót khi thao tác

Lúc này bạn sẽ viết một Playbook - nơi chứa chi tiết tất cả những gì bạn muốn làm với các server từ xa kia và cách thức thực hiện chúng

Mỗi một thao tác trong playbook được gọi là một `Task` (Cài đặt, khởi động, dừng)

Ta sử dụng Module để tạo thành Task (Ví dụ: muốn cài đặt một gói trên CentOS 7 ta sử dụng Module yum của Ansible)

# Định dạng của Task

```sh
- name: Install httpd
  yum:
    name: httpd
    state: latest
```

`name`: Là một tùy chọn nhưng bạn nên sử dụng nó để đặt tên cho các Task. Nó sẽ hiển thị khi Task được thực thi giúp bạn dễ quan sát, theo dõi. Với những người sử dụng lại Playbook của bạn, họ sẽ dễ dàng đọc, hiểu Playbook hơn

`yum`: Là Module tích hợp sẵn Ansible giúp Ansible hiểu được bạn muốn quản lý các package trên CentOS

**Task này thể hiện rằng bạn muốn cập nhật httpd package lên bản mới nhất. Nếu chưa có, nó sẽ được cài đặt**

# Định dạng của Playbook

Các Playbook là các file định dạng YAML chứa một loạt các mô tả chỉ thị nhằm mục đích tự động hóa trên server từ xa

```sh
---
  host: centos9
  become: True
  tasks:
  - name: Install httpd
    yum:
      name: httpd
      state: latest
  - name: Start httpd
    service:
      name: httpd
      state: start
      enabled: True
```

YAML dựa vào việc thụt đầu dòng để sắp xếp cấu trúc dữ liệu. Bạn cần cẩn thận điều này khi viết Playbook

# Viết playbook

### Làm việc với các biến

Cách đơn giản nhất để xác định các biến là sử dụng section có tên `vars` của Playbook

Ví dụ dưới đây, ta định nghĩa các biến `package` - biến mà sau này được sử dụng trong các task

```sh
---
  hosts: centos9
  become: True
  become_user: root
  vars:
    package: httpd
  tasks:
  - name: Install httpd
    yum:
      name: "{{httpd}}"
      state: latest
```

Biến `package` có phạm vi sử dụng trên toàn Playbook

### Sử dụng vòng lặp

Ta sử dụng vòng lặp khi phải lặp lại một task nhiều lần

Chẳng hạn như cài 10 package khác nhau. Chắc hẳn bạn không muốn viết đi viết lại cả 10 task

Để tạo một vòng lặp bên trong một task ta sử dụng `with_items` kèm theo bên dưới là một mảng giá trị. Ta truy xuất đến các giá trị này thông qua vòng lặp `item`

```sh
---
  hosts: centos9
  become: True
  become_user: root
  tasks:
  - name: Install package
    yum:
      name: "{{item}}"
      state: latest
    with_items:
    - httpd
    - php
    - php-mysql
    - php-fpm
    - mariadb-server
    - mariadb
```

Ta cũng có thể sử dụng kết hợp với một biến mảng

```sh
---
  hosts: centos9
  become: True
  become_user: root
  tasks:
  - name: Install httpd
    yum:
      name: ['httpd', 'php', 'php-mysql', 'php-fpm', 'mariadb-server', 'mariadb']
      state: latest
```

### Sử dụng câu điều kiện (Conditionals)

Các câu điều kiện sử dụng để tự động quyết định xem liệu một task có được thực thi hay không dựa trên một biến hay một output từ một nguồn, ví dụ: output của một command

Ví dụ:

```sh
  - name: Shutdown CentOS Based Systems
    command: /sbin/shutdown -t now
    when: ansible_facts['distribution'] == "CentOS"
```

Ở ví dụ trên ta sử dụng một trong các biến `ansible_facts` (Các biến đặc biệt của Ansible) là `ansible_fact['distribution']` nhằm kiểm tra distro của node client. Nếu là `CentOS` thì sẽ thực hiện shutdown node đó

Một ví dụ khác:

```sh
---
  hosts: centos9
  become: True
  become_user: root
  tasks:
  - name: Check if HTTPD is installed
    register: http_installed
    command: httpd -v
    ignore_errors: true

  - name: This task is only executed if HTTPD is installed
    debug: var=http_installed
    when: http_installed is success

  - name: This task is only executed if HTTPD is not installed
    debug: msg='HTTPD is NOT installed'
    when: http_installed is failed
```

Kết quả thực hiện Playbook khi note `asb-node01` đã cài httpd

```sh
root@asb-control:/tubt/ansible# ansible-playbook -i inventory.ini checkhttpd.yaml 

PLAY [centos9] ************************************************************************************************************************
TASK [Gathering Facts] ****************************************************************************************************************ok: [asb-node01]

TASK [Check httpd is installed] *******************************************************************************************************changed: [asb-node01]

TASK [This task is only executed if HTTPD is installed] *******************************************************************************ok: [asb-node01] => {
    "http_installed": {
        "changed": true,
        "cmd": [
            "httpd",
            "-v"
        ],
        "delta": "0:00:00.030104",
        "end": "2023-08-25 02:49:15.121016",
        "failed": false,
        "msg": "",
        "rc": 0,
        "start": "2023-08-25 02:49:15.090912",
        "stderr": "",
        "stderr_lines": [],
        "stdout": "Server version: Apache/2.4.57 (CentOS Stream)\nServer built:   Jul 20 2023 00:00:00",
        "stdout_lines": [
            "Server version: Apache/2.4.57 (CentOS Stream)",
            "Server built:   Jul 20 2023 00:00:00"
        ]
    }
}

TASK [This task is only executed if HTTPD is NOT installed] ***************************************************************************skipping: [asb-node01]

PLAY RECAP ****************************************************************************************************************************asb-node01                 : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

Kết quả thực hiện Playbook khi node `asb-node01` đã gỡ httpd

```sh
root@asb-control:/tubt/ansible# ansible-playbook -i inventory.ini checkhttpd.yaml 

PLAY [centos9] ************************************************************************************************************************
TASK [Gathering Facts] ****************************************************************************************************************ok: [asb-node01]

TASK [Check httpd is installed] *******************************************************************************************************fatal: [asb-node01]: FAILED! => {"changed": false, "cmd": "httpd -v", "msg": "[Errno 2] No such file or directory: b'httpd'", "rc": 2, "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}
...ignoring

TASK [This task is only executed if HTTPD is installed] *******************************************************************************skipping: [asb-node01]

TASK [This task is only executed if HTTPD is NOT installed] ***************************************************************************ok: [asb-node01] => {
    "msg": "HTTPD is NOT installed"
}

PLAY RECAP ****************************************************************************************************************************asb-node01                 : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=1
```

Ở ví dụ này ta viết 3 task

- task 1: Chạy lệnh kiểm tra version của apache trên các host thuộc group `centos9`. Nếu đã cài apache thì lệnh sẽ chạy bình thường, output sẽ được lưu vào biến `http_installed`
- task 2: Kiểm tra xem lệnh ở task 1 có được thực thi thành công không thông qua việc kiểm tra biến `http_installed`. Nếu thành công thì hiển thị nội dung của biến `http_installed`
- task 3: Kiểm tra xem lệnh ở task 1 có được thực thi thành công không thông qua viêc kiểm tra biến `http_installed`. Nếu không thành công thì hiển thị nội dung `HTTPD is NOT installed`

### Làm việc với các Template

Các template thường được sử dụng để thiết lập các tệp cấu hình, cho phép sử dụng các biến và các tính năng khác nhằm làm cho các tệp trở nên linh hoạt và thuận tiện hơn cho việc tái sử dụng

Ví dụ:

Tôi có 1 file là `index.html` có nội dung như sau:

```sh
root@asb-control:/var/www/html# cat index.html
<p>My name is {{my_name}}</p>
```

Hãy để ý biến `my_name` trong file. Cùng với đó tôi có một playbook ở cùng với folder chứa file `index.html` kia

```sh
---
- hosts: centos9
  become: True
  vars:
    my_name: 'Tubt'
  tasks:
  - name: Test template
    template:
      src: index.html
      dest: /var/www/html/index.html
```

Node client đã cài đặt và start apache. Sau khi chạy playbook ta thu được kết quả

```sh
root@asb-control:/tubt/ansible# curl http://asb-node01
<p>My name is Tubt</p>
```

### Khai báo và kích hoạt các Handler

Các `handler` được sử dụng để kích hoạt một trạng thái nào đó của service như restart hay stop

Các `handler` giống như các task nhưng chỉ được thực thi khi được kích hoạt bởi một chỉ thị `notify` bên trong 1 task

Chúng thường được khai báo như một mảng trong phần `handlers` của playbook

```sh
---
- hosts: centos9
  become: True
  become_user: root
  vars:
    my_name: 'Tubt'
  tasks:
  - name: Template config file
    temple:
      src: index.html
      dest: /var/www/html/index.html
    notify:
      - restart httpd
  handlers:
      - name: restart httpd
        service:
          name: httpd
          state: restarted
```

### Playbook mẫu

Cuối cùng tôi sẽ đưa ra một ví dụ về playbook mẫu

```sh
---
- hosts: centos9
  become: True
  become_user: root
  vars:
    my_name: 'Tubt'
    package: httpd
  tasks:
  - name: Install httpd
    yum:
      name: "{{package}}"
      state: latest

  - name: Check HTTPD is installed
    register: http_installed
    command: httpd -v
    ignore_errors: True

  - name: This task is only executed if HTTPD is installed
    debug: var=http_installed
    when: http_installed is success

  - name: This task is only executed if HTTPD is NOT installed
    debug: msg='HTTPD is not installed'
    when: http_installed is failed

  - name: Template config file
    template:
      src: index.html
      dest: /var/www/html/index/html
    notify:
      - name: restart httpd
  handlers:
      - name: restart httpd
        service:
          name: httpd
          state: restarted
```

Một số điểm cẩn lưu ý:

- `hosts: centos9`: Playbook bắt đầu bằng cách nói rằng nó sẽ được áp dụng cho một máy chủ có tên là `centos9` hoặc tất cả máy chủ nằm trong group `centos9` bên trong file `inventory.ini` của bạn.

- `become: True`: Sử dụng đặc quyền sudo để chạy tất cả các task bên trong Playbook

- `vars`: Nơi khai báo các biến

- `task`: Nơi các task được khai báo

- `handlers`: Nơi service cùng trạng thái của nó được khai báo

- `ignore_errors`: Dùng để bỏ qua các lệnh trả về kết quả fail.Theo mặc định Ansible sẽ dừng thực thi các task trên máy chủ khi một tác vụ không thành công trên máy chủ đó. Bạn có thể sử dụng `ignore_errors` để tiếp tục các task mặc dùng thất bại. Ở đây mình để giá trị `ignore_errors: True` để nếu output của lệnh `httpd -v` là fail thì playbook vẫn sẽ được thực thi tiếp

- `debug`: In giá trị câu lệnh trong khi thực thi, hữu ích trong việc gỡ lỗi các biến hoặc biểu thức mà không nhất thiết phải tạm dừng playbook. Thường đi với `when`

- `when`: Một câu lệnh điều kiện trong ansible

- `msg`: In đoạn message trong `msg` ra màn hình

Còn về mục đích của playbook thì tôi đã giải thích ở các phần trên rồi

### Chạy một Playbook

Viêc chạy một playbook không có gì quá phức tạp

```sh
ansible-playbook -i <path_to_inventory_file> <path_to_playbook>
```

- `-i`: Chỉ định đường dẫn inventory file

- `path_to_inventory_file`: Đường dẫn tới file inventory

- `path_to_playbook`: Đường dẫn tới file playbook

**PLAY RECAP**

```sh
PLAY RECAP ****************************************************************************************************************************asb-node01                 : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=1
```

Lưu ý phần cuối sau khi kết thúc một Playbook `PLAY RECAP`. Đây chính là ưu điểm của Ansbile

Đó là nếu Ansible duyệt qua 1 task mà task đó đã được thực hiện trước đó rồi mà không có gì thay đổi thì Ansible sẽ đi tới task tiếp theo mà không phải mất công chạy lại task đó nữa