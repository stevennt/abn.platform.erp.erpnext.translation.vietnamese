<!-- add-breadcrumbs -->
# Tài khoản Ngân hàng

Trong ERPNext, Tài khoản Ngân hàng có thể được tạo cho Công ty cũng như các bên khác như Khách hàng, Nhà cung cấp, v.v. Việc này cho phép bạn ghi lại tất cả các giao dịch ngân hàng một cách chính xác để đảm bảo tính chính xác trong kế toán.

Bạn có thể thêm Tài khoản Ngân hàng trong ERPNext cho Công ty, Nhà cung cấp, Khách hàng hoặc bất kỳ bên nào khác mà các giao dịch được thực hiện. Sau đó, Tài khoản Ngân hàng có thể được chọn trong [Bút toán thanh toán](payment-entry.md) dưới dạng [Phương thức thanh toán](mode-of-payment.md).

Để truy cập Tài khoản Ngân hàng, hãy đi tới:
> Trang chủ > Kế toán > Sao kê ngân hàng > Tài khoản Ngân hàng

![Bank Account](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/bank-account.png)

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Tài khoản Ngân hàng, bạn nên tạo các mục sau trước:

* [Ngân hàng](bank.md)

## 2. Cách tạo Tài khoản Ngân hàng
1. Nhập Tên tài khoản.
1. Liên kết tài khoản Sổ cái được thiết lập trong 'Tài khoản Ngân hàng' trong [Hệ thống tài khoản](chart-of-accounts.md).
1. Chọn một Ngân hàng.
1. Lưu.

### 2.1 Các tùy chọn bổ sung khi tạo Tài khoản Ngân hàng

* **Is the Default Account (Là tài khoản mặc định)**: Bật tùy chọn này sẽ sử dụng đây làm tài khoản ngân hàng mặc định cho tất cả các bút toán.
* **Is Company Account (Là tài khoản Công ty)**: Bật nếu Tài khoản Ngân hàng này là tài khoản của Công ty.
* Có thể thiết lập Loại tài khoản (Account Type) và Loại tài khoản phụ (Account Subtype) để phân loại chi tiết hơn trong các báo cáo, v.v.

## 3. Các tính năng
### 3.1 Chi tiết về Bên liên quan

* **Party Type (Loại bên liên quan)**: Nếu đây không phải là tài khoản công ty, hãy thiết lập tài khoản này thuộc về ai. Các tùy chọn có sẵn là: Khách hàng, Nhân viên, Thành viên, Cổ đông, Học sinh và Nhà cung cấp.
* **Party (Bên liên quan)**: Chọn Khách hàng/Nhà cung cấp cụ thể, v.v.

### 3.2 Chi tiết tài khoản

Để tham khảo, các chi tiết sau về Tài khoản Ngân hàng có thể được lưu trữ trong ERPNext:

* IBAN
* Số tài khoản ngân hàng (Bank Account No)
* Mã chi nhánh (Branch Code)
* Mã SWIFT

### 3.3 Địa chỉ và Liên hệ

* **Địa chỉ (Address)**: Một ngân hàng có thể có nhiều chi nhánh trong cùng một khu vực. Địa chỉ chi nhánh ngân hàng có thể được thiết lập tại đây.
* **Liên hệ (Contact)**: Có thể liên kết một Người liên hệ tại đây. Các ngân hàng thường cung cấp một người liên hệ chuyên trách cho các tài khoản doanh nghiệp, bạn có thể thêm thông tin liên hệ của người đó tại đây.
* **Website**: Bạn có thể thêm trang web của ngân hàng tại đây.

### 3.4 Chi tiết tích hợp

**Last Integration Date (Ngày tích hợp cuối cùng)**: Nếu ngân hàng của bạn hỗ trợ [Tích hợp Plaid](../erpnext_integration/plaid_integration.md), việc thiết lập một ngày tại đây sẽ thực hiện đồng bộ hóa vào ngày đã chọn. Việc này sẽ tạo ra các bút toán Giao dịch Ngân hàng.

{next}