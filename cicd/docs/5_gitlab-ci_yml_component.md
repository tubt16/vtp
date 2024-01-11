# Các thành phần trong file `.gitlab-ci.yml`

Để có thể sử dụng CI/CD trên Gitlab thì bạn cần tạo 1 file `.gitlab-ci.yml`. File này sẽ chứa các thông tin cần thiết để Gitlab runner và executor sử dụng và thực thi các công việc được yêu cầu. Các thành phần cơ bản sẽ bảo gồm như sau:

- Danh sách cac bước (stage) sẽ thực hiện

- Các công việc (job) cần được thực hiện của stage đi kèm với danh sách câu lệnh

- Các biến môi trường cần sử dụng cho toàn bộ các công việc hoặc từng job (nếu có)

- Các tập tin cần thiết từ các repository khác cần được thêm (nếu có)

- Docker image cần sử dụng cho các job (nếu có)

- Danh sách các câu lệnh cần được thực thi trước và sau khi thực thi job (nếu có)

- Tag dùng để chỉ định runner nào được chọn để thực thi job (nếu có)

Ví dụ:

```sh
stages:										##### Danh sách các bước (stage) pipeline sẽ có
  - build
  - test
  - deploy

variables:									##### Biến môi trường sử dụng cho TOÀN BỘ (global) các job
  VAR_GLOBAL_1: value_1
  VAR_GLOBAL_2: value_2

build-job:									##### Job build
  stage: build-job							##### Thuộc stage "build"
  script:									##### Danh sách các câu lệnh mà job này sẽ thực hiện 
    - command build 1
    - command build n
  variables:								##### Biến môi trường chỉ sử dụng cho Job build 
    VAR_1: value_1
    VAR_2: value_2

unit-test-jobs:								##### Job unit-test
  stage: test 								##### Thuộc stage "test"
  script:									##### Danh sách các câu lệnh mà job này sẽ thực hiện
    - command test 1
    - command test n

lint-test-jobs:								##### Job lint-test
  stage: test 								##### Thuộc stage "test"
  script:									##### Danh sách các câu lệnh mà job này sẽ thực hiện
    - command lint test 1
    - command lint test n

deploy-job:									##### Job deploy
  stage: deploy 							##### 
  script:
    - command deploy 1
    - command deploy n
```

Pipeline từ file `.gitlab-ci.yml` trên

![](/cicd/images/pipelines1.png)

# Stages - Các bước thực hiện

Từ khóa này được sử dụng để khai báo thứ tự các bước (stage) mà pipeline của người dùng sẽ có. Nếu như không được khai báo trong file `.gitlab-ci.yml`, pipeline của người dùng sẽ bao gồm các stage mặc định của Gitlab

- `.pre`
- `Build`
- `Test`
- `Deploy`
- `.post`

Người dùng có thể tự khai báo các stage với cách đặt tên và thứ tự các stage theo như cầu của mình, không yêu cầu phải giống như cấu hình mặc định của Gitlab. Ví dụ:

```sh
stages:
 - linter
 - unit-test
 - build-image
 - deploy-service
```

Các stage sẽ được thực thi 1 cách tuần tự, từ trên xuống dưới. Khi stage đầu tiên thực thi "thành công" các job của mình thì sẽ thực thi tiếp đến các stage tiếp theo. Quá trình này sẽ do người dùng quy định dựa vào cách liệt kê và sắp xếp các stage

![](/cicd/images/stage.png)

Một stage sẽ có thể bao gồm nhiều job khác nhau, nhưng 1 job thì chỉ thuộc 1 stage. Những job nào không khai báo "stage" thì sẽ mặc định được cấu hình thuộc stage "test". Các job thuộc cùng 1 stage sẽ được xử lý đồng thời (parallel) tùy theo số lượng runner hiện có của repo

# Job - Các công việc cần thực hiện của từng stage 

Các job sẽ được người dùng khai báo bằng cách đặt tên không trùng với từ khóa mặc định của Gitlab-CI (default, stage, variables ...) Nội dung của 1 job cơ bản bao gồm:

- stage: Tên của stage mà job thuộc về. Nếu không khai báo thì mặc định job sẽ thuộc về stage "test"

- script: Danh sách các câu lệnh mà job sẽ thực hiện

- image: Docker image được sử dụng cho job (Chỉ áp dụng đối với executor là Docker)

- variables: Danh sách các biến môi trường của job (tùy chọn - không bắt buộc)

- tags: Danh sách các tag dùng để chỉ định runner nào sẽ thực thi job

