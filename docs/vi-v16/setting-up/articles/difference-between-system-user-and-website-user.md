<!-- add-breadcrumbs -->
# Sự khác biệt giữa Người dùng hệ thống (System User) và Người dùng website (Website User)

**Câu hỏi:** Tôi đã thêm Nhân viên của mình làm Người dùng và cũng đã gán các Vai trò cho họ. Tuy nhiên, họ vẫn không thể xem được Trang tổng quan sau khi đăng nhập.

**Trả lời:**

Có hai loại Người dùng trong ERPNext.

* **Người dùng hệ thống (System User)**: Họ là Nhân viên của công ty bạn. Ví dụ về các Vai trò được gán cho Người dùng hệ thống là Kế toán, Quản lý bán hàng, Nhân viên mua hàng, Đội ngũ hỗ trợ, v.v.

* **Người dùng website (Website User)**: Họ là các bên liên quan (như Khách hàng và Nhà cung cấp) của Công ty bạn.

Ví dụ về các Vai trò Người dùng website là Khách hàng và Nhà cung cấp.

Làm thế nào để kiểm tra một Vai trò dành cho Người dùng hệ thống hay Người dùng website?

Trong Role master, nếu trường "Desk Access" được tích chọn, thì Vai trò đó dành cho Người dùng hệ thống. Nếu trường Desk Access không được tích chọn, thì Vai trò đó dành cho Người dùng website.

<img alt="Role Desk Permission" class="screenshot" src="../assets/img/articles/role-deskperm.png">