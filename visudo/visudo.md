# Giới thiệu

Phân tách đặc quyền là một trong những mô hình bảo mật cơ bản được triển khai trong các hệ điều hành giống Linux và Unix. Người dùng thông thường hoạt động với các đặc quyền hạn chế nhằm giảm phạm vi ảnh hưởng của họ đến môi trường của chính họ chứ không phải hệ điều hành

Một người dùng đặc biệt tên là `root`, có đặc quyền siêu người dùng. Đây là tài khoản quản trị không có hạn chế đối với người dùng thông thường. Người dùng có thể thực thi các lệnh với đặc quyền siêu người dùng hoặc quyền `root` theo một số cách khác nhau

Trong bài viết này chúng ta tập trung vào việc lấy quyền `root` một cách an toàn và chính xác, đặc biệt tập trung vào việc chính sửa tệp `/etc/sudoers`

# Làm thế nào để có được đặc quyền `root`

Có 3 cách cơ bản để có được quyền `root`, chúng khác nhau về mức độ phức tạp

**Đăng nhập bằng quyền `Root`**

Phương pháp đơn giản và dễ hiểu nhất để có được đặc quyền `root` là đăng nhập trực tiếp vào máy chủ của bạn với tư cách là người dùng `root`

Nếu đăng nhập qua SSH hãy chỉ định người dùng `root` trước địa chỉ IP hoặc tên miền trong chuỗi kết nối SSH:

```sh
ssh root@server_domain_or_ip
```

**Sử dụng `su` để trở thành `root`**

Đăng nhập hệ thống bằng tài khoản `root` thường không được khuyến khích vì tài khoản `root` có mọi đặc quyền, điều này rất nguy hiểm (Vì trên đường truyền từ máy chủ local đến máy chủ từ xa rất có thể sẽ bị rò rỉ thông tin khi nhập password từ bàn phím)

Cách tiếp theo để có được quyền siêu người dùng, cho phép bạn trở thành người dùng `root` bất kỳ lúc nào bạn cần

Chúng ta có thể thực hiện điều này bằng cách gọi lệnh `su`, viết tắt của "substitute user"

```sh
su
```

Bạn sẽ được nhắc nhập mật khẩu của người dùng `root`, sau đó, bạn sẽ được đưa vào phiên shell root

Khi bạn đã hoàn thành các tác vụ yêu cầu quyền `root`, hãy quay lại shell thường bằng cách gõ

```sh
exit
```

**Sử dụng `sudo` để thực các lệnh với quyền `Root`**

Cách cuối cùng để có được quyền `root` là sử dụng lệnh `sudo`

Lệnh `sudo` cho phép bạn thực thi các lệnh một lần với quyền `root` mà không cần tạo shell mới. Nó được thực hiện như sau:

```sh
sudo command_to_execute
```

Không giống như `su`, lệnh `sudo` sẽ yêu cầu mật khẩu của người dùng hiện tại chứ không phải mật khẩu `root`

Do ý nghĩa bảo mật của nó, quyền `sudo` không được cấp cho người dùng theo mặc định

Để cấp quyền `sudo` cho một user ta làm như sau:

**Bước 1:** Login server với quyền `root`

```sh
ssh root@your_server_ip_address
```

**Bước 2:** Tạo user

```sh
root@buitu:~# useradd tubt
```

**Bước 3:** Set password

```sh
root@buitu:~# passwd tubt
New password:
Retype new password:
passwd: password updated successfully
```

**Bước 4:** Thêm user vào `sudo` group

Sử dụng `usermod` để thêm người dùng vào nhóm `sudo`

```sh
root@buitu:~# usermod -aG sudo tubt
root@buitu:~#
```

# Visudo là gì ?

Lệnh `sudo` được cấu hình thông qua một tệp nằm ở `/etc/sudoers`

**Lưu ý: Không bao giờ chỉnh sửa tệp này bằng trình soạn thảo văn bản thông thường! Thay vào đó hãy luôn sử dụng lệnh `visudo`**

Vì cú pháp không đúng trong tệp `/etc/sudoers` có thể khiến hệ thống của bạn bị hỏng và không thể có được các đặc quyền nâng cao, điều quan trọng là bạn cần sử dụng lệnh `visudo` để chỉnh sửa tệp

Lệnh `visudo` mở trình soạn thảo văn bản như thông thường nhưng nó xác thực cú pháp của tệp khi lưu. Điều này ngăn các lỗi cấu hình chặn các hoạt động `sudo`

Theo mặc định, visudo mở tệp `/etc/sudoers` bằng trình soạn thảo văn bản `vi`. Tuy nhiên Ubuntu đã cấu hình `visudo` để sử dụng trình soạn thảo văn bản bằng `nano` thay thế

