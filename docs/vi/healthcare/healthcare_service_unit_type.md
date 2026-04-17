<!-- add-breadcrumbs -->

# Loại Đơn vị Dịch vụ Y tế

Bạn có thể xác định các thuộc tính tiêu chuẩn của [Đơn vị Dịch vụ Y tế](/docs/v13/user/manual/en/healthcare/healthcare_service_unit) bằng cách sử dụng Loại Đơn vị Dịch vụ Y tế. Bằng cách cấu hình các loại đơn vị dịch vụ khác nhau trong cơ sở của bạn với các đơn giá và thuộc tính khác tương ứng, bạn có thể dễ dàng tạo nhiều Đơn vị Dịch vụ Y tế chỉ bằng cách chọn loại. Loại Đơn vị Dịch vụ Y tế là một loại chung. Ví dụ, "Phòng phẫu thuật" có thể là một Loại Đơn vị Dịch vụ Y tế và Neurology-OT, Procedure-Room-1, v.v. có thể là các Đơn vị Dịch vụ Y tế.

## 1. Cách tạo Loại Đơn vị Dịch vụ Y tế

Để tạo một Loại Đơn vị Dịch vụ Y tế, hãy đi đến:

> Trang chủ > Healthcare > Masters > Healthcare Service Unit Type

- **Service Unit Type**: Nhập tên duy nhất cho Loại Đơn vị Dịch vụ.

Bây giờ có hai tùy chọn:

- **Allow Appointments**: Đánh dấu vào đây nếu loại đơn vị dành cho cơ sở Điều trị Ngoại trú.
- **Inpatient Occupancy**: Đánh dấu vào đây nếu loại đơn vị dành cho cơ sở Điều trị Nội trú.

Nhưng "Consulting Rooms" chỉ có thể cho phép Hẹn lịch và

Tùy chọn sau sẽ xuất hiện nếu bạn đánh dấu "Allow Appointments":

- **Allow Overlap**: Đánh dấu vào đây nếu loại đơn vị có thể được sử dụng bởi nhiều hơn một bệnh nhân hoặc cho nhiều hơn một cuộc hẹn cùng một lúc.

Ví dụ, các Trung tâm Hoạt động Thể chất sẽ cho phép Hẹn lịch có sự trùng lặp:

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/healthcare_service_unit_type_1.png">

Tuy nhiên, các phòng Tư vấn sẽ chỉ cho phép Hẹn lịch mà không có sự trùng lặp:

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/healthcare_service_unit_type_2.png">

Tùy chọn sau sẽ xuất hiện nếu bạn đánh dấu "Inpatient Occupancy":

- **Is Billable**: Đánh dấu vào đây nếu loại đơn vị dành cho IPD (nội trú) có thể tính phí như Giường bệnh.

Ví dụ, các Phòng phẫu thuật sẽ có Chỗ ở Nội trú được tính phí. Nếu bạn đánh dấu "Inpatient Occupancy" và "Is Billable", hệ thống sẽ yêu cầu Chi tiết Mặt hàng để tạo một mặt hàng cho Loại Đơn vị Dịch vụ sẽ được sử dụng để lập hóa đơn:

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/healthcare_service_unit_type.png">

Mặt hàng sẽ tự động được tạo và liên kết với tài liệu khi Lưu.

Nếu Loại Đơn vị Dịch vụ Y tế không được sử dụng, bạn có thể vô hiệu hóa nó. Việc vô hiệu hóa sẽ không cho phép chọn mặt hàng đã được tạo cho loại đó khi lập hóa đơn.

Nếu bạn muốn thay đổi Mã mặt hàng của mặt hàng được tạo cho Loại Đơn vị Dịch vụ Y tế có thể tính phí, hãy nhấp vào nút **Change Item Code**.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/healthcare_service_unit_type_3.png">

> Biểu mẫu này đã được thay đổi trong Phiên bản 13

## 2. Các chủ đề liên quan
1. [Healthcare Service Unit](/docs/v13/user/manual/en/healthcare/healthcare_service_unit)

{next}