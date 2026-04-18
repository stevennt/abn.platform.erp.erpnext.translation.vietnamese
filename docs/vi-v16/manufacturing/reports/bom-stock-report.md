<!-- add-breadcrumbs -->
# Báo cáo tồn kho BOM

Để truy cập Báo cáo tồn kho BOM, hãy đi đến:

> Trang chủ > Sản xuất > Báo cáo > Báo cáo tồn kho BOM

<img class="screenshot" alt="Task" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/bom-stock-report.png">

Báo cáo tồn kho BOM cung cấp thông tin chi tiết về số lượng nguyên vật liệu cần thiết để sản xuất và số lượng thực tế đang có trong kho (dựa trên bộ lọc Kho được chọn). 

Trong phiên bản v16, báo cáo này được cải tiến để hỗ trợ quản lý sản xuất chính xác hơn:

*   **Trạng thái sẵn sàng:** Các mặt hàng có số lượng tồn kho không đủ để đáp ứng định mức BOM sẽ được hiển thị bằng **màu đỏ**. Các mặt hàng có đủ số lượng để sản xuất Mặt hàng BOM sẽ được hiển thị bằng **màu xanh lá cây**.
*   **Hệ thống Giữ hàng tồn kho (Stock Reservation System):** Báo cáo sẽ tính toán dựa trên số lượng thực tế có thể sử dụng, sau khi đã trừ đi các lượng hàng đã được giữ chỗ (reserved) cho các lệnh sản xuất hoặc đơn hàng khác.
*   **Truy xuất Lô hàng/Số Serial (Serial/Batch Traceability):** Hỗ trợ kiểm tra khả năng đáp ứng của các Lô hàng (Batch) cụ thể để đảm bảo tính liên tục trong sản xuất.
*   **Kế toán tồn kho theo Mặt hàng (Item-Level Stock Accounting):** Cung cấp cái nhìn sâu hơn về giá trị tồn kho của nguyên vật liệu phục vụ cho BOM.

{next}