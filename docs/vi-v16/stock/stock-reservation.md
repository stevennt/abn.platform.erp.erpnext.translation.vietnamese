# Giữ tồn kho (Stock Reservation)

**Mới trong v16**

Tính năng **Giữ tồn kho (Stock Reservation)** trong ERPNext v16 cho phép bạn dành riêng một lượng **Mặt hàng** nhất định trong **Kho** cho các tài liệu cụ thể (như **Đơn bán hàng** hoặc **Lệnh sản xuất**). Điều này giúp ngăn chặn việc phân bổ sai hàng hóa cho các đơn hàng khác, đảm bảo tính sẵn sàng của hàng hóa cho các cam kết đã ký kết với **Khách hàng**.

## 1. Giới thiệu tính năng
Trong các phiên bản trước, việc quản lý tồn kho dựa trên số lượng thực tế có thể dẫn đến tình trạng hàng hóa bị "hụt" khi chuẩn bị xuất kho nếu có nhiều đơn hàng cùng lúc. Với tính năng Giữ tồn kho, hệ thống sẽ tạo một trạng thái "Đã giữ" (Reserved), giúp bộ phận kho biết chính xác lượng hàng nào đã được dành riêng cho các đơn hàng cụ thể, ngay cả khi chưa lập **Phiếu giao hàng (DN)**.

## 2. Điều kiện tiên quyết
Để sử dụng tính năng này, bạn cần đảm bảo các thiết lập sau:
* Đã kích hoạt tính năng Quản lý kho trong module **Tồn kho**.
* Đã thiết lập **Mặt hàng** và **Kho** đầy đủ.
* (Tùy chọn) Đã bật tính năng *Allow Stock Reservation* trong *Stock Settings*.

## 3. Hướng dẫn từng bước

### 3.1. Cách bật tính năng Giữ tồn kho cho Mặt hàng
Trước tiên, bạn cần cho phép một **Mặt hàng** cụ thể có thể được giữ hàng.

1. Truy cập vào danh sách **Mặt hàng**.
2. Chọn **Mặt hàng** bạn muốn thiết lập.
3. Cuộn xuống phần **Kho (Stock)**.
4. Tích chọn vào ô **Allow Stock Reservation** (Cho phép giữ tồn kho).
5. Nhấn **Lưu**.

![Minh họa thiết lập mặt hàng](../../screenshots/stock/item-list.png)

### 3.2. Giữ hàng từ Đơn bán hàng (SO)
Khi bạn xác nhận một **Đơn bán hàng**, bạn có thể yêu cầu hệ thống giữ hàng ngay lập tức.

1. Tạo mới hoặc mở một **Đơn bán hàng (SO)** đã được **Xác nhận (Submit)**.
2. Tại bảng **Mặt hàng** trong đơn hàng, kiểm tra cột **Reserved Qty** (Số lượng giữ).
3. Khi bạn **Xác nhận (Submit)** đơn hàng, nếu Mặt hàng đã được bật tính năng giữ hàng, hệ thống sẽ tự động tính toán số lượng cần giữ dựa trên số lượng đặt hàng.
4. Số lượng này sẽ được trừ vào "Tồn kho khả dụng" nhưng vẫn nằm trong "Tồn kho thực tế".

### 3.3. Giữ hàng cho Lệnh sản xuất (Work Order)
Để đảm bảo nguyên vật liệu luôn sẵn sàng cho sản xuất:

1. Mở **Lệnh sản xuất (Work Order)** tương ứng.
2. Kiểm tra danh sách **Yêu cầu vật tư (MR)** được tạo ra từ lệnh sản xuất.
3. Khi **Lệnh sản xuất** được xác nhận, hệ thống sẽ thực hiện giữ các **Mặt hàng** nguyên vật liệu cần thiết trong **Kho** để tránh việc các bộ phận khác lấy mất.

### 3.4. Giải phóng hàng (Release Reservation)
Nếu đơn hàng bị **Hủy (Cancel)** hoặc khách hàng thay đổi ý định, số lượng hàng giữ sẽ được giải phóng.

1. **Trường hợp tự động:** Khi bạn **Hủy (Cancel)** **Đơn bán hàng (SO)** hoặc **Lệnh sản xuất**, hệ thống sẽ tự động giải phóng số lượng hàng đã giữ về trạng thái sẵn sàng bán.
2. **Trường hợp thủ công:** Bạn có thể điều chỉnh số lượng trên tài liệu gốc trước khi **Xác nhận (Submit)** để thay đổi mức độ giữ hàng.

## 4. Các tùy chọn và cài đặt liên quan
* **Stock Settings:** Kiểm tra cấu hình chung về cách hệ thống tính toán tồn kho khả dụng.
* **Bin (Thùng hàng):** Kiểm tra số lượng *Reserved Qty* trong bảng Bin để biết lượng hàng đang bị giữ cho các đơn hàng khác.

## 5. Lưu ý quan trọng
* **Tồn kho khả dụng (Available Qty) vs Tồn kho thực tế (Actual Qty):** Sau khi giữ hàng, *Tồn kho thực tế* không đổi, nhưng *Tồn kho khả dụng* sẽ giảm xuống.
* **Ưu tiên hàng hóa:** Tính năng này giúp tránh xung đột giữa bộ phận Kinh doanh (muốn giữ hàng cho khách) và bộ phận Sản xuất (muốn giữ hàng cho lệnh sản xuất).
* **Kiểm tra chất lượng (QI):** Nếu hàng hóa đang trong trạng thái chờ **Kiểm tra chất lượng (QI)**, bạn nên lưu ý trước khi thực hiện giữ hàng để tránh thiếu hụt hàng đạt chuẩn.

## 6. Liên kết đến trang liên quan
* [Quản lý Mặt hàng](../stock/item-list.md)
* [Quy trình Đơn bán hàng](../sales/sales_order.md)
* [Quản lý Kho và Lô hàng](../stock/warehouse_batch.md)
* [Sản xuất và Lệnh sản xuất](../manufacturing/work_order.md)