# Docker command

Docker command bắt đầu bằng từ khóa `docker`. Cấu trúc của một command như sau:

`docker [OPTIONS] COMMAND [ARG...]`

Tuy nhiên có thể sử dụng theo cấu trúc sau:

`docker [MANAGERMENT_CATEGORY] [OPTIONS] COMMAND [ARG...]`

bạn có thể thấy gợi ý cách dùng bằng lệnh `docker` hoặc `docker --help`

```sh
root@docker:~# docker --help

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image
  exec        Execute a command in a running container
  ps          List containers
  build       Build an image from a Dockerfile
  pull        Download an image from a registry
  push        Upload an image to a registry
  images      List images
  login       Log in to a registry
  logout      Log out from a registry
  search      Search Docker Hub for images
  version     Show the Docker version information
  info        Display system-wide information

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx (Docker Inc., v0.11.2)
  compose*    Docker Compose (Docker Inc., v2.20.2)
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  plugin      Manage plugins
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Swarm Commands:
  swarm       Manage Swarm

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Global Options:
      --config string      Location of client config files (default "/root/.docker")
  -c, --context string     Name of the context to use to connect to the daemon
                           (overrides DOCKER_HOST env var and default context set
                           with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket to connect to
  -l, --log-level string   Set the logging level ("debug", "info", "warn", "error",
                           "fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "/root/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/root/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/root/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Run 'docker COMMAND --help' for more information on a command.

For more help on how to use Docker, head to https://docs.docker.com/go/guides/
```

Lưu ý `MANAGERMENT_CATEGORY` chính là phần management commands trong phần mô tả ở trên

## Version

`docker version`: Hiển thị thông tin chi tiết về các phiên bản docker (docker client và docker server)

```sh
root@docker:~# docker version
Client: Docker Engine - Community
 Version:           24.0.5
 API version:       1.43
 Go version:        go1.20.6
 Git commit:        ced0996
 Built:             Fri Jul 21 20:35:23 2023
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          24.0.5
  API version:      1.43 (minimum version 1.12)
  Go version:       go1.20.6
  Git commit:       a61e2b4
  Built:            Fri Jul 21 20:35:23 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.22
  GitCommit:        8165feabfdfe38c65b599c4993d227328c231fca
 runc:
  Version:          1.1.8
  GitCommit:        v1.1.8-0-g82f18fe
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

## Login

`docker login`: Đăng nhập vào docker registry. Docker registry sẽ là nơi lưu trữ và phân phối docker image của chính bạn

```sh
root@docker:~# docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: tubt16a6
Password: 
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

Như trên ta thấy mặc định docker sẽ đăng nhập vào Docker hub. Nếu muốn đăng nhập vào một registry khác ta chỉ cần thêm địa chỉ IP của host kèm theo port:

```sh
docker login <IP_HOST:8080>
```

## PS

`docker ps`: Liệt kê các container đang chạy

`docker ps -a`: Liệt kê tất cả các container đang có trong hệ thống (kể cả container đã bị stop)

```sh
root@docker:~# docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS          PORTS     NAMES
ea6af41c3247   centos    "/bin/bash"   26 minutes ago   Up 26 minutes             zealous_ellis

root@docker:~# docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                        PORTS     NAMES
d67b1f0777e8   ubuntu    "/bin/bash"   42 seconds ago   Exited (130) 23 seconds ago             friendly_hoover
ea6af41c3247   centos    "/bin/bash"   26 minutes ago   Up 26 minutes                           zealous_ellis
a4befa4af82b   centos    "-itd"        27 minutes ago   Created                                 sweet_williamson
```

Trong đó:

`CONTAINER_ID`: ID của container. Mỗi container sau khi tạo sẽ có một ID duy nhất

`IMAGE`: Tên của IMAGE

`COMMAND`: Command khi run container

`CREATED`: Thời gian container đã được start trên hệ thống

`STATUS`: `UP` có nghĩa là container đang chạy, còn `Exited` là đã stop

