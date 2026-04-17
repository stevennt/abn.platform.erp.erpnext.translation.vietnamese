<!-- add-breadcrumbs -->
# Chuyển vật tư từ Phiếu giao hàng và Phiếu nhập hàng


Trong ERPNext, bạn có thể tạo bút toán Chuyển vật tư từ chứng từ [Phiếu kho](../stock-entry.html.md). Tuy nhiên, có một số trường hợp trong việc Chuyển vật tư mà nó cần được thể hiện dưới dạng Phiếu giao hàng và Phiếu nhập hàng.

## Chuyển vật tư từ Phiếu giao hàng

### Các trường hợp

1. Một trong những ví dụ là khi bạn chuyển vật tư từ kho của mình đến công trường dự án, tuy nhiên, bạn cần phải xuất trình nó dưới dạng Phiếu giao hàng cho khách hàng.

2. Ngoài ra, có những yêu cầu pháp lý về việc thuế phải được áp dụng cho mỗi lần chuyển vật tư. Việc quản lý sẽ dễ dàng hơn trong một giao dịch như Phiếu giao hàng so với Phiếu kho.

Xem xét các trường hợp này, tính năng Chuyển vật tư cũng đã được thêm vào trong Phiếu giao hàng. Dưới đây là các bước để sử dụng Phiếu giao hàng để tạo bút toán Chuyển vật tư.

### Các bước thực hiện

#### Kích hoạt Kho mục tiêu

DocType Phiếu giao hàng mặt hàng (Delivery Note Item) có một trường ẩn là Kho mục tiêu (Target Warehouse) (trước đây là Kho khách hàng - Customer Warehouse). Bạn có thể kích hoạt nó từ [Thiết lập kho](../stock-settings.md) bằng cách bật tùy chọn "Allow Material Transfer From Delivery Note and Sales Invoice".

Lưu ý rằng khách hàng được chọn phải đại diện cho cùng một công ty. Để thực hiện việc này, hãy bật tùy chọn 'Is Internal Customer' trong biểu mẫu khách hàng và chọn công ty của bạn trong trường 'Represents Company'.

<!-- <img class="screenshot" alt="Delivery Note Material Transfer" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/customer-warehouse.gif"> -->

### Chọn Kho

Khi tạo Phiếu giao hàng để Chuyển vật tư, đối với một mặt hàng, hãy chọn kho nguồn là Kho xuất (From Warehouse).

Trong Kho khách hàng (Customer Warehouse), hãy chọn một Kho nơi vật tư sẽ được chuyển đến hoặc chọn một kho mục tiêu.

<img class="screenshot" alt="Delivery Note Material Transfer" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/customer-warehouse-2.png">

Khi Xác nhận Phiếu giao hàng, tồn kho của mặt hàng sẽ được trừ khỏi "Kho xuất" và cộng vào "Kho khách hàng".

## Chuyển vật tư từ Phiếu nhập hàng

### Các trường hợp

Có những yêu cầu pháp lý về việc thuế phải được áp dụng cho mỗi lần chuyển vật tư. Việc quản lý tình huống này sẽ dễ dàng hơn trong một giao dịch như Phiếu nhập hàng so với Phiếu kho, vì thuế không thể được áp dụng cho việc chuyển mặt hàng thông qua Phiếu kho.

Dưới đây là các bước để sử dụng Phiếu nhập hàng để tạo bút toán Chuyển vật tư.

### Các bước thực hiện

#### Kích hoạt Kho nhà cung cấp

Tương tự như Kho khách hàng được hiển thị ở trên, bước đầu tiên là kích hoạt Kho nhà cung cấp (Supplier Warehouse) từ [Thiết lập kho](../stock-settings.md) như đã hiển thị ở trên.

Lưu ý rằng nhà cung cấp được chọn phải đại diện cho cùng một công ty. Để thực hiện việc này, hãy bật tùy chọn 'Is Internal Supplier' trong biểu mẫu Nhà cung cấp và chọn công ty của bạn trong trường 'Represents Company'.

<!-- <img class="screenshot" alt="Delivery Note Material Transfer" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/supplier-warehouse-enable.gif"> -->

### Chọn Kho

Khi tạo Phiếu nhập hàng để Chuyển vật tư, đối với một Mặt hàng, hãy chọn kho mục tiêu là Kho nhận (Accepted Warehouse).

Đây là cách bạn tạo một Phiếu nhập hàng nội bộ từ một Phiếu giao hàng nội bộ:

<img class="screenshot" alt="Purchase Receipt Material Transfer" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/supplier-warehouse-1.png">

Trong Kho nhà cung cấp (Supplier Warehouse), hãy chọn một Kho nơi vật tư sẽ được chuyển đi.

<img class="screenshot" alt="Purchase Receipt Material Transfer" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/supplier-warehouse.png">

Khi Xác nhận Phiếu nhập hàng, tồn kho của mặt hàng sẽ được trừ khỏi "Kho nhà cung cấp" và cộng vào "Kho nhận".