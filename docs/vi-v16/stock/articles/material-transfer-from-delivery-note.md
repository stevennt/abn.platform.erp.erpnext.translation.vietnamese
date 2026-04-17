<!-- add-breadcrumbs -->
# Chuyển vật tư từ Phiếu giao hàng và Phiếu nhập hàng

Trong ERPNext, bạn có thể tạo bút toán Chuyển vật tư từ chứng từ [Phiếu kho](../stock-entry.md). Tuy nhiên, có một số trường hợp việc Chuyển vật tư cần được thể hiện dưới dạng Phiếu giao hàng và Phiếu nhập hàng để phù hợp với quy trình vận hành và quản lý tồn kho chuyên sâu.

## Chuyển vật tư từ Phiếu giao hàng

### Các trường hợp

1. **Chuyển vật tư nội bộ giữa các kho:** Ví dụ, khi bạn chuyển vật tư từ kho chính đến công trường dự án, bạn cần xuất trình Phiếu giao hàng cho đơn vị tiếp nhận.
2. **Quản lý thuế và pháp lý:** Có những yêu cầu pháp lý về việc thuế phải được áp dụng cho mỗi lần chuyển vật tư. Việc quản lý sẽ dễ dàng hơn trong một giao dịch như Phiếu giao hàng so với Phiếu kho.
3. **Hệ thống Giữ hàng (Stock Reservation):** Với tính năng mới trong v16, việc sử dụng Phiếu giao hàng giúp đồng bộ hóa trạng thái giữ hàng cho các đơn hàng đã đặt.

### Các bước thực hiện

#### Kích hoạt Kho mục tiêu

DocType Phiếu giao hàng mặt hàng (Delivery Note Item) có một trường ẩn là Kho mục tiêu (Target Warehouse) (trước đây là Kho khách hàng - Customer Warehouse). Bạn có thể kích hoạt nó từ [Thiết lập kho](../stock-settings.md) bằng cách bật tùy chọn "Allow Material Transfer From Delivery Note and Sales Invoice".

**Lưu ý:** Khách hàng được chọn phải đại diện cho cùng một công ty. Để thực hiện việc này, hãy bật tùy chọn 'Is Internal Customer' trong biểu mẫu Khách hàng và chọn công ty của bạn trong trường 'Represents Company'.

#### Chọn Kho

Khi tạo Phiếu giao hàng để Chuyển vật tư, đối với một Mặt hàng, hãy chọn kho nguồn là Kho xuất (From Warehouse).

Trong Kho khách hàng (Customer Warehouse), hãy chọn một Kho nơi vật tư sẽ được chuyển đến hoặc chọn một kho mục tiêu.

<img class="screenshot" alt="Delivery Note Material Transfer" src="../assets/img/stock/customer-warehouse-2.png">

Khi **Xác nhận** Phiếu giao hàng, tồn kho của mặt hàng sẽ được trừ khỏi "Kho xuất" và cộng vào "Kho khách hàng".

---

## Chuyển vật tư từ Phiếu nhập hàng

### Các trường hợp

1. **Quản lý thuế:** Tương tự như Phiếu giao hàng, việc áp dụng thuế cho các giao dịch chuyển vật tư sẽ được quản lý dễ dàng hơn thông qua Phiếu nhập hàng.
2. **Tính giá vốn hàng nhập (Landed Cost):** Trong v16, việc sử dụng Phiếu nhập hàng cho phép bạn áp dụng chi phí liên quan (Landed Cost) trực tiếp vào giá trị tồn kho của Mặt hàng, giúp phản ánh chính xác giá trị thực tế của vật tư khi nhập kho.
3. **Truy xuất nguồn gốc (Traceability):** Kết hợp với tính năng Báo cáo truy xuất nguồn gốc theo Lô hàng/Số sê-ri (Serial/Batch Traceability Report), việc chuyển vật tư qua Phiếu nhập hàng giúp kiểm soát chặt chẽ lịch sử biến động của từng lô hàng.

### Các bước thực hiện

#### Kích hoạt Kho nhà cung cấp

Tương tự như Kho khách hàng, bước đầu tiên là kích hoạt Kho nhà cung cấp (Supplier Warehouse) từ [Thiết lập kho](../stock-settings.md).

**Lưu ý:** Nhà cung cấp được chọn phải đại diện cho cùng một công ty. Hãy bật tùy chọn 'Is Internal Supplier' trong biểu mẫu Nhà cung cấp và chọn công ty của bạn trong trường 'Represents Company'.

#### Chọn Kho

Khi tạo Phiếu nhập hàng để Chuyển vật tư, đối với một Mặt hàng, hãy chọn kho mục tiêu là Kho nhận (Accepted Warehouse).

Đây là cách bạn tạo một Phiếu nhập hàng nội bộ từ một Phiếu giao hàng nội bộ:

<img class="screenshot" alt="Purchase Receipt Material Transfer" src="../assets/img/stock/supplier-warehouse-1.png">

Trong Kho nhà cung cấp (Supplier Warehouse), hãy chọn một Kho nơi vật tư sẽ được chuyển đi.

<img class="screenshot" alt="Purchase Receipt Material Transfer" src="../assets/img/stock/supplier-warehouse.png">

Khi **Xác nhận** Phiếu nhập hàng, tồn kho của mặt hàng sẽ được trừ khỏi "Kho nhà cung cấp" và cộng vào "Kho nhận". Với tính năng Kế toán tồn kho theo từng mặt hàng (Item-Level Stock Accounting) trong v16, các bút toán này sẽ được ghi nhận chính xác vào sổ cái ngay khi bạn xem trước bút toán (Ledger Preview).