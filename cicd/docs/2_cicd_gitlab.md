# Introduction

![](/cicd/images/cicdGitlab.png)

Mục tiêu của CI/CD là tự động hóa hoàn toàn các khâu trong quy trình phát triển phần mềm hiện nay

Hiện nay có rất nhiều hệ thống như Travis, Jenkins, Circle, Gitlab có thể giúp bạn làm được điều đó. Trong bài viết này sẽ giới thiệu tổng quan `Gitlab CI` và cách xây dựng một hệ thống cơ bản

# Git Flow

![](/cicd/images/gitFlow.png)

Dev hoàn thành một task nào đó và push commit lên Gitlab để mọi người review

Khi đó `Gitlab CI` cũng bắt đầu thực hiện công việc mà nó được tạo giao. Nó sử dụng file `.gitlab-ci.yml` nằm trong thư mục gốc của repo để cấu hình project sử dụng các Runner. Một `pipeline`. CI sinh ra và report sẽ được hiển thị trên giao diện

Vậy `Pipelines` là gì ?

# Pipelines

Là thành phần cấp cao nhất của tích hợp, phân phối và triển khai liên tục

```sh
Pipelines are the top-level component of continuous integration, delivery, and deployment.
```

**Pipelines** bao gồm:

- Jobs: Các công việc được giao thực thi (Ví dụ: biên dịch mã hoặc chạy test)

- Stage: Xác định các thời điểm và cách thực hiện (Ví dụ: test chỉ chạy sau khi biên dịch thành công)

**Pipelines** hoạt động theo nguyên tắc sau:

- Tất cả các công việc trong cùng một `stage` được `Runner` sử dụng song song nếu có đủ số lượng `Runner` đồng thời

- Nếu Success, pipeline sẽ chuyển sang `stage` tiếp theo

- Nếu Failed, pipeline sẽ dừng lại. Có một ngoại lệ là nếu job được đánh dấu làm thủ công, thì dù bị fail pipeline vẫn sẽ tiếp tục

Bên dưới là ví dụ về một Pipeline thông thường

![](/cicd/images/pipelines.png)

Tóm lại, các bước để `Gitlab CI` hoạt động như sau: 

- Thêm `.gitlab-ci.yml` vào thư mục gốc của repo

- Cấu hình gitlab `Runner`

# Config gitlab-ci.yml

### Create `.gitlab-ci.yml`

`.gitlab-ci.yml` được viết theo dạng YAML

Như đã đề cập ở trên, `.gitlab-ci.yml` cho `Runner` biết những công việc cần phải làm. Mặc định, nó sẽ chạy một pipeline với 3 stage:

- `build`

- `test`

- `deploy`

Tuy nhiên bạn không nhất thiết phải dùng cả 3 stage, các stage không được giao việc sẽ được bỏ qua

Dưới đây là một ví dụ đơn giản cho project java

```sh
variables:
  MAVEN_OPTS: -Dmaven.repo.local=.m2/repository

image: maven:latest

stages:
    - build
    - test
    - package
    - deploy
    
cache:
  paths:
    - .m2/repository
    - target

build_job:
  stage: build
  tags:
    - docker 

  script: 
    - echo "Maven compile started"
    - "mvn compile"


test_job:
  stage: test
  tags:
    - docker 

  script: 
    - echo "Maven test started"
    - "mvn test"

package_job:
  stage: package
  tags:
    - docker 

  script: 
    - echo "Maven packaging started"
    - "mvn package"


Deploy_job:
  stage: deploy
  tags:
    - docker 

  script: 
    - echo "Maven deploy started"
```

# Gitlab Runner

Trong gitlab, các `Runner` thực thi các jobs được định nghĩa trong file `.gitlab-ci.yml`

Một `Runner` có thể là một máy ảo (VM), một VPS, một docker-container hay thậm chí là một cluster-container. Gitlab và Runners giao tiếp với nhau thông qua API, vì vậy yêu cầu duy nhất là máy chạy Runner có quyền truy cập Gitlab server

Một `Runner` có thể xác định cụ thể cho một dự án nhất định hoặc phục vụ cho nhiều dự án trong Gitlab. Nếu nó phục vụ cho tất cả project thì được gọi là `Shared Runner`

Để xác định xem Runner nào chỉ định cho project của bạn, Vào settings -> CI/CD -> Runner -> Expand

![](/cicd/images/runner.png)

# Cài đặt Gitlab Runner trên OS Linux

Download và cài đặt file nhị phân

```sh
# Download the binary for your system
sudo curl -L --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64

# Give it permission to execute
sudo chmod +x /usr/local/bin/gitlab-runner

# Create a GitLab Runner user
sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash

# Install and run as a service
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
sudo gitlab-runner start
```

Register Runner

```sh
gitlab-runner register

Enter the GitLab instance URL (for example, https://gitlab.com/):
# Nhập URL gitlab của bạn

Enter the registration token:
# Nhập token của Project

Enter a description for the runner:
# Nhập mô tả về cho runner

Enter tags for the runner (comma-separated):
# Đặt tag cho runner

Enter an executor: custom, parallels, ssh, docker-autoscaler, kubernetes, docker, docker-windows, shell, virtualbox, docker+machine, instance:
# Chọn executor cho Runner (chọn 1 trong các giá trị trên)

Enter the default Docker image (for example, ruby:2.7):
# Nếu executor là docker ta cần thêm image mặc định cho nó 
```

Đến đây là đã thiết lập thành công Gitlab runner