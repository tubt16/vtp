# ENTRYPOINT & CMD

Để hiểu rõ hơn về `ENTRYPOINT` và `CMD` mình sẽ đưa ra 3 ví dụ đơn giản sau

Thực hiện tạo thư mục

```sh
mkdir -p ~/EntryCmd/cmd 
mkdir -p ~/EntryCmd/entry 
mkdir -p ~/EntryCmd/entrypointcmd
```

```sh
root@docker:~/EntryCMD# ls ~/EntryCMD/
cmd  entry  entrypointcmd
```

### CMD

Tạo một Dockerfile với nội dụng đơn giản

```sh
root@docker:~/EntryCMD# cat cmd/Dockerfile 
FROM ubuntu:latest
CMD ["echo", "hello"]
```

Build Dockerfile trên thành image

```sh
root@docker:~/EntryCMD# docker build -t printer:1.0 cmd
[+] Building 0.4s (6/6) FINISHED                                                                                       docker:default
 => [internal] load build definition from Dockerfile                                                                             0.0s
 => => transferring dockerfile: 78B                                                                                              0.0s
 => [internal] load .dockerignore                                                                                                0.0s
 => => transferring context: 2B                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                                 0.3s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                    0.0s
 => CACHED [1/1] FROM docker.io/library/ubuntu:latest@sha256:aabed3296a3d45cede1dc866a24476c4d7e093aa806263c27ddaadbdce3c1054    0.0s
 => exporting to image                                                                                                           0.0s
 => => exporting layers                                                                                                          0.0s
 => => writing image sha256:3c1b59e93c8935d4b927130bb7312eec0ad51de05d16c9c7e405c3bbf590c3bb                                     0.0s
 => => naming to docker.io/library/printer:1.0                                                                                   0.0s
```

Run container từ image

```sh
root@docker:~/EntryCMD# docker run printer:1.0
hello
```

**Đó là đối với `CMD`, ta cung cấp cả lệnh và đối số, ở đây lệnh là `echo` và đối số là `hello`, ta tiếp tục chuyển qua `ENTRY`**

### ENTRY

Tạo Dockerfile với nội dung

```sh
root@docker:~/EntryCMD# cat entry/Dockerfile 
FROM ubuntu:latest
ENTRYPOINT ["echo"]
```

Build Dockerfile trên thành Image

```sh
root@docker:~/EntryCMD# docker build -t printer:2.0 entry
[+] Building 0.4s (6/6) FINISHED                                                                                       docker:default
 => [internal] load .dockerignore                                                                                                0.0s
 => => transferring context: 2B                                                                                                  0.0s
 => [internal] load build definition from Dockerfile                                                                             0.0s
 => => transferring dockerfile: 76B                                                                                              0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                                 0.3s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                    0.0s
 => CACHED [1/1] FROM docker.io/library/ubuntu:latest@sha256:aabed3296a3d45cede1dc866a24476c4d7e093aa806263c27ddaadbdce3c1054    0.0s
 => exporting to image                                                                                                           0.0s
 => => exporting layers                                                                                                          0.0s
 => => writing image sha256:ab3256f3eb6569c72b6df38e3c5663167e77936ec3f3624cf031db287528d793                                     0.0s
 => => naming to docker.io/library/printer:2.0                                                                                   0.0s
```

Run container từ image trên

```sh
root@docker:~/EntryCMD# docker run printer:2.0

```

Sau khi chạy container trên nó sẽ in ra một dòng trống, nhưng nếu bạn đưa argument (đối số) vào trong câu lệnh thì nó sẽ in ra đối số đó

```sh
root@docker:~/EntryCMD# docker run printer:2.0 hello tubt
hello tubt
```

**Nếu chỉ dụng chỉ thị `ENTRYPOINT` người dùng cần tự truyền đối số vào câu lệnh. Vì vậy ta cần kết hợp cả `ENTRYPOINT` và `CMD`**

### ENTRYCMD

Tạo Dockerfile với nội dung

```sh
FROM ubuntu:latest
ENTRYPOINT ["echo"]
CMD ["hello", "tubt", "sysadmin"]
```

Build Dockerfile trên thành Image

```sh
root@docker:~/EntryCMD# docker build -t printer:3.0 entrypointcmd
[+] Building 0.2s (5/5) FINISHED                                                                                       docker:default
 => [internal] load build definition from Dockerfile                                                                             0.0s
 => => transferring dockerfile: 110B                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                0.0s
 => => transferring context: 2B                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                                 0.2s
 => CACHED [1/1] FROM docker.io/library/ubuntu:latest@sha256:aabed3296a3d45cede1dc866a24476c4d7e093aa806263c27ddaadbdce3c1054    0.0s
 => exporting to image                                                                                                           0.0s
 => => exporting layers                                                                                                          0.0s
 => => writing image sha256:419567f9af0166252f92b97c48dc1e9cb5e7bbbfcd48eb3dcf6363d7e345737e                                     0.0s
 => => naming to docker.io/library/printer:3.0                                                                                   0.0s
```

Run container từ image trên

```sh
root@docker:~/EntryCMD# docker run printer:3.0 
hello tubt sysadmin
```

Chúng ta cũng có thể ghi đè đối số bằng cách đưa nó vào trong lệnh

```sh
root@docker:~/EntryCMD# docker run printer:3.0 tubt1 tubt2 tubt3
tubt1 tubt2 tubt3
```

--> `ENTRYPOINT` sẽ có mức độ ưu tiên cao hơn `CMD`, `CMD` có thể thay đổi đối số được khi ta truyền đối số vào lệnh `docker run`, và nếu ta không truyền bất cứ đối số gì nó mới sử dụng các đối số mặc định được khai báo trong `Dockerfile`

**Nếu ta sử dụng cả `ENTRYPOINT` và `CMD` thì `ENTRYPOINT` sẽ cung cấp lệnh còn `CMD` sẽ cung cấp đối số. Đó là mục đích của việc sử dụng cả 2 cùng nhau.**

Mục đích thứ hai là bạn có thể cần phải có một số script cần thực thi và khởi tạo thứ gì đó và bạn muốn chạy nó trước, bạn sẽ đưa script đó vào `ENTRYPOINT` và sau đó, lệnh thực sự của bạn để bắt đầu quá trình sẽ được đưa vào `CMD`. Vì vậy chúng ta nên sử dụng `ENTRYPOINT` và `CMD` cùng nhau