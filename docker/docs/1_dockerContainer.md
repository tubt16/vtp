# Container

Container là giải pháp ảo hóa, giúp giải quyết vấn đề làm sao để chuyển giao phần mềm một cách đáng tin cậy (không phát sinh lỗi) giữa các môi trường máy tính khác nhau. Chẳng hạn như giữa máy tính của lập trình viên với máy tính của tester, giữa môi trường stagging (mt tiền thực tế) với môi trường thực tế, hay thậm chí giữa máy chủ vật lý đặt tạo Data center với máy ảo trên Cloud

Container giải quyết vấn đề trên bằng việc tạo ra môi trường bị cô lập (isolated) chứa mọi thứ mà phần mềm cần để có thể chạy được bao gồm mã nguồn, các thư viện runtime, các thư viện hệ thống, các công cụ hệ thống...(gọi là sự phụ thuộc hoặc các phụ thuộc) mà không bị các yếu tố liên quan đến môi trường hệ thống làm ảnh hưởng tới, cũng như không làm ảnh hưởng tới phần còn lại của hệ thống

Thông thường các container cho người dùng sự cải thiện về hiệu suất. Bằng cách tránh các hệ điều hành riêng biệt và thay vì sử dụng một share core, người dùng có thể tối ưu hóa CPU, dung lượng lưu trữ và hiệu quả bộ nhớ

# Docker

Docker là một công cụ cho phép user tạo container images, đẩy hoặc kéo images từ các registries bên ngoài, chạy và quản lý container trong nhiều môi trường khác nhau

Docker là một ứng dụng mã nguồn mở cho phép đóng gói các ứng dụng, các phần mềm phụ thuộc lẫn nhau trong cùng một container. Container này sau đó có thể mang đi triển khai trên bất kì một hệ thống Linux phổ biến nào. Các container hoàn toàn độc lập với các container khác nhưng đều dùng chung kernel của HostOS

Docker có 2 phiên bản phổ biến:
- Docker Community Edition (CE): Là phiên bản miễn phí và chủ yếu dựa vào các sản phẩm mã nguồn mở khác
- Docker Enterprise (EE): Phiên bản dành cho các doanh nghiệp, khi sử dụng phiên bản này sẽ nhận được support từ nhà phát hành, ngoài ra còn có thêm tính năng quản lý và bảo mật

Các thành phần trogn Docker Engine:

![](/docker/images/docker_element.png)

- Docker Daemon: Chạy trên host, đóng vai trò là server, nhận các Restful request từ Docker Client và thực thi nó. Là một lightweight runtime giúp build, run, quản lý các container và các thành phần liên quan khác

- Docker client (CLI): Cung cấp giao diện dòng lệnh cho người dùng, đồng thời cũng gửi request đến Docker daemon 

- Docker Registry: Nơi lưu trữ Docker image. Docker Hub là một registry công khai mà bất cứ ai cũng có thể sử dụng và Docker được cấu hình để tìm kiếm image trên Docker Hub theo mặc định. Bạn thậm chí có thể chạy registry riêng của mình. Có 2 loại registry là public và private registry (tương tự như github và gitlab)

Storage trong Docker là một tính năng quản lý data của Docker. Data ở đây có thể hiểu là các file được sinh ra trong quấ trình chạy ứng dụng ví dụ như log, data, report...

Docker Storage có 3 option là volumes, bind mounts, tmpfs mounts. Tùy vào nhu cầu mà chúng ta có thể sử dụng option phù hợp với mình:

- Volumes: Mount-point nằm ở `/var/lib/docker/volumes` của Docker host và được quản lý bằng Docker

- Bind mounts: mount-points có thể nằm ở bất kỳ đâu trong Docker Host mà không bị quản lý bởi Docker 

- tmpfs mounts: data sẽ được lưu vào memory của Docker Host và sẽ mất đi khi khởi động lại hoặc stop container

