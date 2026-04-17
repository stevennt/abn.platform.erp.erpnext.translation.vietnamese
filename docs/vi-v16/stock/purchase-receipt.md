<!-- add-breadcrumbs -->
# Phiếu nhập hàng

**Phiếu nhập hàng được lập khi bạn chấp nhận các Mặt hàng từ Nhà cung cấp, thường là dựa trên một Đơn mua hàng.**

Bạn cũng có thể lập Phiếu nhập hàng trực tiếp mà không cần Đơn mua hàng. Để làm điều này, hãy thiết lập Purchase Order Required thành “No” trong Cài đặt mua hàng (Buying Settings).

Để truy cập danh sách Phiếu nhập hàng, hãy đi đến:
> Home > Stock > Stock Transactions > Purchase Receipt

![Purchase Receipt flow](https://docs.erpnext.com/docs/v16/assets/img/stock/purchase-receipt-flow.png)

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Phiếu nhập hàng, bạn nên tạo các mục sau trước:

* [Purchase Order](../buying/purchase-order.md)

> Lưu ý: Từ phiên bản 16, hệ thống sử dụng sổ cái bất biến (immutable ledger), điều này thay đổi các quy tắc về việc hủy các phiếu kho và ghi sổ các giao dịch kho lùi ngày trong ERPNext. [Tìm hiểu thêm tại đây](../accounts/articles/immutable-ledger-in-erpnext.md).


## 2. Cách tạo Phiếu nhập hàng
Một Phiếu nhập hàng thường được tạo từ [Purchase Order](../buying/purchase-order.md). Trong Đơn mua hàng, nhấp vào Create > Purchase Receipt.

Để tạo Phiếu nhập hàng một cách _thủ công_ (không được khuyến khích), hãy làm theo các bước sau:

1. Đi đến danh sách Phiếu nhập hàng, nhấp vào New.
1. Tên Nhà cung cấp và các Mặt hàng có thể được lấy từ Đơn mua hàng bằng cách nhấp vào 'Get Items from > Purchase Order'.
1. Bạn có thể thiết lập Kho chấp nhận (Accepted Warehouse) cho tất cả các mặt hàng trong Phiếu nhập hàng này. Thông tin này sẽ được lấy nếu đã được thiết lập trong Đơn mua hàng.
1. Trong trường hợp có bất kỳ Mặt hàng nào bị lỗi, hãy thiết lập Kho bị loại (Rejected Warehouse) nơi những Mặt hàng đó sẽ được lưu trữ.
1. Chọn Mặt hàng và nhập số lượng vào bảng Mặt hàng.
1. Đơn giá sẽ được lấy và số tiền sẽ được tính toán tự động.
1. Bạn có thể mở rộng dòng mặt hàng để thay đổi Kho chấp nhận cho một Mặt hàng.
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Purchase Receipt" src="https://docs.erpnext.com/docs/v16/assets/img/stock/purchase-receipt.png">

Bạn cũng có thể thêm 'Phiếu giao hàng của Nhà cung cấp' (Supplier Delivery Note) vào Phiếu nhập hàng nếu Nhà cung cấp có thêm một số ghi chú.
Sử dụng hộp kiểm 'Edit Posting Date and Time' để bạn có thể chỉnh sửa ngày và giờ ghi sổ của Phiếu nhập hàng. Theo mặc định, ngày và giờ được thiết lập khi bạn nhấp vào nút New.

Is Return: Tích vào hộp kiểm này nếu bạn đang trả lại các Mặt hàng không được chấp nhận vào Kho của mình.

### 2.1 Trạng thái

Đây là các trạng thái mà một Phiếu nhập hàng có thể có:

* **Draft**: Bản nháp đã được Lưu nhưng chưa được Xác nhận vào hệ thống.
* **To Bill**: Chưa được lập Hóa đơn bằng [Purchase Invoice](../accounts/purchase-invoice.md).
* **Completed**: Đã Xác nhận và đã nhận tất cả các Mặt hàng.
* **Return Issued**: Tất cả các Mặt hàng đã được trả lại.
* **Cancelled**: Đã Hủy Phiếu nhập hàng.
* **Closed**: Mục đích của việc Đóng là để quản lý việc đóng sớm đơn hàng. Ví dụ: bạn đặt hàng 20 số lượng, nhưng đóng khi mới nhận 15 số lượng. 5 số lượng còn lại sẽ không được nhận hoặc lập hóa đơn.

## 3. Các tính năng
### 3.1 Tiền tệ và Bảng giá
Tiền tệ của Phiếu nhập hàng được hiển thị trong phần này, nó được lấy từ Đơn mua hàng. Giá mặt hàng sẽ được lấy từ Bảng giá đã thiết lập. Tích vào Ignore Pricing Rule sẽ bỏ qua các Quy tắc định giá được thiết lập trong Accounts > Pricing Rule.

Vì Mặt hàng nhập về ảnh hưởng đến giá trị tồn kho của bạn, nên việc chuyển đổi sang tiền tệ cơ sở là rất quan trọng nếu bạn đặt hàng bằng một Tiền tệ khác. Bạn sẽ cần cập nhật Tỷ giá hối đoái nếu cần thiết.

Đọc về [Bảng giá](price-lists.md)
và [Giao dịch đa tiền tệ](../accounts/articles/managing-transactions-in-multiple-currency.md)
để biết thêm chi tiết.

### 3.2 Chi tiết Kho
Các thiết lập Kho sau đây sẽ áp dụng cho tất cả các Mặt hàng trong bảng Mặt hàng của Phiếu nhập hàng. Bạn có thể thay đổi Kho cho từng Mặt hàng riêng lẻ thông qua bảng.

* **Accepted Warehouse**: Đây là Kho mà bạn sẽ chấp nhận và lưu trữ các Mặt hàng nhập về. Thông thường, đây là Kho 'Stores'.
* **Rejected Warehouse:** Đây là Kho mà bạn sẽ giữ các Mặt hàng bị loại, những mặt hàng bị lỗi hoặc không đạt tiêu chuẩn chất lượng.

#### Gia công ngoài (Subcontracting)

* **Raw Materials Consumed**: Trong trường hợp bạn thuê gia công ngoài, hãy chọn 'Yes' để tiêu hao Nguyên vật liệu từ nhà cung cấp. Đọc [Subcontracting](https://docs.erpnext.com/docs/v16/user/manual/en/manufacturing/subcontracting) để biết thêm chi tiết.

#### Chi phí liên quan (Landed Cost)

Trong phiên bản v16, bạn có thể áp dụng **Landed Cost** (Chi phí thu mua) trực tiếp cho Phiếu nhập hàng. Điều này cho phép bạn phân bổ các chi phí như vận chuyển, thuế nhập khẩu hoặc phí bốc dỡ vào giá trị của từng Mặt hàng trong kho, giúp phản ánh chính xác giá trị tồn kho thực tế.

### 3.3 Bảng Mặt hàng

* **Barcode**: Bạn có thể theo dõi các Mặt hàng bằng [mã vạch](articles/track-items-using-barcode.md).

* **Scan Barcode**: Bạn có thể thêm các Mặt hàng vào bảng Mặt hàng bằng cách quét mã vạch nếu bạn có máy quét mã vạch. Đọc tài liệu về [theo dõi mặt hàng bằng mã vạch](articles/track-items-using-barcode.md) để biết thêm chi tiết.

* **Hệ thống Giữ hàng (Stock Reservation)**: V16 hỗ trợ tính năng giữ hàng, giúp đảm bảo các Mặt hàng đã được đặt mua sẽ được dành riêng cho các nhu cầu cụ thể, tránh tình trạng thiếu hụt khi hàng về kho.

* **Truy xuất nguồn gốc (Serial/Batch Traceability)**: Khi nhập hàng, bạn có thể quản lý chi tiết theo [Lô hàng (Batch)](batch.md) hoặc Số sê-ri (Serial Number). Báo cáo truy xuất nguồn gốc sẽ giúp bạn theo dõi lịch sử của từng đơn vị hàng hóa từ khi nhập đến khi xuất.

* **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting)**: V16 cho phép ghi nhận các bút toán kế toán chi tiết hơn cho từng Mặt hàng, giúp việc đối soát giữa sổ cái và tồn kho trở nên chính xác tuyệt đối.

* **Xem trước Sổ cái (Ledger Preview)**: Bạn có thể xem nhanh các Bút toán (JE) liên quan đến giao dịch kho ngay tại giao diện Phiếu nhập hàng để kiểm tra tính chính xác của việc ghi sổ.

* Mã Mặt hàng, tên, mô tả, Hình ảnh và Nhà sản xuất sẽ được lấy từ danh mục Mặt hàng.

* **Received and Accepted**: Thiết lập số lượng đã nhận, đã chấp nhận và bị loại. Đơn vị tính (UoM) được lấy từ danh mục Mặt hàng. Bạn sẽ cần cập nhật “UOM Conversion Factor” nếu Đơn mua hàng cho một Mặt hàng có Đơn vị tính (UOM) khác với Đơn vị tính tồn kho (Stock UOM).

    ![Purchase Receipt Items table](https://docs.erpnext.com/docs/v16/assets/img/stock/purchase-receipt-item.png)

* **Rate**: Đơn giá được lấy nếu đã được thiết lập trong [Bảng giá](price-lists.md) và tổng Số tiền sẽ được tính toán.

* **Item Tax Template**: Bạn có thể thiết lập Mẫu thuế mặt hàng để áp dụng một mức Thuế cụ thể cho Mặt hàng đó. Để biết thêm, hãy truy cập [trang này](../accounts/item-tax-template.md).

* Chi tiết Trọng lượng mặt hàng trên mỗi đơn vị và Đơn vị tính trọng lượng được lấy nếu đã được thiết lập trong danh mục Mặt hàng.