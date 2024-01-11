# Cài đặt docker trên Ubuntu

Install guild: https://docs.docker.com/engine/install/ubuntu/

### OS requirement

- Ubuntu Lunar 23.04
- Ubuntu Kinetic 22.10
- Ubuntu Jammy 22.04 (LTS)
- Ubuntu Focal 20.04 (LTS)

### Gỡ cài đặt các gói cũ

Trước khi cài đặt docker engine, bạn cần chắc chắn rằng các gói gây xung đột đều được gỡ cài đặt

Các distro cung cấp bản phân phối không chính thức của các gói Docker trong APT. Bạn phải gỡ các đặt các gói này trước khi có thể cài đặt phiên bản chính thức của Docker Engine

Các gói không chính thức để gỡ cài đặt là:

- `docker.io`
- `docker-compose`
- `docker-doc`
- `podman-docker`

Chạy lệnh sau để gỡ tất cả các gói xung đột:

```sh
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

# Cài đặt bằng apt repo

### Thiết lập kho lưu trữ

1. Cập nhật `apt` chỉ mục gói và cài đặt các gói để cho phép `apt` sử dụng kho lưu trữ qua https

```sh
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
```

2. Thêm khóa GPG chính thức của Docker:

```sh
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

3. Thiết lập kho lưu trữ

```sh
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

4. Cập nhật `apt` chỉ mục gói

```sh
sudo apt-get update
```

### Cài đặt Docker Engine

Cài đặt Docker engine, containerd và Docker compose

```sh
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

Phân quyền cho người dùng hiện tại có quyền thao tác với docker

```sh
sudo usermod -aG docker $(whoami)
```

Xác minh quá trình cài đặt docker engine thành công bằng cách chạy lệnh

```sh
docker -v
```

