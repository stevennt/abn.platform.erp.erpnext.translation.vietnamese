<!-- add-breadcrumbs -->
# Chuyên gia y tế

Chuyên gia y tế là các bác sĩ, điều dưỡng, hộ lý, kỹ thuật viên phòng xét nghiệm, v.v., những người đang phục vụ tại đơn vị bệnh viện theo những cách khác nhau. ERPNext Healthcare cho phép bạn tạo nhiều chuyên gia y tế và liên kết với một Người dùng (User) với các Vai trò (Roles) phù hợp. Bạn cũng có thể liên kết một Chuyên gia y tế với một [Nhân viên](/docs/v16/user/manual/en/human-resources/employee) để theo dõi Bảng lương, Chấm công hoặc các hoạt động Quản lý nhân sự khác.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/practitioner_1.png">

Để tạo một Chuyên gia y tế, hãy đi tới,

> Home > Healthcare > Masters > Healthcare Practitioner

## 1. Cách tạo Chuyên gia y tế

1. Đi tới danh sách Chuyên gia y tế và nhấn New.
2. Chọn Naming Series.
3. Nhập các chi tiết cơ bản như Họ tên, Tên, Giới tính, Số điện thoại di động.
4. Tùy chọn, chọn Khoa y tế (Medical Department).
4. Lưu.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/practitioner.png">

## 2. Các tính năng

### 2.1 Theo dõi Bảng lương, Chấm công, Vai trò và Quyền hạn

Để theo dõi tất cả các hoạt động Quản lý nhân sự cho Chuyên gia y tế, bạn cần tạo và chọn [Nhân viên](/docs/v16/user/manual/en/human-resources/employee) trong trường "Employee" trong hồ sơ chuyên gia. Điều này sẽ giúp chạy [Bảng lương](/docs/v16/user/manual/en/human-resources/payroll-intro) và cũng giúp theo dõi sự sẵn sàng và việc chấm công để đặt lịch hẹn bằng cách thiết lập [Danh sách ngày nghỉ](/docs/v16/user/manual/en/human-resources/holiday-list) và [Lịch làm việc của Chuyên gia](/docs/v16/user/manual/en/healthcare/practitioner_schedule) phù hợp. Sau đó, bạn có thể tạo một Người dùng ERPNext được liên kết với tài liệu Nhân viên. Điều này sẽ giúp theo dõi các quyền hạn cho Chuyên gia y tế.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/practitioner-employee.png">

> Lưu ý: Việc chọn trường Nhân viên sẽ lấy tất cả các trường liên quan đã được cấu hình trong tài liệu Nhân viên để giúp bạn thiết lập Chuyên gia y tế một cách dễ dàng.

Nếu các Chuyên gia y tế không phải là nhân viên trong các Đơn vị y tế của bạn, bạn có thể liên kết Người dùng với Chuyên gia y tế và chỉ định cho họ các vai trò cần thiết.

### 2.2 Sự sẵn sàng của Chuyên gia

Bạn có thể chọn nhiều [Lịch làm việc của Chuyên gia](/docs/v16/user/manual/en/healthcare/practitioner_schedule) cho mỗi chuyên gia và tùy chọn thiết lập một đơn vị dịch vụ nơi chuyên gia đó sẽ làm việc.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/practitioner_availability.png">

### 2.3 Chi phí của Chuyên gia y tế

Bạn có thể chọn hoặc tạo các mặt hàng dịch vụ cho phí tư vấn và thiết lập chúng trong "Out-Patient Consulting Charge Item" (Mặt hàng phí tư vấn ngoại trú) và "In-Patient Consulting Charge Item" (Mặt hàng phí tư vấn nội trú). Những thông tin này sẽ được lấy vào Hóa đơn bán hàng. Bạn có thể thiết lập các phí tư vấn áp dụng cho chuyên gia. Nếu cần, bạn cũng có thể chọn một Tài khoản thu nhập cho Bác sĩ để hạch toán tất cả các phí tư vấn vào các tài khoản riêng biệt.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/practitioner_charges.png">

> Lưu ý: Hãy đảm bảo rằng các Mặt hàng bạn tạo cho dịch vụ đã được bỏ chọn "Maintain Stock" (Theo dõi tồn kho) và "Include Items in Manufacturing" (Bao gồm mặt hàng trong sản xuất) vì chúng là các mặt hàng dịch vụ.

### 2.4 Bác sĩ giới thiệu

Bạn cũng có thể muốn quản lý danh sách các Bác sĩ là người giới thiệu Bệnh nhân đến cơ sở của mình. Bạn có thể quản lý dữ liệu như vậy ngay trong tài liệu Chuyên gia y tế bằng cách để trống các liên kết Nhân viên và Người dùng.

### 2.5 Liên kết nhiều Địa chỉ và Liên hệ

Giả sử Chuyên gia y tế làm việc tại nhiều bệnh viện khác nhau, bạn có thể liên kết nhiều thông tin liên hệ và địa chỉ cho Chuyên gia đó.

## 3. Các chủ đề liên quan

1. [Người dùng và Quyền hạn](/docs/v16/user/manual/en/setting-up/users-and-permissions)
2. [Nhân viên](/docs/v16/user/manual/en/human-resources/employee)
3. [Lịch làm việc của Chuyên gia](/docs/v16/user/manual/en/healthcare/practitioner_schedule)

{next}