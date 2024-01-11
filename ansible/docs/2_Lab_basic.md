# Mô hình

|AnsibleServer |OS |IP|
|---|---|---|
|asb-control|Ubuntu 22|172.31.47.230|
|asb-node01|CentOS 9|172.31.41.73|
|asb-node02|CentOS 9|172.31.42.113|
|asb-node03|Ubuntu 20|172.31.43.239|


# Cấu hình SSH key và khai báo file Inventory

Ansible hoạt động theo cơ chế angentless, có nghĩa là không cần cài agent vào các máy client để điều khiển, thay vào đó ansible sẽ sử dụng việc điều khiển các client thông qua SSH. Do vậy tới bước này ta có thể dùng 2 cách để ansible có thể điều khiển được máy client

- Cách 1: Sử dụng username, port ssh, password để khai báo trong `Inventory` file. Cách này không được khuyến cáo khi sử dụng trong môi tường thực tế vì password sẽ được khai báo dạng clear text hiển thị trong file `Inventory` như vậy rất dễ để lộ thông tin cá nhân hoặc ta cần file secure cho file `Inventory` bằng `Ansible-vault` để có thể sử dụng cách này
- Cách 2: Sử dụng ssh keypair. Có nghĩa là ta phải tạo ra private key và public key trên node `Ansible Server` và copy public key sang các node client (Private key đóng vai trò là ổ khóa, còn Public key đóng vai trò là chìa khóa, chìa khóa khớp với ổ khóa thì ta mới cho phép điều khiển)

Trong hướng dẫn này sử dụng cách 2

# Tạo SSH key cho các node

Đứng tại node `Ansible Server` tạo SSH key, sau đó copy SSH key sang các node còn lại

Mục tiêu là sử dụng keypair để không phải nhập password mỗi khi đăng nhập vào các client

Vì đây là môi trường lab nên sẽ sử dụng user `root` để thực hiện

Đứng tại user `root` của node Ansible và thực hiện bước tạo key

```sh
ssh-keygen
```

Thực hiện copy file key sang các node còn lại

```sh
ssh-copy-id root@172.31.41.73
ssh-copy-id root@172.31.42.113
ssh-copy-id root@172.31.43.239
```

Sau khi copy ssh key sang các node client, hãy thử SSH sang các node đó, nếu không bị hỏi thì ta đã copy ssh key thành công

# Tạo file inventory

Ansible sử dụng file `Inventory` để kết nối tới các server cần thao tác. Giống như file `host` trong `/etc/hosts` để trỏ IP tới domain, thì một file `Ansible inventory` sẽ trỏ các server (địa chỉ IP hoặc tên domain) tới groups

File `Inventory` có sẵn khi chúng ta cài đặt Ansible

Đường dẫn chứa file `Inventory`: `/etc/ansible/hosts`

Ta có thể tạo một file `Iventory` tại vị trí khác, ở đây mình sử dụng đường dẫn này

```sh
sudo mkdir -p /tubt/ansible
```

Thực hiện tạo file `Inventory` có định dạng `.ini` và khai báo các host cần quản lý

```sh
touch inventory.ini
```

Nội dung của file `Inventory` định dạng INI sẽ có dạng như sau

```sh
[centos9]
172.31.41.73 
172.31.42.113

[ubuntu20]
172.31.43.239
```

Sau khi thêm các dòng trên, ta lưu lại file trên, lưu ý rằng cặp thẻ `[]` để khai báo các group. Các group này do ta quy hoạch sao cho phù hợp với hệ thống

Thực hiện kiểm tra danh sách các host đã được khai báo trong file `inventory.ini` trên bằng lệnh

```sh
ansible all -i inventory.ini --list-host
```

Trong đó `all` là một tùy chọn của lệnh trên, mục tiêu là liệt kê tất cả các hosts nằm trong file `inventory.ini`, bất kể các host đó nằm ở group nào

Kết quả:

```sh
root@asb-control:/tubt/ansible# ansible all -i inventory.ini --list-host
  hosts (3):
    172.31.41.73
    172.31.42.113
    172.31.43.239
```

Nếu chỉ muốn kiểm tra danh sách các host trong group `ubuntu20` ta thực hiện với tùy chọn lệnh như sau

```sh
ansible ubuntu20 -i inventory.ini --list-host
```

