<!-- add-breadcrumbs -->
# Bút toán thanh toán

**Bút toán thanh toán là một bản ghi cho biết việc thanh toán đã được thực hiện cho một hóa đơn.**

Bút toán thanh toán có thể được thực hiện đối với các giao dịch sau:

* Hóa đơn bán hàng
* Hóa đơn mua hàng
* Đơn bán hàng (Thanh toán trước)
* Đơn mua hàng (Thanh toán trước)
* Yêu cầu thanh toán chi phí
* Chuyển khoản nội bộ

Trong ERPNext, có hai tùy chọn mà Người dùng có thể ghi nhận thanh toán:

* Bút toán thanh toán (Mặc định)
* Bút toán

Dưới đây là các sơ đồ để hiểu quy trình:

Trong Bán hàng:
![Payment Sales](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pe-sales.png)

Trong Mua hàng:
![Payment Purchase](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pe-purchase.png)


Để truy cập danh sách Bút toán thanh toán, hãy đi tới:
> Home > Accounting > Accounts Receivable/Payable > Payment Entry

## 1. Điều kiện tiên quyết
Một Bút toán thanh toán cũng có thể được tạo trực tiếp sau đó liên kết với một đơn hàng/hóa đơn sau. Trước khi tạo và sử dụng Bút toán thanh toán, lời khuyên là nên tạo các mục sau trước:

1. [Khách hàng](../CRM/customer.md)
1. [Nhà cung cấp](../buying/supplier.md)
1. [Tài khoản ngân hàng](bank-account.md)

Nếu bạn đang thực hiện theo Chu trình Bán hàng/Mua hàng, bạn sẽ cần các mục sau:

1. [Đơn bán hàng](../selling/sales-order.md) (Thanh toán trước)
1. [Đơn mua hàng](../buying/purchase-order.md) (Thanh toán trước)
1. [Hóa đơn bán hàng](sales-invoice.md)
1. [Hóa đơn mua hàng](purchase-invoice.md)


Thiết lập:

1. [Hệ thống tài khoản](chart-of-accounts.md)
1. [Công ty](../setting-up/company-setup.md) (để có các tài khoản mặc định)

## 2. Cách tạo Bút toán thanh toán
Khi Xác nhận một chứng từ mà từ đó có thể thực hiện Bút toán thanh toán, bạn sẽ thấy tùy chọn Thanh toán dưới nút **Create**.

![Payment Entry from Sales Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-entry-button-in-sales-invoice.png)

1. Thay đổi ngày hạch toán.
1. Loại thanh toán (Payment Type) sẽ được thiết lập dựa trên giao dịch mà bạn đang thực hiện. Các loại bao gồm 'Receive' (Nhận), 'Pay' (Chi) và 'Internal Transfer' (Chuyển khoản nội bộ).
1. Loại đối tác (Party Type), Đối tác (Party), Tên đối tác (Party Name) sẽ được lấy tự động.
1. Tài khoản nhận thanh toán (Account Paid To) và Tài khoản chi thanh toán (Account Paid From) sẽ được lấy theo thiết lập trong [mẫu Công ty](../setting-up/company-setup.md).
1. Số tiền đã thanh toán (Amount Paid) sẽ được lấy từ Hóa đơn.
1. Lưu và Xác nhận.
 ![Payment Entry from SO](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-entry-from-invoice.gif)

### 2.1 Tạo Thanh toán Thủ công
Một Bút toán thanh toán được tạo thủ công sẽ không có đơn hàng/hóa đơn nào được liên kết. Các khoản thanh toán thực hiện theo cách này sẽ được ghi nhận vào tài khoản của Khách hàng/Nhà cung cấp và có thể được đối chiếu sau bằng [Công cụ đối chiếu thanh toán](payment-reconciliation.md).

1. Đi tới danh sách Bút toán thanh toán và nhấn New.
1. Chọn Loại đối tác (Party Type) và Khách hàng/Nhà cung cấp tương ứng.
1. Chọn Tài khoản ngân hàng/Tài khoản tiền mặt nhận thanh toán (Account Paid To) và chi thanh toán (Account Paid From). Nhập Số séc và ngày nếu là chuyển khoản ngân hàng.
1. Nhập Số tiền đã thanh toán (Amount Paid).
1. Lưu và Xác nhận.


