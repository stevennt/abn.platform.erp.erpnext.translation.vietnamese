<!-- add-breadcrumbs -->
# Khách hàng

**Khách hàng, đôi khi được gọi là khách hàng thân thiết, người mua hoặc người thanh toán, là người nhận hàng hóa, dịch vụ, sản phẩm hoặc ý tưởng từ người bán để đổi lấy một khoản tiền.**

Mỗi khách hàng cần được gán một ID duy nhất. Bản thân tên Khách hàng có thể là ID hoặc bạn có thể thiết lập một chuỗi đặt tên để các ID được tạo tự động trong [Cài đặt bán hàng](../selling/selling-settings.md).

Để truy cập danh sách Khách hàng, hãy đi đến:
> Home > CRM > Sales Pipeline

Hoặc

> Home > Selling > Customers

## 1. Cách tạo Khách hàng

1. Đi đến danh sách Khách hàng và nhấn vào Mới.
1. Nhập Họ tên đầy đủ của khách hàng.
1. Chọn Cá nhân nếu khách hàng là một cá nhân hoặc Công ty nếu khách hàng đại diện cho một công ty trong trường Loại.
1. Chọn [Nhóm khách hàng](customer-group.md). Các nhóm Cá nhân, Thương mại, Phi lợi nhuận và Chính phủ có sẵn theo mặc định. Bạn có thể tạo thêm các nhóm khác nếu cần.
1. Chọn Khu vực.
1. Nếu khách hàng được tạo từ một khách hàng tiềm năng, bạn có thể chọn khách hàng tiềm năng đó trong trường Từ khách hàng tiềm năng.
1. Lưu.

    ![Creating New Customer](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/create-customer.gif)

Bạn có thể không cho phép tạo đơn bán hàng và hóa đơn bán hàng đối với một khách hàng bằng cách nhấn vào 'Disabled'.

> Mẹo nâng cao: Nếu khách hàng đại diện cho một trong các công ty của chính bạn, hãy tích vào 'Is Internal Customer'. Xem thêm chi tiết tại [Hóa đơn liên công ty](../accounts/inter-company-invoices.md).

Bạn cũng có thể tải lên thông tin chi tiết của khách hàng thông qua [Công cụ nhập dữ liệu](../setting-up/data/data-import.md).

## 2. Các tính năng
Luồng giao dịch chung cho một khách hàng như sau:

![Sales Flowchart](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/customer-to selling-flowchart.jpeg)

> Lưu ý: Khách hàng tách biệt với Liên hệ và Địa chỉ. Một Khách hàng có thể có nhiều Liên hệ và Địa chỉ.

### 2.1 Nhiều Liên hệ và Địa chỉ

[Liên hệ](contact.md) và [Địa chỉ](address.md) được lưu trữ riêng biệt để bạn có thể đính kèm nhiều Liên hệ hoặc Địa chỉ cho khách hàng.

### 2.2 Cho phép tạo Hóa đơn bán hàng mà không cần Đơn bán hàng và Phiếu giao hàng

Nếu tùy chọn "Yêu cầu Phiếu giao hàng" hoặc "Yêu cầu Đơn bán hàng" được cấu hình là "Có" trong [Cài đặt bán hàng](../selling/selling-settings.md), tùy chọn này có thể được ghi đè cho một khách hàng cụ thể bằng cách bật "Cho phép tạo Hóa đơn bán hàng không cần Đơn bán hàng" hoặc "Cho phép tạo Hóa đơn mua hàng không cần Phiếu giao hàng" trong Hồ sơ khách hàng.

![Sales Order Mandatory Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/customer-so-dn-required.png)

### 2.3 Thiết lập Danh mục khấu trừ thuế

Bạn có thể thiết lập Danh mục khấu trừ thuế để thiết lập TCS đối với các khách hàng đủ điều kiện. Để biết thêm thông tin, hãy truy cập trang [Danh mục khấu trừ thuế](../accounts/tax-withholding-category.md).

### 2.4 Tiền tệ mặc định và Bảng giá
ERPNext hỗ trợ [Đa tiền tệ](../accounts/multi-currency-accounting.md) và [Bảng giá](../stock/price-lists.md).

