<!-- add-breadcrumbs -->
# Đơn mua hàng

**Đơn mua hàng là một hợp đồng ràng buộc với Nhà cung cấp, trong đó bạn cam kết mua một nhóm mặt hàng theo các điều kiện nhất định.**

Nó tương tự như Đơn bán hàng nhưng thay vì gửi cho bên thứ ba, bạn giữ nó để ghi chép nội bộ.

> Home > Buying > Purchasing > Purchase Order

![Buying Flow](https://docs.erpnext.com/docs/v16/assets/img/buying/buying_flow_po.png)

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Đơn mua hàng, bạn nên tạo các thông tin sau trước:

* [Nhà cung cấp](supplier.md)
* [Mặt hàng](../stock/item.md)


## 2. Cách tạo Đơn mua hàng

Đơn mua hàng có thể được tạo tự động từ một [Yêu cầu vật tư](../stock/material-request.md) hoặc Báo giá của Nhà cung cấp.

1. Đi tới danh sách Đơn mua hàng, nhấn vào Mới.
1. Chọn Nhà cung cấp, ngày cần hàng.
1. Trong bảng mặt hàng, chọn mặt hàng theo mã, bạn có thể thay đổi ngày cần hàng cho từng mặt hàng.
1. Thiết lập số lượng và đơn giá sẽ được lấy tự động nếu đã được thiết lập trong danh mục Mặt hàng.
1. Thiết lập thuế.
1. [Lưu](https://docs.erpnext.com/docs/v16/user/manual/vi/core-concepts/data-management#save) và [Xác nhận](https://docs.erpnext.com/docs/v16/user/manual/vi/core-concepts/data-management#submit).
    <img class="screenshot" alt="Purchase Order" src="https://docs.erpnext.com/docs/v16/assets/img/buying/purchase-order.png">

### 2.1 Thiết lập Kho

* **Thiết lập Kho đích**: Tùy chọn, bạn có thể thiết lập Kho đích mặc định nơi các Mặt hàng đã mua sẽ được giao đến. Thông tin này sẽ được lấy vào các dòng trong bảng mặt hàng.

### 2.2 Lấy Mặt hàng từ các Yêu cầu vật tư đang mở
Các mặt hàng có thể được lấy tự động vào Đơn mua hàng từ các [Yêu cầu vật tư](../stock/material-request.md) đang mở. Để thực hiện việc này, cần thực hiện các bước sau:

1. Chọn một Nhà cung cấp trong Đơn mua hàng.
1. Thiết lập Nhà cung cấp mặc định trong biểu mẫu Mặt hàng tại mục [Thiết lập mặc định cho mặt hàng](../stock/item.md#39-item-defaults).
1. [Yêu cầu vật tư](../stock/material-request.md) cần phải có loại là 'Purchase'.
1. Nhấp vào nút **Get Items from open Material Requests** bên dưới tên Nhà cung cấp. Một hộp thoại sẽ xuất hiện hiển thị các Yêu cầu vật tư có chứa các Mặt hàng mà Nhà cung cấp mặc định trùng với Nhà cung cấp đã chọn trong Đơn mua hàng. Sau khi chọn các Yêu cầu vật tư và nhấp vào **Get Items**, các Mặt hàng sẽ được lấy từ các Yêu cầu vật tư đó.
<img class="screenshot" alt="Get Items from Open Material Requests" src="https://docs.erpnext.com/docs/v16/assets/img/buying/get-items-from-open-mr.png">

> **Lưu ý:** Nút **Get Items from Open Material Requests** sẽ hiển thị chừng nào bảng mặt hàng còn trống.

## 3. Các tính năng mới và nâng cao (v16)

### 3.1 Lọc Nhà cung cấp không vận chuyển (Non-transporter supplier filtering)
Trong phiên bản v16, bạn có thể thiết lập bộ lọc để chỉ hiển thị các Nhà cung cấp có khả năng vận chuyển hoặc các Nhà cung cấp chuyên biệt, giúp việc chọn Nhà cung cấp trong Đơn mua hàng trở nên chính xác và nhanh chóng hơn.

### 3.2 Số tham chiếu Nhà cung cấp (Supplier reference numbers)
Bạn có thể lưu trữ và quản lý các số tham chiếu riêng của Nhà cung cấp (như số hợp đồng hoặc mã định danh riêng của họ) ngay trong Đơn mua hàng để đối chiếu dễ dàng hơn khi làm việc với bên bán.

### 3.3 Tạo bản nháp PI qua Email (Email append-to tạo PI draft)
Tính năng này cho phép bạn tự động tạo bản nháp của Proforma Invoice (PI) dựa trên các thông tin được gửi qua email, giúp tối ưu hóa quy trình làm việc giữa bộ phận mua hàng và nhà cung cấp.

### 3.4 Xem trước Sổ cái (Ledger Preview)
Trước khi [Xác nhận](https://docs.erpnext.com/docs/v16/user/manual/vi/core-concepts/data-management#submit) Đơn mua hàng, bạn có thể sử dụng tính năng **Ledger Preview** để xem trước các bút toán [JE](accounts/articles/journal-entry.md) sẽ được tạo. Điều này giúp đảm bảo các tài khoản chi phí và thuế được hạch toán chính xác.

## 4. Các tính năng khác

### 4.1 Địa chỉ và Liên hệ

* **Chọn Địa chỉ Nhà cung cấp**: Địa chỉ thanh toán của Nhà cung cấp.
* **Chọn Địa chỉ giao hàng**: Địa chỉ giao hàng của Nhà cung cấp, nơi họ sẽ gửi các mặt hàng đi.
* Địa chỉ, Địa chỉ giao hàng, Liên hệ, Email liên hệ sẽ được lấy tự động nếu đã được lưu trong danh mục Nhà cung cấp.

Dành cho Ấn Độ:

* **GSTIN của Nhà cung cấp và Công ty**: Mã số định danh thuế GST của Nhà cung cấp và công ty của bạn.
* **Địa điểm cung ứng**: Đối với GST, Địa điểm cung ứng là bắt buộc. Nó bao gồm tên và mã số của bang.

### 4.2 Tiền tệ và Bảng giá
Bạn có thể thiết lập loại tiền tệ mà đơn mua hàng sẽ được lưu trữ. Nếu bạn thiết lập một Bảng giá, thì giá mặt hàng sẽ được lấy từ bảng đó. Việc tích vào Bỏ qua Quy tắc định giá sẽ bỏ qua các Quy tắc định giá đã được thiết lập trong Accounts > Pricing Rule.

Đọc thêm về [Bảng giá](../stock/price-lists.md)
và [Giao dịch đa tiền tệ](../accounts/articles/managing-transactions-in-multiple-currency.md)
để biết thêm chi tiết.

### 4.3 Gia công hoặc 'Cung cấp nguyên vật liệu'

Thiết lập tùy chọn 'Supply Raw Materials' rất hữu ích cho việc gia công, nơi bạn cung cấp nguyên vật liệu để sản xuất một mặt hàng. Để biết thêm, hãy truy cập [Trang Gia công](https://docs.erpnext.com/docs/v16/user/manual/vi/manufacturing/subcontracting).

### 4.4 Bảng mặt hàng

* **Quét mã vạch**: Bạn có thể thêm các Mặt hàng vào bảng mặt hàng bằng cách quét mã vạch nếu có máy quét mã vạch. Đọc tài liệu về [theo dõi mặt hàng bằng mã vạch](../stock/articles/track-items-using-barcode.md) để biết thêm.

* **Số lượng và Đơn giá**: Khi bạn chọn mã Mặt hàng, tên, mô tả và Đơn vị tính của nó sẽ được lấy tự động. 'Hệ số chuyển đổi Đơn vị tính' được đặt mặc định là 1, bạn có thể thay đổi tùy thuộc vào Đơn vị tính nhận được từ người bán, xem thêm ở phần tiếp theo.

    'Đơn giá Bảng giá' sẽ được lấy nếu có thiết lập Đơn giá mua tiêu chuẩn. 'Đơn giá mua gần nhất' hiển thị đơn giá của mặt hàng từ Đơn mua hàng gần nhất của bạn. Đơn giá được lấy nếu đã được thiết lập trong danh mục Mặt hàng. Bạn có thể đính kèm một Mẫu thuế mặt hàng để áp dụng mức thuế cụ thể cho mặt hàng đó.

* **Trọng lượng mặt hàng** sẽ được lấy tự động nếu đã được thiết lập trong danh mục Mặt hàng, nếu không hãy nhập thủ công.

* **Kho**: Kho nơi các mặt hàng sẽ được giao đến sẽ được tự động điền nếu 'Thiết lập Kho đích' đã được thiết lập trong Đơn mua hàng. Thông qua Đơn hàng tổng quát (Blanket Order), một Đơn hàng tổng quát có thể được liên kết, để biết thêm [nhấp vào đây](../selling/blanket-order.md). Một 'Dự án' có thể được liên kết để theo dõi tiến độ. Một 'Định mức nguyên vật liệu' cũng có thể được liên kết để theo dõi tiến độ.

* 'Số lượng theo Đơn vị tính kho' sẽ hiển thị lượng tồn kho hiện tại theo Đơn vị tính được thiết lập trong danh mục Mặt hàng. 'Số lượng đã nhận' sẽ được cập nhật khi các mặt hàng được lập [Hóa đơn](accounts/doctype/sales-invoice/sales-invoice.md).

* **Chi tiết kế toán**: Phần này được tự động điền cho Đơn mua hàng. 'Tài khoản chi phí' là tài khoản mà Đơn mua hàng được lập hóa đơn và Trung tâm chi phí là trung tâm chi phí mà Đơn mua hàng được tính vào.

**Ngày "Cần hàng" cho mỗi Mặt hàng**: Nếu bạn đang mong đợi việc giao hàng từng phần, Nhà cung cấp sẽ biết cần giao bao nhiêu số lượng vào ngày nào. Điều này sẽ giúp bạn tránh việc cung ứng quá mức. Nó cũng giúp bạn theo dõi khả năng đáp ứng đúng hạn của Nhà cung cấp.

**Cho phép Giá trị tính giá bằng 0**: