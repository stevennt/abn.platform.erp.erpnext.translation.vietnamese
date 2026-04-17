<!-- add-breadcrumbs -->
# Số serial

Như đã thảo luận trong trang [Mặt hàng](item.md), nếu một **Mặt hàng** được *có số serial*, một bản ghi **Số serial** (Serial No) sẽ được duy trì cho mỗi đơn vị của **Mặt hàng** đó. Thông tin này giúp theo dõi vị trí của Số serial, thông tin bảo hành và thông tin hết hạn sử dụng (vòng đời).

**Số serial** cũng hữu ích để quản lý tài sản cố định. [Lịch bảo trì](https://docs.erpnext.com/docs/v16/user/manual/vi/support/maintenance-schedule) cũng có thể được tạo dựa trên Số serial để lập kế hoạch và sắp xếp hoạt động bảo trì cho các tài sản này (nếu chúng yêu cầu bảo trì).

Bạn cũng có thể theo dõi xem bạn đã mua **Số serial** đó từ **Nhà cung cấp** nào và đã bán nó cho **Khách hàng** nào. Trạng thái của **Số serial** sẽ cho bạn biết tình trạng tồn kho hiện tại của nó. Ngoài ra, với các tính năng mới trong v16, bạn có thể theo dõi chi tiết kế toán theo từng mặt hàng và xem trước bút toán liên quan.

Nếu Mặt hàng của bạn được *có số serial*, bạn sẽ phải nhập các Số serial vào cột liên quan với mỗi Số serial trên một dòng mới. Bạn có thể quản lý các đơn vị riêng lẻ của các mặt hàng có số serial bằng cách sử dụng Số serial.

Để truy cập danh sách Số serial, hãy đi tới:
> Trang chủ > Kho > Số serial và Lô hàng > Số serial

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Số serial, bạn nên tạo các mục sau trước:

* [Mặt hàng](item.md)
* Bật 'Has Serial No' trong danh mục Mặt hàng
    ![Serial No Enabled](https://docs.erpnext.com/docs/v16/assets/img/stock/serial-no-enabled.png)


## 2. Cách tạo Số serial
Thông thường, Số serial được tự động tạo khi các giao dịch được thực hiện đối với một Mặt hàng có số serial. Điều này chỉ hoạt động khi 'Has Serial No' được bật và một chuỗi số (series) đã được thiết lập trong danh mục Mặt hàng.

Ví dụ, một chuỗi số đã được thiết lập cho Mặt hàng sau là 'PB2L.#####'. Sau đó, một **Phiếu kho** được **Xác nhận** để nhập Mặt hàng. Các Số serial đã được tạo tương ứng.

![Serial No Created](https://docs.erpnext.com/docs/v16/assets/img/stock/serial-no-created.png)

Tuy nhiên, nếu bạn muốn tạo Số serial *thủ công*, hãy làm theo các bước sau:

1. Đi tới danh sách Số serial, nhấn vào Mới.
1. Nhập một Số serial.
1. Nhập Mã mặt hàng và các chi tiết sẽ được lấy ra.
1. Nếu có bất kỳ giao dịch nào được thực hiện với một mặt hàng, Số serial không thể được thiết lập hoặc hủy thiết lập.
1. **Lưu**.

Tồn kho của một Mặt hàng chỉ có thể bị ảnh hưởng nếu Số serial được giao dịch thông qua một giao dịch Kho (**Phiếu kho**, **Phiếu nhập hàng**, **Phiếu giao hàng**, **Hóa đơn**). Khi một Số serial mới được tạo trực tiếp, Kho của nó không thể được thiết lập.

<img class="screenshot" alt="Serial Number" src="https://docs.erpnext.com/docs/v16/assets/img/stock/serial-no.png">

### 2.1 Lưu ý về Số serial

* Trạng thái được thiết lập dựa trên **Phiếu kho**.
* Chỉ những Số serial có trạng thái 'Available' (Sẵn có) mới có thể được giao.
* Số serial có thể được tự động tạo từ **Phiếu kho** hoặc **Phiếu nhập hàng**. Nếu bạn ghi Số serial vào cột Số serial, hệ thống sẽ tự động tạo các số serial đó.
* Nếu trong danh mục Mặt hàng có ghi Chuỗi số serial, bạn có thể để trống cột Số serial trong **Phiếu kho** / **Phiếu nhập hàng**. Các Số serial sẽ tự động được thiết lập từ chuỗi số đó.
* **Hệ thống Giữ chỗ Tồn kho (Stock Reservation System):** Trong v16, Số serial có thể được giữ chỗ để đảm bảo sẵn sàng cho các đơn hàng hoặc yêu cầu vật tư sắp tới.

## 3. Các tính năng mới và nâng cao (v16)
### 3.1 Chi tiết Mua hàng/Sản xuất
Chứng từ mà từ đó Số serial được tạo sẽ được hiển thị. Nếu bạn mua nó từ một **Nhà cung cấp**, nó sẽ được liên kết tại đây.

### 3.2 Chi tiết Giao hàng
Nếu Số serial được tạo từ một **Đơn bán hàng**, **Khách hàng** sẽ được liên kết tại đây.

### 3.3 Chi tiết Bảo hành/AMC
Nếu Mặt hàng đang trong thời hạn bảo hành hoặc AMC (Hợp đồng bảo trì hàng năm), ngày hết hạn cho các mục này có thể được thiết lập.

### 3.4 Báo cáo Truy xuất nguồn gốc (Serial/Batch Traceability Report)
Tính năng mới trong v16 cho phép bạn theo dõi toàn bộ lịch sử di chuyển của một Số serial từ khi nhập kho, qua các lần chuyển kho, sản xuất cho đến khi xuất bán.

### 3.5 Kế toán và Kiểm soát Tồn kho nâng cao
* **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Theo dõi giá trị và giá vốn chính xác hơn cho từng đơn vị có số serial.
* **Xem trước Bút toán (Ledger Preview):** Cho phép kiểm tra nhanh các **Bút toán** liên quan đến giá trị của Số serial ngay tại giao diện quản lý.
* **Landed Cost cho Phiếu kho:** Tính toán chi phí nhập hàng (vận chuyển, thuế...) trực tiếp vào giá trị của Số serial khi thực hiện **Phiếu nhập hàng**.

## 4. Video
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/Q4tYKYTbVek" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 5. Các chủ đề liên quan
1. [Mã hóa Mặt hàng](articles/item-codification.md)
1. [Biến thể Mặt hàng](item-variants.md)
1. [Đặt tên Số serial](articles/serial-no-naming.md)