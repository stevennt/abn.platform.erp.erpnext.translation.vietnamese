<!-- add-breadcrumbs -->
# Thiết lập Phòng khám / Cơ sở hành nghề

Bạn có thể dễ dàng cấu hình các danh mục chính để thiết lập ERPNext Healthcare cho cơ sở hành nghề của mình. Dưới đây là danh sách các tài liệu giúp bạn đẩy nhanh quá trình nhập liệu. Ngoài ra, hãy đọc thêm [Cài đặt Y tế](../docs/v16/user/manual/en/healthcare/healthcare_settings) để thiết lập mô-đun Healthcare.

## Khoa Y tế (Medical Department)
Để tổ chức phòng khám của bạn thành các khoa, bạn có thể tạo nhiều Khoa Y tế khác nhau.

`Healthcare > Setup > Medical Department > New Medical Department`

## Loại cuộc hẹn (Appointment Type)
Bạn có thể tạo các danh mục chính cho nhiều loại Cuộc hẹn khác nhau. Loại cuộc hẹn cho phép bạn xác định trước thời lượng của cuộc hẹn, nhờ đó khi chọn Loại cuộc hẹn, thời lượng sẽ tự động được thiết lập trong Cuộc hẹn. Điều này cho phép bạn ghi đè thời lượng cuộc hẹn đã được thiết lập bởi Lịch trình của Người hành nghề và các khung giờ sẽ tự động điều chỉnh sang khung giờ trống tiếp theo.

>Lưu ý: Để tắt tính năng này, bạn có thể bật tùy chọn `Always Use Slot Duration as Appointment Duration` trong danh mục Người hành nghề. Tùy chọn này sẽ luôn thiết lập thời lượng khung giờ đã được cấu hình trong Lịch trình của Người hành nghề làm thời lượng của Cuộc hẹn.

Bạn cũng có thể thiết lập màu sắc cho mỗi Loại cuộc hẹn, điều này sẽ giúp bạn nhận diện các cuộc hẹn thuộc một loại cụ thể trong chế độ xem Lịch.

`Healthcare > Setup > Appointment Type > New Appointment Type`

## Loại Đơn vị Dịch vụ Y tế (Healthcare Service Unit Type)
Khi thiết lập lịch trình cho Người hành nghề Y tế, bạn có thể tùy chọn chọn một [Đơn vị Dịch vụ Y tế](../docs/v16/user/manual/en/healthcare/healthcare_service_unit) nơi Người hành nghề sẽ thực hiện các cuộc thăm khám. Bạn nên tích chọn tùy chọn `Allow Appointments` cho Đơn vị Dịch vụ Y tế để có thể đặt lịch hẹn. Bạn cũng có thể xác định các thuộc tính của đơn vị dịch vụ trong `Healthcare Service Unit Type`, hãy đọc thêm về [Thiết lập Cơ sở Nội trú](../docs/v16/user/manual/en/healthcare/setup_inpatient) để biết thêm chi tiết.

## Các danh mục chính để dễ dàng nhập liệu
ERPNext Healthcare cho phép bạn cấu hình một số danh mục chính thường xuyên được sử dụng để việc nhập liệu trở nên dễ dàng hơn.

#### Dạng liều dùng (Dosage Forms)
Dạng liều dùng giúp bạn cấu hình hình thức đóng gói của thuốc, ví dụ: Viên nang, Siro, v.v.

`Healthcare > Setup > Complaints > New Dosage Form`

#### Đường dùng thuốc (Route of Administration)
Đường dùng thuốc tương ứng với con đường mà thuốc được đưa vào cơ thể Bệnh nhân. Ví dụ: Đường uống, Đường tĩnh mạch, v.v.

`Healthcare > Setup > Complaints > New Route of Administration`

#### Liều lượng & Thời gian dùng thuốc (Prescription Dosage & Duration)
Bạn có thể cấu hình các liều lượng khác nhau để sử dụng khi kê đơn thuốc cho bệnh nhân. Bạn có thể đặt tên Liều lượng kê đơn theo bất kỳ cách nào bạn muốn (ví dụ: BID hoặc I-0-I), sau đó thiết lập hàm lượng thuốc và thời điểm cần dùng thuốc.

`Healthcare > Setup > Prescription Dosage > New Prescription Dosage`

`Healthcare > Setup > Prescription Duration > New Prescription Duration`

#### Than phiền và Chẩn đoán (Complaint and Diagnosis)
Để dễ dàng nhập liệu khi ghi lại kết quả thăm khám, ERPNext Healthcare cho phép bạn lưu mọi dữ liệu Than phiền / Chẩn đoán mà bạn nhập ngay từ màn hình Thăm khám Bệnh nhân. Bằng cách này, cơ sở dữ liệu sẽ liên tục xây dựng một danh sách tất cả các than phiền và chẩn đoán mà bạn đã nhập. Sau này, mỗi khi bạn bắt đầu nhập liệu, bạn sẽ có thể chọn từ / câu đã nhập trước đó từ trường tìm kiếm. Bạn cũng có thể cấu hình các danh mục này một cách thủ công bằng cách vào:

`Healthcare > Setup > Complaints > New Complaint`

`Healthcare > Setup > Diagnosis > New Diagnosis`

# Mẫu Quy trình Lâm sàng (Clinical Procedures Templates)
ERPNext Healthcare cho phép bạn cấu hình các mẫu với các thuộc tính khác nhau của Quy trình Lâm sàng để đơn giản hóa quá trình tạo Quy trình. Bạn có thể tạo Mẫu Quy trình Lâm sàng mới bằng cách vào:

`Healthcare > Setup > Clinical Procedure Template`

Các mẫu cho phép bạn quản lý Mặt hàng có thể tính phí, đơn giá, v.v. cho một quy trình cụ thể. Phần `Consumables` (Vật tư tiêu hao) cho phép bạn thiết lập các Mặt hàng vật tư tiêu hao, số lượng mặc định, v.v. để các mặt hàng này được tải sẵn trong các Quy trình Lâm sàng được tạo dựa trên mẫu. Điều này cho phép người thực hiện quy trình có thể dễ dàng nhập số lượng đã sử dụng hoặc thêm các mặt hàng bổ sung thực tế đã được tiêu dùng như một phần của quy trình.

Nếu tùy chọn `Invoice Consumables Separately` (Lập hóa đơn vật tư tiêu hao riêng) được bật, các chi phí cho các Mặt hàng vật tư tiêu hao sẽ được thêm vào Hóa đơn bán hàng một cách riêng biệt bên cạnh `Billing Rate` (Giá dịch vụ) của quy trình.

Lưu ý rằng bạn cũng có thể bật `Sample Collection` (Lấy mẫu) cho một Quy trình Lâm sàng nếu phù hợp. Ngoài ra, bạn cũng có thể thêm nhiều giai đoạn vào Mẫu để Quy trình Lâm sàng có thể được theo dõi qua các giai đoạn khác nhau như đã cấu hình trong mẫu.

{next}