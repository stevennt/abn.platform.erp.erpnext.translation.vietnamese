# Gia công nhận hàng (Inward Subcontracting)

![Giao diện ERPNext v16](../workspace-home.png)

## 1. Giới thiệu tính năng
**[Mới trong v16]** 

**Gia công nhận hàng (Inward Subcontracting)** là quy trình quản lý khi doanh nghiệp của bạn đóng vai trò là đơn vị gia công. Trong kịch bản này, **Khách hàng** sẽ gửi nguyên vật liệu (NVL) đến kho của bạn. Bạn sử dụng các NVL đó để sản xuất thành phẩm theo yêu cầu, sau đó giao thành phẩm lại cho khách hàng.

Quy trình này ngược lại với *Gia công thuê ngoài (Outward Subcontracting)*. Tính năng này giúp theo dõi chính xác lượng tồn kho của khách hàng đang nằm tại kho của bạn, đảm bảo tính minh bạch trong việc quản lý vật tư và kiểm soát chi phí gia công.

## 2. Điều kiện tiên quyết
Để thực hiện quy trình này, hệ thống cần được thiết lập sẵn các điều kiện sau:
* **Mặt hàng (Item):** Đã khai báo đầy đủ cho cả Nguyên vật liệu và Thành phẩm.
* **BOM (Định mức nguyên vật liệu):** Thành phẩm phải có BOM để hệ thống tự động tính toán lượng NVL cần thiết.
* **Kho (Warehouse):** Đã thiết lập các Kho chứa NVL khách hàng gửi và Kho chứa thành phẩm.
* **Đơn bán hàng (SO):** Đã có Đơn bán hàng cho thành phẩm cần gia công.

## 3. Hướng dẫn từng bước

### Bước 1: Tạo Đơn bán hàng (Sales Order)
Tạo một **Đơn bán hàng (SO)** cho khách hàng. Trong dòng sản phẩm, hãy đảm bảo bạn đã chọn đúng mặt hàng thành phẩm mà khách hàng yêu cầu gia công.

### Bước 2: Tạo Đơn gia công nhận hàng (Subcontracting Inward Order)
Từ **Đơn bán hàng (SO)**, bạn tạo một bản ghi **Đơn gia công nhận hàng**. Tài liệu này sẽ liên kết trực tiếp với SO để xác định số lượng thành phẩm cần sản xuất.

### Bước 3: Nhận Nguyên vật liệu từ Khách hàng
Khi khách hàng gửi NVL đến kho của bạn:
1. Truy cập vào **Đơn gia công nhận hàng** đã tạo.
2. Tạo **Phiếu nhập hàng (PR)** hoặc **Phiếu kho (SE)** để ghi nhận việc nhập NVL từ khách hàng vào kho của bạn.
3. **Lưu** và **Xác nhận (Submit)** phiếu để tăng tồn kho NVL (dưới dạng hàng ký gửi/hàng của khách).

### Bước 4: Sản xuất và Hoàn tất
Sau khi quá trình sản xuất hoàn tất:
1. Thực hiện lệnh sản xuất (Work Order) dựa trên BOM.
2. Khi hoàn thành, hệ thống sẽ trừ lượng NVL đã nhận và tăng lượng Thành phẩm trong kho.
3. Tạo **Phiếu giao hàng (DN)** để xuất thành phẩm cho khách hàng.

### Bước 5: Xuất Hóa đơn (Invoice)
Tạo **Hóa đơn (Invoice)** cho khách hàng dựa trên số lượng thành phẩm thực tế đã giao và phí gia công đã thỏa thuận.

## 4. Ảnh minh họa
*(Vui lòng xem sơ đồ quy trình tại: ../../screenshots/workspace-home.png)*

## 5. Các tùy chọn/cài đặt liên quan
* **Quản lý theo Lô hàng (Batch):** Nếu NVL hoặc thành phẩm yêu cầu truy xuất nguồn gốc, hãy kích hoạt tính năng **Lô hàng (Batch)** trong danh mục **Mặt hàng (Item)**.
* **Kiểm tra chất lượng (QI):** Có thể thiết lập quy trình **Kiểm tra chất lượng (QI)** ngay khi nhận NVL từ khách hàng hoặc khi hoàn tất thành phẩm để đảm bảo tiêu chuẩn.
* **Định mức vật tư (BOM):** Kiểm soát chặt chẽ tỷ lệ hao hụt vật tư trong quá trình gia công.

## 6. Lưu ý quan trọng
* **Quản lý tồn kho:** Cần phân biệt rõ giữa tồn kho sở hữu của doanh nghiệp và tồn kho của khách hàng đang nằm tại kho của mình để tránh sai lệch khi kiểm kê.
* **Xác nhận (Submit):** Mọi giao dịch nhập/xuất vật tư phải được **Xác nhận (Submit)** để đảm bảo các bút toán kho và kế toán được ghi nhận chính xác.
* **Hao hụt:** Nếu quá trình gia công có tỷ lệ hao hụt cao, cần điều chỉnh định mức trong BOM để phản ánh đúng thực tế tiêu hao.

## 7. Liên kết đến trang liên quan
* [Quản lý Đơn bán hàng (SO)](sales_order.md)
* [Quản lý Kho và Phiếu kho (SE)](stock_management.md)
* [Quy trình Gia công thuê ngoài (Outward Subcontracting)](outward_subcontracting.md)
* [Quản lý Mặt hàng (Item)](item_management.md)