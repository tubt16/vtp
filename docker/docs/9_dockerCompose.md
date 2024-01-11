# Bài toán

Chúng ta muốn sử dụng Docker cho 

- Dự án mới 

- Hoặc là dự án đang phát triển

-> Vậy chúng ta làm như thế nào ?

Qua những bài viết trước, chúng ta hoàn toàn có thể sử dụng `Dockerfile`, chúng ta sẽ viết `Dockerfile` cài đặt tất cả môi trường cần thiết như (PHP, mysql, apache, redis ...) lên một container `duy nhất`. Và sau đó chạy project trên container `duy nhất` đó

-> Tuy nhiên:

- Nếu bạn muốn kết hợp nhiều image có sẵn trên DockerHub thì phải làm thế nào ?

- Nếu một database sử dụng chung cho nhiều project thì sẽ xử lý như thế nào

-> Từ đó sinh ra `docker-compose` để kết nối các container riêng lẻ với nhau

Khi đó, chúng ta sẽ xây dựng nhiều container, khi nào cần tương tác với database thì gọi tới container `mysql`, khi nào cần tương tác với `redis` thì gọi tới container `redis`, cần cái gì thì gọi tới container làm nhiệm vụ đó

# Docker Compose

`docker-compose` là một công cụ để thực thi nhiều container cùng lúc cho ứng dụng của bạn. Cùng một lúc, chỉ cần một câu lệnh bạn có thể khởi chạy hàng loạt container

Docker Compose có nhiệm vụ kết nối các container riêng lẻ với nhau

# Cài đặt Docker Compose

**Bước 1: Chạy lệnh dưới để tải xuống phiển bản mới nhất của Docker Compose**

```sh
curl -SL https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```

**Bước 2: Cấp quyền thực thi cho tệp tin nhị phân `/usr/local/bin/docker-compose`**

```sh
sudo chmod +x /usr/local/bin/docker-compose
```

**Bước 3: Kiểm tra cài đặt**

```sh
docker-compose --version
```

Đây là phiên bản đang cài đặt trên máy chủ Linux của mình

```sh
root@docker:~/EntryCMD# docker-compose --version
Docker Compose version v2.20.3
```

# Sử dụng Docker Compose

Với Docker Compose chúng ta sẽ cần đến một tệp YAML(`docker-compose.yml`), nơi đề cập đến tất cả thông tin container

`docker-compose.yml` trông sẽ như sau:

```sh
services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
      - logvolume01:/var/log
    depends_on:
      - redis
  redis:
    image: redis
volumes:
  logvolume01: {}
```

**Giải thích:**

Tệp YAML trên chứa thôn tin của 2 container là `web` và `redis`.

Container `redis` có image là `redis`, nó sẽ giống như khi chúng ta chạy `docker run redis` sẽ chạy một container có tên là `redis` từ image `redis:latest`.

Container `web` chứa nhiều option:

- `build`: Giá trị `.` cho biết Image của container này sẽ được build từ một Dockerfile trong thư mục cùng cấp với tệp YAML

- `ports`: Container này sẽ được ánh xạ cổng 8000 của máy Host tới cổng 5000 của container

- `volumes`: Dòng đầu tiên `.:code`, thực hiện mount thư mục hiện tại (thư mục chứa file `docker-compose.yml`) trên máy host với thư mục `/code` trên container, dòng tiếp theo `logvolume01:/var/log`, ta để ý dòng cuối cùng trong file YAML, dòng đó có nghĩa là tạo một ổ đĩa có tên `logvolume01` và sau khi tạo ổ đĩa đó được ánh xạ tới thư mục `/var/log` trên container

Và sau đó để build, run và stop các container, ta sử dụng các command sau:

```sh
docker-compose build
docker-compose up
docker-compose down
```

**Trong đó:**

- `docker-compose build`: Dùng để build tất cả các container được định nghĩa trong `docker-compose.yml` 

- `docker-compose up`: Thực hiện tạo và khởi chạy các container. Các option thường đi kèm với lệnh `docker-compose up` là `-d` và `--force-recreate`. Với `-d`thì các container sẽ được chạy dưới dạng background. Với `--force-recreate` thì các container sẽ được tạo lại ngay cả khi cấu hình và image của chúng không thay đổi. Để tìm hiểu thêm về các option về lệnh up, ta truy cập đường dẫn sau https://docs.docker.com/engine/reference/commandline/compose_up/

- `docker-compose down`: Dùng để dừng các container và xóa hết những gì được tạo từ lệnh `docker-compose up`. Về cơ bản thì nó sẽ xóa bỏ những container và network được định nghĩa trong compose file

## Viết Docker Compose

