<!-- add-breadcrumbs -->
# Bệnh nhân

Trong ERPNext Healthcare, tài liệu Bệnh nhân tương ứng với bất kỳ cá nhân nào là người nhận các dịch vụ chăm sóc y tế mà bạn cung cấp. Đối với mỗi tài liệu, việc có một Bệnh nhân liên kết với nó là rất quan trọng.

Để tạo một Bệnh nhân mới:

> Trang chủ > Healthcare > Masters > Patient > New Patient

## 1. Cách tạo Bệnh nhân

1. Đi tới danh sách Bệnh nhân và nhấn vào New.
2. Nhập Tên, Giới tính, Nhóm máu, Ngày sinh, v.v.
3. Nhập số điện thoại di động của bệnh nhân. Điều này quan trọng nếu bạn đã bật thông báo SMS cho bệnh nhân.
4. Nhập địa chỉ email của bệnh nhân.
5. Đối với trường "Khách hàng", bạn có thể tạo một khách hàng và chọn tại đây. Nếu bạn không tạo, hãy chọn một Khách hàng có sẵn; nếu bạn đã bật "Link Customer to Patient" trong [Healthcare Settings](/docs/v13/user/manual/en/healthcare/healthcare_settings), một khách hàng sẽ tự động được tạo và liên kết ngay khi bạn Lưu tài liệu.
6. Lưu.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient_1.png">

> Lưu ý: Việc liên kết một Khách hàng với Bệnh nhân là cần thiết để thực hiện thanh toán và lập hóa đơn.

Chuyển sang chế độ xem "Image" từ thanh bên của danh sách để xem và chỉnh sửa nhiều bệnh nhân cùng với ảnh của họ.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient-repo.png">

## 2. Các tính năng

### 2.1 Ghi lại lịch sử

#### 2.1.1 Lịch sử cá nhân

Bạn có thể tùy chọn ghi lại Lịch sử cá nhân như Nghề nghiệp và Tình trạng hôn nhân cùng với các mối quan hệ của Bệnh nhân với các bệnh nhân hiện có.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient_personal_history.png">

#### 2.1.2 Ghi lại tiền sử y tế

Tùy chọn ghi lại Tiền sử y tế như Dị ứng, Thuốc, Tiền sử bệnh và Tiền sử phẫu thuật.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient_surgical_history.png">

#### 2.1.3 Ghi lại các yếu tố nguy cơ và hơn thế nữa

Ghi lại các Yếu tố nguy cơ như thói quen sử dụng thuốc lá và rượu, v.v.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient_risk_factors.png">

### 2.2 Bệnh nhân là một Khách hàng

ERPNext, đặc biệt là phân hệ Kế toán, sử dụng tài liệu **Khách hàng** để ghi nhận tất cả các giao dịch. Vì vậy, bạn có thể muốn liên kết mọi Bệnh nhân với một Khách hàng. Theo mặc định, hệ thống sẽ tạo một Khách hàng cùng với Bệnh nhân và liên kết với nó. Nếu vì lý do nào đó bạn không có ý định sử dụng phân hệ Kế toán của ERPNext, bạn có thể tắt hành vi này bằng cách hủy chọn tùy chọn "Link Customer to Patient" trong [Healthcare Settings](/docs/v13/user/manual/en/healthcare/healthcare_settings).

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient_link_customer.png">

Trong nhiều trường hợp, bạn có thể muốn liên kết nhiều Bệnh nhân với một Khách hàng duy nhất để ghi nhận các giao dịch. Ví dụ, một bác sĩ thú y sẽ yêu cầu các dịch vụ chăm sóc cung cấp cho các thú cưng khác nhau của một cá nhân được lập hóa đơn cho một Khách hàng duy nhất. Trong trường hợp đó, hãy chọn cùng một Khách hàng cho tất cả các bệnh nhân này khi tạo.

### 2.3 Phí đăng ký

Nhiều cơ sở lâm sàng thu phí đăng ký trong quá trình Đăng ký Bệnh nhân. Bạn có thể bật tính năng này bằng cách tích vào "Collect Registration Fee" trong Healthcare Settings và thiết lập số tiền phí đăng ký.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient_registration_fee.png">

Nếu bạn bật tùy chọn này, tất cả Bệnh nhân mới mà bạn tạo sẽ ở trạng thái "Disabled" (Bị vô hiệu hóa) theo mặc định và sẽ chỉ được kích hoạt sau khi Lập hóa đơn Phí đăng ký. Để tạo Hóa đơn và ghi nhận biên lai thanh toán, bạn có thể sử dụng nút **Invoice Patient Registration** trong tài liệu Bệnh nhân.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/patient_disabled.png">

> Lưu ý: Các Bệnh nhân ở trạng thái "Disabled" sẽ được lọc ra khỏi tất cả các tài liệu ERPNext Healthcare.

### 2.4 Cấp quyền truy cập Cổng thông tin Bệnh nhân
ERPNext Healthcare cho phép bạn tạo một người dùng cổng thông tin liên kết với một Bệnh nhân chỉ bằng cách nhập email người dùng. Một email chào mừng sẽ được gửi đến địa chỉ email của Bệnh nhân để "Hoàn tất" đăng ký.

### 2.5. Các hành động

> Lưu ý: Người dùng cần có quyền hạn phù hợp (User Role) để xem các nút bấm

Bạn có thể sử dụng các liên kết tài liệu trong trang tổng quan để duyệt danh sách tài liệu liên kết với bộ lọc Bệnh nhân đã được áp dụng hoặc sử dụng các biểu tượng + để tạo các bản ghi mới. Ngoài ra, tài liệu Bệnh nhân cho phép bạn:

* Xem Lịch sử sức khỏe của Bệnh nhân, bằng cách sử dụng nút **View > Patient History**.

* **Create > Vital Signs** để ghi lại các chỉ số sinh tồn của Bệnh nhân.

* Thêm dữ liệu thủ công vào Hồ sơ y tế của Bệnh nhân, ví dụ: một bản quét kết quả Xét nghiệm được thực hiện tại một Phòng thí nghiệm bên ngoài hoặc một ghi chú nhanh về tình trạng của Bệnh nhân, bằng cách sử dụng nút **Create > Medical Record**.

* Ghi lại chi tiết của một lần thăm khám bằng cách sử dụng nút **Create > Patient Encounter**.

Tài liệu Bệnh nhân giữ mã vạch của Bệnh nhân và có thể được sử dụng trong bất kỳ mẫu in mặc định nào hoặc bất kỳ [Mẫu in tùy chỉnh](/docs/v13/user/manual/en/customize-erpnext/print-format) nào mà bạn tạo để in thẻ nhận dạng bệnh nhân.

> Biểu mẫu này đã được Thay đổi trong Phiên bản 13

## 3. Các chủ đề liên quan
1. [Healthcare Settings](/docs/v13/user/manual/en/healthcare/healthcare_settings)

{next}