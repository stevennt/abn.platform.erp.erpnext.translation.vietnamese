<!-- add-breadcrumbs -->
# Giấy báo Nợ

**Giấy báo Nợ là một chứng từ được người mua gửi cho Nhà cung cấp để thông báo rằng một khoản ghi nợ đã được ghi nhận đối với số hàng hóa đã trả lại cho Nhà cung cấp.**

Giấy báo Nợ được phát hành cho giá trị của số hàng hóa trả lại. Trong một số trường hợp, người bán cũng gửi Giấy báo Nợ, trường hợp này nên được xử lý như một hóa đơn khác.

Khoản ghi nợ là để bạn ghi chép lại khoản nợ đối với các Mặt hàng mà bạn trả lại.

## 1. Cách tạo Giấy báo Nợ

Người dùng có thể tạo Giấy báo Nợ dựa trên Hóa đơn mua hàng hoặc có thể tạo trực tiếp Giấy báo Nợ từ Hóa đơn mua hàng mà không cần tham chiếu.

1. Đi tới Hóa đơn mua hàng tương ứng và nhấp vào **Create > Return / Debit Note**.
 ![Debit Note from Invoice](/docs/v13/assets/img/accounts/debit-note-from-purchase-invoice.png)
1. Thông tin Nhà cung cấp và Mặt hàng sẽ được lấy từ thông tin đã thiết lập trong Hóa đơn mua hàng.
1. Nếu bạn đã thanh toán một phần hoặc toàn bộ, hãy thực hiện một Bút toán thanh toán đối với Hóa đơn mua hàng gốc.
1. Lưu và Xác nhận.

 ![Debit Note](/docs/v13/assets/img/accounts/debit-note.png)

Các bước khác tương tự như [Hóa đơn mua hàng](/docs/v13/user/manual/en/accounts/purchase-invoice).


### 1.1 Giấy báo Nợ ảnh hưởng đến sổ cái như thế nào
Giấy báo Nợ sẽ đảo ngược tác động của hóa đơn mua hàng.

![Debit Note Ledger](/docs/v13/assets/img/accounts/debit-note-ledger.png)

Tham khảo trang [Hóa đơn mua hàng](/docs/v13/user/manual/en/accounts/purchase-invoice) để biết thêm chi tiết khác.

### 1.2 Trường hợp chưa thực hiện thanh toán đối với Hóa đơn bán hàng
Trong trường hợp **không có thanh toán** nào được thực hiện đối với hóa đơn gốc, bạn chỉ cần Hủy Hóa đơn bán hàng. Tuy nhiên, nếu chỉ có 5 trên 10 Mặt hàng được trả lại từ một hóa đơn, việc tạo Giấy báo Nợ sẽ hữu ích để cập nhật sổ cái.

## 2. Ví dụ
Từ Nhà cung cấp Blue Mills, bạn đã mua Bông trị giá 2400 Rs + thuế và tại thời điểm giao hàng, bạn thấy rằng sản phẩm bị hư hỏng. Bây giờ bạn trả lại sản phẩm và một Giấy báo Nợ sẽ được phát hành.

Giấy báo Nợ với bút toán thanh toán trong ERPNext cho ví dụ trên như dưới đây:

![Creating Debit Note](/docs/v13/assets/img/accounts/creating-debit-note.gif)

### 3. Các chủ đề liên quan
1. [Bút toán thanh toán](/docs/v13/user/manual/en/accounts/payment-entry)
1. [Giấy báo Có](/docs/v13/user/manual/en/accounts/credit-note)

{next}