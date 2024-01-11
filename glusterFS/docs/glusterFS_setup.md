# GlusterFS 9 Install

Hướng dẫn này sẽ cài đặt GlusterFS với 2 node GlusterFS server (`gluster1`, `gluster2`) và 2 node GlusterFS client (`nexus1`, `nexus2`)

Mô hình

|Node|Role|IP|OS|
|---|---|---|---|
|gluster1|glusterfs-server|34.31.177.7|CentOS 7|
|gluster2|glusterfs-server|34.42.126.121|CentOS 7|
|nexus1|glusterfs-client|34.133.42.58|CentOS 7|
|nexus2|glusterfs-client|34.67.118.182|CentOS 7|

## Install glusterfs-server

Bước 1: Add host trên tất cả các node

Thêm các dòng sau vào file `/etc/hosts` trên tất cả các node

```sh
34.31.177.7 gluster1
34.42.126.121 gluster2
34.133.42.58 nexus1
34.67.118.182 nexus2
```

Buớc 2: Cài đặt glusterfs-server trên 2 node `gluster1` và `gluster2`

- Add repo `centos-release-gluster9`

```sh
yum -y install centos-release-gluster9
```

- Chỉnh sửa repo vừa mới thêm

```sh
sed -i -e "s/enabled=1/enabled=0/g" /etc/yum.repos.d/CentOS-Gluster-9.repo
```

- Cài đặt glusterfs-server từ kho lưu trữ `centos-release-gluster9` vừa mới thêm

```sh
yum --enablerepo=centos-gluster9 -y install glusterfs-server
```

- Start và enable service glusterd

```sh
systemctl start glusterd

systemctl status glusterd

systemctl enable glusterd
```

## Install glusterfs-client

Thực hiện cài đặt glusterfs-client (`glusterfs` và `glusterfs-fuse`) trên 2 node `nexus1` và `nexus2`

- Add repo `install centos-release-gluster9`

```sh
yum -y install centos-release-gluster9
```

- Chỉnh sửa repo vừa mới thêm

```sh
sed -i -e "s/enabled=1/enabled=0/g" /etc/yum.repos.d/CentOS-Gluster-9.repo
```

## Cài đặt và cấu hình trên các glusterfs-server (`gluster1`, `gluster2`)

Đầu tiên, tạo một thư mục trên 2 GlusterFS server nằm trên phân vùng khác với phân vùng `/`

`mkdir /data`

Ở đây, ta add thêm 1 ổ cứng mới ở cả 2 server và phân vùng, format thành định dạng xfs và mount vào thư mục `/data/`

Đầu tiên tạo partition:

`fdisk /dev/sdb`

Format the partition:

```sh
mkfs.xfs -i size=512 /dev/sdb1
```

Khai báo vào file cấu hình `/etc/fstab` để khi restart server, hệ thống sẽ tự động mount vào thư mục

```sh
echo '/dev/sdb1 /data xfs defaults 1 2' >> /etc/fstab
mount -a && mount
```

## Add node glusterfs-server vào Pool

Trong bài viết này chỉ có 2 node đóng vai trò là glusterfs-server vì thế ta chỉ cần đứng trên 1 node và add node còn lại vào Pool

Đứng tại node1 và add node 2 vào Pool

```sh
gluster peer probe gluster2
```

Đứng tại 2 node và kiểm tra status của pool

```sh
[root@gluster1 gluster]# gluster peer status
Number of Peers: 1

Hostname: gluster2
Uuid: 86c995be-cdc8-43cd-9da0-a5748a174285
State: Peer in Cluster (Connected)


[root@gluster1 distributed]# gluster peer status
Number of Peers: 1

Hostname: gluster2
Uuid: 86c995be-cdc8-43cd-9da0-a5748a174285
State: Peer in Cluster (Connected)
```

## Tạo Volume Distributed

Distributed Volume là 1 loại volume có dữ liệu được phân tán trên từng brick, nếu chúng ta có 2 file thì `file1` sẽ nằm trong `brick1`, `file2` sẽ nằm trong `brick2`

- Ưu điểm: Mở rộng được dung lượng store (Dung lượng store bằng tổng số lượng các brick)

- Nhược điểm: Nếu 1 trong các brick bị lỗi, dữ liệu trên brick đó sẽ mất

Tạo Volume `vol_distributed` từ bất kỳ node nào trong 2 node `gluster1` và `gluster2`

```sh
[root@gluster1 gluster]# gluster volume create vol_distributed \
> gluster1:/data/gluster/distributed \
> gluster2:/data/gluster/distributed
volume create: vol_distributed: success: please start the volume to access data
```

Start volume

```sh
[root@gluster1 gluster]# gluster volume start vol_distributed
volume start: vol_distributed: success
```

Confirm volume info

```sh
[root@gluster1 gluster]# gluster volume info vol_distributed
 
Volume Name: vol_distributed
Type: Distribute
Volume ID: e573d797-d557-4143-9531-30a55ebbd966
Status: Started
Snapshot Count: 0
Number of Bricks: 2
Transport-type: tcp
Bricks:
Brick1: gluster1:/data/gluster/distributed
Brick2: gluster2:/data/gluster/distributed
Options Reconfigured:
storage.fips-mode-rchecksum: on
transport.address-family: inet
nfs.disable: on
```

