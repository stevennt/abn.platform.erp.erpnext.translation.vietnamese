# Hiệu lực phí

Nhiều cơ sở y tế không tính phí cho các lần tái khám trong một khoảng thời gian nhất định sau lần khám đầu tiên. Bạn có thể cấu hình số lượng lần tái khám miễn phí được cho phép cũng như khoảng thời gian cho các lần khám miễn phí trong Cài đặt y tế (Healthcare Settings). Việc này sẽ tạo ra một chứng từ Hiệu lực phí (Fee Validity).


## 1. Cách bật Tái khám miễn phí:


Để bật tính năng tái khám miễn phí, hãy đi đến:


> Trang chủ > Y tế > Cài đặt > Cài đặt y tế

- Tích chọn "Enable Free Follow Ups" (Bật tái khám miễn phí).
- Nhập "Number of Patient Encounters in Valid Days" (Số lần thăm khám của bệnh nhân trong số ngày hợp lệ).
- Nhập "Valid number of days" (Số ngày hợp lệ)


Ví dụ, như hiển thị dưới đây, một bệnh nhân có thể có 3 lần tái khám miễn phí trong vòng 30 ngày:


<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/fee_validity_settings.png">


Sau khi cấu hình xong, ngay khi bạn tạo một Lịch hẹn (Appointment) cho một bệnh nhân mới, một chứng từ Hiệu lực phí (Fee Validity) sẽ được tạo ra.


<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/fee_validity.png">


Chứng từ Hiệu lực phí này sẽ được cập nhật sau mỗi lần hẹn:


- **Status (Trạng thái)**: Trạng thái được đặt là _Pending_ (Chờ xử lý) cho đến khi hoàn thành số lượng lịch hẹn miễn phí và ngày hẹn nằm trong thời hạn "Valid Till" (Có hiệu lực đến). Khi tất cả các lịch hẹn miễn phí đã được tạo, trạng thái sẽ được cập nhật thành _Completed_ (Hoàn thành).
- **Max number of visits (Số lần thăm khám tối đa)**: Số lượng lần thăm khám miễn phí tối đa được cho phép.
- **Visited (Đã thăm khám)**: Số lượng lần thăm khám miễn phí đã hoàn thành.
- **Start Date (Ngày bắt đầu)**: Ngày của lần hẹn miễn phí đầu tiên.
- **Valid Till (Có hiệu lực đến)**: Ngày cuối cùng của Hiệu lực phí. Ngày này được tính bằng _Ngày bắt đầu + Số ngày hợp lệ_ (từ Cài đặt y tế).
- **Reference Appointments (Lịch hẹn tham chiếu)**: Liên kết đến tất cả các lịch hẹn nằm trong phạm vi của chứng từ Hiệu lực phí.


<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/fee_validity_completed.png">


> Biểu mẫu này đã được thay đổi trong Phiên bản 13

## 2. Các chủ đề liên quan


1. [Lịch hẹn bệnh nhân](/docs/v13/user/manual/en/healthcare/patient_appointment)
1. [Bệnh nhân](/docs/v13/user/manual/en/healthcare/patient)
1. [Cài đặt y tế](/docs/v13/user/manual/en/healthcare/healthcare_settings)


{next}