<!-- add-breadcrumbs -->
# Tự động tạo Việc cần làm (To-Do)

Mọi Tài liệu trong ERPNext đều có một tùy chọn gọi là 'Assign To' (Giao cho) ở thanh bên. Sử dụng tùy chọn này, bất kỳ Tài liệu nào cũng có thể được giao cho người dùng. Người dùng đó sẽ đồng thời được giao một Việc cần làm (ToDo).

![ToDo Auto Creation](https://docs.erpnext.com/docs/v13/assets/img/using-erpnext/using-todo-auto-assign-1.gif)

Trong các điều kiện như vậy, ba trạng thái của Việc cần làm được xác định dựa trên các cập nhật về việc giao việc.

Hãy xem xét một kịch bản nơi một Việc cần làm được giao thông qua một Vấn đề (Issue). Giả sử có 2 cấp độ Hỗ trợ trong một tổ chức là L1 và L2, và mỗi phiếu hỗ trợ mới được coi là một vấn đề hỗ trợ L1 và được giao cho các thành viên nhóm liên quan. Trong trường hợp này, các trạng thái Việc cần làm sẽ thay đổi như sau:

1. **Open (Mở)**: Khi một vấn đề được tạo và giao cho một thành viên nhóm hỗ trợ L1.
2. **Closed (Đóng)**: Thành viên nhóm hỗ trợ L1 xác định vấn đề và giải quyết nó.
3. **Cancelled (Hủy)**: Thành viên nhóm hỗ trợ L1 xác định vấn đề thuộc cấp độ hỗ trợ L2 và giao nó cho thành viên nhóm liên quan.

## Mở lại các việc đã được giao và đóng lại

Trong cùng một kịch bản như trên, giả sử phiếu hỗ trợ đã được đánh dấu là đóng bởi một thành viên nhóm hỗ trợ L1. Tuy nhiên, Vấn đề sẽ được mở lại nếu phiếu hỗ trợ được mở lại một lần nữa, hoặc có một hoạt động mới phát sinh trong vấn đề này.

Đồng thời, Việc cần làm liên kết với Phiếu hỗ trợ cũng sẽ được mở lại.

![ToDo](https://docs.erpnext.com/docs/v13/assets/img/using-erpnext/using-to-do-6.png)