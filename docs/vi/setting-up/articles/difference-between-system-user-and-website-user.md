<!-- add-breadcrumbs -->
# Sự khác biệt giữa Người dùng hệ thống (System User) và Người dùng website (Website User)

**Câu hỏi:** Tôi đã thêm Nhân viên của mình làm Người dùng và cũng đã gán các Vai trò cho họ. Tuy nhiên, họ vẫn không thể xem được Trang tổng quan sau khi đăng nhập.

**Trả lời:**

Có hai loại Người dùng trong ERPNext.

* **System User (Người dùng hệ thống)**: Họ là Nhân viên của công ty bạn. Ví dụ về các Vai trò được gán cho System User là Account User, Sales Manager, Purchase User, Support Team, v.v.

* **Website User (Người dùng website)**: Họ là các bên liên quan (như Khách hàng và Nhà cung cấp) của Công ty bạn.

Ví dụ về các Vai trò Website User là Customer và Suppliers.

Làm thế nào để kiểm tra một Vai trò dành cho System User hay Website User?

Trong Role master, nếu trường "Desk Access" được tích chọn, thì Vai trò đó dành cho System User. Nếu trường Desk Access không được tích chọn, thì Vai trò đó dành cho Website User.

<img alt="Role Desk Permission" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/role-deskperm.png">