# High Availability - Phần 3: Tổng quan về Quorum, STONITH/Fencing

## Tổng quan về Quorum 

Định nghĩa 

`split-brain`: Là hiện tượng cluster lớn bị tách ra thành nhiều cluster nhỏ. Điều này sẽ dẫn đến sự mất đồng bộ giữa các tài nguyên, ảnh hưởng tới sự toàn vẹn của hệ thống

Quorum là giải pháp ngăn chặn hiện tượng "split brain" trong cluster. Cluster có quorum chỉ khi node đang hoạt động nhiều hơn một nửa số node thuộc Cluster (Số node hoạt động > tổng số node của cụm/2)

Quorum được thiết lập bằng cơ chế `voting`. Khi node thuộc cluster xảy ra sự cố hoặc mất kết nối với phần còn lại của cluster, các node hoạt động sẽ vote cho việc node nào sẽ bị đóng băng cô lập, node nào sẽ tiếp tục hoạt động

Kỹ thuật Quorum được hỗ trợ mặc định trong pacement, với 2 kỹ thuật

