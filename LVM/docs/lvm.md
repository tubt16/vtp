# Logical Volume Manager

Logical Volume Manager (LVM) đã có sẵn trên hầu hết tất cả các bản phân phối Linux, có nhiều lợi thế so với quản lý phân vùng truyền thống. Logical Volume Management được sử dụng để tạo nhiều ổ đĩa logic

Nó cho phép các bộ phận logic được thay đổi kích thước (giảm hoặc tăng) theo ý muốn của người quản trị

Cấu trúc của LVM bao gồm:

- Một hoặc nhiều đĩa cứng hoặc phân vùng được định cấu hình là physical volume (PV)

- Một volume group (VG) được tạo bằng cách sử dụng một hoặc nhiều khối vật lý

- Nhiều logical volume có thể được tạo trong một volume group

# Các bước để quản lý và tạo LVM bằng các lệnh vgcreate, lvcreate và lvextend

## Tạo Physical Volume , Volume Group và Logical Volume

**Tạo Physical Volume**

Chạy lệnh sau để tạo Physical Volume (PV) trên `/dev/sdb`, `/dev/sdc` và `/dev/sdd`

```sh
root@linux-lab:~# pvcreate /dev/sdb /dev/sdc /dev/sdd
  Physical volume "/dev/sdb" successfully created.
  Physical volume "/dev/sdc" successfully created.
  Physical volume "/dev/sdd" successfully created.
```

Để liệt kê các physical volume (PV) mới được tạo, chạy như sau:

```sh
root@linux-lab:~# pvs
  PV         VG Fmt  Attr PSize  PFree 
  /dev/sdb      lvm2 ---  15.00g 15.00g
  /dev/sdc      lvm2 ---  20.00g 20.00g
  /dev/sdd      lvm2 ---  10.00g 10.00g
```

Ý nghĩa các trường của `pvs`:

- `PV`: Đĩa sử dụng

- `PSize`: Kích thước đĩa vật lý (Kích thước PV)

- `PFree`: Kích thước còn trống của đĩa vật lý

Để có được thông tin chi tiết về mỗi physical volume (PV), sử dụng lệnh sau `pvdisplay`

Xem chi tiết về physical volume (PV) `/dev/sdb`. Chúng ta thực hiện như sau:

```sh
root@linux-lab:~# pvdisplay /dev/sdb
  "/dev/sdb" is a new physical volume of "15.00 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/sdb
  VG Name               
  PV Size               15.00 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               bbf2Q4-AiZc-aJ9r-qYPM-ubk0-JHgZ-EKOtGh
```

Lưu ý: Nếu chúng ta có 2 ổ đĩa hay nhiều ổ đĩa để tạo một volume mà một ổ đĩa ở volume bị mất thì dẫn tới volume đó mất luôn, vì thế phải chạy LVM trên RAID hoặc dùng tính năng RAID của LVM để có khả năng dung lỗi

**Tạo Volume Group**

Để tạo volume group với tên `vg0` bằng cách sử dụng `/dev/sdb` và `/dev/sdc`. Chúng ta thực hiện như sau

```sh
root@linux-lab:~# vgcreate vg0 /dev/sdb /dev/sdc
  Volume group "vg0" successfully created
```

Thực hiện lệnh sau để xem thông tin volume group vừa tạo:

```sh
root@linux-lab:~# vgdisplay vg0
  --- Volume group ---
  VG Name               vg0
  System ID             
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               34.99 GiB
  PE Size               4.00 MiB
  Total PE              8958
  Alloc PE / Size       0 / 0   
  Free  PE / Size       8958 / 34.99 GiB
  VG UUID               17A1QN-q6ET-ZdVe-dqFT-vWWA-Cg7k-BC2xVv
```

Vì `vg0` chứa 2 đĩa 15GB và 20GB nên VG Size = 34.99GB

Ý nghĩa của các trường thông tin của Volume Group khi chạy lệnh `vgdisplay`:

- `VG Name`: Tên Volume Group

- `Format`: Kiến trúc LVM được sử dụng

- `VG Access`: Volume Group có thể đọc, viết và sẵn sàng được sử dụng

- `VG Status`: Volume Group có thể được thay đổi kích cỡ, chúng ta có thể mở rộng thêm nếu cần thêm dung lượng

- `PE Size`: Mở rộng Physical, kích thước cho đĩa có thể được xác định bằng kích thước PE hoặc GB, 4MB là kích thước PE mặc định của LVM

- `Total PE`: Dung lượng Volume Group có

- `Alloc PE`: Tổng PE đã sử dụng

- `Free PE`: Tổng PE chưa sử dụng

Chúng ta có thể kiểm tra số lượng Physical Volume (PV) dùng để tạo Volume Group như sau:

