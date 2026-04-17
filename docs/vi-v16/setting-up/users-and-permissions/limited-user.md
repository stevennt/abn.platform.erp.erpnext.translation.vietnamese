<!-- add-breadcrumbs -->
# Người dùng hạn chế

**Người dùng sẽ được cấp quyền truy cập hạn chế vào hệ thống.**

Người dùng hạn chế chỉ có thể truy cập vào các tài liệu cụ thể của các phân hệ cụ thể. Một số người dùng nhất định không sử dụng tất cả các phân hệ mà chỉ cần các phân hệ nhất định. Ví dụ, trong công ty, để ghi chép việc chấm công hàng ngày hoặc đơn xin nghỉ phép, mọi nhân viên đều được cấp quyền truy cập hệ thống cần thiết. Nhưng giả sử có 500 người đang làm việc trong công ty, trong đó chỉ có 100 người sử dụng tất cả các tài liệu và 400 người còn lại chỉ cần các tài liệu về chấm công hàng ngày hoặc đơn xin nghỉ phép. Những người dùng như vậy là người dùng hạn chế.

DocType User đóng vai trò quan trọng để xử lý trường hợp này. Có các Loại người dùng (User Type) mặc định là "System User" và "Website User", trong đó System User có thể truy cập vào desk và cổng thông tin website, trong khi Website User chỉ có thể truy cập cổng thông tin website. Để xử lý trường hợp nhân viên bị hạn chế quyền truy cập tài liệu, theo mặc định ERPNext đã thêm một loại người dùng mới là 'Employee Self Service'.

## Loại người dùng (User Type)

Để truy cập DocType User Type, hãy đi tới:

> Users > User Type

<img class="screenshot" alt="User Type" src="../assets/img/users-and-permissions/user-type.png">

Website User và System User sẽ là các loại người dùng tiêu chuẩn và không thể bị xóa hoặc chỉnh sửa. Tuy nhiên, các loại người dùng không tiêu chuẩn (Tùy chỉnh) có thể được xóa, tạo hoặc chỉnh sửa. Theo mặc định, quyền xóa không được cấp cho bất kỳ người dùng nào.

## Loại người dùng không tiêu chuẩn

1) Đối với loại người dùng không tiêu chuẩn, người dùng phải chọn Vai trò tùy chỉnh (Custom Role), tài liệu mà họ muốn áp dụng quyền người dùng, và tên trường (fieldname) của người dùng.

<img class="screenshot" alt="User Type" src="../assets/img/users-and-permissions/user-type-role.png">

Trong hình trên, Nhân viên (Employee) có trường liên kết User ID được liên kết với DocType User. Vì mục "Apply User Permission on" đã được thiết lập là "Employee", nên người dùng của nhân viên tương ứng chỉ có thể xem các tài liệu mà trường nhân viên tương ứng được liên kết. Ví dụ, nhân viên chỉ có thể xem phiếu lương (salary slip) được tạo dựa trên mã nhân viên của họ.

2) Các loại tài liệu (Document Types):

Người dùng thuộc loại người dùng không tiêu chuẩn chỉ có thể truy cập các tài liệu đã được đề cập trong loại người dùng đó.

<img class="screenshot" alt="User Type" src="../assets/img/users-and-permissions/user-type-document-type.png">

Bảng trên cũng đóng vai trò như Role Permission Manager cho Loại người dùng cụ thể này (trong trường hợp của chúng ta là Employee Self Service). Vai trò Employee Self Service sẽ không thể truy cập được trong Role Permission Manager thông thường.

3) Các loại tài liệu (Chỉ chọn quyền Xem - Select Permissions Only):

Trong bảng này, bạn cần liệt kê tất cả các DocType mà bạn muốn người dùng Employee Self Service có quyền truy cập SELECT (Xem). Không có giới hạn về số lượng DocType mà bạn có thể thêm vào đây. Người dùng sẽ không thể tạo các bản ghi cho các tài liệu mà họ chỉ có quyền truy cập Select.

<img class="screenshot" alt="User Type" src="../assets/img/users-and-permissions/user-type-select-perm.png">

## Thêm người dùng không tiêu chuẩn

Khi thêm người dùng mới, người dùng cần chọn loại người dùng. Trong trường hợp là loại người dùng không tiêu chuẩn, người dùng tương ứng phải được liên kết với tài liệu đã được thiết lập trong trường "Apply User Permission On".

<img class="screenshot" alt="User Type" src="../assets/img/users-and-permissions/limited-access-user.png">