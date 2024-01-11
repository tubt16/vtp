# Docker logs

Để kiểm tra nhật ký của container và hiểu sâu về nó ta cần thực hiện những bước sau đây

Thực hiện pull image nginx về máy

```sh
docker pull nginx
```

Xem thông tin chi tiết của image `nginx` vừa mới pull về (Output của lệnh trả về JSON format)

```sh
docker inspect nginx
```

```sh
root@docker:~# docker inspect nginx
[
    {
        "Id": "sha256:eea7b3dcba7ee47c0d16a60cc85d2b977d166be3960541991f3e6294d795ed24",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:104c7c5c54f2685f0f46f3be607ce60da7085da3eaa5ad22d3d9f01594295e9c"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-08-16T09:50:55.765544033Z",
        "Container": "50b019921f82064e1d8af7e2723929d4c5fafcfd6d8b03595711bd1e455dd3c4",
        "ContainerConfig": {
            "Hostname": "50b019921f82",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.2",
                "NJS_VERSION=0.8.0",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"nginx\" \"-g\" \"daemon off;\"]"
            ],
            "Image": "sha256:d59ed5fe14c2a306f94488f41ddc8fb060312ee31997f5e077a4c4b29b19114e",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "DockerVersion": "20.10.23",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.2",
                "NJS_VERSION=0.8.0",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "sha256:d59ed5fe14c2a306f94488f41ddc8fb060312ee31997f5e077a4c4b29b19114e",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 186639842,
        "VirtualSize": 186639842,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/976a058985251af415bd1ca605ffc7c798eccd49c53581fcbaa3e5f9f2845564/diff:/var/lib/docker/overlay2/8e7f4abeeb5de38b7c6d268de744cf81a318a52a301c9671d5616498d035d61e/diff:/var/lib/docker/overlay2/b88fa44494374e1099d93d2034d7503c34b25e23c5d5c83d137971af2dbcacef/diff:/var/lib/docker/overlay2/2e91a3889892b7b7108b9cfe9f3f16cb0658c0c3be517e41cdbf197f458c0dee/diff:/var/lib/docker/overlay2/a25eb8ff27a2d832e81229fcdf70069a8b8daef10b26d5cbcd78c3324bc64a35/diff:/var/lib/docker/overlay2/4815148652a322ca565966c5e010a4542c0556e3cc462d05b95b5d4ee4e511f8/diff",
                "MergedDir": "/var/lib/docker/overlay2/af753f67b910bb50c43a6fccf79638b0682807ddcd166db68793fd7a46ea0ee4/merged",
                "UpperDir": "/var/lib/docker/overlay2/af753f67b910bb50c43a6fccf79638b0682807ddcd166db68793fd7a46ea0ee4/diff",
                "WorkDir": "/var/lib/docker/overlay2/af753f67b910bb50c43a6fccf79638b0682807ddcd166db68793fd7a46ea0ee4/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:511780f88f80081112aea1bfdca6c800e1983e401b338e20b2c6e97f384e4299",
                "sha256:4713cb24eeff341d0c36343149beba247572a5ff65c2be5b5d9baafb345c7393",
                "sha256:d0a62f56ef413f60049bc87e43e60032b2a2ab8d931e15b86ee0286c85ae91a2",
                "sha256:8a7e12012e6f60450e6d2d777b2a2c2256d34a0ccd84d605f72cc5329a87c8b8",
                "sha256:e161c3f476b5199ab13856c7e190ed12a6562b7be059c7026ae9f594e1abbcaf",
                "sha256:6fb960878295b567d25900b590157b976d080340caeaa8bf8c46d38c01b4537d",
                "sha256:563c64030925e9016a2329d3a2b7d47b0c90931baf5d2d0aa926c4c8d94ab894"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
```

Đầu ra của lệnh trên trả về rất nhiều thông tin nhưng trong phần này chúng ta chỉ nên quan tâm 2 chỗ

```sh
"Cmd": [
    "nginx",
    "-g",
    "daemon off;"
],
```

```sh
"Entrypoint": [
    "/docker-entrypoint.sh"
],
```

