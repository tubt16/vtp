# Yellow Dog Updater Modified (YUM)

Về mặt chức năng, nó tương tự như tiện ích APT trên hệ thống dựa trên Debian, có thể tìm kiếm, cài đặt, cập nhật và xóa các gói cũng như tự động xử lý các phần phụ thuộc. Yum có thể được sử dụng để cài đặt một gói hoặc nâng cấp toàn hệ thống cùng 1 lúc

### Searching for Packages

Để cài đặt một gói, bạn cần biết tên của gói đó. Để làm được điều này bạn có thể thực hiện tìm kiếm gói với lệnh `yum search <package_name>`

Ví dụ: Tìm một gói tên unzip

```sh
[root@centos7lpic ~]# yum search unzip
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.aktkn.sg
 * epel: ftp.iij.ad.jp
 * extras: mirror.aktkn.sg
 * updates: mirror.aktkn.sg
========================================================= N/S matched: unzip ==========================================================perl-PerlIO-gzip.x86_64 : Perl extension to provide a PerlIO layer to gzip/gunzip
unzip.x86_64 : A utility for unpacking zip files

  Name and summary matches only, use "search all" for everything.
```

### Installing, Upgrading and Removing Packages

Để cài đặt một gói bằng Yum, hãy sử dụng lệnh `yum install <package_name>`

```sh
yum install unzip
```

Để nâng cấp một gói ta chạy lệnh `yum update <package_name>`

```sh
yum update wget
```

Để kiểm tra xem có bản cập nhật cho một gói cụ thể hay không, ta sử dụng `yum check-update <package_name>`

```sh
yum check-update wget
```

Để xóa gói đã cài đặt, sử dụng `yum remove <package_name>`

```sh
yum remove wget
```

### Tìm kiếm Package Provides chứa một lệnh cụ thể

Để tìm kiếm ta sử dụng lệnh `yum whatprovides <package_name>`

Ví dụ tìm kiếm gói chứa lệnh `ping`

```sh
[root@centos7lpic ~]# yum whatprovides ping
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.aktkn.sg
 * epel: ftp.iij.ad.jp
 * extras: mirror.aktkn.sg
 * updates: mirror.aktkn.sg
base/7/x86_64/filelists_db                                                                                      | 7.2 MB  00:00:04
epel/x86_64/filelists_db                                                                                        |  12 MB  00:00:06
extras/7/x86_64/filelists_db                                                                                    | 303 kB  00:00:00
updates/7/x86_64/filelists_db                                                                                   |  12 MB  00:00:05
iputils-20160308-10.el7.x86_64 : Network monitoring tools including ping
Repo        : base
Matched from:
Filename    : /usr/bin/ping



iputils-20160308-10.el7.x86_64 : Network monitoring tools including ping
Repo        : @anaconda
Matched from:
Filename    : /usr/bin/ping
```

Từ đó ta thấy được để sử dụng được lệnh ping ta phải cài đặt gói `iputils-20160308-10.el7.x86_64` 

```sh
yum install iputils-20160308-10.el7.x86_64
```

### Nhận thông tin về một gói cụ thể

Để tìm kiếm thông tin về một gói cụ thể, chẳng hạn như phiên bản, kiến trúc, mô tả, kích thước ... ta sử dụng `yum info <package_name>`

```sh
[root@centos7lpic ~]# yum info wget
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.aktkn.sg
 * epel: ftp.iij.ad.jp
 * extras: mirror.aktkn.sg
 * updates: mirror.aktkn.sg
Installed Packages
Name        : wget
Arch        : x86_64
Version     : 1.14
Release     : 18.el7_6.1
Size        : 2.0 M
Repo        : installed
From repo   : base
Summary     : A utility for retrieving files using the HTTP or FTP protocols
URL         : http://www.gnu.org/software/wget/
License     : GPLv3+
Description : GNU Wget is a file retrieval utility which can use either the HTTP or
            : FTP protocols. Wget features include the ability to work in the
            : background while you are logged out, recursive retrieval of
            : directories, file name wildcard matching, remote file timestamp
            : storage and comparison, use of Rest with FTP servers and Range with
            : HTTP servers to retrieve files over slow or unstable connections,
            : support for Proxy servers, and configurability.
```

### Managing Software Repositories

