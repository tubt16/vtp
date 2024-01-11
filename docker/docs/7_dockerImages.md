# Docker Images

## Tổng quan về images Docker 

Image docker là một đơn vị đóng gói chứa mọi thứ cần thiết để 1 ứng dụng chạy. Nó bao gồm code, dependencies, OS constructs

Để có một image, ta có thể pull image từ registry hoặc build image từ Dockerfile

Khi 1 container được tạo, nó sẽ kéo (pull) các image từ Docker Hub (registry mặc định) về máy chạy local sau đó tạo container từ image đó

Images như 1 container đã bị stopped, vậy nên image còn được coi là `build-time` còn contianer thì được coi là `run-time`

![](/docker/images/dockerImages.png)

### Image và containers

Khi một container tạo và chạy từ 1 image, chúng sẽ trở nên phụ thuộc vào nhau và ta không thể xóa image cho đến khi container cuối cùng sử dụng nó bị xóa. Nếu cố gắng xóa 1 image mà không dừng hoặc xóa container sẽ dẫn đến lỗi

### Luôn tối ưu dung lượng của một image 

Mục đích của container là chạy ứng dụng hoặc 1 dịch vụ. Điều này có nghĩa là nó chỉ cần code của ứng dụng và các dependencies mà ứng dụng đó cần, nó không cần bất cứ thứ gì khác. Vậy nên image luôn có dung lượng thấp vì nó loại bỏ các phần không thiết yếu

Một điểm đáng lưu ý là **Image không chứa Kernel** - Tất cả các container chạy trên máy chủ Docker đều được chia sẻ quyền truy cập vào kernel của máy chủ đó

Một ví dụ điển hình về mức độ nhỏ của images là image chính thức của Alpine khoảng 7.34MB, có những image có thể nhỏ hơn. Một ví dụ điển hình hơn là image docker của ubuntu có dung lượng khoảng 63.2MB. Các image đều đã bị loại bỏ hầu hết các phần không cần thiết

### Pulling Images

Nơi lưu trữ image tại local thường được đặt tại `/var/lib/docker/image` đối với Linux và `C:\ProgramData\docker\windowsfilter` đối với Windows. Có thể sử dụng lệnh sau để kiểm tra xem có bất cứ image nào được lưu trữ cục bộ hay không

```sh
[root@jenkins1 ~]# docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
alpine       latest    8ca4688f4f35   6 weeks ago    7.34MB
ubuntu       18.04     f9a80a55f492   5 months ago   63.2MB
```

Quá trình để nhận được image về máy chủ docker được gọi là pulling. Vì vậy nếu muốn có 1 image mới về máy chủ docker, ta có thể sử dụng `pull` và kiểm tra với `docker images`

Ví dụ

```sh
[root@jenkins1 ~]# docker pull busybox
Using default tag: latest
latest: Pulling from library/busybox
3f4d90098f5b: Pull complete 
Digest: sha256:3fbc632167424a6d997e74f52b878d7cc478225cffac6bc977eedfe51c7f4e79
Status: Downloaded newer image for busybox:latest
docker.io/library/busybox:latest
[root@jenkins1 ~]# docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
alpine       latest    8ca4688f4f35   6 weeks ago    7.34MB
busybox      latest    a416a98b71e2   4 months ago   4.26MB
ubuntu       18.04     f9a80a55f492   5 months ago   63.2MB
```

Ta thấy được rằng các image vừa được pull đã có trên máy chủ docker 

### Image registries

Như đã đề cập ở các mục trước, image được lưu trữ tại nơi lưu trữ tập trung được gọi là image registries. Điều này giúp dễ dàng chia sẻ và truy cập. Registry phổ biến và được sử dụng mặc định là Docker Hub

Registry chứa 1 hoặc nhiều image repositories, trong image repositories chứa 1 hoặc nhiều image. Như hình sau đây chop thấy cách registry lưu trữ các image

![](/docker/images/registry.png)

### Repo chính thức và không chính thức

Docker Hub có 2 khái niệm là lưu trữ chính thức (offical repositories) và lưu trữ không chính thức (unoffical repositories) 

Các kho lưu trữ chính thức là nơi lưu trữ các image được kiểm duyệt bởi Docker Inc. Với các repo này sẽ được Docker đánh nhãn là Docker Offical Images

Các kho lưu trữ không chính thức không bị kiểm duyệt có thể không an toàn vì chúng không được kiểm định. Tuy nhiên không phải repo không chính thức nào cũng xấu

### Name và tag trong images

Để pull 1 image từ repo chính thức, ta cần chỉ ra tên của repo và tag của nó cách nhau bởi dấu `:`, nếu không chỉ ra tag, nó sẽ hiểu mặc định là tag `latest`

```sh
docker pull <repository>:<tag>
```

Ví dụ để thêm 1 image từ kho lưu trữ chính thức

```sh
[root@jenkins1 ~]# docker pull redis
Using default tag: latest
latest: Pulling from library/redis
578acb154839: Pull complete 
536258f1438d: Pull complete 
b2c17634dc83: Pull complete 
0a9ed92f5eca: Pull complete 
8e9838754832: Pull complete 
4f4fb700ef54: Pull complete 
8e7abba29a95: Pull complete 
Digest: sha256:d2f4d823a498f366c540b81e6b69bce397062f980f2e42340402225af0d9b5ab
Status: Downloaded newer image for redis:latest
docker.io/library/redis:latest
```

