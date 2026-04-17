<!-- add-breadcrumbs -->
# Cho phép Giao hàng/Lập hóa đơn vượt mức

Khi tạo Phiếu giao hàng, hệ thống sẽ kiểm tra xem số lượng mặt hàng có khớp với Đơn bán hàng hay không. Nếu số lượng mặt hàng đã vượt quá số lượng đặt hàng, bạn sẽ nhận được thông báo xác nhận về việc giao hàng hoặc nhập hàng vượt mức.

Trong trường hợp bán hàng, nếu bạn muốn có thể giao nhiều mặt hàng hơn so với số lượng đã nêu trong Đơn bán hàng, bạn nên cập nhật mục **"Allow over delivery or receipt upto this percent"** (Cho phép giao hàng hoặc nhập hàng vượt mức tối đa bao nhiêu phần trăm) trong danh mục Mặt hàng.

<img alt="Itemised Limit Percentage" class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/articles/limit-1.png">

Khi tạo Hóa đơn, đơn giá của mặt hàng cũng được kiểm tra dựa trên các giao dịch trước đó như Đơn bán hàng. Điều này cũng áp dụng khi tạo Phiếu nhập hàng hoặc Hóa đơn mua hàng từ Đơn mua hàng. Việc cập nhật "Allow over delivery or receipt upto this percent" sẽ có hiệu lực trong tất cả các giao dịch mua và bán.

**Ví dụ:** Nếu bạn đã đặt hàng 100 đơn vị của một Mặt hàng, và nếu tỷ lệ phần trăm nhập hàng vượt mức của Mặt hàng đó là 50%, thì bạn được phép lập Phiếu nhập hàng cho tối đa 150 đơn vị.

### Cấu hình mặc định cho toàn bộ hệ thống

Bạn có thể cập nhật giá trị chung cho "Allow over delivery or receipt upto this percent" từ Cài đặt kho. Giá trị được cập nhật tại đây sẽ áp dụng cho tất cả các Mặt hàng nếu không được thiết lập riêng lẻ.

1. Đi tới `Kho > Thiết lập > Cài đặt kho` ([Stock Settings](stock_settings.md)).
2. Thiết lập `Limit Percentage`.
3. **Lưu** Cài đặt kho.

<img alt="Item wise Allowance percentage" class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/articles/limit-2.png">

---

### Các tính năng mới trong v16 (Cập nhật)

Trong phiên bản v16, hệ thống quản lý kho đã được nâng cấp mạnh mẽ với các tính năng sau:

*   **Hệ thống Giữ hàng (Stock Reservation System):** Cho phép giữ trước số lượng tồn kho cho các Đơn bán hàng hoặc yêu cầu sản xuất, giúp đảm bảo hàng hóa luôn sẵn sàng cho các đơn hàng ưu tiên.
*   **Báo cáo Truy xuất nguồn gốc Lô hàng/Số Serial (Serial/Batch Traceability Report):** Theo dõi chi tiết lịch sử di chuyển của từng Lô hàng hoặc Số Serial từ khi nhập kho đến khi xuất kho, hỗ trợ kiểm soát chất lượng (QI) chặt chẽ hơn.
*   **Tính giá vốn hàng nhập kho (Landed Cost) cho Phiếu kho:** Cho phép phân bổ các chi phí liên quan (vận chuyển, thuế, phí bốc xếp...) trực tiếp vào giá trị của Mặt hàng khi thực hiện Phiếu nhập hàng, giúp phản ánh chính xác giá trị Tồn kho.
*   **Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting):** Cung cấp khả năng theo dõi chi tiết giá trị tài chính và bút toán (JE) cho từng Mặt hàng cụ thể trong kho.
*   **Xem trước Sổ cái (Ledger Preview):** Cho phép kiểm tra nhanh các bút toán liên quan trực tiếp từ giao diện phiếu kho hoặc hóa đơn trước khi thực hiện Xác nhận.