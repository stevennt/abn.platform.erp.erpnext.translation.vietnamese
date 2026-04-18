<!-- add-breadcrumbs -->
# Mặt hàng thay thế

**Mặt hàng thay thế là một Mặt hàng tương tự như mặt hàng gốc và có thể được sử dụng thay thế cho mặt hàng gốc trong sản xuất.**

Nếu nguyên vật liệu được xác định trong BOM không có sẵn trong quá trình sản xuất, thì Mặt hàng thay thế tương ứng có sẵn có thể được sử dụng để hoàn tất quá trình sản xuất.

Trước tiên, bạn cần bật tùy chọn "Allow Alternative Item" trong Mặt hàng.
<img class="screenshot" alt="Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/allow-alternative-item.png">

Để truy cập danh sách mặt hàng thay thế, hãy đi đến:
> Home > Kho > Mặt hàng và Giá > Mặt hàng thay thế

Việc này cũng có thể được thực hiện bằng cách nhấp vào dấu cộng bên cạnh 'Mặt hàng thay thế' từ trang tổng quan của Mặt hàng.
Bạn có thể bật tính năng thay thế hai chiều (Two-Way replacement) giữa một Mặt hàng và mặt hàng thay thế của nó nếu cả hai đều có thể được sử dụng làm phương án thay thế cho nhau.

<img class="screenshot" alt="Item Alternative" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/item-alternative.png">

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Mặt hàng thay thế, bạn nên tạo các mục sau trước:

* [Mặt hàng](/docs/v16/user/manual/vi/stock/item)

## 2. Mặt hàng thay thế cho Lệnh sản xuất

Để cho phép sử dụng các Mặt hàng thay thế trong quá trình sản xuất, người dùng có thể cấu hình 'Allow Alternative Item' trong BOM/Lệnh sản xuất.

### 2.1 Quy định cho phép mặt hàng thay thế trong BOM
Bạn có thể bật 'Allow Alternative Item' trong một BOM, sau đó chọn mặt hàng thay thế trong Phiếu kho. Việc này cũng có thể được thực hiện với Lệnh sản xuất.
<img class="screenshot" alt="Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/allow-alternative-item-bom.png">


### 2.2 Quy định cho phép Mặt hàng thay thế trong Lệnh sản xuất
Người dùng cũng có thể bật/tắt tính năng cho phép mặt hàng thay thế cho từng Lệnh sản xuất riêng biệt.
<img class="screenshot" alt="Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/allow-alternative-item-wo.png">


Khi tích vào ô 'Allow Alternative Item', một nút có tên 'Alternate Item' sẽ xuất hiện. Bạn có thể nhấp vào nút này để thiết lập Mặt hàng thay thế trong Lệnh sản xuất. Đây là cách bạn sử dụng Mặt hàng thay thế trong một Lệnh sản xuất:
<img class="screenshot" alt="Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/work_order_item_alternative.gif">

Đây là cách bạn sử dụng Mặt hàng thay thế với một Phiếu kho:
<img class="screenshot" alt="Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/se_item_alternative.gif">

Nếu ô 'Allow Alternative Item' trong bảng Mặt hàng bị tắt, bạn không thể thiết lập Mặt hàng thay thế cho Mặt hàng này.

### 2.3 Mặt hàng thay thế cho gia công ngoài
Trong gia công ngoài, người dùng phải chuyển nguyên vật liệu cho Nhà cung cấp gia công để nhận lại thành phẩm từ họ. Nếu nguyên vật liệu không có sẵn trong Kho, với tính năng này, người dùng có thể chuyển mặt hàng thay thế của nguyên vật liệu gia công cho Nhà cung cấp. Việc này được thực hiện trong Phiếu kho.

<img class="screenshot" alt="Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/purchase_order_item_alternative.gif">

Sau đó, khi bạn tạo Phiếu nhập hàng từ Lệnh sản xuất, mặt hàng thay thế sẽ được hiển thị.

## 3. Các tính năng mới trong v16 (Liên quan đến quản lý kho)
Trong phiên bản v16, việc quản lý mặt hàng thay thế kết hợp chặt chẽ với các tính năng nâng cao:
* **Hệ thống Giữ hàng (Stock Reservation System):** Đảm bảo các mặt hàng thay thế được giữ đúng mục đích khi có lệnh sản xuất.
* **Truy xuất nguồn gốc Lô/Số sê-ri (Serial/Batch Traceability Report):** Theo dõi chính xác lô hàng của mặt hàng thay thế được sử dụng.
* **Kế toán kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Kiểm soát giá trị tồn kho chính xác khi sử dụng mặt hàng thay thế có giá trị khác biệt.

## 4. Các chủ đề liên quan
1. [Định mức nguyên vật liệu (BOM)](/docs/v16/user/manual/vi/manufacturing/bill-of-materials)
1. [Lệnh sản xuất](/docs/v16/user/manual/vi/manufacturing/work-order)

{next}