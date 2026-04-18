<!--add breadcrumbs-->

# Công cụ nhập Hệ thống tài khoản

> Được giới thiệu trong Phiên bản 12

Khi một công ty mới được tạo trong ERPNext, Hệ thống tài khoản cho công ty đó sẽ được tạo mặc định với một cấu trúc có sẵn. Tuy nhiên, nếu bạn đã có Hệ thống tài khoản riêng, bạn có thể nhập nó bằng cách sử dụng Công cụ nhập Hệ thống tài khoản.

Công cụ này cho phép bạn tạo Hệ thống tài khoản của riêng mình theo yêu cầu và nhập vào hệ thống.

Bất kỳ Hệ thống tài khoản hiện có nào của công ty đó sẽ bị ghi đè. Hãy đảm bảo rằng công ty bạn đang chọn không có bất kỳ giao dịch nào đã tồn tại, nếu không bạn sẽ nhận được lỗi xác thực.

Để truy cập, hãy đi tới:
> Home > Getting Started > Chart of Accounts Importer

## 1. Cách nhập Hệ thống tài khoản

1. Chọn Công ty mà bạn muốn nhập Hệ thống tài khoản.

1. Nhấp vào nút "Download Template" để tải mẫu xuống. Chọn loại tệp mà bạn muốn tải mẫu. Chọn loại mẫu và nhấp vào "Download". "Sample Template" chứa dữ liệu mẫu đã được điền sẵn để bạn có ý tưởng về cách điền mẫu. Bạn có thể chỉnh sửa dữ liệu ngay trong "Sample Template" hoặc tải "Blank Template" để có một mẫu trống mới.

    <img class="screenshot" alt="COA Import" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/coa-template-download.png">

    <img class="screenshot" alt="COA Import" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/coa-blank-template.png">

1. Sau khi bạn tải mẫu xuống, hãy điền các chi tiết vào mẫu như được hiển thị trong mẫu mẫu dưới đây. Vui lòng đảm bảo tạo các tài khoản cho các loại tài khoản là "Cost of Goods Sold", "Depreciation", "Fixed Asset", "Payable", "Receivable", "Stock Adjustment". Các loại gốc (Root types) cho các tài khoản này phải là một trong các loại: Asset, Liability, Income, Expense, và Equity.

    Để biết thêm về "Account Types" và "Root Types", <a href="accounts/chart-of-accounts">nhấp vào đây</a>

    <img class="screenshot" alt="COA Import" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/coa-sample-template.png">

1. Nhấp vào "Attach" để tải mẫu lên.

    <img class="screenshot" alt="COA Import" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/coa-attach.png">

1. Sau khi bạn tải mẫu lên, bạn sẽ có thể xem trước Hệ thống tài khoản trong phần Chart Preview.

    <img class="screenshot" alt="COA Import" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/coa-preview.png">

1. Nếu mọi thứ trong bản xem trước có vẻ chính xác, hãy nhấp vào "Import" ở góc trên bên phải và các tài khoản sẽ được tạo.

    <img class="screenshot" alt="COA Import" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/coa-start-import.png">

1. Để xác minh các tài khoản đã tạo, bạn có thể đi tới Hệ thống tài khoản và xem các tài khoản mới được tạo cho công ty đó.

    <img class="screenshot" alt="COA Import" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/coa-import.png">

### 2. Các chủ đề liên quan
1. [Chart Of Accounts](../accounts/chart-of-accounts.md)