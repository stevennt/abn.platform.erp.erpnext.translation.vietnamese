<!-- add-breadcrumbs -->
# Hóa đơn mua hàng - Lỗi Loại tài khoản

**Câu hỏi:** Khi Lưu Hóa đơn mua hàng, tôi nhận được thông báo xác thực rằng Tài khoản ghi có (Credit To Account) phải là một tài khoản Bảng cân đối kế toán.

![Credit To Account in Purchase Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/credit-to-ledger-in-purchase-invoice.png)

**Trả lời:** Khi Xác nhận một Hóa đơn mua hàng, khoản phải trả sẽ được cập nhật cho Nhà cung cấp. Theo các tiêu chuẩn kế toán, Tài khoản phải trả được xếp vào nhóm Nợ phải trả ngắn hạn (bên Có của Bảng cân đối kế toán).

Thông báo lỗi cho biết Tài khoản được chọn trong trường Credit To không thuộc Nhóm Nợ phải trả. Vui lòng đảm bảo rằng Tài khoản phải trả được chọn trong Hóa đơn mua hàng nằm trong nhóm Nợ phải trả.

{next}