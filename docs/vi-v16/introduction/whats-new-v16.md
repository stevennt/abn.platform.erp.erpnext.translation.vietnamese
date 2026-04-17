# Có gì mới trong ERPNext v16

![Giao diện ERPNext v16](../workspace-home.png)

Chào mừng bạn đến với phiên bản ERPNext v16. Bản cập nhật này tập trung mạnh mẽ vào việc tối ưu hóa hiệu suất hệ thống, cải thiện trải nghiệm người dùng (UI/UX) và bổ sung các tính năng quản trị chuyên sâu cho Sản xuất, Kho và Nhân sự.

---

## 1. Giới thiệu tính năng (Mới trong v16)

Phiên bản v16 mang đến những bước nhảy vọt về công nghệ và nghiệp vụ:

*   **Hiệu năng vượt trội (2x Speed):** Tối ưu hóa cơ sở dữ liệu và cấu trúc backend giúp tốc độ xử lý nhanh gấp đôi so với phiên bản cũ.
*   **Thiết kế giao diện mới (UI Redesign):** Giao diện hiện đại, trực quan, giúp người dùng dễ dàng thao tác và tìm kiếm thông tin.
*   **Mẫu báo cáo tài chính (Financial Report Templates):** Cho phép tùy chỉnh linh hoạt các mẫu báo cáo tài chính mà không cần can thiệp sâu vào code.
*   **Hoạch định sản xuất nâng cao (MRP):** Cải tiến quy trình lập kế hoạch nhu cầu nguyên vật liệu dựa trên lệnh sản xuất và tồn kho thực tế.
*   **Giữ chỗ tồn kho (Stock Reservation):** Tính năng cho phép giữ hàng cho các Đơn bán hàng (SO) hoặc Đơn mua hàng (PO) cụ thể, tránh tình trạng thiếu hụt hàng khi có nhiều đơn hàng cùng lúc.
*   **Truy xuất nguồn gốc Lô/Số Serial (Serial/Batch Traceability):** Nâng cấp khả năng theo dõi chi tiết vòng đời của Mặt hàng theo Lô hàng (Batch) và Số Serial.
*   **Gia công ngoài nhập kho (Inward Subcontracting):** Quy trình quản lý vật tư chuyển cho nhà thầu phụ và nhập lại thành phẩm hoàn thiện một cách chặt chẽ.
*   **Cải tiến Điểm bán hàng (POS Improvements):** Giao diện POS nhanh hơn, hỗ trợ tốt hơn cho các thiết bị di động và quản lý thanh toán linh hoạt.
*   **Nâng cấp quản trị nhân sự (HRMS Enhancements):** Bổ sung các module quản lý hiệu suất và quy trình tuyển dụng thông minh hơn.

---

## 2. Điều kiện tiên quyết

Để trải nghiệm tốt nhất các tính năng mới trong v16, bạn cần đảm bảo:
*   Hệ thống đã được nâng cấp lên phiên bản ERPNext v16.
*   Quyền truy cập (Role Permissions) đã được thiết lập cho các module mới (MRP, HRMS, v.v.).
*   Dữ liệu về Mặt hàng (Item), Kho (Warehouse) và Danh mục tài khoản đã được chuẩn hóa.

---

## 3. Hướng dẫn từng bước

Vì v16 là một bản cập nhật tổng thể, dưới đây là hướng dẫn cách tiếp cận các tính năng mới:

### 3.1. Làm quen với giao diện mới
1.  Đăng nhập vào hệ thống.
2.  Quan sát thanh điều hướng và Workspace mới đã được sắp xếp lại theo nhóm chức năng.
3.  Sử dụng thanh tìm kiếm thông minh để truy cập nhanh các tài liệu như: [Khách hàng](../customer.md), [Nhà cung cấp](../supplier.md), hoặc [Mặt hàng](../item.md).

### 3.2. Thiết lập Giữ chỗ tồn kho (Stock Reservation)
1.  Truy cập vào **Mặt hàng (Item)**.
2.  Tại mục **Kho (Stock)**, kích hoạt tùy chọn "Allow Stock Reservation".
3.  Khi tạo **Đơn bán hàng (SO)**, chọn mục "Reserve Stock" để hệ thống tự động giữ hàng trong **Kho (Warehouse)**.

### 3.3. Sử dụng Mẫu báo cáo tài chính mới
1.  Truy cập module **Kế toán (Accounting)**.
2.  Chọn **Báo cáo tài chính (Financial Report)**.
3.  Sử dụng trình kéo thả để tùy chỉnh các dòng/cột dựa trên **Mẫu báo cáo (Report Template)** có sẵn.
4.  Nhấn **Lưu (Save)** để áp dụng mẫu.

### 3.4. Quy trình Gia công ngoài (Inward Subcontracting)
1.  Tạo **Đơn mua hàng (PO)** cho dịch vụ gia công.
2.  Tạo **Phiếu xuất kho (SE)** để chuyển nguyên vật liệu cho Nhà cung cấp.
3.  Khi nhận hàng, tạo **Phiếu nhập hàng (PR)** hoặc **Phiếu giao hàng (DN)** để ghi nhận thành phẩm đã hoàn thiện.

---

## 4. Ảnh minh họa

*(Vui lòng xem ảnh chụp màn hình giao diện Workspace mới tại đây)*
![Giao diện ERPNext v16](../screenshots/workspace-home.png)

---

## 5. Các tùy chọn/cài đặt liên quan

*   **Cài đặt Kho (Stock Settings):** Để cấu hình tự động kiểm tra số lượng khi có yêu cầu giữ chỗ.
*   **Cài đặt Sản xuất (Manufacturing Settings):** Để kích hoạt các tính năng MRP nâng cao.
*   **Cài đặt Nhân sự (HR Settings):** Để tùy chỉnh các quy trình phê duyệt mới.

---

## 6. Lưu ý quan trọng

*   **Sao lưu dữ liệu:** Luôn thực hiện sao lưu (Backup) toàn bộ cơ sở dữ liệu trước khi tiến hành nâng cấp lên v16.
*   **Kiểm tra hiệu năng:** Do tốc độ xử lý tăng 2x, hãy kiểm tra lại các tùy chỉnh báo cáo cũ để đảm bảo tính tương thích.
*   **Đồng bộ dữ liệu:** Khi sử dụng tính năng **Truy xuất nguồn gốc (Traceability)**, đảm bảo mọi giao dịch nhập/xuất đều phải được **Xác nhận (Submit)** để dữ liệu lô hàng được chính xác.

---

## 7. Liên kết đến trang liên quan

*   [Hướng dẫn quản lý Kho (Stock)](../stock.md)
*   [Hướng dẫn quản lý Sản xuất (Manufacturing/MRP)](../manufacturing.md)
*   [Hướng dẫn quản lý Bán hàng (Sales/SO)](../sales.md)
*   [Hướng dẫn quản lý Mua hàng (Buying/PO)](../buying.md)
*   [Hướng dẫn Kế toán & Báo cáo tài chính](../accounting.md)