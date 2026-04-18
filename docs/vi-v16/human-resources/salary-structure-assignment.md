<!-- add-breadcrumbs -->
# Phân bổ Cấu trúc Lương

**Biểu mẫu Phân bổ Cấu trúc Lương cho phép bạn phân bổ một Cấu trúc Lương cụ thể cho nhân viên.**

Trong ERPNext, bạn có thể tạo nhiều bản Phân bổ Cấu trúc Lương cho cùng một Nhân viên cho các giai đoạn khác nhau.

Để truy cập Phân bổ Cấu trúc Lương, hãy đi đến:
> Home > Human Resources > Payroll > Salary Structure Assignment

## 1. Điều kiện tiên quyết

Trước khi bạn tạo Phân bổ Cấu trúc Lương, bạn nên có sẵn các tài liệu sau:

1. [Nhân viên](/docs/v16/user/manual/vi/human-resources/employee)
1. [Thành phần lương](/docs/v16/user/manual/vi/human-resources/salary-component)
1. [Cấu trúc lương](/docs/v16/user/manual/vi/human-resources/salary-structure)

## 2. Cách tạo Phân bổ Cấu trúc Lương:

1. Đi đến danh sách Salary Structure Assignment và nhấn vào New.
1. Chọn Nhân viên và Cấu trúc lương.
1. Chọn Ngày bắt đầu (From Date) mà Cấu trúc Lương cụ thể này sẽ được áp dụng.
1. Chọn mức Thuế thu nhập (Income Tax Slab) ưu tiên cho nhân viên.
1. Nhập số tiền Cơ bản (Base) và Biến đổi (Variable) theo yêu cầu. Số tiền Cơ bản đề cập đến Lương cơ bản của Nhân viên, là khoản cố định được chi trả, bất kể nhân viên có đạt được mục tiêu hay không. Ngược lại, lương Biến đổi là phần thù lao bán hàng được xác định dựa trên hiệu suất của nhân viên. Khi nhân viên đạt được mục tiêu (hay còn gọi là chỉ tiêu), lương biến đổi sẽ được cung cấp dưới dạng tiền thưởng, tiền khuyến khích hoặc hoa hồng.

 <img class="screenshot" alt="Salary Structure Assignment" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/salary-structure-assignment.png">

### 2.1 Các cách khác để tạo Phân bổ Cấu trúc Lương

Bạn cũng có thể phân bổ Cấu trúc Lương cho (các) Nhân viên trực tiếp thông qua tài liệu Cấu trúc lương. Để phân bổ Cấu trúc Lương cho một nhân viên duy nhất, hãy nhấp vào nút 'Assign Salary Structure' trong tài liệu Cấu trúc lương.

<img class="screenshot" alt="Salary Structure Assignment" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/assign-sal1.png">

Nếu bạn muốn phân bổ hàng loạt Cấu trúc Lương cho nhiều nhân viên, bạn có thể thực hiện thông qua nút 'Assign to Employees'.

<img class="screenshot" alt="Salary Structure Assignment" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/assign-sal2.png">

Bạn có thể tùy chọn lọc nhân viên dựa trên Cấp bậc nhân viên (Employee Grade), Phòng ban (Department), Chức danh (Designation) và chính Nhân viên đó.

<img class="screenshot" alt="Salary Structure Assignment" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/assign-sal3.png">

Sau khi hoàn tất, hãy nhấn nút 'Assign' để thực hiện phân bổ Cấu trúc Lương tương ứng.

## 3. Các chủ đề liên quan

1. [Thành phần lương](/docs/v16/user/manual/vi/human-resources/salary-component)
1. [Cấu trúc lương](/docs/v16/user/manual/vi/human-resources/salary-structure)
1. [Cấp bậc nhân viên](/docs/v16/user/manual/vi/human-resources/employee-grade)
1. [Phòng ban](/docs/v16/user/manual/vi/human-resources/department)
1. [Chức danh](/docs/v16/user/manual/vi/human-resources/designation)
1. [Phiếu lương](/docs/v16/user/manual/vi/human-resources/payroll-entry)