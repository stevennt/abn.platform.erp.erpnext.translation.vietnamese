<!-- add-breadcrumbs -->
# Lịch sử y tế của Bệnh nhân

Việc duy trì hồ sơ y tế chính xác và đầy đủ của bệnh nhân là một trong những nguyên tắc cơ bản đối với các bác sĩ và nhà cung cấp dịch vụ chăm sóc sức khỏe. Trên hết, sự thuận tiện trong việc truy cập thông tin của bác sĩ là yếu tố then chốt để cung cấp dịch vụ chăm sóc hiệu quả và chất lượng cao.

ERPNext Healthcare giúp bạn lập lịch sử y tế của Bệnh nhân bất cứ lúc nào bằng cách tìm kiếm và chọn Bệnh nhân một cách nhanh chóng.

Để xem Lịch sử Bệnh nhân, bạn có thể đi tới:

> Home > Healthcare > Records and History > Patient History

Lịch sử các lần tương tác của bệnh nhân được duy trì trong loại DocType Hồ sơ y tế của Bệnh nhân. Các hồ sơ này được tự động tạo khi Xác nhận Patient Encounter, Vital Signs, Clinical Procedure, Lab Test, Therapy Session, và Inpatient Medication Order.

Từ phiên bản 13 trở đi, bạn có thể cấu hình tất cả các loại DocType và các trường nào sẽ là một phần của Hồ sơ y tế của Bệnh nhân và Lịch sử Bệnh nhân bằng cách sử dụng [Patient History Settings](patient_history_settings.md).

Nút **View > Patient History** có sẵn trong tất cả các biểu mẫu mà các Bác sĩ sử dụng để họ có thể dễ dàng chuyển sang trang "Patient History" để xem lịch sử của bệnh nhân.

## 1. Các phần

- **Thông tin Bệnh nhân (Patient Information)**: Ngay khi bạn chọn Bệnh nhân, tất cả thông tin từ hồ sơ Bệnh nhân sẽ được truy xuất và hiển thị ở thanh bên của trang.
- **Chỉ số sinh tồn của Bệnh nhân (Patient Vitals)**: Dựa trên các Chỉ số sinh tồn được ghi lại cho bệnh nhân, phần này hiển thị các biểu đồ để trực quan hóa sự thay đổi của Huyết áp, Nhịp thở/Nhịp tim, Nhiệt độ và BMI theo thời gian. Bạn có thể nhấp vào từng nút riêng biệt để hiển thị biểu đồ tương ứng.
- **Tài liệu cho các lần tương tác của Bệnh nhân (Documents for Patient Interactions)**: Một dòng thời gian các tài liệu được truy xuất từ Hồ sơ y tế của Bệnh nhân được hiển thị trong phần này. Bạn có thể thấy tên DocType, liên kết đến tài liệu và ngày mà hồ sơ được tạo. Khi tải trang, bản tóm tắt của mỗi tài liệu sẽ được hiển thị. Bạn có thể sử dụng mũi tên bên dưới mỗi tài liệu để xem chi tiết.
- **Bộ lọc (Filters)**: Từ phiên bản 13 trở đi, bạn cũng có thể lọc tất cả các DocType mà bạn muốn xem các lần tương tác bằng cách sử dụng bộ lọc danh sách chọn nhiều. Sử dụng bộ lọc phạm vi ngày, bạn có thể lấy được luồng lịch sử giữa hai ngày bất kỳ.

<img class="screenshot" alt="Patient History" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient-history-1.gif">

## 2. Thêm Hồ sơ y tế thủ công

Hồ sơ y tế sẽ tự động theo dõi tất cả các Khiếu nại, Chẩn đoán và các thông tin khác được ghi lại như một phần của Patient Encounter, Vital Signs, Lab Investigations, các Clinical Procedures được chỉ định, Nhập viện, v.v.

Trong tài liệu Bệnh nhân, **Create > Medical Record** sẽ cho phép bạn ghi chép các ghi chú một cách thủ công. Bạn cũng có thể đính kèm tệp khi thực hiện việc này, và Hồ sơ y tế sẽ hiển thị các liên kết đến tệp đính kèm bên cạnh các ghi chú. Bạn cũng có thể thêm Hồ sơ y tế từ Patient Encounter.

<img class="screenshot" alt="Patient Medical Record" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/medical_record_2.png">

## 3. Các chủ đề liên quan

1. [Patient History Settings](patient_history_settings.md)

{next}