Nếu bạn muốn thay đổi nó trở lại thành `vi`, hãy đưa ra lệnh sau:

```sh
sudo update-alternatives --config editor
```

Output:

```sh
root@buitu:~# sudo update-alternatives --config editor
There are 4 choices for the alternative editor (providing /usr/bin/editor).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /bin/nano            40        auto mode
  1            /bin/ed             -100       manual mode
  2            /bin/nano            40        manual mode
  3            /usr/bin/vim.basic   30        manual mode
  4            /usr/bin/vim.tiny    15        manual mode

Press <enter> to keep the current choice[*], or type selection number: 3
update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/editor (editor) in manual mode
```

Chọn số tương ứng với lựa chọn bạn muốn thực hiện

Trên CentOS, bạn có thể thay đổi giá trị này bằng cách thêm dòng sau vào `~/.bashrc`

```sh
export EDITOR=`which name_of_editor`
```

Nguồn tệp để thực hiện các thay đổi

```sh
. ~/.bashrc
```

Sau khi đã thực hiện lựa chọn trình soạn thảo cho `visudo`, hãy thực hiện lệnh để truy cập `/etc/sudoers`

# Cách sửa đổi tệp `Sudoers`

```sh
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

zabbix    ALL=(ALL:ALL) NOPASSWD:ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
```

Chúng ta hãy xem các dòng sau để làm gì

**Default Lines**

- Dòng đầu tiên, `Defaults env_reset`, đặt lại môi trường đầu cuối để xóa mọi biến người dùng. Đây là biện pháp an toàn được sử dụng để xóa các biến môi trường có khả năng gây hại khỏi phiên `sudo`

- Dòng thứ hai, `Defaults mail_badpass`, yêu cầu hệ thống gửi thông báo về các lần thử mật khẩu `sudo` sai tới người `mailto` đã định cấu hình. Theo mặc định, đây là tài khoản `root`

- Dòng thứ ba, bắt đầu bằng `Defaults secure_path=...`, chỉ định PATH (các vị trí trong hệ thống tệp mà hệ điều hành sẽ tìm kiếm ứng dụng) sẽ được sử dụng cho hoạt động sudo. Điều này ngăn chặn việc sử dụng đường dẫn người dùng có thể gây hại

**User Privilege Lines**

Dòng thứ tư quy định các đặc quyền sudo của người dùng `root`. Chúng ta hãy xem ý nghĩa của các trường sau:

- '**root** ALL=(ALL:ALL) ALL': Trường đầu tiên cho biết người dùng mà quy tắc sẽ áp dụng lên

- 'root **ALL**=(ALL:ALL) ALL': Trường `ALL` đầu tiên chỉ ra rằng quy tắc này áp dụng cho tất cả các host

- 'root ALL=(**ALL**:ALL) ALL': Trường `ALL` thứ hai chỉ ra rằng người dùng `root` có thể chạy các lệnh với tư cách là tất cả `user`

- 'root ALL=(ALL:**ALL**) ALL': Trường `ALL` thứ ba chỉ ra rằng người dùng `root` có thể chạy các lệnh với tư cách là tất cả `group`

- 'root ALL=(ALL:ALL) **ALL**': Trường `ALL` thứ tư cho biết quy tắc này áp dụng cho tất cả các lệnh

Điều trên có nghĩa là người dùng `root` của tôi có thể chạy bất kỳ lệnh nào bằng `sudo`, miễn là tôi cung cấp mật khẩu

**Group Privilege Lines**

Hai dòng tiếp theo tương tự như dòng đặc quyền người dùng, nhưng chúng chỉ định quy tắc `sudo` cho các nhóm

Tên bắt đầu bằng `%` cho biết tên nhóm

Ở đây, chúng ta thấy nhóm `admin`, có thể thực thi bất kỳ lệnh nào với tư cách là bất kỳ người dùng nào trên bất kỳ máy chủ nào. Tương tự, nhóm `sudo` có cùng đặc quyền nhưng cũng có thể thực thi như bất kỳ `group` nào

**Include `/etc/sudoers.d`**

```sh
. . .

#includedir /etc/sudoers.d
```

Dòng này được thực tế chỉ ra rằng các tệp trong thư mục `/etc/sudoers.d` cũng sẽ được lấy nguồn và áp dụng

Các tệp trong thư mục đó tuân theo các quy tắc tương tụ như chính tệp `/etc/sudoers`. Bất kỳ tệp nào không kết thúc bằng `~` và không có phần mở rộng `.` trong đó sẽ được đọc và thêm vào cấu hình `sudo`

