<!-- add-breadcrumbs -->
# Tích hợp Plaid

ERPNext cung cấp khả năng đồng bộ hóa các tài khoản ngân hàng của bạn thông qua một dịch vụ có tên là [Plaid](https://plaid.com/). Vui lòng kiểm tra [câu hỏi thường gặp của Plaid](https://plaid.com/docs/v13/faq/#does-plaid-support-international-bank-accounts-) để xem quốc gia của bạn có được hỗ trợ hay không.

Nếu phiên bản của bạn đã được kết nối với Plaid, bạn có thể đồng bộ hóa các giao dịch tài khoản ngân hàng mà không cần phải nhập tệp CSV hoặc XLSX một cách thủ công.


## Cài đặt

Để cấp quyền truy cập cho ERPNext vào Plaid, bạn cần thêm ba tham số sau vào tệp `site_config.json` của mình.

- `plaid_env`
- `plaid_public_key`
- `plaid_secret`

## Kích hoạt

Để kích hoạt Plaid trên một phiên bản, hãy nhấp vào nút "Enable" trong DocType Plaid Settings.

<img class="screenshot" alt="Enable Plaid" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/plaid_enable.gif">

Sau khi được kích hoạt, bạn có thể tạo một tài khoản mới trực tiếp từ Trang tổng quan Đối chiếu ngân hàng.


## Tạo tài khoản ngân hàng

Để liên kết một trong các tài khoản ngân hàng hiện có của bạn với ERPNext, hãy nhấp vào "Link a new bank account" và làm theo các bước do Plaid đề xuất.

<img class="screenshot" alt="Link your bank account" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/new_account_creation.gif">


## Đồng bộ hóa ngân hàng

Để đồng bộ hóa một tài khoản ngân hàng với ERPNext, hãy chọn một tài khoản và nhấp vào nút "Action" để chọn "Synchronize this account".

<img class="screenshot" alt="Synchronize your bank account" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/plaid_synchronization.gif">

Việc đồng bộ hóa dựa trên "Last integration date" có sẵn trong DocType "Bank Account".

Nếu vì bất kỳ lý do gì, bạn muốn thực hiện lại việc đồng bộ hóa, bạn có thể thay đổi ngày này và đồng bộ hóa lại tài khoản.
Vì tất cả các giao dịch ngân hàng đều được gắn với một ID giao dịch cụ thể, việc đồng bộ hóa sẽ chỉ mang tính chất cộng dồn (incremental).


## Đồng bộ hóa tự động

Bạn có thể cho phép Plaid đồng bộ hóa tài khoản ngân hàng của mình với ERPNext mỗi giờ bằng cách chọn "Synchronize all accounts every hour" trong Plaid Settings.