```sh
root@linux-lab:~# vgs
  VG  #PV #LV #SN Attr   VSize  VFree 
  vg0   2   0   0 wz--n- 34.99g 34.99g
```

Trong đó:

- `VG`: Tên Volume Group

- `#PV`: Physical Volume sử dụng trong Volume Group

- `VFree`: Hiển thị không gian trống có sẵn trong Volume Group

- `VSize`: Tổng kích thước của Volume Group

- `#LV`: Logical Volume nằm trong Volume Group

- `#SN`: Số lượng Snapshot của Volume Group

- `Attr`: Trạng thái của Volume group có thể ghi, có thể đọc, có thể thay đổi

Khi tạo ra các Logical Volume , chúng ta cần phải xem xét dung lượng khi tạo Logical Volume sao cho phù hợp với nhu cầu sử dụng

**Tạo Logical Volume**

Chúng ta sẽ tạo 2 logical volume với tên `projects` có dung lượng là 10GB và `backups` sử dụng toàn bộ dung lượng còn lại của volume group . Chúng ta sử dụng lệnh sau:

```sh
root@linux-lab:~# lvcreate -n projects -L 10G vg0
  Logical volume "projects" created.

root@linux-lab:~# lvcreate -n backups -l 100%FREE vg0
  Logical volume "backups" created.
```

Trong đó:

- `-n`: Sử dụng chỉ ra tên của logical volume cần tạo

- `-L`: Sử dụng chỉ một kích thước cố định

- `-l`: Sử dụng chỉ phần trăm của không gian còn lại trong volume group

Chạy lệnh sau để xem danh sách Logical Volume vừa tạo:

```sh
root@linux-lab:~# lvs
  LV       VG  Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  backups  vg0 -wi-a----- 24.99g                                                    
  projects vg0 -wi-a----- 10.00g
```

Ý nghĩa các trường của `lvs`: 

- `LV`: Tên Logical Volume

- `%DATA`: Phần trăm dung lượng Logical Volume được sử dụng 

- `Lsize`: Kích thước của Logical Volume 

Sử dụng lệnh sau để hiển thị thông tin chi tiết của các Logical Volume

```sh
root@linux-lab:~# lvdisplay vg0/projects
  --- Logical volume ---
  LV Path                /dev/vg0/projects
  LV Name                projects
  VG Name                vg0
  LV UUID                FRQMCZ-ocJw-YtSz-tCUW-cjtq-3Kgy-3jHOpY
  LV Write Access        read/write
  LV Creation host, time linux-lab, 2023-09-20 08:52:31 +0000
  LV Status              available
  # open                 0
  LV Size                10.00 GiB
  Current LE             2560
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:0
   
root@linux-lab:~# lvdisplay vg0/backups
  --- Logical volume ---
  LV Path                /dev/vg0/backups
  LV Name                backups
  VG Name                vg0
  LV UUID                Djx6fe-DSSx-TPjS-nnYV-oSGg-fV0v-JXryaf
  LV Write Access        read/write
  LV Creation host, time linux-lab, 2023-09-20 08:53:13 +0000
  LV Status              available
  # open                 0
  LV Size                24.99 GiB
  Current LE             6398
  Segments               2
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:1
```

Chúng ta sẽ sử dụng file system `ext4` vì nó cho phép chúng ta tăng và giảm kích thước của mỗi Logical Volume (Đối với file system `xfs` chỉ cho phép tăng kích thước). Chúng ta thực hiện như sau:

```sh
root@linux-lab:~# mkfs.ext4 /dev/vg0/projects 
mke2fs 1.45.5 (07-Jan-2020)
Discarding device blocks: done                            
Creating filesystem with 2621440 4k blocks and 655360 inodes
Filesystem UUID: 63128812-5914-4c7f-9fc0-207b8a65831d
Superblock backups stored on blocks: 
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done 

root@linux-lab:~# mkfs.ext4 /dev/vg0/backups 
mke2fs 1.45.5 (07-Jan-2020)
Discarding device blocks: done                            
Creating filesystem with 6551552 4k blocks and 1638400 inodes
Filesystem UUID: a64d4c6b-d6cd-445a-82cb-4f77b04f1f29
Superblock backups stored on blocks: 
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
        4096000

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information: done  
```

## Mở rộng Volume Group và thay đổi kích thước các Logical Volume

Trong ví dụ dưới đây chúng ta sẽ thêm một Physical Volume có tên `/dev/sdd` với kích thước 10GB vào Volume Group `vg0`, sau đó chúng ta sẽ tăng kích thước của Logical Volume `/projects` lên `10GB`, thực hiện như sau:

Chạy các lệnh sau để mount

```sh
root@linux-lab:~# mkdir backups
root@linux-lab:~# mkdir projects
root@linux-lab:~# mount /dev/vg0/backups /root/backups/
root@linux-lab:~# mount /dev/vg0/projects /root/projects/
```