hoặc

```sh
[root@jenkins1 ~]# docker pull httpd:2.4
2.4: Pulling from library/httpd
578acb154839: Already exists 
c1a8c8567b78: Pull complete 
10b9ab03bf45: Pull complete 
74dbedf7ddc0: Pull complete 
6a3b76b70f73: Pull complete 
Digest: sha256:4e24356b4b0aa7a961e7dfb9e1e5025ca3874c532fa5d999f13f8fc33c09d1b7
Status: Downloaded newer image for httpd:2.4
docker.io/library/httpd:2.4
```

### Tìm kiếm Image từ Docker Hub

Lệnh `docker search` cho phép ta tìm kiếm trên Docker Hub từ CLI. Ví dụ để tìm các image alpine trên Docker Hub

```sh
[root@jenkins1 ~]# docker search alpine
NAME                               DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
alpine                             A minimal Docker image based on Alpine Linux…   10435     [OK]       
alpinelinux/docker-cli             Simple and lightweight Alpine Linux image wi…   9                    
alpinelinux/alpine-gitlab-ci       Build Alpine Linux packages with Gitlab CI      3                    
alpinelinux/gitlab-runner-helper   Helper image container gitlab-runner-helper …   4                    
alpinelinux/rsyncd                                                                 2                    
alpinelinux/alpine-drone-ci        Build Alpine Linux packages with drone CI       0                    
alpinelinux/unbound                                                                6                    
alpinelinux/apkbuild-lint-tools    Tools for linting APKBUILD files in a CI env…   0                    
alpinelinux/docker-compose         docker-compose image based on Alpine Linux      2                    
alpinelinux/gitlab-runner          Alpine Linux gitlab-runner (supports more ar…   5                    
alpinelinux/ansible                Ansible in docker                               8                    
alpinelinux/darkhttpd                                                              1                    
alpinelinux/docker-alpine                                                          0                    
alpinelinux/golang                 Build container for golang based on Alpine L…   2                    
alpinelinux/alpine-docker-gitlab   Gitlab running on Alpine Linux                  0                    
alpinelinux/docker-abuild          Dockerised abuild                               0                    
grafana/alpine                     Alpine Linux with ca-certificates package in…   6                    
alpinelinux/alpine-www             The Alpine Linux public website (www.alpinel…   0                    
alpinelinux/build-base             Base image suitable for building packages wi…   0                    
alpinelinux/turbo-paste            Alpine Linux paste service                      0                    
alpinelinux/mqtt-exec                                                              0                    
alpinelinux/git-mirror-syncd                                                       0                    
alpinelinux/package-builder        Container to build packages for a repository    1                    
alpinelinux/mirror-status                                                          0                    
alpinelinux/netbox                 dockerized netbox                               0 
```

- Cột `NAME` cho biết tên của image

- Cột `DESCRIPTION` mô tả ngắn gọn về images

- Cột `OFFICIAL` cho biết image chính thức hay không chính thức

Nếu chỉ muốn tìm những image chính thức hãy sử dụng lệnh sau để lọc:

```sh
docker search alpine --filter "is-official=true"
```

Output:

```sh
[root@jenkins1 ~]# docker search alpine --filter "is-official=true"
NAME      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
alpine    A minimal Docker image based on Alpine Linux…   10435     [OK]
```

### Images và layers

**Layer trong images**

Images Docker là 1 loạt các layer read-only được kết nối với nhau. Mỗi layer bao gồm 1 hoặc nhiều file

![](/docker/images/layer.png)

Trên thực tế, khi pull 1 image ta sẽ thấy các layer của image đó:

```sh
[root@jenkins1 ~]# docker pull redis
Using default tag: latest
latest: Pulling from library/redis
578acb154839: Pull complete 
536258f1438d: Pull complete 
b2c17634dc83: Pull complete 
0a9ed92f5eca: Pull complete 
8e9838754832: Pull complete 
4f4fb700ef54: Pull complete 
8e7abba29a95: Pull complete 
Digest: sha256:d2f4d823a498f366c540b81e6b69bce397062f980f2e42340402225af0d9b5ab
Status: Downloaded newer image for redis:latest
docker.io/library/redis:latest
```

Mỗi dòng sẽ kết thúc bằng `Pull complete` đại diện cho một layer đã được pull

![](/docker/images/layer1.png)

```sh
# docker insect redis
...
...
RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:ec983b16636050e69677eb81537e955ab927757c23aaf73971ecf5f71fcc262a",
                "sha256:9a603daeb2a51c50acd7acc0df31b1207103219f16e8d279db039703341f0451",
                "sha256:4465d19c7e1211527b34f919a664c033c4dd9b7d7b748b5267df11f8414d147f",
                "sha256:0adc6adbb7a4802855a2a15947402c51e7484efc4e01e346c55a3296376fda0e",
                "sha256:57fe7f7dc7d555517d182743e252c6313eb719dc0880b767ad4a390d1fbf414a",
                "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
                "sha256:a51f1d394661de18c1e8a9be6904cecef69290fe17f666e1e98eaf449c5cde90"
            ]
        },
...
...
```

### Chia sẻ layer giữa các image

Các image có thể chia sẻ các layer với nhau, điều này dẫn đến hiệu quả về không gian và hiệu suất. Khi pull image, các trạng thái layer được thông báo là Already exist tức là layer đó đã tồn tại và image sẽ sử dụng layer đó mà không cần pull layer mới
