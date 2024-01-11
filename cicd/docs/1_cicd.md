# CI/CD

## CI - Continuous Integration

CI là Continuous Integration. Nó là phương pháp phát triển phần mềm yêu cầu các thành viên của team tích hợp công việc của họ thường xuyên, mỗi ngày ít nhất 1 lần. Mỗi tích sẽ được build tự động nhằm phát hiện ra lỗi nhanh nhất có thể

Một kịch bản CI bắt đầu bằng việc devloper commit code lên repository (gitlab chẳng hạn). Bất kỳ thay đổi nào trên repository cũ sẽ trigger một vòng đời CI. Các bước trong một kịch bản CI sẽ như sau:

- Đầu tiên, developer commit code lên repo

- CI server giám sát repo và kiểm tra xem liệu có thay đổi nào trên repo hay không (giám sát liên tục, chẳng hạn mỗi phút 1 lần)

- Ngay khi commit xảy ra, CI server phát hiện repo có thay đổi, nó nhận code mới nhất từ repo và sau đó build, test,...

- CI sẽ tiếp tục chờ thay đổi từ repo

![](/cicd/images/ci.png)

Mỗi lần developer làm xong task, họ phải chạy một private build (tức là chạy phần mềm trên local trước), kiểm tra cẩn thận và commit code lên repo khi đã thấy ổn. Bước này xảy ra thường xuyên và ở bất kỳ thời điểm nào trong ngày. Việc build tích hợp sẽ không xảy ra khi những thay đổi này chưa ảnh hưởng đến repo (kiểu như bạn commit mà chưa được merge vậy)

Tóm lại thì lợi ích của việc sử dụng CI là:

- Giảm thiểu rủi ro nhờ việc phát hiện lỗi sớm và fix sớm, tăng chất lượng phần mềm nhờ việc tự động test và inspect (đây cũng là một lợi ích của CI, code được inspect tự động dựa theo config đã cài đặt)

- Giảm thiểu những quy trình thủ công lặp đi lặp lại (build css, js, migrate, test ...)

- Sinh ra phần mềm có thể deploy ở bất kỳ thời gian địa điểm

## Continuous Delivery & Continuous Deployment

Trong khi Continuos Integration là quy trình để build và test tự động thì Continuous Delivery (tạm dịch là chuyển giao liên tục) bằng cách triển khai tất cả các thay đổi về code (đã được build và test) đến môi trường testing hoặc staging. Continuous Delivery cho phép developer tự động hóa phần testing bên cạnh việc sử dụng unit test, kiểm tra phần mềm qua nhiều thước đo trước khi triển khai cho khách hàng (production). Nó tự động hoàn toàn quy trình release phần mềm 

Có một khái niệm nữa là Continuous Deployment, và hai khái niệm này thường bị nhầm lẫn với nhau. Nếu Continuous Delivery là triển khai code lên môi trường dev, staging và deploy thủ công lên môi trường production thì Continuous Deployment (cũng viết tắt là CD) lại là kỹ thuật lên môi trường Production một cách tự động và cũng là mục tiêu của hầu hết công ty

![](/cicd/images/cd.png)

