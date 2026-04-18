<!-- add-breadcrumbs -->
# Đặt tên Số serial

Số serial là giá trị duy nhất được gán cho mỗi đơn vị của một mặt hàng. Số serial giúp theo dõi chi tiết bảo hành, lịch sử di chuyển và hạn sử dụng của mặt hàng. Thông thường, các mặt hàng có giá trị cao như máy móc, máy tính, thiết bị đắt tiền sẽ được quản lý theo số serial.

Trong phiên bản v16, việc quản lý số serial được kết hợp chặt chẽ với hệ thống **Hệ thống giữ hàng (Stock Reservation System)** và **Báo cáo truy xuất nguồn gốc Lô/Số serial (Serial/Batch Traceability Report)** để đảm bảo tính chính xác tuyệt đối trong quản lý tồn kho.

Để thiết lập mặt hàng là có quản lý theo số serial, trong danh mục [Mặt hàng](item.md), hãy tích chọn **Has Serial No**.

Có hai cách để số serial có thể được tạo trong ERPNext.

### 1. Quản lý số serial cho hàng mua về

Nếu các mặt hàng mua về đã được nhà sản xuất gốc (OEM) áp số serial, bạn có thể sử dụng chính số serial đó trong ERPNext. Khi tạo [PR](pr.md) (Phiếu nhập hàng), bạn sẽ quét mã hoặc nhập thủ công các số serial cho một mặt hàng. Khi **Xác nhận** [PR](pr.md), các Số serial sẽ được ghi nhận vào hệ thống. Nếu sử dụng số serial của OEM, thì trong danh mục [Mặt hàng](item.md), không nên điền Tiền tố (Prefix) cho việc quản lý số serial. Trong trường hợp này, trường Prefix nên được để trống.

Nếu các mặt hàng nhận về đã có mã vạch số serial, bạn chỉ cần quét mã vạch đó để nhập Số serial vào [PR](pr.md). Nhấp [vào đây](https://frappe.io/blog/management/using-barcodes-to-ease-data-entry) để tìm hiểu thêm về vấn đề này.

Khi **Xác nhận** [PR](pr.md) hoặc [SE](stock_entry.md) (Phiếu kho) cho mặt hàng có quản lý số serial, các Số serial sẽ được cập nhật vào hệ thống. Với tính năng mới trong v16, bạn có thể theo dõi chi tiết giá trị hàng tồn kho theo từng số serial thông qua **Kế toán tồn kho theo mặt hàng (Item-Level Stock Accounting)**.

<img alt="Serial Nos Entry" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/serial-naming-1.png">

Các số serial đã tạo sẽ được cập nhật cho từng mặt hàng.

<img alt="Serial Nos Created" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/serial-naming-2.png">

### 2. Quản lý số serial cho hàng sản xuất

Để quản lý số serial cho hàng sản xuất, bạn có thể định nghĩa Chuỗi (Series) để tạo Số serial ngay trong danh mục [Mặt hàng](item.md). Theo chuỗi đó, hệ thống sẽ tạo các Số serial cho Mặt hàng khi có lệnh sản xuất được thực hiện.

#### 2.1 Chuỗi Số serial

Khi Mặt hàng được thiết lập là có quản lý số serial, hệ thống sẽ cho phép bạn điền Chuỗi (Series) cho mặt hàng đó.

<img alt="Serial Nos Created" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/serial-naming-3.png">

#### 2.2 Tạo số serial khi sản xuất

Khi **Xác nhận** lệnh sản xuất hoặc [SE](stock_entry.md) (Phiếu kho) cho mặt hàng sản xuất, hệ thống sẽ tự động tạo các Số serial theo Chuỗi đã được chỉ định trong danh mục [Mặt hàng](item.md).

Trong phiên bản v16, khi thực hiện các nghiệp vụ này, bạn có thể sử dụng tính năng **Xem trước sổ cái (Ledger Preview)** để kiểm tra ngay các [Bút toán](journal_entry.md) liên quan đến giá trị của từng số serial cụ thể.

<img alt="Serial Nos Created" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/serial-naming-4.png">

---
**Lưu ý nâng cao trong v16:**
* **Hệ thống giữ hàng (Stock Reservation System):** Giúp giữ chỗ các số serial cụ thể cho các [SO](sales_order.md) (Đơn bán hàng) để tránh việc xuất nhầm hàng hoặc thiếu hàng.
* **Báo cáo truy xuất (Traceability Report):** Cho phép bạn xem toàn bộ lịch sử của một số serial từ lúc nhập kho ([PR](pr.md)), qua các lần chuyển [Kho](warehouse.md), cho đến khi xuất bán ([DN](delivery_note.md)).
* **Chi phí thu mua (Landed Cost):** Bạn có thể phân bổ chi phí vận chuyển, thuế vào từng [SE](stock_entry.md) (Phiếu kho) nhập hàng, giúp giá trị của từng số serial phản ánh đúng giá vốn thực tế.