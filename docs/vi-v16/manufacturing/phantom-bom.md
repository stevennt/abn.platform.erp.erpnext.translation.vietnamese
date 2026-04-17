# Định mức NVL ảo (Phantom BOM)

![Giao diện ERPNext v16](../workspace-home.png)

## 1. Giới thiệu tính năng
> **✨ Mới trong v16**

Trong ERPNext v16, tính năng **Định mức NVL ảo (Phantom BOM)** được tối ưu hóa để hỗ trợ quy trình sản xuất đa cấp phức tạp. Tính năng này cho phép bạn định nghĩa các cụm lắp ráp phụ (sub-assembly) trong cấu trúc BOM mà không cần phải tạo Lệnh sản xuất (Work Order) riêng biệt cho từng cấp trung gian.

Khi bạn tạo một Lệnh sản xuất cho thành phẩm cuối cùng, hệ thống sẽ tự động **mở rộng (expand)** các thành phần của Phantom BOM, đưa trực tiếp các nguyên vật liệu của cấp phụ vào danh sách vật tư của lệnh sản xuất chính. Điều này giúp đơn giản hóa việc quản lý kho và giảm bớt các bước thao tác thừa trên hệ thống.

## 2. Điều kiện tiên quyết
Để sử dụng tính năng Phantom BOM, bạn cần đảm bảo các điều kiện sau:
* Đã thiết lập danh mục **Mặt hàng (Item)** cho cả thành phẩm và bán thành phẩm.
* Đã thiết lập **Định mức nguyên vật liệu (BOM)** cho tất cả các cấp trong cấu trúc sản phẩm.
* Tài khoản người dùng có quyền truy cập vào module Sản xuất và Kho.

## 3. Hướng dẫn từng bước

### Bước 1: Thiết lập BOM cho bán thành phẩm (Sub-assembly)
1. Truy cập vào danh mục **Mặt hàng (Item)** và chọn mặt hàng đóng vai trò là cụm lắp ráp phụ.
2. Mở bảng **Định mức nguyên vật liệu (BOM)** của mặt hàng đó.
3. Thêm các nguyên vật liệu thành phần cần thiết.
4. **Quan trọng:** Đảm bảo BOM này được lưu và sẵn sàng để sử dụng.

### Bước 2: Thiết lập Phantom BOM cho thành phẩm chính
1. Truy cập vào **Định mức nguyên vật liệu (BOM)** của thành phẩm cuối cùng.
2. Trong bảng **Thành phần (Items)**, thêm mặt hàng bán thành phẩm (đã tạo ở Bước 1) vào danh sách.
3. Tìm cột **Is Phantom** (Là ảo) và tích chọn vào ô này.
4. Nhấn **Lưu (Save)** để hoàn tất.

### Bước 3: Kiểm tra việc tự động mở rộng khi tạo Lệnh sản xuất
1. Tạo một **Lệnh sản xuất (Work Order)** mới cho thành phẩm chính.
2. Chọn BOM đã thiết lập có chứa Phantom BOM.
3. Nhấn **Lưu (Save)** hoặc **Xác nhận (Submit)**.
4. Kiểm tra bảng **Danh sách vật tư (Material List)**: Bạn sẽ thấy các nguyên vật liệu của bán thành phẩm phụ đã tự động xuất hiện trực tiếp trong danh sách vật tư của Lệnh sản xuất chính mà không cần thông qua một Lệnh sản xuất trung gian nào.

## 4. Ảnh minh họa
*(Hình ảnh minh họa cấu trúc Phantom BOM và quá trình tự động mở rộng vật tư)*
![Giao diện ERPNext v16](../workspace-home.png)

## 5. Các tùy chọn/cài đặt liên quan
* **Is Phantom (Là ảo):** Tùy chọn quyết định xem một dòng trong BOM có được coi là một thực thể tồn kho độc lập hay chỉ là một tập hợp các linh kiện để lắp ráp nhanh.
* **BOM Explosion (Bùng nổ BOM):** Cơ chế hệ thống tự động tính toán các cấp nguyên vật liệu khi có sự xuất hiện của Phantom Item.

## 6. Lưu ý quan trọng
* **Quản lý Tồn kho:** Vì là "Ảo", hệ thống sẽ không tạo ra các phiếu nhập kho hay phiếu xuất kho riêng cho bán thành phẩm này. Tồn kho sẽ được ghi nhận trực tiếp cho các nguyên vật liệu thành phần và thành phẩm cuối cùng.
* **Chi phí:** Chi phí của Phantom BOM được tính toán bằng tổng chi phí của các thành phần bên trong nó và được cộng dồn vào giá thành của thành phẩm chính.
* **Không dùng cho sản xuất độc lập:** Nếu bạn có kế hoạch sản xuất bán thành phẩm đó để lưu kho riêng biệt, **KHÔNG** được tích chọn "Is Phantom".

## 7. Liên kết đến trang liên quan
* [Quản lý Định mức nguyên vật liệu (BOM)](bom.md)
* [Quy trình Lệnh sản xuất (Work Order)](work_order.md)
* [Quản lý Kho và Tồn kho (Stock)](stock.md)
* [Danh mục Mặt hàng (Item)](item.md)