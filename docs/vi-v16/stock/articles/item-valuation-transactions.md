<!-- add-breadcrumbs -->
# Phương pháp và Giao dịch Tính giá Mặt hàng

Trong ERPNext, giá trị tồn kho của Mặt hàng được cập nhật khi thực hiện các giao dịch liên quan đến nhập hoặc xuất kho.

### Các giao dịch ảnh hưởng đến giá trị tồn kho

Giá trị tồn kho của Mặt hàng sẽ được tính toán và cập nhật thông qua các giao dịch sau:

1.  **Phiếu nhập hàng (PR)**
2.  **Phiếu kho (SE)** (loại Nhập vật tư)
3.  **Phiếu giao hàng (DN)** (loại Xuất kho)
4.  **Đối chiếu tồn kho**: Được thực hiện để cập nhật số dư tồn kho thực tế và giá trị tồn kho đầu kỳ.

### Thiết lập Phương pháp tính giá

Bạn có thể chọn phương pháp tính giá dựa trên cách mà giá trị của mặt hàng sẽ được tính toán. Phương pháp tính giá có thể được thiết lập chung cho tất cả các mặt hàng từ **Cài đặt Kho**.

<img class="screenshot" alt="Thiết lập phương pháp tính giá trong Cài đặt Kho" src="https://docs.erpnext.com/docs/v16/assets/img/articles/item-valuation-1.png">

Bạn cũng có thể thiết lập riêng **Phương pháp tính giá** trong danh mục **Mặt hàng**, đặc biệt khi phương pháp tính giá cho một mặt hàng cụ thể khác với phương pháp mặc định của hệ thống.

<img class="screenshot" alt="Thiết lập phương pháp tính giá trong Mặt hàng" src="https://docs.erpnext.com/docs/v16/assets/img/articles/item-valuation-2.png">

**Lưu ý:** Một khi các **Bút toán (JE)** sổ cái đã được lập cho một Mặt hàng, tùy chọn phương pháp tính giá sẽ không còn hiển thị trong biểu mẫu Mặt hàng để đảm bảo tính nhất quán của dữ liệu kế toán.

### Các tính năng nâng cao trong v16

Phiên bản v16 mang đến những cải tiến quan trọng trong quản lý giá trị và kiểm soát tồn kho:

*   **Hệ thống Giữ chỗ Tồn kho (Stock Reservation System):** Cho phép giữ chỗ số lượng Mặt hàng cho các Đơn bán hàng (SO) hoặc yêu cầu cụ thể, giúp quản lý kế hoạch xuất kho chính xác hơn.
*   **Báo cáo Truy xuất nguồn gốc Lô hàng/Số sê-ri (Serial/Batch Traceability Report):** Cung cấp khả năng theo dõi chi tiết lịch sử di chuyển của từng Lô hàng hoặc Số sê-ri từ khi nhập kho đến khi xuất kho.
*   **Chi phí thu mua (Landed Cost) cho Phiếu kho (Stock Entry):** Cho phép phân bổ các chi phí liên quan (như vận chuyển, thuế nhập khẩu) trực tiếp vào giá trị của Mặt hàng trong Phiếu kho, giúp phản ánh chính xác giá trị tồn kho thực tế.
*   **Kế toán tồn kho theo cấp độ Mặt hàng (Item-Level Stock Accounting):** Tăng cường độ chính xác trong việc hạch toán giá trị tồn kho cho từng loại Mặt hàng cụ thể.
*   **Xem trước Bút toán (Ledger Preview):** Cho phép kiểm tra nhanh các bút toán kế toán liên quan đến giao dịch kho ngay tại giao diện giao dịch.

[Nhấp vào đây để tìm hiểu về các phương pháp tính giá có sẵn trong ERPNext và cách chúng hoạt động.](https://frappe.io/blog/erpnext-features/inventory-valuation-method-fifo-vs-moving-average)