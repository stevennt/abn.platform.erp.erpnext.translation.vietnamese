<!-- add-breadcrumbs -->
# ADT Nội trú

Việc quản lý ADT (Nhập viện, Xuất viện, Chuyển viện) trong một Bệnh viện bận rộn là một chức năng khá phức tạp và ERPNext Healthcare giúp đơn giản hóa việc này rất nhiều. Trong ERPNext Healthcare, mọi việc nhập viện của bệnh nhân đều được quản lý bằng tài liệu [Hồ sơ nội trú](/docs/v16/user/manual/vi/healthcare/inpatient_record.html).

## Nhập viện
Một Bác sĩ có thể yêu cầu nhập viện cho bệnh nhân từ màn hình Patient Encounter bằng cách sử dụng lệnh `Order Admission`.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/ip_order_admission.png">

Là một phần của Lệnh Nhập viện (Admission Order), bác sĩ có thể cung cấp các chi tiết cần thiết về loại giường tại khoa mà Bệnh nhân cần được nhập viện, và bất kỳ hướng dẫn nhập viện nào khác cho nhân viên.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/ip_admission_order.png">

Khi thực hiện lệnh nhập viện cho bệnh nhân, ERPNext Healthcare sẽ tạo một Hồ sơ nội trú cho Bệnh nhân với tất cả các hướng dẫn do Bác sĩ cung cấp. Bất kỳ đơn thuốc, xét nghiệm hoặc lệnh thủ thuật nào được kê trong Encounter tương ứng sẽ được chuyển vào hồ sơ nội trú.

> Lưu ý: Quyền hạn ở cấp độ trường được áp dụng theo mặc định để thông tin Chẩn đoán, Hướng dẫn Nhập viện và các chi tiết khác chỉ hiển thị cho người dùng có vai trò Physician và Nursing User.

Nhân viên tiếp nhận nội trú có thể xem Hồ sơ nội trú với trạng thái _Admission Scheduled_ (Đã lên lịch nhập viện) và phân bổ Khoa cho Bệnh nhân tùy theo tình trạng sẵn có. Nút `Admit` trong Hồ sơ nội trú sẽ cho phép nhân viên tiếp nhận chọn giường tại khoa cho Bệnh nhân và tiến hành nhập viện.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/ip_admit_patient.png">

Sau khi một Đơn vị Dịch vụ (Service Unit) được chỉ định cho bệnh nhân, trạng thái của Hồ sơ nội trú sẽ được cập nhật thành _Admitted_ (Đã nhập viện).

## Xuất viện

Tương tự như Lên lịch Nhập viện, các Patient Encounter dành cho Bệnh nhân đã nhập viện sẽ có tùy chọn `Order Discharge` (Lệnh Xuất viện), kích hoạt trạng thái của Hồ sơ nội trú thành _Discharge Scheduled_ (Đã lên lịch xuất viện).

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/ip_order_discharge.png">

Bác sĩ có thể yêu cầu xuất viện cho bệnh nhân nội trú thông qua Patient Encounter hoặc Hồ sơ nội trú. Lệnh Xuất viện cho phép Bác sĩ chọn nội dung của `Discharge Notes` (Ghi chú xuất viện) (hoặc Tóm tắt xuất viện), nội dung này sẽ được cập nhật vào tài liệu Hồ sơ nội trú của bệnh nhân. Bác sĩ có thể chọn các xét nghiệm, thuốc và thủ thuật đã được bao gồm trong quá trình điều trị của Bệnh nhân tại cơ sở để in trong ghi chú xuất viện và có thể thêm các nhận xét của mình để in.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/ip_discharge_order.png">

Nhân viên tiếp nhận có thể in Ghi chú Xuất viện từ Hồ sơ nội trú và sử dụng nút `Discharge` để ghi nhận việc bệnh nhân rời viện và chuyển trạng thái sang _Discharged_ (Đã xuất viện).

> Lưu ý: ERPNext Healthcare xác nhận rằng tất cả các dịch vụ đã sử dụng trong thời gian lưu trú tại cơ sở đã được lập Hóa đơn để hoàn tất thành công tùy chọn `Discharge`. Tuy nhiên, lưu ý rằng việc xác nhận này _không_ xem xét trạng thái của Hóa đơn.

## Chuyển viện
Hồ sơ nội trú lưu giữ tất cả dữ liệu liên quan đến thời gian lưu trú của Bệnh nhân tại cơ sở, bao gồm tất cả các giường tại khoa (Service Unit) đã sử dụng.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/ip_transfer.png">

Bạn luôn có thể chuyển một bệnh nhân từ Đơn vị Dịch vụ này sang Đơn vị Dịch vụ khác bằng nút `Transfer`. Thao tác này sẽ cho phép bạn chọn Đơn vị Dịch vụ mà Bệnh nhân sẽ được chuyển đến.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/ip_transfer_patient.png">

{next}