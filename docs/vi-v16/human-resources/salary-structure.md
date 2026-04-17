<!-- add-breadcrumbs -->
# Định mức lương

**Định mức lương là chi tiết về mức lương được đề nghị cho một Nhân viên, xét về sự phân chia của các thành phần khác nhau cấu thành nên khoản thù lao.**

Bất kỳ thay đổi nào đối với Định mức lương, tức là giữa các thành phần, đều có thể có tác động lớn đến những gì Nhân viên thực hiện, chẳng hạn như loại miễn thuế được yêu cầu.

ERPNext cho phép bạn xác định các Khoản thu nhập và Khoản khấu trừ của một Định mức lương, tần suất tính Bảng lương, và Phương thức thanh toán cùng các tính năng khác.

Để truy cập Định mức lương, hãy đi đến:
> Home > Human Resources > Payroll > Salary Structure


## 1. Điều kiện tiên quyết

Trước khi bạn tạo Định mức lương, bạn nên có các nội dung sau:

* [Thành phần lương](/docs/v16/user/manual/en/human-resources/salary-component)


## 2. Cách tạo Định mức lương

1. Đi đến danh sách Định mức lương, nhấp vào Mới.
2. Nhập Tên Định mức lương.
3. Chọn Tên Công ty và Tần suất tính Bảng lương.
4. Lưu và Xác nhận.


## 2. Tính năng

### 2.1 Khoản thu nhập và Khoản khấu trừ

Khoản thu nhập xác định các Thành phần lương mà Nhân viên được hưởng. Các thành phần này thường bao gồm lương cơ bản, phụ cấp, tiền thưởng và các khoản khuyến khích được cộng vào Tổng lương của nhân viên. Mặt khác, Khoản khấu trừ xác định các Thành phần lương được khấu trừ từ Tổng lương của nhân viên. Những khoản này thường bao gồm các loại thuế.

>**Lưu ý:** Chỉ các Thành phần lương được thiết lập là 'Earnings' mới được hiển thị trong bảng Thu nhập và các thành phần được thiết lập là 'Deductions' sẽ được hiển thị trong bảng Khấu trừ.


Để tạo Khoản thu nhập và Khoản khấu trừ, hãy chọn Thành phần lương trong cột Thành phần. Nhập Công thức/Điều kiện nếu chưa được chỉ định trước đó khi tạo [Thành phần lương](/docs/v16/user/manual/en/human-resources/salary-component). Ngoài ra, bạn cũng có thể nhập một số tiền xác định trước trong cột Số tiền.



<img class="screenshot" alt="Salary Structure" src="https://docs.erpnext.com/docs/v16/assets/img/human-resources/salary-structure.png">


> **Lưu ý:** Hãy đảm bảo nhấp vào mũi tên hướng xuống và bật hộp kiểm 'Amount based on formula' trong trường hợp Thành phần lương được tính toán bằng một công thức.


### 2.2 Tài khoản

Trong phần này, [Phương thức thanh toán](/docs/v16/user/manual/en/accounts/mode-of-payment) và [Tài khoản thanh toán](/docs/v16/user/manual/en/accounts/chart-of-accounts) được sử dụng để trả lương có thể được chỉ định.

### 2.3 Định mức lương cho Lương dựa trên Bảng chấm công

Trong ERPNext, bạn cũng có thể xác định Định mức lương cho Phiếu lương dựa trên Bảng chấm công, cho phép Công ty trả lương cho Nhân viên theo giờ làm việc.

Các bước để tạo Định mức lương dựa trên Bảng chấm công:

1. Đi đến Danh sách Định mức lương, nhấp vào Mới.
1. Chọn hộp kiểm **Salary Slip Based on Timesheet**.
1. Chọn Thành phần lương.
1. Nhập Đơn giá giờ. Dựa trên Đơn giá đã nhập, số tiền cho giờ làm việc của Thành phần lương được chọn sẽ được tính toán tương ứng.
1. Lưu và Xác nhận.

 <img class="screenshot" alt="Create Salary Slip based on Timesheets" src="https://docs.erpnext.com/docs/v16/assets/img/human-resources/salary-structure-for-salary-based-on-timesheets.png">


### 2.4 Số tiền quy đổi ngày nghỉ phép

Trong trường hợp Nhân viên có các ngày nghỉ có thể quy đổi thành tiền, bạn có thể xác định số tiền quy đổi ngày nghỉ mỗi ngày trong trường này cho Định mức lương cụ thể này. Dựa trên 'Thành phần thu nhập' được thiết lập trong [Loại nghỉ phép](/docs/v16/user/manual/en/human-resources/leave-type) được quy đổi và số tiền mỗi ngày, giá trị cho Thành phần lương sẽ được tính toán tương ứng trong Phiếu lương.


### 2.5 Phúc lợi tối đa (Số tiền)

Trong trường này, Số tiền Phúc lợi tối đa cho Định mức lương có thể được chỉ định. Nếu trường này được điền, hãy đảm bảo Định mức lương có một [Thành phần lương](/docs/v16/user/manual/en/human-resources/salary-component) với mục "Is Flexible Benefits" được chọn, mà theo đó số tiền này sẽ được chi trả.



Sau khi tất cả thông tin được lưu và xác nhận, bạn có thể gán Định mức lương cho một Nhân viên thông qua nút **Assign Salary Structure** hoặc bằng cách tạo một [Phân bổ Định mức lương](/docs/v16/user/manual/en/human-resources/salary-structure-assignment) mới thông qua trang tổng quan.

Bạn cũng có thể gán Định mức lương đã tạo cho nhiều nhân viên dựa trên [Cấp bậc nhân viên](/docs/v16/user/manual/en/human-resources/employee-grade), [Phòng ban](/docs/v16/user/manual/en/human-resources/department), [Chức danh](/docs/v16/user/manual/en/human-resources/designation), v.v. thông qua nút 'Assign to Employees'.
Ngoài ra, Phiếu lương cũng có thể được tạo trực tiếp thông qua trang tổng quan.

## 3. Các chủ đề liên quan

1. [Thành phần lương](/docs/v16/user/manual/en/human-resources/salary-component)
1. [Phân bổ Định mức lương](/docs/v16/user/manual/en/human-resources/salary-structure-assignment)
1. [Nhập bảng lương](/docs/v16/user/manual/en/human-resources/payroll-entry)