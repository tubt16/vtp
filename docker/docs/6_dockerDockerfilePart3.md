# Cách viết Dockerfile 

Sau khi đã nắm được các thành phần của Dockerfile, việc tiếp theo là làm thế nào để viết Dockerfile từ các thành phần đó. Xem lại ví dụ ta có thể định hình ra được cấu trúc của Dockerfile sẽ gồm các phần chính:

- FROM: Xác định base Image, lệnh đầu tiên của bất cứ image nào

- Thiết lập WORKDIR: Chỉ rõ thư mục làm việc đẻ copy source hoặc cài đặt ứng dụng tại thư mục đó. Việc này rất cần thiết để tách biệt các ứng dụng đó với nhau

- Cài đặt ứng dụng: Sau khi đã có source code thì hẳn là run build và start application

- Tùy chỉnh cấu hình: Đây là bước cuối để chốt lại cái mà bạn định public với container được tạo ra từ Image định nghĩa bởi Dockerfile. Nào là port, cần chạy thêm command nào... Đây chính là nơi mà các bạn sẽ sử dụng những lệnh như `CMD`, `EXPOSE`, `ENTRYPOINT`. Và một điều lưu ý là ta cần phải `HEALTHCHECK` đối với một số container quan trọng

# Build Image sử dụng Dockerfile

Để build Image từ Dockerfile ta sử dụng lệnh sau:

```sh
docker build [OPTIONS] PATH | URL | -
```

Thông thường chúng ta thực thi lệnh này ngay tại folder chứa Dockerfile nên về `PATH` và `URL` không thường xuyên được sử dụng

Option hay sử dụng nhất khi build Image từ Dockerfile là `-t` hay `--tag` để gán tên và tag cho image

**Ví dụ:**

```sh
docker build -t demo_image:latest
```

Lệnh trên sẽ thực hiện build image với tên `demo_image` và tag là `latest`. Sau khi build image chúng ta thực hiện `docker run` để start container từ image đó.

# Viết Dockerfile và build thành Image hoàn chỉnh

Thực hiện tải xuống source html và nén lại thành file có đuôi `tar.gz`

```sh
wget https://www.tooplate.com/zip-templates/2137_barista_cafe.zip
```

```sh
FROM ubuntu:latest
LABEL "Author"="TuBT"
LABEL "Project"="barista_cafe"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install git -y
RUN apt install apache2 -y

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80

WORKDIR /var/www/html

VOLUME /var/log/apache2

ADD barista_cafe.tar.gz /var/www/html
```

Giải thích: https://stackoverflow.com/questions/44376852/how-to-start-apache2-automatically-in-a-ubuntu-docker-container#comment118667516_63851454

- `ENV DEBIAN_FRONTEND=noninteractive`: Đưa ra biến môi trường để ngăn việc tương tác khi build. Khi Chúng ta build Dockerfile trên mà không có dòng `ENV`, hệ thống sẽ hỏi chúng ta chọn timezone và điều đó sẽ dẫn đến việc ta cần tương tác với hệ thống. Vì thế ở đây mình đưa ra biến môi trường và đặt giá trị `noninteractive` cho nó để quá trình build hoàn tất mà không cần bất kỳ sự tương tác nào. Nó giống như khi bạn chạy `apt install git` và `apt install git -y` vậy, hệ thống sẽ hỏi mình có muốn cài hay không và mình phải nhập `y` để cài

- `CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]`: Nếu ta thay bằng dòng `CMD service apache2 start` thì sẽ không có tác dụng vì khi thực thi quy trình lệnh này `apache2` sẽ bị detach ra khỏi shell. Nhưng Docker chỉ hoạt động khi tiến trình còn hoạt động. Vậy nên giải pháp là chạy `apache2` ở `FOREGROUND`

Sau khi hoàn thiện Dockerfile ta tiến hành build nó thành một Image hoàn chỉnh

```sh
docker build -t barista_cafe:1.0 .
```

Lưu ý dấu `.` ở cuối cùng vì Dockerfile đang ở thư mục hiện tại mà mình đang đứng. Nếu chúng ta thực hiện build Dockerfile khi chúng ta không ở thư mục hiện hành chứa Dockerfile thì chúng ta cần phải khai báo đường dẫn tuyệt đối

