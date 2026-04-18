<!-- add-breadcrumbs -->

# Tiếp xúc Bệnh nhân

ERPNext Healthcare cho phép bạn ghi lại mọi lần tiếp xúc với bệnh nhân thông qua chứng từ Tiếp xúc Bệnh nhân. Bạn cũng có thể tạo một Tiếp xúc Bệnh nhân dựa trên một Lịch hẹn đã được đặt trước đó.

## 1. Cách tạo Tiếp xúc Bệnh nhân

Để tạo một Tiếp xúc Bệnh nhân, hãy đi đến:

> Trang chủ > Healthcare > Consultation > Patient Encounter

1. Chọn Naming Series cho chứng từ.
2. Nếu bạn chọn một Lịch hẹn, các chi tiết về Bệnh nhân, Khoa và Chuyên gia Y tế, v.v. sẽ được tự động lấy ra.
3. Nếu không, bạn có thể chọn Bệnh nhân một cách riêng biệt. Các chi tiết về Bệnh nhân sẽ được lấy ra.
4. Chọn Chuyên gia Y tế. Khoa sẽ được tự động lấy ra.
5. Thiết lập Ngày và Giờ tiếp xúc.
6. Chọn Triệu chứng và Chẩn đoán trong phần Encounter Impression. Bạn có thể chọn bao gồm dữ liệu đã ghi lại trong bản in Tiếp xúc Bệnh nhân bằng cách tích vào "In Print".
7. Lưu.

Bạn cũng có thể tạo và ghi lại chi tiết tiếp xúc cho một bệnh nhân từ Lịch hẹn Bệnh nhân, Tiếp xúc Bệnh nhân hoặc các chứng từ danh mục Bệnh nhân bằng cách sử dụng nút **Create > Patient Encounter**.
Nếu bạn đang tạo Tiếp xúc Bệnh nhân một cách thủ công, bạn có thể tìm kiếm Bệnh nhân theo tên, email, số điện thoại, v.v.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient_encounter_1.png">

## 2. Các tính năng

### 2.1 Mã hóa Y tế

Bạn cũng có thể đính kèm một hoặc nhiều Mã Y tế để chỉ định Chẩn đoán trong phần Medical Coding. Bạn sẽ phải chọn Tiêu chuẩn Mã Y tế mà bạn muốn dùng để mã hóa chẩn đoán, sau đó chọn Mã bằng cách tìm kiếm chính Mã đó hoặc Mô tả Mã.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/encounter_4.png">

### 2.2 Thuốc

Bạn có thể kê đơn thuốc trong phần Medication bằng cách chọn các mã thuốc (Mặt hàng Kho) và liều lượng phù hợp. Nếu bạn không quản lý Kho và các Mặt hàng chưa được cấu hình, bạn có thể chỉ cần nhập tên Thuốc và hàm lượng trong trường Strength để được in ra. Bạn có thể tùy chọn thêm nhận xét trong mục bảng Thuốc và chọn Dạng bào chế (Viên nén, Siro).

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/encounter_medication.png">

Nếu bạn có duy trì tồn kho, Kho thuốc có thể được quản lý bằng cách sử dụng Phân hệ Kho:

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/healthcare-inventory.png">

### 2.3 Xét nghiệm (Thăm dò)

Trong phần Investigations, bạn có thể chỉ định các Xét nghiệm cho Bệnh nhân. Nếu bạn đã cấu hình các Mẫu Xét nghiệm, bạn có thể chọn từ danh sách và tùy chọn thêm nhận xét.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/encounter_investigation.png">

Các Xét nghiệm có thể được cấu hình để tự động tạo khi Xác nhận Hóa đơn bán hàng bằng cách tích vào _Create Lab Test(s) on Sales Invoice Submission_ trong [Healthcare Settings](healthcare_settings.md).

### 2.4 Thủ thuật Lâm sàng

Bạn cũng có thể chỉ định một Thủ thuật Lâm sàng để thực hiện cho Bệnh nhân trong phần Procedures. Chọn Mẫu Thủ thuật Lâm sàng và tùy chọn chỉ định ngày thực hiện Thủ thuật.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/encounter_procedures.png">

### 2.5 Trị liệu

Nếu cơ sở Y tế của bạn cung cấp các dịch vụ Phục hồi chức năng và Vật lý trị liệu, bạn có thể chỉ định các liệu pháp trong Tiếp xúc Bệnh nhân và một Kế hoạch Trị liệu sẽ được tự động tạo khi Xác nhận Tiếp xúc Bệnh nhân.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/therapy-encounter.jpg">

### 2.6 Thanh toán và Đơn thuốc

Người dùng Nhà thuốc (Bán hàng / Kế toán) có thể lấy các đơn thuốc và chỉ định xét nghiệm (Xét nghiệm) từ Tiếp xúc Bệnh nhân bằng cách sử dụng **Get items from > Prescription** trong Hóa đơn bán hàng.

Các chỉ định Thủ thuật Lâm sàng có thể được lấy bằng nút **Get Prescribed Clinical Procedures** khi đặt Lịch hẹn cho thủ thuật đó. Sau đó, chúng sẽ có sẵn để thanh toán thông qua **Get items from > Healthcare Services**.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/prescription.png">

## 3. Các hành động

> Lưu ý: Người dùng phải có quyền hạn phù hợp (Vai trò người dùng) để xem các nút

Sau khi bạn đã hoàn tất việc điền tất cả các phần cần thiết, bạn có thể Xác nhận chứng từ. Các nút Hành động sẽ chỉ hiển thị sau khi đã Xác nhận.

  * Dấu hiệu sinh tồn: Nút **Create > Vital Signs** sẽ đưa bạn đến màn hình Dấu hiệu sinh tồn mới để ghi lại các chỉ số sinh tồn của Bệnh nhân.

  * Hồ sơ Y tế: Nút **Create > Medical Record** sẽ đưa bạn đến màn hình Hồ sơ Y tế mới để ghi lại chi tiết. Bạn cũng có thể đính kèm một số báo cáo vào hồ sơ.

  * Thủ thuật Lâm sàng: Sử dụng nút **Create > Clinical Procedure** bạn có thể tạo một Thủ thuật Lâm sàng.

  * Lịch sử Bệnh nhân: **View > Patient History**.

  * Lập lịch Nhập viện: Bạn có thể Lập lịch Nhập viện bằng nút này. Việc này sẽ tạo một Hồ sơ Nội trú.

> Biểu mẫu này đã được thay đổi trong Phiên bản 13

## 4. Các chủ đề liên quan

1. [Lịch hẹn Bệnh nhân](patient_appointment.md)
1. [Mẫu Thủ thuật Lâm sàng](clinical_procedure_template.md)

{next}