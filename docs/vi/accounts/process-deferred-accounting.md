<!-- add-breadcrumbs -->
# Xử lý kế toán hoãn lại

**Xử lý kế toán hoãn lại là một nhật ký được tạo ra sau mỗi lần xử lý doanh thu hoặc chi phí hoãn lại.**

Các bản ghi Xử lý kế toán hoãn lại được tạo tự động khi hạch toán Doanh thu hoặc Chi phí hoãn lại. Việc này được thực hiện thông qua một tác vụ chạy ngầm, nhưng người dùng cũng có thể tạo bản ghi để hạch toán Doanh thu hoặc Chi phí hoãn lại theo cách thủ công.

Để truy cập danh sách Xử lý kế toán hoãn lại, hãy đi tới:
> Trang chủ > Kế toán > Sổ cái > Xử lý kế toán hoãn lại

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Xử lý kế toán hoãn lại, bạn nên tạo và tìm hiểu trước các mục sau:

* [Doanh thu hoãn lại](deferred-revenue.md)
* [Chi phí hoãn lại](deferred-expense.md)


## 2. Cách tạo Xử lý kế toán hoãn lại
1. Đi tới danh sách Xử lý kế toán hoãn lại, nhấn vào Mới.
1. Nhập Công ty.
1. Chọn loại quy trình kế toán hoãn lại. Chọn 'Income' để hạch toán doanh thu hoãn lại hoặc chọn 'Expense' để hạch toán chi phí hoãn lại.
1. Mở rộng phần ngày hạch toán.
1. Nhập Ngày bắt đầu và Ngày kết thúc dịch vụ.
1. Lưu và Xác nhận.

![Process Deferred Revenue](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/process-deferred-accounting.png)

## 3. Các tính năng

### 3.1 Khi Xác nhận

Khi Xác nhận một tài liệu Xử lý kế toán hoãn lại, các Bút toán sổ cái (GL Entries) cho việc hạch toán doanh thu hoặc chi phí hoãn lại sẽ được tạo cho tất cả các hóa đơn nằm trong khoảng giữa Ngày bắt đầu và Ngày kết thúc dịch vụ.

Nhập tài khoản nếu Doanh thu hoặc Chi phí hoãn lại chỉ cần được hạch toán cho một tài khoản thu nhập hoặc chi phí hoãn lại cụ thể.

### 3.2 Bật kế toán hoãn lại tự động

Để bật kế toán hoãn lại tự động, hãy chọn ô 'Automatically Process Deferred Account Entry' bằng cách điều hướng đến Cài đặt kế toán.

Để truy cập Cài đặt kế toán, hãy đi tới:
> Trang chủ > Kế toán > Danh mục kế toán > Cài đặt kế toán

![Deferred Accounting Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/deferred-accounting-settings.png)

{next}