# Đơn vay vốn

**Đơn vay vốn là một chứng từ chứa thông tin liên quan đến Người nộp đơn vay, Loại khoản vay, Phương thức hoàn trả, Số tiền vay và Lãi suất.**

Nhân viên có thể đăng ký vay vốn bằng cách đi tới:

> Nhân sự > Khoản vay > Đơn vay vốn

## 1. Điều kiện tiên quyết

Trước khi tạo Đơn vay vốn, bạn nên tạo các chứng từ sau:

* [Nhân viên](employee.md)
* [Loại khoản vay](loan-type.md)

## 2. Cách tạo Đơn vay vốn

1. Đi tới: Đơn vay vốn > Mới.
1. Nhập tên Người nộp đơn.
1. Nhập thông tin khoản vay như Loại khoản vay, Số tiền vay và Ngày cần tiền.
1. Chọn [Phương thức hoàn trả](#31-phương-thức-hoàn-trả) và dựa trên thông tin khoản vay, các thông tin như Tổng số tiền phải trả và Lãi sẽ được tính toán.
1. Lưu và Xác nhận.

  <img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/loan-application.png">

## 3. Các tính năng

### 3.1 Phương thức hoàn trả

Có hai loại Phương thức hoàn trả trong Đơn vay vốn:

#### 1. Hoàn trả Số tiền cố định mỗi kỳ

* Nhập Số tiền thanh toán hàng tháng.
* Lưu.
* Sau khi lưu, dựa trên Lãi suất, Tổng lãi phải trả và Tổng số tiền phải trả sẽ được tính toán cùng với Kỳ hạn (tính theo tháng).
* Xác nhận.

  <img class="screenshot" alt="Repayment Fixed Amount Per Period" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/repayment1.png">

#### 2. Hoàn trả theo Số kỳ hạn

* Nhập Kỳ hạn hoàn trả (tính theo tháng).
* Lưu.
* Sau khi lưu, dựa trên Lãi suất, Tổng lãi phải trả và Tổng số tiền phải trả sẽ được tính toán cùng với Số tiền hoàn trả hàng tháng.
* Xác nhận.

  <img class="screenshot" alt="Repayment Fixed Amount Per Period" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/repayment2.png">

## 4. Các chủ đề liên quan

1. [Loại khoản vay](loan-type.md)
1. [Khoản vay](loan.md)