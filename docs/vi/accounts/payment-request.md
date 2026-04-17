<!-- add-breadcrumbs -->
# Yêu cầu thanh toán

**Yêu cầu thanh toán được sử dụng để yêu cầu thanh toán từ Khách hàng cho một Đơn bán hàng hoặc Hóa đơn.**

Yêu cầu thanh toán được gửi qua email và sẽ chứa một liên kết đến Cổng thanh toán nếu đã được thiết lập. Bạn có thể tạo yêu cầu thanh toán thông qua Đơn bán hàng hoặc Hóa đơn bán hàng. Một Yêu cầu thanh toán cũng có thể được thiết lập dựa trên Đơn mua hàng hoặc Hóa đơn mua hàng để phục vụ ghi chép nội bộ. Sau đó, các khoản thanh toán có thể được xử lý hàng loạt bằng cách sử dụng [Lệnh thanh toán](/docs/v13/user/manual/en/accounts/payment-order).

Để truy cập Điều khoản thanh toán, hãy đi tới:
> Home > Accounting > Accounts Receivable > Payment Term

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Yêu cầu thanh toán, bạn nên tạo các chứng từ sau trước:

1. [Hóa đơn bán hàng](/docs/v13/user/manual/en/accounts/sales-invoice)
1. [Hóa đơn mua hàng](/docs/v13/user/manual/en/accounts/purchase-invoice)
1. [Đơn bán hàng](/docs/v13/user/manual/en/selling/sales-order)
1. [Đơn mua hàng](/docs/v13/user/manual/en/buying/purchase-order)

## 2. Cách tạo Yêu cầu thanh toán
Yêu cầu thanh toán không thể được tạo thủ công, nó được tạo từ Đơn bán hàng/Đơn mua hàng hoặc Hóa đơn.

### 2.1 Tạo Yêu cầu thanh toán thông qua Đơn bán hàng
Trong một Đơn bán hàng, nhấp vào Create và sau đó nhấp vào Payment để thực hiện thanh toán tạm ứng. Để biết thêm về thanh toán tạm ứng, hãy truy cập trang [Bút toán thanh toán tạm ứng](/docs/v13/user/manual/en/accounts/advance-payment-entry).

![Payment Request From Sales Order](/docs/v13/assets/img/accounts/payment-request-from-sales-order.png)

### 2.2 Tạo Yêu cầu thanh toán thông qua Hóa đơn bán hàng
Trong một Hóa đơn bán hàng, nhấp vào Create và sau đó nhấp vào Payment để thực hiện thanh toán cho hóa đơn.

![Payment Request From Sales Invoice](/docs/v13/assets/img/accounts/payment-request-from-sales-invoice.png)

Chọn Tài khoản cổng thanh toán (Payment Gateway Account) phù hợp trên Yêu cầu thanh toán để hạch toán tài khoản. Tài khoản được chỉ định trên cổng thanh toán sẽ được xem xét để tạo Bút toán.

> Lưu ý: Tiền tệ của Hóa đơn/Đơn hàng và tiền tệ của 'Payment Gateway Account' phải giống nhau.

![Payment Request Details](/docs/v13/assets/img/accounts/payment-request-details.png)

### 2.3 Thông báo cho Khách hàng
Bạn có thể thông báo cho khách hàng từ Yêu cầu thanh toán bằng cách sử dụng [Mẫu in](/docs/v13/user/manual/en/setting-up/print/print-format). Nếu email liên hệ của khách hàng đã được thiết lập, nó sẽ được lấy tự động. Nếu không, bạn có thể thiết lập một địa chỉ email trong Yêu cầu thanh toán.

![Payment Request Details](/docs/v13/assets/img/accounts/payment-request-recipient-details.png)

### 2.4 Email yêu cầu
Đây là một ví dụ về email yêu cầu. URL sẽ được tạo tự động nếu bạn đã thiết lập tích hợp thanh toán tương ứng. Để biết thêm về các tích hợp, hãy [truy cập trang này](/docs/v13/user/manual/en/erpnext_integration).

<img class="screenshot" alt="Payment Request" src="{{docs_base_url}}/v13/assets/img/accounts/pr-email.png">

### 2.5 Yêu cầu thanh toán không sử dụng Cổng thanh toán

Trong trường hợp bạn không muốn sử dụng bất kỳ tích hợp hoặc cổng thanh toán nào mà chỉ muốn gửi thông báo, hãy chỉ cần thiết lập Tài khoản ngân hàng. Bạn sẽ phải soạn nội dung tin nhắn phù hợp với thông tin ngân hàng. Bên liên quan sau đó có thể chuyển Số tiền đến tài khoản ngân hàng đã nêu.

## 3. Các chủ đề liên quan
1. [Bút toán thanh toán](/docs/v13/user/manual/en/accounts/payment-entry)
1. [Điều khoản thanh toán](/docs/v13/user/manual/en/accounts/payment-terms)
1. [Hóa đơn bán hàng](/docs/v13/user/manual/en/accounts/sales-invoice)
1. [Hóa đơn mua hàng](/docs/v13/user/manual/en/accounts/purchase-invoice)

{next}