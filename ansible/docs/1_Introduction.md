# Ansible là gì?

Việc cài đặt cấu hình các máy chủ một cách thủ công trên từng thiết bị hoặc máy chủ qua CLI mất nhiều thời gian và nhân lực. Thông qua Ansible chúng ta có thể cài đặt môi trường một lúc trên nhiều thiết bị, server

- Ansible là một công cụ `automation` và `orchestration ` phổ biến, giúp cho chúng ta đơn giản tự động hóa việc triển khai ứng dụng. Nó có thể cấu hình hệ thống, deploy phần mềm 
- Ansible có thể tự động hóa việc cài đặt, cập nhật nhiều hệ thống hay triển khai ứng dụng từ xa

# Ưu điểm của Ansible 

- Clear: Ansible sử dụng cú pháp đơn giản (YAML) và dễ hiểu

- Fast: Cài đặt nhanh chóng không cẩn phải cài đặt phần mềm hay daemon nào khác trên server của chúng ta

- Complete: Chúng ta có mọi thứ chúng ta cần trong một package hoàn chỉnh

- Efficent: Việc không có phần mềm bổ sung trên máy chủ của chúng ta sẽ giúp chúng ta tiết kiệm tài nguyên và dành nhiều tài nguyên hơn cho các ứng dụng

- Secure: Ansible sử dụng SSH và không yêu cầu mở thêm port hoặc daemon nên tránh bị truy cập vào máy chủ thông qua port hoặc daemon

# Các thuật ngữ quan trọng của Ansible

- Ansible server: Là nơi được cài đặt và từ đó tất cả các tasks và playbooks sẽ được chạy 

- Module: Là một lệnh hoặc tập hợp các lệnh tương tự được thực thi ở client side. Khi chúng ta giao tiếp với Ansible sẽ thông qua module

- Task: Một task xác định một công việc đơn lẻ được hoành thành là những công việc nhỏ trong playbooks

- Role: Một tập hợp các playbook, các file liên quan được tổ chức theo cách được xác định để tạo điều kiện tái sự dụng và chia sẻ 
- Fact: Các biến toàn cục chứa các thông tin về hệ thống

- Playbook: Một file YAML chứa một tập các công việc cần tự động hóa

- Inventory: Một file INI hoặc YAML chứa các thông tin về các server từ xa mà bạn quản lý

- Play: Một lần thực thi một Playbook

- Handler: Sử dụng để kích hoạt thay đổi trạng thái các service

- Tag: Tên được gắn cho một task, có thể được sử dụng sau này có nhiệm vụ chỉ cụ thể task hoặc một nhóm các task

# Ansible hoạt động như thế nào?

![](/ansible/images/ansible.png)

- `Management Node` trong hình đóng vai trò là `Ansible Server`, là nơi quản lý cac nodes điều khiển toàn bộ quá trình thực thi của playbook

- `Playbook` sẽ chứa chi tiết tất cả những gì chúng ta muốn thực hiện với các server mà chúng ta muốn quản lý và cách thức thực hiện chúng

- `Inventory` cung cấp danh sách các máy chủ mà chúng ta cần quản lý

Sau khi đọc được các host mà chúng ta cần chạy ở file `Inventory` thì `Management Node` sẽ thực hiện việc connect tới các host này thông qua SSH connection và thực thi các modules

# Cài đặt Ansible

Cài đặt Ansible trên Ubuntu

```sh
sudo apt-add-repository ppa:ansible/ansible
```

```sh
sudo apt update
```

```sh
sudo apt install ansible -y
```

Kiểm tra ansible đã được cài đặt chưa bằng lệnh

```sh
ansible --version
```