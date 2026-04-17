<!-- add-breadcrumbs -->
# Bút toán thanh toán trước

**Khoản thanh toán được thực hiện bởi Khách hàng/Nhà cung cấp trước khi hóa đơn được gửi đi được gọi là Thanh toán trước.**

Thông thường, thanh toán trước được thực hiện trong trường hợp các giao dịch có giá trị cao. Hãy xem xét trường hợp một Khách hàng - Jane D'souza đặt mua một mặt hàng nội thất xa xỉ có giá ₹24,000. Cô ấy được yêu cầu trả trước một khoản tiền trước khi cửa hàng nội thất bắt đầu thực hiện đơn hàng của mình. Cô ấy trả cho họ ₹10,000 bằng tiền mặt.

Trong ERPNext, bút toán thanh toán trước được tạo bằng cách sử dụng Bút toán thanh toán. Nếu đã có Đơn bán hàng, bạn có thể tạo trực tiếp một Bút toán thanh toán cho số tiền thanh toán trước. Nếu không, bạn cũng có thể tạo một Bút toán thanh toán độc lập cho Khách hàng. Tương tự, bạn cũng có thể tạo Bút toán thanh toán trước cho Nhà cung cấp thông qua Đơn mua hàng.

![Payment Entry From Sales Order](https://docs.erpnext.com/docs/v13/assets/img/accounts/payment-option-in-sales-order.png)

> Lưu ý: Nếu khoản thanh toán không được liên kết với một hóa đơn, nó sẽ được coi là khoản thanh toán trước. Các khoản thanh toán trước sẽ được phản ánh trong các báo cáo Phải thu khách hàng và Phải trả nhà cung cấp.

## 1. Điều kiện tiên quyết
Để tạo một bút toán thanh toán trước, các mục sau đây cần được tạo trước:

* Đối tác (Khách hàng/ Nhà cung cấp)
* Tài khoản thanh toán (Tài khoản Ngân hàng hoặc Tiền mặt)

## 2. Cách tạo Bút toán thanh toán trước
Sau khi Đơn bán hàng hoặc Đơn mua hàng đã được Xác nhận, bạn sẽ thấy tùy chọn để tạo một khoản Thanh toán cho đơn hàng đó. Bạn cũng có thể tạo Bút toán thanh toán mới và chọn các giá trị một cách thủ công (như Đối tác và tài khoản thanh toán). Dưới đây là các bước để tạo Thanh toán trước đối với Đơn bán hàng.

1. Đi tới Đơn bán hàng và nhấp vào **Make > Payment Entry**.
1. Thiết lập/kiểm tra các tài khoản.
1. Lưu và Xác nhận.


Bất kỳ Bút toán thanh toán nào không được liên kết với một hóa đơn đều được hệ thống ERPNext coi là thanh toán trước.

Nếu Khách hàng đã đưa trước $5,000 bằng tiền mặt, nó sẽ được ghi nhận là một bút toán có (credit) đối với tài khoản Phải thu của Khách hàng. Để cân bằng [theo hệ thống kế toán kép], $5000 sẽ được ghi nợ (debit) vào tài khoản tiền mặt của Công ty.

### 2.2 Phân bổ Thanh toán trước vào Hóa đơn

Khi tạo hóa đơn, bạn có thể kiểm tra xem có khoản Thanh toán trước nào đối với Đối tác đó hay không.

![Fetch Advance Payments in Sales Invoice](https://docs.erpnext.com/docs/v13/assets/img/accounts/fetch-advance-payments-in-invoice.png)

Khi nhấp vào nút **Get Advance Received**, hệ thống sẽ lấy các Bút toán thanh toán trước được tìm thấy cho đối tác đó. Sau khi các Bút toán thanh toán trước được lấy ra, bạn có thể phân bổ Số tiền thanh toán trước cho hóa đơn này. Việc phân bổ sẽ làm giảm Số tiền còn lại của hóa đơn đó ngay lập tức.

Lưu và Xác nhận Hóa đơn bán hàng.

### 3. Các chủ đề liên quan
1. [Sales Invoice](sales-invoice.md)
1. [Journal Entry](journal-entry.md)
1. [Payment Entry](payment-entry.md)

{next}