Đối với `yum`, “repos” được liệt kê trong thư mục `/etc/yum.repos.d/`. Mỗi kho lưu trữ được biểu thị bằng một tệp `.repo`, như `CentOS-Base.repo`

```sh
[root@centos7lpic ~]# cd /etc/yum.repos.d/
[root@centos7lpic yum.repos.d]# ls
CentOS-Base.repo  CentOS-Debuginfo.repo  CentOS-Media.repo    CentOS-Vault.repo          epel.repo
CentOS-CR.repo    CentOS-fasttrack.repo  CentOS-Sources.repo  CentOS-x86_64-kernel.repo  epel-testing.repo
```

Người dùng có thể thêm các kho lưu trữ bổ sung bằng cách thêm tệp `.repo` vào thư mục được đề cập ở trên hoặc ở cuối `/etc/yum.conf`. Tuy nhiên, cách được khuyến nghị để thêm hoặc quản lý kho lưu trữ là sử dụng công cụ `yum-config-manager`.

Để thêm kho lưu trữ, hãy sử dụng tham số `--add-repo`, theo sau là URL tới tệp .repo.

```sh
yum-config-manager --add-repo https://rpms.remirepo.net/enterprise/remi.repo
```

Để có danh sách tất cả các kho lưu trữ có sẵn ta sử dụng `yum repolist all`