**Khi chúng ta thực hiện và đặt tên cho image. Nó sẽ thực hiện chạy script `docker-entrypoint.sh` như trong mô tả. Sau đó nó sẽ lệnh trong CMD và chúng ta sẽ không thể nhìn thấy đầu ra của các lệnh này khi chúng ta chạy ở chế độ nền**

# Trường hợp 1: Run container dưới chế độ nền

Thực hiện run container từ image `nginx` đã pull trước đó dưới chế độ nền

```sh
docker run -d -P nginx
```

- `-d`: Option này thể hiện việc run container dưới chế độ nền

- `-P`: Option này sẽ mapping port của HOST một cách ngẫu nhiên với port của container

```sh
58c2aff38e744d74e4e7cf4f349f128e22695b4c7ba52744c8c45389e0291a2b
```

Kiểm tra logs của container

```sh
docker logs <container_name>
```

```sh
root@docker:~# docker logs awesome_murdock
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/08/31 07:23:20 [notice] 1#1: using the "epoll" event method
2023/08/31 07:23:20 [notice] 1#1: nginx/1.25.2
2023/08/31 07:23:20 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2023/08/31 07:23:20 [notice] 1#1: OS: Linux 5.15.0-1039-gcp
2023/08/31 07:23:20 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/08/31 07:23:20 [notice] 1#1: start worker processes
2023/08/31 07:23:20 [notice] 1#1: start worker process 29
2023/08/31 07:23:20 [notice] 1#1: start worker process 30
```

**Từ đầu ra của lệnh trên, ta thấy được nó đã chạy file script `/docker-entrypoint.sh` như tôi đã nói ở trên và tập lệnh đó trả về một số kết quả. Sau đó nó tiếp tục chạy các lệnh khác trong CMD (`nginx`, `-g`, `daemon off`)**

**Và đó là nhật ký đầu ra của lệnh khi chúng ta run container**

# Trường hợp 2: Run container

Bây giờ chúng ta không cung cấp option `-d` khi chạy container

```sh
docker run -P nginx
```

```sh
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/08/31 07:53:37 [notice] 1#1: using the "epoll" event method
2023/08/31 07:53:37 [notice] 1#1: nginx/1.25.2
2023/08/31 07:53:37 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2023/08/31 07:53:37 [notice] 1#1: OS: Linux 5.15.0-1039-gcp
2023/08/31 07:53:37 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/08/31 07:53:37 [notice] 1#1: start worker processes
2023/08/31 07:53:37 [notice] 1#1: start worker process 29
2023/08/31 07:53:37 [notice] 1#1: start worker process 30
```

Nếu chúng ta không chạy container ở chế độ nền thì bạn sẽ thấy đầu ra ngày trên màn hình của mình. Và sau khi chạy xong câu lệnh chúng ta cũng sẽ exec vào container luôn. 

Để thoát ra chúng ta phải bấm `Crtl + C` và điều đó cũng sẽ kill luôn process, container sẽ stop

```sh
root@docker:~# docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS                                     NAMES
ccf942f7620e   nginx     "/docker-entrypoint.…"   7 minutes ago    Exited (0) 19 seconds ago                                             silly_chebyshev
58c2aff38e74   nginx     "/docker-entrypoint.…"   37 minutes ago   Up 37 minutes               0.0.0.0:32768->80/tcp, :::32768->80/tcp   awesome_murdock
```

# Sử dụng docker logs hiệu quả

Chúng ta sẽ thực hiện fix lỗi bằng cách đọc log trả về khi chạy lệnh `docker logs`

Thực hiện run container ở chế độ nền

```sh
root@docker:~# docker run -d -P mysql:5.7
Unable to find image 'mysql:5.7' locally
5.7: Pulling from library/mysql
70e9ff4420fb: Pull complete 
7ca4383b183f: Pull complete 
3e282e7651b1: Pull complete 
1ffa0e0ca707: Pull complete 
6eb790cf6382: Pull complete 
b4b277ff2929: Pull complete 
692fe4469429: Pull complete 
c0d447d97bbd: Pull complete 
99ee594517ba: Pull complete 
a9ae52de4d77: Pull complete 
66cc05a182b5: Pull complete 
Digest: sha256:2c23f254c6b9444ecda9ba36051a9800e8934a2f5828ecc8730531db8142af83
Status: Downloaded newer image for mysql:5.7
1495b081c0e4a602161967eddaa74019491791c0022a7db9e50a03d5b7a2226c
```

