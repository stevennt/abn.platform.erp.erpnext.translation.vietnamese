<!-- add-breadcrumbs -->
# Đánh giá lại tỷ giá hối đoái

Trong ERPNext, bạn có thể thực hiện các bút toán kế toán bằng nhiều loại tiền tệ khác nhau. Ví dụ, nếu bạn có một tài khoản ngân hàng bằng ngoại tệ, bạn có thể thực hiện các giao dịch bằng loại tiền tệ đó và hệ thống sẽ hiển thị số dư ngân hàng bằng loại tiền tệ cụ thể đó.

Mục đích của danh mục Đánh giá lại tỷ giá hối đoái là để điều chỉnh số dư trong các tài khoản Sổ cái theo bất kỳ thay đổi nào về tỷ giá hối đoái. Điều này hữu ích khi bạn đang chốt sổ kế toán và muốn cập nhật các tài khoản Sổ cái của Công ty bằng cách quy đổi tiền từ các tài khoản ngoại tệ khác.

Để truy cập danh sách Đánh giá lại tỷ giá hối đoái, hãy đi đến:
> Home > Accounting > Multi Currency > Exchange Rate Revaluation

## 1. Cách thiết lập tiền tệ trong một tài khoản

1. Để bắt đầu với kế toán đa tiền tệ, bạn cần chỉ định tiền tệ kế toán trong bản ghi Tài khoản.
1. Bạn có thể xác định Tiền tệ từ Hệ thống tài khoản khi tạo một tài khoản.

 ![Currency in Ledger](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/currency-in-ledger.png)

1. Bạn cũng có thể chỉ định/sửa đổi tiền tệ cho các tài khoản hiện có bằng cách mở bản ghi Tài khoản cụ thể.
1. Nhấp vào Tài khoản và Nhấp vào Edit.

 ![Set Account Currency](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/update-currency-in-ledger.png)

## 2. Cách kích hoạt Đánh giá lại tỷ giá hối đoái

Tính năng Đánh giá lại tỷ giá hối đoái dùng để xử lý tình huống khi bạn có các tài khoản với các loại tiền tệ khác nhau trong cùng một Hệ thống tài khoản của Công ty.

1. Đi đến: **Setup > Company > *chọn công ty***.
1. Thiết lập trường 'Unrealized Exchange Gain/Loss Account' trong DocType Công ty. Tài khoản này dùng để cân bằng sự chênh lệch giữa tổng bên Có và tổng bên Nợ.

 ![Unrealized Exchange Gain/Loss Ledger in Company](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/unrealized-exchange-gain-loss-ledger-in-company.png)

1. Đi đến **Accounting > Setup > Exchange Rate Revaluation > New**.
1. Chọn Công ty.
1. Nhấp vào nút 'Get Entries'. Hệ thống sẽ lấy các tài khoản có tiền tệ khác với 'Default Currency' được thiết lập trong Công ty.
1. Thao tác này sẽ tự động lấy tỷ giá hối đoái mới nếu chưa được thiết lập trong DocType Currency Exchange cho loại tiền tệ đó, nếu không nó sẽ lấy 'Exchange Rate' được thiết lập trong DocType [Currency Exchange](currency-exchange.md).
 <img class="screenshot" alt="Exchange Rate Revaluation"   src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/exchange-rate-revaluation.png">


1. Sau khi Xác nhận, nút **Create Journal Entry** sẽ xuất hiện.
![Journal Entry Option After Submission](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/exchange-rate-revaluation-submit.png)


1. Nhấp vào nút này sẽ tạo một Bút toán cho việc Đánh giá lại tỷ giá hối đoái.
![Exchange Rate Revaluation Journal Entry](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/exchange-rate-revaluation-journal-entry.png)


1. Sau khi Xác nhận Bút toán, sổ cái sẽ bị ảnh hưởng như sau:
![Exchange Rate Revaluation GL](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/exchange-rate-revaluation-gl.png)


### 3. Các chủ đề liên quan
1. [Inter Company Journal Entry](inter-company-journal-entry.md)
1. [Inter Company Invoices](inter-company-invoices.md)

{next}