<!-- add-breadcrumbs -->
# Cài đặt Y tế

Hầu hết các cài đặt chung cho phân hệ Y tế có thể được thực hiện thông qua trang Cài đặt Y tế.

Để xem và thay đổi các cài đặt, hãy đi tới:

> Trang chủ > Y tế > Cài đặt > Cài đặt Y tế

> Lưu ý: Đảm bảo rằng bạn đã được cấp vai trò "Healthcare Administrator" để có thể truy cập trang này.

## 1. Cài đặt Ngoại trú

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/healthcare_settings_1.png">

* **Patient Name By**: Theo mặc định, chứng từ Bệnh nhân sử dụng chuỗi đặt tên (naming series) để đặt tên, nhưng bạn cũng có thể chọn thay đổi thành "Patient Name" (Tên bệnh nhân) nếu cần.

* **Link Customer to Patient**: Tùy chọn này sẽ cho phép hệ thống tạo và liên kết một Khách hàng bất cứ khi nào một Bệnh nhân mới được tạo. Khách hàng này sẽ được sử dụng khi đặt tất cả các giao dịch. Hóa đơn Bệnh nhân sẽ được tạo dựa trên Khách hàng này. Bạn cũng có thể chọn một Khách hàng hiện có khi tạo Bệnh nhân.

* **Default Medical Code Standard**: ERPNext Healthcare cho phép bạn sử dụng nhiều Tiêu chuẩn Mã Y tế khác nhau. Tại đây, bạn cũng có thể chọn Tiêu chuẩn Mã Y tế mặc định.

* **Collect Fee for Patient Registration**: Nếu bạn bật tùy chọn này, tất cả Bệnh nhân mới mà bạn tạo sẽ bị *Vô hiệu hóa* theo mặc định và sẽ chỉ được kích hoạt sau khi Xuất hóa đơn Phí đăng ký. Để tạo Hóa đơn và ghi nhận Bút toán thanh toán, bạn có thể sử dụng nút **Invoice Patient Registration** trong chứng từ Bệnh nhân. Ngoài ra, lưu ý rằng tất cả các chứng từ ERPNext Healthcare sẽ lọc bỏ các hồ sơ Bệnh nhân đang bị vô hiệu hóa.

* **Registration Fee**: Bạn có thể thiết lập Phí đăng ký cần thu tại đây nếu bạn đã chọn "Collect Fee for Patient Registration".

* **Automate Appointment Invoicing**: Nếu bạn muốn tự động tạo Hóa đơn bán hàng (bao gồm phí khám của Người hành nghề đã chọn), bạn có thể bật tùy chọn này. Tính năng này đặc biệt hữu ích nếu cơ sở của bạn thu tiền ngay khi đặt lịch hẹn. Biểu mẫu Lịch hẹn Bệnh nhân sẽ cho phép bạn chọn Phương thức thanh toán và Số tiền đã nhận. Ngoài ra, các hóa đơn sẽ tự động bị Hủy khi Lịch hẹn bị hủy.

* **Enable Free Follow-ups**: Nhiều cơ sở y tế không thu phí cho các lần khám tái khám trong một khoảng thời gian nhất định sau lần khám đầu tiên (Đăng ký Bệnh nhân). Hãy tích vào ô này nếu bạn muốn cho phép tái khám miễn phí. Sau khi chọn, hãy cấu hình số lượng lần tái khám miễn phí được cho phép (_Patient Encounters in Valid Days_) cũng như khoảng thời gian (_Valid number of days_) cho các lần khám miễn phí tại đây.

## 2. Cài đặt Nội trú

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/inpatient-settings.png">

* **Allow Discharge Despite Unbilled Healthcare Services**: Một số cơ sở y tế cho bệnh nhân xuất viện để giải phóng phòng cho các ca nhập viện mới và sau đó mới lập hóa đơn sau. Nếu tùy chọn này được chọn, khi cho bệnh nhân xuất viện, hệ thống sẽ không kiểm tra các dịch vụ chưa được lập hóa đơn của bệnh nhân đó.

