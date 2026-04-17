# Có gì mới trong ERPNext v16

![Giao diện ERPNext v16](../workspace-home.png)

Chào mừng bạn đến với phiên bản ERPNext v16. Bản cập nhật này tập trung vào việc tối ưu hóa hiệu suất hệ thống, cải thiện trải nghiệm người dùng (UI/UX) và bổ sung các tính năng chuyên sâu cho quản lý sản xuất, kho vận và tài chính.

---

## 1. Giới thiệu tính năng (Mới trong v16)

Phiên bản v16 mang đến những bước nhảy vọt về công nghệ và quy trình nghiệp vụ:

*   **Hiệu năng tăng gấp 2 lần:** Tối ưu hóa cơ sở dữ liệu và cấu trúc backend giúp tốc độ tải trang và xử lý dữ liệu nhanh hơn 2 lần so với v15.
*   **Thiết kế lại giao diện (UI Redesign):** Giao diện người dùng hiện đại, trực quan và thân thiện hơn, giúp giảm thao tác chuột.
*   **Mẫu báo cáo tài chính (Financial Report Templates):** Cho phép tùy chỉnh linh hoạt các mẫu báo cáo tài chính mà không cần can thiệp sâu vào code.
*   **Hoạch định nhu cầu vật tư nâng cao (MRP):** Cải tiến thuật toán tính toán nhu cầu dựa trên kế hoạch sản xuất và tồn kho.
*   **Giữ chỗ tồn kho (Stock Reservation):** Tính năng mới cho phép giữ chỗ hàng hóa cho các Đơn bán hàng (SO) cụ thể, tránh tình trạng thiếu hụt khi có nhiều đơn hàng cùng lúc.
*   **Truy xuất nguồn gốc Lô hàng/Số Serial (Serial/Batch Traceability):** Nâng cấp khả năng theo dõi chi tiết vòng đời của Mặt hàng theo Lô hàng hoặc Số Serial.
*   **Gia công ngoài nhập kho (Inward Subcontracting):** Quy trình quản lý vật tư chuyển cho nhà cung cấp gia công và nhập lại thành phẩm hoàn thiện.
*   **Cải tiến Điểm bán hàng (POS improvements):** Giao diện POS mượt mà hơn, hỗ trợ tốt hơn cho các thiết bị di động và thanh toán nhanh.
*   **Nâng cấp Quản trị nhân sự (HRMS enhancements):** Bổ sung các module quản lý hiệu suất và đào tạo chuyên sâu.

## 2. Điều kiện tiên quyết

Để trải nghiệm tốt nhất các tính năng mới trong v16, bạn cần đảm bảo:
*   Hệ thống đã được nâng cấp lên phiên bản ERPNext v16.
*   Quyền truy cập (Role Permissions) đã được thiết lập cho các module mới (MRP, HRMS nâng cao).
*   Dữ liệu về Mặt hàng (Item) và Kho (Warehouse) đã được chuẩn hóa.

## 3. Hướng dẫn từng bước

Vì v16 là một bản cập nhật lớn bao gồm nhiều module, dưới đây là hướng dẫn tiếp cận các thay đổi quan trọng nhất:

### 3.1. Làm quen với Giao diện mới
1.  Đăng nhập vào hệ thống.
2.  Quan sát thanh điều hướng và Workspace mới đã được tinh chỉnh gọn gàng hơn.
3.  Sử dụng thanh tìm kiếm thông minh để truy cập nhanh các chứng từ như **Đơn bán hàng (SO)** hoặc **Hóa đơn (Invoice)**.

### 3.2. Thiết lập Giữ chỗ tồn kho (Stock Reservation)
1.  Truy cập vào **Mặt hàng (Item)**.
2.  Trong phần thiết lập kho, kích hoạt tùy chọn "Allow Stock Reservation".
3.  Khi tạo **Đơn bán hàng (SO)**, chọn mục "Reserve Stock" để hệ thống tự động giữ hàng trong **Kho (Warehouse)**.

### 3.3. Sử dụng Mẫu báo cáo tài chính mới
1.  Truy cập module **Kế toán (Accounting)**.
2.  Chọn **Báo cáo tài chính (Financial Report Templates)**.
3.  Sử dụng trình kéo thả để tùy chỉnh các dòng/cột cho **Bút toán (JE)** và các báo cáo tổng hợp.

### 3.4. Quy trình Gia công ngoài (Inward Subcontracting)
1.  Tạo **Đơn mua hàng (PO)** cho dịch vụ gia công.
2.  Tạo **Phiếu xuất kho (SE)** để chuyển nguyên vật liệu cho **Nhà cung cấp (Supplier)**.
3.  Khi nhận hàng, tạo **Phiếu nhập hàng (PR)** hoặc **Phiếu giao hàng (DN)** để ghi nhận thành phẩm đã hoàn thiện.

## 4. Ảnh minh họa

![Giao diện Workspace mới của ERPNext v16](../workspace-home.png)
*Hình 1: Giao diện Workspace được thiết kế lại giúp truy cập nhanh các module chính.*

## 5. Các tùy chọn/cài đặt liên quan

*   **Cài đặt Hệ thống (System Settings):** Kiểm tra các cấu hình về hiệu suất và bộ nhớ đệm.
*   **Cài đặt Kho (Stock Settings):** Kích hoạt tính năng truy xuất Lô hàng (Batch) và Số Serial.
*   **Cài đặt Nhân sự (HR Settings):** Cấu hình các quy trình đánh giá nhân sự mới.

## 6. Lưu ý quan trọng

*   **Sao lưu dữ liệu:** Luôn thực hiện sao lưu (Backup) toàn bộ cơ sở dữ liệu trước khi tiến hành nâng cấp lên v16.
*   **Kiểm tra tính tương thích:** Các tùy chỉnh (Custom Scripts/Client Scripts) cũ có thể cần được điều chỉnh để tương thích với UI mới.
*   **Hiệu suất:** Mặc dù hiệu năng tăng 2x, nhưng nếu dữ liệu quá lớn, hãy đảm bảo cấu hình Server đủ mạnh để tận dụng tối đa tốc độ mới.

## 7. Liên kết đến trang liên quan

*   [Hướng dẫn Quản lý Kho (Stock Management)](../stock/overview.md)
*   [Hướng dẫn Quản lý Sản xuất (Manufacturing/MRP)](../manufacturing/mrp_guide.md)
*   [Hướng dẫn Kế toán (Accounting)](../accounting/financial_reports.md)
*   [Hướng dẫn Bán hàng (Sales)](../sales/so_process.md)