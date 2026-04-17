# Công cụ Tạo Báo cáo Học sinh

Tài liệu này hướng dẫn cách sử dụng công cụ tạo báo cáo học sinh trong hệ thống ERPNext v16. Công cụ này cho phép trích xuất dữ liệu học sinh, điểm số và tình trạng học tập để tạo ra các báo cáo chuyên nghiệp.

## Tổng quan

Công cụ tạo báo cáo giúp quản trị viên và giáo viên nhanh chóng tổng hợp dữ liệu từ các module liên quan mà không cần thao tác thủ công trên từng bản ghi.

## Các bước thực hiện

### 1. Thiết lập điều kiện báo cáo
Trước khi tạo báo cáo, bạn cần xác định các tiêu chí lọc dữ liệu:
* **Khối lớp/Lớp học:** Chọn lớp cụ thể để lấy danh sách học sinh.
* **Học kỳ/Năm học:** Xác định khoảng thời gian cần báo cáo.
* **Trạng thái:** Lọc theo học sinh đang theo học hoặc đã thôi học.

### 2. Quy trình tạo báo cáo

1. Truy cập vào module **Học sinh (Student)**.
2. Tìm đến mục **Báo cáo học sinh (Student Report)**.
3. Nhấn **Lưu (Save)** các thiết lập bộ lọc của bạn.
4. Nhấn **Xác nhận (Submit)** để hệ thống bắt đầu truy vấn dữ liệu từ cơ sở dữ liệu.

### 3. Kiểm tra và Xuất dữ liệu

* **Kiểm tra chất lượng (QI):** Sau khi báo cáo được tạo, hãy kiểm tra tính chính xác của điểm số và thông tin cá nhân so với hồ sơ gốc.
* **Xuất báo cáo:** Bạn có thể xuất báo cáo dưới dạng PDF hoặc Excel để lưu trữ hoặc gửi cho phụ huynh.
* **Hủy (Cancel):** Nếu thông tin bộ lọc bị sai, hãy nhấn **Hủy (Cancel)** để xóa bản ghi báo cáo tạm thời và thực hiện lại từ đầu.

## Lưu ý quan trọng

* **Dữ liệu Tồn kho (Stock) & Vật tư (MR):** Đối với các trường học có quản lý bán trú, báo cáo học sinh có thể liên kết với dữ liệu **Yêu cầu vật tư (MR)** để thống kê định mức ăn uống của học sinh.
* **Thanh toán (Payment):** Đảm bảo các khoản **Hóa đơn (Invoice)** học phí đã được **Xác nhận (Submit)** để báo cáo tình trạng nợ học phí được chính xác.
* **Phân quyền:** Chỉ những người dùng có quyền quản trị mới có thể **Xác nhận (Submit)** các báo cáo tổng hợp cuối kỳ.

---
**Xem thêm:**
* [Hướng dẫn Quản lý Khách hàng (Phụ huynh).md](./customer_management.md)
* [Quy trình Quản lý Hóa đơn học phí.md](./invoice_management.md)
* [Quản lý Kho vật tư học đường.md](./stock_management.md)