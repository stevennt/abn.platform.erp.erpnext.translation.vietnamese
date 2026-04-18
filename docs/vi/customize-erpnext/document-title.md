<!-- add-breadcrumbs -->
# Tiêu đề tài liệu

**Bạn có thể tùy chỉnh tiêu đề của các tài liệu dựa trên các thuộc tính để có thông tin có ý nghĩa cho các chế độ xem danh sách.**

Ví dụ, tiêu đề mặc định của một Báo giá là tên khách hàng, nhưng nếu bạn chỉ làm việc với một vài khách hàng và gửi rất nhiều báo giá cho mỗi khách hàng, bạn có thể muốn tùy chỉnh lại.

![Document Title](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/document-title.png)

## Thiết lập các trường Tiêu đề

Từ phiên bản ERPNext 6.0 trở đi, tất cả các giao dịch đều có thuộc tính 'Title' (Tiêu đề). Nếu không có thuộc tính tiêu đề, bạn có thể thêm một **Custom Field** (Trường tùy chỉnh) làm tiêu đề và thiết lập **Title Field** thông qua **Customize Form**.

Bạn có thể thiết lập giá trị mặc định của thuộc tính đó bằng cách sử dụng định dạng chuỗi kiểu Python trong phần **Default** hoặc **Options**.

1. Để chỉnh sửa tiêu đề mặc định, hãy đi tới Customize Form
2. Chọn Form mà bạn muốn thay đổi Title Field.
3. Chỉnh sửa **Title Field** trong form.

## Định nghĩa Tiêu đề

Bạn có thể định nghĩa tiêu đề bằng cách thiết lập các thuộc tính tài liệu trong dấu ngoặc nhọn `{}`. Ví dụ, nếu tài liệu của bạn có trường `customer_name`, bạn có thể chỉ định trường đó làm Tiêu đề của Form.

![Set Document Title](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/set-document-title.gif)

Ngoài ra, bạn cũng có thể định nghĩa một trường cụ thể làm 'Title Field' trong Customize Form.

![Title Field](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/title-field-in-view-settings.png)    

## Tiêu đề Cố định hoặc Có thể chỉnh sửa

Nếu tiêu đề của bạn được tạo dưới dạng tiêu đề mặc định, người dùng có thể chỉnh sửa bằng cách nhấp vào tiêu đề của tài liệu.

<img class="screenshot" alt = "Editable Title"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-document title.gif">

Nếu bạn muốn một tiêu đề cố định, bạn có thể thiết lập quy tắc trong thuộc tính **Options**. Bằng cách này, tiêu đề sẽ được tự động cập nhật mỗi khi tài liệu được cập nhật.

{next}