# Triggers 

## Tổng quan

`Triggers` là các biểu thức logic ĐÁNH GIÁ dữ liệu được thu thập theo các `Items` và thể hiện trạng thái của hệ thống hiện tại

Măc dù các `Items` được sử dụng để thu thập dữ liệu hệ thống, nhưng việc theo dõi những dữ liệu này và đưa ra cảnh báo là công việc của `Triggers` với các biểu thức chính quy 

Biểu thức kích hoạt cho phép xác định ngưỡng trạng thái "Có thể chấp nhận được". Do đó, nếu dữ liệu vượt qua trạng thái có thể chấp nhận được thì `Trigger` sẽ được "kích hoạt" và thay đổi state của cảnh báo thành `PROBLEM`

Một `Triggers` có thể có các trạng thái sau:

|State|Description|
|---|---|
|OK|Đây là trạng thái bình thường của Trigger|
|Problem|Có sự cố gì đã xảy ra, Ví dụ: CPU load cao trong 10m|
|Unknown|Không thể tính toán giá trị kích hoạt|

Trigger state (biểu thức): được tính toán lại mỗi khi Zabbix-server nhận được một giá trị mới là 1 phần của biểu thức

**Unknown state**

Có thể có một toán hạng không xác định xuất hiện trong Trigger nếu:

- Một `Item` không được hỗ trợ được sử dụng 

- Việc đánh giá chức năng cho một `Item` dẫn đến lỗi

Trong trường hợp này `Trigger` thường có giá trị là "không xác định" 

## Tạo một Trigger

Để tạo một Trigger ta làm như sau:

Đi tới `Configuration` -> `Hosts`

![](/zabbix/images/triggers1.png)

Nhấn vào `Triggers` ở host cần tạo

![](/zabbix/images/triggers2.png)

Nhấn vào `Create trigger` ở góc phải màn hình

![](/zabbix/images/triggers3.png)

Nhập các tham số của `Trigger`vào biểu mẫu

Ở trên mình tạo một `Trigger` cảnh báo khi đầy ổ

Chúng ta sẽ thực hiện tạo một file chiếm dung lượng làm cho server của chúng ta đầy ổ để xem `Trigger` có đang hoạt động hay không

Login vào server và kiểm tra Disk space

```sh
root@buitu:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        20G  2.7G   17G  14% /
devtmpfs        977M     0  977M   0% /dev
tmpfs           981M     0  981M   0% /dev/shm
tmpfs           197M  980K  196M   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           981M     0  981M   0% /sys/fs/cgroup
/dev/loop0       64M   64M     0 100% /snap/core20/2015
/dev/loop1      341M  341M     0 100% /snap/google-cloud-cli/171
/dev/loop2       92M   92M     0 100% /snap/lxd/24061
/dev/loop3       41M   41M     0 100% /snap/snapd/20092
/dev/sda15      105M  6.1M   99M   6% /boot/efi
tmpfs           197M     0  197M   0% /run/user/0
```

Như vậy Disk space còn lại là khoảng 17GB. Chúng ta sẽ lệnh `fallocate` để phân bổ trước dung lượng cho một tệp

Thực hiện tạo file có tên là `tubt.txt` và gán cho nó 16GB

```sh
fallocate -l 16G tubt.txt
```

Kiểm tra lại Disk space của hệ thống

```sh
root@buitu:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        20G   19G  565M  98% /
devtmpfs        977M     0  977M   0% /dev
tmpfs           981M     0  981M   0% /dev/shm
tmpfs           197M  980K  196M   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           981M     0  981M   0% /sys/fs/cgroup
/dev/loop0       64M   64M     0 100% /snap/core20/2015
/dev/loop1      341M  341M     0 100% /snap/google-cloud-cli/171
/dev/loop2       92M   92M     0 100% /snap/lxd/24061
/dev/loop3       41M   41M     0 100% /snap/snapd/20092
/dev/sda15      105M  6.1M   99M   6% /boot/efi
tmpfs           197M     0  197M   0% /run/user/0
```

Sau khi tạo file xong. Mức sử dụng Disk space đã lên đến 98%. Chúng ta mở Zabbix frontend đẻ check cảnh báo xem Trigger vừa tạo đã hoạt động hay chưa

![](/zabbix/images/triggers4.png)

Trên Zabbix frontend đã xuất hiện cảnh báo, vậy là Trigger vùa tạo đã hoạt động, ta thực hiện xóa file `tubt.txt` sau đó kiểm tra xem trạng thái của Trigger có chuyển từ `PROBLEM` về `RESOLVED` hay không

```sh
root@buitu:~# rm -rf tubt.txt 
```

![](/zabbix/images/triggers5.png)

Trigger state đã chuyển về `RESOLVED`. Như vậy Trigger chúng ta tạo đã hoạt động