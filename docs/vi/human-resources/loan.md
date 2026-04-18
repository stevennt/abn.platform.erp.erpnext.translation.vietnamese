# Khoản vay

**Sau khi Đơn xin vay vốn được quản lý phê duyệt, một bản ghi Khoản vay và lịch trình thanh toán có thể được tạo cho Người nộp đơn bằng cách sử dụng Khoản vay.**

Để truy cập Khoản vay, hãy đi tới:

> Human Resources > Loans > Loan


## 1. Điều kiện tiên quyết

Trước khi tạo bản ghi Khoản vay, bạn cần phải tạo các tài liệu sau:

* [Loại khoản vay](loan-type.md)
* [Đơn xin vay vốn](loan-application.md)
* [Hệ thống tài khoản](../accounts/chart-of-accounts.md)

## 2. Cách tạo bản ghi Khoản vay

1. Đi tới: Loan > New.
1. Chọn tên Người nộp đơn.
1. Chọn Đơn xin vay vốn. Sau khi chọn, các thông tin khoản vay như Loại khoản vay, Số tiền vay, Lãi suất, Phương thức thanh toán, Kỳ hạn thanh toán (tháng) và Số tiền thanh toán hàng tháng sẽ được tự động lấy về.
1. Nhập Ngày bắt đầu thanh toán.

  <img class="screenshot" alt="Loan" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/loan1.png">

1. Nhập Thông tin tài khoản như Phương thức thanh toán, Tài khoản thanh toán, Tài khoản khoản vay và Tài khoản thu nhập lãi.
1. Lưu. Sau khi lưu, Lịch trình thanh toán sẽ tự động được tạo. Ngày thanh toán đầu tiên sẽ được thiết lập theo "Ngày bắt đầu thanh toán".


  <img class="screenshot" alt="Repayment Schedule" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/loan2.png">

> Lưu ý: Tích chọn "Repay from Salary" nếu khoản thanh toán khoản vay sẽ được khấu trừ vào lương.

Ngoài ra, bạn có thể tạo bản ghi Khoản vay trực tiếp từ [Đơn xin vay vốn](loan-application.md)


## 3. Các tính năng

### 3.1 Tạo Bút toán giải ngân

Sau khi Xác nhận tài liệu Khoản vay, nếu trạng thái là "Sanctioned" (Đã phê duyệt), bạn có thể nhấp vào "Create Disbursement Entry" để tạo một Bút toán cho Khoản vay.


<img class="screenshot" alt="Disbursement Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/disbursement-entry.png">

### 3.2 Khấu trừ thanh toán khoản vay từ Lương

Để tự động khấu trừ khoản thanh toán Khoản vay từ Lương, hãy tích chọn "Repay from Salary" trong Khoản vay. Nó sẽ hiển thị dưới dạng Khoản thanh toán khoản vay trong Phiếu lương.

<img class="screenshot" alt="Salary Slip" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/loan-repayment-salary-slip.png">

### 3.3 Gia hạn Khoản vay
Số tiền vay được khấu trừ từ lương. Nếu nhân viên nghỉ không lương trong một khoảng thời gian, khoản vay hiện tại có thể được gia hạn mà không cần phải tạo khoản vay mới. Điều này có thể được thực hiện bằng cách chỉnh sửa bảng Lịch trình thanh toán ngay cả sau khi đã Xác nhận khoản vay.

![Extending Loan](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/change-loan-amount.gif)

## 4. Các chủ đề liên quan

1. [Bút toán](../accounts/journal-entry.md)
1. [Bút toán bảng lương](payroll-entry.md)