Chạy lệnh sau để kiểm tra sử dụng không gian đĩa của hệ thống tập tin

```sh
root@linux-lab:~# df -TH
Filesystem               Type      Size  Used Avail Use% Mounted on
/dev/root                ext4       21G  2.1G   19G  10% /
devtmpfs                 devtmpfs  1.1G     0  1.1G   0% /dev
tmpfs                    tmpfs     1.1G     0  1.1G   0% /dev/shm
tmpfs                    tmpfs     206M  975k  205M   1% /run
tmpfs                    tmpfs     5.3M     0  5.3M   0% /run/lock
tmpfs                    tmpfs     1.1G     0  1.1G   0% /sys/fs/cgroup
/dev/loop0               squashfs   67M   67M     0 100% /snap/core20/2015
/dev/loop2               squashfs   97M   97M     0 100% /snap/lxd/24061
/dev/loop1               squashfs  358M  358M     0 100% /snap/google-cloud-cli/171
/dev/loop3               squashfs   43M   43M     0 100% /snap/snapd/20092
/dev/sda15               vfat      110M  6.4M  104M   6% /boot/efi
tmpfs                    tmpfs     206M     0  206M   0% /run/user/0
/dev/mapper/vg0-backups  ext4       27G   25k   25G   1% /root/backups
/dev/mapper/vg0-projects ext4       11G   25k   10G   1% /root/projects
```

Sử dụng lệnh sau để thêm `/dev/sdd` vào volume group `vg0`:

```sh
root@linux-lab:~# vgextend vg0 /dev/sdd 
  Volume group "vg0" successfully extended
```

Chúng ta chạy lệnh `vgdisplay vg0` trước và sau khi thực hiện lệnh `vgextend vg0 /dev/sdd`, bạn sẽ thấy sự tăng kích thước của Volume Group (VG)

**Trước khi chạy lệnh `vgextend vg0 /dev/sdd`**

```sh
root@linux-lab:~# vgdisplay vg0
  --- Volume group ---
  VG Name               vg0
  System ID             
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               34.99 GiB
  PE Size               4.00 MiB
  Total PE              8958
  Alloc PE / Size       0 / 0   
  Free  PE / Size       8958 / 34.99 GiB
  VG UUID               17A1QN-q6ET-ZdVe-dqFT-vWWA-Cg7k-BC2xVv
```

Sau khi chạy lệnh `vgextend vg0 /dev/sdd`

```sh
root@linux-lab:~# vgdisplay vg0
  --- Volume group ---
  VG Name               vg0
  System ID             
  Format                lvm2
  Metadata Areas        3
  Metadata Sequence No  6
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                2
  Open LV               2
  Max PV                0
  Cur PV                3
  Act PV                3
  VG Size               <44.99 GiB
  PE Size               4.00 MiB
  Total PE              11517
  Alloc PE / Size       8958 / 34.99 GiB
  Free  PE / Size       2559 / <10.00 GiB
  VG UUID               17A1QN-q6ET-ZdVe-dqFT-vWWA-Cg7k-BC2xVv
```

Qua lệnh kiểm tra trên chúng ta thấy dung lượng thêm vào của chúng ta là 10G, chúng ta có thể tăng kích thước của Logical Volume `/projects` lên 10GB như sau:

```sh
root@linux-lab:~# lvextend -l +2000 /dev/vg0/projects
  Size of logical volume vg0/projects changed from 10.00 GiB (2560 extents) to 17.81 GiB (4560 extents).
  Logical volume vg0/projects successfully resized.
```

Sau khi chạy lệnh trên chúng ta cần thay đổi kích thước hệ thống tệp, vì thế chúng ta phải chạy lệnh sau để resize:

- Đối với file system (ext2, ext3, ext4): `resize2fs`

- Đối với file system (xfs): `xfs_growfs`

```sh
root@linux-lab:~# resize2fs /dev/vg0/projects 
resize2fs 1.45.5 (07-Jan-2020)
Filesystem at /dev/vg0/projects is mounted on /root/projects; on-line resizing required
old_desc_blocks = 2, new_desc_blocks = 3
The filesystem on /dev/vg0/projects is now 4669440 (4k) blocks long.
```

Kiểm tra lại 

