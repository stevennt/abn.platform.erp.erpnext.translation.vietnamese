<!-- add-breadcrumbs -->
# Chấm công

**Chấm công là bản ghi cho biết một Nhân viên có hiện diện vào một ngày cụ thể hay không.**

Trong ERPNext, bạn có thể đánh dấu và ghi lại việc chấm công của một Nhân viên hàng ngày bằng cách sử dụng DocType Chấm công.

Để truy cập Chấm công, hãy đi tới:

> Home > Human Resources > Attendance

## 1. Điều kiện tiên quyết

Trước khi tạo bản ghi Chấm công, bạn nên tạo các mục sau trước:

* [Employee](/docs/v16/user/manual/en/human-resources/employee)
* [Shift Type](/docs/v16/user/manual/en/human-resources/shift-management)

## 2. Cách tạo Chấm công

1. Đi tới danh sách Chấm công, nhấn vào New.
1. Chọn Nhân viên.
1. Chọn Ngày chấm công.
1. Chọn Ca làm việc (tùy chọn).
1. Chọn Trạng thái (Có mặt, Vắng mặt, Nghỉ phép, Nửa ngày).
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Attendance" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/attendance.png">


> **Lưu ý:** Không thể đánh dấu chấm công cho các ngày trong tương lai.


Bạn có thể lấy báo cáo hàng tháng về dữ liệu Chấm công của mình bằng cách đi tới báo cáo **Monthly Attendance Details**.

Bạn có thể dễ dàng thiết lập chấm công cho Nhân viên bằng cách sử dụng [Employee Attendance Tool](/docs/v16/user/manual/en/human-resources/employee-attendance-tool).

Bạn cũng có thể tải lên dữ liệu chấm công hàng loạt bằng cách sử dụng [Upload Attendance](/docs/v16/user/manual/en/human-resources/upload-attendance).

## 3. Các tính năng
### 3.1 Đánh dấu các bản ghi Chấm công chưa được đánh dấu
Trong trường hợp việc chấm công cho một số nhân viên chưa được ghi nhận, bạn có thể đánh dấu họ là có mặt, vắng mặt hoặc nửa ngày.

#### Cách Đánh dấu Chấm công
1. Đi tới danh sách Chấm công.
1. Nhấn vào nút **Mark Attendance**.
1. Một hộp thoại sẽ xuất hiện.
1. Chọn Nhân viên và Tháng.
1. Chọn Trạng thái là Có mặt, Vắng mặt hoặc Nửa ngày.
1. Chọn các ngày mà bạn muốn đánh dấu chấm công cho Nhân viên đã chọn.
1. Nhấn vào nút **Mark Attendance** và nhấn **Yes**.

    <img class="screenshot" alt="Attendance" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/marking_unmarked_attendance.gif">

## 4. Các chủ đề liên quan

1. [Employee Attendance Tool](/docs/v16/user/manual/en/human-resources/employee-attendance-tool)
1. [Shift Management](/docs/v16/user/manual/en/human-resources/shift-management)
1. [Auto Attendance](/docs/v16/user/manual/en/human-resources/auto-attendance)
1. [Upload Attendance](/docs/v16/user/manual/en/human-resources/upload-attendance)
1. [Attendance Request](/docs/v16/user/manual/en/human-resources/attendance-request)


Ngoài ra, bạn cũng có thể thiết lập việc đánh dấu chấm công tự động dựa trên nhật ký check-in/check-out từ các Thiết bị Sinh trắc học/RFID (hoặc bất kỳ cơ chế tương tự nào khác tạo ra nhật ký VÀO/RA của nhân viên). Vui lòng tham khảo tính năng [Auto Attendance](/docs/v16/user/manual/en/human-resources/auto-attendance) để biết thêm thông tin.

{next}