**OUTPUT:**

```sh
root@docker:~/images/barista_cafe# docker build -t barista_cafe:1.0 .
[+] Building 25.6s (11/11) FINISHED                                                                                   docker:default
 => [internal] load .dockerignore                                                                                               0.0s
 => => transferring context: 2B                                                                                                 0.0s
 => [internal] load build definition from Dockerfile                                                                            0.0s
 => => transferring dockerfile: 360B                                                                                            0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                                0.6s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                   0.0s
 => [internal] load build context                                                                                               0.1s
 => => transferring context: 4.68MB                                                                                             0.1s
 => [1/5] FROM docker.io/library/ubuntu:latest@sha256:aabed3296a3d45cede1dc866a24476c4d7e093aa806263c27ddaadbdce3c1054          2.9s
 => => resolve docker.io/library/ubuntu:latest@sha256:aabed3296a3d45cede1dc866a24476c4d7e093aa806263c27ddaadbdce3c1054          0.0s
 => => sha256:445a6a12be2be54b4da18d7c77d4a41bc4746bc422f1f4325a60ff4fc7ea2e5d 29.54MB / 29.54MB                                0.7s
 => => sha256:aabed3296a3d45cede1dc866a24476c4d7e093aa806263c27ddaadbdce3c1054 1.13kB / 1.13kB                                  0.0s
 => => sha256:b492494d8e0113c4ad3fe4528a4b5ff89faa5331f7d52c5c138196f69ce176a6 424B / 424B                                      0.0s
 => => sha256:c6b84b685f35f1a5d63661f5d4aa662ad9b7ee4f4b8c394c022f25023c907b65 2.30kB / 2.30kB                                  0.0s
 => => extracting sha256:445a6a12be2be54b4da18d7c77d4a41bc4746bc422f1f4325a60ff4fc7ea2e5d                                       1.9s
 => [2/5] RUN apt update && apt install git -y                                                                                 13.0s
 => [3/5] RUN apt install apache2 -y                                                                                            7.6s
 => [4/5] WORKDIR /var/www/html                                                                                                 0.0s 
 => [5/5] ADD barista_cafe.tar.gz /var/www/html                                                                                 0.2s 
 => exporting to image                                                                                                          1.2s 
 => => exporting layers                                                                                                         1.2s 
 => => writing image sha256:c8e1203b923104aaecde3cb757ba4ad87eab685cab418019d84da99fdb498502                                    0.0s 
 => => naming to docker.io/library/barista_cafe:1.0                                                                             0.0s
```

Sau khi build image từ Docker file ta kiểm tra xem image đã được build thành công chưa

```sh
root@docker:~/images/barista_cafe# docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
barista_cafe   1.0       c8e1203b9231   52 seconds ago   258MB
```

Tiếp đến sau khi có image, chúng ta sẽ run image thành container

```sh
docker run -d --name barista_cafe_website -p 9090:80 barista_cafe:1.0
```

**OUTPUT:**

```sh
root@docker:~/images/barista_cafe# docker run -d --name barista_cafe_website -p 9090:80 barista_cafe:1.0
d7751fe448fe5bbe3487d5b58dd85ebd892bd3b75492c05bf18d06bb76bc9950

root@docker:~/images/barista_cafe# docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED         STATUS         PORTS                                   NAMESd7751fe448fe   barista_cafe:1.0   "/usr/sbin/apache2ct…"   7 seconds ago   Up 6 seconds   0.0.0.0:9090->80/tcp, :::9090->80/tcp   barista_cafe_website
```

Sau khi container đã run thành công, truy cập trình duyệt port 9090 để kiểm tra

![](/docker/images/barista_cafe_website.png)

# Thực hiện push image đã tạo lên docker hub

Truy cập vào https://hub.docker.com -> Repository để tạo Repo chứa image

![](/docker/images/pushImage.png)

Để đẩy image lên docker hub thì tên image phải là `<your_username>/<image_name>`. Vì vậy tên image của mình sẽ là `tubt16a6/barista_cafe`

Thực hiện build lại image

```sh
docker build -t tubt16a6/barista_cafe:1.0 .
```

Giờ tôi muốn đẩy image này lên docker hub, trước tiên ta cần login docker hub từ máy chủ

