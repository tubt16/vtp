# Boot The System (Quá trình khởi động - sysvinit - Từ bật nguồn điện trên máy tính đến vào chế độ dòng lệnh của hệ điều hành)

**sysvinit**

- Quản lý hệ thống và dịch vụ của hệ điều hành Linux cũ (centos 6 trở về trước)

- Dựa trên các tập lệnh init

Thứ tự khởi động hệ thống của Linux (Thứ tự khởi động của các hđh Linux là khác nhau giữa sysvinit, systemd và upstart)

Thứ tự khởi động chung như sau:

1. Bật nguồn máy tính

2. BIOS tải lên (Trên các hệ thống Linux mới, sử dụng UEFI)

3. BIOS tìm và chuyển giao cho `boot sector` của ổ đĩa chính hoặc ổ đĩa được chọn

4. Boot sector cung cấp MBR (Master Boot Record), nằm trong 512 byte đầu tiên của ổ đĩa hoạt động (hoặc ổ đầu tiên tùy vào quá trình cài đặt)

5. Boot loader được thực thi

6. Boot loader LILO/GRUB/GRUB2 bắt đầu

7. BƯỚC NHẬP DỮ LIỆU NGƯỜI DÙNG - tùy thuộc vào cấu hình boot loader, người dùng có thể chọn từ menu các loại khởi động/kernel hoặc cho phép sử dụng mặc định

8. Kernel Linux được đọc và thực thi

9. Khởi tạo thiết bị, tải các module và initial RAM disk (initrd)

10. Khởi tạo thiết bị, tải các module và initial RAM disk (initrd)

11. Chương trình init được tải lên (và trở thành PID đầu tiên - /sbin/init)

12. /etc/inittab được đọc và các tập lệnh runlevel tương ứng được chạy

- Debian/Ubuntu - /etc/init.d/rc#
- Red Hat/CentOS - /etc/rd.d/init.d/rc.sysinit

13. Các module được chỉ định trong các tập lệnh init được tải lên

14. Kiểm tra file hệ thống gốc

15. Các file hệ thống cục bộ còn lại được gắn mount vào hệ điều hành Linux

16. Thiết bị mạng được khởi động

17. Các filesystems từ xa được gắn mount vào hệ điều hành (nếu được cấu hình)

18. init process đọc lại /etc/inittab và chuyển đến runlevel mặc định được chỉ định và thực thi các tập lệnh tương ứng

19. Thực thi các tập lệnh runlevel theo thứ tự số (#dịch vụ(service) cho runlevel được chỉ định trong /etc/inittab

20. Các phiên tty được tải theo thứ tự được liệt kê trong /etc/inittab

21. Màn hình nhắc đăng nhập hiển thị, hệ thống Linux đã sẵn sàng để đăng nhập

- Các runlevel của sysvinit

	+ 0 - Tắt hệ thống shutdown
	+ 1 - Chế độ một người dùng đơn lẻ single user
	+ 2 - Chế độ nhiều người dùng multi-user (không có mạng hoặc filesystem từ xa)
	+ 3 - Chế độ nhiều người dùng đầy đủ multi user (có mạng)
	+ 4 - Không sử dụng unused
	+ 5 - X11 (chế độ desktop đồ họa)
	+ 6 - Khởi động lại reboot

# Khởi động hệ thống (Quá trình khởi động - systemd và upstart - Từ bật nguồn điện trên máy tính đến vào chế độ dòng lệnh của hệ điều hành)

**systemd**

Mặc định các bản phân phối Linux hiện đại (từ CentOS7 trở lên) sử dụng systemd thay vì sysvinit

Các thành phần chính:

- systemd: quản lý các dịch vụ(servives) và hệ thống(systems)

- systemctl: lệnh chính để điều khiển start(khởi động)/stop(dừng)/restart(khởi động lại)/status(trạng thái dịch vụ)

- system-analyze: hiển thị thông tin về hiệu suất khởi động hệ thống, cho phép theo dõi và thông tin cho việc gỡ lỗi

- logind: thay thế consolekit, hỗ trợ các trình quản lý X Windows

- consoled: dịch vụ console daemon, thay thế các virtual terminals

- journald: hệ thống ghi nhật ký(logging system), sử dụng ghi nhật ký nhị phân(mặc dù có thể được thay thế bằng các dịch vụ ghi nhật ký khác)

- networkd: dịch vụ hỗ trợ mạng trong Linux

Dịch vụ phần mở rộng:

+ .service: Dịch vụ hệ thống

+ .swap: Thiết bị device hoặc file swap

+ .socket: socket IPC

+ .target: unit(một hoặc một nhóm)

+ .snapshot: Trạng thái đã lưu của quản lý systemd

+ .slice: Các units được nhóm lại trong một cấu trúc phân cấp để quản lý các tiến trình

+ .timer: Bộ hẹn giờ

+ .mount: Điểm gắn kết (mount point) trên filesystem (cục bộ hoặc từ xa)

+ .automount: Tự động gắn trên filesystem

+ .scope: Tiến trình được tạo ra bên ngoài

+ .path: File hoặc thư mục trên filesystem

+ .device: Thiết bị được sử dụng bởi system kernel

Các runlevel trong systemd

0 - poweroff.target - Tắt hệ thống- hệ điều hành

1 - rescue.target - Chế độ đơn người dùng(single user)/cứu hộ(rescue shell)

2 - multi-user.target - Không có giao diện đồ họa, nhưng cho phép chạy mạng(full network) và đa người dùng (multi user)

3 - multi-user.target - Không có giao diện đồ họa, nhưng đầy đủ mạng và đa người dùng 

4 - multi-user.target - Không có giao diện đồ họa, nhưng đầy đủ mạng (full network) và đa người dùng(multi-user)..

5 - graphical.target - Môi trường đồ họa đầy đủ(full graphical desktop), đa người dùng(multi-user)

6 - reboot.target - Khởi động lại hệ thống- hệ điều hành(reboot)