## 3. Các tính năng

### 3.1 Thiết lập Phương thức thanh toán

**Phương thức thanh toán (Mode of Payment)**: Việc nhập thông tin này giúp phân loại các Bút toán thanh toán dựa trên phương thức thanh toán được sử dụng. Các Phương thức thanh toán có thể là Ngân hàng, Tiền mặt, Chuyển khoản, v.v.

> **Mẹo**: Trong danh mục [Phương thức thanh toán](mode-of-payment.md), Tài khoản mặc định có thể được thiết lập. Tài khoản thanh toán mặc định này sẽ được lấy vào các Bút toán thanh toán.

### 3.2 Thanh toán Từ/Đến (Payment From/To)

![Payment Party](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-from-to.png)

* **Loại đối tác (Party Type)**: Có thể là Khách hàng, Nhà cung cấp, Nhân viên, Cổ đông, Học sinh, hoặc Thành viên NGO.
* **Đối tác (Party)**: Đối tác cụ thể mà Bút toán thanh toán được thực hiện.
* **Tên đối tác (Party Name)**: Tên của đối tác, thông tin này được lấy tự động.
* **Tài khoản ngân hàng Công ty (Company Bank Account)**: [Tài khoản ngân hàng](bank-account.md) của Công ty bạn.
* **Tài khoản ngân hàng Đối tác (Party Bank Account)**: [Tài khoản ngân hàng](bank-account.md) của Đối tác.
* **Liên hệ (Contact)**: Nếu Đối tác là một tổ chức, một người Liên hệ có thể được lưu trữ tại đây.

### 3.3 Tài khoản (Accounts)

![Payment Accounts](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-accounts.png)

* **Số dư đối tác (Party Balance)**: Tổng số tiền phải thu hoặc phải trả từ Khách hàng hoặc Nhà cung cấp từ các Hóa đơn được thiết lập trong Bút toán thanh toán hiện tại. Số tiền đã thanh toán sẽ là số dương và nếu có các khoản thanh toán trước, chúng sẽ là số âm.
* **Tài khoản chi thanh toán (Account Paid From)**: [Tài khoản](chart-of-accounts.md) mà số tiền sẽ bị trừ đi khi Thanh toán được Xác nhận.
* **Tài khoản nhận thanh toán (Account Paid To)**: [Tài khoản CoA](chart-of-accounts.md) mà số tiền sẽ được cộng vào khi Bút toán thanh toán được Xác nhận.

* **Tiền tệ tài khoản (Account Currency)**: Tiền tệ của các tài khoản này sẽ được lấy theo thiết lập trong [Tài khoản](chart-of-accounts.md) và không thể chỉnh sửa tại đây. Để biết thêm về các giao dịch bằng nhiều loại tiền tệ, hãy [truy cập trang này](articles/managing-transactions-in-multiple-currency.md).
* **Số dư tài khoản (Account Balance)**: Tổng số dư từ tất cả các hóa đơn của các tài khoản đã chọn.

**Số tiền đã thanh toán (Paid Amount)**: **Tổng số tiền** đã thanh toán cho Bút toán thanh toán hiện tại được hiển thị trong trường này.

> **Lưu ý**: Khi thực hiện các Bút toán thanh toán, tài khoản ngân hàng mặc định sẽ được lấy theo thứ tự sau nếu được thiết lập:

> * Mẫu Công ty
> * Tài khoản mặc định của Phương thức thanh toán
> * Tài khoản ngân hàng mặc định của Khách hàng/Nhà cung cấp
> * Chọn thủ công trong Bút toán thanh toán

### 3.4 Tham chiếu (Reference)

#### Lấy các Hóa đơn chưa thanh toán

Tính năng này có thể được sử dụng để thanh toán cho nhiều Hóa đơn bán hàng bằng một Bút toán thanh toán. Khi tạo một Bút toán thanh toán mới, khi nhấp vào nút **Get Outstanding Invoice** (Lấy hóa đơn chưa thanh toán), tất cả các Hóa đơn chưa thanh toán và Đơn hàng đang mở của đối tác sẽ được lấy ra. Bạn cần nhập 'Số tiền đã thanh toán' (Paid Amount) để thấy nút này. Từ đây, bạn có thể chọn một khoảng ngày và các hóa đơn cần lấy.