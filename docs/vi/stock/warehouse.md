<!-- add-breadcrumbs -->
# Kho

**Kho là một tòa nhà thương mại dùng để lưu trữ hàng hóa. Kho được sử dụng bởi các nhà sản xuất, nhà nhập khẩu, nhà xuất khẩu, nhà bán buôn, doanh nghiệp vận tải, hải quan, v.v.**

Chúng thường là những tòa nhà lớn nằm trong các khu công nghiệp của thành phố, thị trấn và làng mạc. Chúng chủ yếu có các bến bãi để bốc dỡ hàng hóa từ xe tải.

Tuy nhiên, thuật ngữ 'Kho' trong ERPNext rộng hơn một chút và có thể được coi là "các vị trí lưu trữ". Bạn có thể tạo một Kho phụ, ví dụ như một kệ hàng bên trong vị trí thực tế của bạn.

Điều này có thể trở thành một cấu trúc Cây khá chi tiết như sau:

*Kho > Phòng > Dãy > Kệ > Ô hàng*

Để truy cập danh sách Kho, hãy đi tới:
> Home > Stock > Settings > Warehouse

## 1. Cách tạo Kho
1. Đi tới danh sách Kho, nhấn vào New.
1. Nhập tên cho Kho.
1. Thiết lập/kiểm tra Kho cha (Parent Warehouse). Nếu bạn tích vào 'Is Group', bạn có thể tạo các Kho phụ dưới Kho nhóm này.
1. Lưu.

Các Kho được lưu với tên viết tắt của Công ty tương ứng. Điều này giúp dễ dàng nhận diện Kho nào thuộc về công ty nào ngay khi nhìn qua.

### 1.1 Các tùy chọn bổ sung khi tạo Kho
**Account**: Thiết lập một tài khoản mặc định tại đây cho tất cả các giao dịch với Kho này. Việc thiết lập tài khoản này sẽ hiển thị các giao dịch từ Kho này trong Sổ cái kế toán.
**Warehouse Type**: Bạn có thể tạo Loại Kho để phân loại các Kho. Ví dụ, có thể gắn thẻ Kho của Nhà cung cấp, Kho tồn kho, Kho bán thành phẩm (WIP), Phòng, v.v. Việc phân loại này hữu ích khi lập báo cáo hoặc trong một số giao dịch kho nhất định.

#### Địa chỉ và liên hệ
Bạn có thể thêm địa chỉ Thanh toán, địa chỉ Giao hàng và các loại địa chỉ khác cho Kho. Bạn cũng có thể thêm một liên hệ, ví dụ như Quản lý Kho.

![Warehouse](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/warehouse.png)

### 1.2 Sau khi Lưu
Sau khi lưu một Kho, bạn sẽ thấy các tùy chọn sau:

* **Stock Balance**: Tùy chọn này sẽ mở báo cáo Số lượng tồn kho để hiển thị số lượng, giá trị, số dư, v.v.
* **General Ledger**: Tùy chọn này sẽ mở Sổ cái để hiển thị các giao dịch kế toán.
* **Non-Group to Group**: Nếu Kho là Kho không phải nhóm (Non-Group Warehouse), tức là không thể chứa các Kho khác bên dưới, nút này sẽ chuyển nó thành Kho nhóm (Group Warehouse).

## 2. Các tính năng

### 2.1 Chế độ xem Cây (Tree View)
Bạn cũng có thể chuyển sang chế độ xem 'Tree' để hiển thị tất cả các Kho nhóm và Kho con.

<img class="screenshot" alt="Warehouse" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/warehouse-tree.png">

### 2.2 Tài khoản Kho
Trong ERPNext, nếu bạn bật [Perpetual Inventory](perpetual-inventory.md), mọi Kho phải thuộc về một công ty cụ thể để duy trì số dư tồn kho theo từng công ty. Để làm được điều này, mỗi Kho nên được liên kết với một Tài khoản trong Hệ thống tài khoản (tên giống với tên của chính Kho đó). Tài khoản này ghi nhận giá trị tiền tệ tương đương của hàng hóa hoặc vật tư được lưu trữ trong kho cụ thể đó.

Nếu bạn có một Cấu trúc Cây Kho chi tiết hơn, rất có thể bạn nên liên kết các vị trí phụ (phòng, dãy, kệ, v.v.) với tài khoản của Kho thực tế (Kho gốc của Cây đó) vì hầu hết các trường hợp không yêu cầu hạch toán giá trị của các mặt hàng tồn kho theo từng Kệ hoặc Ô hàng. Ví dụ, nếu bạn có Kho A, và các phòng, dãy là B, C, v.v., thì hãy liên kết B và C với tài khoản của A.

> Mẹo: ERPNext duy trì số dư tồn kho cho mọi sự kết hợp riêng biệt giữa Mặt hàng và Kho. Do đó, bạn có thể lấy được số dư tồn kho cho bất kỳ Mặt hàng cụ thể nào trong một Kho nhất định vào bất kỳ ngày cụ thể nào.

### 3. Các chủ đề liên quan
1. [Stock Entry Purpose](articles/stock-entry-purpose.md)
1. [Stock Level Report](stock-level-report.md)