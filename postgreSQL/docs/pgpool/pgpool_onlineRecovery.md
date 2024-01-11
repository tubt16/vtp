# Online Recovery

Pgpool-II có thể đồng bộ hóa các node cơ sở dữ liệu và đính kèm node mà không cần dừng dịch vụ. Tính năng này được gọi là "online recovery". Online recovery có thể được thực hiện bằng cách sử dụng lệnh `pcp_recovery_node`

Để khôi phục trực tuyến (Online recovery), node target phải ở trạng thái bị detach khỏi cụm. Điều này có nghĩa là node phải được detach thủ công bởi lệnh `pcp_detach_node` hoặc tự động bị detach bởi Pgpool-II failover

Nếu muốn thêm một máy chủ mới vào cụm, hãy thêm máy chủ đó vào file config của Pgpool-II (`pgpool.conf`), sau khi thêm `backend_hostname` và tham số liên quan của nó. Thao tác này sẽ đăng ký thêm mới một node backend dưới dạng bị detach, sau đó bạn chỉ cần thực thi lệnh `pcp_recovery_node` máy chủ mới này sẽ được thêm vào cụm

**NOTE: Nếu service PostgreSQL trên node backend target đang được khởi động, bạn phải tắt nó trước khi chạy lệnh `pcp_recovery_node`**

Online Recovery được thực hiện theo hai giai đoạn. Giai đoạn đầu tiên được gọi là "first stage" và giai đoạn thứ hai gọi là "second stage". Chỉ có chế độ `native_replication_mode` và `snapshot_isolation_mode` mới yêu cầu thực hiện "second stage" trong Online Recovery

Trong giai đoạn đầu tiên (first stage), node standby (replica) được tạo ra bằng cách sử dụng lệnh `pg_basebackup` của PostgreSQL (Tham khảo về lệnh `pg_basebackup` tại [đây](/postgreSQL/docs/postgreSQL_streamingReplication.md) )

Trong giai đoạn thứ hai (second stage), node target sẽ được start và sẽ được đồng bộ cơ sở dữ liệu với node Primary

Bạn cần cung cấp các file kịch bẳn (scripts) cho từng stage. Các file mẫu hoàn chỉnh được lưu trong `/etc/pgpool-II/sample_scripts/`

**Pgpool thực hiện các bước sau khi thực hiện khôi phục trực tuyến:**

- CHECKPOINT

- Thực thi "first stage" trong Online Recovery (file mẫu có trong `/etc/pgpool-II/sample_scripts/`)

- Đợi cho tất cả các kết nối từ client bị ngắt kết nối (Chỉ đối với `native_replication_mode` và `snapshot_isolate_mode`)

- CHECKPOINT (Chỉ đối với `native_replication_mode` và `snapshot_isolate_mode`)

- Thực thi "second stage" trong Online Recovery (Chỉ đối với `native_replication_mode` và `snapshot_isolate_mode`)

- Khởi động postmaster (thực hiện `pgpool_remote_start`). `pgpool_remote_start` là tập lệnh để khởi động node PostgreSQL target. `pgpool_remote_start` nhận 2 tham số sau:

	+ Tên máy chủ của node backend cần được khôi phục

	+ Đường dẫn đến cụm cơ sở dữ liệu của node Primary

- Attach Node vào cụm

# Các tham số cần thêm trong `pgpool.conf` để thực hiện khôi phục trực tuyến

`recovery_user` (string): 

- Chỉ định tên người dùng PostgreSQL để thực hiện khôi phục trực tuyến

`recovery_password` (string): 

- Chỉ định mật khẩu cho tên người dùng PostgreSQL được cấu hình trong `recovery_user` để thực hiện khôi phục trực tuyến

- Nếu `recovery_password` được để trống, Pgpool-II trước tiên sẽ cố lấy mật khẩu cho `recovery_user` từ tệp `pool_passwd` trước khi sử dụng mật khẩu trống

`recovery_1st_stage_command` (string):

- Chỉ định tệp sẽ được chạy bởi node Primary ở stage đầu tiên của của quá trình Online recovery. Tệp lệnh phải được đặt trong thư mục cơ sở dữ liệu vì lý do bảo mật. Ví dụ `recovery_1st_stage_command = 'recovery_1st_stage'` thì Pgpool-II sẽ tìm tập lệnh trong thư mục $PGDATA (thư mục chứa cở sở dữ liệu của PostgreSQL) và sẽ cố gắng thực thi `$PGDATA/recovery_1st_stage`

`recovery_1st_stage_command` nhận đủ 7 tham số sau

- Đường dẫn đến cụm cơ sở dữ liệu của node Primary

- Hostname của node backend cần được khôi phục

- Đường dẫn đến cụm cơ sở dữ liệu của node cần khôi phục

- Port của node Primary 

- ID của node cần được khôi phục

- Port của node cần được khôi phục

- Host name của node Primary

`recovery_timeout` (integer):

- Chỉ định thời gian chờ tính bằng giây để hủy quá trình khôi phục trực tuyến nếu nó không hoàn thành trong thời gian này 

`client_idle_limit_in_recovery` (integer)

- Chỉ định thời gian để ngắt kết nối máy khách nếu nó không hoạt động kể từ lần truy vấn cuối cùng trong quá trình khôi phục trực tuyến 

> Tham khảo: https://www.pgpool.net/docs/44/en/html/runtime-online-recovery.html