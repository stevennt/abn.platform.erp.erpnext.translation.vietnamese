<!-- add-breadcrumbs -->
# Phiếu lương

**Phiếu lương là một chứng từ được cấp cho nhân viên. Nó chứa mô tả chi tiết về các thành phần lương và số tiền lương của nhân viên.**

Để truy cập Phiếu lương, hãy đi tới:
> Home > Human Resources > Payroll > Salary Slip

## 1. Điều kiện tiên quyết
Trước khi tạo Phiếu lương, bạn nên tạo các mục sau trước:

* [Nhân viên](/docs/v16/user/manual/vi/human-resources/employee)
* [Cấu trúc lương](/docs/v16/user/manual/vi/human-resources/salary-structure)
* [Gán cấu trúc lương](/docs/v16/user/manual/vi/human-resources/salary-structure-assignment)

## 2. Cách tạo Phiếu lương


1. Đi tới Salary Slip, Nhấp vào **Mới**.
1. Chọn **Nhân viên**. Khi chọn Nhân viên, tất cả thông tin chi tiết của Nhân viên sẽ được lấy từ Cấu trúc lương đã được gán cho Nhân viên đó. Thông tin này bao gồm các chi tiết như Kỳ tính lương (Payroll Frequency), Các khoản thu nhập (Earnings), Các khoản khấu trừ (Deductions), v.v.
1. Chọn **Ngày bắt đầu** và **Ngày kết thúc**.
1. **Lưu**.

## 3. Tính năng

### 3.1. Phiếu lương dựa trên Chấm công/Nghỉ phép

Người dùng HR có thể tạo Phiếu lương dựa trên Chấm công hoặc Nghỉ phép.
Số ngày làm việc sẽ được tính toán dựa trên việc nghỉ phép/Chấm công, tùy thuộc vào trường **Calculate Payroll Working Days Based On** trong [Cài đặt HR](/docs/v16/user/manual/vi/human-resources/hr-settings). Nếu việc tính lương dựa trên Chấm công, thì **Leave without pay** (Nghỉ không lương) sẽ được coi là vắng mặt và **half-day** (nửa ngày) sẽ được coi là vắng mặt nửa ngày.

### 3.2. Phiếu lương dựa trên Timesheet

Để tạo Phiếu lương dựa trên timesheet, bạn cần tạo Salary Structure cho Timesheets.

ERPNext cũng cung cấp tùy chọn tạo Phiếu lương dựa trên giờ làm việc dựa trên [Timesheet](/docs/v16/user/manual/vi/projects/timesheets).
Bạn có thể tạo Phiếu lương sau khi **Xác nhận** Timesheet bằng cách nhấp trực tiếp vào nút **Create Salary Slip** ở góc trên bên phải.

<img class="screenshot" alt="Create Salary Slip based on Timesheets" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/create-salary-slip-based-on-timesheets.png">

Số tiền Thanh toán được tính dựa trên Hour Rate (Đơn giá giờ) được xác định trong Salary Structure và được phản ánh trong bảng Thu nhập (Earnings).

### 3.3 Year to Date và Month to Date

Đối với mỗi phiếu lương, 'Year to Date' (Lũy kế từ đầu năm) và 'Month to Date' (Lũy kế từ đầu tháng) đều được tính toán.

<img class="screenshot" alt="Year to Date and Month to Date" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/ytd-and-mtd.png">

- **Year to Date**: Tổng lương đã ghi nhận cho nhân viên cụ thể đó từ đầu năm (kỳ tính lương hoặc năm tài chính) cho đến ngày kết thúc của phiếu lương hiện tại.
- **Month to Date**: Tổng lương đã ghi nhận cho một nhân viên cụ thể từ đầu tháng (tháng mà bút toán lương được tạo) cho đến ngày kết thúc của phiếu lương hiện tại.

Year to Date cũng được tính toán cho mọi thành phần trong bảng thu nhập và khấu trừ. Mẫu in "Salary Slip with Year to Date" có sẵn các tính toán Year to Date và Month to Date.

<img class="screenshot" alt="Year to Date for Salary Slip Components" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/ytd-component.png">