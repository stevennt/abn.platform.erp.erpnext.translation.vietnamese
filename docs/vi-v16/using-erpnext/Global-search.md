<!-- add-breadcrumbs -->
# Tìm kiếm toàn cầu

**Tìm kiếm toàn cầu là một thao tác xử lý văn bản mạnh mẽ trong ERPNext giúp bạn tìm kiếm một DocType hoặc Tài liệu cụ thể.**

Với mỗi chuỗi từ hoặc một tập hợp các ký tự, bạn sẽ nhận được kết quả tìm kiếm.

### Sử dụng Awesome Bar để Tìm kiếm toàn cầu.

![Tree Master Renaming](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-global-search-2.gif)

Tìm kiếm toàn cầu giúp người dùng tìm thấy thông tin một cách nhanh chóng. Nó nằm ở góc trên bên phải trong ERPNext. Chỉ cần nhập một vài ký tự vào Thanh tìm kiếm, kết quả từ nhiều loại bản ghi khác nhau (Liên hệ, Khách hàng, Vấn đề, v.v.) liên quan đến từ khóa đó sẽ được hiển thị. Bạn cũng có thể tùy chỉnh các trường để quyết định kết quả tìm kiếm nào sẽ được hiển thị.

Bạn cũng có thể nhập nhiều từ khóa cách nhau bởi toán tử `&` để tìm kết quả mong muốn. Bạn có thể tham khảo các trường hợp sau để làm ví dụ:

- Nhập `"apple & iPod"` có thể trả về các tài liệu mà một trường chứa Apple và trường còn lại chứa iPod (Nhà cung cấp của Đơn mua hàng và Mặt hàng).
- Nhập `"iPhone & iPod"` có thể trả về các tài liệu mục tiêu có chứa cả mặt hàng iPhone và iPod (các mặt hàng trong bảng con).
- Nhập `"iPhone & black"` có thể trả về mặt hàng có mô tả chứa cả iPhone và black (trường văn bản dài).
- Nhập `"foo & bar"` có thể trả về bất kỳ tài liệu nào được gán cả hai thẻ foo và bar (trường văn bản dài đặc biệt *usertags*).

### Bật Tìm kiếm toàn cầu cho các trường trong một DocType.

![Tree Master Renaming](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/using-global-search-1.gif)