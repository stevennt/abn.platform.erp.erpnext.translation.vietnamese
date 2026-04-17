<!-- add-breadcrumbs -->
# Vai trò và Hồ sơ Vai trò

**Một Vai trò xác định các quyền để truy cập vào các tài liệu khác nhau trong ERPNext.**

Các Vai trò xác định một tập hợp các quyền có thể được thiết lập từ [Quản lý quyền theo Vai trò](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-based-permissions). Các vai trò được sử dụng phổ biến nhất đã được định nghĩa sẵn trong ERPNext, bạn có thể sử dụng hệ thống với chúng. Nếu cần, bạn có thể thêm các vai trò khác. Ví dụ, nếu bạn gán vai trò Sales User cho một người dùng, họ sẽ có thể truy cập các tài liệu như Báo giá và Đơn bán hàng vì các quyền đã được thiết lập sẵn cho vai trò Sales User.

**Hồ sơ Vai trò lưu trữ các vai trò khác nhau để có thể gán nhiều vai trò cùng một lúc.**

Hồ sơ Vai trò đóng vai trò như một mẫu để lưu trữ và lựa chọn nhiều vai trò. Hồ sơ Vai trò này sau đó có thể được gán cho một [Người dùng](/docs/v16/user/manual/en/setting-up/users-and-permissions/adding-users). Ví dụ, một Giám sát viên Kinh doanh sẽ có các vai trò Employee, Sales Manager, Sales User và Sales Master Manager. Hồ sơ Vai trò rất hữu ích để gán nhiều vai trò cùng một lúc khi thêm nhiều nhân viên.

Để truy cập Vai trò, hãy đi tới:
> Home > Users and Permissions > Role

## 1. Cách thêm một Vai trò
1. Đi tới danh sách Vai trò, nhấn vào New.
1. Nhập tên cho Vai trò.
1. Chọn xem Vai trò đó có quyền truy cập vào desk hay không. Một vai trò có quyền truy cập desk có thể truy cập các phân hệ của ERPNext và các tài liệu của công ty. Mức độ truy cập phụ thuộc vào các vai trò được gán cho người dùng.
1. Lưu.

Bạn có thể thêm xác thực hai yếu tố cho vai trò và cũng có thể giới hạn nó trong một lĩnh vực cụ thể. Từ đây, bạn có thể đi tới [Quản lý quyền theo Vai trò](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-based-permissions) và thiết lập quyền cho vai trò trên các DocType khác nhau.

![Permissions for new Role](https://docs.erpnext.com/docs/v16/assets/img/users-and-permissions/role-permissions.png)

## 2. Cách thêm một Hồ sơ Vai trò

Để truy cập Hồ sơ Vai trò, hãy đi tới:
> Home > Users and Permissions > Permissions > Role Profile

1. Đi tới danh sách Hồ sơ Vai trò, nhấn vào New.
1. Nhập tên.
1. Chọn các vai trò bạn muốn gán cho hồ sơ này.
1. Lưu.

    ![Role Profile](https://docs.erpnext.com/docs/v16/assets/img/users-and-permissions/role-profile.png)

### 3. Các chủ đề liên quan
1. [Quyền dựa trên Vai trò](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-based-permissions)
1. [Quyền Người dùng](/docs/v16/user/manual/en/setting-up/users-and-permissions/user-permissions)
1. [Quyền Vai trò cho Trang và Báo cáo](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-permission-for-page-and-report)