* **Do Not Bill Patient Encounters for Inpatients**: Một số cơ sở y tế không lập hóa đơn riêng cho các lần khám của Bệnh nhân nội trú. Nếu tùy chọn này được chọn, khi sử dụng chức năng **Get Items From > Healthcare Services** trong Hóa đơn bán hàng, hệ thống sẽ không lấy các lần khám bệnh có liên kết với Hồ sơ nội trú.

## 3. Mặt hàng Dịch vụ Y tế Mặc định

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/healthcare_settings_2.png">

ERPNext Healthcare sử dụng phân hệ Kế toán để lập hóa đơn cho Bệnh nhân. Bạn có thể cấu hình các "Mặt hàng" mặc định để tính phí khám bệnh, phí tiêu hao vật tư thủ thuật, v.v. tại đây. Hãy đảm bảo rằng "Inpatient Visit Charge Item" và "Out-Patient Consulting Charge Item" là các mặt hàng dịch vụ, tức là chúng phải được bỏ chọn ô *Maintain Stock* (Duy trì tồn kho).

## 4. Tài khoản Mặc định

Nếu bạn muốn ghi đè các cài đặt tài khoản mặc định và cấu hình các tài khoản Thu nhập và Phải thu cho Y tế, bạn có thể thực hiện tại đây.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/healthcare_settings_3.png">

* **Income Account**: Tài khoản Thu nhập mặc định sẽ được sử dụng nếu không được thiết lập trong Người hành nghề Y tế để ghi nhận phí đặt lịch hẹn.

* **Receivable Account**: Tài khoản Phải thu mặc định sẽ được sử dụng để ghi nhận phí đặt lịch hẹn.

## 5. Thông báo SMS Ngoại trú

Bạn có thể bật tính năng gửi thông báo SMS khi Đặt lịch hẹn Bệnh nhân, Đăng ký Bệnh nhân, v.v., và cũng có thể cấu hình nội dung tin nhắn trong phần này.

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/healthcare_settings_4.png">

* **Patient Registration**: Tin nhắn này sẽ được gửi khi một Bệnh nhân mới được tạo trong hệ thống của bạn.

* **Appointment Confirmation**: Tin nhắn này sẽ được gửi khi một Lịch hẹn được đặt cho Bệnh nhân.

* **Avoid Confirmation**: Tích vào ô này nếu bạn không muốn gửi tin nhắn Đặt lịch hẹn khi Lịch hẹn được đặt ngay trong cùng ngày.

* **Appointment Reminder**: Tin nhắn này sẽ được gửi vào ngày hẹn như một lời nhắc.

* **Remind Before**: Bạn có thể cấu hình khoảng thời gian trước khi tất cả các tin nhắn nhắc nhở được gửi đi.

## 6. Cài đặt Phòng xét nghiệm

<img class="screenshot" alt="ERPNext Healthcare" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/healthcare_settings_5.png">

* **Create Lab Test(s) on Sales Invoice Submit**: Nếu cơ sở của bạn lập Hóa đơn và thu tiền từ Bệnh nhân trước khi thực hiện Xét nghiệm, bạn có thể bật tùy chọn này để tự động tạo các Xét nghiệm cho tất cả các Xét nghiệm đã được lập hóa đơn. Nếu bạn đã bật "Create Sample Collection document for Lab Test" và Xét nghiệm đó có cấu hình _Mẫu thử (Sample)_ trong Mẫu xét nghiệm (Lab Test Template), một chứng từ Thu thập mẫu sẽ cũng được tạo ra.

* **Create Sample Collection document for Lab Test**: Nếu tùy chọn này được bật, mỗi khi bạn tạo một Xét nghiệm, một chứng từ Thu thập mẫu sẽ được tạo.

* **Employee Name and Designation in