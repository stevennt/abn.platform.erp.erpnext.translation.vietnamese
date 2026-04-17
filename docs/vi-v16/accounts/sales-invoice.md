<!-- add-breadcrumbs -->
# Hóa đơn bán hàng

**Hóa đơn bán hàng là hóa đơn mà bạn gửi cho Khách hàng để Khách hàng thực hiện thanh toán.**

Hóa đơn bán hàng là một giao dịch kế toán. Khi Xác nhận Hóa đơn bán hàng, hệ thống sẽ cập nhật các khoản phải thu và ghi nhận thu nhập vào Tài khoản Khách hàng.

Để truy cập danh sách Hóa đơn bán hàng, hãy đi tới:
> Home > Accounting > Accounts Receivable > Sales Invoice

![SO Flow](https://docs.erpnext.com/docs/v16/assets/img/accounts/so-flow.png)

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Hóa đơn bán hàng, bạn nên tạo các thông tin sau trước:

* [Mặt hàng](../stock/item.md)
* [Khách hàng](../selling/customer-list.md)

* Tùy chọn:
 * [Đơn bán hàng](../selling/sales-order.md)
 * [Phiếu giao hàng](../stock/delivery-note.md)

## 2. Cách tạo Hóa đơn bán hàng
Hóa đơn bán hàng thường được tạo từ Đơn bán hàng hoặc Phiếu giao hàng. Chi tiết Mặt hàng của Khách hàng sẽ được lấy vào Hóa đơn bán hàng. Tuy nhiên, bạn cũng có thể tạo Hóa đơn bán hàng trực tiếp, ví dụ như hóa đơn POS.

Để lấy thông tin tự động trong Hóa đơn bán hàng, hãy nhấp vào **Get Items from**. Thông tin có thể được lấy từ Đơn bán hàng, Phiếu giao hàng hoặc Báo giá.

Để tạo thủ công, hãy làm theo các bước sau:

1. Đi tới danh sách Hóa đơn bán hàng và nhấp vào **New**.
1. Chọn Khách hàng.
1. Thiết lập Ngày đến hạn thanh toán.
1. Trong bảng Mặt hàng, chọn các Mặt hàng và thiết lập số lượng.
1. Giá sẽ được lấy tự động nếu [Mặt hàng Price](../stock/item-price.md) được thêm vào, nếu không hãy thêm giá vào bảng.
1. Ngày và giờ ghi sổ sẽ được thiết lập theo thời gian hiện tại, bạn có thể chỉnh sửa sau khi tích vào ô kiểm bên dưới Posting Time để tạo một bút toán lùi ngày.
1. **Lưu** và **Xác nhận**.
 ![New Sales Invoice](https://docs.erpnext.com/docs/v16/assets/img/accounts/new-sales-invoice.png)

### 2.1 Các tùy chọn bổ sung khi tạo Hóa đơn bán hàng

* **Include Payment (POS)**: Nếu hóa đơn này dành cho bán lẻ / Điểm bán hàng. [Tìm hiểu thêm tại đây](sales-invoice.md#324-pos-invoices).
* **Is Return Credit Note**: Tích vào đây nếu khách hàng đã trả lại Mặt hàng. Để biết thêm chi tiết, hãy truy cập trang [Credit Note](credit-note.md).

![POS and Credit Note Options](https://docs.erpnext.com/docs/v16/assets/img/accounts/pos-and-credit-note-in-sales-invoice.png)

Dành cho Ấn Độ:
**e-Way Bill No**: Theo quy định của GST, đơn vị vận chuyển cần mang theo e-Way Bill. Để biết cách tạo e-Way Bill, [hãy truy cập trang này](https://docs.erpnext.com/docs/v16/user/manual/en/regional/india/auto-generate-e-way-bill-JSON).

### 2.2 Trạng thái

Đây là các trạng thái được tự động gán cho Hóa đơn bán hàng.

* **Draft**: Bản nháp đã được Lưu nhưng chưa được Xác nhận.
* **Ledger Preview**: (Mới trong v16) Cho phép xem trước các bút toán sẽ được ghi vào sổ cái trước khi bạn thực hiện Xác nhận.
* **Submitted**: Hóa đơn đã được Xác nhận vào hệ thống và sổ cái đã được cập nhật.
* **Paid**: Khách hàng đã thực hiện thanh toán và một [Bút toán thanh toán](payment-entry.md) đã được Xác nhận.
* **Unpaid**: Hóa đơn đã được tạo nhưng việc thanh toán đang chờ xử lý và vẫn trong hạn thanh toán.
* **Overdue**: Việc thanh toán đang chờ xử lý và đã quá hạn thanh toán.
* **Canceled**: Hóa đơn bán hàng đã bị Hủy vì bất kỳ lý do gì. Khi một hóa đơn bị Hủy, các tác động của nó đối với Tài khoản và Tồn kho sẽ được hoàn tác.
* **Credit Note Issued**: Mặt hàng được trả lại bởi Khách hàng và một [Credit Note](credit-note.md) được tạo cho hóa đơn này.
* **Return**: Trạng thái này được gán cho Credit Note được tạo đối với Hóa đơn bán hàng gốc. Tuy nhiên, bạn cũng có thể tạo một Credit Note độc lập.
* **Unpaid and Discounted**: Việc thanh toán đang chờ xử lý và bất kỳ gói đăng ký đang diễn ra nào đã được chiết khấu bằng cách sử dụng [Invoice Discounting](invoice_discounting.md).
* **Overdue and Discounted**: Việc thanh toán đang chờ xử lý và đã quá hạn thanh toán, đồng thời bất kỳ gói đăng ký đang diễn ra nào đã được chiết khấu bằng cách sử dụng [Invoice Discounting](invoice_discounting.md).

## 3. Tính năng
### 3.1 Ngày tháng

* **Ngày hạch toán (Posting Date)**: Ngày mà Hóa đơn bán hàng sẽ ảnh hưởng đến sổ sách kế toán của bạn, tức là Sổ cái. Điều này sẽ ảnh hưởng đến tất cả các số dư của bạn trong kỳ kế toán đó.

* **Hạn thanh toán (Due Date)**: Ngày mà khoản thanh toán đến hạn (nếu bạn bán hàng trả chậm). Hạn mức tín dụng có thể được thiết lập từ danh mục [Khách hàng](../selling/customer-list.md).

### 3.2 Chiều kế toán (Accounting Dimensions)
Chiều kế toán cho phép bạn gắn thẻ các giao dịch dựa trên một Khu vực, Chi nhánh, Khách hàng cụ thể, v.v. Điều này giúp xem các báo cáo kế toán riêng biệt dựa trên (các) chiều đã chọn. Để biết thêm, hãy xem trợ giúp về tính năng [Chiều kế toán](accounting-dimensions.md).

> Lưu ý: Dự án và Trung tâm chi phí được mặc định coi là các chiều kế toán.

### 3.3 Chi tiết Đơn mua hàng của Khách hàng

* **Đơn mua hàng của Khách hàng (Customer's Purchase Order)**: Theo dõi số Đơn mua hàng của khách hàng nhận được, chủ yếu để ngăn chặn việc tạo trùng Đơn bán hàng hoặc Hóa đơn cho cùng một Đơn mua hàng nhận được từ Khách hàng. Bạn có thể cấu hình thêm các thiết lập liên quan đến việc xác thực số Đơn mua hàng của khách hàng trong [Thiết lập bán hàng](../selling/selling-settings.md#44-allow-multiple-sales-orders-against-a-customers-purchase-order)
* **Ngày Đơn mua hàng của Khách hàng**: Ngày mà Khách hàng đặt Đơn mua hàng.

![Chi tiết Đơn mua hàng](https://docs.erpnext.com/docs/v16/assets/img/accounts/purchase-order-details-in-invoice.png)

### 3.4 Địa chỉ và Liên hệ

* **Địa chỉ Khách hàng:** Đây là Địa chỉ thanh toán của Khách hàng.
* **Người liên hệ**: Nếu Khách hàng là một công ty, người cần liên hệ sẽ được lấy từ biểu mẫu [Khách hàng](../selling/customer-list.md) nếu đã được thiết lập.
* **Khu vực:** Khu vực địa lý của Khách hàng.