## Tạo volume Replicated

Replicated Volume là 1 loại volume mà trong đó dữ liệu sẽ được nhân bản đến những brick còn lại. Khi dữ liệu trên 1 brick bị mất (tức là dữ liệu trên 1 server) thì dữ liệu đó vẫn còn trên brick còn lại và tự động đồng bộ lại cho cả 2 server. Đảm bảo dữ liệu luôn đồng bộ và sẵn sàng

- Ưu điểm: Phù hợp với hệ thống yêu cầu tính sẵn sàng cao

- Nhược điểm: Tốn tài nguyên hệ thống

Tạo Volume `vol_replicated` từ bất kỳ node nào trong 2 node `gluster1` và `gluster2`

```sh
[root@gluster1 gluster]# gluster volume create vol_replicated rep 2 \
> gluster1:/data/gluster/replicated \
> gluster2:/data/gluster/replicated
Replica 2 volumes are prone to split-brain. Use Arbiter or Replica 3 to avoid this. See: http://docs.gluster.org/en/latest/Administrator%20Guide/Split%20brain%20and%20ways%20to%20deal%20with%20it/.
Do you still want to continue?
 (y/n) y
volume create: vol_replicated: success: please start the volume to access data
```

NOTE: Thông số `rep` là số lượng brick, tức là dữ liệu sẽ được lưu đồng thời trên cả 2 brick trên `gluster1` và `gluster2`

Start volume

```sh
[root@gluster1 gluster]# gluster volume start vol_replicated
volume start: vol_replicated: success
```

Confirm volume info

```sh
[root@gluster1 gluster]# gluster volume info vol_replicated
 
Volume Name: vol_replicated
Type: Replicate
Volume ID: 63e12b8e-69dc-4362-8f18-37b51c7d9120
Status: Started
Snapshot Count: 0
Number of Bricks: 1 x 2 = 2
Transport-type: tcp
Bricks:
Brick1: gluster1:/data/gluster/replicated
Brick2: gluster2:/data/gluster/replicated
Options Reconfigured:
cluster.granular-entry-heal: on
storage.fips-mode-rchecksum: on
transport.address-family: inet
nfs.disable: on
performance.client-io-threads: off
```

## Tạo volume Stripe

## Một số command khi sử dụng GlusterFS

- Add 1 node vào Pool

```sh
gluster peer probe <hostname or IP-server>
```

Trong đó: `<hostname or IP-server>` lần lượt là hostname của server hoặc địa chỉ IP của server

- Xem status của pool

```sh
gluster peer status
```

- Xóa node ra khỏi pool

```sh
gluster peer detach <hostname or IP-server>
```

- Tạo volume

```sh
gluster volume create <NEW-VOLNAME> [stripe <COUNT>] [[replica <COUNT> [arbiter <COUNT>]]|[replica 2 thin-arbiter 1]] [disperse [<COUNT>]] [disperse-data <COUNT>] [redundancy <COUNT>] [transport <tcp|rdma|tcp,rdma>] <NEW-BRICK> <TA-BRICK>... [force]
```

- Start volume

```sh
gluster volume start <volume_name>
```

Trong đó: `<volume_name>` là tên volume cần start

- Xem thông tin tất cả volume đã tạo

```sh
gluster volume info
```

- Stop volume

```sh
gluster volume stop <volume_name>
```

- Delete volume

```sh
gluster volume delete <volume_name>
```

- Add thêm brick vào volume

```sh
gluster volume add-brick <volume_name> <server:/data>
```

Trong đó `<server:/data>` là đường dẫn của brick cần add

- Tương tự Reomve brick ra khỏi volume

```sh
gluster volume remove-brick <volume_name> <server:/data>
```

- Migrate volume (QUAN TRỌNG): Chuyển dữ liệu từ 1 brick TRONG Pool đến brick khác nằm NGOÀI Pool

```sh
gluster volume replace-brick <volume_name> <server1:/data> <server2:/data> start 		### Bắt đầu quá trình chuyển dữ liệu tù brick data1 đến data2
gluster volume replace-brick <volume_name> <server1:/data> <server2:/data> status		### Xem quá trình chuyển dữ liệu
gluster volume replace-brick <volume_name> <server1:/data> <server2:/data> commit
```

- Rebalance Volume: Đồng bộ dữ liệu khi THÊM, XÓA brick

```sh
gluster volume rebalance <volume_name> fix-layout start
gluster volume rebalance <volume_name> migrate-data start
gluster volume rebalance <volume_name> start
```

Trong đó:

- `fix-layout`:  Sửa bố cục để sử dụng cấu trúc liên kết ổ đĩa mới để có thể phân phối tệp đến các node mới được thêm vào

- `migrate-date`: Cân bằng lại volume bằng cách sửa bố cục để sử dụng cấu trúc liên kết ổ đĩa mới và di chuyển dữ liệu hiện có
