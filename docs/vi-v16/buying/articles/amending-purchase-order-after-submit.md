# Sửa đổi Đơn mua hàng sau khi Xác nhận

Đơn giá và Số lượng trong Đơn mua hàng hiện có thể được sửa đổi sau khi Xác nhận bằng cách sử dụng nút `Cập nhật mặt hàng`.

<img alt="Update Items" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/po-update-items.png">

Để cập nhật Đơn giá và Số lượng trong một Đơn mua hàng đã Xác nhận, hãy nhấp vào nút `Cập nhật mặt hàng`. Một hộp thoại sẽ hiện ra để bạn thực hiện thay đổi.

<img alt="Update Items" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/po-update-items-rate-and-qty.gif">

Vui lòng lưu ý các điều kiện kiểm tra và trường hợp sử dụng sau:

- Tính năng Cập nhật sẽ kiểm tra xem Đơn mua hàng đã có Phiếu nhập hàng hay chưa.
- Số lượng có thể được cập nhật đối với Đơn mua hàng chưa nhập hàng hoặc đã nhập hàng một phần. Đối với Đơn mua hàng đã hoàn tất Phiếu nhập hàng, số lượng không thể cập nhật được.
- Đơn giá có thể được cập nhật đối với Đơn mua hàng chưa có Hóa đơn hoặc đã xuất hóa đơn một phần. Đối với Đơn mua hàng đã có Hóa đơn đã Xác nhận, đơn giá không thể cập nhật được.

---

### Các cập nhật mới trong phiên bản v16

Trong phiên bản v16, quy trình quản lý Nhà cung cấp và Đơn mua hàng được cải tiến với các tính năng sau:

- **Lọc Nhà cung cấp không vận chuyển (Non-transporter supplier filtering):** Cho phép lọc danh sách Nhà cung cấp chính xác hơn dựa trên vai trò vận chuyển trong quy trình mua hàng.
- **Số tham chiếu Nhà cung cấp (Supplier reference numbers):** Hỗ trợ thêm các trường số tham chiếu từ phía Nhà cung cấp để dễ dàng đối soát trong Đơn mua hàng.
- **Email append-to tạo bản nháp PI:** Tự động đính kèm hoặc tạo bản nháp Phiếu thông báo (Proforma Invoice) khi gửi email cho Nhà cung cấp.
- **Xem trước Sổ cái (Ledger Preview):** Cho phép kiểm tra nhanh các bút toán liên quan trực tiếp trước khi thực hiện các thao tác tiếp theo.