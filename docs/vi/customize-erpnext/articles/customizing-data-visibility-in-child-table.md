<!-- add-breadcrumbs -->
# Tùy chỉnh hiển thị dữ liệu trong Bảng con (Child Table)

Trong ERPNext, có một tính năng gọi là lưới có thể chỉnh sửa (editable grid). Tính năng này cho phép người dùng thêm các giá trị vào bảng con mà không cần mở hộp thoại/biểu mẫu cho từng dòng.

Đây là cách bảng Quotation Item hiển thị giá trị khi chế độ Editable Grid được bật. Bảng sẽ có tối đa bốn cột.

<img alt="Child Table" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-child-table-5.png">

Theo cài đặt mặc định, chỉ có bốn cột được liệt kê trong bảng con. Dưới đây là cách bạn có thể thêm nhiều cột hơn ngay trong chính Editable Grid.

Để một trường được thêm làm cột trong bảng, hãy nhập giá trị vào trường Column. Đồng thời, hãy đảm bảo rằng thuộc tính "Is List View" của trường đó đã được tích chọn.

<img alt="Child Table" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-child-table-2.png">

Dựa trên giá trị trong trường Column, các cột sẽ được thêm vào bảng con. Hãy đảm bảo rằng tổng giá trị được thêm vào trường Column không vượt quá 10. Dựa trên giá trị Column, độ rộng của cột đó sẽ được thiết lập.

<img alt="Child Table" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-child-table-3.png">

**Chuyển sang Lưới không thể chỉnh sửa (Un-editable Grid)**

Để hiển thị nhiều giá trị hơn trong phần xem trước của bảng Quotation Item, bạn có thể tắt chế độ Editable Grid cho DocType Quotation Item. Các bước thực hiện như sau.

<img alt="Child Table" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-child-table.gif">

Khi chế độ Editable Grid bị tắt đối với Quotation Item, các giá trị sẽ được hiển thị trong phần xem trước của bảng Quotation Item theo cách sau:

<img alt="Child Table" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-child-table-4.png">

Để hiển thị giá trị của một trường cụ thể trong phần xem trước, hãy đảm bảo rằng trong công cụ Customize Form, thuộc tính "In List View" của trường đó đã được tích chọn.

<img alt="Child Table" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-child-table-1.png">

{next}