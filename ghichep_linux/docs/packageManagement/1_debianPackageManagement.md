# Debian Package Tool (dpkg)

Dpkg là tiện ích thiết yếu để cài đặt, định cấu hình, bảo trì và xóa các gói phần mềm trên hệ thống dựa trên Debian. Thao tác cơ bản nhất là cài đặt gói `.deb`, có thể thực hiện bằng:

## Install Package

```sh
dpkg -i PACKAGENAME
```

Trước khi cài đặt gói, dpkg sẽ kiểm tra xem phiên bản trước đó đã tồn tại trong hệ thống chưa. Nếu gói đã được cài trước đó rồi, gói đó sẽ được nâng cấp lên phiên bản mới. Nếu không, một gói mới sẽ được cài đặt

## Removing Packages

Để xóa gói, chuyển tham số `-r` cho dpkg, theo sau là tên gói. Ví dụ: lệnh sau sẽ xóa gói unrar khỏi hệ thống

```sh
dpkg -r unrar
```
## Kiểm tra thông tin Package

Để kiểm tra thông tin gói với `dpkg` ta sử dụng option `-I` theo sau đó là tên gói muốn kiểm tra

```sh
dpkg -I google-chrome-stable_current_amd64.deb
```

## Liệt kê các Package và nội dung Package

Để kiểm tra danh sách mọi gói được cài trên hệ thống của bạn, hãy sử dụng tùy chọn `-L` 

```sh
dpkg -L unrar
```

## Cấu hình và cài đặt lại các Package đã cài

```sh
dpkg-reconfigure tzdata
```

# APT

Phần chính mà mình muốn đề cập đến trong bài viết này là APT. APT là một hệ thống quản lý gói, bao gồm một bộ công cụ giúp đơn giản hóa việc cài đặt nâng cấp, xóa và quản lý gói. APT cung cấp các tính năng như khả năng tìm kiếm nâng cao

`APT` không phải là sự thay thế cho `dpkg`. Bạn hãy coi nó như một công cụ bổ sung lấp đầy khoảng trống cho `dpkg`

Có nhiều tiện ích tương tác với APT, nhưng tiện ích đó là:

- `apt-get`: Được sử dụng để tải xuống, cài đặt, nâng cấp hoặc xóa gói khỏi hệ thống

- `apt-cache`: Được sử dụng để thực hiện các hoạt động, như tìm kiếm chỉ mục gói

- `apt-file`: Được sử dụng để tìm kiếm các tệp tin bên trong gói

Ngoài ra còn một tiện ích có tên đơn giản hơn là `apt`

### Update Package

```sh
apt-get update
```

### Installing and Removing Packages

Để cài đặt một gói ta sử dụng `apt-get install`

```sh
apt-get install xournal
```

Để gỡ cài đặt một gói ta sử dụng `apt-get remove`

```sh
apt-get remove xournal
```

Lưu ý khi cài đặt hoặc gỡ bỏ gói, APT sẽ tự động giải quyết sự phụ thuộc. Điều này có nghĩa là mọi gói bổ sung cần thiết cho gói bạn cài đặt sẽ được cài đặt và các gói phụ thuộc vào gói bạn đang xóa cũng sẽ bị xóa. APT sẽ luôn hiển thị những gì cài đặt hoặc xóa trước khi hỏi bạn có muốn tiếp tục không

```sh
root@ubuntulpic:~# apt-get remove unzip
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages will be REMOVED:
  unzip
0 upgraded, 0 newly installed, 1 to remove and 7 not upgraded.
After this operation, 567 kB disk space will be freed.
Do you want to continue? [Y/n]
```

Lưu ý rằng khi gỡ bỏ một gói, các tệp cấu hình tương ứng vẫn còn trên hệ thống. Để xóa gói và mọi tệp cấu hình, hãy sử dụng tham số thanh lọc thay vì xóa tham số bằng tùy chọn `--purge`

```sh
apt-get purge unzip
```
hoăc

```sh
apt-get remove --purge unzip
```

### Sửa chữa các thành phần phụ thuộc bị lỗi

Trong khi cái đặt gói, có thể xảy ra việc phụ thuộc của gói bị hỏng. Điều này nghĩa là một hoặc nhiều gói đã cài đặt vào gói khác không tồn tại. Điều này có thể xảy ra do lỗi APT hoặc các gói phụ thuộc được cài thủ công

Để giải quyết vấn này, hãy sử dụng lệnh `apt-get install -f`. Điều này sẽ cố gắng fix các gói bị hỏng bằng cách cài đặt các phần phụ thuộc bị thiếu, đảm bảo rằng tất cả các gói đều nhất quán trở lại

