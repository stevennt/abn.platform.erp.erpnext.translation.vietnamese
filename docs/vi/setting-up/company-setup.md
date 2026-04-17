<!-- add-breadcrumbs -->
# Thiết lập Công ty

**Công ty là một thực thể pháp lý được tạo thành bởi một nhóm người để thực hiện một doanh nghiệp thương mại hoặc công nghiệp.**

Trong ERPNext, Công ty đầu tiên được tạo khi tài khoản ERPNext được thiết lập. Đối với mỗi Công ty, bạn có thể thiết lập một lĩnh vực hoạt động như sản xuất, bán lẻ hoặc dịch vụ tùy thuộc vào tính chất hoạt động kinh doanh của bạn.

Nếu bạn có nhiều hơn một công ty, bạn có thể thêm chúng từ:

> Home > Accounting > Company

## 1. Cách tạo Công ty mới
1. Đi đến danh sách Công ty, nhấp vào New.
1. Nhập tên, chữ viết tắt và tiền tệ mặc định cho công ty.
1. Lưu.

Chữ viết tắt cho công ty của bạn được tạo theo mặc định. Ví dụ: FT cho Frappe Technologies. Chữ viết tắt giúp phân biệt tài sản của công ty này với công ty khác.

Chữ viết tắt cũng xuất hiện trong các tài khoản, trung tâm chi phí, mẫu thuế, kho, v.v., của công ty bạn.

Bạn cũng có thể đính kèm logo công ty và thêm mô tả cho công ty.

![Company Master](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/company-master.png)

### 1.1 Cấu trúc Đa Công ty

Giả sử bạn điều hành một tập đoàn gồm nhiều công ty, một số có thể là công ty lớn và một số có thể là công ty nhỏ hơn là một phần của (các) công ty lớn hơn.

Trong ERPNext, bạn có thể thiết lập nhiều công ty. Cấu trúc công ty có thể song song, tức là các công ty chị em, công ty mẹ-con, hoặc kết hợp cả hai.

Công ty mẹ là một tổ chức lớn hơn bao gồm một hoặc nhiều công ty con. Công ty con là công ty con của một công ty mẹ.

Chế độ xem cây công ty hiển thị cấu trúc tổng thể của các công ty của bạn.

<img class="screenshot" alt="Company Tree" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/company-tree.png">

Khi bạn xây dựng cây công ty, ERPNext sẽ xác nhận xem các tài khoản của các công ty con có khớp với các tài khoản trong công ty mẹ hay không. Tất cả các tài khoản có thể được kết hợp trong một báo cáo hệ thống tài khoản hợp nhất.

### 1.2 Các tùy chọn khác khi Tạo Công ty

* **Domain**: Lĩnh vực hoạt động mà công ty tham gia. Ví dụ: sản xuất, dịch vụ, v.v. Chọn một tùy chọn khi thiết lập tài khoản của bạn.
* **Is Group**: Nếu được chọn, đây sẽ trở thành công ty mẹ.
* **Parent Company**: Nếu đây là một công ty con, hãy thiết lập công ty mẹ từ trường này, tức là chọn công ty tập đoàn mà công ty này thuộc về. Nếu một công ty mẹ được thiết lập, hệ thống tài khoản cho công ty mới bạn đang tạo sẽ được tạo dựa trên công ty mẹ đã chọn.

### 1.3 Hệ thống tài khoản
Đối với mỗi Công ty, master cho Hệ thống tài khoản được duy trì riêng biệt. Điều này cho phép bạn duy trì kế toán riêng biệt cho từng công ty theo các yêu cầu pháp lý. Bạn cũng có thể nhập hệ thống tài khoản bằng cách sử dụng [Charts Of Accounts Importer](/docs/v13/user/manual/en/setting-up/chart-of-accounts-importer).

ERPNext có sẵn Hệ thống tài khoản được bản địa hóa cho một số quốc gia. Khi tạo một Công ty mới, bạn có thể chọn thiết lập Hệ thống tài khoản cho nó từ một trong các tùy chọn sau.

* Standard Chart of Accounts (Hệ thống tài khoản chuẩn)
* Based on Existing Company's Chart of Account (Dựa trên Hệ thống tài khoản của Công ty hiện có)

<img class="screenshot" alt="Company Chart of Accounts" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/new-company-coa-based-on.png">

Lưu ý rằng, nếu Công ty mẹ được chọn khi tạo một Công ty mới, Hệ thống tài khoản sẽ được tạo dựa trên Công ty mẹ hiện có.

### 1.4 Các giá trị mặc định
Trong master Công ty, bạn có thể thiết lập nhiều giá trị mặc định cho các master và tài khoản. Các tài khoản mặc định này sẽ giúp bạn hạch toán nhanh các giao dịch kế toán, nơi giá trị của tài khoản sẽ được lấy từ master Công ty nếu được cung cấp. Ngay khi công ty được tạo, Hệ thống tài khoản và Trung tâm chi phí mặc định sẽ tự động được tạo.