```sh
root@linux-lab:~# df -TH
Filesystem               Type      Size  Used Avail Use% Mounted on
/dev/root                ext4       21G  2.1G   19G  10% /
devtmpfs                 devtmpfs  1.1G     0  1.1G   0% /dev
tmpfs                    tmpfs     1.1G     0  1.1G   0% /dev/shm
tmpfs                    tmpfs     206M  975k  205M   1% /run
tmpfs                    tmpfs     5.3M     0  5.3M   0% /run/lock
tmpfs                    tmpfs     1.1G     0  1.1G   0% /sys/fs/cgroup
/dev/loop0               squashfs   67M   67M     0 100% /snap/core20/2015
/dev/loop2               squashfs   97M   97M     0 100% /snap/lxd/24061
/dev/loop1               squashfs  358M  358M     0 100% /snap/google-cloud-cli/171
/dev/loop3               squashfs   43M   43M     0 100% /snap/snapd/20092
/dev/sda15               vfat      110M  6.4M  104M   6% /boot/efi
tmpfs                    tmpfs     206M     0  206M   0% /run/user/0
/dev/mapper/vg0-backups  ext4       27G   25k   25G   1% /root/backups
/dev/mapper/vg0-projects ext4       19G   25k   18G   1% /root/projects
```

**Giảm kích cỡ Logical Volume**

Khi chúng ta muốn giảm kích cỡ các Logical Volume. Chúng ta cần phải chú ý vì nó rất quan trọng và có thể bị lỗi trong khi chúng ta giảm dung lượng Logical Volume. Để đảm bảo an toằn khi giảm Logical Volume cần thực hiện các bước sau:

- Trước khi bắt đầu, cần sao lưu dữ liệu

- Để giảm dung lượng volume, cần thực hiện đầy đủ và cẩn thận 5 bước cần thiết

- Khi giảm dung lượng Logical Volume chúng ta phải ngắt kết nối hệ thống tệp trước khi giảm

Cần thực hiện 5 bước dưới đây:

- Ngắt kết nối file system 

- Kiểm tra file system sau khi ngắt kết nối 

- Giảm file system 

- Giảm kích thước Logical Volume hơn kích thước hiện tại

- Kiểm tra lỗi cho file system 

- Mount lại file system và kiểm tra kích thước của nó

**Ví dụ:** Giảm Logical Volume có tên `projects` với kích thước 17.81 GB giảm xuống còn 10GB mà không làm mất dữ liệu. Chúng ta thực hiện các bước sau:

Kiểm tra dung lượng của Logical Volume và kiểm tra file system trước khi thực hiện giảm:

```sh
root@linux-lab:~# lvs
  LV       VG  Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  backups  vg0 -wi-ao---- 24.99g                                                    
  projects vg0 -wi-ao---- 17.81g                                                    
root@linux-lab:~# df -TH
Filesystem               Type      Size  Used Avail Use% Mounted on
/dev/root                ext4       21G  2.1G   19G  10% /
devtmpfs                 devtmpfs  1.1G     0  1.1G   0% /dev
tmpfs                    tmpfs     1.1G     0  1.1G   0% /dev/shm
tmpfs                    tmpfs     206M  975k  205M   1% /run
tmpfs                    tmpfs     5.3M     0  5.3M   0% /run/lock
tmpfs                    tmpfs     1.1G     0  1.1G   0% /sys/fs/cgroup
/dev/loop0               squashfs   67M   67M     0 100% /snap/core20/2015
/dev/loop2               squashfs   97M   97M     0 100% /snap/lxd/24061
/dev/loop1               squashfs  358M  358M     0 100% /snap/google-cloud-cli/171
/dev/loop3               squashfs   43M   43M     0 100% /snap/snapd/20092
/dev/sda15               vfat      110M  6.4M  104M   6% /boot/efi
tmpfs                    tmpfs     206M     0  206M   0% /run/user/0
/dev/mapper/vg0-backups  ext4       27G   25k   25G   1% /root/backups
/dev/mapper/vg0-projects ext4       19G   25k   18G   1% /root/projects
```

Bước 1: Unount file system

Sử dụng lệnh `umount` như bên dưới

```sh
root@linux-lab:~# umount /root/projects 
root@linux-lab:~# df -TH
Filesystem              Type      Size  Used Avail Use% Mounted on
/dev/root               ext4       21G  2.1G   19G  10% /
devtmpfs                devtmpfs  1.1G     0  1.1G   0% /dev
tmpfs                   tmpfs     1.1G     0  1.1G   0% /dev/shm
tmpfs                   tmpfs     206M  975k  205M   1% /run
tmpfs                   tmpfs     5.3M     0  5.3M   0% /run/lock
tmpfs                   tmpfs     1.1G     0  1.1G   0% /sys/fs/cgroup
/dev/loop0              squashfs   67M   67M     0 100% /snap/core20/2015
/dev/loop2              squashfs   97M   97M     0 100% /snap/lxd/24061
/dev/loop1              squashfs  358M  358M     0 100% /snap/google-cloud-cli/171
/dev/loop3              squashfs   43M   43M     0 100% /snap/snapd/20092
/dev/sda15              vfat      110M  6.4M  104M   6% /boot/efi
tmpfs                   tmpfs     206M     0  206M   0% /run/user/0
/dev/mapper/vg0-backups ext4       27G   25k   25G   1% /root/backups
```

