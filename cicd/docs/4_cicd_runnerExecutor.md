# Runner executor

Runner executor có thể hiểu đơn giản thì đây là phần mềm/dịch vụ sử dụng để xử lý các job được nhận từ Gitlab runner. Như đã đề cập ở bài [trước](./3_cicd_gitlabRunner.md). Gitlab runner chỉ đóng vai trò như một anh shipper chuyên đi giao nhận các job từ người dùng đến các executor. Các phần mềm/dịch vụ này sẽ được giao và gửi kết quả đến người dùng thông qua Gitlab runner

# Thư mục lưu trữ mã nguồn của executor

Mặc định mã nguồn (source code) của dự án/repository sẽ được lưu vào đường dẫn sau:

```sh
~/builds/<short-token>/<concurrent-id>/<namespace>/<tên dự án / repository>
```

Trong đó:

- <short-token>: 8 ký tự đầu tiên của ID runner

- <concurrent-id>: Job ID tương ứng với runner thực thi job

- <namespace>: Tên group user

Người dùng hoàn toàn có thể tự định nghĩa thư mục dùng để lưu trữ mã nguồn khi bằng cách thêm trường `build_dir` bên dưới phần `[[runners]]` trong file `config.toml`, chỉ định vị trí sẽ lưu mã nguồn của mình

# Các loại executor

Gitlab hỗ trợ khá nhiều loại executor để người dùng có thể cân nhắc sử dụng

## SSH

Đầu tiên, đây là executor mà ngay cả chính Gitlab khuyến cáo không nên dùng. Executor này giúp người dùng có thể kết nối SSH đến một máy chủ chỉ định với các thông tin do người dùng cung cấp. Sau đó thực thi các câu lệnh mà người đã quy định cho job. Một lưu ý khi sử dụng executor dạng này đó là chỉ thực thi được Bash script và không hỗ trợ "caching" ở thời điểm hiện tại

Đặc điểm nhận dạng của executor này là trong file `config.toml`, phần executor sẽ có giá trị là "ssh". Bên dưới là cấu hình đơn giản cho SSH executor

```sh
[[runners]]
  executor = "ssh"
  [runners.ssh]
  	host = "example.com"
  	port = "22"
  	user = "root"
  	password = "pasword"
  	indentity_file = "/path/to/indentity/file"
```

Trong đó:

- `executor`: Loại executor được sử dụng

- `runners.ssh`: Khu vực khai báo thông tin kết nối SSH

	+ `host`: Thông tin máy chủ sẽ kết nối đến (IP/Hostname)

	+ `port`: Port kết nối (mặc định port của SSH là 22)

	+ `user`: User dùng để kết nối

	+ `password`: Mật khẩu để đăng nhập vào máy chủ (có thể khai báo thông tin này hoặc là thông tin `indentity_file` bên dưới)

	+ `indentity_file`: Gitlab runner sẽ không tự đọc file chứa thông tin định danh của bạn từ thư mục `/home/user/.ssh/id_rsa`, thay vào đó, người dùng cần phải khai báo đường dẫn cụ thể để Gitlab runner có thể sử dụng khi tạo kết nối SSH

## Shell

Đây là loại executor đơn giản nhất vì job sẽ được xử lý ngay tại máy chủ mà Gitlab runner đang hoạt động. Runner được cài đặt ở đâu, executor sẽ hoạt động ở đó. Người dùng có thể chạy các script được viết bằng Bash, PowerShell Core, Windows PowerShell (tùy thuộc vào hệ điều hành của máy chủ)

```sh
[[runners]]
  name = "mavengitlabproject"
  url = "http://gitlab.monest.sbs/"
  id = 10
  executor = "shell"
```

Khi cài đặt Gitlab runner từ nguồn chính thức do Gitlab cung cấp trên hệ điều hành Linux, quá trình cài đặt sẽ ưu tiên sử dụng user có tên là `gitlab_ci_multi_runner`. Nếu không tìm thấy user này tồn tại trên server, quá trình cài đặt sẽ tự tạo một user mới có tên là `gitlab-runner`. Vì vậy, khi quá trình xử lý job diễn ra, Runner sẽ sử dụng một trong 2 user này để chạy job

