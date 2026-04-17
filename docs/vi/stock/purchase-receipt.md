<!-- add-breadcrumbs -->
# Phiếu nhập hàng

**Phiếu nhập hàng được lập khi bạn chấp nhận các Mặt hàng từ Nhà cung cấp, thường là dựa trên một Đơn mua hàng.**

Bạn cũng có thể lập Phiếu nhập hàng trực tiếp mà không cần Đơn mua hàng. Để làm điều này, hãy thiết lập Purchase Order Required thành “No” trong Cài đặt mua hàng (Buying Settings).

Để truy cập danh sách Phiếu nhập hàng, hãy đi đến:
> Home > Stock > Stock Transactions > Purchase Receipt

![Purchase Receipt flow](/docs/v13/assets/img/stock/purchase-receipt-flow.png)

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Phiếu nhập hàng, bạn nên tạo các mục sau trước:

* [Purchase Order](/docs/v13/user/manual/en/buying/purchase-order)

> Lưu ý: Từ phiên bản 13 trở đi, chúng tôi đã giới thiệu sổ cái bất biến (immutable ledger), điều này thay đổi các quy tắc về việc hủy các phiếu kho và ghi sổ các giao dịch kho lùi ngày trong ERPNext. [Tìm hiểu thêm tại đây](/docs/v13/user/manual/en/accounts/articles/immutable-ledger-in-erpnext).


## 2. Cách tạo Phiếu nhập hàng
Một Phiếu nhập hàng thường được tạo từ [Purchase Order](/docs/v13/user/manual/en/buying/purchase-order). Trong Đơn mua hàng, nhấp vào Create > Purchase Receipt.

Để tạo Phiếu nhập hàng một cách _thủ công_ (không được khuyến khích), hãy làm theo các bước sau:

1. Đi đến danh sách Phiếu nhập hàng, nhấp vào New.
1. Tên Nhà cung cấp và các Mặt hàng có thể được lấy từ Đơn mua hàng bằng cách nhấp vào 'Get Items from > Purchase Order'.
1. Bạn có thể thiết lập Kho chấp nhận (Accepted Warehouse) cho tất cả các mặt hàng trong Phiếu nhập hàng này. Thông tin này sẽ được lấy nếu đã được thiết lập trong Đơn mua hàng.
1. Trong trường hợp có bất kỳ Mặt hàng nào bị lỗi, hãy thiết lập Kho bị loại (Rejected Warehouse) nơi những Mặt hàng đó sẽ được lưu trữ.
1. Chọn Mặt hàng và nhập số lượng vào bảng Mặt hàng.
1. Đơn giá sẽ được lấy và số tiền sẽ được tính toán tự động.
1. Bạn có thể mở rộng dòng mặt hàng để thay đổi Kho chấp nhận cho một Mặt hàng.
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Purchase Receipt" src="{{docs_base_url}}/v13/assets/img/stock/purchase-receipt.png">

Bạn cũng có thể thêm 'Phiếu giao hàng của Nhà cung cấp' (Supplier Delivery Note) vào Phiếu nhập hàng nếu Nhà cung cấp có thêm một số ghi chú.
Sử dụng hộp kiểm 'Edit Posting Date and Time' để bạn có thể chỉnh sửa ngày và giờ ghi sổ của Phiếu nhập hàng. Theo mặc định, ngày và giờ được thiết lập khi bạn nhấp vào nút New.

Is Return: Tích vào hộp kiểm này nếu bạn đang trả lại các Mặt hàng không được chấp nhận vào Kho của mình.

### 2.1 Trạng thái

Đây là các trạng thái mà một Phiếu nhập hàng có thể có:

* **Draft**: Bản nháp đã được lưu nhưng chưa được xác nhận vào hệ thống.
* **To Bill**: Chưa được lập Hóa đơn bằng [Purchase Invoice](/docs/v13/user/manual/en/accounts/purchase-invoice).
* **Completed**: Đã xác nhận và đã nhận tất cả các Mặt hàng.
* **Return Issued**: Tất cả các Mặt hàng đã được trả lại.
* **Cancelled**: Đã Hủy Phiếu nhập hàng.
* **Closed**: Mục đích của việc Đóng là để quản lý việc đóng sớm đơn hàng. Ví dụ: bạn đặt hàng 20 số lượng, nhưng đóng khi mới nhận 15 số lượng. 5 số lượng còn lại sẽ không được nhận hoặc lập hóa đơn.