Bước 2: Kiểm tra lỗi file system bằng lệnh `e2fsck`

```sh
root@linux-lab:~# e2fsck -f /dev/vg0/projects 
e2fsck 1.45.5 (07-Jan-2020)
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
/dev/vg0/projects: 11/1171456 files (0.0% non-contiguous), 101189/4669440 blocks
```

Trong đó tùy chọn `-f` dùng để kiểm tra (force check)

Bước 3: Giảm kích thước của `projects` theo kích thước mong muốn

Giảm Logical Volume có tên `projects` với kích thước từ 17.81 GB giảm xuống còn 10GB chúng ta thực hiện như sau:

```sh
root@linux-lab:~# resize2fs /dev/vg0/projects 10G
resize2fs 1.45.5 (07-Jan-2020)
Resizing the filesystem on /dev/vg0/projects to 2621440 (4k) blocks.
The filesystem on /dev/vg0/projects is now 2621440 (4k) blocks long.
```

Bước 4: Bây giờ giảm kích thước bằng lệnh `lvreduce`

```sh
root@linux-lab:~# lvreduce -L 10G /dev/vg0/projects 
  WARNING: Reducing active logical volume to 10.00 GiB.
  THIS MAY DESTROY YOUR DATA (filesystem etc.)
Do you really want to reduce vg0/projects? [y/n]: y
  Size of logical volume vg0/projects changed from 17.81 GiB (4560 extents) to 10.00 GiB (2560 extents).
  Logical volume vg0/projects successfully resized.
```

Bước 5: Để đảm bảo an toàn, bây giờ ta cần kiểm tra lỗi file system đã giảm

```sh
root@linux-lab:~# e2fsck -f /dev/vg0/projects 
e2fsck 1.45.5 (07-Jan-2020)
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
/dev/vg0/projects: 11/655360 files (0.0% non-contiguous), 66753/2621440 blocks
```

Bước 6: Mount lại file system và kiểm tra kích thước của nó

```sh
root@linux-lab:~# mount /dev/vg0/projects /root/projects/
root@linux-lab:~# df -TH
Filesystem               Type      Size  Used Avail Use% Mounted on
/dev/root                ext4       21G  2.1G   19G  10% /
devtmpfs                 devtmpfs  1.1G     0  1.1G   0% /dev
tmpfs                    tmpfs     1.1G     0  1.1G   0% /dev/shm
tmpfs                    tmpfs     206M  975k  205M   1% /run
tmpfs                    tmpfs     5.3M     0  5.3M   0% /run/lock
tmpfs                    tmpfs     1.1G     0  1.1G   0% /sys/fs/cgroup
/dev/loop0               squashfs   67M   67M     0 100% /snap/core20/2015
/dev/loop2               squashfs   97M   97M     0 100% /snap/lxd/24061
/dev/loop1               squashfs  358M  358M     0 100% /snap/google-cloud-cli/171
/dev/loop3               squashfs   43M   43M     0 100% /snap/snapd/20092
/dev/sda15               vfat      110M  6.4M  104M   6% /boot/efi
tmpfs                    tmpfs     206M     0  206M   0% /run/user/0
/dev/mapper/vg0-backups  ext4       27G   25k   25G   1% /root/backups
/dev/mapper/vg0-projects ext4       11G   25k   10G   1% /root/projects
```

## Mounting Logical Volume 

Chúng ta cần phải gắn kết vĩnh viễn ngay cả khi khởi động lại hệ thống. Để thực hiện gắn kết vĩnh viễn phải nhập trong tệp `/etc/fstab`. Ta có thể sử dụng trình soạn thảo `vi` để thêm vào:

Thực hiện mount vĩnh viễn trong tệp `/etc/fstab`

```sh
root@linux-lab:~# cat /etc/fstab 
LABEL=cloudimg-rootfs   /        ext4   defaults        0 1
LABEL=UEFI      /boot/efi       vfat    umask=0077      0 1

UUID=63128812-5914-4c7f-9fc0-207b8a65831d /backups ext4 defaults 0 0
UUID=a64d4c6b-d6cd-445a-82cb-4f77b04f1f29 /projects ext4 defaults 0 0
```

Để xác định UUID trên mỗi đĩa. Chúng ta chạy lệnh sau:

```sh
root@linux-lab:~# blkid /dev/vg0/projects
/dev/vg0/projects: UUID="63128812-5914-4c7f-9fc0-207b8a65831d" TYPE="ext4"

root@linux-lab:~# blkid /dev/vg0/backups
/dev/vg0/backups: UUID="a64d4c6b-d6cd-445a-82cb-4f77b04f1f29" TYPE="ext4"
```

Lưu lại file `/etc/fstab` và chạy lệnh sao lưu các thay đổi và mount Logical Volume