Nếu như job cần được xử lý phải gọi các tài nguyên có quyền đặc biệt, người dùng cần phải thêm các user của Runner vào group được quyền truy cập vào các tài nguyên này. Ví dụ job cần thao tác đến Docker Engine và Virtual Box, Gitlab runner đang sử dụng user `gitlab-runner`. Việc cần làm là chạy 2 câu lệnh bên dưới để tránh gặp lỗi phân quyền khi job được xử lý:

```sh
usermod -aG docker gitlab-runner

usermod -aG vboxusers gitlab-runner
```

## Virtual Box

Loại executor này cho phép người dùng sử dụng một máy ảo đã được tạo trước đó để xử lý các job được yêu cầu. Executor này sẽ phù hợp với những ai muốn xử lý "job" hoặc "build" trên nhiều hệ điều hành khác nhau, giúp giảm chi phí về server/máy chủ. Việc của Gitlab runner lúc này là kết nối đến các máy ảo được chỉ định để xử lý các job được yêu cầu từ phía Gitlab server

NOTE: Thư mục chưa mã nguồn của repository lúc này sẽ không có phần `<concurrent-id>` 

Để sử dụng loại executor này, Gitlab runner sẽ được cài trên máy chủ đã cài đặt VirtualBox. Máy ảo cần phải được thiết lập sẵn SSH (OpenSSH server), các thư viện, phần mềm cần có để xử lý job. Đối với cấu hình của máy ảo cần được cấu hình NAT để Gitlab runner có thể kết nối đến máy ảo

## Parallels

Cách cài đặt và quy trình xử lý tương tự như VirtualBox

## Docker

Executor sẽ xử lý các job dựa trên các Docker image do người dùng chỉ định. Thông qua việc kết nối với Docker Engine, executor sẽ xử lý từng job với từng container riêng biệt với các Docker image được chỉ định trong file `.gitlab-ci.yml`, hoặc dựa theo cấu hình trong file `config.toml`

```sh
[[runners]]
  name = "projectmaven"
  url = "http://gitlab.monest.sbs/"
  id = 11
  token = "xxxxxxxxxxxxxxxxxxxxxx"
  token_obtained_at = 2023-10-26T06:38:23Z
  token_expires_at = 0001-01-01T00:00:00Z
  executor = "docker"
  [runners.docker]
    tls_verify = false
    image = "maven:latest"
    privileged = false
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache"]
    shm_size = 0
    network_mtu = 0
```

Người dùng có thể tạo ra 1 Docker image đã được cài đặt toàn bộ các thư viện, phần mềm cần thiết để xử lý các job, lưu chúng ở registry. Sau đó executor chỉ việc sử dụng image này và xử lý job, không còn phải tốn thời gian cho việc cài đặt thư viện, phần mềm bổ sung để xử lí các job

## Docker Machine (auto-schaling)

Đây là phiên bản đặc biệt của Docker executor với tính "auto-scaling"

Sơ lược về Docker Machine: service này cho phép người dùng tạo ra Docker hosts trên chính máy chủ của mình, trên các nhà cung cấp dịch vụ điện toán đám mây. Công cụ này tạo ra các máy chủ, cài đặt Docker trên chúng, sau đó cấu hình Docker client để kiểm soát chúng

## Kubernetes 

Đã nhắc đến Docker thì không thể nào thiếu Kubernetes (k8s). Người dùng sẽ sử dụng các k8s cluster hiện có để xử lý các job. Các executor sẽ gọi API của k8s cluster và tạo ra các pod mới để xử lý từng job 

Chi tiết xem hình dưới

![](/cicd/images/runnerk8s.png)

## Custom 

Với `Custom` executor, người dùng sẽ tạo ra một executor mới cho riêng mình

Người dùng sẽ tùy biến Gitlab runner để chỉ định service/script nào được gọi để xử lý job. Các service/script thực thi này được gọi chung là Driver