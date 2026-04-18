<!-- add-breadcrumbs -->
# Đơn hàng khung

**Đơn hàng khung là một đơn đặt hàng từ khách hàng để cung cấp vật tư cho các mặt hàng cụ thể trong một khoảng thời gian với mức giá đã thỏa thuận trước.**

Từ một đơn hàng khung, các đơn bán hàng có thể được tạo ra theo lịch trình giao hàng do khách hàng cung cấp. Đơn hàng khung giúp khách hàng tránh việc phải lưu trữ vật tư với số lượng lớn, đồng thời cho phép họ tận dụng được mức giá cố định bằng cách cam kết số lượng trong một khoảng thời gian cụ thể.

Để truy cập Đơn hàng khung, hãy đi tới:
> Home > Selling > Sales > Blanket Order

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Đơn hàng khung, bạn nên tạo các thông tin sau trước:

* [Khách hàng](https://docs.erpnext.com/docs/v16/user/manual/en/CRM/customer) hoặc [Nhà cung cấp](../buying/supplier.md)
* [Mặt hàng](../stock/item.md)

## 2. Cách tạo Đơn hàng khung cho Bán hàng và Mua hàng

1. Đi tới danh sách Đơn hàng khung, nhấn vào **New**.
1. Chọn Selling/Purchasing trong **Order Type**.
1. Chọn Khách hàng/Nhà cung cấp.
1. Chỉ định thời hạn hiệu lực của đơn hàng bằng cách chọn **From Date** và **To Date**.
1. Nhập **Item Code**, Số lượng và Đơn giá trong bảng Mặt hàng. Bạn cũng có thể ghi chú các Điều khoản và Điều kiện cho từng mặt hàng.
1. **Lưu**.
1. **Xác nhận**.

![Blanket Order Selling](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/blanket-order-selling.gif)

## 3. Các tính năng

### 3.1 Tạo Đơn bán hàng

Trường 'Ordered Quantity' sẽ được cập nhật sau khi một Đơn bán hàng được tạo. Sau khi Đơn hàng khung đã được **Xác nhận**, bạn có thể tạo các Đơn bán hàng mới bằng cách nhấn vào **Sales Order** dưới nút **Create**.

*Lưu ý: Trong phiên bản v16, bạn có thể truy cập nhanh các Đơn bán hàng hoặc Báo giá liên quan ngay tại form [Khách hàng](https://docs.erpnext.com/docs/v16/user/manual/en/CRM/customer) thông qua các nút bấm tùy chỉnh.*

### 3.2 Tạo Đơn mua hàng

Trường 'Ordered Quantity' sẽ được cập nhật sau khi một Đơn mua hàng được tạo. Sau khi Đơn hàng khung đã được **Xác nhận**, bạn có thể tạo các Đơn mua hàng mới bằng cách nhấn vào **Purchase Order** dưới nút **Create**.

### 3.3 Tạo Báo giá

Sau khi Đơn hàng khung đã được **Xác nhận**, bạn có thể tạo các Báo giá mới bằng cách nhấn vào **Quotation** dưới nút **Create**.

### 3.4 Cutoff date cho Phiếu giao hàng (DN)

Trong phiên bản v16, khi tạo Phiếu giao hàng (DN) từ Đơn bán hàng (SO) dựa trên Đơn hàng khung, hệ thống hỗ trợ thiết lập ngày cắt mốc (Cutoff date). Điều này giúp kiểm soát chính xác thời điểm giao hàng và quản lý lượng hàng tồn kho dự kiến hiệu quả hơn.

### 3.5 Giữ chỗ tồn kho (Stock Reservation)

Khi sử dụng Đơn hàng khung, bạn có thể kết hợp với tính năng **Stock Reservation** để giữ chỗ trước các mặt hàng trong kho, đảm bảo nguồn cung luôn sẵn sàng cho các Đơn bán hàng được tạo ra theo lịch trình từ Đơn hàng khung.

### 3.6 Trang tổng quan

Bạn có thể xem các Đơn mua hàng, Đơn bán hàng và Báo giá liên quan đến Đơn hàng khung này thông qua Trang tổng quan.

![Blanket Order Dashboard](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/blanket-order-dashboard.png)

**Lưu ý-** Có thể tạo nhiều Đơn bán hàng, Đơn mua hàng và Báo giá dựa trên một Đơn hàng khung.

## 4. Các chủ đề liên quan
* [Đơn bán hàng](sales-order.md)
* [Đơn mua hàng](../buying/purchase-order.md)

{next}