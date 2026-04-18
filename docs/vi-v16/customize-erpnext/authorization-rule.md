<!-- add-breadcrumbs -->
# Quy tắc Ủy quyền

**Quy tắc Ủy quyền cho phép cấu hình việc ủy quyền / phê duyệt tùy chỉnh trên các chứng từ, dựa trên các điều kiện được xác định.**

Ví dụ: Nếu Tổng cộng của một Đơn bán hàng vượt quá 1.000 USD, thì nó chỉ được phép Xác nhận bởi Quản lý bán hàng, ngay cả khi Nhân viên bán hàng có quyền "Xác nhận".

Tương tự như vậy, bạn có thể xác định Quy tắc Ủy quyền dựa trên các trường như Tổng ròng, Tổng cộng, % Chiết khấu và chỉ định ai sẽ là người phê duyệt chứng từ nếu điều kiện ủy quyền được khớp.

![Authorization Rule](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/authorization-rule.png)

Hãy cùng xem xét một ví dụ chi tiết về Quy tắc Ủy quyền để hiểu rõ hơn.

Giả sử Quản lý bán hàng cần ủy quyền cho các Đơn bán hàng, chỉ khi giá trị Tổng cộng của nó vượt quá 10.000. Nếu giá trị Đơn bán hàng nhỏ hơn 10.000, thì ngay cả Nhân viên bán hàng cũng có thể Xác nhận nó. Điều này có nghĩa là quyền Xác nhận của Nhân viên bán hàng sẽ bị giới hạn chỉ đối với các Đơn bán hàng có Tổng cộng nhỏ hơn 10.000.

## 1. Cách tạo Quy tắc Ủy quyền

1. Đi tới danh sách Quy tắc Ủy quyền, nhấn vào Mới.
1. Chọn giao dịch mà Quy tắc Ủy quyền sẽ được áp dụng. Chức năng này chỉ khả dụng cho một số giao dịch giới hạn.
1. Nhập Giá trị Ủy quyền (Authorized Value), v.v. Điều này phụ thuộc vào trường bạn đã chọn trong phần Dựa trên (Based On).
1. Chọn Dựa trên (Based On). Quy tắc Ủy quyền sẽ được áp dụng dựa trên giá trị được chọn trong trường này.
1. Chọn Vai trò áp dụng (Applicable Role). Đây là vai trò mà Quy tắc Ủy quyền này sẽ được áp dụng. Theo ví dụ, đó sẽ là Nhân viên bán hàng.
1. Để cụ thể hơn, bạn cũng có thể chọn Áp dụng cho Người dùng (Applicable To User) nếu bạn muốn áp dụng quy tắc cho một Nhân viên bán hàng cụ thể, thay vì áp dụng cho tất cả Nhân viên bán hàng.
1. Chọn Vai trò phê duyệt (Approving Role). Đây là vai trò có thể phê duyệt các biểu mẫu vượt quá Giá trị Ủy quyền. Theo ví dụ của chúng ta, đó là Quản lý bán hàng.
1. Bạn cũng có thể chọn một Quản lý bán hàng cụ thể.
1. Lưu.

![Authorization Rule](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/new-authorization-rule.png)

Nếu Nhân viên bán hàng cố gắng Xác nhận Đơn bán hàng có giá trị cao hơn 10.000, họ sẽ nhận được thông báo lỗi.

![Authorization Rule Validation Message](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/authorization-rule-validation-message.png)

> Nếu bạn muốn hạn chế Nhân viên bán hàng Xác nhận các Đơn bán hàng, thay vì tạo Quy tắc Ủy quyền, bạn nên xóa quyền Xác nhận của Nhân viên bán hàng trong [Phân quyền theo Vai trò](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-based-permissions).

### Các chứng từ có thể áp dụng Quy tắc Ủy quyền

1. Đơn bán hàng
1. Đơn mua hàng
1. Báo giá
1. Phiếu giao hàng
1. Hóa đơn bán hàng
1. Hóa đơn mua hàng
1. Phiếu nhập hàng
1. Đánh giá

### Các trường có thể dùng làm điều kiện cho Quy tắc Ủy quyền

1. Tổng cộng
1. Chiết khấu trung bình
1. Chiết khấu theo Khách hàng
1. Chiết khấu theo Mặt hàng

{next}