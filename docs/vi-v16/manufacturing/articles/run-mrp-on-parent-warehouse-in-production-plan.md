# Tài liệu ERPNext v16

Chào mừng bạn đến với tài liệu hướng dẫn sử dụng ERPNext phiên bản 16. Tài liệu này đã được cập nhật các tính năng mới nhất nhằm tối ưu hóa quy trình quản lý kho và kế toán.

## 1. Quản lý Tồn kho (Stock Management)

Trong phiên bản v16, hệ thống quản lý tồn kho đã được nâng cấp mạnh mẽ với các tính năng kiểm soát chính xác hơn.

### 1.1. Hệ thống Giữ hàng (Stock Reservation System)
Tính năng mới cho phép bạn giữ hàng hóa cho các **Đơn bán hàng (SO)** hoặc **Đơn mua hàng (PO)** cụ thể. Khi thực hiện **Giữ hàng**, số lượng này sẽ được tách biệt để đảm bảo hàng luôn sẵn sàng cho các đơn hàng đã cam kết, tránh tình trạng thiếu hụt khi thực hiện xuất kho.

### 1.2. Báo cáo Truy xuất Lô hàng & Số Serial (Serial/Batch Traceability Report)
Cải tiến khả năng truy xuất nguồn gốc. Bạn có thể theo dõi toàn bộ vòng đời của một **Mặt hàng (Item)** từ khi nhập kho qua **Phiếu nhập hàng (PR)**, qua các lần **Kiểm tra chất lượng (QI)**, cho đến khi xuất kho qua **Phiếu giao hàng (DN)** dựa trên số **Lô hàng (Batch)** hoặc số **Serial**.

### 1.3. Chi phí thu mua (Landed Cost) cho Phiếu kho (Stock Entry)
Cho phép phân bổ các chi phí liên quan đến vận chuyển, thuế và phí bốc dỡ trực tiếp vào giá trị của **Mặt hàng (Item)** ngay khi thực hiện **Phiếu kho (SE)** hoặc **Phiếu nhập hàng (PR)**. Điều này giúp giá trị **Tồn kho (Stock)** phản ánh chính xác giá trị thực tế của hàng hóa.

### 1.4. Kế toán Tồn kho theo từng Mặt hàng (Item-Level Stock Accounting)
Nâng cấp khả năng hạch toán chi tiết. Hệ thống cho phép theo dõi giá trị tồn kho và các bút toán liên quan đến từng **Mặt hàng (Item)** cụ thể một cách minh bạch, giúp việc đối soát với **Bút toán (JE)** trở nên dễ dàng hơn.

---

## 2. Quy trình Nghiệp vụ chính

### 2.1. Quy trình Mua hàng (Procurement)
1. Tạo **Đơn mua hàng (PO)** dựa trên nhu cầu.
2. Thực hiện **Phiếu nhập hàng (PR)** khi hàng về đến kho.
3. Thực hiện **Kiểm tra chất lượng (QI)** để xác nhận hàng đạt chuẩn.
4. **Xác nhận (Submit)** **Hóa đơn (Invoice)** từ **Nhà cung cấp (Supplier)**.
5. Thực hiện **Thanh toán (Payment)** cho **Nhà cung cấp (Supplier)**.

### 2.2. Quy trình Bán hàng (Sales)
1. Tạo **Đơn bán hàng (SO)**.
2. Sử dụng tính năng **Giữ hàng (Stock Reservation)** để đảm bảo hàng hóa.
3. Tạo **Phiếu giao hàng (DN)** để xuất kho.
4. Xuất **Hóa đơn (Invoice)** cho **Khách hàng (Customer)**.
5. Ghi nhận **Thanh toán (Payment)** từ **Khách hàng (Customer)**.

---

## 3. Kế toán & Kiểm soát (Accounting & Control)

### 3.1. Xem trước Sổ cái (Ledger Preview)
Tính năng mới cho phép người dùng xem nhanh các **Bút toán (JE)** liên quan trực tiếp từ các chứng từ như **Hóa đơn (Invoice)** hoặc **Phiếu kho (SE)** mà không cần phải chuyển sang phân hệ Kế toán tổng hợp.

### 3.2. Quản lý Kho (Warehouse Management)
*   **Kho (Warehouse):** Quản lý đa kho, đa vị trí.
*   **Lô hàng (Batch):** Quản lý hạn sử dụng và số lô để kiểm soát chất lượng.
*   **Yêu cầu vật tư (MR):** Tạo yêu cầu chuyển hàng hoặc xuất hàng nội bộ.

---

## 4. Phụ lục & Liên kết nhanh

*   [Hướng dẫn thiết lập Mặt hàng (.md)](item_setup.md)
*   [Quy trình Quản lý Kho (.md)](stock_management.md)
*   [Hướng dẫn Kế toán bán hàng (.md)](sales_accounting.md)
*   [Hướng dẫn Kế toán mua hàng (.md)](purchase_accounting.md)