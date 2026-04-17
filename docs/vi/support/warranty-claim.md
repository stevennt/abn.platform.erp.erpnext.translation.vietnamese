<!-- add-breadcrumbs -->
# Khiếu nại Bảo hành

**Khiếu nại Bảo hành là khi Khách hàng yêu cầu sửa chữa miễn phí trong Thời hạn Bảo hành của mặt hàng/dịch vụ mà bạn đang cung cấp.**

Nếu bạn đang bán các Mặt hàng được bảo hành hoặc nếu bạn đã bán và gia hạn hợp đồng dịch vụ như Hợp đồng Bảo trì hàng năm (AMC), Khách hàng của bạn có thể liên hệ với bạn về một vấn đề hoặc sự cố hỏng hóc của sản phẩm và cung cấp cho bạn Số serial của Mặt hàng này.

Để truy cập danh sách Khiếu nại Bảo hành, hãy đi đến:

> Home > Support > Warranty > Warranty Claim

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Khiếu nại Bảo hành, bạn nên tạo các mục sau trước:

* [Customer](/docs/v13/user/manual/en/CRM/customer)
* [Serial Number](/docs/v13/user/manual/en/stock/serial-no)
* [Item](/docs/v13/user/manual/en/stock/item)

## 2. Cách tạo Khiếu nại Bảo hành

1. Đi đến danh sách Khiếu nại Bảo hành, nhấn vào Mới.
1. Chọn một Khách hàng.
1. Chọn Số serial của Mặt hàng mà Khiếu nại Bảo hành sẽ được ghi nhận. Hệ thống sau đó sẽ tự động lấy chi tiết của Số serial và cho biết mặt hàng này đang trong thời hạn bảo hành hay AMC.
1. Nhập mô tả về Vấn đề. Người dùng có thể tải lên một hình ảnh và tạo một bảng.
1. Lưu.
    ![Warranty Claim](https://docs.erpnext.com/docs/v13/assets/img/support/warranty-claim.png)

### 2.1 Các tùy chọn bổ sung khi tạo Khiếu nại Bảo hành

* **Status (Trạng thái)**: Khi đang tạo Khiếu nại Bảo hành, trạng thái sẽ được đặt là "Open" (Mở). Người dùng có thể thay đổi trạng thái thành:
    * Work In Progress (Đang xử lý): Việc sửa chữa/khắc phục đang được thực hiện trên Mặt hàng.
    * Closed (Đã đóng): Việc sửa chữa đã hoàn tất và Khiếu nại Bảo hành hiện đã được đóng.
    * Cancelled (Đã hủy): Khiếu nại Bảo hành không hợp lệ và khiếu nại đã được đóng.
* **Issue Date (Ngày phát sinh vấn đề)**: Khi đang tạo Khiếu nại Bảo hành, ngày hiện tại sẽ được ghi nhận. Trường này có thể chỉnh sửa được.


## 3 Tính năng

### 3.1 Chi tiết Mặt hàng và Bảo hành:

Sau khi một Số serial được chọn, các chi tiết sau về Mặt hàng sẽ được lấy ra:

* Item Code (Mã mặt hàng)
* Item Name (Tên mặt hàng)
* Item Description (Mô tả mặt hàng)

Các chi tiết về Bảo hành/AMC sẽ được lấy dựa theo Số serial.

* **Warranty / AMC Status (Trạng thái Bảo hành / AMC):** Các tùy chọn có thể là "Under Warranty" (Trong thời hạn bảo hành), "Out of Warranty" (Hết hạn bảo hành), "Under AMC" (Trong thời hạn AMC), hoặc "Out of AMC" (Hết hạn AMC). Trạng thái có thể được đổi thành Out of Warranty/AMC nếu Mặt hàng đã bị can thiệp trái phép hoặc Bảo hành bị vô hiệu tùy theo các điều khoản dịch vụ của bạn.
* Warranty Expiry Date (Ngày hết hạn bảo hành)
* AMC Expiry date (Ngày hết hạn AMC)

    ![Warranty Serial](https://docs.erpnext.com/docs/v13/assets/img/support/warranty-serial.png)

### 3.2 Resolution (Giải quyết)
* **Resolution Date (Ngày giải quyết):** Khi bảo hành hoặc AMC được đóng (Closed), ngày và giờ hiện tại sẽ tự động được lấy vào trường Ngày giải quyết. Trường này cũng có thể chỉnh sửa được.
* **Resolved By (Người giải quyết):** Thiết lập ID Email của Người dùng đã giải quyết Khiếu nại Bảo hành. ID email được liên kết với [User](/docs/v13/user/manual/en/setting-up/users-and-permissions/adding-users) được tạo trong hệ thống.
* **Resolved Details (Chi tiết giải quyết):** Đây là một trường văn bản. Người dùng có thể nhập chi tiết về khiếu nại Bảo hành hoặc AMC. Người dùng cũng có thể tải lên hình ảnh, nhập hoặc tạo một bảng.

    ![Warranty Resolution](https://docs.erpnext.com/docs/v13/assets/img/support/warranty-resolution.png)

### 3.3 Chi tiết Khách hàng

Các chi tiết sau của [Customer](/docs/v13/user/manual/en/CRM/customer) sẽ được lấy ra:

* Customer Name (Tên khách hàng)
* Contact Person (Người liên hệ)
* Territory (Khu vực)
* Customer Group (Nhóm khách hàng)
* Customer Addresss (Địa chỉ khách hàng)

**Service Address (Địa chỉ dịch vụ):** Người dùng có thể nhập Địa chỉ dịch vụ nếu nó khác với Địa chỉ khách hàng.

![Warranty Customer](https://docs.erpnext.com/docs/v13/assets/img/support/warranty-customer.png)

### 3.4 Thông tin thêm

* **Company (Công ty):** Công ty tạo Bảo hành hoặc AMC sẽ được chọn tự động.
* **Raised By (Người yêu cầu):** Người dùng có thể nhập Tên của người đã yêu cầu Bảo hành hoặc AMC trong trường hợp Khách hàng là một tổ chức.
* **From Company (Từ công ty):** Người dùng có thể nhập tên công ty nơi bảo hành hoặc AMC đã được tạo.

Nếu cần một chuyến thăm để xử lý vấn đề, bạn có thể tạo một bản ghi Maintenance Visit (Chuyến thăm bảo trì) mới từ đây.

## 4. Các chủ đề liên quan
1. [Issue](/docs/v13/user/manual/en/support/issue)
1. [Maintenance Visit](/docs/v13/user/manual/en/support/maintenance-visit)

{next}