Kết quả:

```sh
root@asb-control:/tubt/ansible# ansible ubuntu20 -i inventory.ini --list-host
  hosts (1):
    172.31.43.239
```

Một file `Iventory` tương đối hoàn chỉnh sẽ có định dạng sau. Hãy sử lại file inventory để có định dạng như bên dưới, sẽ bổ sung thêm các tùy chọn

```sh
[centos9]
asb-node01 ansible_host=172.31.41.73 ansible_port=22 ansible_user=root

[centos]
asb-node02 ansible_host=172.31.42.113 ansible_port=22 ansible_user=root

[ubuntu20]
asb-node03 ansible_host=172.31.43.239 ansible_port=22 ansible_user=root
```

- `asb-node01`, `asb-node02`, `asb-node03` tương ứng là các hostname của các node
- `ansible_host`: Địa chỉ IP của node client tương ứng
- `ansible_port`: Port của SSH phía client, nếu ta thay đổi thì sẽ chỉnh lại cho đúng
- `ansible_user`: Là username của client mà AnsibleServer sẽ dùng để tương tác

# Sử dụng Ad-hoc command cơ bản

Ad-hoc command là các lệnh chạy đơn để thực hiện 1 chức năng nhanh chóng. Chúng có thể được sử dụng khi chúng ta đưa ra một lệnh trên một hoặc nhiều server

Chúng ta có thể kiểm tra việc truy cập vào các hosts đã khai báo từ file `inventory.ini` bằng lệnh sau:

```sh
ansible all -i inventory.ini -m ping 
```

Trong đó `-m` là dấu hiệu của việc sử dụng module trong câu lệnh (`-m` là viết tắt của module). Câu lệnh trên sử dụng module `ping`, một module có sẵn của Ansible. Bạn có thể tìm kiếm các module có sẵn tại https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html

Kết quả của lệnh trên:

```sh
asb-node03 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
asb-node02 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
asb-node01 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

### Sử dụng module `command`

Kiểm tra `uptime` của các client

```sh
ansible all -i inventory.ini -m command -a "uptime"
```

Trong đó tùy chọn `-a` để truyền thêm các đầu vào cho module `command`. Tùy chọn này cũng được dùng trong các module khác

Kết quả:

```sh
asb-node01 | CHANGED | rc=0 >>
 07:02:24 up 15:53,  1 user,  load average: 0.08, 0.02, 0.01
asb-node02 | CHANGED | rc=0 >>
 07:02:24 up  3:36,  1 user,  load average: 0.00, 0.00, 0.00
asb-node03 | CHANGED | rc=0 >>
 07:02:24 up 53 min,  1 user,  load average: 0.00, 0.00, 0.00
```

Ta có thể thực hiện với nhiều lệnh khác

```sh
ansible all -i inventory.ini -m command -a "ls-lah"
ansible all -i inventory.ini -m command -a "uname -rms"
ansible all -i inventory.ini -m command -a "free -m"
```

### Module setup trong Ansible

Ta có thể sử dụng module `setup` để kiểm tra các thông tin tổng quát về hệ điều hành của các node, ví dụ kiểm tra phiên bản, kiểm tra thông tin card mạng, tên host , thông số về phần cứng

Ví dụ ta có thể sử dụng lệnh sau để kiểm tra xem distro của các host là gì

```sh
ansible all -i inventory.ini -m setup -a "filter=ansible_distribution"
```

Kết quả của lệnh trên

```sh
asb-node02 | SUCCESS => {
    "ansible_facts": {
        "ansible_distribution": "CentOS",
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false
}
asb-node01 | SUCCESS => {
    "ansible_facts": {
        "ansible_distribution": "CentOS",
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false
}
asb-node03 | SUCCESS => {
    "ansible_facts": {
        "ansible_distribution": "Ubuntu",
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false
}
```

Hoặc 

```sh
ansible all -i inventory.ini -m setup -a "filter=all_ipv4_addresses"
```

Kết quả

```sh
asb-node02 | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "172.31.42.113"
        ],
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false
}
asb-node01 | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "172.31.41.73"
        ],
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false
}
asb-node03 | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "172.31.43.239"
        ],
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false
}
```

Tìm hiểu thêm về module `setup` tại đây https://docs.ansible.com/ansible/latest/collections/ansible/builtin/setup_module.html