```sh
root@linux-lab:~# mount -a
root@linux-lab:~# mount | grep projects
/dev/mapper/vg0-projects on /projects type ext4 (rw,relatime)

root@linux-lab:~# mount | grep backups
/dev/mapper/vg0-backups on /backups type ext4 (rw,relatime)
```

# Snapshot và restore của Logical Volume 

## Snapshot Logical Volume

**Tạo snapshot LVM**

Trước khi tạo snapshot chúng ta kiểm tra `/dev/vg0/projects`:

```sh
root@linux-lab:~# cd /projects/
root@linux-lab:/projects# ls -l
total 996376
-rw-r--r-- 1 root root 1020264448 Nov  3  2020 CentOS-7-x86_64-Minimal-2009.iso
drwx------ 2 root root      16384 Sep 25 01:33 lost+found
-rw-r--r-- 1 root root         13 Sep 25 02:21 tubt.txt
root@linux-lab:/projects# cat tubt.txt 
Bui Thanh Tu
```

Kiểm tra không gian trong Volume Group để tạo snapshot mới chúng ta thực hiện như sau:

```sh
root@linux-lab:/projects# vgs
  VG  #PV #LV #SN Attr   VSize   VFree  
  vg0   3   2   0 wz--n- <44.99g <15.00g
root@linux-lab:/projects# lvs
  LV       VG  Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  backups  vg0 -wi-ao---- 19.99g                                                    
  projects vg0 -wi-ao---- 10.00g
```

Qua lệnh kiểm tra trên chúng ta thấy hiện có 15GB trống còn lại. Vì vậy, tạo một snapshot có tên là `snap_1` với dung lượng 2GB bằng lệnh sau

```sh
root@linux-lab:/projects# lvcreate -L 2GB -s -n snap_1 /dev/vg0/projects
  Logical volume "snap_1" created.
```

Trong đó ý nghĩa các tùy chọn là:

- `-s` - (snap): Tạo snapshot

- `-n` - (name): Tên cho snapshot

Tương tự chúng ta tạo một snapshot có tên là `snap_2` với dung lượng 1GB

```sh
root@linux-lab:/projects# lvcreate -L 1GB -s -n snap_2 /dev/vg0/projects
  Logical volume "snap_2" created.
```

Nếu muốn xóa snapshot, ta có thể sử dụng lệnh `lvremove`

```sh
root@linux-lab:/projects# lvremove /dev/vg0/snap_2 
Do you really want to remove and DISCARD active logical volume vg0/snap_2? [y/n]: y
  Logical volume "snap_2" successfully removed
```

Kiểm tra lại snapshot vừa tạo

```sh
root@linux-lab:/projects# lvs
  LV       VG  Attr       LSize  Pool Origin   Data%  Meta%  Move Log Cpy%Sync Convert
  backups  vg0 -wi-ao---- 19.99g                                                      
  projects vg0 owi-aos--- 10.00g                                                      
  snap_1   vg0 swi-a-s---  2.00g      projects 0.01  
```

Chúng ta sẽ thêm một số tệp mới vào `/dev/vg0/projects` với dung lượng tệp khoảng 975MB và kích thước snapshot của chúng ta là 2GB. Vì vậy, có đủ không gian để sao lưu các thay đổi của chúng ta. Chúng ta thực hiện lệnh bên dưới để kiểm tra:

```sh
root@linux-lab:/projects# du -sh /projects/
975M    /projects/
```

```sh
root@linux-lab:/projects# lvs
  LV       VG  Attr       LSize  Pool Origin   Data%  Meta%  Move Log Cpy%Sync Convert
  backups  vg0 -wi-ao---- 19.99g                                                      
  projects vg0 owi-aos--- 10.00g                                                      
  snap_1   vg0 swi-a-s---  2.00g      projects 47.81 
```

Qua việc kiểm tra trên chúng ta thấy 47.81% dung lượng snapshot đã được sử dụng. Để biết thêm thông tin chi tiết chúng ta chạy lệnh sau:

```sh
root@linux-lab:/projects# lvdisplay /dev/vg0/snap_1 
  --- Logical volume ---
  LV Path                /dev/vg0/snap_1
  LV Name                snap_1
  VG Name                vg0
  LV UUID                dVLCq3-5PCX-ewfr-M0gz-ECIc-Lhm8-9ZEtYz
  LV Write Access        read/write
  LV Creation host, time linux-lab, 2023-09-25 02:32:03 +0000
  LV snapshot status     active destination for projects
  LV Status              available
  # open                 0
  LV Size                10.00 GiB
  Current LE             2560
  COW-table size         2.00 GiB
  COW-table LE           512
  Allocated to snapshot  47.81%
  Snapshot chunk size    4.00 KiB
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:4
```

Trong đó ý nghĩa các trường của lệnh `lvdisplay` như sau:

- `LV Name`: Tên của Snapshot Logical Volume

