<!-- add-breadcrumbs -->
# Phiếu kho

**Phiếu kho cho phép bạn ghi lại sự luân chuyển Mặt hàng giữa các Kho.**

Để truy cập danh sách Phiếu kho, hãy đi đến:
> Home > Kho > Giao dịch kho > Phiếu kho

Phiếu kho có thể được lập cho các mục đích sau:

* **Xuất vật tư (Material Issue)**: Nếu vật tư được xuất cho một người nào đó trong hoặc ngoài công ty (Vật tư đi). Các Mặt hàng sẽ được trừ khỏi Kho được thiết lập trong Kho nguồn (Source Warehouse).
* **Nhập vật tư (Material Receipt)**: Nếu vật tư được nhận vào (Vật tư đến). Các Mặt hàng sẽ được thêm vào Kho được thiết lập trong Kho đích (Target Warehouse).
* **Chuyển vật tư (Material Transfer)**: Nếu vật tư được di chuyển từ Kho nội bộ này sang Kho nội bộ khác.
* **Chuyển vật tư để sản xuất (Material Transfer for Manufacturing)**: Nếu nguyên vật liệu được chuyển để sản xuất. Việc chuyển hàng có thể thực hiện dựa trên một [Lệnh sản xuất](manufacturing/work-order.md) hoặc một [Thẻ công việc](manufacturing/job-card.md). Để biết thêm, hãy truy cập trang [Định mức nguyên vật liệu](manufacturing/bill-of-materials.md).
* **Tiêu hao vật tư để sản xuất (Material Consumption for Manufacture)**: Có thể có nhiều phiếu kho tiêu hao cho một Lệnh sản xuất. [Tham khảo liên kết này để biết thêm chi tiết](manufacturing/articles/material_consumption.md)
* **Sản xuất (Manufacture)**: Nếu Vật tư được nhận từ một hoạt động Sản xuất/Gia công.
* **Đóng gói lại (Repack)**: Nếu Mặt hàng gốc được đóng gói lại thành mặt hàng mới.
* **Gửi cho bên gia công (Send to Subcontractor)**: Nếu Vật tư được xuất cho một hoạt động gia công ngoài. Phiếu này được lập từ một Đơn mua hàng. Để biết thêm, hãy truy cập trang [gia công](manufacturing/subcontracting.md).

Để biết thêm chi tiết về các loại mục đích phiếu kho, [hãy truy cập trang này](articles/stock-entry-purpose.md).


## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Phiếu kho, bạn nên tạo các mục sau trước:

* [Kho](warehouse.md)
* [Mặt hàng](item.md)


## 2. Cách tạo Phiếu kho
Phiếu kho cho mục đích Sản xuất thường được tạo từ một [Lệnh sản xuất](manufacturing/work-order.md). Để tạo Phiếu kho thủ công cho các mục đích khác, hãy làm theo các bước sau:

1. Đi đến danh sách Phiếu kho, nhấn vào Mới (New).
1. Chọn Mục đích Phiếu kho (Stock Entry Purpose) từ các mục được liệt kê ở trên.
1. Nếu bạn thiết lập Kho nguồn hoặc Kho đích mặc định, chúng sẽ tự động được điền cho các dòng trong bảng Mặt hàng.
1. Kho nguồn/đích sẽ khả dụng tùy theo Mục đích Phiếu kho mà bạn đã chọn.
1. Chọn các Mặt hàng và nhập số lượng.
1. Đơn giá cơ bản sẽ được lấy ra và số tiền sẽ được tính toán tự động.
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Stock Entry" src="https://docs.erpnext.com/docs/v16/assets/img/stock/stock-entry.png">

Thông thường, cả "Kho nguồn" và "Kho đích" đều được thiết lập để ghi lại một sự luân chuyển.

### 2.1 Các tùy chọn bổ sung khi tạo Phiếu kho