## 3. Các tính năng
### 3.1 Tiền tệ và Bảng giá
Tiền tệ của Phiếu nhập hàng được hiển thị trong phần này, nó được lấy từ Đơn mua hàng. Giá mặt hàng sẽ được lấy từ Bảng giá đã thiết lập. Tích vào Ignore Pricing Rule sẽ bỏ qua các Quy tắc định giá được thiết lập trong Accounts > Pricing Rule.

Vì Mặt hàng nhập về ảnh hưởng đến giá trị tồn kho của bạn, nên việc chuyển đổi sang tiền tệ cơ sở là rất quan trọng nếu bạn đặt hàng bằng một Tiền tệ khác. Bạn sẽ cần cập nhật Tỷ giá hối đoái nếu cần thiết.

Đọc về [Bảng giá](/docs/v13/user/manual/en/stock/price-lists)
và [Giao dịch đa tiền tệ](/docs/v13/user/manual/en/accounts/articles/managing-transactions-in-multiple-currency)
để biết thêm chi tiết.

### 3.2 Chi tiết Kho
Các thiết lập Kho sau đây sẽ áp dụng cho tất cả các Mặt hàng trong bảng Mặt hàng của Phiếu nhập hàng. Bạn có thể thay đổi Kho cho từng Mặt hàng riêng lẻ thông qua bảng.

* **Accepted Warehouse**: Đây là Kho mà bạn sẽ chấp nhận và lưu trữ các Mặt hàng nhập về. Thông thường, đây là Kho 'Stores'.
* **Rejected Warehouse:** Đây là Kho mà bạn sẽ giữ các Mặt hàng bị loại, những mặt hàng bị lỗi hoặc không đạt tiêu chuẩn chất lượng.

#### Gia công ngoài (Subcontracting)

* **Raw Materials Consumed**: Trong trường hợp bạn thuê gia công ngoài, hãy chọn 'Yes' để tiêu hao Nguyên vật liệu từ nhà cung cấp. Đọc [Subcontracting](/docs/v13/user/manual/en/manufacturing/subcontracting) để biết thêm chi tiết.

### 3.3 Bảng Mặt hàng

* **Barcode**: Bạn có thể theo dõi các Mặt hàng bằng [mã vạch](/docs/v13/user/manual/en/stock/articles/track-items-using-barcode).

* **Scan Barcode**: Bạn có thể thêm các Mặt hàng vào bảng Mặt hàng bằng cách quét mã vạch nếu bạn có máy quét mã vạch. Đọc tài liệu về [theo dõi mặt hàng bằng mã vạch](/docs/v13/user/manual/en/stock/articles/track-items-using-barcode) để biết thêm chi tiết.

* Mã Mặt hàng, tên, mô tả, Hình ảnh và Nhà sản xuất sẽ được lấy từ danh mục Mặt hàng.

* **Received and Accepted**: Thiết lập số lượng đã nhận, đã chấp nhận và bị loại. Đơn vị tính (UoM) được lấy từ danh mục Mặt hàng. Bạn sẽ cần cập nhật “UOM Conversion Factor” nếu Đơn mua hàng cho một Mặt hàng có Đơn vị tính (UOM) khác với Đơn vị tính tồn kho (Stock UOM).

    ![Purchase Receipt Items table](/docs/v13/assets/img/stock/purchase-receipt-item.png)

* **Rate**: Đơn giá được lấy nếu đã được thiết lập trong [Bảng giá](/docs/v13/user/manual/en/stock/price-lists) và tổng Số tiền sẽ được tính toán.

* **Item Tax Template**: Bạn có thể thiết lập Mẫu thuế mặt hàng để áp dụng một mức Thuế cụ thể cho Mặt hàng đó. Để biết thêm, hãy truy cập [trang này](/docs/v13/user/manual/en/accounts/item-tax-template).

* Chi tiết Trọng lượng mặt hàng trên mỗi đơn vị và Đơn vị tính trọng lượng được lấy nếu đã được thiết lập trong danh mục Mặt hàng.

* **Warehouse and Reference**: Bạn có thể thiết lập Kho chấp nhận và Kho bị loại, đồng thời có thể thêm Kiểm tra chất lượng, xem phần tiếp theo.

* **Serial No, Batch No, và BOM**: Nếu Mặt hàng của bạn có số serial hoặc theo lô, bạn sẽ phải nhập Số serial và Lô trong bảng Mặt hàng. Bạn được phép nhập nhiều...