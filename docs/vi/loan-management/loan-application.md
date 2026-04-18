<!-- add-breadcrumbs -->
# Đơn vay vốn
> Giới thiệu trong Phiên bản 13

**Một Đơn vay vốn bao gồm các chi tiết về người nộp đơn và các chi tiết tài sản đảm bảo khoản vay để xem xét.**

Trong quá trình vay vốn, bước đầu tiên mà khách hàng hoặc nhân viên phải thực hiện là xác nhận một Đơn vay vốn để xem xét. Trong trường hợp khoản vay có tài sản đảm bảo, Đơn vay vốn cũng có thể bao gồm các tài sản đảm bảo khoản vay được đề xuất.

<img class="screenshot" alt="Make Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-application-flow.png">

Để truy cập danh sách Đơn vay vốn, hãy đi tới:
> Home > Loan Management > Loan > Loan Application


<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-application.png">

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Tài sản đảm bảo khoản vay, bạn nên tạo các mục sau trước:

* [Loại tài sản đảm bảo khoản vay](loan-security-type.md)
* [Tài sản đảm bảo khoản vay](loan-security.md)
* [Loại khoản vay](loan-type.md)

## 2. Cách tạo Đơn vay vốn
1. Đi tới Danh sách Đơn vay vốn, nhấn vào Mới.
2. Chọn Loại người nộp đơn.
3. Chọn Người nộp đơn.
4. Chọn Loại khoản vay. Tất cả các chi tiết về khoản vay như lãi suất, tài khoản khoản vay sẽ được tự động lấy từ Loại khoản vay.
5. Nhập Số tiền vay.
6. Nếu khoản vay là khoản vay có kỳ hạn, hãy nhập Phương thức hoàn trả. Nếu Phương thức hoàn trả được chọn là "Repay Over Number Of Periods" thì bạn sẽ phải nhập số tháng thực hiện hoàn trả vào mục "Repayment Period in Months". Nếu phương thức hoàn trả được chọn là "Repay Fixed Amount per Period" thì bạn sẽ phải nhập "Monthly Repayment Amount".
7. Bạn cũng có thể nêu các tài sản đảm bảo được đề xuất sẽ được thế chấp cho khoản vay. Để làm điều đó, trước tiên hãy tích vào ô "Is Secure Loan". Sau đó, trong bảng tài sản thế chấp đề xuất, bạn có thể nhập các tài sản đảm bảo và số lượng của chúng.
8. Nhấn "Lưu" để lưu bản nháp của Đơn vay vốn.
9. Nhấn "Xác nhận" để xác nhận đơn vay vốn.

## 3. Các tính năng

### 3.1 Tạo Cam kết tài sản đảm bảo khoản vay
Một [Cam kết tài sản đảm bảo khoản vay](loan-security-pledge.md) dựa trên các tài sản đảm bảo được đề xuất có thể được tạo trực tiếp từ Đơn vay vốn thông qua nút **Create** ở góc trên bên phải. Cam kết tài sản đảm bảo khoản vay này sau đó có thể được thế chấp cho một khoản vay như một Cam kết tài sản đảm bảo khoản vay ban đầu.

<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/create-loan-security-pledge.png">

### 3.2 Xác nhận Đơn vay vốn
Sau khi Đơn vay vốn được xác nhận và phê duyệt, bạn có thể tạo một Khoản vay từ Đơn vay vốn bằng cách sử dụng nút **Create** và tất cả các chi tiết cần thiết từ Đơn vay vốn sẽ được tự động ánh xạ vào khoản vay.

<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/create-loan.png">

{next}