Hướng dẫn này được đưa ra để giới thiệu cá khái niệm chính của Docker Compose trong khi xây dựng một ứng dụng web Python đơn giản. Ứng dụng sử dụng Flask (Một framework của Python) và Redis

Các khái niệm trình bày ở đây đều dễ hiểu ngay cả khi bạn không quen với Python

**Điều kiện tiên quyết:**

Bạn cần có Docker Engine và Docker Compose trên máy của mình

**Bước 1: Xác định các phụ thuộc cửa ứng dụng**

1. Tạo một thư mục cho project

```sh
mkdir composetest
cd composetest
```

2. Tạo một tệp có tên là `app.py` trong thư mục project và dán đoạn mã sau vào:

```sh
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello, I have been seen {} times.\n'.format(count)
```

Trong ví dụ này, redis là tên máy chủ của container redis trên ứng dụng mạng. Ta sử dụng cổng mặc định cho Redis là 6379

3. Tạo một thư mục khác có tên là `requirements.txt` trong thư mục project của bạn và dán đoạn sau vào:

```sh
flask
redis
```

**Bước 2: Tạo Dockerfile**

Dockerfile được sử dụng để build Docker image. Image này chứa tất cả các phụ thuộc, môi trường mà ứng dụng Python yêu cầu, bao gồm cả chính Python

```sh
# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

**Giải thích:**

- `FROM python:3.7-alpine`: Sử dụng base Image `python:3.7-alpine`

- `WORKDIR /code`: Đặt thư mục làm việc thành `/code`

- `ENV FLASK_APP=app.py; ENV FLASK_RUN_HOST=0.0.0.0`: Thiết lập 2 biến môi trường là `FLASK_APP=app.py` và `FLASK_RUN_HOST=0.0.0.0`

- `RUN apk add --no-cache gcc musl-dev linux-headers`: `apk add` cài đặt `gcc` và các gói cần thiết trên `alpine`, ta hãy coi `apk add` trên alpine như `apt-get` trên ubuntu để dễ hiểu hơn

- `COPY requirements.txt requirements.txt`: Sao chép file `requirements.txt` từ thư mục hiện tại trên máy host vào thư mục `/code` trên container

- `RUN pip install -r requirements.txt`: Cài đặt các thành phần phụ thuộc của Python được khai báo trong file `requirements.txt` sử dụng `pip`

- `EXPOSE 5000`: Container lắng nghe trên cổng 5000

- `COPY . .`: Copy nội dụng thư mục hiện tại vào thư mục `/code` trên container. Nội dùng của thư mục hiện tại bao gồm 

```sh
root@docker:~/composetest# ls
Dockerfile  app.py  requirements.txt
```

- `CMD ["flask", "run"]`: Chạy lệnh mặc định cho container là `flask run`

**Bước 3: Tạo file `compose.yaml`**

Tạo một tệp có tên là `compose.yaml` trong thư mục dự án của bạn và dán đoạn mã sau vào:

```sh
services:
  web:
    build: .
    ports:
      - "8000:5000"
  redis:
    image: "redis:alpine"
