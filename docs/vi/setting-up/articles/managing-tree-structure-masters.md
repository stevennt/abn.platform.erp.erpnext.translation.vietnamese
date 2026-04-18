<!-- add-breadcrumbs -->
#Quản lý các Danh mục theo cấu trúc cây

Một số danh mục trong ERPNext được duy trì theo cấu trúc cây. Các danh mục có cấu trúc cây cho phép bạn thiết lập Danh mục Cha và các Danh mục Con dưới các Danh mục Cha đó. Việc thiết lập cấu trúc này cho phép bạn tạo các báo cáo thông minh và theo dõi sự tăng trưởng ở mỗi cấp trong hệ thống phân cấp.

Dưới đây là danh sách một phần các danh mục được duy trì theo cấu trúc cây.

* Hệ thống tài khoản

* Hệ thống tài khoản Trung tâm chi phí

* Nhóm khách hàng

* Khu vực

* Nhân viên bán hàng

* Nhóm mặt hàng

Sau đây là các bước để quản lý và tạo bản ghi trong danh mục có cấu trúc cây. Hãy xem xét danh mục Khu vực để hiểu cách quản lý các danh mục cây.

####Bước 1: Đi đến Danh mục

`Bán hàng > Thiết lập > Khu vực`

####Bước 2: Khu vực Cha

<img alt="Default Territories" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/territory-2.png">

Khi nhấp vào Khu vực Cha, bạn sẽ thấy tùy chọn để thêm khu vực con bên dưới nó. Tất cả các Nhóm Khu vực mặc định sẽ được liệt kê dưới Nhóm Cha có tên là "Tất cả khu vực". Bạn có thể thêm thêm các Nhóm Khu vực Cha hoặc con bên dưới nó.

####Bước 3: Thêm khu vực mới

Khi nhấp vào Thêm con, một hộp thoại sẽ hiển thị hai trường.

**Tên nhóm khu vực**

Khu vực sẽ được Lưu với Tên khu vực được cung cấp tại đây.

**Nút nhóm**

Nếu Nút nhóm được chọn là Có, thì Khu vực này sẽ được tạo dưới dạng Cha, nghĩa là bạn có thể tạo thêm các khu vực con bên dưới nó. Nếu chọn Không, thì nó sẽ trở thành Khu vực con mà bạn có thể chọn trong các danh mục khác.

<div class="well">Chỉ các Nhóm Khu vực con mới có thể được chọn trong các danh mục và giao dịch khác.</div>

<img alt="Default Territories" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/territory-1.gif">

Sau đây là cách các Khu vực con sẽ được liệt kê dưới một Khu vực Cha.

<img alt="Adding new Territories" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/territory-3.png">

Thực hiện theo các bước này, bạn cũng có thể quản lý các danh mục cây khác trong ERPNext.

<!-- markdown -->