### Upgrade Packages

APT có thể sử dụng để tự động nâng cấp mọi gói đã cài đặt trên hệ thống lên phiên bản mới nhất có sẵn từ kho lưu trữ. Việc này được thực hiện bằng việc nâng cấp `apt-get`. Trước khi `upgrade` ta cần cập nhật chỉ mục gói bằng `apt-get update`

```sh
root@ubuntulpic:~# apt-get upgrade
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

Phần tóm tắt ở cuối cho biết bao nhiêu gói được nâng cấp, bao nhiêu gói sẽ được cài đặt, gỡ bỏ hoăc giữ lại

Giống dpkg, apt-get trước tiên sẽ kiểm tra xem phiên bản trước của gói đã được cài đặt chưa. Nếu rồi, gói sẽ được nâng cấp lên phiên bản mới nhất có sẵn trong kho. Nếu chưa, một bản sao mới sẽ được cài đặt

### Local Cache

Khi bạn cài đặt hoặc cập nhật một gói, tệp `.deb` tương tự sẽ được tải xuống thư mục local cache trước khi cài đặt gói. Theo mặc định, thư mục này là `/var/cache/apt/archives`. Các tệp đã tải xuống một phần sẽ được sao chép vào `/var/cache/apt/archives/partial`

```sh
root@ubuntulpic:/var/cache/apt/archives# ls
apparmor_2.12-4ubuntu5.3_amd64.deb      lock     ubuntu-advantage-tools_28.1~18.04_amd64.deb  zip_3.0-11build1_amd64.deb
libapparmor1_2.12-4ubuntu5.3_amd64.deb  partial  unzip_6.0-21ubuntu1.2_amd64.deb
```

Truy cập vào đường dẫn `/var/cache/apt/archives`, ta thấy các tệp `.deb` được ghi vào

Khi bạn cài đặt hoặc nâng cấp gói, thư mục bộ đệm có thể khá lớn. Để lấy lại dung lượng, bạn có thể làm trống bộ đệm bằng cách sử dụng lệnh `apt-get clean`. Thao tác này sẽ xóa nội dụng của thư mục `/var/cache/apt/archives` và `/var/cache/apt/archives/partial`

### Searching for Package

Tiện ích `apt-cache` có thể được sử dụng để thực hiện các thao tác trên chỉ mục gói, chẳng hạn như tìm kiếm một gói cụ thể 

Để tiến hành tìm kiếm ta sử dụng lệnh sau

```sh
root@ubuntulpic:/var/cache/apt/archives# apt-cache search net-tools
iproute2 - networking and traffic control tools
net-tools - NET-3 networking toolkit
atm-tools - Base programs for ATM in Linux, the net-tools for ATM
ddnet-tools - Tools for DDNet
```

Hiển thị chi tiết một gói cụ thể

```sh
root@ubuntulpic:/var/cache/apt/archives# apt-cache show net-tools
Package: net-tools
Architecture: amd64
Version: 1.60+git20161116.90da8a0-1ubuntu1
Multi-Arch: foreign
Priority: optional
Section: net
Origin: Ubuntu
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: net-tools Team <pkg-net-tools-maintainers@lists.alioth.debian.org>
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Installed-Size: 784
Depends: libc6 (>= 2.14), libselinux1 (>= 1.32)
Conflicts: ja-trans (<= 0.8-2)
Replaces: ja-trans (<= 0.8-2), netbase (<< 4.00)
Filename: pool/main/n/net-tools/net-tools_1.60+git20161116.90da8a0-1ubuntu1_amd64.deb
Size: 194236
MD5sum: 8bb5adf81a4a939ab676c2270b009611
SHA1: 9d36a6fa20df867673d86860aa09838a6aafdc71
SHA256: 80958d972b3a26aa23a272877138a65cafbb81501b4db172f4568e2e0e4803e8
Homepage: http://sourceforge.net/projects/net-tools/
Description-en: NET-3 networking toolkit
 This package includes the important tools for controlling the network
 subsystem of the Linux kernel.  This includes arp, ifconfig, netstat,
 rarp, nameif and route.  Additionally, this package contains utilities
 relating to particular network hardware types (plipconfig, slattach,
 mii-tool) and advanced aspects of IP configuration (iptunnel, ipmaddr).
 .
 In the upstream package 'hostname' and friends are included. Those are
 not installed by this package, since there is a special "hostname*.deb".
Description-md5: 08f345ee19e62d4fd85e960d3a061a33
Task: dns-server, cloud-image, server, xubuntu-desktop, ubuntustudio-desktop, ubuntu-mate-core, ubuntu-mate-desktop
Supported: 5y
```