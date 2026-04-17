<!-- add-breadcrumbs -->
# Đơn thuốc Nội trú

**Đơn thuốc Nội trú (IPMO) được tạo ra để giúp quy trình điều dưỡng trở nên dễ dàng hơn. Khi bệnh nhân nhập viện, có những loại thuốc cần được cung cấp cho họ theo lịch trình đã được chỉ định. Đơn thuốc Nội trú được tạo để kê đơn thuốc cho bệnh nhân nội trú cùng với thông tin đơn vị dịch vụ, loại thuốc, liều lượng, dạng bào chế, cũng như ngày và giờ phải uống thuốc.**

Để truy cập danh sách Đơn thuốc Nội trú, hãy đi đến:

> Home > Healthcare > Inpatient > Inpatient Medication Order

## 1. Điều kiện tiên quyết

Trước khi tạo Đơn thuốc Nội trú, bạn cần tạo các bản ghi sau trước:

* [Patient](/docs/v13/user/manual/en/healthcare/patient)
* [Inpatient Record](/docs/v13/user/manual/en/healthcare/inpatient_record)

## 2. Cách tạo Đơn thuốc Nội trú

Bạn có thể tạo Đơn thuốc Nội trú theo hai cách.

### 2.1 Tạo thủ công

1. Đi đến danh sách Đơn thuốc Nội trú và nhấp vào New.
2. Chọn Bệnh nhân (Patient). Danh sách bệnh nhân đã được lọc để chỉ hiển thị các lựa chọn là bệnh nhân nội trú tại đây.
3. Có thể chọn Chuyên gia y tế (Healthcare Practitioner).
4. Thiết lập Ngày bắt đầu (Start Date) cho đơn thuốc. Lịch trình cho các loại thuốc được kê đơn sẽ được tạo bắt đầu từ ngày này.
5. Trong bảng Đơn thuốc (Medication Orders), có nút **Add Medication Orders**. Nhấp vào nút này. Một hộp thoại sẽ hiển thị để điền chi tiết đơn thuốc.
6. Chọn loại thuốc (item), liều lượng, chu kỳ và dạng bào chế. Sau đó nhấp vào **Add**.
7. Các mục lịch trình chi tiết cho đơn thuốc bắt đầu từ Ngày bắt đầu sẽ được thêm vào bảng. Đóng hộp thoại.
8. Lưu và Xác nhận. Ngày kết thúc (End Date) sẽ được thiết lập tự động dựa trên thời gian kê đơn.
9. Bạn có thể xem Tổng số đơn (Total Orders) và Số đơn đã hoàn thành (Completed Orders) trong phần Chi tiết khác (Other Details).

<img class="screenshot" alt="IPMO-PE" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/ipmo-manual.gif">

### 2.2 IPMO từ Lượt khám của Bệnh nhân (Patient Encounter)

1. Sau khi tạo Lượt khám của Bệnh nhân (Patient Encounter) cho một bệnh nhân nội trú, với các loại thuốc được kê trong bảng Đơn thuốc (Drug Prescription), bạn có thể thấy tùy chọn để tạo Đơn thuốc Nội trú tại mục **Create > Inpatient Medication Order**.
2. Bạn có thể sử dụng nút này để tạo IPMO. Một IPMO với chế độ xem mở rộng của lịch trình sẽ được tạo. Lưu và Xác nhận.

<img class="screenshot" alt="IPMO-PE" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/ipmo-pe.gif">

### 2.3 Trạng thái

Trạng thái của IPMO được quản lý bởi tổng số các mục đơn thuốc đã hoàn thành. Các mục đơn thuốc được đánh dấu là đã hoàn thành khi một [Inpatient Medication Entry](/docs/v13/user/manual/en/healthcare/inpatient_medication_entry) được tạo cho mục đơn thuốc đó.

* **Draft**: Bản nháp đã được lưu nhưng chưa được xác nhận vào hệ thống.
* **Pending**: Chưa có mục đơn thuốc nào trong bảng Đơn thuốc được hoàn thành.
* **In Progress**: Một số mục đơn thuốc trong bảng Đơn thuốc đã được hoàn thành.
* **Completed**: Tất cả các mục đơn thuốc trong bảng Đơn thuốc đã được hoàn thành.
* **Cancelled**: Đơn thuốc Nội trú đã bị hủy.

<img class="screenshot" alt="IPMO-PE" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/ipmo-status.png">

## 3. Các chủ đề liên quan

1. [Inpatient Medication Entry](/docs/v13/user/manual/en/healthcare/inpatient_medication_entry)
1. [Patient Encounter](/docs/v13/user/manual/en/healthcare/patient_encounter)

{next}