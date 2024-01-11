# Volume trong Docker

## Tạo Volume

Rất dễ dàng để bạn có thể tạo được volume với docker bằng lệnh sau:

`docker volume create [volume_name]`

Lệnh này sẽ tạo ra một volume lưu trữ dữ liệu có thể sử dụng bởi một container cụ thể hoặc được chia sẻ giữa một nhóm các container. Bây giờ bạn có thể gắn volume này vào một vị trí bên trong container. Sau khi hoàn tất, bạn có thể dễ dàng lưu trữ hoặc truy cập dữ liệu container từ máy chủ

## Hiển thị volumes

Trong thực tế khi làm việc bạn sẽ phải quản lý một số lượng lớn các volume dữ liệu, điều quan trọng là bạn có thể xác định được đúng volume cụ thể mà bạn đang cần. Và bạn có thể dễ dàng liệt kê tất cả các volume hiện đang có bằng lệnh:

```sh
docker volume ls
```

**Output**

```sh
root@docker:~# docker volume ls
DRIVER    VOLUME NAME
local     tubt_vol
local     tubt_volume
```

Đối với Linux, các volume của bạn sau khi tạo sẽ được lưu trữ tại `/var/lib/docker/volumes` trên máy chủ của bạn

## Kiểm tra volumes

Lệnh kiểm tra docker volume sẽ cung cấp cho chúng ta thông tin chi tiết về một volume cụ thể. Nó hiển thị các thông tin về volume driver, mount point, scope hay labels (nhãn) của volume

```sh
docker volume inspect [volume_name]
```

**Output**

```sh
root@docker:~# docker inspect tubt_vol
[
    {
        "CreatedAt": "2023-08-31T09:17:01Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/tubt_vol/_data",
        "Name": "tubt_vol",
        "Options": null,
        "Scope": "local"
    }
]
```

Các thông tin mà lệnh này cung cấp rất hữu ích khi bạn cần khắc phục sự cố liên quan đến volume trên docker

## Xóa volumes

Nếu như bạn đang có volume không sử dụng và muốn xóa chúng đi để giải phóng không gian lưu trữ cho máy chủ của bạn

- Khi bạn muốn xóa một volume cụ thể:

```sh
docker volume rm [volume_name]
```

- Khi bạn muốn xóa nhiều volume cùng lúc

```sh
docker volume rm [volume_name1] [volume_name2] [volume_name3]...
```

- Ngoài ra khi bạn có một số lượng volume lớn cần xóa đi thì docker daemon còn cung cấp cho bạn một lệnh rất hữu ích đó là:

```sh
docker volume prune
```

Hoặc

```sh
docker system prune -a --volumes
```

**Khi sử dụng lệnh trên docker sẽ chỉ xóa đi những volume đang không được sử dụng bởi bất kỳ một container nào hiện có. Do đó lệnh này an toàn và được sử dụng rất thường xuyên**

## Tạo một container và mount tới volumes

Trong thực tế, chúng ta thường sẽ gắn luôn volume của mình vào các docker container trong câu lệnh khởi tạo. Lệnh sau đây sẽ chỉ cho các bạn cách tạo một docker container và mount volume vào container này. Nếu volume liên kết không có sẵn thì Docker Engine sẽ tạo một volume mới:

### Cách 1: Sử dụng tùy chọn `--volume`:

Cú pháp câu lệnh:

```sh
docker run --name [container_name] --volume "[volume_name]":/mnt [docker_image]
```

Ví dụ:

```sh
docker run -itd --name tubt_container --volume "tubt_volume":/mnt centos
```

Lệnh trên sẽ tạo một container có tên là `tubt_container` bằng cách sử dụng image `centos` và gắn volume `tubt_volume` vào thư mục `/mnt` của container này (Nếu image `centos` chưa có thì nó sẽ pull image đó từ docker registry về, nếu volume `tubt_volume` chưa được tạo trước đó thì nó sẽ được tạo và sau đó volume mới này sẽ được mount vào container)

Bạn cũng có thể kiểm tra thêm thông tin bằng lệnh kiểm tra container là `docker inspect tubt_volume` và kiểm tra phần `Mount` để xem volume đã được mount vào container hay chưa

```sh
"Mounts": [
    {
        "Type": "volume",
        "Name": "tubt_volume",
        "Source": "/var/lib/docker/volumes/tubt_volume/_data",
        "Destination": "/mnt",
        "Driver": "local",
        "Mode": "z",
        "RW": true,
        "Propagation": ""
    }
],
```

### Cách 2: Sử dụng tùy chọn `--mount`:

Sử dụng tùy chọn `--mount` sẽ đem lại kết quả tương tự như trên. Nhưng cú pháp sử dụng mount rõ ràng và dài dòng hơn sử dụng `--volume`. Trong khi `--volume` kết hợp tất cả chỉ trong một chuỗi thì `--mount` phân tách chúng. Đối với đa số các Linux sysadmin thì có lẽ `--mount` sẽ đem lại cái nhìn trực quan hơn so với `--volume`

Cú pháp câu lệnh:

```sh
docker run -itd --name [container_name] --mount source=[volume_name],destination=[path_in_container] [docker_image]
```

