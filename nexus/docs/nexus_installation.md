# Cài đặt Nexus 3.61.0

# Yêu cầu

OS: CentOS 7

Disk: 100GB

Ram: 4GB

Java: Java 8 trở lên

# Cài đặt Nexus

Bước 1: Để chạy được Nexus trước tiên cần phải cài đặt Java (yêu cầu java 8 trở lên)

```sh
yum install java-1.8.0-openjdk.x86_64 wget -y
```

Kiểm tra

```sh
[root@nexus1 bin]# java -version
openjdk version "1.8.0_382"
OpenJDK Runtime Environment (build 1.8.0_382-b05)
OpenJDK 64-Bit Server VM (build 25.382-b05, mixed mode)
```

Bước 2: Tạo thư mục cần thiết trong quá trình cài đặt Nexus (Thư mục chứa source và thư mục download source từ trang chủ)

```sh
mkdir -p /opt/nexus/   
mkdir -p /tmp/nexus/ 
```

Bước 3: Đi tới thư mục `/tmp/nexus` và tải về source của Nexus bản mới nhất và giải nén

```sh
cd /tmp/nexus/
wget https://download.sonatype.com/nexus/3/nexus-3.61.0-02-unix.tar.gz -O nexus.tar.gz
tar xzvf nexus.tar.gz
```

Bước 4: Xóa file nén và copy source đến thư mục `/opt/nexus` (Nơi lưu trữ source của Nexus)

```sh
rm -rf /tmp/nexus/nexus.tar.gz
cp -r /tmp/nexus/* /opt/nexus/
```

Bước 5: Tạo user `nexus` và phân quyền cho user này sở hữu thư mục `/opt/nexus`

```sh
useradd nexus
chown -R nexus.nexus /opt/nexus 
```

Bước 6: Cấu hình Nexus chạy như một service trên Linux (Tạo file config trong systemd)

```sh
cat <<EOF>> /etc/systemd/system/nexus.service
[Unit]                                                                          
Description=nexus service                                                       
After=network.target                                                            
                                                                  
[Service]                                                                       
Type=forking                                                                    
LimitNOFILE=65536                                                               
ExecStart=/opt/nexus/nexus-3.61.0-02/bin/nexus start                                  
ExecStop=/opt/nexus/nexus-3.61.0-02/bin/nexus stop                                    
User=nexus                                                                      
Restart=on-abort                                                                
                                                                  
[Install]                                                                       
WantedBy=multi-user.target                                                      
EOF
```

Bước 7: Cấu hình để Start service Nexus với user `nexus`

```sh
echo 'run_as_user="nexus"' > /opt/nexus/nexus-3.61.0-02/bin/nexus.rc
```

Bước 8: Reload cấu hình systemd và khởi động service Nexus

```sh
systemctl daemon-reload
systemctl start nexus
systemctl enable nexus
```

Sau khi cài đặt Nexus ta chờ khoảng 2p sau đó truy cập đường dẫn sau `http://[IP-Server]:8081`

Ta đăng nhập với mật khẩu lấy trong file `/opt/nexus/sonatype-work/nexus3/admin.password`

![](/nexus/images/nexus.png)

Ngoài ra ta có thể chạy script sau để cài nexus 

[Setup-nexus](/nexus/scripts/nexus-setup.sh)