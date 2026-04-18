# Nhật ký xe

**Nhật ký xe được sử dụng để nhập chỉ số đồng hồ đo quãng đường, Chi phí nhiên liệu và chi tiết Chi phí bảo dưỡng.**

Để truy cập Nhật ký xe, hãy đi đến:

> Human Resources > Fleet Management > Vehicle Log


## 1. Điều kiện tiên quyết

Trước khi tạo Nhật ký xe, bạn cần phải tạo các tài liệu sau:

* [Vehicle](/docs/v16/user/manual/vi/human-resources/vehicle)


## 2. Cách tạo Nhật ký xe

1. Đi đến danh sách Nhật ký xe, nhấn vào Mới.
1. Chọn Biển số xe (License Plate) và Nhân viên (Employee).
1. Nhập thông tin Chỉ số đồng hồ đo quãng đường như Ngày và Chỉ số đồng hồ (Odometer).
1. Nhập Chi tiết đổ nhiên liệu [tùy chọn] như Số lượng nhiên liệu, Giá nhiên liệu, Nhà cung cấp và Tham chiếu hóa đơn.

    <img class="screenshot" alt="Vehicle Log" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/vehicle-log1.png">


1. Ngoài ra, Chi tiết bảo dưỡng xe cũng có thể được thêm vào như hình dưới đây (tùy chọn).

    <img class="screenshot" alt="Vehicle Log" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/vehicle-log2.png">

1. Lưu. Sau khi thông tin được lưu, các giá trị Model và Make sẽ được tự động lấy về.




## 3. Các tính năng

Quản lý đội xe trong ERPNext cho phép bạn tự động tạo [Expense Claim](/docs/v16/user/manual/vi/human-resources/expense-claim) cho các Chi phí xe của mình.

### 3.1 Tạo Expense Claim cho Chi phí xe

Nhấn vào nút Make Expense Claim. Nút này chỉ xuất hiện trong trường hợp Nhật ký xe đã được Xác nhận.

<img class="screenshot" alt="Expense Claim Button" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/vehicle-log-expense-claim-button.png">

Khi bạn nhấn vào 'Make Expense Claim',

  1. Ngày, Nhân viên, Tổng chi phí sẽ được chuyển sang Expense Claim được tạo.
  2. Tổng chi phí nhiên liệu và chi phí bảo dưỡng được tính toán và chuyển sang Số tiền Expense Claim.
  3. Nhân viên có thể Xác nhận Expense Claim để xử lý tiếp theo.

	<img class="screenshot" alt="Vehicle Log" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/vehicle-log-expense-claim.png">

## 4. Các chủ đề liên quan

1. [Expense Claim](/docs/v16/user/manual/vi/human-resources/expense-claim)