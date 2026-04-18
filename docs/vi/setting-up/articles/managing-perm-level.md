<!-- add-breadcrumbs -->
#Quản lý Cấp độ Quyền trong Trình quản lý Quyền

Cấp độ Quyền (Perm Level) là một cách để giảm lượng thông tin có thể hiển thị hoặc có thể thay đổi trong một DocType cụ thể đối với các Nhóm Người dùng nhất định. Trong khi bạn có thể xác định khả năng hiển thị hoặc khả năng thay đổi cho từng DocType bằng cách tùy chỉnh Quy tắc Quyền cụ thể của DocType đó, thì với Cấp độ Quyền, bạn có thể thay đổi những điều này cho các Phần hoặc Trường cụ thể.

Trong mỗi tài liệu, bạn có thể nhóm các trường theo các "cấp độ". Mỗi nhóm trường hoặc nhóm trường được ký hiệu bằng một con số duy nhất (0, 1, 2, 3, v.v.). Một bộ quy tắc quyền riêng biệt có thể được áp dụng cho mỗi nhóm trường. Theo mặc định, tất cả các trường đều ở cấp độ 0.

Cấp độ Quyền (viết tắt của Permission Level) cho một trường có thể được xác định trong [Customize Form](../../customize-erpnext/customize-form.html.md).

<img alt="Perm Level Field" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/perm-level-1.gif">

Nếu bạn cần gán các quyền khác nhau cho một trường cụ thể cho các người dùng khác nhau, bạn có thể thực hiện thông qua Cấp độ Quyền. Hãy cùng xem xét một ví dụ để hiểu rõ hơn.

Phiếu giao hàng có thể được truy cập bởi Quản lý Kho cũng như Nhân viên Kho. Bạn không muốn Nhân viên Kho truy cập vào các trường liên quan đến Số tiền trong Phiếu giao hàng, nhưng các trường khác vẫn phải hiển thị giống như đối với Quản lý Kho.

Đối với tất cả các trường liên quan mà không muốn cho xem, bạn có thể đặt Cấp độ Quyền là (ví dụ) 2.

Đối với các Quản lý Kho, họ sẽ có quyền đối với các trường trên Phiếu giao hàng có Cấp độ Quyền là 2, trong khi Nhân viên Kho sẽ không có bất kỳ quyền nào đối với Cấp độ Quyền 2 trong Phiếu giao hàng, vì vai trò của họ không được gán quy tắc cho phép họ đọc hoặc ghi vào Trường có Cấp độ Quyền là 2, như hiển thị dưới đây.

<img alt="Perm Level Rule" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/perm-level-2.png">

Cũng với kịch bản đó, nếu bạn muốn một Nhân viên Kho có thể truy cập vào một trường ở Cấp độ Quyền 2, nhưng không muốn cho phép chỉnh sửa trường đó, thì Nhân viên Kho sẽ chỉ được gán quyền chỉ có thể đọc ở Cấp độ Quyền 2, chứ không được ghi/chỉnh sửa.

<img alt="Perm Level Rule 2" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/perm-level-3.png">

Các Cấp độ Quyền (1, 2, 3 hoặc 2, 1, 3 hoặc 3, 2, 1) không cần phải theo một thứ tự cụ thể nào. Chúng không ám chỉ thứ bậc. Cấp độ Quyền chủ yếu được sử dụng để nhóm một số trường lại với nhau, sau đó gán quyền cho các Vai trò cho nhóm đó. Do đó, bạn có thể đặt bất kỳ cấp độ quyền nào cho một mục, và sau đó thực hiện thiết lập quyền cho nó.

Nếu bạn muốn thay đổi quyền cho tất cả các trường trong một phần, bạn chỉ cần thay đổi cấp độ quyền cho trường của phần đó và nó sẽ được áp dụng cho tất cả các trường trong phần đó.

<!-- markdown -->