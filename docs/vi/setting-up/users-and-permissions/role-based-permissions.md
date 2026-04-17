<!-- add-breadcrumbs -->
# Phân quyền dựa trên Vai trò

**Quyền truy cập vào các tài liệu khác nhau có thể được kiểm soát bằng cách sử dụng Phân quyền dựa trên Vai trò.**

ERPNext có hệ thống phân quyền dựa trên vai trò. Điều này có nghĩa là bạn có thể gán Vai trò cho Người dùng, và các Quyền có thể được thiết lập trên các Vai trò đó. Trình quản lý Quyền Vai trò (Role Permissions Manager) cho phép bạn thiết lập vai trò nào có thể truy cập vào tài liệu nào và với những quyền gì (đọc, ghi, xác nhận, v.v.).

Sau khi các vai trò được gán cho một người dùng, quyền truy cập của họ có thể được giới hạn trong các tài liệu cụ thể. Cấu trúc phân quyền cho phép bạn xác định các quy tắc phân quyền khác nhau cho các trường khác nhau bằng một khái niệm gọi là **Cấp độ Quyền (Permission Level)** của một trường.

## 1. Cách sử dụng Trình quản lý Quyền Vai trò
Để bắt đầu sử dụng Trình quản lý Quyền Vai trò, hãy đi tới:
> Home > Users and Permissions > Role Permissions Manager

<img alt="Manage Read, Write, Create, Submit, Amend access using the Role Permissions Manager" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/users-and-permissions/setting-up-permissions-leave-application.png">

Quyền được áp dụng dựa trên sự kết hợp của:

  * **Vai trò (Roles):** Như chúng ta đã thấy trước đó, Người dùng được gán các Vai trò và chính trên các Vai trò này các quy tắc phân quyền được áp dụng. Ví dụ, một người dùng bán hàng có thể được cấp các vai trò là Nhân viên và Người dùng bán hàng.

  Các ví dụ về Vai trò bao gồm Quản lý kế toán, Nhân viên, Người dùng nhân sự, v.v.

  * **Loại tài liệu (Document Types):** Mỗi loại tài liệu, dù là dữ liệu danh mục hay giao dịch, đều có một danh sách phân quyền dựa trên vai trò riêng biệt như trong ảnh chụp màn hình trước đó.

  Các ví dụ về Loại tài liệu là Hóa đơn bán hàng, Đơn xin nghỉ phép, Phiếu kho, v.v.

  * **Cấp độ Quyền (Permission Levels):** Trong mỗi tài liệu, bạn có thể nhóm các trường theo "cấp độ". Mỗi nhóm trường được ký hiệu bằng một số duy nhất (từ 0 đến 9). Một bộ quy tắc phân quyền riêng biệt có thể được áp dụng cho mỗi nhóm trường. Theo mặc định, tất cả các trường đều ở cấp độ 0.

    "Cấp độ" Quyền kết nối các trường ở cấp độ X với một quy tắc phân quyền ở cấp độ X. Để biết thêm, hãy nhấp [vào đây](/docs/v13/user/manual/en/setting-up/articles/managing-perm-level).

  * **Các giai đoạn của tài liệu (Document Stages):** Quyền được áp dụng cho mỗi giai đoạn của tài liệu như Khởi tạo, Lưu, Xác nhận, Hủy và Sửa đổi. Một vai trò có thể được cho phép In, Email, Nhập hoặc Xuất dữ liệu, truy cập Báo cáo, hoặc xác định Quyền Người dùng.

  * **Quyền Người dùng (User Permissions):** Sử dụng Quyền Người dùng trong ERPNext, một người dùng có thể bị giới hạn chỉ được truy cập vào các Tài liệu cụ thể cho Loại tài liệu đó. Ví dụ: Chỉ một Khu vực trong tất cả các Khu vực. Các Quyền Người dùng được xác định cho các Loại tài liệu khác cũng sẽ được áp dụng nếu chúng liên quan đến Loại tài liệu hiện tại thông qua các Trường Liên kết (Link Fields).

    Ví dụ, Khách hàng là một trường liên kết trong Đơn bán hàng hoặc Báo giá. Trong Trình quản lý Quyền Vai trò, Quyền Người dùng có thể được thiết lập bằng nút 'Set User Permissions'.

    Để thiết lập Quyền Người dùng dựa trên tài liệu/trường, hãy đi tới:
    > Home > Users and Permissions > Permissions > [User Permissions](/docs/v13/user/manual/en/setting-up/users-and-permissions/user-permissions)

  * **Thêm Quy tắc Mới (Add a New Rule)**: Trong Trình quản lý Quyền Vai trò, để thêm một quy tắc mới, hãy nhấp vào nút **Add a New Rule** và một hộp thoại sẽ yêu cầu bạn chọn một Vai trò và một Cấp độ Quyền. Sau khi bạn chọn điều này và nhấp vào 'Add', một hàng mới sẽ được thêm vào bảng quy tắc của bạn.

