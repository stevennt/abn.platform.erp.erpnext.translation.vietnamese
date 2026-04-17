<!-- add-breadcrumbs -->
# Đơn bán hàng

**Đơn bán hàng là sự xác nhận một đơn đặt hàng từ khách hàng của bạn.**

Nó thường là một Hợp đồng ràng buộc với Khách hàng của bạn. Khi khách hàng xác nhận Báo giá, bạn có thể chuyển đổi Báo giá của mình thành Đơn bán hàng.

![Sales Flow](https://docs.erpnext.com/docs/v16/assets/img/selling/selling-flow-so.png)

Để truy cập Đơn bán hàng, hãy đi đến:
> Home > Selling > Sales > Sales Order

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Đơn bán hàng, bạn nên tạo các mục sau trước:

* [Khách hàng](customer-list.md)
* [Mặt hàng](../stock/item.md)

## 2. Cách tạo Đơn bán hàng
1. Đi đến danh sách Đơn bán hàng, nhấn vào Mới.
1. Chọn Khách hàng.
1. Thiết lập 'Ngày giao hàng' - áp dụng cho toàn bộ đơn hàng.
1. Với Loại đơn hàng (Order Type), bạn có thể thiết lập đó là Đơn bán hàng, Đơn bảo trì, hoặc từ [Giỏ hàng](https://docs.erpnext.com/docs/v16/user/manual/en/website/shopping-cart) trực tuyến của trang web. Theo mặc định, giá trị này được đặt là "Sales".
1. Trong phần "Đơn mua hàng của Khách hàng", bạn có thể nhập Số đơn mua hàng của Khách hàng hoặc các chi tiết khác có thể hữu ích để tham chiếu.
1. Nhập các mặt hàng và số lượng cần giao trong bảng Mặt hàng. Nếu Đơn giá Mặt hàng đã được thiết lập cho các mặt hàng, trường Đơn giá sẽ được tự động điền. Nếu không, hãy nhập Đơn giá mặt hàng theo cách thủ công. Bạn cũng có thể ghi đè Đơn giá Mặt hàng được tự động điền trong trường hợp bạn muốn thay đổi giá trị đó.
1. Nhấn "Lưu" để lưu bản nháp của Đơn bán hàng.
1. Nhấn "Xác nhận" để xác nhận Đơn bán hàng vào Hệ thống.

### 2.1 Các cách khác để tạo Đơn bán hàng
1. Bạn cũng có thể tạo Đơn bán hàng từ một Báo giá đã được xác nhận thông qua nút Tạo ở góc trên bên phải.

  ![Make Sales Order from Quotation](https://docs.erpnext.com/docs/v16/assets/img/selling/make-SO-from-quote.png)

1. Hoặc bạn có thể tạo một Đơn bán hàng mới và lấy thông tin chi tiết từ một Báo giá.

  ![Make Sales Order from Quotation](https://docs.erpnext.com/docs/v16/assets/img/selling/so-from-quote.gif)

2. **Từ Khách hàng**: Tại màn hình chi tiết của Khách hàng, bạn có thể nhanh chóng tạo Đơn bán hàng hoặc Báo giá thông qua các nút chức năng được tích hợp sẵn trong phần liên quan.

Để cho phép các Quy tắc định giá theo từng Khách hàng, từng Mặt hàng ("Khách hàng A" trả 1,00 $ cho "Mặt hàng 1" nhưng "Khách hàng B" trả 1,25 $ cho "Mặt hàng 1"), có một hộp kiểm gọi là 'Allow User to Edit Price List Rate in Transaction' trong [Cài đặt bán hàng](selling-settings.md). Điều này cho phép lưu giá mặt hàng cụ thể cho từng khách hàng khi bạn thay đổi giá trong Đơn bán hàng.

## 3. Các tính năng

### 3.1 Tiền tệ và Bảng giá
Bạn có thể thiết lập tiền tệ mà báo giá/đơn bán hàng sẽ được gửi đi. Nếu bạn thiết lập một Bảng giá, thì giá mặt hàng sẽ được lấy từ bảng đó. Việc tích vào 'Ignore Pricing Rule' sẽ bỏ qua các [Quy tắc định giá](../accounts/pricing-rule.md) đã được thiết lập trong Accounts > Pricing Rule.

Đọc về [Bảng giá](../stock/price-lists.md)
và [Giao dịch đa tiền tệ](../accounts/articles/managing-transactions-in-multiple-currency.md)
để biết thêm chi tiết.

### 3.2 Thiết lập Kho nguồn
Nếu bạn có cùng một lượng tồn kho trong nhiều kho khác nhau, việc thiết lập một kho ở đây sẽ khiến tất cả các mặt hàng từ bảng mặt hàng được lấy từ kho này. Bạn cần phải có sẵn hàng trong 'kho nguồn' mà bạn đang thiết lập. Lưu ý rằng tùy chọn này sẽ ghi đè lên 'Kho mặc định' mà bạn đã thiết lập trong danh mục Mặt hàng.

### 3.3 Bảng Mặt hàng

* **Ngày giao hàng cho từng mặt hàng**: Nếu có nhiều mặt hàng và nếu bạn nhập ngày giao hàng ở dòng đầu tiên, ngày đó cũng sẽ được sao chép sang các dòng khác nếu chúng đang để trống. Bạn sẽ phải thiết lập các ngày này nếu không thiết lập chung ở phía trên của Đơn bán hàng.

    Một Đơn bán hàng hiển thị số tiền đã lập hóa đơn, giá trị tính giá và lợi nhuận gộp trong bảng mặt hàng khi bạn nhấp vào hình tam giác ngược để mở rộng một dòng.

    Bạn cũng có thể thêm Mặt hàng vào bảng Mặt hàng bằng cách quét mã vạch nếu bạn có máy quét mã vạch. Đọc tài liệu về [theo dõi mặt hàng bằng mã vạch](../stock/articles/track-items-using-barcode.md) để biết thêm.

* **Kho giao hàng**: Đây là kho mà hàng sẽ được lấy ra để giao cho khách hàng của bạn.

* **Drop Ship (Giao hàng thẳng)**: Đây là tình huống mà bạn không giữ hàng trong kho của mình mà giao hàng trực tiếp cho khách hàng từ một nhà phân phối. Để bật tính năng drop shipping cho một mặt hàng, hãy tích vào 'Supplier delivers to Customer'. Khi bạn tích vào mục này, tùy chọn Kho giao hàng sẽ biến mất vì bạn không trực tiếp giao hàng. Hãy chọn nhà cung cấp của bạn trong trường 'Nhà cung cấp'.

    Hơn nữa, nếu bạn tạo một đơn mua hàng từ đơn bán hàng này, nó sẽ được tạo cho nhà cung cấp mà bạn đã chọn ở đây và chỉ dành cho các mặt hàng hợp lệ để drop shipping.

* **Lập kế hoạch & Giữ hàng (Stock Reservation)**: ERPNext v16 hỗ trợ tính năng Giữ hàng trong kho. Khi bạn xác nhận Đơn bán hàng, hệ thống có thể thực hiện giữ số lượng tồn kho cho các mặt hàng trong đơn để đảm bảo khả năng cung ứng khi cần giao hàng. Đọc về [Số lượng dự kiến](../stock/projected-quantity.md) để biết thêm về các trường trong phần lập kế hoạch.

Các trường khác trong bảng mặt hàng tương tự như đã được giải thích trong [Báo giá](quotation.md#23-the-items-table).

### 3.4 Phiếu đóng gói

Mục này được liên kết với [Gói sản phẩm](product-bundle.md) và chỉ xuất hiện khi giao dịch có liên quan đến một gói sản phẩm.

Bảng “Phiếu đóng gói” sẽ tự động được cập nhật khi bạn “Lưu” Đơn bán hàng. Nếu bất kỳ Mặt hàng nào trong bảng của bạn là Gói sản phẩm, thì “Phiếu đóng gói” sẽ chứa danh sách chi tiết (đã tách) các Mặt hàng của bạn.

Bạn sẽ được yêu cầu chọn một Kho giao hàng ngay cả đối với một mặt hàng gói sản phẩm, kho này sau đó sẽ được cập nhật trong các mặt hàng của Phiếu đóng gói. Bạn có thể thay đổi kho, số serial và lô hàng trong các mặt hàng của phiếu đóng gói trong trường hợp các mặt hàng trong gói sản phẩm của bạn đến từ các kho khác nhau.

Dưới đây là hình ảnh của một Phiếu đóng gói:

![Packing List](https://docs.erpnext.com/docs/v16/assets/img/selling/so-packing-list.png)

### 3.5 Ngày chốt (Cutoff Date) cho Phiếu giao hàng
Trong phiên bản v16, khi bạn tạo Phiếu giao hàng (DN) từ Đơn bán hàng (SO), hệ thống cho phép thiết lập ngày chốt (Cutoff date). Điều này giúp kiểm soát việc xuất kho và quản lý các lô hàng/phiếu giao hàng phát sinh trong một khoảng thời gian nhất định, đảm bảo tính chính xác của dữ liệu tồn kho và kế toán.

### 3.6 Thuế và Phí
Để thêm thuế vào Báo giá, bạn có thể chọn một [Mẫu thuế và phí bán hàng](sales-taxes-and-charges.md).