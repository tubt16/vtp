# GlusterFS

## Giới thiệu về GlusterFS

GlusterFS là một open source, là một hệ thống tệp phân tán, có khả năng mở rộng, tổng hợp tài nguyên lưu trữ đĩa từ nhiều máy chủ vào một không gian chung duy nhất

**Lợi ích**

- Quy mô đến vài petabyte

- Xử lý hàng ngàn client

- Linh hoạt kết hợp với các thiết bị lưu trữ vật lý, ảo và tài nguyên điện toán đám mây để cung cấp một hệ thống lưu trữ có tính sẵn sàng cao 

- Chương trình có thể lưu trữ dữ liệu trên các mô hình, thiết bị khác nhau, nó kết nối với tất cả các node cài đặt GlusterFS qua giao thức TCP hoặc RDMA tạo ra nguồn tài nguyên lưu trữ duy nhất (distributed mode) hoặc sử dụng tối đa không gian ổ cứng có sẵn trên tất cả các ghi chú để nhân bản dữ liệu (replicated mode)

## Một số khái niệm khi sử dụng GlusterFS

Để có thể hiểu rõ về GlusterFS và ứng dụng được nó, trước hết ta cần phải biết rõ nhưng khái niệm có trong GlusterFS

Sau đây là những khái niệm quan trọng khi sử dụng GlusterFS

**Trusted Storage Pool:**

Trong một hệ thống GlusterFS, những server dùng để lưu trữ được gọi là những node và những node này kết hợp với nhau thành một không gian lưu trữ lớn được gọi là Pool. Dưới đây là mô hình kết nối giữa 2 node thành một Trusted Storage Pool

![](/glusterFS/images/trustedStoragePool.png)

**Brick**

- Từ những phân vùng lưu trữ mới (những phân vùng chưa dùng đến) trên mỗi node chúng ta có thể tạo ra những brick

- Brick được định nghĩa bởi 1 server (name or IP) và 1 đường dẫn. VD: 10.10.10.20:/mnt/brick (đã mount 1 partition `/dev/sdb1` vào `/mnt`)

- Mỗi Brick có dưng lượng bị giới hạn bởi filesystem

- Trong mô hình lý tưởng, mỗi brick thuộc cluster có dung lượng bằng nhau. Để có thể hiểu rõ hơn về Bricks, chúng ta có thể tham khảo hình dưới đây:

![](/glusterFS/images/brick.png)

**Volume**

- Từ những brick trên các node thuộc cùng một Pool, kết hợp những brick đó lại thành một không gian lưu trữ lớn và thống nhất để client có thể mount đến và sử dụng

- Một volume là tập hợp logic của các brick

- Volume được mount bởi client: `mount -t glusterfs server1:/ /my/mnt/point`

- Một Volume có thể chứa các brick từ các node khác nhau

- Sau đây là mô hình tập hợp những Brick thành Volume

![](/glusterFS/images/volume.png)

Tại hình trên, chúng ta có thể thẫy mỗi Node1, Node2, Node3 đã tạo 2 brick là `/export/brick1` và `/export/brick2`

Và từ 3 brick `/export/brick1` trên 3 node đã tạo thành 1 volume music

Tương tự với 3 brick `/export/brick2` trên 3 node tập hợp lại thành volume Videos

## Các loại volume trong GlusterFS

Khi sử dụng GlusterFS có thể tạo nhiều loại Volume và mỗi loại có được những tính năng khác nhau. Dưới đây là 5 loại volume cơ bản

**Distributed volume**

Distributed Volume có những đặc điểm cơ bản sau:

- Dữ liệu được lưu trữ phân tán trên từng bricks, file1 nằm trong `brick1`, file 2 nằm trong `brick2`...

- Ưu điểm: Mở rộng được dung lượng store (Dung lượng store bằng tổng dung lượng các brick)

- Nhược điểm: Nếu 1 trong các brick bị lỗi, dữ liệu trên brick đó sẽ mất

![](/glusterFS/images/distributedVolume.png)

**Replicated Volume**

- Dữ liệu được nhân bản đến những brick còn lại, trên tất cả các node và đồng bộ tất cả các nhân bản mới cập nhật

- Đảm bảo tính nhất quán về mặt dữ liệu

- Không giới hạn số lượng replicas

- Ưu điểm: Phù hợp với hệ thống yêu cầu tính sẵn sàng cao

- Nhược điểm: Tốn tài nguyên hệ thống

![](/glusterFS/images/replicatedVolume.png)

**Stripe volume**

- Dữ liệu chia thành những phần khác nhau và lưu trữ ở những brick khác nhau (1 file được chia nhỏ ra trên các brick)

- Ưu điểm: Phù hợp với những môi trường yêu cầu hiệu năng, đặc biệt truy cập những file lớn

- Nhược điểm: Một brick bị lỗi volume không thể hoạt động được

![](/glusterFS/images/stripeVolume.png)

**Distributed replicated Volume**

Kết hợp từ Distributed và replicated

![](/glusterFS/images/distributedReplicateVolume.png)

Với mô hình trên, hệ thống sẽ yêu cầu cần tổi thiểu 3 node, vừa có thể mở rộng được dung lượng lưu trữ, vừa tăng tính dự phòng cho hệ thống. Tuy nhiên nếu đồng thời bị lỗi 2 node `server1` `server2` hoặc 2 node `server3` `server4` thì hệ thống sẽ không hoạt động được

**Distributed stripe Volume**

Kết hợp từ Distributed và stripe. Do đó nó có hầu hết những thuộc tính của hai loại trên và khi 1 node và 1 brick delete đồng nghĩa volume cũng không hoạt động được nữa

![](/glusterFS/images/distributedStripe.png)

**Replicated Strip Volume**

Kết hợp từ replicated và stripe

![](/glusterFS/images/replicatedStripe.png)
