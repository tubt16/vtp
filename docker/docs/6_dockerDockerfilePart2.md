# Dockerfile

Nhắc lại về Dockerfile, Dockerfile là dạng text không có phần đuôi mở rộng, chứa các đặc tả về một trường thực thi phần mềm, cấu trúc cho `Docker image`. Từ những câu lệnh đó, Docker sẽ build ra Docker image

# Cú pháp của một Dockerfile

Cú pháp chung của một Dockerfile có dạng :

`INSTRUCTION arguments`

- `INSTRUCTION` là tên các chỉ thị có trong Dockerfile, mỗi chỉ thị thực hiện một nhiệm vụ nhất định, được Docker quy định. Khi khai báo, chỉ thị này phải được viết bằng chũ **IN HOA**

- Một Dockerfile bắt buộc phải bắt đầu bẳng chỉ thị `FROM` để khai báo đâu là image sẽ được sử dụng làm nền để xây dựng nên image của bạn

- `arguments` là nội dung của chỉ thị, quyết định chỉ thị sẽ làm gì

Ví dụ: 

```sh
FROM ubuntu:latest

RUN apt update && \
	apt install curl && \
	apt install git && \
	apt install vim && \
	apt install unzzip
```

# Các chị thị chính trong Dockerfile 

## FROM

Chỉ định rằng image nào sẽ được dùng làm image cở sở để quá trình build image thực hiện các câu lệnh tiếp theo. Các image base này sẽ được tải về từ Public registry hoặc Private registry riêng của mỗi người theo từng setup

**Cú pháp:**

```sh
FROM <image> [AS <name>]
FROM <image>[:<tag>] [AS <name>]
FROM <image>[@<digest>] [AS <name>]
```

Chỉ thị `FROM` là bắt buộc và phải được khai báo phía trên cùng của một Dockerfile

**Ví dụ:**

```sh
FROM ubuntu 
hoặc
FROM ubuntu:latest
```

## LABEL

Chỉ thị `LABEL` được dùng để thêm các thông tin metadata vào Dockerfile khi chúng được build. Chúng tồn tại dưới dạng các cặp *key-value*, được lưu trữ dưới dạng chuỗi

Có thể chỉ định nhiều label cho một Docker Image và tất nhiên mỗi cặp *key - value* phải là duy nhất. Nếu cùng một `key` mà được khai báo nhiều giá trị `value` thì giá trị được khai báo gần nhất sẽ ghi đè lên giá trị trước đó

**Cú pháp:**

```sh
LABEL <key>=<value> <key>=<value> <key>=<value> <key>=<value> ... <key>=<value> 
```

Bạn có thể khai báo metadata cho Image theo từng dòng chỉ thị hoặc có thể tách ra khai báo thành từng dòng riêng biệt

**Ví dụ:**

```sh
LABEL "Author"="Tubt"
LABEL "Project"="docker" "version"="latest"
```

Để xen thông tin meta của một Docker Image, ta sử dụng lệnh:

```sh
docker inspect <image_id>
```

## MAINTAINER

Chỉ thị `MAINTAINER` dùng để khai báo thông tin tác giả người viết ra file Dockerfile

**Cú pháp:**

```sh
MAINTAINER <name> [<email>]
```

**Ví dụ:**

```sh
MAINTAINER TuBT <tubui16091999@gmail.com>
```

Hiện này theo tài liệu chính thức từ bên phía Docker thì việc khai báo `MAINTAINER` đang dần được thay thế bằng `LABEL maintainer` bởi tính linh hoạt của nó khi ngoài thông tin về tên, email của tác giả thì ta có thể thêm nhiều thông tin tùy chọn khác qua các thẻ metadata và có thể lấy thông tin dễ dạng với câu lệnh `docker ispect <image_name>`

**Ví dụ:**

```sh
LABEL author="tubui16091999@gmail.com"
```

## EXPOSE

Lệnh `EXPOSE` thông báo cho Docker rằng vùng chứa sẽ lắng nghe trên các cổng mạng được chỉ định trong thời gian chạy. Bạn có thể chỉ định cổng lắng nghe trên TCP hoặc UDP và mặc định sẽ là TCP nếu giao thức không được chỉ định

**Cú pháp:**

```sh
EXPOSE <port> [<port>/<protocol>...]
```

**Ví dụ:**

```sh
EXPOSE 80/tcp
EXPOSE 80/udp
```