Các giá trị mặc định sau đây có thể được thiết lập cho một công ty:

* Default Finance Book (Sổ tài chính mặc định)
* Default Letter Head (Tiêu đề thư mặc định)
* Default Holiday List (Danh sách ngày nghỉ mặc định)
* Standard Working Hours (Giờ làm việc tiêu chuẩn)
* Default Terms and Conditions (Điều khoản và Điều kiện mặc định)
* Country (Quốc gia)
* Tax ID (Mã số thuế)
* Date of Establishment (Ngày thành lập)

## 2. Các tính năng
### 2.1 Mục tiêu doanh số hàng tháng
Thiết lập con số mục tiêu doanh số hàng tháng bằng tiền tệ của công ty, ví dụ: $10,000. Tổng doanh số hàng tháng sẽ hiển thị sau khi các giao dịch được thực hiện. Để biết thêm [nhấp vào đây](/docs/v13/user/manual/en/setting-up/setting-company-sales-goal).

### 2.2 Cài đặt Tài khoản
Một số tài khoản sau đây sẽ được thiết lập mặc định khi bạn tạo một công ty mới, những tài khoản khác có thể được tạo thêm. Các tài khoản có thể được xem trong [Hệ thống tài khoản](/docs/v13/user/manual/en/accounts/chart-of-accounts). Các giá trị này có thể được thay đổi sau nếu cần.

* Default Bank Account (Tài khoản ngân hàng mặc định)
* Default Cash Account (Tài khoản tiền mặt mặc định)
* Default Receivable Account (Tài khoản phải thu mặc định)
* Round Off Account (Tài khoản chênh lệch làm tròn)
* Round Off Cost Center (Trung tâm chi phí làm tròn)
* Write Off Account (Tài khoản xóa nợ)
* Discount Allowed Account (Tài khoản chiết khấu cho phép)
* Discount Received Account (Tài khoản chiết khấu được hưởng)
* Exchange Gain / Loss Account (Tài khoản lãi/lỗ tỷ giá)
* Unrealized Exchange Gain/Loss Account (Tài khoản lãi/lỗ tỷ giá chưa thực hiện)
* Default Payable Account (Tài khoản phải trả mặc định)
* Default Employee Advance Account (Tài khoản tạm ứng nhân viên mặc định)
* Default Cost of Goods Sold Account (Tài khoản giá vốn hàng bán mặc định)
* Default Income Account (Tài khoản thu nhập mặc định)
* Default Deferred Revenue Account (Tài khoản doanh thu chưa thực hiện mặc định)
* Default Deferred Expense Account (Tài khoản chi phí trả trước mặc định)
* Default Payroll Payable Account (Tài khoản phải trả lương mặc định)
* Default Expense Claim Payable Account (Tài khoản phải trả yêu cầu chi phí mặc định)
* Default Cost Center (Trung tâm chi phí mặc định)
* Credit Limit (Hạn mức tín dụng)
* Default Payment Terms Template (Mẫu điều khoản thanh toán mặc định)

### 2.3 Cài đặt Kho
Tính năng Kiểm kê thường xuyên sẽ dẫn đến các giao dịch Kho tác động đến sổ sách kế toán của công ty. Tìm hiểu thêm [tại đây](/docs/v13/user/manual/en/stock/perpetual-inventory). Tính năng này được bật theo mặc định.

* Default Inventory Account (Tài khoản tồn kho mặc định)
* Stock Adjustment Account (Tài khoản điều chỉnh kho)
* Stock Received But Not Billed (Hàng đã nhận nhưng chưa lập hóa đơn)
* Expenses Included In Valuation (Chi phí bao gồm trong giá trị tính giá)

    ![Stock Settings in Company](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/company-stock-settings.png)

### 2.4 Cài đặt Khấu hao Tài sản cố định
Để quản lý tài sản cố định trong một công ty, cần có các tài khoản sau. Hầu hết chúng sẽ được tạo mặc định. Chúng có thể được xem trong [Hệ thống tài khoản](/docs/v13/user/manual/en/accounts/chart-of-accounts).

* Accumulated Depreciation Account (Tài khoản khấu hao lũy kế)
* Depreciation Expense Account (Tài khoản chi phí khấu hao)
* Series for Asset Depreciation Entry (Journal Entry) (Chuỗi cho Bút toán khấu hao tài sản (Bút toán))
* Expenses Included In Asset Valuation (Chi phí bao gồm trong giá trị tài sản)
* Gain/Loss Account on Asset (Tài khoản lãi/lỗ tài sản)