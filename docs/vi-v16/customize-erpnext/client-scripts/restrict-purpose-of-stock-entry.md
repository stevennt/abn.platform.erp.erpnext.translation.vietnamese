<!-- add-breadcrumbs -->
# Hạn chế Mục đích của Phiếu kho

Để kiểm soát quy trình vận hành và đảm bảo tính chính xác của dữ liệu tồn kho, bạn có thể thiết lập các quy tắc kiểm tra (validation) dựa trên người dùng và mục đích của phiếu.

Dưới đây là đoạn mã script để giới hạn người dùng cụ thể chỉ được phép tạo **Phiếu yêu cầu vật tư (MR)** với mục đích là **Nhận vật tư (Material Receipt)**.

```javascript
frappe.ui.form.on("Material Request", "validate", function(frm) {
    // Kiểm tra nếu người dùng là 'user1@example.com' 
    // và mục đích (purpose) không phải là 'Material Receipt'
    if(frappe.user == "user1@example.com" && frm.doc.purpose != "Material Receipt") {
        frappe.msgprint(__("Bạn chỉ được phép thực hiện Nhận vật tư"));
        frappe.throw(__("Không được phép"));
    }
});
```

### Giải thích các tính năng mới trong ERPNext v16 liên quan đến quản lý kho:

Trong phiên bản v16, việc quản lý **Tồn kho (Stock)** đã được nâng cấp mạnh mẽ để hỗ trợ các doanh nghiệp có quy trình phức tạp:

*   **Hệ thống Giữ hàng (Stock Reservation System):** Cho phép giữ trước **Mặt hàng (Item)** trong **Kho (Warehouse)** cho các **Đơn bán hàng (SO)** hoặc các yêu cầu khác, giúp tránh tình trạng thiếu hụt hàng khi thực hiện xuất kho.
*   **Báo cáo Truy xuất nguồn gốc Lô hàng/Số Serial (Serial/Batch Traceability Report):** Cung cấp khả năng theo dõi chi tiết lịch sử của từng **Lô hàng (Batch)** hoặc số Serial từ khi nhập kho (PR) cho đến khi xuất kho hoặc bán hàng.
*   **Chi phí thu mua (Landed Cost) cho Phiếu kho (Stock Entry):** Cho phép phân bổ các chi phí liên quan (vận chuyển, thuế, phí bốc xếp...) trực tiếp vào giá trị của **Mặt hàng (Item)** ngay khi thực hiện **Phiếu kho (SE)**, giúp tính toán giá vốn chính xác hơn.
*   **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Tự động hóa việc ghi nhận các **Bút toán (JE)** chi tiết cho từng loại mặt hàng, giúp việc đối soát giữa sổ cái và kho trở nên dễ dàng.
*   **Xem trước Sổ cái (Ledger Preview):** Cho phép người dùng xem nhanh các tác động của giao dịch đối với sổ cái ngay tại giao diện phiếu trước khi nhấn **Xác nhận (Submit)**.

---
[Quay lại danh sách tài liệu](../README.md)