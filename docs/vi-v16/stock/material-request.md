<!-- add-breadcrumbs -->
# Yêu cầu vật tư

**Yêu cầu vật tư là một tài liệu đơn giản xác định nhu cầu về một nhóm các Mặt hàng (sản phẩm hoặc dịch vụ) vì một lý do cụ thể.**

Yêu cầu vật tư có thể có các mục đích sau:

* **Mua hàng**: Nếu vật tư được yêu cầu cần phải mua.
* **Chuyển vật tư**: Nếu vật tư được yêu cầu cần được chuyển từ Kho này sang Kho khác.
* **Xuất vật tư**: Nếu vật tư được yêu cầu cần được Xuất cho một mục đích nào đó như sản xuất.
* **Sản xuất:** Nếu vật tư được yêu cầu cần được sản xuất.
* **Khách hàng cung cấp**: Nếu vật tư được yêu cầu sẽ do Khách hàng cung cấp. Để biết thêm về điều này, hãy truy cập trang [Mặt hàng do Khách hàng cung cấp](https://docs.erpnext.com/docs/v16/user/manual/en/manufacturing/articles/customer-provided-items).

<img class="screenshot" alt="Material Request" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/material-request-flowchart.png">

Để truy cập danh sách Yêu cầu vật tư, hãy đi đến:
> Trang chủ > Kho > Giao dịch kho > Yêu cầu vật tư

## 1. Cách tạo Yêu cầu vật tư
1. Đi đến danh sách Yêu cầu vật tư, nhấn vào Mới.
1. Nhập ngày cần hàng.
1. Chọn một trong các mục đích được liệt kê ở trên.
1. Bạn có thể lấy Mặt hàng từ một Định mức nguyên vật liệu, Đơn bán hàng hoặc Gói sản phẩm.
  ![MR fetch from](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/mr-fetch-from.png)
1. Chọn Mặt hàng và thiết lập số lượng.
1. Chọn Kho cần dùng Mặt hàng.
1. Bạn có thể thay đổi ngày Cần hàng cho từng Mặt hàng riêng biệt trong bảng này.
1. Lưu và Xác nhận.

### 1.1 Các cách khác để tạo Yêu cầu vật tư
Yêu cầu vật tư có thể được tạo tự động:

* Từ một [Đơn bán hàng](../selling/sales-order.md).
* Khi Số lượng dự kiến của một Mặt hàng trong Kho đạt đến một mức nhất định.
* Từ [Kế hoạch sản xuất](../manufacturing/production-plan.md) để lập kế hoạch cho các hoạt động sản xuất của bạn.

Nếu các Mặt hàng của bạn là hàng tồn kho, bạn cũng phải nêu rõ Kho nơi bạn mong muốn các Mặt hàng này được giao đến. Điều này giúp theo dõi [Số lượng dự kiến](projected-quantity.md) cho Mặt hàng này. Ngoài ra, với hệ thống mới, việc này giúp hỗ trợ [Hệ thống giữ hàng (Stock Reservation)](stock-reservation.md) chính xác hơn.

> Thông tin: Yêu cầu vật tư không phải là bắt buộc. Sẽ lý tưởng hơn nếu bạn có quy trình mua hàng tập trung để có thể thu thập thông tin này từ các bộ phận khác nhau.

### 1.2 Trạng thái

Đây là các trạng thái mà một Yêu cầu vật tư có thể có:

* **Nháp**: Bản nháp đã được Lưu nhưng chưa được Xác nhận vào hệ thống.
* **Đã xác nhận**: Tài liệu đã được Xác nhận vào hệ thống.
* **Dừng**: Nếu không cần thêm vật tư nữa, Yêu cầu vật tư có thể được dừng lại.
* **Đã hủy**: Vật tư không còn cần thiết nữa và yêu cầu đã bị Hủy.
* **Chờ xử lý**: Việc Mua hàng/Sản xuất đang chờ để hoàn tất Yêu cầu vật tư.
* **Đã đặt hàng một phần**: Đơn mua hàng cho một số Mặt hàng từ Yêu cầu vật tư đã được tạo và một số khác đang chờ.
* **Đã đặt hàng**: Tất cả các Mặt hàng trong Yêu cầu vật tư đã được đặt thông qua Đơn mua hàng.
* **Đã xuất**: Vật tư đã được xuất bằng Phiếu kho Xuất vật tư.
* **Đã chuyển**: Các vật tư cần thiết đã được chuyển từ Kho này sang Kho khác bằng Phiếu kho.
* **Đã nhận**: Vật tư đã được đặt và đã được nhận tại Kho của bạn bằng Phiếu nhập hàng.

## 2. Các tính năng
### 2.1 Bảng Mặt hàng
* **Mã vạch**: Bạn có thể theo dõi các Mặt hàng bằng [mã vạch](articles/track-items-using-barcode.md).

* Mã Mặt hàng, tên, mô tả, Hình ảnh và Nhà sản xuất sẽ được lấy từ danh mục Mặt hàng.

* **Quét mã vạch**: Bạn có thể thêm các Mặt hàng vào bảng Mặt hàng bằng cách quét mã vạch của chúng nếu có máy quét mã vạch. Đọc tài liệu về [theo dõi mặt hàng bằng mã vạch](articles/track-items-using-barcode.md) để biết thêm chi tiết.

* Đơn vị tính, Hệ số chuyển đổi và Số tiền sẽ được tự động lấy. Bạn có thể thay đổi Kho nơi vật tư đang được yêu cầu.

* Các chi tiết kế toán như Tài khoản chi phí và Chiều kích thước kế toán có thể được thiết lập cho các Mặt hàng. Với phiên bản v16, hệ thống hỗ trợ [Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting)](stock-accounting.md) để quản lý giá trị chính xác hơn.

