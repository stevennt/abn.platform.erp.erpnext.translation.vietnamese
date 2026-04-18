<!-- add-breadcrumbs -->
# Các chế độ xem Dự án

Vì các dự án luôn nhạy cảm về mặt thời gian, chúng ta cần các loại chế độ xem khác nhau để truyền tải thông tin một cách trực quan cho người dùng khi xem chúng.

Ngoài các chế độ xem danh sách và báo cáo thông thường cho dự án và công việc, ERPNext cũng cung cấp các chế độ xem Gantt, Kanban và Lịch cho các công việc. Bạn có thể truy cập các chế độ xem này bằng cách đi tới danh sách Công việc và chọn chúng thông qua thanh bên trái.

## Chế độ xem Gantt

Biểu đồ Gantt hiển thị cách các công việc được liên kết với nhau và cho thấy trình tự thực hiện của chúng, dựa trên ngày bắt đầu và ngày kết thúc được thiết lập trong các công việc cùng với bất kỳ sự phụ thuộc nào, nếu có.

![Task - Gantt View](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/project/task-gantt-chart.png)
*Biểu đồ Gantt cho Công việc*

Bạn có thể cập nhật phạm vi của biểu đồ bằng cách chọn một trong các tùy chọn: Quý, Nửa ngày, Ngày, Tuần hoặc Tháng.

Việc kéo một công việc dọc theo các ngày sẽ cập nhật ngày bắt đầu và ngày kết thúc của công việc đó.

Nếu bạn muốn tùy chỉnh thêm biểu đồ và làm cho nó nhiều màu sắc hơn, hãy đọc [bài viết này](articles/make-a-colorful-gantt-chart.md)

## Chế độ xem Kanban

Kanban trong tiếng Nhật có nghĩa là "bảng thông báo" hoặc "biển báo", vì phương pháp quản lý công việc này có nguồn gốc từ quy trình sản xuất tinh gọn của Toyota. Trong một thiết lập bảng kanban điển hình, bạn có một bảng hoặc một bức tường được chia thành các phần đại diện cho các giai đoạn thực hiện hoặc hoàn thành khác nhau. Các công việc được đưa lên bảng dưới dạng các tờ ghi chú (sticky notes) và di chuyển qua bảng để cập nhật giai đoạn hiện tại của chúng trong quy trình.

![Task - Kanban View](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/project/task-kanban.png)
*Bảng Kanban của ERPNext*

ERPNext hiển thị chế độ xem Kanban cho các công việc dựa trên trạng thái của chúng. Bạn có thể cập nhật trạng thái của một công việc bằng cách di chuyển thẻ đại diện từ cột này sang cột tiếp theo. Bạn cũng có thể gán màu cho các cột này để dễ dàng tham chiếu trực quan.

Đọc [tùy chỉnh bảng Kanban](../customize-erpnext/kanban-board.md) để tìm hiểu thêm.

## Chế độ xem Lịch

Giống như biểu đồ Gantt, chế độ xem lịch cũng hiển thị công việc và số ngày dự kiến cần thiết để hoàn thành. Tuy nhiên, chế độ xem này hiển thị công việc trải dài trên lịch thông thường của bạn.

![Task - Calendar View](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/project/task-calendar.png)
*Chế độ xem Lịch cho Công việc*

{next}