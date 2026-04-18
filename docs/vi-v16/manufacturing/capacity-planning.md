<!-- add-breadcrumbs -->

> Được giới thiệu trong Phiên bản 16

# Lập kế hoạch năng lực

Lập kế hoạch năng lực là quá trình mà một tổ chức quyết định có chấp nhận các đơn hàng mới hay không dựa trên các nguồn lực và các lệnh sản xuất hiện có.

Lập kế hoạch năng lực đã được bật mặc định trong tài khoản của bạn, để biết thêm thông tin hãy đi đến:

> Trang chủ > Sản xuất > Cài đặt > Cài đặt sản xuất

<img class="screenshot" alt="Work Order" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/capacity_planning_settings.png">

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Lệnh sản xuất, bạn nên tạo các mục sau trước:

* [Định mức nguyên vật liệu](../manufacturing/bill-of-materials)
* [Công đoạn](../manufacturing/operation)
* [Máy móc/Trạm làm việc](../manufacturing/workstation)
* [Lệnh sản xuất](../manufacturing/work-order)

## 2. Cách thức Lập kế hoạch năng lực hoạt động trong ERPNext
Người dùng phải xác định số ngày trong trường "Lập kế hoạch năng lực cho" trong phần cài đặt sản xuất để lập kế hoạch cho các lệnh sản xuất sắp tới. Ví dụ, nếu bạn đặt Lập kế hoạch năng lực cho 30 ngày và để sản xuất 1 thành phẩm cần 5 ngày, thì vào ngày hiện tại người dùng chỉ có thể chấp nhận 6 lệnh sản xuất (30/5 = 6). Bạn có thể tiếp nhận Lệnh sản xuất tiếp theo khi [Máy móc/Trạm làm việc](../manufacturing/workstation) của bạn trống.

### 2.1 Tạo Lệnh sản xuất với các Công đoạn
Người dùng cần tạo Lệnh sản xuất kèm theo các Công đoạn để hệ thống có thể theo dõi thời gian của [Thẻ công việc](../manufacturing/job-card) so với Lệnh sản xuất.

<img class="screenshot" alt="Work Order" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/work_order_with_operations.png">

Sau khi người dùng Xác nhận Lệnh sản xuất, hệ thống sẽ tạo Thẻ công việc với chi tiết thời gian của Máy móc/Trạm làm việc hiện có. Nếu 'Cho phép làm thêm giờ' bị tắt trong Cài đặt sản xuất, hệ thống sẽ lập lịch công việc theo thời gian được xác định trong Máy móc/Trạm làm việc. Nếu "Cho phép sản xuất vào ngày lễ" bị tắt, hệ thống sẽ chỉ lập lịch công việc vào các ngày làm việc.

### 2.2 Năng lực sản xuất của Máy móc/Trạm làm việc

Trong Máy móc/Trạm làm việc, người dùng có thể thiết lập 'Năng lực sản xuất'. Đây là số lượng Công đoạn mà hệ thống sẽ cho phép bạn thực hiện tại Máy móc/Trạm làm việc này. Ví dụ, nếu một Máy móc/Trạm làm việc nhất định có thể xử lý 10 công đoạn cùng một lúc, hãy nhập 'Năng lực sản xuất' là 10.

<img class="screenshot" alt="Work Order" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/work_station_capacity.png">

### 2.3 Thẻ công việc với Thời gian
Hệ thống sẽ tự động tạo Thẻ công việc với thời gian cho từng công đoạn dựa trên thời gian cần thiết để hoàn thành công đoạn đó và sự sẵn có của Máy móc/Trạm làm việc. Người dùng phải thiết lập ngày bắt đầu dự kiến và dựa trên thời gian công đoạn, hệ thống sẽ tính toán ngày kết thúc dự kiến.

<img class="screenshot" alt="Work Order" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/job_card_timing.png">

### 2.4 Ngày bắt đầu và Ngày kết thúc dự kiến của Lệnh sản xuất
Dựa trên ngày bắt đầu và ngày kết thúc dự kiến, người dùng có thể tính toán năng lực của các máy móc/trạm làm việc của họ. Ngoài ra, họ có thể theo dõi trạng thái của lệnh sản xuất bằng cách sử dụng [Lịch](../using-erpnext/calendar).

Để xem lịch, hãy đi đến:

> Danh sách Lệnh sản xuất > Lịch > Mặc định

<img class="screenshot" alt="Work Order" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/work_order_calendar.png">

### 2.5 Lỗi lập kế hoạch năng lực
Nếu số ngày Năng lực sản xuất ít hơn thời gian cần thiết để hoàn thành công đoạn, hệ thống sẽ báo lỗi lập kế hoạch năng lực. Trong trường hợp này, người dùng phải tăng số ngày trong mục "Năng lực sản xuất" tại Cài đặt sản xuất hoặc giảm số lượng thành phẩm theo năng lực của Máy móc/Trạm làm việc.

<img class="screenshot" alt="Work Order" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/capacity_planning_error.png">