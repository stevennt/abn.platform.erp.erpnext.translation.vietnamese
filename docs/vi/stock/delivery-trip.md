<!-- add-breadcrumbs -->
# Chuyến giao hàng

**Một Chuyến giao hàng ghi lại các lần Giao hàng cho Khách hàng trên cùng một phương tiện.**

Có thể thêm nhiều điểm dừng và có thể gắn các Phiếu giao hàng đã được Xác nhận cho từng Khách hàng.

## 1. Cách tạo Chuyến giao hàng
Một Chuyến giao hàng có thể được tạo từ [Phiếu giao hàng](delivery-note.md) bằng cách nhấp vào 'Create > Delivery Trip'.

1. Đi đến: **Stock > Stock Transactions > Delivery Trip > New**
1. Chọn Tài xế và Phương tiện, tạo cả hai nếu chưa có.
1. Thiết lập ngày, ngày và giờ khởi hành.
1. Thêm khách hàng cho các điểm dừng giao hàng, địa chỉ sẽ được lấy tự động nếu đã được thiết lập. Khách hàng cũng có thể được lấy bằng cách nhấp vào 'Get customers from > Delivery Note'. Có thể thêm các Điểm dừng giao hàng bổ sung bằng cách nhấp vào nút Add Row trước khi xác nhận:

    <img class="screenshot" alt="Delivery" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/delivery_stops.png">

1. Lưu và xác nhận.

    <img class="screenshot" alt="Delivery" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/delivery_trip.png">

## 2. Các tính năng
### 2.1 Tính toán thời gian đến dự kiến
Nếu địa chỉ Khách hàng và địa chỉ Tài xế đã được thiết lập, bạn có thể tính toán thời gian đến dự kiến cho các lần giao hàng. Dữ liệu này được lấy từ Google Maps.

### 2.2 Tối ưu hóa lộ trình
Sử dụng Google Maps, lộ trình tốt nhất cho các lần giao hàng sẽ được tính toán.


### Các chủ đề liên quan
1. [Phiếu đóng gói](packing-slip.md)
1. [Quy tắc vận chuyển](../selling/shipping-rule.md)