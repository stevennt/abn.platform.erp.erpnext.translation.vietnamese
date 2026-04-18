<!-- add-breadcrumbs -->
# Kỳ kế toán

**Kỳ kế toán xác định một khoảng thời gian mà trong đó các báo cáo tài chính được ghi chép.**

Trong ERPNext, Kỳ kế toán là một khung thời gian mà bên ngoài khoảng thời gian đó, các giao dịch có thể Xác nhận được chọn (như Hóa đơn bán hàng/Hóa đơn mua hàng, Phiếu kho, Bút toán lương, Bút toán, v.v.) sẽ không được phép tạo. Nói cách khác, các giao dịch được chọn chỉ được phép tạo trong Kỳ kế toán đã xác định.

**Tại sao cần Kỳ kế toán?**

Khi các giao dịch được Xác nhận, chúng ảnh hưởng đến sổ cái và các báo cáo xử lý dữ liệu sổ cái.
Điều này có thể gây ra vấn đề khi các báo cáo tài chính phải được lập để kiểm toán bởi các cơ quan chức năng hoặc để khóa sổ kế toán cho năm tài chính.

Tại đây, Kỳ kế toán có thể được sử dụng để giới hạn khoảng thời gian mà các giao dịch có thể được Xác nhận nhằm bảo vệ tính toàn vẹn của các báo cáo tương ứng.

## 1. Cách tạo Kỳ kế toán

### 1.1 Tùy chọn "Đóng" (Closed) cho các giao dịch được chọn dùng để làm gì?

![Accounting Period Child Table](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/accounting-period-closed.png)

Tùy chọn "Đóng" trong bảng con cho các DocType giao dịch được sử dụng để chọn xem giao dịch nào trong số chúng sẽ bị hạn chế sau khi kết thúc Kỳ kế toán.

Lưu ý rằng nếu Kỳ kế toán kết thúc và nếu bất kỳ giao dịch nào được chọn trong bảng con không được tích chọn "Đóng", thì chúng sẽ không bị hạn chế sau khi Kỳ kế toán kết thúc.

1. Nhập tên cho Kỳ kế toán.
2. Xác định khung thời gian bằng cách thiết lập Ngày bắt đầu và Ngày kết thúc.
3. Thêm hoặc xóa các giao dịch khỏi bảng. Lưu ý rằng tất cả các giao dịch được liệt kê trong bảng có tùy chọn "Đóng" được tích chọn sẽ bị hạn chế sau khi kỳ kế toán kết thúc.
4. Lưu và Xác nhận.
    ![Accounting Period](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/accounting-period.png)


Nếu bạn cố gắng xác nhận một giao dịch đã đóng sau khi Kỳ kế toán của nó kết thúc, bạn sẽ thấy thông báo lỗi xác thực ngăn bạn thực hiện việc đó.
![Accounting Period](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/accounting-period-closed-for-transaction.png)

> Lưu ý: Không có vai trò nào có thể xác nhận các giao dịch được xác định trong Kỳ kế toán, ngay cả Vai trò được thiết lập trong 'Role Allowed to Set Frozen Accounts & Edit Frozen Entries' trong [Account Settings](accounts-settings.md).

## 2. Các chủ đề liên quan
* [Cách Kỳ kế toán được sử dụng để Khóa sổ kế toán](https://frappe.io/blog/erpnext-features/closing-accounting-books-in-erpnext)
* [Phiếu khóa kỳ](period-closing-voucher.md)

{next}