<!-- add-breadcrumbs -->
# Bộ lọc tìm kiếm

**Bộ lọc tìm kiếm là một tùy chọn cho phép bạn lọc các bản ghi dựa trên một giá trị cụ thể của một trường nhất định trong một Tài liệu.**

Bộ lọc tìm kiếm có sẵn trong Chế độ xem Danh sách (List View) và Trình tạo Báo cáo (Report Builder) của một DocType.

Mỗi tùy chọn bộ lọc có ba trường.

#### Trường (Field)

Chọn trường của tài liệu mà dựa vào đó bạn muốn lọc các bản ghi. Tất cả các trường trong một biểu mẫu sẽ có thể chọn được trong danh sách này.

![Search Filter](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-search-filer-1.png)

#### Dựa trên (Based On)

Đối với trường đã chọn, bạn sẽ cần nhập một giá trị của trường đó. Trong phần 'Dựa trên', bạn có thể xác định các tiêu chí mà dựa vào đó hệ thống sẽ tìm kiếm tài liệu.

![Search Filter](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-search-filter-2.png)

Các điều kiện khác nhau mà bộ lọc dựa vào là:

* '=' : Bằng
* '!=' : Khác
* '>' : Lớn hơn
* '<' : Nhỏ hơn
* '>=' : Lớn hơn hoặc bằng
* '<=' : Nhỏ hơn hoặc bằng
* 'Like' : Chứa (tìm kiếm tương đối)
* 'In' : Nằm trong danh sách

#### Giá trị (Value)

Tại đây, bạn sẽ cần nhập giá trị mà bạn đang dùng để chạy tìm kiếm tài liệu.

![Search Filter](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-search-filter-3.png)

Vì vậy, nhìn chung, một thuật toán hoặc một phương trình để tìm kiếm các tài liệu sẽ được tạo ra, cho phép bạn truy xuất được tập hợp các tài liệu mong muốn.

![Search Filter](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-search-filter.gif)

Bạn cũng có thể áp dụng nhiều bộ lọc cùng một lúc. Để xóa một bộ lọc cụ thể, chỉ cần nhấp vào dấu 'x' trên bộ lọc đó.

## Bộ lọc mặc định

Có một số bộ lọc được tích hợp sẵn cho các chế độ xem có thể được sử dụng để lọc kết quả tìm kiếm. Các bộ lọc mặc định cho bất kỳ DocType nào có thể được thiết lập từ tùy chọn [Tùy chỉnh biểu mẫu](/docs/v16/user/manual/vi/customize-erpnext/custom-field).

![Search Filter](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-search-filter-4.png)

## Xem thêm

1. [Lọc theo](/docs/v16/user/manual/vi/using-erpnext/filter-by)
1. [Lưu bộ lọc](/docs/v16/user/manual/vi/using-erpnext/save-filter)

<!-- markdown -->