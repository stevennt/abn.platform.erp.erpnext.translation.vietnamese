<!-- add-breadcrumbs -->
# Bán hàng Drop Ship

**Drop shipping** là một kỹ thuật quản lý chuỗi cung ứng trong đó nhà bán lẻ không giữ hàng trong kho. Thay vào đó, họ chuyển đơn hàng của khách hàng và chi tiết giao hàng cho nhà sản xuất, một nhà bán lẻ khác hoặc nhà bán buôn, sau đó bên này sẽ giao hàng trực tiếp cho khách hàng.

Trong ERPNext, bạn có thể thực hiện Drop Shipping bằng cách tạo Đơn mua hàng dựa trên Đơn bán hàng.

> Bán hàng > Chứng từ > Đơn bán hàng > Đơn mua hàng

#### Thiết lập trên Danh mục Mặt hàng

Thiết lập **_Delivered by Supplier (Drop Ship)_** và **_Default Supplier_** trong Danh mục Mặt hàng.

<img class="screenshot" alt="Setup Item Master" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/setup-drop-ship-on-item-master.png">

#### Thiết lập trên Đơn bán hàng
Nếu Drop Shipping đã được thiết lập trong Danh mục Mặt hàng, hệ thống sẽ tự động thiết lập **Supplier delivers to Customer** và **Supplier** trên Mặt hàng của Đơn bán hàng.

Bạn có thể thiết lập Drop Shipping trên Mặt hàng của Đơn bán hàng. Trong phần **Drop Ship**, hãy thiết lập **Supplier delivers to Customer** và chọn **Supplier** mà Đơn mua hàng sẽ được tạo dựa trên đó.

<img class="screenshot" alt="Setup Drop Shipping on Sales Order Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/setup-drop-ship-on-sales-order-item.png">

*Lưu ý: Tại giao diện Khách hàng, bạn có thể truy cập nhanh các Đơn bán hàng hoặc Báo giá liên quan thông qua các nút **SO/Quotation** được tích hợp sẵn trên form Khách hàng.*

#### Tạo Đơn mua hàng
Sau khi Xác nhận Đơn bán hàng, hãy tạo Đơn mua hàng.

<img class="screenshot" alt="Setup Drop Shipping on Sales Order Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/drop-ship-sales-order.png">

Từ Đơn bán hàng, tất cả các mặt hàng có tích chọn **Supplier delivers to Customer** hoặc có ghi **Supplier** (khớp với nhà cung cấp được chọn trong cửa sổ bật lên For Supplier) sẽ được ánh xạ sang Đơn mua hàng.

Hệ thống sẽ tự động thiết lập Khách hàng, Địa chỉ khách hàng và Người liên hệ.

Sau khi Xác nhận Đơn mua hàng, để cập nhật trạng thái giao hàng, hãy sử dụng tùy chọn **Delivered** dưới nút **Status** trên Đơn mua hàng. Nó sẽ cập nhật tỷ lệ phần trăm giao hàng và số lượng đã giao trên Đơn bán hàng.

<img class="screenshot" alt="Purchase Order for Drop Shipping" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/drop-ship-purchase-order.png">

<span style="color:#18B52D">**_Close_**</span>, là một tính năng để đóng hoặc đánh dấu việc hoàn tất đơn hàng trên **Đơn mua hàng** và **Đơn bán hàng**.

<img class="screenshot" alt="Close Sales Order" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/close-option-in-sales-order.png">

#### Quản lý Tồn kho và Giao hàng
Trong quy trình Drop Ship, việc quản lý tồn kho được tối ưu hóa thông qua tính năng **Stock Reservation** (Giữ hàng) để đảm bảo hàng hóa từ Nhà cung cấp được dành riêng cho đơn hàng của Khách hàng.

Khi thực hiện tạo Phiếu giao hàng (DN) từ Đơn bán hàng, hệ thống v16 áp dụng cơ chế **Cutoff date** để kiểm soát chính xác thời điểm ghi nhận việc giao hàng, giúp việc đối soát giữa Đơn bán hàng và thực tế giao từ Nhà cung cấp được chính xác hơn.

### Mẫu in Drop Shipping
Bạn có thể thông báo cho Nhà cung cấp bằng cách gửi email sau khi Xác nhận Đơn mua hàng bằng cách đính kèm mẫu in Drop Shipping.

<img class="screenshot" alt="Drop Dhip Print Format" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/drop-ship-print-format.png">

### Video Hướng dẫn về Drop Ship

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/hUc0hu_XLdo?rel=0" frameborder="0" allowfullscreen>
    </iframe>
</div>

{next}