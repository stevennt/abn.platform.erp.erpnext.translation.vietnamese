<!-- add-breadcrumbs -->
# Kế toán Tồn kho

Giá trị của hàng tồn kho hiện có được coi là Tài sản ngắn hạn trong [Hệ thống tài khoản](../accounts/chart-of-accounts.md) của công ty. Để lập Bảng cân đối kế toán, bạn nên thực hiện các bút toán kế toán cho các tài sản đó. ERPNext v16 cung cấp các phương pháp quản lý linh hoạt giữa kiểm kê thường xuyên và kiểm kê định kỳ với các tính năng nâng cao về báo cáo và tự động hóa.

## 1. Kiểm kê thường xuyên (Auto/Perpetual Inventory)

Trong quy trình này, đối với mỗi giao dịch kho, hệ thống sẽ ghi các bút toán kế toán liên quan để đồng bộ số dư kho và số dư kế toán. Đây là thiết lập mặc định trong ERPNext. Theo mặc định, Kiểm kê thường xuyên được bật trong [Công ty](setup/company-setup).

Khi bạn mua và nhận hàng (thông qua [PR](../stock/purchase-receipt.md) hoặc [PO](../stock/purchase-order.md)), các mặt hàng đó được ghi nhận là tài sản của công ty (tồn kho). Khi bạn bán và giao các mặt hàng đó (thông qua [DN](../stock/delivery-note.md)), một khoản chi phí (Giá vốn hàng bán - COGS) tương đương với giá trị của các mặt hàng sẽ được ghi nhận. 

**Các điểm mới và cải tiến trong v16:**
* **Tách biệt chi phí:** Hệ thống cho phép tách biệt rõ ràng giữa Giá vốn hàng bán (COGS) và Chi phí dịch vụ (Service Expenses) để báo cáo chính xác hơn.
* **Xem trước Sổ cái (Ledger Preview):** Trước khi thực hiện **Xác nhận (Submit)** một giao dịch kho, người dùng có thể xem trước các [Bút toán (JE)](../accounts/journal-entry.md) sẽ được tạo ra để đảm bảo tính chính xác.
* **Tự động tính giá tồn kho (Automatic Closing Stock):** Hệ thống hỗ trợ tự động hóa việc tính toán giá trị tồn kho cuối kỳ, giúp việc chốt sổ nhanh chóng và chính xác hơn.

Các bút toán Sổ cái được tạo ra sau mỗi giao dịch kho. Kết quả là, giá trị theo Sổ cái kho luôn khớp với số dư tài khoản liên quan. Điều này giúp cải thiện độ chính xác của Bảng cân đối kế toán và Báo cáo kết quả hoạt động kinh doanh.

Đọc [tài liệu về Kiểm kê thường xuyên](perpetual-inventory.md) để kiểm tra các bút toán kế toán cho một giao dịch kho cụ thể.

### 1.2 Ưu điểm của Kiểm kê thường xuyên

Hệ thống Kiểm kê thường xuyên giúp bạn dễ dàng duy trì tính chính xác của các giá trị tài sản và chi phí của công ty. Số dư [Kho (Warehouse)](../stock/warehouse.md) sẽ luôn được đồng bộ với số dư tài khoản liên quan, vì vậy không cần phải thực hiện nhập liệu thủ công định kỳ để cân đối chúng.

Trong trường hợp có các giao dịch kho mới lùi ngày hoặc **Hủy (Cancel)** một giao dịch hiện có, tất cả các bút toán Sổ cái kho và Bút toán Sổ cái trong tương lai sẽ được tính toán lại cho tất cả các [Mặt hàng (Item)](../stock/item.md) của giao dịch đó. Điều tương tự cũng áp dụng nếu có bất kỳ chi phí nào được thêm vào [Phiếu nhập hàng (PR)](../stock/purchase-receipt.md) đã **Xác nhận (Submit)** sau đó thông qua Chứng từ chi phí chuyển đến.

> **Lưu ý:** Kiểm kê thường xuyên phụ thuộc hoàn toàn vào giá trị tính giá của mặt hàng. Do đó, bạn phải cẩn thận hơn khi nhập giá trị tính giá khi thực hiện bất kỳ giao dịch nhập kho nào như [Phiếu nhập hàng (PR)](../stock/purchase-receipt.md), [Phiếu nhập vật tư (MR)](../stock/material-request.md), hoặc Sản xuất/Đóng gói lại.

---

## 2. Kiểm kê định kỳ (Periodic Inventory)

Trong phương pháp này, các bút toán kế toán cần được tạo thủ công để đồng bộ số dư kho và số dư tài khoản liên quan. Hệ thống không tự động tạo các bút toán kế toán cho tài sản tại thời điểm mua hoặc bán vật tư.

Trong một kỳ kế toán, khi bạn mua và nhận hàng, một khoản chi phí được ghi nhận trong hệ thống kế toán của bạn. Bạn bán và giao một số mặt hàng này. Vào cuối kỳ kế toán, tổng giá trị của các mặt hàng dự kiến bán cần được ghi nhận là tài sản của công ty (tồn kho).

**Các tính năng hỗ trợ trong v16:**
* **Kế toán định kỳ (Periodic Accounting):** Hỗ trợ các quy trình ghi nhận chi phí và tài sản theo chu kỳ thay vì theo từng giao dịch đơn lẻ.
* **Báo cáo tài chính hợp nhất (Consolidated Trial Balance):** Cho phép tổng hợp Bảng cân đối số phát sinh từ nhiều công ty hoặc chi nhánh khác nhau, giúp quản lý kiểm kê định kỳ ở quy mô tập đoàn dễ dàng hơn.
* **Mẫu báo cáo tài chính (Financial Report Templates):** Cho phép tùy chỉnh các mẫu báo cáo để phù hợp với cách tính toán giá trị tồn kho định kỳ đặc thù của doanh nghiệp.

Sự chênh lệch giữa giá trị của các mặt hàng còn lại để bán và giá trị tồn kho của kỳ trước có thể là số dương hoặc số âm. Nếu là số dương, giá trị này được trừ vào chi phí (Giá vốn hàng bán) và được cộng vào tài sản (tồn kho). Nếu là số âm, một bút toán ngược sẽ được thực hiện.

Nếu bạn là người dùng hiện tại đang sử dụng Kiểm kê định kỳ và muốn chuyển sang Kiểm kê thường xuyên, bạn cần thực hiện [một vài bước](articles/migrate-to-perpetual-inventory.md) để chuyển đổi.

---

## 3. Các chủ đề liên quan
1. [Kiểm kê thường xuyên](perpetual-inventory.md)
2. [Chuyển đổi sang Kiểm kê thường xuyên](articles/migrate-to-perpetual-inventory.md)
3. [Quản lý Kho và Lô hàng](stock/batch-wise-inventory.md)