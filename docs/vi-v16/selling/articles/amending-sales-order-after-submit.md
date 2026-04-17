<!-- add-breadcrumbs -->
# Sửa đổi Đơn bán hàng sau khi Xác nhận

Đơn giá và Số lượng trong Đơn bán hàng hiện có thể được sửa đổi sau khi Xác nhận bằng cách sử dụng nút `Cập nhật mặt hàng` (Update Items).

![Update Items](https://docs.erpnext.com/docs/v16/assets/img/selling/so-update-items.png)

Để cập nhật Đơn giá và Số lượng trong một Đơn bán hàng đã Xác nhận, hãy nhấp vào nút `Cập nhật mặt hàng`. Một hộp thoại sẽ hiện ra để bạn thực hiện thay đổi.

![Update Items](https://docs.erpnext.com/docs/v16/assets/img/selling/so-update-items-rate-and-qty.gif)

Vui lòng lưu ý các điều kiện kiểm tra và trường hợp sử dụng sau:

- **Kiểm tra giao hàng (Cutoff date):** Tính năng Cập nhật sẽ kiểm tra xem Đơn bán hàng đã có Phiếu giao hàng (DN) hay chưa.
- **Số lượng:** Số lượng có thể được cập nhật đối với Đơn bán hàng chưa giao hàng hoặc đối với Phiếu giao hàng một phần. Đối với Đơn bán hàng đã hoàn tất tất cả các Phiếu giao hàng, số lượng sẽ không thể cập nhật.
- **Đơn giá:** Đơn giá có thể được cập nhật đối với Đơn bán hàng chưa xuất Hóa đơn hoặc mới xuất Hóa đơn một phần. Đối với Đơn bán hàng đã có Hóa đơn đã Xác nhận, đơn giá sẽ không thể cập nhật.

---

### Các tính năng mới trong v16

#### Nút lệnh trên Khách hàng
Trong giao diện Khách hàng, các nút lệnh để tạo nhanh Đơn bán hàng (SO) hoặc Báo giá (Quotation) đã được tối ưu hóa để giúp người dùng truy cập nhanh chóng các tài liệu liên quan từ hồ sơ Khách hàng.

#### Giữ chỗ Tồn kho (Stock Reservation)
Hệ thống v16 bổ sung tính năng Giữ chỗ Tồn kho, cho phép quản lý việc giữ hàng cho các Đơn bán hàng đã Xác nhận, giúp đảm bảo hàng hóa luôn sẵn sàng cho các đơn hàng ưu tiên và tránh tình trạng thiếu hụt khi thực hiện xuất kho.

{next}