Bạn có thể thiết lập tiền tệ mặc định được sử dụng cho khách hàng này trong các đơn bán hàng và hóa đơn bán hàng bằng cách chọn tiền tệ phù hợp trong Tiền tệ thanh toán.

Tương tự, bạn có thể thiết lập bảng giá mặc định được sử dụng cho khách hàng này trong các đơn bán hàng và hóa đơn bán hàng bằng cách chọn bảng giá phù hợp trong Bảng giá mặc định.

### 2.5 Tích hợp với Kế toán

Không giống như nhiều phần mềm kế toán khác, bạn không cần phải tạo một sổ cái kế toán riêng biệt cho mỗi khách hàng.
Theo mặc định, một sổ cái thống nhất có tên là **Phải thu khách hàng** sẽ được tạo.

Tuy nhiên, nếu bạn đặc biệt cần một sổ cái riêng cho một khách hàng, trước tiên hãy tạo sổ cái đó trong mục Phải thu khách hàng thuộc [Hệ thống tài khoản](../accounts/chart-of-accounts.html.md) và sau đó thêm nó vào phần KẾ TOÁN của khách hàng.

> Mẹo nâng cao: ERPNext hỗ trợ [Kế toán đa công ty](../accounts/inter-company-journal-entry.md). Bạn có thể sử dụng cùng một hồ sơ khách hàng trong nhiều công ty. Vì sổ cái kế toán phụ thuộc vào từng công ty, bạn cần chọn công ty và sổ cái tương ứng trong phần KẾ TOÁN nếu bạn quyết định có sổ cái kế toán riêng cho một khách hàng.

### 2.6 Hạn mức tín dụng và Điều khoản thanh toán

Bạn có thể thiết lập hạn mức tín dụng bằng cách nhập số tiền vào trường 'Hạn mức tín dụng'. Đọc thêm về [Hạn mức tín dụng](../accounts/credit-limit.md) để biết thêm chi tiết.

Bạn có thể chọn [Điều khoản thanh toán](../accounts/payment-terms.md) mặc định được áp dụng trong các đơn bán hàng và hóa đơn bán hàng trong trường 'Mẫu điều khoản thanh toán mặc định'.

### 2.7 Đội ngũ bán hàng và Đối tác bán hàng

Nếu bạn có một hoặc nhiều [Nhân viên bán hàng](sales-person.md) để quản lý việc bán hàng cho khách hàng, bạn có thể thêm họ vào phần ĐỘI NGŨ BÁN HÀNG. Nếu có nhiều nhân viên bán hàng tham gia, bạn có thể chia tỷ lệ đóng góp giữa họ. Hãy đảm bảo rằng tổng đóng góp của tất cả nhân viên bán hàng bằng 100%.

Kiểm tra [Nhân viên bán hàng trong giao dịch bán hàng](../selling/articles/sales-persons-in-the-sales-transactions.md) để biết thêm chi tiết.

[Đối tác bán hàng](../selling/sales-partner.md) là bên thứ ba là nhà phân phối / đại lý / đại lý hoa hồng / liên kết / đại lý bán lẻ, người hỗ trợ việc bán sản phẩm/dịch vụ của bạn để nhận hoa hồng.
Nếu bạn bán sản phẩm/dịch vụ của mình cho khách hàng thông qua một đối tác bán hàng, bạn có thể thiết lập trong trường 'Đối tác bán hàng' và ghi rõ 'Tỷ lệ hoa hồng' để tính toán hoa hồng.

### 2.8 Chương trình khách hàng thân thiết

Nếu bạn muốn cung cấp [Chương trình khách hàng thân thiết](../accounts/loyalty-program.md) cho khách hàng, hãy chọn tùy chọn đó trong trường Chương trình khách hàng thân thiết.

### 2.9 Xem Sổ cái kế toán và Phải thu khách hàng

Nhấp vào nút Sổ cái kế toán để xem tất cả các giao dịch kế toán với khách hàng.

Nhấp vào nút Phải thu khách hàng để xem chi tiết về tất cả các hóa đơn chưa thanh toán.

### 2.10 Thiết lập ID Khách hàng, Nhóm khách hàng mặc định, Khu vực, và