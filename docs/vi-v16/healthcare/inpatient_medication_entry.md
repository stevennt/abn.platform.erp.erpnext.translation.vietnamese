<!-- add-breadcrumbs -->
# Nhập thuốc nội trú

**Nhập thuốc nội trú (Inpatient Medication Entry - IPME) được tạo để xử lý hàng loạt các Đơn thuốc nội trú dựa trên một số bộ lọc và có tùy chọn cập nhật tồn kho khi cấp phát thuốc.**

Để truy cập danh sách Nhập thuốc nội trú, hãy đi đến:

> Home > Healthcare > Inpatient > Inpatient Medication Entry

## 1. Điều kiện tiên quyết

Trước khi tạo Nhập thuốc nội trú, bạn cần tạo các bản ghi sau trước:

* [Bệnh nhân (Patient)](/docs/v16/user/manual/vi/healthcare/patient)
* [Hồ sơ nội trú (Inpatient Record)](/docs/v16/user/manual/vi/healthcare/inpatient_record)
* [Đơn thuốc nội trú (Inpatient Medication Order)](/docs/v16/user/manual/vi/healthcare/inpatient_medication_order)

## 2. Cách tạo Nhập thuốc nội trú

1. Đi đến danh sách Nhập thuốc nội trú và nhấn vào Mới (New).
2. Chọn Công ty (Company).
3. Thiết lập Ngày hạch toán (Posting Date).
4. Có nhiều bộ lọc khác nhau để lấy các Đơn thuốc nội trú đang chờ xử lý:

    - **Mã mặt hàng (Thuốc) (Item Code (Drug))**
    - **Phân công cho (Assigned To)**: Bạn có thể chọn người dùng được phân công hoàn thành Đơn thuốc nội trú.
    - **Bệnh nhân (Patient)**
    - **Chuyên gia y tế (Healthcare Practitioner)** người đã kê đơn thuốc.
    - **Đơn vị dịch vụ y tế (Healthcare Service Unit)** nơi bạn muốn cấp phát thuốc. Bạn có thể sử dụng các bộ lọc này bất cứ khi nào bạn cấp phát thuốc tại một đơn vị dịch vụ y tế cụ thể như Phòng cách ly, v.v.
    - **Bộ lọc Ngày và Giờ (Date and Time filters)**

    <img class="screenshot" alt="Inpatient Medication Entry filters" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/ime-filters.png">

5. Sau khi thiết lập các bộ lọc, nhấn vào nút **Lấy các đơn thuốc đang chờ (Get Pending Medication Orders)** để lấy các đơn hàng đang chờ xử lý khớp với các bộ lọc đã chọn.
6. Tùy chọn, đánh dấu hoặc bỏ đánh dấu *Cập nhật tồn kho (Update Stock)*. Nếu được đánh dấu, hãy chỉ định Kho (Warehouse) nơi thuốc sẽ được xuất.

    <img class="screenshot" alt="Update Stock" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/ime-stock.png">

### 2.2 Khi Xác nhận Nhập thuốc nội trú

Các Đơn thuốc nội trú tương ứng sẽ được đánh dấu là đã hoàn thành.

<img class="screenshot" alt="Completed Inpatient Medication Order Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/imoe-completed.png">

Nếu *Cập nhật tồn kho (Update Stock)* được đánh dấu, các kiểm tra tồn kho sẽ được thực hiện và các đơn hàng sẽ được xử lý để tạo Phiếu kho (Stock Entry) với các tham chiếu được cập nhật cho từng mục.
Bạn có thể kiểm tra các tham chiếu cho Nhập thuốc nội trú trong Phiếu kho, và trong bảng Chi tiết Phiếu kho (Stock Entry Detail) cho Bệnh nhân và Mục nhập tương ứng.

<img class="screenshot" alt="Stock Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/ime-stock-entry.png">

<img class="screenshot" alt="Stock Entry Detail" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/ime-stock-entry-detail.png">

### 2.3 Khi Hủy Nhập thuốc nội trú

Phiếu kho tương ứng sẽ bị hủy và Đơn thuốc nội trú liên kết sẽ được đánh dấu là chưa hoàn thành một lần nữa.

## 3. Các tính năng

### 3.1 Tạo Phiếu kho khi thiếu thuốc

Nếu *Cập nhật tồn kho (Update Stock)* được đánh dấu, và số lượng thuốc cần thiết không có sẵn để sử dụng trong kho đã chọn, khi xác nhận, bạn sẽ thấy một bản tóm tắt tất cả các loại thuốc và số lượng bị thiếu.

<img class="screenshot" alt="Drug Shortage Dialog" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/drug-shortage-dialog.gif">

Nút **Tạo Phiếu kho (Make Stock Entry)** sẽ hiển thị khi tài liệu ở trạng thái Nháp (Draft) và *Cập nhật tồn kho (Update Stock)* được đánh dấu. Khi nhấn nút này, hệ thống sẽ kiểm tra tình trạng thiếu thuốc và tạo một Phiếu kho mới để Điều chuyển vật tư bằng cách ánh xạ tất cả các loại thuốc và số lượng thiếu của từng loại. "Kho đến" (To Warehouse) cho Phiếu kho này sẽ là Kho thuốc mà bạn đã chọn trong Nhập thuốc nội trú. Sau đó, bạn có thể thiết lập "Kho nguồn" (Source Warehouse), Lưu và Xác nhận Phiếu kho để tiếp tục quá trình Nhập thuốc.

<img class="screenshot" alt="Make Stock Entry for Drug Shortage" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/healthcare/make-stock-entry.gif">

## 3. Các chủ đề liên quan

1. [Đơn thuốc nội trú (Inpatient Medication Order)](/docs/v16/user/manual/vi/healthcare/inpatient_medication_order)

{next}