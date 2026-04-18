<!-- add-breadcrumbs -->
# Lương bổ sung

**Lương bổ sung là khoản mà Nhân viên nhận được từ công ty nơi họ làm việc, ngoài mức lương thông thường của họ.**


ERPNext cung cấp cho bạn một tính năng gọi là Lương bổ sung để cộng thêm hoặc trừ đi khoản lương đột xuất cho một Nhân viên cụ thể trong khi xử lý Bảng lương. Một số ví dụ về Lương bổ sung có thể là Thưởng hiệu suất, Phụ cấp biệt phái, Lương truy lĩnh, Tiền thưởng hoặc các khoản điều chỉnh khác.

Để truy cập Lương bổ sung, hãy đi đến:

> Home > Human Resources > Payroll > Additional Salary

## 1. Điều kiện tiên quyết

Trước khi tạo Lương bổ sung, bạn nên tạo các mục sau:

* [Employee](employee.md)
* [Salary Component](salary-component.md)


## 2. Cách tạo Lương bổ sung


1. Đi đến danh sách Additional Salary, nhấn vào New.
2. Chọn Employee.
3. Chọn Salary Component.
4. Nhập Amount.
1. Nhập Payroll Date. Nếu Payroll Date cho Lương bổ sung nằm trong khoảng thời gian mà lương được xử lý, nó sẽ được cộng vào các khoản thu nhập/khấu trừ.
1. Lưu và Xác nhận.

Chọn hộp kiểm 'Overwrite Salary Structure Amount' để ghi đè thành phần Lương bổ sung lên số tiền trong Cấu trúc lương. Ngoài ra, có thể chọn hộp kiểm 'Deduct Full Tax on Selected Payroll Date' nếu cần khấu trừ toàn bộ thuế cho thành phần Lương bổ sung vào ngày tính lương cụ thể đó.

<img class="screenshot" alt="Additional Salary" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/additional-salary.png">

## 3. Tính năng

### 3.1 Lương bổ sung định kỳ
Tính năng này cho phép người dùng tạo một khoản Lương bổ sung cho một khoảng thời gian cố định.
Khi chọn 'Is Recurring', bạn cần điền 'To Date' và 'From Date'.
Điều này sẽ cộng hoặc trừ số tiền lương bổ sung cho nhân viên này trong phạm vi ngày được chọn và nó sẽ được phản ánh trong Phiếu lương của nhân viên. Lương bổ sung sẽ được lặp lại hàng tháng trong khoảng thời gian từ 'From Date' đến 'To Date'.

## 4. Các chủ đề liên quan

1. [Retention Bonus](retention-bonus.md)
1. [Employee Incentive](employee-incentive.md)
1. [Salary Structure](salary-structure.md)
1. [Salary Structure Assignment](salary-structure-assignment.md)
1. [Payroll Entry](payroll-entry.md)
1. [Payroll Period](payroll-period.md)


{next}