```sh
root@docker:~/images/barista_cafe# docker login
Authenticating with existing credentials...
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

Do mình đã đăng nhập từ trước nên ở đây không hỏi

Thực hiện push image lên docker hub

```sh
docker push tubt16a6/barista_cafe:1.0
```

**OUTPUT:**

```sh
root@docker:~/images/barista_cafe# docker push tubt16a6/barista_cafe:1.0 
The push refers to repository [docker.io/tubt16a6/barista_cafe]
90f4571bced3: Pushed 
5f70bf18a086: Pushed 
c5f539f9a42b: Pushed 
99f57b10a9f5: Pushed 
dc0585a4b8b7: Mounted from library/ubuntu 
1.0: digest: sha256:684cc0a1b867172e7f08c4c252d5b24effcafba028ee6ef91b7a00e1b5249964 size: 1370
```

Thực hiện kiểm tra trên docker hub xem image đã được push lên thành công hay chưa

![](/docker/images/pushImageSuccess.png)

# Layer khi viết docker file

Nhắc lại về layer, quá trình build một container từ image sẽ dựa trên một chuỗi layer. Các layer này được tạo ra từ các dòng lệnh trong Dockerfile. Dockerfile sẽ định nghĩa cho Docker biết những layer đó và thứ tự tạo ra chúng

Vằ có một điểm ta cần phải chú ý đó là Docker có một cơ chế layer caching để không phải thực hiện việc build lại `layer` nếu nó không có sự thay đổi nào so với lần build trước đó. Điều này rất quan trọng và là một trong những điều cơ bản đầu tiên khi thực hiện tối ưu Docker

Những lệnh sẽ tạo ra `layer` trong quá trình build là `RUN`, `COPY`, `ADD`

Chúng ta hãy cùng xem tất cả các `layer` được tạo ra bằng lệnh `history`

```sh
docker history <image>
```

**OUTPUT:**

```sh
root@docker:~/images/barista_cafe# docker history barista_cafe:1.0 
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
c8e1203b9231   29 minutes ago   ADD barista_cafe.tar.gz /var/www/html # buil…   5.23MB    buildkit.dockerfile.v0
<missing>      29 minutes ago   VOLUME [/var/log/apache2]                       0B        buildkit.dockerfile.v0
<missing>      29 minutes ago   WORKDIR /var/www/html                           0B        buildkit.dockerfile.v0
<missing>      29 minutes ago   EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0
<missing>      29 minutes ago   CMD ["/usr/sbin/apache2ctl" "-D" "FOREGROUND…   0B        buildkit.dockerfile.v0
<missing>      29 minutes ago   RUN /bin/sh -c apt install apache2 -y # buil…   56.3MB    buildkit.dockerfile.v0
<missing>      29 minutes ago   RUN /bin/sh -c apt update && apt install git…   119MB     buildkit.dockerfile.v0
<missing>      29 minutes ago   ENV DEBIAN_FRONTEND=noninteractive              0B        buildkit.dockerfile.v0
<missing>      29 minutes ago   LABEL Project=barista_cafe                      0B        buildkit.dockerfile.v0
<missing>      29 minutes ago   LABEL Author=TuBT                               0B        buildkit.dockerfile.v0
<missing>      2 weeks ago      /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B        
<missing>      2 weeks ago      /bin/sh -c #(nop) ADD file:aa9b51e9f0067860c…   77.8MB    
<missing>      2 weeks ago      /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B        
<missing>      2 weeks ago      /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B        
<missing>      2 weeks ago      /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH     0B        
<missing>      2 weeks ago      /bin/sh -c #(nop)  ARG RELEASE                  0B  
```

Từ đầu ra của lệnh trên ta cần chú ý đến cột SIZE. Các lệnh tạo ra `layer` đều có size > 0 và đó là các lệnh `RUN` và `ADD`. Về nguyên tắc thì khi build image, nếu có sự thay đổi so với layer trước thì một layer mới sẽ được tạo ra và các lệnh có `SIZE` > 0 nó làm thay đổi `layer` hiện tại nên dĩ nhiên nó sẽ tạo ra một layer mới.

**Như vậy chúng ta đã viết xong một Dockerfile hoàn chỉnh và hiểu về layer trong quá trình run một container từ image**