`PORT`: Hiển thị port mà host ánh xạ tới container

`NAMES`: Tên của container. Nếu không khai báo tên khi run container thì tên của container sẽ được sinh ra ngẫu nhiên

## Docker system

`docker system <COMMAND>`: Docker system là các lệnh dùng để quản lý docker

Các lệnh trong docker system bao gồm:

`docker system df`: Hiển thị thông tin dung lượng bộ nhớ, (disk space) được sử dụng bởi docker bao gồm image, container, volume, cache

```sh
root@docker:~# docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          2         2         309.1MB   0B (0%)
Containers      3         1         5B        5B (100%)
Local Volumes   0         0         0B        0B
Build Cache     0         0         0B        0B
```

`docker system events`: Hiển thị realtime event từ phía server

`docker system info`: Hiển thị thông tin của toàn hệ thống như số lượng container (đang chạy, dừng), số lượng image...

`docker system prune`: Xóa bỏ những container không sử dụng (Các container đang bị stop)

Với docker system thì lệnh hay sử dụng nhất là `docker system prune`. Tuy nhiên bạn cũng cần nắm cả 4 lệnh để có thể quản lý hệ thống docker của mình một cách toàn diện

## Prune

Đây là lệnh rất hữu ích khi sử dụng docker. Lệnh này giúp chúng ta loại bỏ tất cả container, image, network và build cache không sử dụng. Và một option bổ sung nữa đó là loại bỏ tất cả volume không sử dụng. Nghĩa là giải phóng kha khá dung lượng bộ nhớ

Khi thực thi lệnh này, docker sẽ có thông báo rõ những phần tử nào sẽ được xóa bỏ và cần xác nhận để thực hiện 

`docker system prune`: Loại bỏ tất cả container, image, network và build cache không sử dụng

```sh
root@docker:~# docker system prune
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - all dangling build cache

Are you sure you want to continue? [y/N] y
Deleted Containers:
d67b1f0777e8ea800c632e3debc2da30eede4fd9b1a641ec83ce5c27db318206
a4befa4af82bcd3b3ee6827da5961e366767f620bb25e0c575c953750a70854d

Total reclaimed space: 5B
```

`docker system prune -a --volumes`: Loại bỏ tất cả các container, image, network, build cache và volume không được sử dụng 

```sh
root@docker:~# docker system prune -a --volumes
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all volumes not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] y
Deleted Images:
untagged: ubuntu:latest
untagged: ubuntu@sha256:ec050c32e4a6085b423d36ecd025c0d3ff00c38ab93a3d71a460ff1c44fa6d77
deleted: sha256:01f29b872827fa6f9aed0ea0b2ede53aea4ad9d66c7920e81a8db6d1fd9ab7f9
deleted: sha256:bce45ce613d34bff6a3404a4c2d56a5f72640f804c3d0bd67e2cf0bf97cb950c

Total reclaimed space: 77.82MB
```

Lưu ý:

- `-a` là cách dùng ngắn hơn của option `--all` (Hiện này hầu hết các CLI đều cung cấp các option kiểu như vậy để rút gọn)

- Nếu không muốn xóa bỏ nhiều thành phần cùng một lúc, thì ta có thể sử dụng các lệnh khác như `docker image prune`, `docker container prune` để xóa bỏ những thành phần mong muốn

## Image

`docker image <COMMAND>`: Bao gồm các lệnh dùng để quản lý image

Các lệnh thường dùng với docker image

`docker images`: Hiển thị danh sách các image (có thể dùng docker images thay thế) với các thông tin về tên image, tag, image id, size và thời gian tạo

`docker image ls`: Tương tự như `docker images`

```sh
root@docker:~# docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
ubuntu       latest    01f29b872827   3 weeks ago     77.8MB
centos       latest    5d0da3dc9764   23 months ago   231MB
```

`docker image build`: Thực hiện build image từ Dockerfile (Sẽ thực hiện viết dockerfile ở các series sau)

