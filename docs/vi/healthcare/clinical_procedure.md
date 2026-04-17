<!-- add-breadcrumbs -->

# Thủ thuật Lâm sàng

ERPNext giúp bạn tạo và thiết lập các Thủ thuật Lâm sàng cho bệnh nhân như Làm sạch vết thương hoặc Phẫu thuật đục thủy tinh thể. Hệ thống cho phép bạn cấu hình trước [Mẫu Thủ thuật Lâm sàng](/docs/v13/user/manual/en/healthcare/sample_collection), để bạn không phải thiết lập các thuộc tính mặc định như vật tư tiêu hao, đơn giá, mặt hàng mỗi khi thực hiện một Thủ thuật Lâm sàng.

## 1. Cách tạo một Thủ thuật Lâm sàng

Để tạo một Thủ thuật Lâm sàng, hãy đi tới:

> Home > Healthcare > Consultation > Clinical Procedure

### 1.1 Tạo Thủ thuật Lâm sàng thủ công

1. Chọn Naming Series cho thủ thuật.
2. Chọn Mẫu thủ thuật (Procedure Template). Kho, Khoa Y tế và Vật tư tiêu hao sẽ được tự động lấy dữ liệu.
3. Nếu bạn đã tạo một cuộc hẹn cho Thủ thuật Lâm sàng, bạn có thể chọn Cuộc hẹn (Appointment). Hệ thống sẽ tự động lấy Mẫu thủ thuật, Bệnh nhân, Ngày và Giờ bắt đầu, v.v.
4. Chọn Đơn vị dịch vụ nếu chưa được thiết lập và thủ thuật sẽ được thực hiện tại đơn vị đó.
5. Nhập hoặc chỉnh sửa chi tiết vật tư tiêu hao trong phần Vật tư tiêu hao (Consumables).
6. Nếu có một số Mẫu bệnh phẩm sẽ được thu thập trong hoặc sau khi thực hiện Thủ thuật Lâm sàng, hãy tạo tài liệu Thu thập mẫu (Sample Collection) và liên kết nó.
7. Lưu.
8. Xác nhận.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/clinical_procedure.png">

### 1.2 Tạo Thủ thuật Lâm sàng từ một Cuộc hẹn

Bạn có thể tra cứu và đặt [Cuộc hẹn Bệnh nhân](/docs/v13/user/manual/en/healthcare/patient_appointment) từ các thủ thuật đã được chỉ định cho bệnh nhân trong [Lần khám Bệnh nhân](/docs/v13/user/manual/en/healthcare/patient_encounter) trước đó bằng cách sử dụng nút **Get Prescribed Procedures** có sẵn trong Cuộc hẹn Bệnh nhân.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/prescribed_procedures.png">

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/prescribed_procedures_1.png">

Sau khi Cuộc hẹn được đặt, nhân viên y tế thực hiện có thể dễ dàng tạo một thủ thuật mới từ một cuộc hẹn đã đặt bằng cách sử dụng nút **Create > Clinical Procedure**.

## 2. Các tính năng

### 2.1 Các thao tác Thủ thuật

#### 2.1.1 Bắt đầu Thủ thuật

Nhân viên y tế có thể cập nhật trạng thái thủ thuật thành _In Progress_ (Đang tiến hành) bằng cách nhấp vào nút **Start**.

Nếu thủ thuật có vật tư tiêu hao, để thủ thuật có thể bắt đầu, phải có đủ số lượng tất cả các vật tư tiêu hao trong Kho của Đơn vị Dịch vụ Y tế. Nếu không đủ, hệ thống sẽ yêu cầu bạn xác nhận _Stock Transfer_ (Chuyển kho). Sau khi bạn xác nhận, một [Phiếu kho](/docs/v13/user/manual/en/stock/stock-entry) với Loại phiếu là "Material Transfer" sẽ được tạo và hiển thị. Hãy kiểm tra tài liệu Phiếu kho được tự động tạo, Lưu và Xác nhận. Sau đó bạn có thể bắt đầu Thủ thuật.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/procedure_consumption.png">

#### 2.1.2 Hoàn tất Thủ thuật

Khi thủ thuật hoàn tất, nhân viên y tế có thể cập nhật bảng _Consumables_ (Vật tư tiêu hao) với số lượng tồn kho thực tế đã sử dụng. Nút **Complete and Consume** sẽ ghi nhận việc tiêu hao bằng cách tạo một phiếu kho và cập nhật trạng thái của Thủ thuật Lâm sàng thành _Completed_ (Đã hoàn tất). Nếu Thủ thuật không có bất kỳ mặt hàng tồn kho nào trong bảng Vật tư tiêu hao, nút **Complete** sẽ được hiển thị.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v13/assets/img/healthcare/complete_and_consume.png">

### 2.2 Lập hóa đơn

Bạn có thể tạo Hóa đơn cho các thủ thuật được thực hiện cho bệnh nhân bằng cách đi tới:
> Home > Selling > Sales > Sales Invoice > Get Items From > Healthcare Services.

Bằng cách này, người dùng lập hóa đơn không cần truy cập vào các tài liệu trong mô-đun Healthcare và các dịch vụ chưa được lập hóa đơn cho Bệnh nhân sẽ được liệt kê để người dùng có thể lựa chọn.

Nếu tùy chọn _Invoice Consumables Separately_ (Lập hóa đơn vật tư tiêu hao riêng biệt) được bật, các chi phí cho các Mặt hàng vật tư tiêu hao sẽ được thêm vào Hóa đơn bán hàng một cách riêng biệt.

> Biểu mẫu này đã được thay đổi trong Phiên bản 13

## 3. Các chủ đề liên quan

1. [Mẫu Thủ thuật Lâm sàng](/docs/v13/user/manual/en/healthcare/clinical_procedure_template)
1. [Thu thập mẫu](/docs/v13/user/manual/en/healthcare/sample_collection)

{next}