### Các thuật ngữ hay gặp trong Docker:

- Docker image: Một Docker image là một read-only template dùng để tạo ra các containers. Image được cấu tạo theo dạng layer và tất cả các layer đều là read-only. Một image có thể được tạo ra dựa trên một image khác với một số tùy chỉnh bổ sung. Nói ngắn gọn, Docker image là nơi lưu trữ các cài đặt môi trường như OS, package, phần mềm cần chạy 

- Dockerfile: Là một dạng file text không có phần đuôi mở rộng, chứa các đặc tả về một trường thực thi phần mềm, cấu trúc cho Docker image. Từ những câu lệnh đó, Docker sẽ build ra docker image

- Docker Container: Được tạo ra từ Docker image, là nơi chứa mọt thứ cần thiết để có thể chạy được ứng dụng. Là ảo hóa nhưng container lại rất nhẹ, có thể coi như là một process của hệ thống. Chỉ mất vài giây để start stop hoặc restart một container. Với một máy chủ vật lý, thay vì chạy một vài máy ảo truyền thống thì ta có thể chạy được vài chục, thậm chí vài trăm Docker Container

- Docker Network: Có nhiệm vụ cung cấp private network (VLAN) để các container trên một host có thể liên lạc với nhau, hoặc các container trên nhiều host có thể liên lạc được với nhau

- Docker Volume: Là cơ chế tạo và sử dụng dữ liệu của Docker, có nhiệm vụ lưu trữ dữ liệu độc lập với vòng đời của container

- Docker Compose: Là công cụ dùng để định nghĩa và run multi-container cho Docker application. Với compose bạn sử dụng YAML để config các services cho application của bạn. Sau đó dùng Command để create và run từ những config đó. Cụ thể:
	- Khai báo app's environment trong Dockerfile
	- Khai báo các service cần thiết để chạy application trong file docker-compose.yml
	- Run docker-compose up để start và run app

- Docker Hub: Gần tương tự như github nhưng dành cho DockerFile và Docker Image. Ở đây có những DockerFile, Images của người dùng cũng như những bản chính thức từ các nhà phát triển lớn như Google, Oracle ... Ngoài ra Docker Hub còn cho phép quản lý các image với những câu lệnh giống như Github như push, pull ... để bạn có thể dễ dàng quản lý image của mình

### Các câu lệnh cơ bản trong Docker

- List các container đang chạy: `docker ps`

- List tất cả các container trên máy chủ: `docker ps -a`

- Tạo mới một container: `docker create -itd centos` (centos là tên của image)

- Khởi chạy 1 container: `docker run -itd centos`

- Xóa 1 container: `docker rm my_container`

- Xóa 1 container đang chạy: `docker rm -f my_container`

- Xóa tất cả các container: `docker rm -f $(docker ps -aq)`

- Start, stop và restart container: `docker start/stop/restart my_container`

- Kiểm tra log của container: `docker log my_container`

- Kiểm tra thông tin chi tiết của container `docker inspect my_container`

- Hiển thị tài nguyên đang sử dụng của container `docker stats my_container`

- Hiển thị các port được map `docker port my_container`

- Hiển thị các thay đổi trong file system kể từ lúc khởi tạo container `docker diff my_container`

- Thực thi một lệnh trong container `docker exec my_container uptime`

- Tạo 1 image từ container đang chạy: `docker container commit my_container my_new_image`

- Hiển thi danh sách image đang có `docker images`

- Tải image từ registry về máy: `docker image pull centos` (image có tên `centos`)

- Upload 1 image lên registry: `docker image push tubt16a6/centos:1.0` (Trong đó `tubt16a6` là tên tài khoản dockerhub, `centos` là tên của image local, `1.0` là tag gắn cho image)

- Lưu image thành 1 file nén: `docker image load -o /mnt/image_name.tar image_name`

- Xóa image: `docker rmi my_image`

