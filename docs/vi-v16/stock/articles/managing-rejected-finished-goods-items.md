<!-- add-breadcrumbs -->
# Quản lý các Mặt hàng Thành phẩm bị Loại bỏ

Có thể có những Mặt hàng được sản xuất nhưng không vượt qua được kiểm tra chất lượng (QI), do đó bị loại bỏ.

Quy trình sản xuất tiêu chuẩn trong ERPNext không bao gồm việc quản lý các mặt hàng bị loại bỏ một cách riêng biệt. Vì vậy, bạn nên tạo phiếu nhập thành phẩm cho cả các mặt hàng được chấp nhận cũng như các mặt hàng bị loại bỏ. Bằng cách này, các mặt hàng bị loại bỏ cũng sẽ được ghi nhận là đã nhập vào kho thành phẩm.

Để chuyển các mặt hàng bị loại bỏ từ kho thành phẩm, bạn nên tạo một [Phiếu kho](stock_entry.md) (Material Transfer). Các bước dưới đây để tạo phiếu Phiếu kho.

#### Bước 1: Tạo Phiếu kho mới

`Kho > Tài liệu > Phiếu kho > Mới`

#### Bước 2: Thiết lập Mục đích

**Mục đích** = Chuyển kho (Material Transfer)

#### Bước 3: Thiết lập Kho

*   **Kho nguồn** = Kho thành phẩm
*   **Kho đích** = Kho hàng lỗi/loại bỏ

*Lưu ý: Việc tách biệt kho giúp bạn dễ dàng theo dõi báo cáo [Tồn kho](stock.md) và quản lý [Lô hàng](batch.md) chính xác hơn.*

#### Bước 4: Chọn Mặt hàng

Chọn **Mặt hàng** không vượt qua kiểm tra chất lượng, và nhập tổng số lượng mặt hàng bị loại bỏ vào ô **Số lượng**.

#### Bước 5: Lưu và Xác nhận Phiếu kho

Sau khi kiểm tra thông tin, nhấn **Lưu** và sau đó nhấn **Xác nhận**. Khi đó, tồn kho của các mặt hàng bị loại bỏ sẽ được chuyển từ Kho thành phẩm sang Kho hàng lỗi/loại bỏ.

---
**Tính năng mới trong v16 áp dụng cho quy trình này:**
*   **Truy xuất nguồn gốc Lô hàng/Số sê-ri (Serial/Batch Traceability Report):** Giúp bạn theo dõi chính xác lô hàng lỗi này được sản xuất từ lệnh sản xuất nào.
*   **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Đảm bảo giá trị của hàng lỗi được hạch toán chính xác vào các tài khoản kho tương ứng thông qua [Bút toán](journal_entry.md) tự động.