## 2. Cách Phân quyền dựa trên Vai trò hoạt động

Đơn xin nghỉ phép là một ví dụ điển hình bao quát tất cả các khía cạnh của một Hệ thống Phân quyền.

* Nó nên được tạo bởi một Nhân viên.
  Đối với việc này, Vai trò Nhân viên nên được cấp các quyền Đọc, Ghi, Tạo.

  <img class="screenshot" alt="Giving Read, Write and Create Permissions to Employee for Leave Application"  src="https://docs.erpnext.com/docs/v13/assets/img/users-and-permissions/setting-up-permissions-employee-role.png">

* Một **Nhân viên** chỉ nên có thể truy cập Đơn xin nghỉ phép của chính mình.
  Do đó, bản ghi Quyền Người dùng nên được tạo cho mỗi sự kết hợp giữa Người dùng-Nhân viên.

  <img class="screenshot" alt="Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager" src="https://docs.erpnext.com/docs/v13/assets/img/users-and-permissions/setting-up-permissions-employee-user-permissions.png">

* Nếu bạn muốn một **Nhân viên** chỉ có thể chọn một tài liệu trong một tài liệu khác mà không có quyền đọc toàn bộ tài liệu đó, thì chỉ cấp quyền Chọn (Select) cho vai trò Nhân viên.

  <img class="screenshot" alt="Limiting access to Leave Applications for a user with Employee Role via User Permissions Manager" src="https://docs.erpnext.com/docs/v13/assets/img/users-and-permissions/setting-up-select-permissions-employee.png">

* **Quản lý nhân sự** nên có thể xem tất cả các Đơn xin nghỉ phép.
  Tạo một Quy tắc Phân quyền cho Quản lý nhân sự ở Cấp độ 0, với quyền Đọc. Mục 'Apply User Permissions' nên được tắt.

  <img class="screenshot" alt="Giving Submit and Cancel permissions to HR Manager for Leave Applications. 'Apply User Permissions' is unchecked to give full access." src="https://docs.erpnext.com/docs/v13/assets/img/users-and-permissions/setting-up-permissions-hr-manager-role.png">

* **Người phê duyệt nghỉ phép** nên có thể xem và cập nhật Đơn xin nghỉ phép của các nhân viên dưới quyền họ.
  Người phê duyệt nghỉ phép được cấp quyền Đọc và Ghi ở Cấp độ 0. Các Tài liệu Nhân viên liên quan nên được liệt kê trong Quyền Người dùng của Người phê duyệt nghỉ phép. (Nỗ lực này được giảm bớt cho những Người phê duyệt nghỉ phép được đề cập trong Tài liệu Nhân viên bằng cách tạo các bản ghi Quyền Người dùng bằng lập trình).

  <img class="screenshot" alt="Giving Read, Write and Submit permissions to Leave Approver for Leave Applications.'Apply User Permissions' is checked to limit access based on Employee." src="https://docs.erpnext.com/docs/v13/assets/img/users-and-permissions/setting-up-permissions-leave-approver-role.png">

* Nó chỉ nên được Phê duyệt/Từ chối bởi Người dùng nhân sự hoặc Người phê duyệt nghỉ phép.
  Trường Trạng thái của Đơn xin nghỉ phép được đặt ở Cấp độ 1. Người dùng nhân sự và Người phê duyệt nghỉ phép được cấp quyền Đọc và Ghi cho Cấp độ 0, trong khi tất cả những người khác (All) được cấp quyền Đọc cho Cấp độ 1.

  <img class="screenshot" alt="Limiting read access for a set of fields to certain Role" src="https://docs.erpnext.com/docs/v13/assets/img/users-and-permissions/setting-up-permissions-leave-approver-role.png">