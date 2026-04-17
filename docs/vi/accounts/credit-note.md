<!-- add-breadcrumbs -->
# Giấy báo có

**Giấy báo có là một chứng từ được người bán gửi cho Khách hàng, thông báo rằng một khoản tín dụng đã được ghi có vào tài khoản của họ đối với số hàng hóa mà người mua đã trả lại.**

Giấy báo có được phát hành cho giá trị của hàng hóa do Khách hàng trả lại, nó có thể ít hơn hoặc bằng tổng số tiền của đơn hàng.

## 1. Cách tạo Giấy báo có

Người dùng có thể tạo Giấy báo có dựa trên Hóa đơn bán hàng hoặc họ có thể tạo trực tiếp Giấy báo có từ Hóa đơn bán hàng mà không cần tham chiếu. Lưu ý rằng để tạo Giấy báo có, hóa đơn phải được thanh toán bằng [Bút toán thanh toán](/docs/v13/user/manual/en/accounts/payment-entry).

1. Đi tới Hóa đơn bán hàng tương ứng và nhấp vào **Create > Return / Credit Note**.
    ![Credit Note from Invoice](/docs/v13/assets/img/accounts/credit-note-from-invoice.png)

1. Thông tin Khách hàng và Mặt hàng sẽ được lấy từ các thông tin đã thiết lập trong Hóa đơn bán hàng.
1. Nếu Khách hàng đã thanh toán một phần hoặc toàn bộ, hãy tạo một Bút toán thanh toán đối với Hóa đơn bán hàng gốc.
1. Lưu và Xác nhận.
    
 ![Credit Note](/docs/v13/assets/img/accounts/credit-note.png)

Số lượng Mặt hàng và Số tiền thanh toán sẽ là số âm vì đây là một khoản trả hàng.

### 1.1 Giấy báo có ảnh hưởng đến sổ cái như thế nào
Sau khi một Bút toán thanh toán được tạo đối với Hóa đơn bán hàng gốc, số tiền sẽ được cộng vào tài khoản của Khách hàng dưới dạng số âm để lần tới khi họ mua hàng, số tiền này sẽ được điều chỉnh.

Đây là cách sổ cái bị ảnh hưởng sau khi có một bút toán thanh toán đối với hóa đơn bị trả lại:
![Credit Note Ledger](/docs/v13/assets/img/accounts/credit-note-ledger.png)

Tham khảo trang [Hóa đơn bán hàng](/docs/v13/user/manual/en/accounts/sales-invoice) để biết thêm các chi tiết khác.

### 1.2 Không có thanh toán nào được thực hiện đối với Hóa đơn bán hàng
Trong trường hợp **không có thanh toán** nào được thực hiện đối với hóa đơn gốc, bạn chỉ cần Hủy Hóa đơn bán hàng. Tuy nhiên, nếu chỉ có 5 trên 10 Mặt hàng được trả lại từ một hóa đơn, việc tạo Giấy báo có sẽ hữu ích để cập nhật sổ cái.

## 2. Ví dụ

Khách hàng Rohan đã mua ống PVC trị giá 300 Rs + thuế và tại thời điểm giao hàng, Khách hàng thấy rằng sản phẩm đã bị hư hỏng. Bây giờ Rohan đã trả lại sản phẩm, một Giấy báo có sẽ được phát hành.

Giấy báo có với bút toán thanh toán trong ERPNext cho ví dụ trên như dưới đây:

![Creating Credit Note](/docs/v13/assets/img/accounts/creating-credit-note.gif)

### 3. Các chủ đề liên quan
1. [Bút toán thanh toán](/docs/v13/user/manual/en/accounts/payment-entry)
1. [Giấy báo nợ](/docs/v13/user/manual/en/accounts/debit-note)
1. [Trả hàng bán](/docs/v13/user/manual/en/stock/sales-return)

{next}