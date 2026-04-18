<!-- add-breadcrumbs -->
# Giao việc

**Giao việc (Assign To) là một tính năng trong ERPNext cho phép bạn giao một tài liệu cụ thể cho một người dùng nhất định, người cần thực hiện các công việc tiếp theo trên tài liệu đó.**

Ví dụ, nếu một Đơn bán hàng cần được Quản lý bán hàng phê duyệt hoặc Xác nhận, người tạo bản Nháp đầu tiên có thể giao Đơn bán hàng đó cho Quản lý bán hàng.

Khi giao tài liệu này cho Quản lý bán hàng, nó sẽ được thêm vào danh sách Việc cần làm (ToDo) của người dùng đó.

Tương tự, đối với Phiếu giao hàng và Hóa đơn bán hàng dựa trên Đơn bán hàng này, việc giao việc có thể được thực hiện cho một Người dùng Kho và một Người dùng Kế toán.

![Assignment](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-assignment-1.png)

> Lưu ý: Việc giao việc có thể được thực hiện bất kể các Hạn chế về Quyền hạn.

## Giao việc mới

Để tạo một giao việc mới, hãy đi tới tài liệu mà bạn muốn thực hiện giao việc và nhấp vào nút 'Assigned to' nằm ở thanh bên trái. Chọn tên của Người dùng mà bạn muốn giao việc này.

![Assignment](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-assignment-2.gif)

Cùng với việc giao việc, bạn cũng có thể để lại một bình luận để người được giao việc xem xét.

![Assignment](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-assignment-3.gif)

### Danh sách Việc cần làm của người được giao

Mọi việc được giao cho một Người dùng cụ thể sẽ được hiển thị trong phần Việc cần làm (ToDo) của họ.

![Assignment](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-assignment-4.png)

### Hủy giao việc

Người dùng có thể hủy các giao việc bằng cách nhấp vào nút "Closed" trong tài liệu.

![Assignment](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-assignment-5.png)

Khi việc được giao được đặt là đã hoàn thành, mục Việc cần làm tương ứng cũng sẽ đồng thời được cập nhật thành 'Closed'.

{next}