Kiểm tra xem container đã được chạy chưa

```sh
root@docker:~# docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                     NAMES
ccf942f7620e   nginx     "/docker-entrypoint.…"   18 minutes ago   Up 5 minutes    0.0.0.0:32770->80/tcp, :::32770->80/tcp   silly_chebyshev
58c2aff38e74   nginx     "/docker-entrypoint.…"   49 minutes ago   Up 49 minutes   0.0.0.0:32768->80/tcp, :::32768->80/tcp   awesome_murdock
```

Oops! Đã xảy ra lỗi ở đây. Tôi đã run container `mysql:5.7` nhưng khi kiểm tra thì lại không hề thấy

Kiểm tra tất cả container trên máy

```sh
root@docker:~# docker ps -a
CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS                     PORTS                                     NAMES
1495b081c0e4   mysql:5.7   "docker-entrypoint.s…"   7 minutes ago    Exited (1) 7 minutes ago                                             lucid_mcnulty
ccf942f7620e   nginx       "/docker-entrypoint.…"   22 minutes ago   Up 8 minutes               0.0.0.0:32770->80/tcp, :::32770->80/tcp   silly_chebyshev
58c2aff38e74   nginx       "/docker-entrypoint.…"   52 minutes ago   Up 52 minutes              0.0.0.0:32768->80/tcp, :::32768->80/tcp   awesome_murdock
```

Giờ thì chúng ta đã thấy container này rồi nhưng STATUS trả về lại là `Exited`. Container đã không chạy. Vì vậy để biết được nguyên nhân tại sao container không chạy ta hãy đi check log bằng `docker logs`

```sh
docker logs lucid_mcnulty
```

Output

```sh
root@docker:~# docker logs lucid_mcnulty
2023-08-31 08:08:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 5.7.43-1.el7 started.
2023-08-31 08:08:19+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2023-08-31 08:08:19+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 5.7.43-1.el7 started.
2023-08-31 08:08:19+00:00 [ERROR] [Entrypoint]: Database is uninitialized and password option is not specified
    You need to specify one of the following as an environment variable:
    - MYSQL_ROOT_PASSWORD
    - MYSQL_ALLOW_EMPTY_PASSWORD
    - MYSQL_RANDOM_ROOT_PASSWORD
```

**Từ log trên chúng ta đã biết được lỗi và nguyên nhân dẫn đến viêc container không chạy. Bản chất khi run container `mysql:5.7` trên nó cũng sẽ chạy một Entrypoint script nhưng file này yêu cầu chúng ta cần khai báo 1 trong các giá trị bên dưới làm biến môi trường**

Thực hiện như sau:

```sh
root@docker:~# docker run -d -P -e MYSQL_ROOT_PASSWORD=mypass mysql:5.7
75cd77f0e3b8050316fa4d3d283b85759ee910d895d94f17e0cab0177fcf4f94
```

Kiểm tra container đã được chạy chưa

```sh
root@docker:~# docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED             STATUS             PORTS                                                                                        NAMES
75cd77f0e3b8   mysql:5.7   "docker-entrypoint.s…"   22 seconds ago      Up 21 seconds      0.0.0.0:32776->3306/tcp, :::32776->3306/tcp, 0.0.0.0:32775->33060/tcp, :::32775->33060/tcp   elastic_carver
ccf942f7620e   nginx       "/docker-entrypoint.…"   43 minutes ago      Up 30 minutes      0.0.0.0:32770->80/tcp, :::32770->80/tcp                                                      silly_chebyshev
58c2aff38e74   nginx       "/docker-entrypoint.…"   About an hour ago   Up About an hour   0.0.0.0:32768->80/tcp, :::32768->80/tcp                                                      awesome_murdock
```

**Kết quả container đã chạy khi ta khai báo biến `MYSQL_ROOT_PASSWORD` với option `-e`. Đó là cách mã chúng ta sử dụng `docker logs` để gỡ lỗi khi vô tình gặp phải**

