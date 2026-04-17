Do bạn không cung cấp nội dung gốc của trang "Final Assessment Grades" từ phiên bản v13, tôi sẽ xây dựng lại cấu trúc tài liệu này theo chuẩn ERPNext v16, áp dụng đúng bộ thuật ngữ bạn đã yêu cầu và định dạng Markdown chuyên nghiệp.

Nếu bạn có nội dung cụ thể cần chuyển đổi, hãy gửi cho tôi. Dưới đây là bản mẫu chuẩn hóa:

---

# Điểm Đánh giá Cuối kỳ (Final Assessment Grades)

Tài liệu này hướng dẫn cách quản lý và xử lý các điểm đánh giá cuối kỳ trong hệ thống ERPNext v16. Quy trình này liên quan đến việc cập nhật kết quả học tập, đối soát với **Hóa đơn (Invoice)** học phí và cập nhật trạng thái hoàn thành cho **Khách hàng (Customer)** (trong trường hợp này là Học viên).

## Tổng quan quy trình

Việc quản lý điểm số cuối kỳ được kết nối trực tiếp với các phân hệ quản lý đào tạo và tài chính để đảm bảo học viên chỉ được công nhận kết quả sau khi đã hoàn tất các nghĩa vụ tài chính.

1. **Nhập điểm**: Tạo bản ghi điểm cho từng **Mặt hàng (Item)** là khóa học/môn học.
2. **Xác nhận (Submit)**: Sau khi kiểm tra, giảng viên thực hiện **Xác nhận (Submit)** điểm để ghi nhận vào hệ thống.
3. **Đối soát thanh toán**: Hệ thống kiểm tra trạng thái **Thanh toán (Payment)** của **Hóa đơn (Invoice)** liên quan.
4. **Xuất chứng chỉ/Kết quả**: Sau khi **Lưu (Save)** và **Xác nhận (Submit)**, kết quả sẽ được sẵn sàng để xuất bản.

## Các bước thực hiện

### 1. Tạo bản ghi điểm đánh giá
* Truy cập vào module Đào tạo/Học tập.
* Chọn **Mặt hàng (Item)** tương ứng với khóa học.
* Nhập điểm số cho từng học viên.
* Nhấn **Lưu (Save)** để lưu tạm bản nháp.

### 2. Kiểm tra và Xác nhận (Submit)
> [!IMPORTANT]
> Khi đã nhấn **Xác nhận (Submit)**, điểm số sẽ được khóa và không thể chỉnh sửa trực tiếp. Nếu có sai sót, bạn phải thực hiện **Hủy (Cancel)** bản ghi trước khi sửa.

* Kiểm tra kỹ lưỡng dữ liệu điểm số.
* Nhấn nút **Xác nhận (Submit)** để chính thức ghi nhận kết quả vào hệ thống.

### 3. Đối soát với Tài chính
Hệ thống sẽ tự động kiểm tra trạng thái của **Khách hàng (Customer)**:
* Nếu **Hóa đơn (Invoice)** đã được **Thanh toán (Payment)** đầy đủ: Trạng thái điểm sẽ hiển thị là "Hoàn thành".
* Nếu chưa thanh toán: Kết quả sẽ ở trạng thái "Chờ xác nhận tài chính".

## Quản lý lỗi và Điều chỉnh

| Hành động | Mô tả |
| :--- | :--- |
| **Lưu (Save)** | Lưu các thay đổi tạm thời khi đang nhập liệu. |
| **Hủy (Cancel)** | Sử dụng khi điểm đã **Xác nhận (Submit)** nhưng phát hiện sai sót nghiêm trọng. |
| **Điều chỉnh (Amend)** | Tạo một bản ghi mới dựa trên bản ghi đã **Hủy (Cancel)** để sửa lỗi. |

## Liên kết liên quan

* [Danh mục Khách hàng (Customer)](customer_list.md)
* [Quản lý Hóa đơn (Invoice)](invoice_management.md)
* [Quản lý Mặt hàng/Khóa học (Item)](item_list.md)
* [Quy trình Thanh toán (Payment)](payment_process.md)

---
*Tài liệu này được cập nhật cho phiên bản ERPNext v16.*