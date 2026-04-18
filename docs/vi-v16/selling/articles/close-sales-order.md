# Đóng Đơn bán hàng

Trong các Đơn bán hàng đã được **Xác nhận**, bạn sẽ thấy tùy chọn **Stop** (Dừng). Việc dừng Đơn bán hàng sẽ hạn chế người dùng tạo **Phiếu giao hàng** và **Hóa đơn** bán hàng dựa trên đơn hàng đó.

![Close Option in Sales Order](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/close-option-in-sales-order.png)

#### Tình huống

Một đơn hàng được nhận cho mười Tuabin gió. **Đơn bán hàng** cũng được tạo cho mười **Mặt hàng**. Do thiếu hụt **Tồn kho**, chỉ có bảy đơn vị được giao cho **Khách hàng**. Ba đơn vị còn lại sẽ được giao sớm. **Khách hàng** thông báo rằng họ không cần giao các mặt hàng còn lại nữa, vì họ đã mua từ **Nhà cung cấp** khác.

Trong trường hợp này, **Phiếu giao hàng** và **Hóa đơn** bán hàng sẽ chỉ được tạo cho bảy đơn vị. Và **Đơn bán hàng** nên được thiết lập ở trạng thái đã dừng (stopped).

![Closed Sales Order](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/closed-sales-order.png)

Khi **Đơn bán hàng** được thiết lập là đã dừng, bạn sẽ không thấy số lượng còn lại (trong trường hợp này là ba) hiển thị trong các báo cáo Chờ giao (Pending to Deliver) và Chờ xuất hóa đơn (Pending to Invoice). Để thực hiện các giao dịch tiếp theo dựa trên **Đơn bán hàng** đã dừng, trước tiên bạn phải chọn **Unstop** (Bỏ dừng) nó.

Bạn cũng sẽ tìm thấy chức năng tương tự trong **Đơn mua hàng**.

#### Các cập nhật mới trong v16

*   **Cutoff date cho Phiếu giao hàng từ Đơn bán hàng:** Trong phiên bản v16, khi tạo **Phiếu giao hàng** từ **Đơn bán hàng**, bạn có thể thiết lập ngày cắt (Cutoff date). Điều này giúp kiểm soát việc chỉ cho phép giao các mặt hàng trong một khoảng thời gian nhất định, tránh việc giao nhầm các mặt hàng thuộc các đợt sau.
*   **Nút SO/Quotation trên Form Khách hàng:** Để tối ưu hóa quy trình bán hàng, tại giao diện thông tin **Khách hàng**, bạn sẽ thấy các nút truy cập nhanh để tạo trực tiếp **Đơn bán hàng** hoặc **Báo giá** mà không cần chuyển đổi nhiều bước.
*   **Giữ chỗ tồn kho (Stock Reservation):** Tính năng này cho phép bạn giữ chỗ các **Mặt hàng** trong **Kho** dựa trên **Đơn bán hàng** đã được **Xác nhận**. Việc này đảm bảo rằng hàng hóa dành riêng cho đơn hàng cụ thể sẽ không bị xuất cho các đơn hàng khác, giúp quản lý kế hoạch giao hàng chính xác hơn.

{next}