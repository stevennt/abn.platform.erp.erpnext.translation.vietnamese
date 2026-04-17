# Hoạch định nhu cầu vật tư (MRP)

![Giao diện làm việc](../screenshots/workspace-home.png)

## 1. Giới thiệu tính năng
**[Mới trong v16]** Hoạch định nhu cầu vật tư (Material Requirements Planning - MRP) là công cụ quản trị thông minh giúp doanh nghiệp tự động hóa việc tính toán nhu cầu vật tư dựa trên các dữ liệu thực tế và dự báo. 

Thay vì tính toán thủ công, MRP trong v16 sẽ kết hợp giữa **Dự báo bán hàng**, **Lịch giao hàng** từ các Đơn bán hàng (SO) và **Thời gian chờ (Lead time)** của nhà cung cấp để đề xuất các lệnh mua hàng hoặc lệnh sản xuất phù hợp. Điều này giúp tối ưu hóa mức tồn kho, tránh tình trạng thiếu hụt vật tư gây gián đoạn sản xuất hoặc tồn kho quá mức gây lãng phí vốn.

## 2. Điều kiện tiên quyết
Để tính năng MRP hoạt động chính xác, hệ thống cần được thiết lập sẵn các dữ liệu sau:
* **Mặt hàng (Item):** Phải có thiết lập định mức nguyên vật liệu (BOM) nếu là sản xuất, và thiết lập đơn vị tính.
* **Tồn kho (Stock):** Dữ liệu tồn kho tại các **Kho (Warehouse)** phải được cập nhật chính xác.
* **Thời gian chờ (Lead Time):** Thiết lập thời gian từ lúc đặt hàng đến khi nhận hàng trong hồ sơ **Nhà cung cấp (Supplier)** hoặc **Mặt hàng (Item)**.
* **Dự báo (Forecast):** Các bản ghi dự báo nhu cầu đã được tạo.
* **Đơn hàng:** Các **Đơn bán hàng (SO)** đã được xác nhận và các **Đơn mua hàng (PO)** đang chờ giao.

## 3. Hướng dẫn từng bước

### Bước 1: Thiết lập thông số MRP
1. Truy cập vào module **Sản xuất** hoặc **Kho**.
2. Tìm kiếm và chọn công cụ **MRP Settings**.
3. Thiết lập các tham số như: *Mức tồn kho an toàn (Safety Stock)*, *Thời gian chờ dự phòng*, và *Ngày chạy MRP định kỳ*.

### Bước 2: Chạy kế hoạch MRP
1. Mở công cụ **Material Requirements Planning**.
2. Chọn **Kho (Warehouse)** hoặc **Nhóm mặt hàng (Item Group)** mà bạn muốn lập kế hoạch.
3. Chọn phạm vi thời gian cần hoạch định.
4. Nhấn nút **Run MRP** (Chạy MRP). Hệ thống sẽ quét toàn bộ dữ liệu từ Đơn bán hàng, Lịch giao hàng và Tồn kho hiện tại.

### Bước 3: Xem xét kết quả và đề xuất
Sau khi chạy xong, hệ thống sẽ hiển thị danh sách các nhu cầu vật tư:
1. **Xem danh sách đề xuất:** Hệ thống sẽ liệt kê các **Đơn mua hàng (PO)** cần tạo hoặc các **Lệnh sản xuất** cần lập.
2. **Kiểm tra Master Production Schedule (MPS):** Xem lịch trình sản xuất tổng thể để đảm bảo năng lực sản xuất đáp ứng được nhu cầu.
3. **Kiểm tra MRP Views:** Sử dụng các bảng xem trực quan để biết mặt hàng nào đang thiếu, mặt hàng nào sắp hết dựa trên ngày dự kiến giao hàng.

### Bước 4: Thực thi kế hoạch
1. Từ danh sách đề xuất, chọn các dòng cần thực hiện.
2. Nhấn **Create Purchase Request (PR)** để tạo Phiếu yêu cầu mua hàng hoặc **Create Manufacturing Order** để tạo Lệnh sản xuất.
3. Sau khi được phê duyệt, tiến hành **Xác nhận (Submit)** các chứng từ này để chuyển sang bước đặt hàng hoặc sản xuất.

## 4. Các tùy chọn và cài đặt liên quan
* **Master Production Schedule (MPS):** Lập kế hoạch sản xuất tổng thể dựa trên dự báo nhu cầu dài hạn.
* **Reorder Level:** Thiết lập điểm đặt hàng lại tự động cho từng mặt hàng.
* **Lead Time Calculation:** Tự động tính toán ngày cần đặt hàng dựa trên thời gian vận chuyển của Nhà cung cấp.

## 5. Lưu ý quan trọng
* **Dữ liệu đầu vào:** Nếu dữ liệu **Tồn kho (Stock)** hoặc **Lô hàng (Batch)** không chính xác, kết quả MRP sẽ bị sai lệch hoàn toàn.
* **Lead Time:** Luôn cập nhật thời gian chờ của Nhà cung cấp để tránh việc hàng về chậm hơn so với kế hoạch sản xuất.
* **Xác nhận chứng từ:** Chỉ những chứng từ đã được **Xác nhận (Submit)** mới được MRP tính toán vào kế hoạch. Các chứng từ đã **Hủy (Cancel)** sẽ bị loại bỏ khỏi tính toán.

## 6. Liên kết đến trang liên quan
* [Quản lý Kho và Tồn kho](../stock/overview.md)
* [Quản lý Mua hàng (PO/PR)](../buying/overview.md)
* [Quản lý Sản xuất (BOM/MPS)](../manufacturing/overview.md)
* [Quản lý Bán hàng (SO/Invoice)](../selling/overview.md)