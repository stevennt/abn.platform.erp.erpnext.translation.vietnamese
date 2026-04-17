# Hoạch định nhu cầu vật tư (MRP)

![Giao diện chính ERPNext](../screenshots/workspace-home.png)

## 1. Giới thiệu tính năng
**[Mới trong v16]** Hoạch định nhu cầu vật tư (Material Requirements Planning - MRP) là công cụ quản trị thông minh giúp doanh nghiệp tự động hóa việc tính toán nhu cầu nguyên vật liệu và thành phẩm. 

Thay vì tính toán thủ công, MRP trong v16 sẽ phân tích dữ liệu từ dự báo bán hàng, lịch giao hàng của Đơn bán hàng (SO), mức tồn kho hiện tại, và thời gian chờ (lead time) để đề xuất các lệnh mua hàng hoặc lệnh sản xuất phù hợp. Điều này giúp tối ưu hóa mức tồn kho, tránh tình trạng thiếu hụt vật tư gây gián đoạn sản xuất hoặc tồn kho quá mức gây lãng phí vốn.

## 2. Điều kiện tiên quyết
Để tính năng MRP hoạt động chính xác, hệ thống cần được thiết lập sẵn các dữ liệu sau:
* **Mặt hàng (Item):** Phải có thiết lập định mức nguyên vật liệu (BOM) cho sản phẩm và thiết lập đơn vị tính.
* **Tồn kho (Stock):** Dữ liệu tồn kho thực tế tại các Kho (Warehouse) phải được cập nhật chính xác.
* **Thời gian chờ (Lead Time):** Được thiết lập trong hồ sơ Mặt hàng hoặc Nhà cung cấp.
* **Dự báo (Forecast):** Các bản ghi dự báo nhu cầu bán hàng đã được tạo.
* **Đơn hàng:** Các Đơn bán hàng (SO) đã được Xác nhận (Submit).

## 3. Hướng dẫn từng bước

### Bước 1: Thiết lập dữ liệu đầu vào
Đảm bảo tất cả các **Mặt hàng** cần hoạch định đã có đầy đủ thông tin về BOM (nếu là sản xuất) và thời gian chờ nhập hàng từ **Nhà cung cấp**.

### Bước 2: Chạy quy trình MRP
1. Truy cập vào module **Sản xuất** hoặc **Kho**.
2. Tìm kiếm và chọn công cụ **Hoạch định nhu cầu vật tư (MRP)**.
3. Thiết lập các tham số bộ lọc:
    * **Ngày bắt đầu/kết thúc:** Khoảng thời gian cần lập kế hoạch.
    * **Kho (Warehouse):** Chọn kho cụ thể hoặc để trống để tính toán toàn bộ.
    * **Loại nhu cầu:** Chọn giữa "Mua hàng" (đối với nguyên vật liệu) hoặc "Sản xuất" (đối với thành phẩm).
4. Nhấn nút **Chạy MRP (Run MRP)**.

### Bước 3: Xem xét kết quả và đề xuất
Sau khi hệ thống xử lý, danh sách các đề xuất sẽ hiển thị:
* **Đề xuất mua hàng:** Hệ thống sẽ gợi ý tạo **Đơn mua hàng (PO)** cho các nguyên vật liệu thiếu hụt.
* **Đề xuất sản xuất:** Hệ thống sẽ gợi ý tạo Lệnh sản xuất dựa trên kế hoạch sản xuất tổng thể (Master Production Schedule).

### Bước 4: Thực thi kế hoạch
1. Kiểm tra các dòng đề xuất.
2. Chọn các dòng phù hợp và nhấn **Tạo Đơn mua hàng (Create PO)** hoặc **Tạo Lệnh sản xuất**.
3. Kiểm tra lại số lượng và ngày cần hàng trước khi nhấn **Xác nhận (Submit)**.

## 4. Các tùy chọn và cài đặt liên quan
* **Master Production Schedule (MPS):** Lập kế hoạch sản xuất tổng thể dựa trên dự báo dài hạn, giúp định hướng cho MRP.
* **Safety Stock (Tồn kho an toàn):** Thiết lập mức tồn kho tối thiểu cho mỗi Mặt hàng để MRP tự động đề xuất mua thêm khi chạm ngưỡng này.
* **Reorder Level (Ngưỡng đặt hàng lại):** Điểm kích hoạt tự động tạo yêu cầu mua hàng.

## 5. Lưu ý quan trọng
* **Độ chính xác của dữ liệu:** MRP chỉ hiệu quả khi dữ liệu **Tồn kho** và **Lịch giao hàng** được cập nhật thời gian thực. Nếu dữ liệu kho sai, kế hoạch MRP sẽ dẫn đến việc mua thừa hoặc thiếu hàng.
* **Lead Time:** Luôn cập nhật thời gian chờ của **Nhà cung cấp**. Nếu thời gian thực tế dài hơn trong hệ thống, bạn sẽ bị động trong việc cung ứng.
* **Kiểm tra lại trước khi Xác nhận:** Luôn rà soát lại các đề xuất của MRP để đảm bảo phù hợp với tình hình tài chính và năng lực kho bãi thực tế của doanh nghiệp trước khi **Xác nhận (Submit)** các đơn hàng.

## 6. Liên kết đến trang liên quan
* [Quản lý Mặt hàng (Item)](item_management.md)
* [Quản lý Kho và Tồn kho (Stock)](stock_management.md)
* [Quy trình Mua hàng (Purchase)](purchase_workflow.md)
* [Quy trình Sản xuất (Manufacturing)](manufacturing_workflow.md)