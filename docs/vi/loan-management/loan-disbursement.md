<!-- add-breadcrumbs -->
# Giải ngân khoản vay
> Giới thiệu trong Phiên bản 13

**Sau khi Khoản vay được phê duyệt, số tiền vay đã sẵn sàng để được giải ngân. Để thực hiện việc đó, một bản ghi Giải ngân khoản vay sẽ được tạo.**

<img class="screenshot" alt="Make Loan Disbursement" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-disbursement-flow.png">

Để truy cập danh sách Giải ngân khoản vay, hãy đi tới:
> Home > Loan Management > Disbursement and Repayment > Loan Disbursement


<img class="screenshot" alt="Loan Disbursement" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-disbursement.png">

## 1. Điều kiện tiên quyết
Trước khi tạo Giải ngân khoản vay, bạn phải tạo các mục sau trước:

* [Loan](loan.md)


## 2. Cách tạo Giải ngân khoản vay
1. Đi tới Danh sách Giải ngân khoản vay, nhấn vào New.
2. Chọn Loan mà số tiền vay sẽ được giải ngân. Loại người đăng ký (Applicant Type) và Người đăng ký (Applicant) sẽ được lấy từ Loan.
3. Nhập Ngày giải ngân (Disbursement Date).
4. Nhập Số tiền giải ngân (Disbursed Amount).
7. Nhấn "Save" để lưu bản Nháp của Giải ngân khoản vay.
8. Nhấn "Submit" để xác nhận Cam kết bảo lãnh khoản vay.

### 2.1. Các cách khác để tạo Giải ngân khoản vay
Bạn cũng có thể tạo Giải ngân khoản vay từ một Khoản vay đã được phê duyệt thông qua nút **Create** ở góc trên bên phải.

<img class="screenshot" alt="Create Loan Disbursement" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/create-loan-disbursement.png">

## 3. Các tính năng

### 3.1 Giải ngân nhiều lần cho một Khoản vay
Có thể thực hiện nhiều lần Giải ngân khoản vay cho một Khoản vay, miễn là bạn không vượt quá số tiền khoản vay đã được phê duyệt.

### 3.2 Giải ngân thêm (Loan Topup)
Việc Giải ngân khoản vay cũng có thể được thực hiện sau khi một phần số tiền vay đã được hoàn trả và vẫn còn đủ tài sản bảo đảm được cam kết cho khoản vay đó. Điều này được gọi là giải ngân thêm (loan topup).

{next}