<!-- add-breadcrumbs -->
# Giấy báo Nợ

**Giấy báo Nợ là một chứng từ được người mua gửi cho Nhà cung cấp để thông báo rằng một khoản ghi nợ đã được ghi nhận đối với số hàng hóa đã trả lại cho Nhà cung cấp.**

Giấy báo Nợ được phát hành cho giá trị của số hàng hóa trả lại. Trong một số trường hợp, người bán cũng gửi Giấy báo Nợ, trường hợp này nên được xử lý như một hóa đơn khác.

Khoản ghi nợ là để bạn ghi chép lại khoản nợ đối với các Mặt hàng mà bạn trả lại.

## 1. Cách tạo Giấy báo Nợ

Người dùng có thể tạo Giấy báo Nợ dựa trên Hóa đơn mua hàng hoặc có thể tạo trực tiếp Giấy báo Nợ mà không cần tham chiếu.

1. Đi tới Hóa đơn mua hàng tương ứng và nhấp vào **Create > Return / Debit Note**.
 ![Debit Note from Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/debit-note-from-purchase-invoice.png)
1. Thông tin Nhà cung cấp và Mặt hàng sẽ được lấy từ thông tin đã thiết lập trong Hóa đơn mua hàng.
1. Nếu bạn đã thanh toán một phần hoặc toàn bộ, hãy thực hiện một Bút toán thanh toán đối với Hóa đơn mua hàng gốc.
1. **Lưu** và **Xác nhận**.

 ![Debit Note](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/debit-note.png)

Các bước khác tương tự như [Hóa đơn mua hàng](purchase-invoice.md).


### 1.1 Giấy báo Nợ ảnh hưởng đến sổ cái như thế nào
Giấy báo Nợ sẽ đảo ngược tác động của hóa đơn mua hàng. Với các tính năng mới trong v16, bạn có thể sử dụng tính năng **Xem trước Bút toán (Ledger Preview)** trước khi **Xác nhận** để kiểm tra chính xác các tài khoản nợ/có sẽ bị ảnh hưởng.

![Debit Note Ledger](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/debit-note-ledger.png)

Tham khảo trang [Hóa đơn mua hàng](purchase-invoice.md) để biết thêm chi tiết khác.

### 1.2 Trường hợp chưa thực hiện thanh toán đối với Hóa đơn mua hàng
Trong trường hợp **không có thanh toán** nào được thực hiện đối với hóa đơn gốc, bạn có thể cân nhắc việc **Hủy** hóa đơn mua hàng nếu cần. Tuy nhiên, nếu chỉ có một phần số lượng Mặt hàng được trả lại từ một hóa đơn, việc tạo Giấy báo Nợ là phương án tối ưu để cập nhật sổ cái và quản lý công nợ chính xác.

## 2. Ví dụ
Từ Nhà cung cấp Blue Mills, bạn đã mua Bông trị giá 2400 Rs + thuế và tại thời điểm giao hàng, bạn thấy rằng sản phẩm bị hư hỏng. Bây giờ bạn trả lại sản phẩm và một Giấy báo Nợ sẽ được phát hành.

Giấy báo Nợ với bút toán thanh toán trong ERPNext cho ví dụ trên như dưới đây:

![Creating Debit Note](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/creating-debit-note.gif)

### 3. Các chủ đề liên quan
1. [Bút toán thanh toán](payment-entry.md)
1. [Giấy báo Có](credit-note.md)

{next}