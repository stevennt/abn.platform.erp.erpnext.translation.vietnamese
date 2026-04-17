# Gia công nhận hàng (Inward Subcontracting)

![Giao diện ERPNext v16](../workspace-home.png)

## 1. Giới thiệu tính năng
**[Mới trong v16]**

**Gia công nhận hàng (Inward Subcontracting)** là quy trình quản lý việc nhận nguyên vật liệu (NVL) từ Khách hàng để thực hiện gia công thành thành phẩm, sau đó giao trả lại thành phẩm cho họ. 

Khác với *Gia công thuê ngoài (Outward Subcontracting)* — nơi bạn gửi nguyên liệu đi, quy trình này tập trung vào việc quản lý lượng tồn kho của khách hàng đang nằm tại kho của bạn. Quy trình này giúp kiểm soát chính xác lượng NVL đầu vào, định mức tiêu hao và số lượng thành phẩm hoàn thiện dựa trên Đơn bán hàng (SO) của khách hàng.

## 2. Điều kiện tiên quyết
Để thực hiện quy trình này, hệ thống cần được thiết lập sẵn các điều kiện sau:
* **Mặt hàng (Item):** Đã khai báo đầy đủ cho cả Nguyên vật liệu và Thành phẩm.
* **BOM (Định mức nguyên vật liệu):** Thành phẩm phải có BOM được thiết lập để hệ thống tự động tính toán lượng NVL cần thiết.
* **Kho (Warehouse):** Đã thiết lập các Kho chứa nguyên vật liệu và Kho chứa thành phẩm.
* **Đơn bán hàng (SO):** Đã có Đơn bán hàng được **Xác nhận (Submit)** cho dịch vụ gia công hoặc thành phẩm.

## 3. Hướng dẫn từng bước

### Bước 1: Tạo Đơn bán hàng (SO)
Tạo một **Đơn bán hàng (SO)** cho khách hàng. Tại dòng sản phẩm, hãy chọn dịch vụ gia công hoặc thành phẩm mà khách hàng yêu cầu.

### Bước 2: Tạo Lệnh gia công nhận hàng (Inward Subcontracting Order)
Từ Đơn bán hàng, tạo một bản ghi **Inward Subcontracting Order**. 
* Hệ thống sẽ tự động lấy thông tin từ SO.
* Kiểm tra danh sách các nguyên vật liệu cần thiết dựa trên BOM.

### Bước 3: Nhận nguyên vật liệu từ khách hàng (Stock Entry - Material In)
Khi khách hàng gửi nguyên vật liệu đến kho của bạn:
1. Tạo một **Phiếu kho (SE)** loại *Material In* hoặc sử dụng tính năng nhận hàng trực tiếp từ lệnh gia công.
2. **Lưu (Save)** và **Xác nhận (Submit)** để tăng tồn kho nguyên vật liệu (dưới dạng hàng ký gửi/hàng của khách).

### Bước 4: Sản xuất và Xuất thành phẩm (Stock Entry - Manufacture)
Sau khi hoàn tất quá trình gia công:
1. Tạo **Phiếu kho (SE)** loại *Manufacture*.
2. Hệ thống sẽ tự động trừ lượng nguyên vật liệu đã tiêu hao dựa trên BOM và tăng lượng thành phẩm trong kho.
3. **Lưu (Save)** và **Xác nhận (Submit)**.

### Bước 5: Giao hàng cho khách (Delivery Note)
Tạo **Phiếu giao hàng (DN)** để xuất thành phẩm đã gia công xong cho khách hàng.

### Bước 6: Xuất hóa đơn (Sales Invoice)
Tạo **Hóa đơn (Invoice)** để thu tiền phí gia công dựa trên số lượng thành phẩm đã giao.

## 4. Ảnh minh họa
*(Vui lòng xem sơ đồ quy trình tại: ../../screenshots/workspace-home.png)*

## 5. Các tùy chọn/cài đặt liên quan
* **Quản lý theo Lô hàng (Batch):** Nếu nguyên vật liệu hoặc thành phẩm yêu cầu quản lý theo số lô, hãy đảm bảo đã bật tính năng *Has Batch No* trong danh mục **Mặt hàng (Item)**.
* **Kiểm tra chất lượng (QI):** Có thể thiết lập quy trình **Kiểm tra chất lượng (QI)** ngay khi nhận nguyên vật liệu từ khách hàng để đảm bảo NVL đầu vào đạt chuẩn trước khi đưa vào sản xuất.
* **Định mức tiêu hao (Wastage):** Thiết lập tỷ lệ hao hụt cho phép trong BOM để hệ thống tính toán chính xác lượng tồn kho thực tế.

## 6. Lưu ý quan trọng
* **Quản lý tồn kho:** Nguyên vật liệu nhận từ khách hàng cần được theo dõi riêng biệt (có thể dùng Warehouse riêng hoặc đánh dấu để tránh nhầm lẫn với hàng tồn kho mua đứt của công ty).
* **Tính chính xác của BOM:** Nếu BOM không chính xác, việc **Xác nhận (Submit)** Phiếu kho sản xuất sẽ làm sai lệch hoàn toàn lượng tồn kho nguyên vật liệu của khách hàng.
* **Trạng thái đơn hàng:** Chỉ những Đơn bán hàng đã được **Xác nhận (Submit)** mới có thể tạo lệnh gia công nhận hàng.

## 7. Liên kết đến trang liên quan
* [Quản lý Đơn bán hàng (SO)](sales_order.md)
* [Quản lý Kho và Phiếu kho (SE)](stock_entry.md)
* [Quản lý Định mức nguyên vật liệu (BOM)](bom.md)
* [Quản lý Phiếu giao hàng (DN)](delivery_note.md)