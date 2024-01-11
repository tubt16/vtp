# Xác đinh cấu hình và cài đặt phần cứng

Linux coi tất cả các thiết bị phần cứng dưới dạng các file. Điều này có nghĩa là các thiết bị như ổ cứng, ổ đĩa CD/DVD, cổng USB, card mạng và các thiết bị khác được đại diện bởi các files trong hệ thống file của Linux

**Procfs:** Thông tin về phần cứng và tình trạng hoạt động của hệ thống trong Linux được chứa trong `pseudofilesystem` này

**proc:** 
- Thường là nơi mà `procfs` filesystem được gắn vào Linux

- Trong thư mục này bạn sẽ tìm thấy các thư mục tương ứng với nhãn số tương ứng với PID (Process ID) của các tiến trình đang chạy

- Ngoài ra, các files và thư mục khác chứa thông tin về hệ thống hoặc phần cứng trong đó bao gồm:
	+ /proc/mounts - một file (hoặc liên kết đến file khác) chứa thông tin về tất cả các filesystems được gắn vào hệ điều hành Linux

	+ /proc/interrupts - hiển thị thông tin về các (interrupts) được sử dụng trong hệ thống và thiết bị phần cứng được hiển thị dưới dạng files

	+ /proc/ioports - một hoặc nhiều địa chỉ xác định một thiết bị và module kernel liên kết đến chúng

	+ /proc/dma - (Direct Memory Access), các giá trị được sử dụng bởi phần cứng để truy cập trực tiếp vào bộ nhớ hệ thống (tức là không cần đến cpu)

	+ /proc/usb - Các ID thiết bị USB và module kernel liên kết đến chúng 

	+ /proc/pci - PCI và các IDs của các thiết bị và kernel modules liên kết đến chúng


**Sysfs:**

- Một 'pseudofilesystem' khác có thể chứa thông tin về phần cứng hệ thống (tương tự như procfs)

- Được thiết kế để giải quyết một số vấn đề với phương pháp procfs (dữ liệu không có
cấu trúc và thông tin về phần cứng và tiến trình được tổng hợp trong cùng một cấu trúc)

**udev:**

- Chương trình quản lý thiết bị cho kernel

- /dev: Thư mục chứa dữ liệu thiết bị

**D-Bus:**

- Liên quan đến hệ thống udev

- Cho phép các ứng dụng desktop gửi thông điệp tới các ứng dụng khác và/hoặc nhận thông điệp từ Linux kernel

# Xác định và cấu hình cài đặt phần cứng

**lsmod**

- Liệt kê các module kernel (drivers) đã được tải vào bộ nhớ (cùng với các thành phần phụ thuộc của chúng)

- Sẽ không tải một driver nếu nó bị thiếu

```sh
root@ubuntulpic:/etc/apt# lsmod
Module                  Size  Used by
ufs                    77824  0
msdos                  20480  0
xfs                  1204224  0
vboxsf                 45056  1
isofs                  45056  0
binfmt_misc            20480  1
crct10dif_pclmul       16384  0
crc32_pclmul           16384  0
ghash_clmulni_intel    16384  0
input_leds             16384  0
serio_raw              16384  0
vboxguest             294912  2 vboxsf
video                  53248  0
sch_fq_codel           20480  3
ib_iser                49152  0
rdma_cm                61440  1 ib_iser
iw_cm                  45056  1 rdma_cm
ib_cm                  53248  1 rdma_cm
ib_core               225280  4 rdma_cm,iw_cm,ib_iser,ib_cm
iscsi_tcp              20480  0
libiscsi_tcp           20480  1 iscsi_tcp
libiscsi               53248  3 libiscsi_tcp,iscsi_tcp,ib_iser
scsi_transport_iscsi    98304  3 iscsi_tcp,ib_iser,libiscsi
ip_tables              28672  0
x_tables               40960  1 ip_tables
autofs4                40960  2
btrfs                1159168  0
zstd_compress         163840  1 btrfs
raid10                 53248  0
raid456               147456  0
async_raid6_recov      20480  1 raid456
async_memcpy           16384  2 raid456,async_raid6_recov
async_pq               16384  2 raid456,async_raid6_recov
async_xor              16384  3 async_pq,raid456,async_raid6_recov
async_tx               16384  5 async_pq,async_memcpy,async_xor,raid456,async_raid6_recov
xor                    24576  2 async_xor,btrfs
raid6_pq              114688  4 async_pq,btrfs,raid456,async_raid6_recov
libcrc32c              16384  2 xfs,raid456
raid1                  40960  0
raid0                  20480  0
multipath              16384  0
linear                 16384  0
aesni_intel           188416  0
mptspi                 24576  1
aes_x86_64             20480  1 aesni_intel
crypto_simd            16384  1 aesni_intel
cryptd                 24576  3 crypto_simd,ghash_clmulni_intel,aesni_intel
glue_helper            16384  1 aesni_intel
psmouse               151552  0
scsi_transport_spi     32768  1 mptspi
mptscsih               40960  1 mptspi
mptbase               102400  2 mptspi,mptscsih
e1000                 143360  0
```

