# Thiết kế layout ổ cứng

## Cài đặt trên 1 ổ cứng duy nhất 

Linux được cài đặt trên một ổ cứng vật lý duy nhất, bao gồm một hoặc nhiều phân vùng (partition)

## Cài đặt trên nhiều ổ cứng

Linux được cài đặt trên nhiều ổ cứng vật lý, mỗi ổ cứng gồm 1 hoăc nhiều phân vùng 

## Quy ước đặt tên thiết bị (đối với ổ cứng SATA hoặc SCSI cục bộ)

- /dev/sda - ổ cứng vật lý đầu tiên 

- /dev/sda2 - ổ cứng vật lý đầu tiên, phân vùng thứ 2

## Các loại thiết bị khác

hda (ổ cứng IDE)

- /dev/hdc2 - ổ cứng IDE thứ 3 phân vùng thứ 2

scd (đĩa CDROM)

- /dev/scd0 (đĩa CDROM đầu tiên): Ổ đĩa CDROM không có phân cùng

## Bố cục hệ thống file (Linux filesystem layout) Linux

Mọi thứ trong Linux đều là một file

Măc dù bạn có nhiều file/thư mục, bất kỳ thư mục nào (với một số ngoại lệ) có thể được mount trên ổ đĩa/phần vùng nào

Lược đồ chung về gắn mount filesystem trong Linux

- `/`: filesystem gốc được gắn mount trên một thiết bị lưu trữ (vd: ổ cứng sata, IDE, SCSI, ...) phân vùng và chứa tất cả các thư mục khác (một số trong số đó thường được gắn mount trên các phân vùng hoặc ổ đĩa khác)

- `/var`: Các files log, files/thư mục chia sẻ (share), thông tin thời gian chạy, file dữ liệu nhị phân

- `/home`: Chứa thư mục home của người dùng users trong Linux

- `/opt`: Thường là nơi cài đặt ứng dụng, phần mềm thứ ba

- `/boot`: Chứa cấu hình của trình khởi động (boot loader) và các kernel files

- `/swap`: Phân vùng dành riêng cho bộ nhớ ảo (swap)

# LVM và Swap

LVM 

**Logical Volume Manager (Quản lý Logical Volume)**

- Cho phép tạo ra `nhóm` ổ đĩa hoặc phân vùng (partitions) có thể gom lại thành một hoặc nhiều filesystems

**Physical Volume(PV)**

- PV - đơn vị lưu trữ cơ bản

- PV tương ứng với một ổ đĩa hoặc phân vùng trên hệ thống Linux

	+ Có thể là cục bộ trên hệ thống (như /dev/sdb1) hoặc một thiết bị lưu trữ SAN (Storage area network)

**Volume Group(VG)**

- Kết hợp một hoặc nhiều PV để tạo thành 1 nhóm lưu trữ có sẵn

	+ PE - Physical Extents (Các đơn vị vật lý)

	+ Được sử dụng để phân chia dễ dàng không gian lưu trữ của một PV

**Logical Volume(Ổ đĩa Logic)**

- Mỗi nhóm ổ đĩa có thể được chia thành một hoặc nhiều Logical Volume, mỗi Logical Volume có thể được định dạng với một loại filesystem cụ thể và sau đó được mount vào hệ điều hành 

**Ưu điểm của LVM**

- Linh hoạt: Bạn có thể tăng kích cỡ của một Logical Volume, chỉ bằng cách điều chỉnh kích thước, lấy thêm dung lượng (space) từ nhóm ổ đĩa (volume group), nếu nhóm ổ đĩa đầy dữ liệu, bạn có thể cấp thêm ổ đĩa vật lý cho nhóm ổ đĩa và thiết đặt nó vào Logical Volumes

- Snapshots: Sao lưu trạng thái bất kỳ của Logical Volume nào có thể được sử dụng để sao lưu, khôi phục, kiểm tra, dịch chuyển... mà không có ảnh hưởng đến Logical Volume trực tiếp

**Swap (Bộ nhớ ảo)**

- Phần vùng swap - một phân vùng dành riêng được định dạng đặc biệt làm dung lượng lưu trữ cho swap (thường được thực hiện trong quá trình cài đặt, nhưng cũng có thể thêm bất cứ lúc nào bạn thêm ổ đĩa hoặc phân vùng)

- Files -file được tạo ra đặc biệt và được sử dụng trên filesystem để làm dung lượng cho swap

