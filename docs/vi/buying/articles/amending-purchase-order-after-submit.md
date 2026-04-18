<!-- add-breadcrumbs -->
#Sửa đổi Đơn mua hàng sau khi Xác nhận
Đơn giá và Số lượng trong Đơn mua hàng hiện có thể được sửa đổi sau khi Xác nhận bằng cách sử dụng nút `Update Items`.

<img alt="Update Items" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/po-update-items.png">

Để cập nhật Đơn giá và Số lượng trong một Đơn mua hàng đã Xác nhận, hãy nhấp vào nút `Update Items`. Một hộp thoại sẽ hiện ra để bạn thực hiện thay đổi.

<img alt="Update Items" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/po-update-items-rate-and-qty.gif">

Vui lòng lưu ý các điều kiện kiểm tra và trường hợp sử dụng sau:

- Tính năng Cập nhật sẽ kiểm tra xem Đơn mua hàng đã có Phiếu nhập hàng và Hóa đơn mua hàng hay chưa.
- Số lượng có thể được cập nhật đối với Đơn mua hàng chưa nhập hàng hoặc đã nhập hàng một phần. Đối với Đơn mua hàng đã hoàn tất Phiếu nhập hàng, số lượng không thể cập nhật được.
- Đơn giá có thể được cập nhật đối với Đơn mua hàng chưa xuất hóa đơn hoặc đã xuất hóa đơn một phần. Đối với Đơn mua hàng đã có Hóa đơn mua hàng đã Xác nhận, đơn giá không thể cập nhật được.