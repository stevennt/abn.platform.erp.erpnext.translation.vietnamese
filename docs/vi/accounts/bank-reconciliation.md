<!-- add-breadcrumbs -->
# Đối chiếu ngân hàng

**Một bản ghi Đối chiếu ngân hàng được sử dụng để khớp các sao kê tài khoản của ERPNext với sao kê tài khoản ngân hàng của bạn.**

Nếu bạn đang nhận thanh toán hoặc thực hiện thanh toán qua séc, các bản sao kê ngân hàng sẽ không khớp chính xác với ngày ghi sổ của bạn, điều này là do ngân hàng thường mất thời gian để "thanh toán" (clear) các khoản thanh toán này.

Ngoài ra, bạn có thể đã gửi séc cho Nhà cung cấp và có thể mất vài ngày trước khi Nhà cung cấp nhận được và nộp séc đó. Trong ERPNext, bạn có thể đồng bộ hóa sao kê ngân hàng và các Bút toán của mình bằng cách sử dụng ngày giao dịch.

## 1. Báo cáo Đối chiếu ngân hàng là gì?
Báo cáo Đối chiếu ngân hàng cung cấp sự chênh lệch giữa số dư ngân hàng hiển thị trong sao kê ngân hàng của một tổ chức, được cung cấp bởi ngân hàng, so với số tiền hiển thị trong Hệ thống tài khoản của công ty.

Đây là giao diện của một bản Đối chiếu ngân hàng:

<img class="screenshot" alt="Bank Reconciliation statement" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/bank-reconciliation-2.png">

Trong báo cáo, hãy kiểm tra xem trường 'Balance as per bank' có khớp với Sao kê tài khoản ngân hàng hay không. Nếu khớp, điều đó có nghĩa là Ngày thanh toán (Clearance Date) đã được cập nhật chính xác cho tất cả các bút toán ngân hàng. Nếu có sự sai lệch, đó là do các bút toán ngân hàng chưa được cập nhật Ngày thanh toán.

Để truy cập Đối chiếu ngân hàng, hãy đi tới:
> Home > Accounting > Banking and Payments > Update Bank Transaction Date

## 2. Cách cập nhật Ngày giao dịch ngân hàng

1. Đi tới Update Bank Transaction Dates.
1. Chọn Tài khoản ngân hàng của bạn.
1. Chọn ngày từ và đến.
1. Bạn có thể chọn bao gồm các bút toán đã đối chiếu và các giao dịch POS.
1. Nhấp vào nút **Get Payment Entries**.
1. Bây giờ bạn sẽ nhận được tất cả các bút toán loại “Bank Voucher”.
1. Trong mỗi bút toán, ở cột ngoài cùng bên phải, hãy cập nhật trường “Clearance Date” và nhấp vào nút **Update Clearance Date**.

Bằng cách này, bạn sẽ có thể đồng bộ hóa sao kê ngân hàng và các bút toán vào hệ thống.

<img class="screenshot" alt="Bank Reconciliation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/bank-reconciliation.png">

## 3. Các loại công cụ đối chiếu

ERPNext có hai công cụ đối chiếu:

1. Một công cụ đối chiếu thủ công cho phép thiết lập ngày thanh toán đối với các bút toán thanh toán, thanh toán hóa đơn bán hàng hoặc bút toán.
2. Một công cụ đối chiếu bán tự động cho phép thanh toán các giao dịch ngân hàng đối với các bút toán thanh toán, hóa đơn bán hàng, hóa đơn mua hàng, bút toán hoặc yêu cầu thanh toán chi phí.

### 3.1 Công cụ Đối chiếu ngân hàng thủ công

Để xem báo cáo này, hãy đi tới **Accounts > Banking and Payments > Bank Reconciliation Statement**. Trong báo cáo, hãy kiểm tra xem trường 'Balance as per bank' có khớp với Sao kê tài khoản ngân hàng hay không. Nếu khớp, điều đó có nghĩa là Ngày thanh toán đã được cập nhật chính xác cho tất cả các bút toán ngân hàng. Nếu có sự sai lệch, đó là do Ngày thanh toán chưa được cập nhật cho các bút toán ngân hàng.


### 3.2 Công cụ Đối chiếu ngân hàng bán tự động

