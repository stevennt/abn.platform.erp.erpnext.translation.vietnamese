<!-- add-breadcrumbs -->
# Hóa đơn mua hàng

**Hóa đơn mua hàng là hóa đơn bạn nhận được từ Nhà cung cấp mà bạn cần phải thực hiện thanh toán.**

Hóa đơn mua hàng hoàn toàn ngược lại với Hóa đơn bán hàng của bạn. Tại đây, bạn ghi nhận các chi phí cho Nhà cung cấp. Việc tạo Hóa đơn mua hàng rất giống với việc tạo Đơn mua hàng.

Để truy cập danh sách Hóa đơn mua hàng, hãy đi đến:
> Trang chủ > Kế toán > Phải trả người bán > Hóa đơn mua hàng

![PI Flow](https://docs.erpnext.com/docs/v16/assets/img/accounts/pi-flow.png)

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Hóa đơn mua hàng, bạn nên tạo các nội dung sau trước:

* [Mặt hàng](../stock/item.md)
* [Nhà cung cấp](../buying/supplier.md)
* [Đơn mua hàng](../buying/purchase-order.md)
* [Phiếu nhập hàng](../stock/purchase_receipt.md) (tùy chọn)

## 2. Cách tạo Hóa đơn mua hàng
Hóa đơn mua hàng thường được tạo từ Đơn mua hàng hoặc Phiếu nhập hàng. Thông tin chi tiết về Mặt hàng của Nhà cung cấp sẽ được lấy vào Hóa đơn mua hàng. Tuy nhiên, bạn cũng có thể tạo Hóa đơn mua hàng trực tiếp.

Để lấy thông tin tự động trong Hóa đơn mua hàng, hãy nhấp vào **Get Items from**. Thông tin có thể được lấy từ Đơn mua hàng hoặc Phiếu nhập hàng.

Để tạo thủ công, hãy làm theo các bước sau:

1. Đi tới danh sách Hóa đơn mua hàng, nhấp vào **New**.
2. Chọn Nhà cung cấp.
3. Ngày và giờ hạch toán sẽ được thiết lập theo thời gian hiện tại, bạn có thể chỉnh sửa sau khi tích vào ô kiểm bên dưới **Posting Time**.
4. Thiết lập Hạn thanh toán.
5. Thêm Mặt hàng và số lượng vào bảng Mặt hàng.
6. Đơn giá và Số tiền sẽ được lấy tự động.
7. **Lưu** và **Xác nhận**.

*Lưu ý trong phiên bản v16: Trước khi nhấn **Xác nhận**, bạn có thể sử dụng tính năng **Ledger Preview** để xem trước các bút toán (JE) sẽ được ghi nhận vào sổ cái, giúp đảm bảo tính chính xác của hạch toán.*

![Purchase Invoice](https://docs.erpnext.com/docs/v16/assets/img/accounts/purchase-invoice.png)

### 2.1 Các tùy chọn bổ sung khi tạo Hóa đơn mua hàng

* **Is Paid**: Bạn có thể tích vào 'Is Paid' nếu số tiền đã được thanh toán thông qua [Thanh toán trước](advance-payment-entry.md). Mục này nên được tích nếu có thanh toán toàn bộ hoặc một phần.
* **Is Return (Debit Note)**: Tích vào mục này nếu bạn trả lại Mặt hàng cho Nhà cung cấp. Để biết thêm chi tiết, hãy truy cập trang [Debit Note](debit-note.md).
* **Apply Tax Withholding Amount**: Nếu Nhà cung cấp được chọn có thiết lập Nhóm khấu trừ thuế, ô kiểm này sẽ được kích hoạt. Để biết thêm thông tin, hãy truy cập trang [Tax Withholding Category](tax-withholding-category.md).

### 2.2 Trạng thái

* **Draft**: Bản nháp đã được **Lưu** nhưng chưa được **Xác nhận** vào hệ thống.
* **Return**: Các Mặt hàng đã được trả lại cho Nhà cung cấp.
* **Debit Note Issued**: Các Mặt hàng đã được trả lại và một [Debit Note](debit-note.md) đã được lập cho hóa đơn.
* **Submitted**: Hóa đơn mua hàng đã được **Xác nhận** vào hệ thống và sổ cái đã được cập nhật.
* **Paid**: Số tiền hóa đơn đã được thanh toán cho Nhà cung cấp và một [Thanh toán](payment-entry.md) đã được **Xác nhận**.
* **Unpaid**: Hóa đơn mua hàng chưa được thanh toán.
* **Overdue**: Hạn thanh toán đã quá hạn.
* **Canceled**: Hóa đơn đã bị **Hủy** vì một lý do nào đó.

## 3. Tính năng

### 3.1 Chiều kế toán (Accounting Dimensions)
Chiều kế toán cho phép bạn gắn thẻ các giao dịch dựa trên một Khu vực, Chi nhánh, Khách hàng cụ thể, v.v. Điều này giúp xem các báo cáo kế toán riêng biệt dựa trên các tiêu chí đã chọn. Để biết thêm, hãy truy cập trang [Accounting Dimensions](accounting-dimensions.md).

> Lưu ý: Dự án và Trung tâm chi phí được mặc định coi là các chiều kế toán.

### 3.2 Tạm giữ Hóa đơn

Đôi khi bạn có thể cần tạm giữ một hóa đơn để nó không bị **Xác nhận**.

**Hold Invoice (Tạm giữ Hóa đơn)**: Bật hộp kiểm này để đưa Hóa đơn mua hàng vào trạng thái tạm giữ. Việc này chỉ có thể thực hiện trước khi **Xác nhận** hóa đơn. Khi 'Hold Invoice' được bật và Hóa đơn mua hàng đã được **Xác nhận**, trạng thái sẽ chuyển thành 'Temporarily on Hold' (Tạm thời bị tạm giữ).

![Purchase Invoice on Hold](https://docs.erpnext.com/docs/v16/assets/img/accounts/purchase-invoice-on-hold.png)

Sau khi hóa đơn mua hàng đã được **Xác nhận** và bạn muốn thay đổi 'Release Date' (Ngày phát hành), bạn có thể sử dụng nút 'Hold Invoice' ở góc trên bên phải.

Nếu bạn muốn tạm giữ hóa đơn mua hàng đã được **Xác nhận**, bạn có thể tạm giữ bằng tùy chọn 'Block Invoice' (Chặn hóa đơn) và nếu bạn muốn bỏ chặn, hãy sử dụng tùy chọn 'Unblock Invoice' (Bỏ chặn hóa đơn).

![Block PI](https://docs.erpnext.com/docs/v16/assets/img/accounts/purchase-invoice-block.png)

Đây là việc tạm giữ ở cấp độ hóa đơn, Nhà cung cấp cũng có thể bị đưa vào trạng thái tạm giữ. [Tìm hiểu thêm tại đây](../buying/supplier.md#23-credit-limit).

### 3.3 Chi tiết Hóa đơn của Nhà cung cấp

* **Supplier Invoice No (Số hóa đơn của Nhà cung cấp)**: Nhà cung cấp có thể định danh đơn hàng này bằng số riêng của họ. Đây là thông tin để tham chiếu.
* **Supplier Invoice Date (Ngày hóa đơn của Nhà cung cấp)**: Ngày mà Nhà cung cấp lập/xác nhận đơn hàng của bạn từ phía họ.

### 3.4 Địa chỉ và Liên hệ

* **Supplier Address (Địa chỉ Nhà cung cấp):** Đây là Địa chỉ thanh toán của Nhà cung cấp.
* **Contact Person (Người liên hệ)**: Nếu Nhà cung cấp là một Công ty, người cần liên hệ sẽ được lấy từ trường này nếu đã được thiết lập trong biểu mẫu [Nhà cung cấp](../buying/supplier.md).
* **Shipping Address (Địa chỉ giao hàng):** Địa chỉ nơi các mặt hàng sẽ được giao đến.

### 3.5 Tiền tệ và Bảng giá
Bạn có thể thiết lập loại tiền tệ mà đơn hàng Hóa đơn mua hàng sẽ được gửi đi. Thông tin này được lấy từ Đơn mua hàng. Nếu bạn thiết lập một Bảng giá, thì giá của mặt hàng sẽ được lấy từ bảng đó. Việc tích vào 'Ignore Pricing Rule' (Bỏ qua Quy tắc định giá) sẽ bỏ qua các [Quy tắc định giá](pricing-rule.md) đã được thiết lập.