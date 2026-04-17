<!-- add-breadcrumbs -->

# Phiên trị liệu

> Được giới thiệu trong Phiên bản 13

ERPNext giúp bạn theo dõi mọi phiên trị liệu được thực hiện với Bệnh nhân trong DocType Phiên trị liệu. Việc đặt lịch hẹn là tùy chọn đối với một Phiên trị liệu. Nó giúp bạn theo dõi tiến trình của Bệnh nhân bằng cách ghi lại Số lần mục tiêu, Số lần đã hoàn thành và Mức độ hỗ trợ cần thiết để Bệnh nhân hoàn thành mỗi Bài tập.

Để tạo một Phiên trị liệu, hãy đi đến:

> Home > Healthcare > Rehabilitation and Physiotherapy > Therapy Session

## 1. Cách tạo một Phiên trị liệu

### 1.1 Tạo một tài liệu Phiên trị liệu

1. Đi đến danh sách Phiên trị liệu, nhấn vào Mới.
2. Chọn Chuỗi đặt tên (Naming Series).
3. Nếu một Lịch hẹn bệnh nhân đã được đặt cho phiên này, hãy chọn Lịch hẹn bệnh nhân đó. Tất cả các chi tiết khác sẽ được tự động lấy ra.
4. Nếu chưa có Lịch hẹn nào được đặt, hãy chọn Bệnh nhân.
5. Chọn Loại trị liệu và Kế hoạch trị liệu cho Bệnh nhân đó. Ngay khi bạn chọn Loại trị liệu, Đơn vị dịch vụ y tế, Đơn giá, Thời lượng, Khoa y tế và tất cả các Bài tập từ mẫu sẽ được tự động lấy ra.
6. Nếu phiên trị liệu được thực hiện bởi một chuyên gia trị liệu, hãy chọn chuyên gia đó trong trường Chuyên gia y tế.
7. Bạn có thể chọn Ngày và Giờ bắt đầu.
8. Lưu.
9. Sau đó, bạn có thể tăng số lượng Số lần đã hoàn thành, và khi một bài tập cụ thể đã được hoàn thành, hãy chọn Mức độ hỗ trợ cần thiết cho bài tập đó. Các chỉ số số lần được hiển thị trên trang tổng quan của tài liệu. Màu xanh lá cây biểu thị đã hoàn thành, màu cam biểu thị chưa đạt được mục tiêu.
10. Sau khi bạn đã ghi lại toàn bộ phiên trị liệu với các số lần, bạn có thể xác nhận tài liệu. Kế hoạch trị liệu sau đó sẽ được cập nhật với số lượng các phiên.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/therapy-session.png">

### 1.2 Tạo Phiên trị liệu từ Lịch hẹn bệnh nhân

Sau khi đặt lịch hẹn cho một Loại trị liệu, hãy nhấn vào **Create > Therapy Session** để tạo một phiên từ Lịch hẹn bệnh nhân.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/therapy-session-from-appointment.png">

Tham khảo [Kế hoạch trị liệu](/docs/v13/user/manual/en/healthcare/therapy_plan) để hiểu về cách tạo các Phiên trị liệu từ Kế hoạch trị liệu.

## 2. Các tính năng

### 2.1 Lập hóa đơn cho các Phiên trị liệu

Để lập hóa đơn cho các Phiên trị liệu:

1. Bạn có thể tạo một Hóa đơn bán hàng mới.
2. Chọn Bệnh nhân.
3. Nhấn vào **Get Items From > Healthcare Services_**.
4. Hộp thoại sẽ hiển thị cho bạn tất cả các phiên chưa được lập hóa đơn của bệnh nhân đó. Sau khi chọn các mặt hàng, đơn giá cho các phiên sẽ được tự động lấy từ mẫu Loại trị liệu.
5. Bạn cũng có thể thêm các mặt hàng một cách thủ công trong bảng con "Items" để lập hóa đơn.
6. Lưu và Xác nhận.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/therapy-invoicing.png">

## 3. Các chủ đề liên quan
1. [Loại trị liệu](/docs/v13/user/manual/en/healthcare/therapy_type)
1. [Kế hoạch trị liệu](/docs/v13/user/manual/en/healthcare/therapy_plan)
1. [Lịch hẹn bệnh nhân](/docs/v13/user/manual/en/healthcare/patient_appointment)

{next}