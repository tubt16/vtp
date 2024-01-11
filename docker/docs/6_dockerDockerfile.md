# Giới thiệu 

Ý tưởng của Docker là tạo ra các container chứa các môi trường độc lập để khởi chạy và phát triển ứng dụng, hiểu đơn giản thì chứa mọi thứ ứng dụng có thể chạy được

Và để tạo được các container đó, chúng ta cần một Docker image. Tạo Docker container từ Docker Image cũng tương tự như cài win từ file ghost, bung file ghost là có tất cả mọi thứ mình cần. Vậy làm sao để tạo ra 1 Docker image, đó chính là viết `Dockerfile`

# Các thành phần trong Dockerfile 

`Dockerfile` sẽ gồm những lệnh sau

- `From`: Chỉ định base image. Base image thông thường sẽ được lấy từ Docker rigistry nơi lưu trữ và chia sẻ các image mà từ đó bạn có thể lấy về tùy chỉnh

- `RUN`: Dùng để thực thi một command bất kỳ trong quá trình build image, thường thì nó được dùng dể build các package trong image

- `CMD`: Dùng để thực thi một command bất kỳ trong quá trình chạy container. CMD sẽ không thực thi bất cứ thứ gì trong quá trình build image và mỗi Dockerfile chỉ chứa duy nhất một lệnh CMD

- `LABEL`: Dùng để cung cấp metadata cho image, nơi chứa thông tin về tác giả, các chú ý ...

- `EXPOSE`: Thiết lập port dể truy cập tới container sau khi đã khởi chạy

- `ENV`: Thiết lập các biến môi trường để sử dụng cho các câu lệnh trong quá trình build 

- `ADD` và `COPY`: Sao chép file, thư mục vào container 

- `ENDTRYPOINT`: Cung cấp một số lệnh măc định cùng tham số khi thực thi container

- `VOLUME`: Tạo một folder dùng để truy cập vào dữ liệu, folder được liên kết từ máy host và container

- `USER`: Dùng để chỉ định username hoăc UID được sử dụng trong quá trình tạo image cho các lệnh `RUN`, `CMD` và `ENTRYPOINT`

- `WORKDIR`: Thiết lập thư mục làm việc trong container cho các lệnh `COPY`, `ADD`, `RUN`, `CMD` va `ENTRYPOINT`

- `ARG`: Định nghĩa các biến để sử dụng trong build-time

- `ONBUILD`: Tạo một trigger cho image để thực thi khi nó được sử dụng làm base image cho việc build một image khác

- `STOPSIGNAL`: Chỉ định kí hiệu hệ thống dùng để stop container

- `HEALCHECK`:  Cung cấp phương thức cho Docker để kiểm tra container có hoạt động bình thường hay không 

- `SHELL`: Dùng để thay đổi các lệnh shell măc định 

Các thành phần cần quan tâm và được dùng nhiều nhất là `FROM`, `WORKDIR`, `RUN`, `COPY`, `ADD`, `EXPOSE`, `ENTRYPOINT` và `HEALTHCHECK`

**Với những lệnh này ta cần chú ý đến một chi tiết quan trọng đó là lệnh nào tạo `layer`, lệnh nào không**

# Layer

Quá trình build container từ image sẽ dựa trên một chuỗi layer. Các layer này tất nhiên là được tạo từ các lệnh ở Dockerfile. Chính Dockerfile sẽ định nghĩa cho Docker biết những layer đó và thứ tự tạo ra chúng. Và ta cần chú ý Docker có một cơ chế layer caching để không phải build lại layer nếu nó không có sự thay đổi so với lần build trước đó. Điều này rất quan trọng và là một trong những điều cơ bản đàu tiên khi thực hiện tối ưu Docker

Những lệnh sẽ tạo ra layer trong quá trình build là `RUN`, `COPY`, `ADD`

Mình sẽ demo về layer ở cuối của part 3