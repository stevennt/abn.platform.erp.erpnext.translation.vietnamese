<!-- add-breadcrumbs -->

# Mẫu Thủ thuật Lâm sàng

ERPNext Healthcare cho phép bạn cấu hình các mẫu với nhiều thuộc tính khác nhau của Thủ thuật Lâm sàng để đơn giản hóa quá trình tạo Thủ thuật. Bạn có thể tạo các mẫu để không phải nhập các vật tư tiêu hao, đơn giá và các mặt hàng liên kết mỗi khi bạn tạo một [Thủ thuật Lâm sàng](../healthcare/clinical_procedure) cho Bệnh nhân.

## 1. Cách tạo Mẫu Thủ thuật Lâm sàng

Bạn có thể tạo các Mẫu Thủ thuật Lâm sàng mới bằng cách đi tới:

> Home > Healthcare > Consultation Setup > Clinical Procedure Template

1. Nhập một tên duy nhất cho Mẫu.
2. Mẫu Thủ thuật Lâm sàng sẽ tự động tạo một Mặt hàng liên kết với nó để phục vụ mục đích lập hóa đơn. Vì lý do này, hãy nhập Mã mặt hàng, Nhóm mặt hàng và Mô tả cho mặt hàng đó.
3. Tùy chọn chọn Khoa Y tế nơi các Thủ thuật Lâm sàng sẽ được thực hiện.
4. Tích chọn "Is Billable" nếu bạn muốn lập hóa đơn cho thủ thuật như Phẫu thuật đầu gối. Nếu bạn tích chọn mục này, hãy thiết lập đơn giá cho Thủ thuật. Bạn có thể không muốn lập hóa đơn cho các thủ thuật như Vệ sinh vết thương.
5. Lưu.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/clinical_procedure_template.png">

## 2. Các tính năng

### 2.1 Tự động tạo Mặt hàng cho các Mẫu

Các mẫu cho phép bạn quản lý Mặt hàng có thể lập hóa đơn, đơn giá, v.v. cho một thủ thuật cụ thể. Hệ thống sẽ tự động tạo một Mặt hàng liên kết với mẫu khi nó được Lưu.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/clinical_procedure_item.png">

Bạn có thể thay đổi Mã mặt hàng liên kết với Thủ thuật nếu cần bằng cách sử dụng nút **Change Item Code**.

### 2.2 Quản lý Vật tư tiêu hao của Thủ thuật

Phần Vật tư tiêu hao cho phép bạn thiết lập các Mặt hàng tồn kho tiêu hao với số lượng mặc định, v.v. sẽ cần thiết trong quá trình thực hiện Thủ thuật để các mặt hàng này được tải sẵn trong các Thủ thuật Lâm sàng được tạo dựa trên mẫu. Điều này cho phép bác sĩ thực hiện dễ dàng nhập số lượng đã sử dụng hoặc thêm các mặt hàng bổ sung đã được sử dụng trong quá trình thực hiện thủ thuật thực tế.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/procedure_consumables.png">

### 2.3 Lập hóa đơn Vật tư tiêu hao riêng biệt

Nếu tùy chọn "Invoice Consumables Separately" được tích chọn, các khoản phí cho các Mặt hàng tiêu hao sẽ được thêm vào Hóa đơn bán hàng một cách riêng biệt bên cạnh "Billing Rate" của thủ thuật.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/invoice_separately.png">

### 2.4 Cấu hình Thu thập mẫu

Lưu ý rằng bạn cũng có thể bật "Sample Collection" cho một Thủ thuật Lâm sàng nếu phù hợp.

<img class="screenshot" alt="ERPNext Healthcare" src="https://docs.erpnext.com/docs/v16/assets/img/healthcare/sample_collection.png">

## 3. Các chủ đề liên quan

1. [Thủ thuật Lâm sàng](../healthcare/clinical_procedure)
1. [Thu thập mẫu](../healthcare/sample_collection)

{next}