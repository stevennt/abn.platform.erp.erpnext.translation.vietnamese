<!-- add-breadcrumbs -->
# Thưởng giữ chân

**Thưởng giữ chân là một khoản thanh toán hoặc phần thưởng nằm ngoài mức lương thông thường của nhân viên, được đưa ra như một sự khuyến khích để giữ chân một nhân viên chủ chốt ở lại làm việc.**

 ERPNext cho phép bạn cấu hình Thưởng giữ chân cho một Nhân viên trong một khoảng thời gian cụ thể.

Để truy cập Thưởng giữ chân, hãy đi tới:
> Home > Human Resources > Payroll > Retention Bonus

## 1. Điều kiện tiên quyết

Trước khi tạo Thưởng giữ chân, bạn nên tạo các mục sau:

* [Employee](employee.md)
* [Salary Component](salary-component.md)

## 2. Cách tạo Thưởng giữ chân

1. Đi tới danh sách Retention Bonus, nhấn vào New.
1. Chọn Employee và Bonus Payment Date.
1. Nhập Bonus Amount.
1. Chọn [Salary Component](salary-component.md) mà bạn muốn dùng để chi trả khoản thưởng.
1. Lưu và Xác nhận.
1. Sau khi xác nhận, tài liệu 'Additional Salary' của 'Salary Component' đã chỉ định sẽ được tạo. Thông tin này sẽ được lấy khi chạy Payroll Entry.

 <img class="screenshot" alt="Retention Bonus" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/retention-bonus.png">

## 3. Các chủ đề liên quan

1. [Employee Incentive](employee-incentive.md)
1. [Additional Salary](additional-salary.md)
1. [Salary Component](salary-component.md)
1. [Salary Structure](salary-structure.md)
1. [Payroll Entry](payroll-entry.md)

{next}