- `VG Name`: Tên Volume group đang được sử dụng

- `LV Write Access`: Snapshot Volume ở chế độ đọc và ghi

- `LV Creation host, time`: Thời gian Snapshot được tạo. Nó rất quan trọng vì snapshot sẽ tìm và lưu lại mọi thay đổi sau thời gian này

- `LV snapshot status`: Snapshot này thuộc vào logical volume `projects`

- `LV Size`: Kích thước của Source volume mà bạn đã snapshot

- `COW-table size`: Kích thước bản Cow

- `Snapshot chunk size`: Cung cấp kích thước của chunk cho snapshot

Nếu chúng ta có Source Volume kích thước là 10GB thì chúng ta cũng nên tạo snapshot có dung lượng 10GB để đủ không gian chứa các thay đổi của Source Volume

**Lưu ý: Dung lượng Snapshot tăng lên đúng bằng dung lượng tạo mới trên LV. Không thể tạo Snapshot mới ghi đè lên Snapshot cũ. Trường hợp bạn có 2 Snapshot cho cùng 1 ổ LV thì dữ liệu mới cũng sẽ được ghi cả vào 2 ổ Snapshot**

**Tăng dung lượng snapshot trong LVM**

Chúng ta cần mở rộng kích thước của snapshot, chúng ta có thể thực hiện bằng cách sử dụng:

```sh
root@linux-lab:/backups# lvextend -L +2GB /dev/vg0/snap_1 
  Size of logical volume vg0/snap_1 changed from 2.00 GiB (512 extents) to 4.00 GiB (1024 extents).
  Logical volume vg0/snap_1 successfully resized.
```

Sau khi thực thi lệnh trên thì snapshot có kích thước 4GB

Tiếp theo, kiểm tra kích thước và bảng COW bằng lệnh sau:

```sh
root@linux-lab:/backups# lvdisplay /dev/vg0/snap_1 
  --- Logical volume ---
  LV Path                /dev/vg0/snap_1
  LV Name                snap_1
  VG Name                vg0
  LV UUID                dVLCq3-5PCX-ewfr-M0gz-ECIc-Lhm8-9ZEtYz
  LV Write Access        read/write
  LV Creation host, time linux-lab, 2023-09-25 02:32:03 +0000
  LV snapshot status     active destination for projects
  LV Status              available
  # open                 0
  LV Size                10.00 GiB
  Current LE             2560
  COW-table size         4.00 GiB
  COW-table LE           1024
  Allocated to snapshot  23.90%
  Snapshot chunk size    4.00 KiB
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           253:4
```

Qua lệnh kiểm tra chúng ta thấy `COW-table size` nó chính là kích thước bảng COW và kích thước bảng cow đã tăng lên 2GB so với kích thước khi chạy lệnh `lvextend`

Bây giờ sau khi tăng dung lượng chúng ta thực hiển chỉnh sửa 1 tệp có tên là `tubt.txt` trong `/dev/vg0/projects`

```sh
root@linux-lab:~# cd /projects/
root@linux-lab:/projects# ls -l
total 997888
-rw-r--r-- 1 root root 1020264448 Nov  3  2020 CentOS-7-x86_64-Minimal-2009.iso
drwx------ 2 root root      16384 Sep 25 01:33 lost+found
-rw-r--r-- 1 root root         13 Sep 25 02:21 tubt.txt
-rw-r--r-- 1 root root    1547178 Sep 25 02:44 wget-log
root@linux-lab:/projects# cat tubt.txt 
Bui Thanh Tu
root@linux-lab:/projects# echo "Tubt-sysadmin" > tubt.txt 
root@linux-lab:/projects# cat tubt.txt 
Tubt-sysadmin
```

**Restore Logical Volume**

Để restore snapshot, chúng ta cần hủy gắn kết hệ thống tệp (Umount)

```sh
root@linux-lab:/projects# df -TH
Filesystem               Type      Size  Used Avail Use% Mounted on
/dev/root                ext4       21G  4.6G   17G  22% /
devtmpfs                 devtmpfs  1.1G     0  1.1G   0% /dev
tmpfs                    tmpfs     1.1G     0  1.1G   0% /dev/shm
tmpfs                    tmpfs     206M  1.0M  205M   1% /run
tmpfs                    tmpfs     5.3M     0  5.3M   0% /run/lock
tmpfs                    tmpfs     1.1G     0  1.1G   0% /sys/fs/cgroup
/dev/loop0               squashfs   67M   67M     0 100% /snap/core20/2015
/dev/loop2               squashfs   97M   97M     0 100% /snap/lxd/24061
/dev/loop1               squashfs  358M  358M     0 100% /snap/google-cloud-cli/171
/dev/loop3               squashfs   43M   43M     0 100% /snap/snapd/20092
/dev/sda15               vfat      110M  6.4M  104M   6% /boot/efi
tmpfs                    tmpfs     206M     0  206M   0% /run/user/0
/dev/mapper/vg0-backups  ext4       21G  1.6M   20G   1% /backups
/dev/mapper/vg0-projects ext4       11G  1.1G  9.0G  11% /projects

root@linux-lab:~# umount /projects 
```

