<!-- add-breadcrumbs -->
#Sửa đổi Đơn bán hàng sau khi Xác nhận
Đơn giá và Số lượng trong Đơn bán hàng hiện có thể được sửa đổi sau khi Xác nhận bằng cách sử dụng nút `Update Items`.

![Update Items](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/so-update-items.png)

Để cập nhật Đơn giá và Số lượng trong một Đơn bán hàng đã Xác nhận, hãy nhấp vào nút `Update Items`. Một hộp thoại sẽ hiện ra để bạn thực hiện thay đổi.

![Update Items](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/so-update-items-rate-and-qty.gif)

Vui lòng lưu ý các điều kiện kiểm tra và trường hợp sử dụng sau:

- Tính năng Cập nhật sẽ kiểm tra xem Đơn bán hàng đã có Phiếu giao hàng và Hóa đơn bán hàng hay chưa.
- Số lượng có thể được cập nhật đối với Đơn bán hàng chưa giao hàng và đối với Phiếu giao hàng một phần. Đối với Đơn bán hàng đã hoàn tất các Phiếu giao hàng, số lượng sẽ không thể cập nhật.
- Đơn giá có thể được cập nhật đối với Đơn bán hàng chưa xuất hóa đơn hoặc mới xuất hóa đơn một phần. Đối với Đơn bán hàng đã có Hóa đơn bán hàng đã Xác nhận, đơn giá sẽ không thể cập nhật.

{next}