```sh
[root@centos7lpic yum.repos.d]# yum repolist all
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.aktkn.sg
 * epel: ftp.iij.ad.jp
 * extras: mirror.aktkn.sg
 * updates: mirror.aktkn.sg
repo id                                      repo name                                                                  status
C7.0.1406-base/x86_64                        CentOS-7.0.1406 - Base                                                     disabled
C7.0.1406-centosplus/x86_64                  CentOS-7.0.1406 - CentOSPlus                                               disabled
C7.0.1406-extras/x86_64                      CentOS-7.0.1406 - Extras                                                   disabled
C7.0.1406-fasttrack/x86_64                   CentOS-7.0.1406 - Fasttrack                                                disabled
C7.0.1406-updates/x86_64                     CentOS-7.0.1406 - Updates                                                  disabled
C7.1.1503-base/x86_64                        CentOS-7.1.1503 - Base                                                     disabled
C7.1.1503-centosplus/x86_64                  CentOS-7.1.1503 - CentOSPlus                                               disabled
C7.1.1503-extras/x86_64                      CentOS-7.1.1503 - Extras                                                   disabled
C7.1.1503-fasttrack/x86_64                   CentOS-7.1.1503 - Fasttrack                                                disabled
C7.1.1503-updates/x86_64                     CentOS-7.1.1503 - Updates                                                  disabled
C7.2.1511-base/x86_64                        CentOS-7.2.1511 - Base                                                     disabled
C7.2.1511-centosplus/x86_64                  CentOS-7.2.1511 - CentOSPlus                                               disabled
C7.2.1511-extras/x86_64                      CentOS-7.2.1511 - Extras                                                   disabled
C7.2.1511-fasttrack/x86_64                   CentOS-7.2.1511 - Fasttrack                                                disabled
C7.2.1511-updates/x86_64                     CentOS-7.2.1511 - Updates                                                  disabled
C7.3.1611-base/x86_64                        CentOS-7.3.1611 - Base                                                     disabled
C7.3.1611-centosplus/x86_64                  CentOS-7.3.1611 - CentOSPlus                                               disabled
C7.3.1611-extras/x86_64                      CentOS-7.3.1611 - Extras                                                   disabled
C7.3.1611-fasttrack/x86_64                   CentOS-7.3.1611 - Fasttrack                                                disabled
C7.3.1611-updates/x86_64                     CentOS-7.3.1611 - Updates                                                  disabled
C7.4.1708-base/x86_64                        CentOS-7.4.1708 - Base                                                     disabled
C7.4.1708-centosplus/x86_64                  CentOS-7.4.1708 - CentOSPlus                                               disabled
C7.4.1708-extras/x86_64                      CentOS-7.4.1708 - Extras                                                   disabled
C7.4.1708-fasttrack/x86_64                   CentOS-7.4.1708 - Fasttrack                                                disabled
C7.4.1708-updates/x86_64                     CentOS-7.4.1708 - Updates                                                  disabled
C7.5.1804-base/x86_64                        CentOS-7.5.1804 - Base                                                     disabled
C7.5.1804-centosplus/x86_64                  CentOS-7.5.1804 - CentOSPlus                                               disabled
C7.5.1804-extras/x86_64                      CentOS-7.5.1804 - Extras                                                   disabled
C7.5.1804-fasttrack/x86_64                   CentOS-7.5.1804 - Fasttrack                                                disabled
C7.5.1804-updates/x86_64                     CentOS-7.5.1804 - Updates                                                  disabled
C7.6.1810-base/x86_64                        CentOS-7.6.1810 - Base                                                     disabled
C7.6.1810-centosplus/x86_64                  CentOS-7.6.1810 - CentOSPlus                                               disabled
C7.6.1810-extras/x86_64                      CentOS-7.6.1810 - Extras                                                   disabled
C7.6.1810-fasttrack/x86_64                   CentOS-7.6.1810 - Fasttrack                                                disabled
C7.6.1810-updates/x86_64                     CentOS-7.6.1810 - Updates                                                  disabled
C7.7.1908-base/x86_64                        CentOS-7.7.1908 - Base                                                     disabled
C7.7.1908-centosplus/x86_64                  CentOS-7.7.1908 - CentOSPlus                                               disabled
C7.7.1908-extras/x86_64                      CentOS-7.7.1908 - Extras                                                   disabled
C7.7.1908-fasttrack/x86_64                   CentOS-7.7.1908 - Fasttrack                                                disabled
C7.7.1908-updates/x86_64                     CentOS-7.7.1908 - Updates                                                  disabled
C7.8.2003-base/x86_64                        CentOS-7.8.2003 - Base                                                     disabled
C7.8.2003-centosplus/x86_64                  CentOS-7.8.2003 - CentOSPlus                                               disabled
C7.8.2003-extras/x86_64                      CentOS-7.8.2003 - Extras                                                   disabled
C7.8.2003-fasttrack/x86_64                   CentOS-7.8.2003 - Fasttrack                                                disabled
C7.8.2003-updates/x86_64                     CentOS-7.8.2003 - Updates                                                  disabled
base/7/x86_64                                CentOS-7 - Base                                                            enabled: 10,072base-debuginfo/x86_64                        CentOS-7 - Debuginfo                                                       disabled
base-source/7                                CentOS-7 - Base Sources                                                    disabled
c7-media                                     CentOS-7 - Media                                                           disabled
centos-kernel/7/x86_64                       CentOS LTS Kernels for x86_64                                              disabled
centos-kernel-experimental/7/x86_64          CentOS Experimental Kernels for x86_64                                     disabled
centosplus/7/x86_64                          CentOS-7 - Plus                                                            disabled
centosplus-source/7                          CentOS-7 - Plus Sources                                                    disabled
cr/7/x86_64                                  CentOS-7 - cr                                                              disabled
epel/x86_64                                  Extra Packages for Enterprise Linux 7 - x86_64                             enabled: 13,770epel-debuginfo/x86_64                        Extra Packages for Enterprise Linux 7 - x86_64 - Debug                     disabled
epel-source/x86_64                           Extra Packages for Enterprise Linux 7 - x86_64 - Source                    disabled
epel-testing/x86_64                          Extra Packages for Enterprise Linux 7 - Testing - x86_64                   disabled
epel-testing-debuginfo/x86_64                Extra Packages for Enterprise Linux 7 - Testing - x86_64 - Debug           disabled
epel-testing-source/x86_64                   Extra Packages for Enterprise Linux 7 - Testing - x86_64 - Source          disabled
extras/7/x86_64                              CentOS-7 - Extras                                                          enabled:    518extras-source/7                              CentOS-7 - Extras Sources                                                  disabled
fasttrack/7/x86_64                           CentOS-7 - fasttrack                                                       disabled
updates/7/x86_64                             CentOS-7 - Updates                                                         enabled:  5,176updates-source/7                             CentOS-7 - Updates Sources                                                 disabled
repolist: 29,536
```

`disabled` repositories sẽ bị bỏ qua khi cài đặt hoặc nâng cấp phần mềm. Để bật hoặc tắt kho lưu trữ, hãy sử dụng tiện ích `yum-config-manager`, theo sau là id kho lưu trữ.

```sh
yum-config-manager --disable C7.0.1406-base
```

```sh
yum-config-manager --enable C7.0.1406-base
```