Ta cũng có thể sử dụng option `-p` với `docker run` để sử dụng cho cả tcp và udp

```sh
docker run -p 80:80/tcp -p 53:53/udp ...
```

## RUN

Chỉ thị `RUN` dùng để chạy một lệnh nào đó trong quá trình build image và thường là các câu lệnh Linux

Tùy vào image gốc được khai báo trong phần `FROM` thì sẽ có các câu lệnh tương ứng. Ví dụ để chạy câu lệnh update với `Ubuntu` sẽ là `RUN apt-get update -y`, còn đối với `CentOS` thì sẽ là `RUN yum update -y`. Kết quả của câu lệnh sẽ được commit lại, kết quả commit đó sẽ được sử dụng trong bước tiếp theo của Dockerfile

**Cú pháp:**

```sh
RUN <command>
RUN ["executable", "param1", "param2"]
```

**Ví dụ:**

```sh
RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME'
-----hoặc-----
RUN ["/bin/bash", "-c", "echo hello"]
```

Bạn có thể thực hiện nhiều câu lệnh trên nhiều dòng hoặc có thể thực hiện chúng trên một câu lệnh với dấu `/`:

```sh
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install unzip -y
```

hoặc

```sh
FROM ubuntu:latest
RUN apt-get update; \
	apt-get install unzip -y
```

## ADD

Chỉ thị `ADD` sẽ thực hiện sao chép các tập thư mục từ máy đang build hoặc remote file URLs từ `src` và thêm chúng vào filesystem của image `dest`

**Cú pháp:**

```sh
ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

Trong đó:

`src`: Có thể khai báo nhiều file, thư mục

`dest`: Phải là đường dẫn tuyệt đối hoặc có quan hệ chỉ thị đối với `WORKDIR`

**Ví du:**

```sh
ADD hom* /mydir
ADD hom?.txt /mydir
ADD test.txt /mydir
```

Ngoài ra ta cũng có thể phân quyền vào các file/thư mục vừa mới được copy 

```sh
ADD --chown=tubt:root files* /somedir
```

## COPY

Chỉ thị `COPY` cũng giống với `ADD` là copy file, thư mục từ `<src>` và thêm chúng vào `<dest>` của container. Khác với `ADD`, nó không hỗ trợ thêm các file remote file URLs từ các nguồn trên mạng

**Cú pháp:**

```sh
COPY [--chown=<user>:<group>] <src>... <dest>
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

**Ví dụ:**

```sh
COPY --chown=myuser:mygroup --chmod=644 files* /somedir/
```

## ENV

Chỉ thị `ENV` dùng để khai báo các biến môi trường. Các biến này được khai báo dưới dạng *key - value* bằng các chuỗi. Giá trị của các biến này sẽ có hữu hiệu cho các chỉ thị tiếp theo của Dockerfile

**Cú pháp:**

```sh
ENV <key>=<value> ...
```

**Ví dụ:**

```sh
ENV Domain="tubt.com"
ENV Port=80
ENV USERNAME="tubt" PASSWORD="secret"
```

Ngoài ra ta còn có thể khởi tạo hơạc thay đổi giá trị của biến môi trường bằng option `--env` trong câu lệnh khởi động contrainer:

```sh
docker run --env <key>=<value>
```

`ENV` chỉ được sử dụng trong các command `ADD`, `COPY`, `ENV`, `EXPOSE`, `FROM`, `LABEL`, `STOPSIGNAL`, `USER`, `VOLUME`, `WORKDIR`

## CMD 

Chỉ thị `CMD` định nghĩa các câu lệnh sẽ được chạy sau khi container được khởi động từ image đã build. Có thể khai báo được nhiều nhưng chỉ có duy nhất `CMD` cuối cùng được chạy

**Cú pháp:**

```sh
CMD ["executable","param1","param2"]
CMD ["param1","param2"] 
CMD command param1 param2
```

**Ví dụ**

```sh
CMD ["echo", "Tubt"]
```

## USER

Có tác dụng set `username` hoặc `UID` để sử dụng khi chạy image và khi chạy các lệnh có trong `RUN`, `CMD`, `ENTRYPOINT` sau nó:

**Cú pháp:**

```sh
USER <user>[:<group>]
hoặc
USER <UID>[:<GID>]
```

**Ví dụ:**

```sh
FROM ubuntu:latest
RUN useradd tubt
USER tubt
```