```

File compose này định nghĩa 2 container là `web` và `redis`

- Container `web` sử dụng Image được build từ Dockerfile trong thư mục hiện tại. Sau đó, nó được ánh xạ tới cổng 8000 của máy host. Container này sử dụng port 5000 để ánh xạ tới port 8000 của máy host

- Container `redis` sử dụng Image trên Docker Hub registry được pull về máy host

**Bước 4: Xây dựng và chạy ứng dụng bằng compose**

1. Từ thư mục project hiện tại `~/composetest`, khởi động ứng dụng ứng dụng của bạn bằng cách chạy lệnh `docker compose up`

```sh
root@docker:~/composetest# docker compose up
[+] Running 7/7
 ✔ redis 6 layers [⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                                 2.1s 
   ✔ 7264a8db6415 Pull complete                                                                   0.5s 
   ✔ a28817da73be Pull complete                                                                   0.6s 
   ✔ 536ccaebaffb Pull complete                                                                   1.0s 
   ✔ f54d1871dea6 Pull complete                                                                   1.4s 
   ✔ 4d190b4b6472 Pull complete                                                                   1.4s 
   ✔ 33fcc95c965f Pull complete                                                                   1.4s 
[+] Building 14.9s (12/12) FINISHED                                                                    
 => [web internal] load build definition from Dockerfile                                          0.0s
 => => transferring dockerfile: 291B                                                              0.0s
 => [web internal] load .dockerignore                                                             0.0s
 => => transferring context: 2B                                                                   0.0s
 => [web internal] load metadata for docker.io/library/python:3.7-alpine                          0.7s
 => [web auth] library/python:pull token for registry-1.docker.io                                 0.0s
 => [web 1/6] FROM docker.io/library/python:3.7-alpine@sha256:9d9b05fc8acdc85a9fc0da1da11a8e90f7  2.1s
 => => resolve docker.io/library/python:3.7-alpine@sha256:9d9b05fc8acdc85a9fc0da1da11a8e90f76b88  0.0s
 => => sha256:9125851493e0d48767e4aff3b4a1cada72207ab01af779634df29f30ac552056 2.85MB / 2.85MB    0.3s
 => => sha256:9d9b05fc8acdc85a9fc0da1da11a8e90f76b88bd36fabb8f57c4c7ef027fbcc9 1.65kB / 1.65kB    0.0s
 => => sha256:0c844a18f7b7b7177cdbe35d5ec934a7801bab3470817321902a6f57c7f67c24 1.37kB / 1.37kB    0.0s
 => => sha256:1b091ebaa5db12afd53b9c1fd5cd9fe95751ffb789c2ce5e530e6a66f535d1f8 6.87kB / 6.87kB    0.0s
 => => sha256:66e1d5e70e420aa86a23bd8b4eebf2a6eb60b4aff9ee8a6ca52e27f51f57b1 622.31kB / 622.31kB  0.2s
 => => sha256:66bedaca5a2f87efebbba7f2fc4fa9d6cea1ab46679fc6292458dc4d43722f25 10.94MB / 10.94MB  0.4s
 => => sha256:f26771d857d7bfe2ecd624f357e8391f27f30ec6960d4c1240babf76a8391466 243B / 243B        0.1s
 => => extracting sha256:66e1d5e70e420aa86a23bd8b4eebf2a6eb60b4aff9ee8a6ca52e27f51f57b1be         0.3s
 => => extracting sha256:66bedaca5a2f87efebbba7f2fc4fa9d6cea1ab46679fc6292458dc4d43722f25         0.8s
 => => extracting sha256:f26771d857d7bfe2ecd624f357e8391f27f30ec6960d4c1240babf76a8391466         0.0s
 => => extracting sha256:9125851493e0d48767e4aff3b4a1cada72207ab01af779634df29f30ac552056         0.4s
 => [web internal] load build context                                                             0.0s
 => => transferring context: 1.03kB                                                               0.0s
 => [web 2/6] WORKDIR /code                                                                       0.7s
 => [web 3/6] RUN apk add --no-cache gcc musl-dev linux-headers                                   4.0s
 => [web 4/6] COPY requirements.txt requirements.txt                                              0.1s 
 => [web 5/6] RUN pip install -r requirements.txt                                                 5.9s 
 => [web 6/6] COPY . .                                                                            0.1s 
 => [web] exporting to image                                                                      1.3s 
 => => exporting layers                                                                           1.3s 
 => => writing image sha256:8b32bb4cb967509eb4b966af352ba93425735ff8c7b088ff5fe4214169a66f9f      0.0s 
 => => naming to docker.io/library/composetest-web                                                0.0s 
[+] Running 3/1                                                                                        
 ✔ Network composetest_default    Created                                                         0.1s 
 ✔ Container composetest-web-1    Created                                                         0.1s 
 ✔ Container composetest-redis-1  Created                                                         0.1s 
Attaching to composetest-redis-1, composetest-web-1
composetest-redis-1  | 1:C 05 Sep 2023 02:29:51.227 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
composetest-redis-1  | 1:C 05 Sep 2023 02:29:51.227 * Redis version=7.2.0, bits=64, commit=00000000, modified=0, pid=1, just started
composetest-redis-1  | 1:C 05 Sep 2023 02:29:51.227 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
composetest-redis-1  | 1:M 05 Sep 2023 02:29:51.231 * monotonic clock: POSIX clock_gettime
composetest-redis-1  | 1:M 05 Sep 2023 02:29:51.232 * Running mode=standalone, port=6379.
composetest-redis-1  | 1:M 05 Sep 2023 02:29:51.233 * Server initialized
composetest-redis-1  | 1:M 05 Sep 2023 02:29:51.234 * Ready to accept connections tcp
composetest-web-1    |  * Serving Flask app 'app.py'
composetest-web-1    |  * Debug mode: off
composetest-web-1    | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
composetest-web-1    |  * Running on all addresses (0.0.0.0)
composetest-web-1    |  * Running on http://127.0.0.1:5000
composetest-web-1    |  * Running on http://172.18.0.3:5000
composetest-web-1    | Press CTRL+C to quit
```

2. Nhập `http://<IP_host>:8000` lên trình duyệt để kiểm tra ứng dụng có đang chạy

Bạn sẽ thấy một thông báo trong trình duyệt

![](/docker/images/compose.png)

3. Chuyển sang cửa sổ terminal khác và nhập `docker images` để liệt kê các Image local

```sh
root@docker:~/composetest# docker images
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
composetest-web         latest    8b32bb4cb967   26 minutes ago   213MB
tubt16a6/barista_cafe   1.0       c8e1203b9231   13 hours ago     258MB
redis                   alpine    3a8d46c63628   2 weeks ago      37.8MB
```

4. Stop ứng dụng bằng cách chạy `docker compose down` trong terminal thứ 2 hoặc bằng cách nhấn `CTRL + C` trong terminal thứ nhất nơi bạn khởi động ứng dụng 

**Bước 5: Chỉnh sửa Compose file để thêm bind mount**

Chỉnh sửa tệp `compose.yaml` trong thư mục của dự án để thêm bind mount cho dịch vụ web

```sh
services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_DEBUG: "true"
  redis:
    image: "redis:alpine"
```

Volume mới sẽ gắn thư mục hiện tại trên máy host `/root/composetest` trên máy chủ vào thư mục `/code` bên trong container, cho phép bạn sửa đổi code một cách nhanh chóng mà không cần phải xây dựng lại image hay exec vào container để sửa đổi. Biến môi trường `FLASK_DEBUG`, biến này yêu cầu chạy ở môi trường dev và tải lại code khi có thay đổi. Chế độ này chỉ nên được sử dụng trong quá trình phát triển

**Bước 6: Xây dựng lại và chạy ứng dụng bằng compose**

Từ thư mục chứa project, chạy lệnh `docker compose up -d` để build lại ứng dụng với tệp đã cập nhật trước đó và chạy nó dưới dạng background

```sh
root@docker:~/composetest# docker compose up -d
[+] Running 3/3
 ✔ Network composetest_default    Created                                                                                                                                  0.1s 
 ✔ Container composetest-redis-1  Started                                                                                                                                  0.7s 
 ✔ Container composetest-web-1    Started
```

**Bước 7: Update ứng dụng**

Vì thư mục hiện tại đã được mount vào thư mục `/code` của container nên bạn có thể thực hiện các thay đổi đối với code và xem các thay đổi đó ngay lập tức mà không cần phải rebuild lại image

Chỉnh sửa lại file `app.py`

```sh
return 'Hello from Docker! I have been seen {} times.\n'.format(count)
```

Refresh lại trình duyệt, để xem thay đổi

![](/docker/images/composeChange.png)

**Bước 8: Thử nghiệm với một số lệnh khác**

Để xem những container nào đang được chạy bởi `docker-compose` ta sử dụng lệnh `docker-compose ps`

```sh
root@docker:~/composetest# docker-compose ps
NAME                  IMAGE               COMMAND                  SERVICE             CREATED             STATUS              PORTS
composetest-redis-1   redis:alpine        "docker-entrypoint.s…"   redis               17 minutes ago      Up 17 minutes       6379/tcp
composetest-web-1     composetest-web     "flask run"              web                 17 minutes ago      Up 17 minutes       0.0.0.0:8000->5000/tcp, :::8000->5000/tcp
```

Để xem cpu 

Lệnh `docker compose run` cho phép bạn chạy các lệnh một lần cho các dịch vụ của mình. Ví dụ: để xem những biến môi trường nào có sẵn cho container `web`:

```sh
root@docker:~/composetest# docker compose run web env
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=046d30ebdd35
TERM=xterm
FLASK_DEBUG=true
LANG=C.UTF-8
GPG_KEY=0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
PYTHON_VERSION=3.7.17
PYTHON_PIP_VERSION=23.0.1
PYTHON_SETUPTOOLS_VERSION=57.5.0
PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/9af82b715db434abb94a0a6f3569f43e72157346/public/get-pip.py
PYTHON_GET_PIP_SHA256=45a2bb8bf2bb5eff16fdd00faef6f29731831c7c59bd9fc2bf1f3bed511ff1fe
FLASK_APP=app.py
FLASK_RUN_HOST=0.0.0.0
HOME=/root
```

Sử dụng lệnh `docker compose --help` để xem thêm về các command khác

Nếu bạn sử dụng `docker compose up -d`, thì ta stop service bằng lệnh

```sh
docker compose stop
```

Để loại bỏ tất cả các containerr được build bởi `docker-compose`. Truyền `--volumes` để xóa data volume được sử dụng bởi `Redis` container

```sh
docker compose down --volumes
```

**Tham khảo:**

https://docs.docker.com/compose/gettingstarted/#step-6-re-build-and-run-the-app-with-compose