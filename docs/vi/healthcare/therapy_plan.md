<!-- add-breadcrumbs -->

# Phác đồ trị liệu

> Được giới thiệu trong Phiên bản 13

Phác đồ trị liệu liệt kê tất cả các liệu pháp cần thiết cho Bệnh nhân cùng với số buổi trị liệu sẽ được thực hiện cho mỗi liệu pháp. Nó cũng theo dõi tiến độ dựa trên số buổi đã hoàn thành.

Để tạo một Phác đồ trị liệu, hãy đi tới:

> Home > Healthcare > Rehabilitation and Physiotherapy > Therapy Plan

## 1. Cách tạo Loại trị liệu

## 1.1 Phác đồ trị liệu để lập hóa đơn cho từng Buổi trị liệu riêng lẻ

1. Đi tới danh sách Phác đồ trị liệu, nhấn vào Mới.
2. Chọn Naming Series.
3. Chọn Bệnh nhân.
4. Chọn Ngày bắt đầu cho Phác đồ.
5. Để thêm các liệu pháp vào phác đồ, nhấn vào nút **Add Row** trong bảng con. Chọn Loại trị liệu và thiết lập số buổi cần thiết để hoàn thành.
6. Lưu.

<img class="screenshot" alt=Therapy Plan" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/therapy-plan.png">

## 1.2 Phác đồ trị liệu từ Mẫu phác đồ trị liệu

Mẫu phác đồ trị liệu được một số cơ sở y tế sử dụng để kê phác đồ trị liệu dưới dạng các gói. Trong những trường hợp như vậy, số buổi thực hiện và tổng chi phí được cố định. Phác đồ trị liệu được tạo bằng Mẫu phác đồ trị liệu sẽ không được lập hóa đơn cho từng buổi riêng lẻ mà cho toàn bộ gói.

1. Chọn Naming Series.
2. Chọn Bệnh nhân.
3. Thiết lập Ngày bắt đầu cho Phác đồ trị liệu.
4. Chọn [Therapy Plan Template](/docs/v13/user/manual/en/healthcare/therapy_plan_template) mà bạn muốn tạo Phác đồ.
5. Các Loại trị liệu và Số buổi sẽ được tự động lấy dữ liệu.
6. Lưu.

<img class="screenshot" alt="Therapy Plan from Therapy Template" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/therapy-plan-from-template.gif">

Khi lấy Dịch vụ y tế để lập hóa đơn, Phác đồ trị liệu chỉ có sẵn để lập hóa đơn nếu phác đồ được tạo bằng Mẫu phác đồ trị liệu. Nếu Phác đồ trị liệu không được tạo từ Mẫu phác đồ trị liệu, các Buổi trị liệu riêng lẻ sẽ được lấy dữ liệu trong quá trình lập hóa đơn.

<img class="screenshot" alt="Therapy Plan Template Invoice" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/therapy-plan-template-invoice.gif">

## 2. Các tính năng

### 2.1 Tự động tạo Phác đồ trị liệu từ Cuộc thăm khám của bệnh nhân

Bạn có thể kê các liệu pháp trong Cuộc thăm khám của bệnh nhân và một Phác đồ trị liệu sẽ được tự động tạo sau khi Xác nhận Cuộc thăm khám của bệnh nhân.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/therapy-encounter.jpg">

### 2.2 Tạo và Theo dõi các Buổi trị liệu

Bạn có thể tạo Buổi trị liệu từ Phác đồ trị liệu. Nó sẽ cung cấp cho bạn các tùy chọn dựa trên các Loại trị liệu đã được kê trong phác đồ hiện tại.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/create-therapy-session.png">

Sau khi Buổi trị liệu được Xác nhận, số lượng _Sessions Completed_ (Số buổi đã hoàn thành) cho Loại trị liệu đó sẽ được tự động cập nhật trong Phác đồ trị liệu.

### 2.3 Tạo Hóa đơn bán hàng từ Phác đồ trị liệu

Nếu Phác đồ trị liệu được tạo từ Mẫu phác đồ trị liệu và chưa được lập hóa đơn, nó sẽ cung cấp cho bạn tùy chọn để tạo Hóa đơn bán hàng từ Phác đồ trị liệu.

<img class="screenshot" alt="Sales Invoice from Therapy Plan" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/sales-invoice-from-therapy-plan.png">

## 3. Các chủ đề liên quan
1. [Therapy Type](/docs/v13/user/manual/en/healthcare/therapy_type)
1. [Therapy Session](/docs/v13/user/manual/en/healthcare/therapy_session)
1. [Patient Encounter](/docs/v13/user/manual/en/healthcare/patient_encounter)

{next}