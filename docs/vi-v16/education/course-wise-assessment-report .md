Vì bạn không cung cấp nội dung chi tiết của trang "Báo cáo Đánh giá theo Khóa học" từ phiên bản v13, tôi sẽ tạo cấu trúc chuẩn cho tài liệu ERPNext v16 dựa trên yêu cầu về thuật ngữ và định dạng Markdown của bạn.

Dưới đây là bản mẫu được viết lại theo phong cách tài liệu kỹ thuật ERPNext v16:

```markdown
<!-- add-breadcrumbs -->
# Báo cáo Đánh giá theo Khóa học

Tài liệu này hướng dẫn cách sử dụng và phân tích **Báo cáo Đánh giá theo Khóa học** trong ERPNext v16. Báo cáo này giúp quản trị viên theo dõi hiệu quả đào tạo, tiến độ hoàn thành và kết quả đánh giá của học viên dựa trên các khóa học đã đăng ký.

## Tổng quan

Báo cáo cung cấp cái nhìn tổng thể về các chỉ số quan trọng liên quan đến việc triển khai đào tạo, giúp bộ phận quản lý đưa ra quyết định tối ưu hóa chương trình học.

## Các bộ lọc báo cáo (Filters)

Để có kết quả chính xác, người dùng có thể tùy chỉnh các bộ lọc sau:

| Bộ lọc | Mô tả |
| :--- | :--- |
| **Khóa học** | Chọn một hoặc nhiều **Mặt hàng** (Khóa học) cụ thể để đánh giá. |
| **Học viên** | Lọc theo tên học viên hoặc nhóm khách hàng/nhân viên. |
| **Kho đào tạo** | Lọc theo địa điểm hoặc **Kho** tổ chức lớp học. |
| **Thời gian** | Khoảng thời gian diễn ra khóa học hoặc thời gian **Xác nhận** kết quả. |

## Hướng dẫn sử dụng

1. **Truy cập báo cáo:**
   - Đi đến module Đào tạo (Training).
   - Chọn **Báo cáo Đánh giá theo Khóa học**.

2. **Thiết lập bộ lọc:**
   - Chọn các tiêu chí cần thiết (ví dụ: chọn **Khóa học** cụ thể).
   - Nhấn **Lọc** để cập nhật dữ liệu.

3. **Thao tác dữ liệu:**
   - **Lưu (Save):** Bạn có thể lưu các thiết lập bộ lọc để sử dụng cho các lần sau.
   - **Xuất dữ liệu:** Sử dụng chức năng xuất Excel/PDF để lưu trữ báo cáo ngoại tuyến.

## Các chỉ số chính trong báo cáo

* **Tỷ lệ hoàn thành:** Phần trăm học viên đã hoàn thành khóa học so với tổng số đăng ký.
* **Điểm đánh giá trung bình:** Điểm số thu được sau khi thực hiện **Kiểm tra chất lượng (QI)** cuối khóa.
* **Trạng thái thanh toán:** Theo dõi xem học viên đã thực hiện **Thanh toán (Payment)** đầy đủ cho khóa học hay chưa thông qua các **Hóa đơn (Invoice)** liên quan.
* **Tình trạng vật tư:** Kiểm tra việc cấp phát tài liệu học tập thông qua **Yêu cầu vật tư (MR)** và **Phiếu kho (SE)**.

## Lưu ý quan trọng

* Đảm bảo tất cả các **Đơn bán hàng (SO)** liên quan đến khóa học đã được **Xác nhận (Submit)** để dữ liệu doanh thu được cập nhật chính xác.
* Kiểm tra kỹ **Tồn kho (Stock)** của các tài liệu học tập trong **Kho (Warehouse)** trước khi bắt đầu khóa học.
* Các bút toán liên quan đến học phí sẽ được tự động ghi nhận vào **Bút toán (JE)** sau khi **Hóa đơn (Invoice)** được **Xác nhận (Submit)**.

---
[Quay lại danh sách báo cáo](../reports/training_reports.md) | [Hướng dẫn sử dụng ERPNext v16](../docs/index.md)