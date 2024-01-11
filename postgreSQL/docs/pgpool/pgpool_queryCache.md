# In Memory Query Cache

In Memory Query Cache (IMQCache) là một tính năng trong Pgpool-II cho phép lưu trữ kết quả truy vấn của các câu lệnh SELECT vào bộ nhớ cache để cung cấp tốc độ truy vấn nhanh hơn cho các truy vấn tương tự trong tương lai. 

Khi một truy vấn SELECT được thực hiện từ client, Pgpool-II sẽ kiểm tra xem kết quả truy vấn đã được lưu trong IMQCache hay chưa. Nếu có nó sẽ trả về kết quả từ cache mà không cần thực hiện truy vấn thực tế lên cơ sở dữ liệu. Và tất nhiên khi Table được cập nhật thì các mục được lưu trong cache tương ứng sẽ được xóa

Điều này giúp giảm tải cho cơ sở dữ liệu và cung cấp thời gian truy xuất nhanh hơn cho các truy vấn SELECT lặp lại

**NOTE: Lưu ý rằng IMQCache chỉ hỗ trợ các câu lệnh SELECT. Các câu lệnh INSERT, UPDATE, DELETE ... và các câu lệnh không phải SELECT không được lưu trong cache**

# Enable IMQCache

`memory_cache_enabled` (boolean): Mặc định là off

# Options

`memqcache_expire` (integer)

Chỉ định thời gian tồn tại của bộ đệm truy vấn tính bằng giây. Mặc định là 0, tức là truy vấn vẫn được lưu trên bộ đệm, cho đến khi Table được cập nhật thì mới bị xóa

`memqcache_auto_cache_invalidation` (boolean)

Nếu set `on` sẽ tự động xóa bộ nhớ đệm liên quan đến các Table đã cập nhật. Khi tắt bộ nhớ đệm sẽ không bị xóa kể cả khi Table được cập nhật. Mặc định giá trị là `on`

`memqcache_maxcache` (integer)

Chỉ định kích thước tối đã tính bằng byte của kết quả truy vấn SELECT sẽ được lưu vào bộ đệm. Kết quả có kích thước dữ liệu lớn hơn giá trị này sẽ không được Pgpool-II lưu vào bộ nhớ đệm

`cache_safe_memqcache_table_list` (string)

Chỉ định danh sách TÊN của các Table, kết quả SELECT của các Table đó sẽ được Pgpool-II lưu vào bộ đệm

`cache_unsafe_memqcache_table_list` (string)

Ngược lại với `cache_safe_memqcache_table_list`. Chỉ định dạng sách Tên của các Table, kết quả SELECT của các Table này sẽ KHÔNG được Pgpool-II lưu vào bộ nhớ đệm


`memqcache_total_size` (integer)

Chỉ định kích thước bộ đệm bộ nhớ dùng chung. Mặc định là 64 MB

Mỗi bộ đệm được lưu trữ trong các KHỐI có kích thước cố định được chỉ định bởi `memqcache_cache_block_size`. Số lượng khối có thể được tính bằng `memqcache_total_size`/`memqcache_cache_block_size`. Kết quả truy vấn SELECT không được lưu trên nhiều KHỐI khác nhau trên bộ đệm

Khi một KHỐI lấp đầy bộ đệm, khối tiếp theo sẽ được sử dụng. Khi tất cả các KHỐI đầy, KHỐI cũ nhất sẽ bị xóa và sử dụng lại

`memqcache_cache_block_size` (integer)

Chỉ định kích thước KHỐI bộ đệm. Mặc định là 1 MB

`memqcache_memcached_host` (string)

Chỉ định tên máy chủ hoặc địa chỉ IP mà memqcache hoạt động. Bạn có thể sử dụng `localhost` nếu memqcache và Pgpool-II nằm trên cùng một máy chủ

`memqcache_memcached_port` (port)

Chỉ định port của memcached. Mặc định là 11211

> Tham khảo: https://www.pgpool.net/docs/44/en/html/runtime-in-memory-query-cache.html