**lscpu**

Hiển thị một thông tin tổng kết về CPU và các tính năng/cấu hình của nó

- `-a` (hoặc --all): Sẽ hiển thị thông tin về CPU khi online và offline
- `-e` (hoặc --extended): Hiển thị thông tin dưới định dạng dễ đọc hơn
- `-p` (hoặc --parse): Cung cấp thông tin hiển thị dưới định dạng phân tách bằng dấu phẩy

**lspci**

Hiển thị thông tin về bus PCI và thiết bị liên quan được kết nối vào nó

Trong trường hợp kernel không nhận ra (hoặc không hỗ trợ theo mặc định) một thiết bị, nó sẽ xuất hiện ở đây và chứa thông tin (khe cắm, ID thiết bị, phạm vi bộ nhớ ...) có thể sử dụng để tìm kiếm driver/module thiết bị

- `-v`: Kiểm soát mức độ chi tiết của thông tin thiết bị

- `-m`: Hiển thị thông tin PCI dưới định dạng dễ phân tíhc

- `-vmm`: Hiển thị danh sách được định dạng đẹp về tất cả các thiết bị PCI trên
hệ thống

- `-t`: Hiển thị một cấu trúc cây của các thiết bị PCI trên hệ thống

**lsscsi**

Hiển thị thông tin về bất kỳ thiết bị SCSI nào được phát hiện 

- `-c` (hay --classic): Đầu ra tương tự với việc chay `cat /proc/scsi/scsi`

- `-d` (hay --device): Cung cấp số thiết bị bổ sung sau mỗi thiết bị được phát hiện

- `-g` (hay --generic): Tên file thiết bị SCSI chung (sg)

- `-l` (hay --long): 

- `-s` (hay --size): hiển thị kích thước ổ đĩa trong định dạng dễ đọc hơn

**lsdev**

Hiển thị tất cả các thiết bị được nhận dạng bởi kernel hệ thống Linux đang chạy

**lsraid**

Hiển thị các hệ thống RAID (Redundant Array of Inexpensive Disks) có trong hệ thống Linux của bạn

**lsusb**

Hiển thị các ID thiết bị USB và thông tin chung về các thiết bị được phát hiện

**lsblk**

Hiển thị các block devices (các ổ đĩa) được kết nối với hệ thống Linux đang chạy

`-a` (hoặc --all): Liệt kê các thiết bị trống, (mặc định là tắt)

`-d` (hoặc --nodeps): Chỉ in thông tin thiết bị cao nhất. Ví dụ: `lsblk--nodeps /dev/sdb` (Chỉ hiển thị thông tin trên ổ đĩa /dev/sdb)

`-e` (hoặc --exclude): Loại trừ các thiết bị chỉ định

`-i` (hoặc --ascii): Sử dụng ký tự ASCII cho chế độ xem dạng cây

`-f` (hoặc --fs): Bao gồm thông tin về filesystem

`-l` (hoặc --list): Định dạng danh sách đầu ra 

`-t` xem các thiết bị và phân vùng ở đĩa trong hệ điều hành dưới dạng cây

