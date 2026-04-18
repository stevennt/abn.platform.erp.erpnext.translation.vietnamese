<!-- add-breadcrumbs -->
# Phiếu giao hàng

**Phiếu giao hàng được lập khi một lô hàng được vận chuyển từ Kho của công ty đến Khách hàng.**

Một bản sao của Phiếu giao hàng thường được gửi kèm với đơn vị vận chuyển. Phiếu giao hàng bao gồm danh sách các Mặt hàng được gửi trong lô hàng và cập nhật tồn kho. Phiếu giao hàng là một bước tùy chọn và Hóa đơn bán hàng có thể được tạo trực tiếp từ Đơn bán hàng.

Để truy cập danh sách Phiếu giao hàng, hãy đi đến:
> Home > Stock > Stock Transactions > Delivery Note

![Delivery Note flow](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/delivery-note-flow.png)


## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Phiếu giao hàng, bạn nên tạo các chứng từ sau trước:

* [Sales Order](../selling/sales-order.md)

> Lưu ý: Từ phiên bản 16, hệ thống sử dụng sổ cái bất biến (immutable ledger), điều này thay đổi các quy tắc về việc hủy các phiếu kho và ghi sổ các giao dịch kho lùi ngày trong ERPNext. [Tìm hiểu thêm tại đây](../accounts/articles/immutable-ledger-in-erpnext.md).

## 2. Cách tạo Phiếu giao hàng
Việc nhập Phiếu giao hàng rất giống với Phiếu nhập hàng. Nó thường được tạo từ một Đơn bán hàng đã "Xác nhận" (chưa được giao hàng) bằng cách nhấp vào Create > Delivery.

Để tạo Phiếu giao hàng một cách _thủ công_ (không được khuyến khích), hãy làm theo các bước sau:

1. Đi đến danh sách Phiếu giao hàng, nhấp vào New.
1. Thông tin Khách hàng và Mặt hàng có thể được lấy bằng cách nhấp vào 'Get Items from > Sales Order'.
1. Đơn vị tính (UOM) và Đơn giá sẽ được tự động lấy về.
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Delivery Note" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/delivery-note.png">

Để lấy các Mặt hàng từ một Đơn bán hàng, hãy nhấp vào Get Items from > Sales Order. Thao tác này sẽ mở một cửa sổ bật lên để bạn có thể tìm kiếm và chọn một Đơn bán hàng.

Bạn sẽ nhận thấy rằng tất cả thông tin về các Mặt hàng chưa được giao và các chi tiết khác sẽ được chuyển sang từ Đơn bán hàng nếu bạn tạo Phiếu giao hàng từ đó.

Bạn cũng có thể chỉnh sửa ngày và giờ ghi sổ, ngày và giờ hiện tại sẽ được thiết lập khi bạn tạo Phiếu giao hàng.


### 2.1 Trạng thái

Đây là các trạng thái mà một Phiếu giao hàng có thể có:

* **Draft**: Bản nháp đã được Lưu nhưng chưa được Xác nhận vào hệ thống.
* **To Bill**: Chưa được lập [Hóa đơn bán hàng](../accounts/sales-invoice.md).
* **Completed**: Đã Xác nhận và đã gửi tất cả các Mặt hàng.
* **Return Issued**: Tất cả các Mặt hàng đã được trả lại.
* **Cancelled**: Đã Hủy Phiếu giao hàng.
* **Closed**: Mục đích của việc Đóng là để quản lý việc đóng sớm đơn hàng. Ví dụ: Khách hàng đặt 20 số lượng nhưng chốt ở mức 15 số lượng. 5 số lượng còn lại sẽ không được gửi hoặc lập hóa đơn.

### 2.2 Giao hàng từng phần và Giữ hàng (Stock Reservation)

Khi bạn tạo Phiếu giao hàng từ một Đơn bán hàng, số lượng có thể được thay đổi. Vì vậy, nếu Đơn bán hàng chứa 10 Mặt hàng cần giao và bạn chỉ giao 5 mặt hàng trong tuần này và số còn lại vào tuần sau, thì bạn có thể tạo 2 Phiếu giao hàng trong hai tuần.

Trong phiên bản 16, hệ thống hỗ trợ **Stock Reservation System** (Hệ thống giữ hàng), giúp đảm bảo các Mặt hàng đã được cam kết trong Đơn bán hàng sẽ được giữ lại trong Kho để phục vụ việc giao hàng, tránh việc các đơn hàng khác lấy mất số lượng này.


## 3. Các hành động liên quan
### 3.1 Chi tiết Đơn mua hàng của Khách hàng
Bạn có thể nhập số Đơn mua hàng của Khách hàng tại đây để tham chiếu.

### 3.2 Địa chỉ và Liên hệ
* **Shipping Address**: Địa chỉ của Khách hàng nơi các Mặt hàng sẽ được giao đến.
* **Contact Person**: Nếu Khách hàng là một tổ chức, hãy thêm người liên hệ vào trường này.

Đối với Ấn Độ, các chi tiết sau có thể được thêm cho GST:

* Customer GSTIN
* Place of Supply
* Billing Address GSTIN
* Company GSTIN
* Company Address Name

[Contacts](https://docs.erpnext.com/docs/v16/user/manual/en/CRM/contact) và [Addresses](https://docs.erpnext.com/docs/v16/user/manual/en/CRM/address) được lưu trữ riêng biệt để bạn có thể đính kèm nhiều Liên hệ hoặc Địa chỉ cho khách hàng.

### 3.3 Tiền tệ và Bảng giá
Bạn có thể thiết lập tiền tệ mà Phiếu giao hàng sẽ được gửi. Thông tin này thường được lấy từ Đơn bán hàng nếu đã được thiết lập. Nếu bạn thiết lập một Bảng giá, thì giá mặt hàng sẽ được lấy từ bảng đó. Việc tích vào Ignore Pricing Rule sẽ bỏ qua các Quy tắc định giá đã được thiết lập trong Accounts > Pricing Rule.

Đọc về [Price Lists](price-lists.md)
và [Multi-Currency Transactions](../accounts/articles/managing-transactions-in-multiple-currency.md)
để biết thêm chi tiết.

### 3.4 Kho và Kiểm soát Tồn kho
* **Set Source Warehouse**: Đây là nơi các Mặt hàng sẽ được lấy ra để gửi cho Khách hàng.
* **To Warehouse**: Trong kịch bản Bán hàng thông thường, Mặt hàng sẽ rời khỏi Kho của bạn và đến tay Khách hàng. Tuy nhiên, nếu bạn muốn giữ lại kho hàng mẫu, hãy nhập một Kho tại đây.

Trong phiên bản 16, việc quản lý kho được nâng cao với khả năng **Item-Level Stock Accounting** (Kế toán tồn kho theo từng Mặt hàng), giúp việc theo dõi giá trị tồn kho chính xác hơn khi thực hiện các giao dịch kho.

### 3.5 Bảng Mặt hàng
* **Barcode**: Bạn có thể theo dõi các Mặt hàng bằng cách sử dụng [mã vạch](articles/track-items-using-barcode.md).

* **Truy xuất nguồn gốc (Traceability)**: Với các Mặt hàng có quản lý theo [Lô hàng (Batch)](batch.md) hoặc Số sê-ri (Serial Number), bạn có thể sử dụng [Báo cáo truy xuất nguồn gốc Lô hàng/Số sê-ri](stock/serial-batch-traceability-report.md) để kiểm soát chính xác dòng chảy của hàng hóa.

* Mã Mặt hàng, tên, mô tả, Hình ảnh và Nhà sản xuất sẽ được lấy từ [danh mục Mặt hàng](item.md).

* **Scan Barcode**: Bạn có thể thêm các Mặt hàng vào bảng Mặt hàng bằng cách quét mã vạch nếu bạn có máy quét mã vạch. Đọc tài liệu về [theo dõi mặt hàng bằng mã vạch](articles/track-items-using-barcode.md) để biết thêm.

* **Discount và Margin**: Bạn có thể áp dụng chiết khấu cho từng Mặt hàng theo tỷ lệ phần trăm hoặc trên tổng số tiền của Mặt hàng đó. Đọc [Applying Discount](../selling/articles/applying-discount.md) để biết thêm chi tiết.

* **Rate**: Đơn giá được lấy nếu đã được thiết lập trong [Bảng giá](price-lists.md) và tổng Số tiền được tính toán.

* **Item Tax Template**: Bạn có thể thiết lập một Mẫu thuế Mặt hàng để áp dụng một mức Thuế cụ thể cho Mặt hàng này. Để biết thêm, hãy truy cập [trang này](../accounts/item-tax-template.md).

* Chi tiết Trọng lượng của Mặt hàng trên mỗi đơn vị và Đơn vị tính Trọng lượng sẽ được lấy nếu đã được thiết lập trong danh mục Mặt hàng.

* **Ledger Preview**: Trong phiên bản 16, bạn có thể xem trước các bút toán liên quan trực tiếp từ giao dịch để đảm bảo tính chính xác của kế toán kho và kế toán doanh thu.