```sh
unit-test-job:        # Job có tên là unit-test-job
  stage: test         # Thuộc stage "test"
  image: python:3.6   # Docker image sử dụng để thực thi job (chỉ áp dụng đối với executor là Docker)
  tags:               # Những runner được đánh tag thuộc danh sách đã liệt kê sẽ thực thi job
    - testing
    - python
  script:             # Danh sách câu lệnh mà job này sẽ thực hiện
    - command test 1
    - command test n
```

# Script - Các câu lệnh job sẽ thực thi

Từ khóa này được khai báo bên trong từng job và sử dụng để liệt kê danh sách các câu lệnh cần được thực thi của các job. Mỗi job sẽ được khai báo các "script" để executor có thể thực hiện 

```sh
build-job:					##### Job build
  stage: build 				##### Thuộc stage "build"
  script:					##### Danh sách các câu lệnh mà Job sẽ thực hiện
  	- command build 1 
  	- command build 2
  variables					##### Biến môi trường chỉ sử dụng cho "build-job"
  	VAR_1: value_1
  	VAR_2: value_2
```

# Stage - Khai báo job thuộc stage được chỉ định (tùy chọn)

Từ khóa này được sử dụng bên trong các job để khai báo job sẽ thuộc một stage trong danh sách đã khai báo trước đó. Nếu như danh sách stage khác với cấu hình mặc định của Gitlab, bạn cần thêm trường này để xác định rõ job sẽ thuộc stage nào trong pipeline. Nếu không được định nghĩa, job sẽ thuộc stage "test"

```sh
build-job:			### Job có tên build-job
  stage: build 		### Job này thuộc stage "build"
...
...
```

# Image - Chỉ áp dụng khi executor là docker (tùy chọn)

Từ khóa này được sử dụng để khai báo Docker image mặc định sử dụng cho toàn bộ các job hoặc chỉ sử dụng cho 1 job cụ thể nếu "executor" của runner là Docker

```sh
build-job:
  stage: build 
  image: python:3.8		### Image được sử dụng để executor xử lý job
...
...
```

# Tags - Dùng để chọn runner xử lý job (tùy chọn)

Khi sử dụng từ khóa này, người dùng có thể chỉ định được runner nào sẽ nhận và xử lý các job bằng cách liệt kê các tag tương ứng. Mặc định chỉ những runner được đánh tag cùng tên với danh sách đã liệt kê sẽ có quyền xử lý job, những runner còn lại nếu chưa đánh tag sẽ hầu như không được nhận job. Cách đặt tên tag do người dùng quyết định 

```sh
unit-test-job:
  stage: test
  tags:
    - tag_1
    - tag_2
    - tag_3
  script
...
...
```

# Variables - Biến môi trường (tùy chọn)

Từ khóa này được sử dụng để khai báo các biến môi trường được sử dụng toàn bộ các job hoặc cho từng job cụ thể nếu chưa được khai báo bên trong các job. Ví dụ:

```sh
stages:
  - build
  - test 
  - deploy 

variables:						### Biến môi trường sử dụng cho toàn bộ các job
  VAR_GLOBAL_1: value_1
  VAR_GLOBAL_2: value_2

build-job:
  stage: build 
  script:
    - command build 1
    - command build 2
  variables:					### Biến môi trường chỉ sử dụng cho job "build"
    VAR_1: value1
    VAR_2: value2
```

# Before_script - Các câu lệnh được thực thi trước khi thực thi các job (tùy chọn)

Từ khóa này được sử dụng để liệt kê danh sách các câu lệnh cần được thực thi trước khi vào câu lệnh chính của job được thực hiện. Bạn có thể sử dụng từ khóa này để áp dụng cho toàn bộ các job nếu khai báo bên từ khóa này không phụ thuộc bất kỳ job nào cả

```sh
build-job:
  stage: build 
  image: python:3.8
  before_script:
    - echo "command before1"
    - echo "command before2"
    - echo "command before3"
...
...
```

# After script - Các câu lệnh sẽ được thực thi sau khi script bên trên đã thực thi xong (tùy chọn)

Từ khóa này được sử dụng để liệt kê danh sách câu lệnh cần được thực thi sau khi script bên trên đã thực thi xong. Bạn có thể sử dụng từ khóa này để tiến hành các câu lệnh mang tính chất dọn dẹp sau khi đã thực thi xong công việc để giải phóng tài nguyên của hệ thống được sinh ra trong quá trình thực thi "script"

```sh
build-job:
  stage: build 
  image: python:3.8
  script:
    - command 1
    - command 2
    - command 3
  after_script:
    - echo "command after1"
    - echo "command after2"
    - echo "command after3"
```