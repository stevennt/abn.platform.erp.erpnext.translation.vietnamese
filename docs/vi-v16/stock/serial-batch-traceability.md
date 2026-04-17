# Truy xuất nguồn gốc lô hàng (Serial & Batch Traceability)

## 1. Giới thiệu tính năng <span style="color: #2ecc71;">(Mới trong v16)</span>

Trong phiên bản ERPNext v16, tính năng **Truy xuất nguồn gốc (Traceability)** được nâng cấp mạnh mẽ để đáp ứng các tiêu chuẩn khắt khe về an toàn thực phẩm và quản lý chuỗi cung ứng lạnh (cold-chain). Tính năng này cho phép doanh nghiệp theo dõi toàn bộ vòng đời của một sản phẩm thông qua số Lô hàng (Batch) hoặc Số Serial.

Khả năng truy xuất bao gồm hai chiều:
* **Truy xuất xuôi (Forward Tracing):** Theo dõi từ Nguyên vật liệu (NVL) $\rightarrow$ Quá trình sản xuất $\rightarrow$ Thành phẩm $\rightarrow$ Khách hàng. Giúp khoanh vùng các lô hàng lỗi cần thu hồi ngay lập tức.
* **Truy xuất ngược (Backward Tracing):** Theo dõi từ Thành phẩm $\rightarrow$ Các lô NVL đầu vào đã sử dụng. Giúp xác định nguyên nhân gốc rễ khi có sự cố chất lượng từ nhà cung cấp.

## 2. Điều kiện tiên quyết

Để sử dụng tính năng này, hệ thống cần được thiết lập các điều kiện sau:
* **Bật quản lý Lô hàng/Số Serial:** Trong danh mục **Mặt hàng (Item)**, mục *Inventory*, phải tích chọn "Has Batch No" hoặc "Has Serial No".
* **Quản lý Kho:** Các giao dịch **Phiếu nhập hàng (PR)**, **Phiếu kho (SE)**, và **Phiếu giao hàng (DN)** phải được thực hiện gắn kèm số Lô hoặc Số Serial.
* **Quy trình sản xuất:** Các lệnh sản xuất phải ghi nhận việc tiêu hao nguyên vật liệu theo từng Lô cụ thể.

## 3. Hướng dẫn từng bước

### Cách 1: Truy xuất từ danh sách Lô hàng (Batch)
Đây là cách nhanh nhất để xem một lô nguyên liệu đã đi đâu hoặc một lô thành phẩm được làm từ đâu.

1. Truy cập vào module **Tồn kho (Stock)**.
2. Chọn danh mục **Lô hàng (Batch)**.
3. Tìm kiếm và chọn số Lô hàng cần kiểm tra.
4. Tại giao diện chi tiết, nhấn vào nút **Traceability** (Truy xuất nguồn gốc) trên thanh công cụ.
5. Hệ thống sẽ hiển thị sơ đồ cây (Tree View) liên kết các chứng từ liên quan.

### Cách 2: Truy xuất từ một Đơn bán hàng (SO) hoặc Hóa đơn (Invoice)
Dùng khi khách hàng phản hồi về một sản phẩm cụ thể.

1. Mở **Hóa đơn (Invoice)** hoặc **Đơn bán hàng (SO)** chứa mặt hàng cần kiểm tra.
2. Nhấp vào mã **Số Serial** hoặc **Số Lô** trong bảng chi tiết mặt hàng.
3. Chọn **View Traceability**.
4. Hệ thống sẽ hiển thị dòng thời gian (Timeline) từ lúc nhập kho (PR) $\rightarrow$ Nhập kho thành phẩm $\rightarrow$ Xuất kho (DN).

## 4. Ảnh minh họa

![Danh sách lô hàng và quản lý Batch](../../screenshots/stock/batch-list.png)
*Hình 1: Giao diện quản lý Lô hàng (Batch) trong ERPNext v16.*

## 5. Các tùy chọn/cài đặt liên quan

* **Cài đặt Kiểm tra chất lượng (QI):** Có thể cấu hình để hệ thống tự động chặn không cho phép xuất kho (DN) nếu Lô hàng đó chưa hoàn thành bước **Kiểm tra chất lượng (QI)**.
* **Hạn sử dụng (Expiry Date):** Trong quản lý **Lô hàng (Batch)**, việc thiết lập ngày sản xuất và hạn sử dụng giúp hệ thống tự động cảnh báo các lô hàng sắp hết hạn trong chuỗi cold-chain.
* **Quản lý theo vị trí (Warehouse):** Theo dõi sự di chuyển của Lô hàng giữa các **Kho (Warehouse)** khác nhau.

## 6. Lưu ý quan trọng

* **Tính chính xác của dữ liệu:** Tính năng truy xuất chỉ có giá trị khi nhân viên kho nhập đúng số Lô/Serial vào các chứng từ **Phiếu nhập hàng (PR)**, **Phiếu kho (SE)** và **Phiếu giao hàng (DN)**. Nếu bỏ qua bước này, chuỗi truy xuất sẽ bị đứt gãy.
* **Ngành thực phẩm (Cold-chain):** Đối với hàng thực phẩm, cần đặc biệt lưu ý kết hợp truy xuất Lô hàng với lịch sử nhiệt độ (nếu có tích hợp cảm biến IoT) để đảm bảo chất lượng sản phẩm.
* **Xác nhận (Submit):** Chỉ những chứng từ đã được **Xác nhận (Submit)** mới được đưa vào sơ đồ truy xuất nguồn gốc.

## 7. Liên kết đến trang liên quan

* [Quản lý Tồn kho (Stock Management)](../stock/management.md)
* [Quản lý Lô hàng và Số Serial (Batch & Serial Management)](../stock/batch-serial.md)
* [Quy trình Kiểm tra chất lượng (Quality Inspection)](https://docs.erpnext.com/docs/v13/user/manual/en/quality/inspection)
* [Quản lý Kho (Warehouse Management)](../stock/warehouse.md)