<!-- add-breadcrumbs -->
# Cho phép thay đổi các trường sau khi Xác nhận

Khi một tài liệu đã được **Xác nhận**, các trường sẽ bị đóng băng và không được phép chỉnh sửa. Tuy nhiên, có một số trường tiêu chuẩn nhất định như Letter Head (Tiêu đề thư), Print Heading (Tiêu đề in) vẫn có thể chỉnh sửa được. Nếu thuộc tính **Allow on Submit** (Cho phép khi Xác nhận) được tích chọn, trường đó sẽ có thể chỉnh sửa được ngay cả sau khi tài liệu đã được **Xác nhận**.

Dưới đây là một ví dụ. Trong DocType 'Hóa đơn bán hàng' (Sales Invoice), trường 'Letter Head' có thể được chỉnh sửa ngay cả sau khi đã **Xác nhận** hóa đơn bán hàng.

![Allow on Submit](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/allow-on-submit-on-standard-field.gif)

> **Lưu ý:** Bạn không thể bật 'Allow on Submit' cho các trường tiêu chuẩn. Một số trường tiêu chuẩn nhất định đã được bật sẵn thuộc tính này theo mặc định. Tuy nhiên, bạn có thể bật thuộc tính này cho các trường tùy chỉnh mà bạn tạo ra.

Để thiết lập thuộc tính này cho một trường tùy chỉnh,

1. Đi đến **Customize Form**.
2. Chọn Form mà bạn muốn thiết lập thuộc tính này.
3. Chọn trường tùy chỉnh.
4. Tích vào ô **'Allow on Submit'**.
5. Nhấn **Update**.

![Allow on Submit on Custom Field](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/allow-on-submit-on-custom-field.gif)

Sau khi cập nhật **Customize Form**, bạn nên tải lại tài khoản ERPNext của mình. Sau đó kiểm tra lại form và trường để xác nhận xem chúng có thể chỉnh sửa được trong trạng thái đã **Xác nhận** hay không.

{next}