<!-- add-breadcrumbs -->
# Phân quyền Vai trò cho Trang và Báo cáo

**Quyền truy cập vào các trang và báo cáo khác nhau có thể được kiểm soát trong Phân quyền Vai trò cho Trang và Báo cáo.**

Các loại tài liệu là Đơn bán hàng, Khách hàng, Nhà cung cấp, v.v. Chúng là một **DocType**, nghĩa là chúng có thể chứa nhiều tài liệu thuộc loại đó. Một Trang là một trang đơn lẻ như [Cài đặt Bán hàng](/docs/v13/user/manual/en/selling/selling-settings). Bạn không thể tạo nhiều Cài đặt Bán hàng, nhưng bạn có thể tạo nhiều Đơn bán hàng.

Trong ERPNext, người dùng có thể tạo giao diện người dùng tùy chỉnh bằng Trang và báo cáo tùy chỉnh bằng [Report Builder](/docs/v13/user/videos/learn/report-builder.html) hoặc [Query Report](https://frappe.io/docs/v13/user/en/guides/reports-and-printing/how-to-make-query-report). ERPNext có [hệ thống phân quyền dựa trên vai trò](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions) nơi bạn có thể gán các vai trò cho người dùng. Cùng một vai trò đó có thể được gán cho trang và báo cáo để truy cập chúng.

Nếu người dùng đã bật chế độ nhà phát triển (developer mode), họ có thể thêm các vai trò trực tiếp trong bản ghi trang và báo cáo. Trong trường hợp đó, các quyền cũng sẽ được phản ánh trong tệp JSON của trang/báo cáo. Giả sử bạn muốn hạn chế các vai trò có thể truy cập vào một số trang và báo cáo nhất định trong ERPNext, việc này có thể được thực hiện thông qua Phân quyền Vai trò cho Trang và Báo cáo.

Để truy cập Phân quyền Vai trò cho Trang và Báo cáo, hãy đi đến:
> Trang chủ > Người dùng và Phân quyền > Phân quyền Vai trò cho Trang và Báo cáo


## 1. Cách sử dụng Công cụ Phân quyền Vai trò cho Trang và Báo cáo

Nếu chế độ nhà phát triển bị tắt, người dùng có thể gán các vai trò cho trang và báo cáo bằng cách sử dụng trang "Phân quyền Vai trò cho Trang và Báo cáo".

<img alt="Tools to assign custom roles to the page" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/role-permission-for-page-and-report.png">

### 1.1 Đặt lại về mặc định

Sử dụng nút "Đặt lại về mặc định", người dùng có thể xóa các quyền tùy chỉnh đã áp dụng cho một trang hoặc báo cáo. Sau đó, các quyền mặc định sẽ được áp dụng cho trang hoặc báo cáo đó.

<img alt="Reset the default roles" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/reset-roles-permission-for-page-report.png">

## Thiết lập Phân quyền Vai trò từ Trang/Báo cáo với tư cách là Nhà phát triển
### Phân quyền Vai trò Cho Trang
1. Đi đến: Trang chủ > Nhà phát triển > Trang.
1. Thêm một dòng và chọn những vai trò khác có thể truy cập Trang.

    <img alt="Assign roles to the page" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/roles-for-page.png">

### Phân quyền Vai trò Cho Báo cáo
1. Đi đến: Trang chủ > Nhà phát triển > Báo cáo.
1. Thêm các dòng với các vai trò có thể truy cập Báo cáo.

    <img alt="Assign roles to the report" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/roles-for-report.png">

### 3. Các chủ đề liên quan
1. [Vai trò và Hồ sơ Vai trò](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-and-role-profile)
1. [Phân quyền dựa trên Vai trò](/docs/v13/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
1. [Phân quyền Người dùng](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions)