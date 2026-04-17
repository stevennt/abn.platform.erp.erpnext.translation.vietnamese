<!-- add-breadcrumbs -->
# Hóa đơn bán hàng

**Hóa đơn bán hàng là hóa đơn mà bạn gửi cho Khách hàng để Khách hàng thực hiện thanh toán.**

Hóa đơn bán hàng là một giao dịch kế toán. Khi Xác nhận Hóa đơn bán hàng, hệ thống sẽ cập nhật các khoản phải thu và ghi nhận thu nhập vào Tài khoản Khách hàng.

Để truy cập danh sách Hóa đơn bán hàng, hãy đi tới:
> Home > Accounting > Accounts Receivable > Sales Invoice

![SO Flow](/docs/v13/assets/img/accounts/so-flow.png)
## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Hóa đơn bán hàng, bạn nên tạo các thông tin sau trước:

* [Mặt hàng](/docs/v13/user/manual/en/stock/item)
* [Khách hàng](/docs/v13/user/manual/en/CRM/customer)

* Tùy chọn:
 * [Đơn bán hàng](/docs/v13/user/manual/en/selling/sales-order)
 * [Phiếu giao hàng](/docs/v13/user/manual/en/stock/delivery-note)
## 2. Cách tạo Hóa đơn bán hàng
Hóa đơn bán hàng thường được tạo từ Đơn bán hàng hoặc Phiếu giao hàng. Chi tiết Mặt hàng của Khách hàng sẽ được lấy vào Hóa đơn bán hàng. Tuy nhiên, bạn cũng có thể tạo Hóa đơn bán hàng trực tiếp, ví dụ như hóa đơn POS.

Để lấy thông tin tự động trong Hóa đơn bán hàng, hãy nhấp vào **Get Items from**. Thông tin có thể được lấy từ Đơn bán hàng, Phiếu giao hàng hoặc Báo giá.

Để tạo thủ công, hãy làm theo các bước sau:

1. Đi tới danh sách Hóa đơn bán hàng và nhấp vào New.
1. Chọn Khách hàng.
1. Thiết lập Ngày đến hạn thanh toán.
1. Trong bảng Mặt hàng, chọn các Mặt hàng và thiết lập số lượng.
1. Giá sẽ được lấy tự động nếu [Item Price](/docs/v13/user/manual/en/stock/item-price) được thêm vào, nếu không hãy thêm giá vào bảng.
1. Ngày và giờ ghi sổ sẽ được thiết lập theo thời gian hiện tại, bạn có thể chỉnh sửa sau khi tích vào ô kiểm bên dưới Posting Time để tạo một bút toán lùi ngày.
1. Lưu và Xác nhận.
 ![New Sales Invoice](/docs/v13/assets/img/accounts/new-sales-invoice.png)

### 2.1 Các tùy chọn bổ sung khi tạo Hóa đơn bán hàng

