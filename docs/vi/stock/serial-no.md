<!-- add-breadcrumbs -->
# Số serial

Như đã thảo luận trong trang [Mặt hàng](item.md), nếu một **Mặt hàng** được _có số serial_, một bản ghi **Số serial** (Serial No) sẽ được duy trì cho mỗi số lượng của **Mặt hàng** đó. Thông tin này giúp theo dõi vị trí của Số serial, thông tin bảo hành và thông tin hết hạn sử dụng (vòng đời).

**Số serial** cũng hữu ích để quản lý tài sản cố định. [Lịch bảo trì](../support/maintenance-schedule.md) cũng có thể được tạo dựa trên Số serial để lập kế hoạch và sắp xếp hoạt động bảo trì cho các tài sản này (nếu chúng yêu cầu bảo trì).

Bạn cũng có thể theo dõi xem bạn đã mua **Số serial** đó từ **Nhà cung cấp** nào và đã bán nó cho **Khách hàng** nào. Trạng thái của **Số serial** sẽ cho bạn biết tình trạng tồn kho hiện tại của nó.

Nếu Mặt hàng của bạn được _có số serial_, bạn sẽ phải nhập các Số serial vào cột liên quan với mỗi Số serial trên một dòng mới.
Bạn có thể quản lý các đơn vị riêng lẻ của các mặt hàng có số serial bằng cách sử dụng Số serial.

Để truy cập danh sách Số serial, hãy đi tới:
> Trang chủ > Kho > Số serial và Lô hàng > Số serial

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Số serial, bạn nên tạo các mục sau trước:

* [Mặt hàng](item.md)
* Bật 'Has Serial No' trong danh mục Mặt hàng
    ![Serial No Enabled](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/serial-no-enabled.png)


## 2. Cách tạo Số serial
Thông thường, Số serial được tự động tạo khi các giao dịch được thực hiện đối với một Mặt hàng có số serial. Điều này chỉ hoạt động khi 'Has Serial No' được bật và một chuỗi số (series) đã được thiết lập trong danh mục Mặt hàng.

Ví dụ, một chuỗi số đã được thiết lập cho Mặt hàng sau là 'PB2L.#####'. Sau đó, một Phiếu kho được Xác nhận để nhập Mặt hàng. Các Số serial đã được tạo tương ứng.

![Serial No Created](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/serial-no-created.png)

Tuy nhiên, nếu bạn muốn tạo Số serial _thủ công_, hãy làm theo các bước sau:

1. Đi tới danh sách Số serial, nhấn vào Mới.
1. Nhập một Số serial.
1. Nhập Mã mặt hàng và các chi tiết sẽ được lấy ra.
1. Nếu có bất kỳ giao dịch nào được thực hiện với một mặt hàng, Số serial không thể được thiết lập hoặc hủy thiết lập.
1. Lưu.

Tồn kho của một Mặt hàng chỉ có thể bị ảnh hưởng nếu Số serial được giao dịch thông qua một giao dịch Kho (Phiếu kho, Phiếu nhập hàng, Phiếu giao hàng, Hóa đơn bán hàng). Khi một Số serial mới được tạo trực tiếp, Kho của nó không thể được thiết lập.

<img class="screenshot" alt="Serial Number" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/serial-no.png">

### 2.1 Lưu ý về Số serial

* Trạng thái được thiết lập dựa trên Phiếu kho.
* Chỉ những Số serial có trạng thái 'Available' (Sẵn có) mới có thể được giao.
* Số serial có thể được tự động tạo từ Phiếu kho hoặc Phiếu nhập hàng. Nếu bạn ghi Số serial vào cột Số serial, hệ thống sẽ tự động tạo các số serial đó.
* Nếu trong danh mục Mặt hàng có ghi Chuỗi số serial, bạn có thể để trống cột Số serial trong Phiếu kho / Phiếu nhập hàng. Các Số serial sẽ tự động được thiết lập từ chuỗi số đó.

## 3. Các tính năng
### 3.1 Chi tiết Mua hàng/Sản xuất
Chứng từ mà từ đó Số serial được tạo sẽ được hiển thị. Nếu bạn mua nó từ một Nhà cung cấp, nó sẽ được liên kết tại đây.

### 3.2 Chi tiết Giao hàng
Nếu Số serial được tạo từ một Đơn bán hàng, Khách hàng sẽ được liên kết tại đây.

### 3.3 Chi tiết Bảo hành/AMC
Nếu Mặt hàng đang trong thời hạn bảo hành hoặc AMC (Hợp đồng bảo trì hàng năm), ngày hết hạn cho các mục này có thể được thiết lập.

### 3.4 Thông tin thêm
Bất kỳ thông tin bổ sung nào về đơn vị Mặt hàng cụ thể này có thể được thiết lập trong phần 'Serial No Details'.

## 4. Video
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/Q4tYKYTbVek" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 5. Các chủ đề liên quan
1. [Mã hóa Mặt hàng](articles/item-codification.md)
1. [Biến thể Mặt hàng](item-variants.md)
1. [Đặt tên Số serial](articles/serial-no-naming.md)