Ví dụ:

```sh
docker run -itd --name tubt_container1 --mount source=tubt_volume1,destination=/mnt centos
```

**Lưu ý nhỏ nhỏ nữa là chỉ có `--mount` là khả dụng với `swarm mode`, còn `--volume` thì không. Vì vậy `--mount` là cách duy nhất khả dụng khi sử dụng docker service**

## Pre-populating volumes

Nếu bạn tạo một container với một volume liên kết như trên khi volume đó chưa có sẵn và được Docker Engine tạo mới, vậy thì nội dung của vị trí đích trong container sẽ được Docker Engine tạo mới, vậy thì nội dung của vị trí đích trong container sẽ được sao chép vào volume, sau đó volume mới được mount với container

Ví dụ:

```sh
docker run -itd --name=nginx_container -v nginx_volume:/usr/share/nginx/html nginx:latest
```

Trước tiên, lệnh trên sẽ tạo volume `nginx_volume` và điền dữ liệu vào volume với nội dung là dữ liệu của vị trí đích `/usr/share/nginx/html` của hệ thống file bên trong container. Bây giờ, dữ liệu này sẽ có thể được truy cập bời các container đang mount đến volume `nginx_volume`. Tương tự bạn cũng có thể sử dụng cú pháp `--mount` để thực hiện lệnh tương tụ như trên:

```sh
docker run -itd --name=nginx_container --mount source=nginx_volume,destination=/usr/sharce/nginx/html nginx:latest
```

##  Sử dụng Read Only Volumes

Theo mặc định, tất cả container đều có quyền đọc ghi dữ liệu đối với volume được mount với chúng. Tuy nhiên trong thực tế vận hành, không phải container nào cũng cần ghi dữ liệu vào volume mà chỉ cần quyền đọc ghi dữ liệu. Trong trường hợp như vậy, bạn hoàn toàn có thể chỉ định quyền chỉ đọc cho container của mình:

```sh
docker run -itd --name=nginx=nginx_container -v nginx_volume:/usr/share/nginx/html:ro nginx:latest
```

hoặc

```sh
docker run -itd --name=nginx_container --mount source=nginx_volume,destination=/usr/share/nginx/html,readonly nginx:latest
```

Như vậy bạn chỉ cần thêm trường `:ro` với tùy chon `-v` (`--volume`) hoặc `readonly` với tùy chọn `--mount`, bạn sẽ có thể cấp quyền chỉ đọc dữ liệu từ volume cho container `nginx_container`

## Tạo volume sử dụng volume drivers cụ thể

Volume drivers là một cơ chế linh hoạt được Docker sử dụng để cung cấp quyền truy cập vào các remote mount, data encrypt (mã hóa dữ liệu) và các tính năng khác. Lệnh dưới đây là ví dụ về cách tạo một volume bằng cách sử dụng một volume driver cụ thể:

```sh
docker volume create --driver tubt/sshfs -o sshcmd=root@192.168.10.1:/home/session -o password=admin123 ssh_volume
```

Lệnh này tạo một docker volume bằng cách sử dụng volume driver `tubt/sshfs`/ Volume driver này cho phép bạn gắn các mục từ xa (remote directory) thông qua sử dụng sshfs

## Backup Container

Volume cung cấp một cách linh hoạt để bạn có thể backup các dữ liệu container quan trọng. Để ví dụ, trước hết mình sẽ tạo một container mới là `tubt_container`

```sh
docker run -itd -v /data --name tubt_container ubuntu:latest /bin/bash
```

Vậy là container `tubt_container` mount với một volume là `/data`. Bây giờ mình sẽ khởi động một container khác và thực hiện mount volume `data` từ `tubt_container`

Sau đó mình sẽ mount một thư mục cục bộ (local directory) trên hệ thống tệp là thư mục `/backup`. Ở đây mình thực thi lệnh tar để lưu trữ nột dung của `/data` vào `/backup` dưới dạng `backup.tar`

```sh
docker run --rm --volumes-from tubt_container -v $(pwd):/backup ubuntu:latest tar cvf /backup/backup.tar /data
```

Option `--volumes-from` được dùng để khởi động một container khác và mount toàn bộ volume đang liên kết với một container khác. Cơ chế này rất hữu dụng khi sao lưu vào khổi phục một container

## Restore Container

Rất dễ dàng để bạn có thể khôi phục container từ các tệp backup như trên. Bạn có thể khôi phục dữ liệu vào cùng một container hoặc vào một container khác. Ở đây mình sẽ khôi phục dữ liệu từ file `backup.tar` ở trên

```sh
docker run -v /data --name tubt_container01 ubuntu /bin/bash
```

Đầu tiên, tạo một container với `/data` volume. Sau đó, chúng ta sẽ trích xuất dữ liệu từ `backup.tar` trong volume mới này

```sh
docker run --rm --volumes-from tubt_container01 -v $(pwd):/backup ubuntu:latest bash -c "cd /data && tar xvf /backup/backup.tar --strip 1"
```

Như vậy, bạn hoàn toàn có thể tự động hóa việc backup và khôi phục dữ liệu container bằng cách sử dụng `docker volume`