`docker image history <IMAGE>`: Hiển thị history của một image như thời gian tạo, kích thước và cách image được tạo ra

```sh
root@docker:~# docker image history centos
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
5d0da3dc9764   23 months ago   /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B        
<missing>      23 months ago   /bin/sh -c #(nop)  LABEL org.label-schema.sc…   0B        
<missing>      23 months ago   /bin/sh -c #(nop) ADD file:805cb5e15fb6e0bb0…   231MB
```

`docker image inspect <IMAGE>`: Hiển thị thông tin chi tiết của một image, đặc biệt là các layer tạo ra nó (Định dạng JSON)

`docker image prune`: Xóa bỏ các image không sử dụng (dangling image)

`docker image push`: Push image của bạn lên docker registry. Để làm được điều này bạn cần phải `docker login` trước

`docker image rm <image_name>` hoặc `docker rmi <image_name>`: Xóa bỏ một hoặc nhiều image được chỉ định 

## Build 

`docker image build [OPTIONS] PATH | URL | -`

Cấu trúc hay sử dụng với lệnh docker build:

```sh
docker image build -t <my_image>:<tag_name> .
```

Trong đó option `-t` (`--tag`) dùng để đặt tên và gắn tag cho image (theo format `<image_name>:<tag_name>`) chú ý dấu `.`  ở cuối lệnh nhé. Dấu `.` để báo cho docker biết rằng sẽ build image từ Dockerfile ở folder hiện tại

## Containers

`docker container <COMMAND>`: Bao gồm các lệnh dùng để quản lý container

Các lệnh được dùng nhiều nhất khi sử dụng docker container 

`docker container create <IMAGE>`: Khởi tạo container từ một image

`docker container inspect <CONTAINER>`: Hiển thị chi tiết thông tin của container

`docker container logs <CONTAINER>`: Hiển thị logs của một container

`docker container ls`: Liệt kê các container hiện có

`docker container prune`: Xóa bỏ tất cả các container không hoạt động

`docker container rm`: Xóa bỏ một hoặc nhiều container 

`docker container run <IMAGE>`: Khởi tạo và chạy một container từ một image

`docker container start/stop`: Khởi chạy container hoặc chấm dứt hoạt động của một container đang chạy

## Create, start và run

Đây là 3 lệnh thường sử dụng khi bắt đầu làm việc với container. Để thực thi một container thì bạn cần khởi tạo container từ image và chạy nó. Để la được điều này bạn có 2 cách

Cách 1: Dùng docker container create để tạo container từ image và dùng docker container start để khởi chạy

```sh
docker container create --name <CONTAINER_NAME> <IMAGE>

docker container start CONTAINER
```

Cách 2: Dùng docker run để tạo container từ image và chạy nó 

```sh
docker container run --name <CONTAINER_NAME> -d <IMAGE> --rm
```

- `--rm`: Container sau khi stop sẽ tự động xóa

- `-d`: Chạy container dưới chế độ background

## Stop và kill

Có 2 cách để dừng một container khi nó đang chạy là `docker container stop ` và `docker container kill`

`docker container stop <CONTAINER>`: Mặc định cung cấp 10 giây để container có thể hoàn thành nốt các task của nó trước khi dừng hoạt động 

`docker container kill <CONTAINER>`: Dừng hoạt động ngay lập tức

Ta hoàn toàn có thể thay đổi giá trị 10 giây mặc định với option `--time/ -t`

## Compose

Docker compose dùng Docker Compose CLI thay vì Docker CLI. Nghĩa là thay vì bắt đầu bằng `docker` thì nó sẽ là `docker-compose`

Các lệnh thường sử dụng với docker compose:

`docker-compose build`: Dùng để build tất cả container được định nghĩa trong compose file

`docker-compose up`: Thực hiện tạo và khởi chạy các container

`docker-compose down`: Dùng để dừng các container và xóa hết những gì được tạo từ lệnh up 