* Ngắt trang sẽ tạo một điểm ngắt trang ngay trước mặt hàng này khi in.

### 2.2 Thiết lập Kho
* **Thiết lập Kho**: Tùy chọn, bạn có thể thiết lập Kho nơi các Mặt hàng được yêu cầu sẽ về tới. Thông tin này sẽ được lấy vào các trường 'Kho nhận' trong các dòng của bảng Mặt hàng.

### 2.3 Thông tin thêm
Trong trường 'Yêu cầu cho', bạn có thể thiết lập một Tham chiếu nơi Yêu cầu vật tư được tạo ra.

### 2.4 Chi tiết in
#### Tiêu đề thư
Bạn có thể in Yêu cầu vật tư trên tiêu đề thư của công ty bạn.
Đọc [tài liệu về Tiêu đề thư](https://docs.erpnext.com/docs/v16/user/manual/en/setting-up/print/letter-head) để tìm hiểu thêm.

#### Tiêu đề in
Tiêu đề Phiếu nhập hàng cũng có thể được thay đổi khi in tài liệu. Bạn có thể thực hiện việc này bằng cách chọn **Tiêu đề in**. Để tạo Tiêu đề in mới, hãy đi đến: Trang chủ > Thiết lập > In ấn > Tiêu đề in. Tìm hiểu thêm [tại đây](https://docs.erpnext.com/docs/v16/user/manual/en/setting-up/print/print-headings).

### 2.5 Điều khoản và Điều kiện
Trong các giao dịch Bán hàng/Mua hàng có thể có các Điều khoản và Điều kiện nhất định mà dựa vào đó Nhà cung cấp cung cấp hàng hóa hoặc dịch vụ cho Khách hàng. Bạn có thể áp dụng các Điều khoản và Điều kiện vào các giao dịch và chúng sẽ xuất hiện khi in tài liệu. Để biết về Điều khoản và Điều kiện, [nhấp vào đây](https://docs.erpnext.com/docs/v16/user/manual/en/setting-up/print/terms-and-conditions)

### 2.6 Sau khi Xác nhận
Bạn có thể tạo các tài liệu sau:

* [Yêu cầu báo giá](../buying/request-for-quotation.md)
* [Đơn mua hàng](../buying/purchase-order.md)
* [Báo giá của Nhà cung cấp](../buying/supplier-quotation.md)

<img class="screenshot" alt="Material Request" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/material-request.png">


### 2.7 Tự động tạo Yêu cầu vật tư

Yêu cầu vật tư có thể được tạo tự động bằng cách bật thiết lập trong [Thiết lập kho](stock-settings.md#9-automatic-material-request) và thiết lập mức độ trong [biểu mẫu Mặt hàng](items.md).