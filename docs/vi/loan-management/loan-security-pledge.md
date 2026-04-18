<!-- add-breadcrumbs -->
# Tài sản thế chấp khoản vay
> Giới thiệu trong Phiên bản 13

**Tài sản thế chấp khoản vay bao gồm các tài sản đảm bảo và số lượng được thế chấp cho một Khoản vay.**

<img class="screenshot" alt="Make Loan Security Pledge" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-security-pledge-flow.png">

Để truy cập danh sách Tài sản thế chấp khoản vay, hãy đi tới:
> Home > Loan Management > Loan > Loan Security Pledge


<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-security-pledge.png">

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Tài sản thế chấp khoản vay, bạn nên tạo các mục sau trước:

* [Loan Security Type](loan-security-type.md)
* [Loan Security](loan-security.md)
* [Loan Application](loan-application.md)

## 2. Cách tạo Tài sản thế chấp khoản vay
1. Đi tới Danh sách Tài sản thế chấp khoản vay, nhấn vào Mới.
2. Chọn Loại người nộp đơn.
3. Chọn Người nộp đơn.
4. Chọn Công ty.
4. Nhập các Tài sản thế chấp khoản vay và số lượng cần bàn giao vào bảng Tài sản thế chấp. Giá Tài sản thế chấp khoản vay sẽ được lấy từ Giá trị tính giá trong danh mục Mặt hàng và số tiền sẽ được tự động tính toán.
6. Nhấn "Lưu" để lưu bản nháp của Tài sản thế chấp khoản vay.
7. Nhấn "Xác nhận" để xác nhận Tài sản thế chấp khoản vay.
8. Sau khi Tài sản thế chấp khoản vay được Xác nhận, nó đã sẵn sàng để được Thế chấp cho một Khoản vay.

### 2.1. Các cách khác để tạo Tài sản thế chấp khoản vay
1. Bạn cũng có thể tạo Tài sản thế chấp khoản vay từ một Đơn vay đã được phê duyệt thông qua nút **Create** ở góc trên bên phải

	<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/create-loan-security-pledge.png">

2. Hoặc bạn cũng có thể tạo Tài sản thế chấp khoản vay từ [Loan Security Shortfall](loan-security-shortfall.md) trong trường hợp thiếu hụt giá trị tài sản thế chấp khoản vay bằng cách nhấn vào nút **Add Loan Security** ở góc trên bên phải

	<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/shortfall-security.png">

{next}