Đây là một quy trình gồm hai bước:
1. Thêm các Giao dịch ngân hàng vào ERPNext thông qua Nhập sao kê ngân hàng hoặc Đồng bộ hóa tài khoản ngân hàng.
1. Đối chiếu Sao kê ngân hàng.

#### 3.2.1 Nhập sao kê ngân hàng


1. Tải xuống bản sao kê ngân hàng từ trang web của ngân hàng bạn.

 <img class="screenshot" alt="Reconcile bank transactions" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/sample_bank_statement.png">
 Đảm bảo rằng bạn có ít nhất ngày, nợ/có (debit/credit) và tiền tệ trên mỗi dòng của sao kê ngân hàng.

Để tải lên Sao kê ngân hàng của bạn, hãy đi tới:
> Accounting > Bank Statement > Bank Statement Import

hoặc chỉ cần tìm kiếm 'Bank Statement Import' trong thanh tìm kiếm (awesomebar).

1. Chọn Công ty và Tài khoản ngân hàng của bạn.
1. Nhấp Lưu.
1. Đính kèm Sao kê ngân hàng.
1. Nhấp vào 'Map Columns' để nhập sơ đồ ánh xạ giữa các cột trong Sao kê ngân hàng đã tải lên và DocType Giao dịch ngân hàng (Bank Transaction).
1. Nhấp vào Start Import để bắt đầu quá trình nhập. Các Giao dịch ngân hàng sẽ được tạo thông qua một tác vụ chạy ngầm, mặc dù tiến trình sẽ được hiển thị tại đây.

 <img class="screenshot" alt="Reconcile bank transactions" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/bank_transaction_upload.gif">

1. Sơ đồ ánh xạ được thực hiện sẽ được lưu trong tài liệu Ngân hàng (Bank) được liên kết với Tài khoản ngân hàng tương ứng. Trong lần tải lên tiếp theo, sơ đồ ánh xạ sẽ được lấy từ đây nhưng hệ thống cho phép người dùng thay đổi nếu cần. Sơ đồ ánh xạ đã thay đổi cũng sẽ được cập nhật trong tài liệu Ngân hàng.
 <img class="screenshot" alt="Reconcile bank transactions" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/bank_configuration.png">


#### 3.2.2 Đồng bộ hóa tài khoản ngân hàng

Bạn có thể sử dụng Plaid (xem [trang Tích hợp Plaid](../erpnext_integration/plaid_integration.md)) để tự động đồng bộ hóa tài khoản ngân hàng của bạn với ERPNext. Tất cả các giao dịch ngân hàng của bạn sẽ được tự động nhập vào ERPNext.

#### 3.2.3 Đối chiếu Sao kê ngân hàng

Sau khi tất cả các giao dịch ngân hàng của bạn đã được nhập vào ERPNext, bạn có thể đối chiếu chúng với các chứng từ hiện có. Đi tới:
> Accounting > Bank Statement > Bank Reconciliation Tool

hoặc chỉ cần tìm kiếm 'Bank Reconciliation Tool' trong thanh tìm kiếm (awesomebar).

1. Chọn Công ty, Tài khoản ngân hàng, Ngày bắt đầu và Ngày kết thúc của Sao kê ngân hàng.
1. Đảm bảo rằng số dư đầu kỳ từ ERPNext khớp với số dư đầu kỳ của Sao kê ngân hàng của bạn.
1. Nhập Số dư cuối kỳ của Sao kê ngân hàng.
1. Việc Lưu tài liệu sẽ hiển thị các giao dịch ngân hàng khớp.
 <img class="screenshot" alt="Reconcile bank transactions" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/bank_reconciliation_tool.png">

1. Mục tiêu cuối cùng của Đối chiếu ngân hàng là làm cho số tiền chênh lệch bằng không (màu xanh lá cây) bằng cách khớp với một chứng từ hiện có hoặc tạo một chứng từ mới.
1. Đối với tất cả các giao dịch ngân hàng có trong Sao kê ngân hàng nhưng chưa có ngày thanh toán, hãy nhấp vào nút Actions để Khớp/Tạo chứng từ (Match/ Create Vouchers).
1. Để khớp, chọn 'Match Against Voucher' trong mục 'Action'. Các chứng từ liên quan đến giao dịch này sẽ được hiển thị.