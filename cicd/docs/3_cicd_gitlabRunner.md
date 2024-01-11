# Gitlab Runner

Gitlab Runner là một phần mềm/công cụ mã nguồn mở được tạo ra để phục vụ cho việc CI/CD cho các dự án/repository được tạo trên Gitlab

Người dùng chỉ cần tạo 1 file `.gitlab-ci.yml` ở thư mục gốc của dự án/repo để khởi tạo CI/CD pipeline và chỉ định Gitlab runner nào được sử dụng

Gitlab sẽ cung cấp 2 gói hỗ trợ bao gồm:

- **Miễn phí**:

	+ Giới hạn 400 phút/tháng đối với `private repository` và 5000 phút/tháng đối với public repository

	+ Không giới hạn: Người dùng tự cài đặt và quản lý runner của riêng mình

- **Trả phí**: Từ $19 - $99 

NOTE: Chỉ áp dụng đối với `shared runner` do Gitlab cung cấp

# Các loại Gitlab Runner

Runner sẽ bao gồm 2 loại:

**Share runner** - do Gitlab quản lý

Nếu bạn theo xu hướng `serverless` (server sạch), đây là một giải pháp hợp lý và nhanh chóng. Bạn không phải cấu hình, quản trị, lo lắng về hiệu năng, tính sẵn sàng của runner. Các công việc này sẽ do Gitlab chịu trách nhiệm và xử lý

Shared runner sẽ xử lý các `job` thông qua một hàng đợi đặc biệt `fair usage queue`. Hàng đợi này sẽ ngăn chặn việc dự án/repository chiếm dụng toàn bộ runner bằng cách tạo ra hàng trăm job cần được xử lý cùng lúc. Thay vào đó, hàng đợi này sẽ ưu tiên phân phối các job cho các dự án/repository có số lượng job đã sử dụng shared runner thấp nhất trước

**Specific runner/Own runner** - do người dùng tự cài đặt và quản lý

Đây là một giải pháp sử dụng CI/CD của Gitlab hoàn toàn miễn phí. Bạn có server của mình, bạn muốn tự mình cài đặt, quản lý runner, chỉ định runner được sử dụng cho 1 hoặc nhiều dự án

**Group runner** - các runner thuộc group trên Gitlab

Khi người dùng tạo 1 runner thuộc loại `Group runner`, toàn bộ dự án/repository thuộc group sẽ có thể sử dụng các runner này. Các runner này sẽ sử dụng cơ chế hàng đợi (queue - FIFO - First In First Out) để xử lý các job

# Tính năng của Gitlab Runner

- Có thể chạy nhiều job CI/CD cùng một lúc miễn là bạn có đủ runner

- Cho phép tùy chọn môi trường chạy các job (Khi bạn chạy Gitlab runner bằng Docker)

- Job có thể chạy ở local/docker container/qua SSH

- Hỗ trợ  Bash, PowerShell Core và Windows PowerShell

- Hỗ trợ “caching” Docker container

- Tích hợp Prometheus metrics HTTP server

# Cơ chế hoạt động của Gitlab Runner

Về cơ chế, có thể hiểu đơn giản sẽ giống như một anh ""shipper"". Anh ""shipper"" này sẽ chuyên đi giao nhận các job từ Gitlab server đến `executor`. Gitlab sẽ đóng vai trò là một đơn vị vận chuyển

Runner sẽ đăng ký làm "shipper" cho Gitlab server:

- Sử dụng token của project/repository để đăng ký lên Gitlab server thông qua API

- Nhận kết quả đăng ký từ API

Runner nhận các job từ Gitlab server và chuyển tiếp đến `executor` để xử lý: (Quan trọng)

- Gọi API để kiểm tra có job phù hợp cần xử lý hay không, nếu có job phù hợp thì nhận về và giao cho `executor`

- Sau khi có được job phù hợp, runner sẽ nhận "job token" và "job payload" từ Gitlab server và chuyển nó đến `executor`

- `Executor` sau khi nhận được thông tin từ runner thì tiến hành lấy các tài nguyên/thông tin cần thiết từ Gitlab server để xử lý job bằng "job token"

- Xử lý xong job, `executor` sẽ đưa kết quả cho runner để gửi về Gitlab server

- Sau khi nhận được kết quả xử lý từ runner, Gitlab server hiển thị kết quả lên giao diện 

Hình ảnh minh họa

![](/cicd/images/gitlabrunner.png)
