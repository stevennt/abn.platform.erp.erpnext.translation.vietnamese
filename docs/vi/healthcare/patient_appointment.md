<!-- add-breadcrumbs -->
# Hẹn khám bệnh

ERPNext Healthcare cho phép bạn đặt Hẹn khám bệnh cho bất kỳ ngày nào và thông báo cho bệnh nhân qua Email hoặc SMS. Bạn có thể dễ dàng sắp xếp các cuộc hẹn cho từng Chuyên gia y tế dựa trên lịch trình sẵn có của họ.

<!-- <img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/appointment_calendar.png"> -->

Để tạo một Hẹn khám bệnh, hãy đi tới:

> Home > Healthcare > Consultation > Patient Appointment


## 1. Điều kiện tiên quyết

Trước khi tạo Hẹn khám bệnh, các thông tin sau cần được tạo trước:

* [Patient](patient.md)
* [Healthcare Practitioner](healthcare_practitioner.md)
* [Practitioner Schedule](practitioner_schedule.md)

Bạn có thể đặt lịch hẹn cho một Bệnh nhân đã đăng ký bằng cách tìm kiếm Bệnh nhân theo ID Bệnh nhân, Tên, Email hoặc Số điện thoại di động. Bạn cũng có thể đăng ký Bệnh nhân mới ngay từ màn hình Hẹn khám bằng cách chọn "Create a new Patient" trong trường Patient.

  <img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient_appointment_link.png">

## 2. Cách tạo Hẹn khám bệnh

1. Đi tới danh sách Patient Appointment, nhấn vào New.
2. Chọn [Patient](patient.md) mà bạn muốn thiết lập cuộc hẹn. Tên Bệnh nhân, Giới tính và Tuổi của Bệnh nhân sẽ được tự động lấy dữ liệu khi chọn Bệnh nhân. Nếu bệnh nhân là Bệnh nhân nội trú (Đã nhập viện), thì Hồ sơ nội trú cũng sẽ được tự động lấy cho họ.
3. Bạn có thể tùy chọn chọn [Service Unit](healthcare_service_unit.md) nơi bạn muốn lên lịch hẹn. Nếu bạn đang đặt lịch hẹn cho một bệnh nhân nội trú, bạn cũng có thể chọn đơn vị dịch vụ nơi bệnh nhân đang nhập viện, bên cạnh các đơn vị dịch vụ đã được bật cấu hình _Allow Appointments_.
4. Nếu bạn cần đặt Hẹn khám cho Thủ thuật lâm sàng, hãy chọn một [Clinical Procedure Template](clinical_procedure_template.md). Nếu bạn muốn chọn một Thủ thuật lâm sàng đã được chỉ định cho bệnh nhân trong lần Tiếp xúc bệnh nhân trước đó, hãy nhấp vào nút **Get Prescribed Clinical Procedures** để chọn từ danh sách các Thủ thuật lâm sàng đã được chỉ định cho Bệnh nhân đã chọn. Quy trình tương tự cũng được áp dụng để lấy các Loại trị liệu đã được chỉ định bằng cách sử dụng nút **Get Prescribed Therapies** hoặc chỉ cần chọn một [Therapy Type](therapy_type.md).
5. Bạn có thể tùy chọn chọn "Appointment Type" và "Duration (in minutes)" (Thời lượng tính bằng phút). Lưu ý rằng, việc chọn "Appointment Type" sẽ tự động thiết lập thời lượng của cuộc hẹn như đã cấu hình trong Appointment Type. Điều này cho phép bạn ghi đè thời lượng cuộc hẹn được thiết lập bởi Practitioner Schedule và các khung giờ sẽ tự động điều chỉnh sang khung giờ trống tiếp theo.
6. Nếu bạn đã tích chọn "Automate Appointment Invoicing" trong [Healthcare Settings](healthcare_settings.md), việc thiết lập các trường "Mode of Payment" và "Amount" trong Patient Appointment là bắt buộc.
7. Sau đó nhấp vào nút **Check Availability**. Nó sẽ cho phép bạn chọn Khoa y tế, Chuyên gia y tế và Ngày mà cuộc hẹn sẽ được đặt. Sau khi chọn các chi tiết, tất cả các khung giờ trống của chuyên gia sẽ được lấy từ [Practitioner Schedule](practitioner_schedule.md) và hiển thị với các chỉ báo trạng thái cho ngày đã chọn. Bạn có thể chọn một khung giờ và nhấn **Book**.
8. Sau khi đã đặt, thời gian dự kiến của cuộc hẹn, Đơn vị dịch vụ theo Chuyên gia và Trạng thái phù hợp sẽ được thiết lập trong tài liệu.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/check_availability.png">

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/appointment.png">

## 3. Các tính năng

### 3.1 Lịch hẹn khám bệnh (Patient Appointment Calendar)

Bạn có thể nhấp vào chế độ xem "Calendar" từ chế độ xem danh sách Patient Appointment. Các loại cuộc hẹn có thể được phân biệt bằng cách thiết lập trường "Color" trong [Appointment Type](appointment_type.md)

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/healthcare-appointments.png">

### 3.2 Thay đổi lịch hẹn (Appointment Rescheduling)

Bạn có thể thay đổi lịch trình cuộc hẹn bằng cách nhấp vào nút **Reschedule** trong tài liệu và thực hiện các bước tương tự.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/reschedule.png">

### 3.3 Quản lý lịch trình

Việc đặt Hẹn khám bệnh sẽ xem xét bất kỳ Đơn xin Nghỉ phép nào đã được "Approved" (Phê duyệt) của Chuyên gia y tế (Nhân viên được liên kết trong danh mục gốc) và không cho phép đặt Hẹn khám bệnh vào những ngày đó.

Khi đặt lịch, hệ thống cũng kiểm tra việc Trùng lịch hẹn và hạn chế việc đặt lịch cho cùng một khung giờ.

### 3.4 Ghi chú và Chuyển tuyến

Trong phần "More Info" của tài liệu Patient Appointment, người dùng có thể thêm "Notes" (Ghi chú) và cũng có thể chọn "Referring Practitioner" (Chuyên gia chuyển tuyến) để giúp theo dõi việc chuyển tuyến.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/more_info.png">

### 3.5 Thông báo SMS cho Bệnh nhân ngoại trú

Bạn có thể tùy chọn cấu hình [Healthcare Settings](healthcare_settings.md) trong ERPNext để tự động gửi thông báo SMS cho Bệnh nhân về việc xác nhận đặt lịch thông qua "Out-Patient SMS Alerts".

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/outpatient_sms_alert.png">

### 3.6 Tự động hóa Hóa đơn cuộc hẹn

Để tự động tạo Hóa đơn bán hàng ngay khi bạn đặt Hẹn khám bệnh, bạn có thể bật cấu hình _Automate Appointment Invoicing_ trong [Healthcare Sett