* **Lệnh sản xuất (Work Order)**: Nếu đây là một phiếu nhập liệu Sản xuất, Lệnh sản xuất sẽ được hiển thị trong trường này.
* **Chỉnh sửa Ngày và Giờ ghi sổ (Edit Posting Date and Time)**: Cho phép bạn chỉnh sửa ngày và giờ của Phiếu kho.
* **Yêu cầu kiểm tra (Inspection Required)**: Nếu cần thực hiện [Kiểm tra chất lượng](quality-inspection.md) đối với các Mặt hàng trước khi Xác nhận Phiếu kho.
* **Từ BOM (From BOM)**: Nếu đây là một phiếu nhập liệu Sản xuất, BOM liên quan của Mặt hàng đang được sản xuất sẽ được hiển thị.
* **Giữ chỗ tồn kho (Stock Reservation)**: Trong phiên bản v16, bạn có thể sử dụng tính năng này để giữ chỗ các Mặt hàng trong kho cho các đơn hàng hoặc lệnh sản xuất cụ thể, đảm bảo khả năng đáp ứng hàng hóa.

### 2.2 Loại Phiếu kho (Stock Entry Type)
Bạn cũng có thể tạo một Loại Phiếu kho mà chỉ có tên là khác đi, ví dụ 'Nhập phế liệu' (Scrap Entry). Mục đích vẫn là Chuyển vật tư nhưng tên gọi sẽ khác. Điều này hữu ích nếu bạn muốn một số Người dùng nhất định chỉ có quyền truy cập vào các hành động cụ thể liên quan đến kho.

![Stock Entry Type](https://docs.erpnext.com/docs/v16/assets/img/stock/stock-entry-type.png)

## 3. Các tính năng

### 3.1 Bảng Mặt hàng
Chi tiết về Mặt hàng, Đơn giá, Số lượng, v.v. sẽ được hiển thị ở đây.

* **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting)**: V16 hỗ trợ kế toán chi tiết hơn, cho phép theo dõi giá trị tồn kho chính xác đến từng mặt hàng cụ thể trong các giao dịch kho.
* **Xem trước sổ cái (Ledger Preview)**: Bạn có thể xem nhanh các bút toán (JE) liên quan trực tiếp từ giao diện Phiếu kho để kiểm tra việc hạch toán giữa tài khoản kho và tài khoản chi phí.

Việc tích vào 'Cho phép Giá trị tính giá bằng 0' (Allow Zero Valuation Rate) sẽ cho phép Xác nhận Phiếu nhập hàng ngay cả khi Giá trị tính giá của Mặt hàng là 0. Đây có thể là một mặt hàng mẫu hoặc do thỏa thuận chung với Nhà cung cấp của bạn.

Các Kho nguồn và Kho đích khác nhau có thể được thiết lập cho các Mặt hàng khác nhau.

### 3.2 Chi phí bổ sung (Landed Cost)
Nếu phiếu kho là phiếu nhập, tức là bất kỳ mặt hàng nào đang được nhận tại một kho đích, bạn có thể thêm các chi phí bổ sung liên quan (như Phí vận chuyển, Thuế hải quan, Chi phí vận hành, v.v.) gắn liền với quy trình. Trong v16, tính năng **Landed Cost cho Stock Entry** giúp phân bổ chính xác các chi phí này vào giá trị tồn kho của mặt hàng ngay khi thực hiện Phiếu kho.

Các Chi phí bổ sung đã thêm sẽ được phân bổ cho các mặt hàng nhận (nơi có Kho đích được đề cập) một cách tương ứng dựa trên Số tiền cơ bản của các mặt hàng. Và chi phí bổ sung được phân bổ sẽ được cộng vào đơn giá cơ bản của mặt hàng để tính Giá trị tính giá.

### 3.3 Truy xuất nguồn gốc (Traceability)
Với các Mặt hàng được quản lý theo **Lô hàng (Batch)** hoặc **Số sê-ri (Serial Number)**, bạn có thể sử dụng **Báo cáo truy xuất nguồn gốc Lô hàng/Số sê-ri (Serial/Batch Traceability Report)** để theo dõi toàn bộ lịch sử di chuyển của mặt hàng từ khi nhập kho đến khi xuất kho.

Số lượng và Đơn giá được hiển thị như sau khi bạn mở rộng bảng Mặt hàng.
<img class="screenshot" alt="Stock Entry Item Valuation Rate" src="https://docs.erpnext.com/docs/v16/assets/img/stock/stock-entry-item-valuation-rate.png">

### 3.4 Chiều kế toán (Accounting Dimensions)
Bạn có thể gắn thẻ các giao dịch khác nhau dựa trên các chiều kế toán đã thiết lập để phục vụ việc phân tích báo cáo tài chính và quản trị kho chuyên sâu.