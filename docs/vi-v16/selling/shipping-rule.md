# Quy tắc vận chuyển

**Sử dụng Quy tắc vận chuyển, bạn có thể xác định chi phí để giao sản phẩm cho Khách hàng hoặc Nhà cung cấp.**

Bạn có thể xác định các quy tắc vận chuyển khác nhau hoặc một số tiền vận chuyển cố định cho cùng một Mặt hàng tại các khu vực khác nhau.

Để truy cập Quy tắc vận chuyển, hãy đi tới:
> Home > Selling > Items and Pricing > Shipping Rule

## 1. Cách tạo Quy tắc vận chuyển
1. Đi tới danh sách Quy tắc vận chuyển, nhấn vào **New**.
2. Nhập nhãn Quy tắc vận chuyển, ví dụ 'Priority Shipping' hoặc 'Next Day Shipping'.
3. Tiếp tục với các chi tiết kế toán như Tài khoản vận chuyển (Shipping Account), Trung tâm chi phí (Cost Center) nơi số tiền sẽ được tính vào, và Số tiền vận chuyển (Shipping Amount).
4. Tại mục **Calculate Based On**, bạn có thể thay đổi cơ sở tính toán mà Quy tắc vận chuyển sẽ được áp dụng như tổng ròng số lượng hoặc tổng ròng trọng lượng, mặc định là "Fixed".
5. **Lưu**.

    <img class="screenshot" alt="Shipping Rule" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/shipping-rule.png">

## 2. Các tính năng mới và nâng cao (v16)

### 2.1 Điều kiện Quy tắc vận chuyển
Khi chọn Net Total hoặc Net Weight, một bảng sẽ xuất hiện nơi bạn có thể thiết lập các giá trị từ (from) và đến (to) cho số tiền hoặc trọng lượng. Nhập Số tiền vận chuyển cần được tính toán cho phạm vi đã nhập. Thêm nhiều điều kiện hơn nếu cần thiết. Bạn chỉ có thể chọn một trong ba phương pháp tính toán trong một Quy tắc vận chuyển.

### 2.2 Giới hạn theo quốc gia
Bạn có thể giới hạn Quy tắc vận chuyển cho một số quốc gia nhất định, hãy thêm các quốc gia vào bảng. Theo mặc định, Quy tắc vận chuyển sẽ được áp dụng trên toàn cầu.

### 2.3 Quản lý tồn kho và Đơn hàng (Cập nhật v16)
Trong phiên bản v16, quy trình vận chuyển được tối ưu hóa thông qua các tính năng:
* **Stock Reservation (Giữ hàng tồn kho):** Cho phép hệ thống giữ trước lượng Mặt hàng trong Kho khi có Đơn bán hàng (SO) hoặc Báo giá (Quotation), giúp đảm bảo khả năng cung ứng khi lập Phiếu giao hàng (DN).
* **Cutoff date cho DN từ SO:** Bạn có thể thiết lập ngày cắt sổ (cutoff date) để kiểm soát việc tạo Phiếu giao hàng (DN) từ Đơn bán hàng (SO), giúp quản lý kế hoạch xuất kho chính xác hơn.
* **Nút truy cập nhanh trên Khách hàng:** Tại form Khách hàng, các nút truy cập nhanh cho SO và Quotation được cải tiến để người dùng dễ dàng theo dõi lịch sử giao dịch và điều hướng nhanh chóng.

## 3. Các chủ đề liên quan
1. [Drop Shipping](articles/drop-shipping.md)
1. [Khách hàng](user/manual/crm/customer.md)

{next}