* **Include Payment (POS)**: Nếu hóa đơn này dành cho bán lẻ / Điểm bán hàng. [Tìm hiểu thêm tại đây](/docs/v13/user/manual/en/accounts/sales-invoice#324-pos-invoices).
* **Is Return Credit Note**: Tích vào đây nếu khách hàng đã trả lại Mặt hàng. Để biết thêm chi tiết, hãy truy cập trang [Credit Note](/docs/v13/user/manual/en/accounts/credit-note).

![POS and Credit Note Options](/docs/v13/assets/img/accounts/pos-and-credit-note-in-sales-invoice.png)

Dành cho Ấn Độ:
**e-Way Bill No**: Theo quy định của GST, đơn vị vận chuyển cần mang theo e-Way Bill. Để biết cách tạo e-Way Bill, [hãy truy cập trang này](/docs/v13/user/manual/en/regional/india/auto-generate-e-way-bill-JSON).

### 2.2 Trạng thái

Đây là các trạng thái được tự động gán cho Hóa đơn bán hàng.

* **Draft**: Bản nháp đã được lưu nhưng chưa được xác nhận.
* **Submitted**: Hóa đơn đã được xác nhận vào hệ thống và sổ cái đã được cập nhật.
* **Paid**: Khách hàng đã thực hiện thanh toán và một [Bút toán thanh toán](/docs/v13/user/manual/en/accounts/payment-entry) đã được xác nhận.
* **Unpaid**: Hóa đơn đã được tạo nhưng việc thanh toán đang chờ xử lý và vẫn trong hạn thanh toán.
* **Overdue**: Việc thanh toán đang chờ xử lý và đã quá hạn thanh toán.
* **Canceled**: Hóa đơn bán hàng đã bị hủy vì bất kỳ lý do gì. Khi một hóa đơn bị hủy, các tác động của nó đối với Tài khoản và Kho sẽ được hoàn tác.
* **Credit Note Issued**: Mặt hàng được trả lại bởi Khách hàng và một [Credit Note](/docs/v13/user/manual/en/accounts/credit-note) được tạo cho hóa đơn này.
* **Return**: Trạng thái này được gán cho Credit Note được tạo đối với Hóa đơn bán hàng gốc. Tuy nhiên, bạn cũng có thể tạo một Credit Note độc lập.
* **Unpaid and Discounted**: Việc thanh toán đang chờ xử lý và bất kỳ gói đăng ký đang diễn ra nào đã được chiết khấu bằng cách sử dụng [Invoice Discounting](/docs/v13/user/manual/en/accounts/invoice_discounting).
* **Overdue and Discounted**: Việc thanh toán đang chờ xử lý và đã quá hạn thanh toán, đồng thời bất kỳ gói đăng ký đang diễn ra nào đã được chiết khấu bằng cách sử dụng [Invoice Discounting](/docs/v13/user/manual/en/accounts/invoice_discounting).
## 3. Tính năng
### 3.1 Ngày tháng

* **Ngày hạch toán (Posting Date)**: Ngày mà Hóa đơn bán hàng sẽ ảnh hưởng đến sổ sách kế toán của bạn, tức là Sổ cái. Điều này sẽ ảnh hưởng đến tất cả các số dư của bạn trong kỳ kế toán đó.

* **Hạn thanh toán (Due Date)**: Ngày mà khoản thanh toán đến hạn (nếu bạn bán hàng trả chậm). Hạn mức tín dụng có thể được thiết lập từ danh mục [Khách hàng](/docs/v13/user/manual/en/CRM/customer#24-credit-limit-and-payment-terms).

### 3.2 Chiều kế toán (Accounting Dimensions)
Chiều kế toán cho phép bạn gắn thẻ các giao dịch dựa trên một Khu vực, Chi nhánh, Khách hàng cụ thể, v.v. Điều này giúp xem các báo cáo kế toán riêng biệt dựa trên (các) chiều đã chọn. Để biết thêm, hãy xem trợ giúp về tính năng [Chiều kế toán](/docs/v13/user/manual/en/accounts/accounting-dimensions).

> Lưu ý: Dự án và Trung tâm chi phí được mặc định coi là các chiều kế toán.

### 3.3 Chi tiết Đơn mua hàng của Khách hàng

* **Đơn mua hàng của Khách hàng (Customer's Purchase Order)**: Theo dõi số Đơn mua hàng của khách hàng nhận được, chủ yếu để ngăn chặn việc tạo trùng Đơn bán hàng hoặc Hóa đơn cho cùng một Đơn mua hàng nhận được từ Khách hàng. Bạn có thể cấu hình thêm các thiết lập liên quan đến việc xác thực số Đơn mua hàng của khách hàng trong [Thiết lập bán hàng](/docs/v13/user/manual/en/selling/selling-settings#44-allow-multiple-sales-orders-against-a-customers-purchase-order)
* **Ngày Đơn mua hàng của Khách hàng**: Ngày mà Khách hàng đặt Đơn mua hàng.

![Chi tiết Đơn mua hàng](/docs/v13/assets/img/accounts/purchase-order-details-in-invoice.png)

### 3.4 Địa chỉ và Liên hệ

* **Địa chỉ Khách hàng:** Đây là Địa chỉ thanh toán của Khách hàng.
* **Người liên hệ**: Nếu Khách hàng là một công ty, người cần liên hệ sẽ được lấy từ biểu mẫu [Khách hàng](/docs/v13/user/manual/en/CRM/customer) nếu đã được thiết lập.
* **Khu vực:** [Khu vực](/docs/v13/user/manual/en/selling/territory) là vùng mà Khách hàng thuộc về, được lấy từ biểu mẫu Khách hàng. Giá trị mặc định là Tất cả khu vực.
* **Địa chỉ giao hàng:** Địa chỉ nơi các mặt hàng sẽ được giao đến.

Đối với Ấn Độ, các chi tiết sau có thể được ghi lại cho mục đích GST. Bạn có thể ghi lại các chi tiết này trong danh mục Địa chỉ và Khách hàng, chúng sẽ được lấy vào Hóa đơn bán hàng.

* GSTIN của Địa chỉ thanh toán
* GSTIN của Khách hàng
* Địa điểm cung ứng
* GSTIN của Công ty

### 3.5 Tiền tệ
Bạn có thể thiết lập loại tiền tệ mà đơn hàng Hóa đơn bán hàng sẽ được gửi đi. Thông tin này có thể được lấy từ danh mục Khách hàng hoặc các giao dịch trước đó như Đơn bán hàng.

* Chọn tiền tệ của Khách hàng chỉ để tham chiếu cho Khách hàng, trong khi việc hạch toán kế toán sẽ chỉ được thực hiện bằng tiền tệ cơ sở của Công ty. Tìm hiểu thêm [tại đây](/docs/v13/user/manual/en/accounts/articles/managing-transactions-in-multiple-currency).
* Duy trì tài khoản phải thu riêng biệt bằng tiền tệ của Khách hàng. Khoản phải thu cho hóa đơn này sẽ được hạch toán bằng chính loại tiền tệ đó. Đọc [Kế toán đa tiền tệ](/docs/v13/user/manual/en/accounts/multi-currency-accounting) để tìm hiểu thêm.

### 3.6 Bảng giá

Nếu bạn chọn một Bảng giá, thì giá của mặt hàng sẽ được lấy từ bảng đó. Việc tích vào 'Bỏ qua Quy tắc định giá' sẽ bỏ qua các [Quy tắc định giá](/docs/v13/user/manual/en/accounts/pricing-rule) được thiết lập trong Kế toán > Quy tắc định giá.

Đọc [tài liệu Bảng giá](/docs/v13/user/manual/en/stock/price-lists) để biết thêm.


### 3.7 Bảng Mặt hàng

> Lưu ý: Từ phiên bản 13 trở đi, chúng tôi đã giới thiệu sổ cái bất biến (immutable ledger), thay đổi các quy tắc về việc hủy phiếu kho và hạch toán các giao dịch kho lùi ngày trong ERPNext. [Tìm hiểu thêm tại đây](/docs/v13/user/manual/en/accounts/articles/immutable-ledger-in-erpnext).

#### Cập nhật Kho
Tích vào ô này sẽ cập nhật Sổ kho khi Xác nhận Hóa đơn bán hàng. Nếu bạn đã tạo Phiếu giao hàng, Sổ kho sẽ được thay đổi. Nếu bạn **bỏ qua** việc tạo Phiếu giao hàng, hãy tích vào ô này.

* **quét mã vạch**: Bạn có thể thêm các Mặt hàng vào bảng Mặt hàng bằng cách quét mã vạch của chúng nếu bạn có máy quét mã vạch. Đọc tài liệu về [theo dõi mặt hàng bằng mã vạch](/docs/v13/user/manual/en/stock/articles/track-items-using-barcode) để biết thêm.

* Mã mặt hàng, tên, mô tả, Hình ảnh và Nhà sản xuất sẽ được lấy từ [danh mục Mặt hàng](/docs/v13/user/manual/en/stock/item).

* **Chiết khấu và Biên lợi nhuận**: Bạn có thể áp dụng chiết khấu cho từng Mặt hàng theo tỷ lệ phần trăm hoặc trên tổng số tiền của Mặt hàng. Đọc [Áp dụng Chiết khấu](/docs/v13/user/manual/en/selling/articles/applying-discount) để biết thêm chi tiết.

* **Đơn giá**: Đơn giá sẽ được lấy nếu đã được thiết lập trong [Bảng giá](/docs/v13/user/manual/en/stock/price-lists) và Tổng số tiền sẽ được tính toán.

* **Giao hàng thả (Drop Ship)**: Drop Shipping là khi bạn thực hiện giao dịch bán hàng, nhưng Mặt hàng lại được giao bởi Nhà cung cấp. Để biết thêm, hãy truy cập trang [Giao hàng thả](/docs/v13/user/manual/en/selling/articles/drop-shipping).

* **Chi tiết kế toán**: Các tài khoản Thu nhập và Chi phí có thể được thay đổi tại đây nếu bạn muốn. Nếu Mặt hàng này là một [Tài sản](/docs/v13/user/manual/en/asset/asset), nó có thể được liên kết tại đây. Điều này hữu ích khi bạn [bán một Tài sản](/docs/v13/user/manual/en/asset/selling-an-asset).

* **Doanh thu hoãn lại**: Nếu doanh thu cho Mặt hàng này sẽ được lập hóa đơn thành nhiều phần trong các tháng tới, hãy tích vào 'Bật Doanh thu hoãn lại'. Để biết thêm, hãy truy cập [trang Doanh thu hoãn lại](/docs/v13/user/manual/en/accounts/deferred-revenue).

* **Trọng lượng mặt hàng**: Chi tiết Trọng lượng mặt hàng trên mỗi đơn vị và Đơn vị tính Trọng lượng sẽ được lấy nếu đã được thiết lập trong danh mục Mặt hàng.

* **Chi tiết kho**: Các chi tiết sau sẽ được lấy từ danh mục Mặt hàng:
 * **Kho**: Kho nơi hàng sẽ được xuất đi.
 * **Số lượng hiện có tại Kho**: Số lượng hiện có trong Kho đã chọn.

* **Số Lô và Số serial**: Nếu Mặt hàng của bạn có số serial hoặc theo lô, bạn sẽ phải nhập [Số serial](/docs/v13/user/manual/en/stock/serial-no) và [Lô hàng](/docs/v13/user/manual/en/stock/batch) trong bảng Mặt hàng. Bạn được phép nhập nhiều Số serial trong một dòng (mỗi số trên một dòng riêng biệt) và bạn phải nhập cùng một số lượng Số serial.
## 4. Thêm
### Tác động kế toán

Tất cả các giao dịch Bán hàng phải được hạch toán vào một "Tài khoản thu nhập" (Income Account). Đây là một Tài khoản nằm trong phần "Thu nhập" (Income) trong Hệ thống tài khoản của bạn. Một thói quen tốt là phân loại thu nhập theo loại (như thu nhập từ sản phẩm, thu nhập từ dịch vụ, v.v.). Tài khoản thu nhập phải được thiết lập cho từng dòng trong bảng Mặt hàng.

> Mẹo: Để thiết lập Tài khoản thu nhập mặc định cho các Mặt hàng, bạn có thể thiết lập trong Mặt hàng hoặc Nhóm mặt hàng.

Tài khoản khác bị ảnh hưởng là Tài khoản của Khách hàng. Tài khoản này được thiết lập tự động từ mục “Debit To” trong phần tiêu đề.

Bạn cũng có thể chỉ định các Trung tâm chi phí mà Thu nhập của bạn phải được hạch toán vào. Hãy nhớ rằng các Trung tâm chi phí sẽ cho bạn biết khả năng sinh lời của các dòng kinh doanh hoặc sản phẩm khác nhau. Bạn cũng có thể thiết lập Trung tâm chi phí mặc định trong danh mục Mặt hàng. Xem thêm: [Accounting Dimensions](/docs/v13/user/manual/en/accounts/accounting-dimensions).

### Các bút toán (Bút toán sổ cái) cho một giao dịch "Bán hàng" ghi sổ kép điển hình:
Khi hạch toán một giao dịch bán hàng (theo cơ chế dồn tích):

* **Nợ:** Khách hàng (tổng cộng)
* **Có:** Thu nhập (tổng ròng, trừ thuế cho mỗi Mặt hàng)
* **Có:** Thuế (các khoản nợ phải trả cho chính phủ)

 ![SI Ledger](/docs/v13/assets/img/accounts/ledger-updates-on-sales-invoice-submission.png)

> Để xem các bút toán trong Hóa đơn bán hàng sau khi bạn "Xác nhận", hãy nhấp vào "View Ledger".
## 5. Các chủ đề liên quan
1. [Trung tâm chi phí](/docs/v13/user/manual/en/accounts/cost-center)
1. [Bút toán](/docs/v13/user/manual/en/accounts/journal-entry)
1. [Bút toán thanh toán](/docs/v13/user/manual/en/accounts/payment-entry)
1. [Hóa đơn mua hàng](/docs/v13/user/manual/en/accounts/purchase-invoice)
1. [Phiếu nhập hàng](/docs/v13/user/manual/en/stock/purchase-receipt)
1. [Thuế theo từng mặt hàng](/docs/v13/user/manual/en/accounts/item-tax-template)
1. [Đơn bán hàng](/docs/v13/user/manual/en/selling/sales-order)
1. [Báo giá](/docs/v13/user/manual/en/selling/quotation)
1. [Phiếu giao hàng](/docs/v13/user/manual/en/stock/delivery-note)

{next}