Kiểm tra xem điểm gắn kết còn hay không:

```sh
root@linux-lab:~# df -h
Filesystem               Size  Used Avail Use% Mounted on
/dev/root                 20G  4.6G   15G  24% /
devtmpfs                 977M     0  977M   0% /dev
tmpfs                    981M     0  981M   0% /dev/shm
tmpfs                    197M  992K  196M   1% /run
tmpfs                    5.0M     0  5.0M   0% /run/lock
tmpfs                    981M     0  981M   0% /sys/fs/cgroup
/dev/loop0                64M   64M     0 100% /snap/core20/2015
/dev/loop1               341M  341M     0 100% /snap/google-cloud-cli/171
/dev/loop2                41M   41M     0 100% /snap/snapd/20092
/dev/loop3                92M   92M     0 100% /snap/lxd/24061
/dev/sda15               105M  6.1M   99M   6% /boot/efi
/dev/mapper/vg0-backups   20G  1.6M   19G   1% /backups
tmpfs                    197M     0  197M   0% /run/user/0
/dev/loop4               341M  341M     0 100% /snap/google-cloud-cli/173
```

Điểm gắn kết của chúng ta đã được hủy, vì vậy chúng ta có thể tiếp tục restore snapshot. Để restore snapshot chúng ta sử dụng lệnh `lvconvert`

```sh
root@linux-lab:~# lvs
  LV       VG  Attr       LSize  Pool Origin   Data%  Meta%  Move Log Cpy%Sync Convert
  backups  vg0 -wi-ao---- 19.99g                                                      
  projects vg0 owi-a-s--- 10.00g                                                      
  snap_1   vg0 swi-a-s---  4.00g      projects 23.90   

root@linux-lab:~# lvconvert --merge /dev/vg0/snap_1 
  Merging of volume vg0/snap_1 started.
  vg0/projects: Merged: 76.15%
  vg0/projects: Merged: 100.00%

root@linux-lab:~# lvs
  LV       VG  Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  backups  vg0 -wi-ao---- 19.99g                                                    
  projects vg0 -wi-a----- 10.00g         

root@linux-lab:~# mount /dev/vg0/projects /projects/

root@linux-lab:~# df -TH
Filesystem               Type      Size  Used Avail Use% Mounted on
/dev/root                ext4       21G  4.9G   16G  24% /
devtmpfs                 devtmpfs  1.1G     0  1.1G   0% /dev
tmpfs                    tmpfs     1.1G     0  1.1G   0% /dev/shm
tmpfs                    tmpfs     206M  1.1M  205M   1% /run
tmpfs                    tmpfs     5.3M     0  5.3M   0% /run/lock
tmpfs                    tmpfs     1.1G     0  1.1G   0% /sys/fs/cgroup
/dev/loop0               squashfs   67M   67M     0 100% /snap/core20/2015
/dev/loop1               squashfs  358M  358M     0 100% /snap/google-cloud-cli/171
/dev/loop2               squashfs   43M   43M     0 100% /snap/snapd/20092
/dev/loop3               squashfs   97M   97M     0 100% /snap/lxd/24061
/dev/sda15               vfat      110M  6.4M  104M   6% /boot/efi
/dev/mapper/vg0-backups  ext4       21G  1.6M   20G   1% /backups
tmpfs                    tmpfs     206M     0  206M   0% /run/user/0
/dev/loop4               squashfs  358M  358M     0 100% /snap/google-cloud-cli/173
/dev/mapper/vg0-projects ext4       11G  1.1G  9.0G  11% /projects
```

Sau khi merge hoàn thành, snapshot volume sẽ tự động bị xóa

Chúng ta kiểm tra lại `/dev/vg0/projects` để xem kết quả

```sh
root@linux-lab:~# cd /projects/
root@linux-lab:/projects# ls -l
total 996376
-rw-r--r-- 1 root root 1020264448 Nov  3  2020 CentOS-7-x86_64-Minimal-2009.iso
drwx------ 2 root root      16384 Sep 25 01:33 lost+found
-rw-r--r-- 1 root root         13 Sep 25 02:21 tubt.txt
root@linux-lab:/projects# cat tubt.txt 
Bui Thanh Tu
```

Qua kiểm tra trên thì kết quả restore cho chúng ta thấy kết quả trả về ban đầu khi chúng ta thực hiện snapshot, dù chúng ta có điều chỉnh gì sau khi tạo snapshot thì khi restore vẫn trở về lúc chúng ta tạo snapshot