Giống như chính tệp `/etc/sudoers`, bạn phải luôn chỉnh sửa các tệp trong thư mục `/etc/sudoers.d` bằng `visudo`. Cú pháp để chỉnh sửa các tệp này sẽ là:

```sh
sudo visudo -f /etc/sudoers.d/file_to_edit
```

**Cách cấp đặc quyền `sudo` cho người dùng**

Thao tác phổ biến nhất mà người dùng muốn thực hiện khi quản lý quyền `sudo` là cấp quyền truy cập `sudo` chung cho người dùng mới. Điều này hữu ích nếu bạn muốn cấp cho tài khoản toàn quyền truy cập quản trị vào hệ thống

Cách dễ nhất để thực hiện việc này trên hệ thống được thiết lập với nhóm quản trị có mục đích chung, như trong hướng dẫn này, thực chất là ta thêm người dùng vào nhóm đã có sẵn các đặc quyền

Trên Ubuntu:

Thêm người dùng vào group `sudo`

```sh
sudo usermod -aG sudo username
```

Trên CentOS:

Trên CentOS thường là group `wheel` thay vì `sudo`

```sh
sudo usermod -aG wheel username
```

# Thiết lập quy tắc tùy chỉnh

Bây giờ chúng ta đã làm quen với cú pháp chung của tệp, hãy tạo một số quy tắc mới

**Tạo bí danh**

Tệp `sudoers` có thể được sắp xếp dễ dàng hơn bằng cách nhóm các thứ lại với nhau với nhiều loại bí danh (alias) khác nhau

```sh
. . .
User_Alias		GROUPONE = abby, brent, carl
User_Alias		GROUPTWO = brent, doris, eric,
User_Alias		GROUPTHREE = doris, felicia, grant
. . .
```

Tên Group phải bắt đầu bằng chữ in hoa. Sau đó, chúng ta có thể cho phép các user trong `GROUPTWO` chạy lệnh `apt-get update` bằng cách tạo quy tắc như sau:

```sh
. . .
GROUPTWO	All= /usr/bin/apt-get update
. . .
```

Nếu chúng ta không chỉ định người dùng/nhóm để chạy như trên, `sudo` sẽ mặc định là người dùng `root`

Chúng ta có thể cho phép các thành viên của `GROUPTHREE` tắt và khởi động lại máy bằng cách tạo `command alias` và sử dụng alias đó trong quy tắc cho `GROUPTHREE`

```sh
. . .
Cmnd_Alias		POWER = /sbin/shutdown, /sbin/halt, /sbin/reboot, /sbin/restart
GROUPTHREE	ALL = POWER
. . .
```

Chúng ta tạo bí danh có tên là `POWER` chứa các lệnh tắt nguồn và khởi động lại máy. Sau đó chúng tôi cho phép các thành viên của `GROUPTHREE` thực thi lệnh này

Chúng ta cũng có thể tạo bí danh `Runas`, bí danh này có thể thay thế phần quy tắc chỉ định người dùng thực thi lệnh dưới dạng:

```sh
. . .
Runas_Alias		WEB = www-data, apache
GROUPONE	ALL = (WEB) ALL
. . .
```

Điều này cho phép bất kỳ ai là thành viên của `GROUPONE` thực thi các lệnh với tư cách là người dùng dữ liệu `www` hoặc người dùng `apache`

Lưu ý rằng các quy tắc sau này sẽ ghi đè các quy tắc trước đó khi có xung đột giữa hai quy tắc

**Khóa quy tắc**

Nếu chúng ta muốn cho phép người dùng thực thi lệnh với quyền `root` mà không cần phải nhập mật khẩu, chúng ta có thể tạo một quy tắc như sau:

```sh
. . .
GROUPONE	ALL = NOPASSWD: /usr/bin/updatedb
. . .
```

`NOPASSWD` là một 'tag' có nghĩa là sẽ không yêu cầu mật khẩu. Nó có một lệnh đồng hành gọi là `PASSWD`, đây là hành vi mặc định. Tag có liên quan đến phần còn lại của quy tắc trừ khi bị tag "kép" của nó ghi đè sau này

Ví dụ ta có một dòng như sau

```sh
. . .
GROUPTWO	ALL = NOPASSWD: /usr/bin/updatedb, PASSWD: /bin/kill
. . .
```

Một thẻ hữu ích khác là `NOEXEC`, có thể được sử dụng để ngăn chặn một số hành vi nguy hiểm trong một số chương trình nhất định

```sh
. . .
username	ALL = NOEXEC: /usr/bin/less
. . .
```
