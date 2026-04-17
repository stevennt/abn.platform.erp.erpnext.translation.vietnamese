<!-- add-breadcrumbs -->
# Hóa đơn mua hàng

**Hóa đơn mua hàng là hóa đơn bạn nhận được từ Nhà cung cấp mà bạn cần phải thực hiện thanh toán.**

Hóa đơn mua hàng hoàn toàn ngược lại với Hóa đơn bán hàng của bạn. Tại đây, bạn ghi nhận các chi phí cho Nhà cung cấp. Việc tạo Hóa đơn mua hàng rất giống với việc tạo Đơn mua hàng.

Để truy cập danh sách Hóa đơn mua hàng, hãy đi đến:
> Trang chủ > Kế toán > Phải trả người bán > Hóa đơn mua hàng

![PI Flow](https://docs.erpnext.com/docs/v13/assets/img/accounts/pi-flow.png)
## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Hóa đơn mua hàng, bạn nên tạo các nội dung sau trước:

* [Mặt hàng](../stock/item.md)
* [Nhà cung cấp](../buying/supplier.md)
* [Đơn mua hàng](../buying/purchase-order.md)
* [Phiếu nhập hàng](../stock/purchase-receipt.md) (tùy chọn)
## 2. Cách tạo Hóa đơn mua hàng:
Hóa đơn mua hàng thường được tạo từ Đơn mua hàng hoặc Phiếu nhập hàng. Thông tin chi tiết về Mặt hàng của Nhà cung cấp sẽ được lấy vào Hóa đơn mua hàng. Tuy nhiên, bạn cũng có thể tạo Hóa đơn mua hàng trực tiếp.

Để lấy thông tin tự động trong Hóa đơn mua hàng, hãy nhấp vào **Get Items from**. Thông tin có thể được lấy từ Đơn mua hàng hoặc Phiếu nhập hàng.

Để tạo thủ công, hãy làm theo các bước sau:

1. Đi tới danh sách Hóa đơn mua hàng, nhấp vào New.
1. Chọn Nhà cung cấp.
1. Ngày và giờ hạch toán sẽ được thiết lập theo thời gian hiện tại, bạn có thể chỉnh sửa sau khi tích vào ô kiểm bên dưới Posting Time.
1. Thiết lập Hạn thanh toán.
1. Thêm Mặt hàng và số lượng vào bảng Mặt hàng.
1. Đơn giá và Số tiền sẽ được lấy tự động.
1. Lưu và Xác nhận.

![Purchase Invoice](https://docs.erpnext.com/docs/v13/assets/img/accounts/purchase-invoice.png)

### 2.1 Các tùy chọn bổ sung khi tạo Hóa đơn mua hàng

* **Is Paid**: Bạn có thể tích vào 'Is Paid' nếu số tiền đã được thanh toán thông qua [Advance Payment Entry](advance-payment-entry.md). Mục này nên được tích nếu có thanh toán toàn bộ hoặc một phần.
* **Is Return (Debit Note)**: Tích vào mục này nếu khách hàng đã trả lại Mặt hàng. Để biết thêm chi tiết, hãy truy cập trang [Debit Note](debit-note.md).
* **Apply Tax Withholding Amount**: Nếu Nhà cung cấp được chọn có thiết lập Nhóm khấu trừ thuế, ô kiểm này sẽ được kích hoạt. Để biết thêm thông tin, hãy truy cập trang [Tax Withholding Category](tax-withholding-category.md).

### 2.2 Trạng thái

* **Draft**: Bản nháp đã được lưu nhưng chưa được xác nhận vào hệ thống.
* **Return**: Các Mặt hàng đã được trả lại cho Nhà cung cấp.
* **Debit Note Issued**: Các Mặt hàng đã được trả lại và một [Debit Note](debit-note.md) đã được lập cho hóa đơn.
* **Submitted**: Hóa đơn mua hàng đã được xác nhận vào hệ thống và sổ cái đã được cập nhật.
* **Paid**: Số tiền hóa đơn đã được thanh toán cho Nhà cung cấp và một [Payment Entry](payment-entry.md) đã được xác nhận.
* **Unpaid**: Hóa đơn mua hàng chưa được thanh toán.
* **Overdue**: Hạn thanh toán đã quá hạn.
* **Canceled**: Hóa đơn đã bị hủy vì một lý do nào đó.
## 3. Tính năng

### 3.1 Chiều kế toán (Accounting Dimensions)
Chiều kế toán cho phép bạn gắn thẻ các giao dịch dựa trên một Khu vực, Chi nhánh, Khách hàng cụ thể, v.v. Điều này giúp xem các báo cáo kế toán riêng biệt dựa trên các tiêu chí đã chọn. Để biết thêm, hãy truy cập trang [Accounting Dimensions](accounting-dimensions.md).

> Lưu ý: Dự án và Trung tâm chi phí được mặc định coi là các chiều kế toán.

### 3.2 Tạm giữ Hóa đơn

Đôi khi bạn có thể cần tạm giữ một hóa đơn để nó không bị Xác nhận.

**Hold Invoice (Tạm giữ Hóa đơn)**: Bật hộp kiểm này để đưa Hóa đơn mua hàng vào trạng thái tạm giữ. Việc này chỉ có thể thực hiện trước khi Xác nhận hóa đơn. Khi 'Hold Invoice' được bật và Hóa đơn mua hàng đã được Xác nhận, trạng thái sẽ chuyển thành 'Temporarily on Hold' (Tạm thời bị tạm giữ).

![Purchase Invoice on Hold](https://docs.erpnext.com/docs/v13/assets/img/accounts/purchase-invoice-on-hold.png)

Sau khi hóa đơn mua hàng đã được Xác nhận và bạn muốn thay đổi 'Release Date' (Ngày phát hành), bạn có thể sử dụng nút 'Hold Invoice' ở góc trên bên phải.

Nếu bạn muốn tạm giữ hóa đơn mua hàng đã được Xác nhận, bạn có thể tạm giữ bằng tùy chọn 'Block Invoice' (Chặn hóa đơn) và nếu bạn muốn bỏ chặn, hãy sử dụng tùy chọn 'Unblock Invoice' (Bỏ chặn hóa đơn).

![Block PI](https://docs.erpnext.com/docs/v13/assets/img/accounts/purchase-invoice-block.png)

Đây là việc tạm giữ ở cấp độ hóa đơn, Nhà cung cấp cũng có thể bị đưa vào trạng thái tạm giữ. [Tìm hiểu thêm tại đây](../buying/supplier.md#23-credit-limit).

### 3.3 Chi tiết Hóa đơn của Nhà cung cấp

* **Supplier Invoice No (Số hóa đơn của Nhà cung cấp)**: Nhà cung cấp có thể định danh đơn hàng này bằng số riêng của họ. Đây là thông tin để tham chiếu.
* **Supplier Invoice Date (Ngày hóa đơn của Nhà cung cấp)**: Ngày mà Nhà cung cấp lập/xác nhận đơn hàng của bạn từ phía họ.

### 3.4 Địa chỉ và Liên hệ

* **Supplier Address (Địa chỉ Nhà cung cấp):** Đây là Địa chỉ thanh toán của Nhà cung cấp.
* **Contact Person (Người liên hệ)**: Nếu Nhà cung cấp là một Công ty, người cần liên hệ sẽ được lấy từ trường này nếu đã được thiết lập trong biểu mẫu [Supplier](../buying/supplier.md).
* **Shipping Address (Địa chỉ giao hàng):** Địa chỉ nơi các mặt hàng sẽ được giao đến.

Tại Ấn Độ, các chi tiết sau có thể được ghi lại cho mục đích GST:

* Supplier GSTIN
* Place of Supply
* Company GSTIN

### 3.5 Tiền tệ và Bảng giá
Bạn có thể thiết lập loại tiền tệ mà đơn hàng Hóa đơn mua hàng sẽ được gửi đi. Thông tin này được lấy từ Đơn mua hàng. Nếu bạn thiết lập một Bảng giá, thì giá của mặt hàng sẽ được lấy từ bảng đó. Việc tích vào 'Ignore Pricing Rule' (Bỏ qua Quy tắc định giá) sẽ bỏ qua các [Pricing Rules](pricing-rule.md) đã được thiết lập trong Accounts > Pricing Rule.

![Purchase Invoice Price List](https://docs.erpnext.com/docs/v13/assets/img/accounts/purchase-invoice-price-list.png)

Đọc về [Price Lists](../stock/price-lists.md)
và [Multi-Currency Transactions](articles/managing-transactions-in-multiple-currency.md)
để biết thêm chi tiết.

### 3.6 Gia công hoặc 'Cung cấp nguyên vật liệu'

Thiết lập tùy chọn 'Supply Raw Materials' (Cung cấp nguyên vật liệu) rất hữu ích cho việc gia công, nơi bạn cung cấp nguyên vật liệu để sản xuất một Mặt hàng. Để biết thêm, hãy truy cập [trang Gia công](https://docs.erpnext.com/docs/v13/user/manual/en/manufacturing/subcontracting).

### 3.7 Bảng Mặt hàng

* **scan barcode (quét mã vạch)**: Bạn có thể thêm các Mặt hàng vào bảng Mặt hàng bằng cách quét mã vạch của chúng nếu bạn có máy quét mã vạch. Đọc tài liệu về [theo dõi mặt hàng bằng mã vạch](../stock/articles/track-items-using-barcode.md) để biết thêm.

* Mã Mặt hàng, tên, mô tả, Hình ảnh và Nhà sản xuất sẽ được lấy từ [danh mục Mặt hàng](../stock/item.md).

* **Manufacturer (Nhà sản xuất)**: Nếu Mặt hàng được sản xuất bởi một nhà sản xuất cụ thể, nó có thể được thêm vào đây. Thông tin này sẽ được lấy nếu đã được thiết lập trong danh mục Mặt hàng.

* **Quantity và Rate (Số lượng và Đơn giá)**: Khi bạn chọn mã Mặt hàng, tên, mô tả và Đơn vị tính (UOM) của nó sẽ được lấy ra. 'UOM Conversion Factor' (Hệ số chuyển đổi Đơn vị tính) được mặc định là 1, bạn có thể thay đổi tùy thuộc vào Đơn vị tính nhận được từ người bán, chi tiết hơn ở phần tiếp theo.

'Price List Rate' (Đơn giá Bảng giá) sẽ được lấy nếu một Đơn giá mua tiêu chuẩn đã được thiết lập. 'Last Purchase Rate' (Đơn giá mua gần nhất) hiển thị đơn giá của mặt hàng từ Đơn mua hàng gần nhất của bạn. Đơn giá được lấy nếu đã được thiết lập trong danh mục Mặt hàng. Bạn có thể đính kèm một Mẫu thuế Mặt hàng để áp dụng một mức thuế cụ thể cho mặt hàng đó.

* **Trọng lượng mặt hàng** sẽ được lấy nếu đã được thiết lập trong danh mục Mặt hàng, nếu không hãy nhập thủ công.

* **Discount on Price List Rate (Chiết khấu trên Đơn giá Bảng giá)**: Bạn có thể áp dụng chiết khấu cho từng Mặt hàng theo tỷ lệ phần trăm hoặc trên tổng số tiền của Mặt hàng. Đọc [Applying Discount](../selling/articles/applying-discount.md) để biết thêm chi tiết.

* **Item Weight (Trọng lượng mặt hàng)**: Chi tiết Trọng lượng mặt hàng trên mỗi đơn vị và Đơn vị tính trọng lượng sẽ được lấy nếu đã được thiết lập trong danh mục Mặt hàng, nếu không hãy nhập thủ công.

* **Accounting Details (Chi tiết kế toán)**: Tài khoản chi phí có thể được thay đổi tại đây nếu bạn muốn.

* **Deferred Expense (Chi phí hoãn lại)**: Nếu chi phí cho Mặt hàng này sẽ được lập hóa đơn thành nhiều phần trong các tháng tới, hãy tích vào 'Enable Deferred Expense' (Bật Chi phí hoãn lại). Để biết thêm, hãy truy cập [trang Chi phí hoãn lại](deferred-expense.md).

* **Allow Zero Valuation Rate (Cho phép Giá trị tính giá bằng 0)**: Tích vào 'Allow Zero Valuation Rate' sẽ cho phép Xác nhận Phiếu nhập hàng ngay cả khi Giá trị tính giá của Mặt hàng bằng 0. Đây có thể là một mặt hàng mẫu hoặc do thỏa thuận chung với Nhà cung cấp của bạn.

* **BOM**: Nếu có [Định mức nguyên vật liệu](https://docs.erpnext.com/docs/v13/user/manual/en/manufacturing/bill-of-materials) được tạo cho Mặt hàng, nó sẽ được lấy tại đây. Điều này hữu ích để tham chiếu khi [gia công](https://docs.erpnext.com/docs/v13/user/manual/en/manufacturing/subcontracting).

* **Item Tax Template (Mẫu thuế Mặt hàng)**: Bạn có thể thiết lập một Mẫu thuế Mặt hàng để áp dụng một mức Thuế cụ thể cho Mặt hàng này. Để biết thêm, hãy truy cập [trang này](item-tax-template.md).

* **Page Break (Ngắt trang)** sẽ tạo một điểm ngắt trang ngay trước Mặt hàng này khi in.

#### Cập nhật Kho

> Lưu ý: Từ phiên bản 13 trở đi, chúng tôi đã giới thiệu sổ cái bất biến (immutable ledger), điều này thay đổi các quy tắc về việc Hủy các phiếu kho và ghi sổ các giao dịch kho lùi ngày trong ERPNext. [Tìm hiểu thêm tại đây](articles/immutable-ledger-in-erpnext.md).

**Update Stock (Cập nhật Kho)**
## 4. Thêm
### 4.1 Ảnh hưởng kế toán
Tương tự như Hóa đơn bán hàng, trong Hóa đơn mua hàng, bạn phải nhập một tài khoản Chi phí hoặc tài khoản Tài sản cho mỗi dòng trong bảng Mặt hàng. Điều này giúp chỉ định xem Mặt hàng đó là Tài sản hay Chi phí. Bạn cũng có thể thay đổi Trung tâm chi phí. Những thông tin này cũng có thể được thiết lập trong danh mục Mặt hàng. Trung tâm chi phí có thể được thiết lập ở cấp Công ty.

Hóa đơn mua hàng sẽ ảnh hưởng đến các tài khoản của bạn như sau:

* Các bút toán kế toán (GL Entry) cho một giao dịch "mua hàng" ghi sổ kép điển hình:
* Nợ:
 * Chi phí hoặc Tài sản (tổng ròng, chưa bao gồm thuế)
 * Thuế (/tài sản nếu là loại VAT hoặc lại là chi phí)
* Có:
 * Nhà cung cấp

![Purchase Invoice Ledger](https://docs.erpnext.com/docs/v13/assets/img/accounts/purchase-invoice-ledger.png)

### 4.2 Kế toán khi chọn **Is Paid**
Nếu **Is Paid** được chọn, ERPNext cũng sẽ thực hiện các bút toán kế toán sau:

Nợ:

 * Nhà cung cấp

Có:

 * Tài khoản Ngân hàng/Tiền mặt

Để xem các bút toán trong Hóa đơn mua hàng sau khi bạn "Xác nhận", hãy nhấp vào "View Ledger".

### 4.3 Mua hàng là "Chi phí" hay "Tài sản"?

Nếu Mặt hàng được tiêu dùng ngay lập tức khi mua, hoặc nếu đó là một dịch vụ, thì việc mua hàng đó trở thành "Chi phí". Ví dụ, hóa đơn điện thoại hoặc hóa đơn công tác phí là "Chi phí" - vì chúng đã được tiêu dùng.

Đối với các Mặt hàng tồn kho có giá trị, các giao dịch mua này chưa phải là "Chi phí", vì chúng vẫn có giá trị khi còn nằm trong kho của bạn. Chúng là "Tài sản". Nếu chúng là nguyên vật liệu (được sử dụng trong một quy trình), chúng sẽ trở thành "Chi phí" ngay khi chúng được tiêu dùng trong quy trình đó. Nếu chúng được bán cho Khách hàng, chúng trở thành "Chi phí" khi bạn giao hàng cho Khách hàng.

### 4.4 Khấu trừ thuế tại nguồn

Ở nhiều quốc gia, luật pháp có thể yêu cầu bạn khấu trừ thuế khi thanh toán cho nhà cung cấp. Các khoản thuế này có thể dựa trên một mức thuế suất tiêu chuẩn. Theo các loại hình này, thông thường nếu một Nhà cung cấp vượt qua một ngưỡng thanh toán nhất định, và nếu loại sản phẩm đó chịu thuế, bạn có thể phải khấu trừ một phần thuế (khoản thuế mà bạn sẽ nộp lại cho chính phủ thay mặt cho Nhà cung cấp).

Để thực hiện việc này, bạn sẽ phải tạo một Tài khoản Thuế mới dưới mục "Tax Liabilities" (Nợ thuế) hoặc tương tự và ghi Có vào Tài khoản này theo tỷ lệ phần trăm mà bạn có nghĩa vụ phải khấu trừ cho mỗi giao dịch.

### 4.5 Tạm dừng thanh toán cho Hóa đơn mua hàng
Có hai cách để tạm dừng một hóa đơn mua hàng:

- Tạm dừng theo khoảng thời gian (Date Span Hold)
- Tạm dừng rõ ràng (Explicit Hold)

#### Tạm dừng rõ ràng (Explicit Hold)
Tạm dừng rõ ràng sẽ giữ hóa đơn mua hàng vô thời hạn.
Để thực hiện, trong phần "Hold Invoice" của biểu mẫu hóa đơn mua hàng, chỉ cần tích vào ô "Hold Invoice". Trong trường văn bản "Reason For Putting On Hold", hãy nhập một lời giải thích lý do tại sao hóa đơn cần được tạm dừng.

Nếu bạn cần tạm dừng một hóa đơn đã được Xác nhận, hãy nhấp vào nút "Make" và nhấp vào "Block Invoice". Đồng thời, hãy thêm một lời giải thích lý do tại sao hóa đơn cần được tạm dừng trong hộp thoại hiện ra và nhấp "Lưu".

#### Tạm dừng theo khoảng thời gian (Date Span Hold)
Tạm dừng theo khoảng thời gian sẽ giữ hóa đơn mua hàng cho đến một ngày cụ thể. Để thực hiện, trong phần "Hold Invoice" của biểu mẫu hóa đơn mua hàng, hãy tích vào ô "Hold Invoice". Tiếp theo, nhập ngày giải tỏa (release date) trong hộp thoại hiện ra và nhấp "Lưu". Ngày giải tỏa là ngày mà lệnh tạm dừng tài liệu hết hạn.

Sau khi hóa đơn đã được Lưu, bạn có thể thay đổi ngày giải tỏa bằng cách nhấp vào nút thả xuống "Hold Invoice" và sau đó chọn "Change Release Date". Thao tác này sẽ làm xuất hiện một hộp thoại.

![Purchase Invoice on hold](https://docs.erpnext.com/docs/v13/assets/img/accounts/purchase-invoice-hold.png)

Chọn ngày giải tỏa mới và nhấp "Lưu". Bạn cũng nên nhập một lời giải thích trong trường "Reason For Putting On Hold".

Lưu ý các điều sau:

- Tất cả các giao dịch mua hàng đã được tạm dừng sẽ không được bao gồm trong bảng tham chiếu của Bút toán thanh toán.
- Ngày giải tỏa không được là một ngày trong quá khứ.
- Bạn chỉ có thể chặn hoặc bỏ chặn hóa đơn mua hàng nếu nó chưa được thanh toán.
- Bạn chỉ có thể thay đổi ngày giải tỏa nếu hóa đơn chưa được thanh toán.

### 5. Các chủ đề liên quan
1. [Sales Invoice](sales-invoice.md)
1. [Item Wise Taxation](item-tax-template.md)
1. [Payment Entry](payment-entry.md)
1. [Payment Request](payment-request.md)
1. [Request For Quotation](../buying/request-for-quotation.md)
1. [Purchase Order](../buying/purchase-order.md)
1. [Purchase Receipt](../stock/purchase-receipt.md)

{next}