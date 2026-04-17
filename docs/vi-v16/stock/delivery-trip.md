<!-- add-breadcrumbs -->
# Chuyến giao hàng

**Một Chuyến giao hàng ghi lại các lần Giao hàng cho Khách hàng trên cùng một phương tiện.**

Có thể thêm nhiều điểm dừng và có thể gắn các Phiếu giao hàng đã được Xác nhận cho từng Khách hàng.

## 1. Cách tạo Chuyến giao hàng
Một Chuyến giao hàng có thể được tạo từ [Phiếu giao hàng](delivery-note.md) bằng cách nhấp vào 'Create > Delivery Trip'.

1. Đi đến: **Kho > Giao dịch kho > Chuyến giao hàng > Mới**
1. Chọn Tài xế và Phương tiện, tạo cả hai nếu chưa có.
1. Thiết lập ngày, ngày và giờ khởi hành.
1. Thêm khách hàng cho các điểm dừng giao hàng, địa chỉ sẽ được lấy tự động nếu đã được thiết lập. Khách hàng cũng có thể được lấy bằng cách nhấp vào 'Get customers from > Delivery Note'. Có thể thêm các Điểm dừng giao hàng bổ sung bằng cách nhấp vào nút Add Row trước khi Xác nhận:

    <img class="screenshot" alt="Delivery" src="https://docs.erpnext.com/docs/v16/assets/img/stock/delivery_stops.png">

1. Lưu và Xác nhận.

    <img class="screenshot" alt="Delivery" src="https://docs.erpnext.com/docs/v16/assets/img/stock/delivery_trip.png">

## 2. Các tính năng mới trong v16

### 2.1 Hệ thống Giữ hàng (Stock Reservation System)
Trong phiên bản v16, Chuyến giao hàng có thể kết hợp với hệ thống Giữ hàng để đảm bảo các Mặt hàng đã được phân bổ cho các Đơn bán hàng cụ thể sẽ luôn sẵn sàng trong Kho khi phương tiện khởi hành, giúp giảm thiểu tình trạng thiếu hụt hàng hóa tại điểm giao.

### 2.2 Truy xuất nguồn gốc Lô hàng/Số Serial (Serial/Batch Traceability Report)
Khi quản lý Chuyến giao hàng, người dùng có thể truy xuất nhanh chóng báo cáo nguồn gốc của các Lô hàng hoặc Số Serial được giao trong chuyến đi đó, giúp kiểm soát chất lượng và quản lý vòng đời sản phẩm chặt chẽ hơn.

### 2.3 Chi phí cập bến cho Phiếu kho (Landed Cost cho Stock Entry)
Cho phép phân bổ các chi phí vận chuyển, bốc xếp phát sinh trong quá trình thực hiện Chuyến giao hàng trực tiếp vào giá trị của Mặt hàng trong Kho, giúp phản ánh chính xác giá trị tồn kho thực tế.

### 2.4 Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting)
Hệ thống tự động ghi nhận các bút toán kế toán chi tiết cho từng Mặt hàng dựa trên các biến động trong Chuyến giao hàng, giúp việc đối soát giữa sổ cái và tồn kho trở nên chính xác tuyệt đối.

### 2.5 Xem trước Sổ cái (Ledger Preview)
Người dùng có thể xem trước các bút toán kế toán liên quan đến việc xuất kho và giao hàng ngay trong giao diện Chuyến giao hàng trước khi thực hiện Xác nhận cuối cùng.

### 2.3 Tính toán thời gian đến dự kiến
Nếu địa chỉ Khách hàng và địa chỉ Tài xế đã được thiết lập, bạn có thể tính toán thời gian đến dự kiến cho các lần giao hàng. Dữ liệu này được lấy từ Google Maps.

### 2.4 Tối ưu hóa lộ trình
Sử dụng Google Maps, lộ trình tốt nhất cho các lần giao hàng sẽ được tính toán.


### Các chủ đề liên quan
1. [Phiếu đóng gói](packing-slip.md)
1. [Quy tắc vận chuyển](../selling/shipping-rule.md)