<!-- add-breadcrumbs -->
# Bút toán chênh lệch

Theo các tiêu chuẩn kế toán, bên nợ trong một bút toán kế toán phải bằng bên có. Nếu không, hệ thống sẽ không cho phép Xác nhận giao dịch kế toán, từ đó ngăn chặn việc hạch toán vào sổ cái. Trong ERPNext, khi Lưu một bút toán kế toán, hệ thống sẽ kiểm tra xem bên nợ và bên có có khớp nhau hay không.

![Debit and Credit](/docs/v13/assets/img/articles/journal-entry-message.png)

Để bút toán được cân bằng, bạn nên thêm một dòng nữa, chọn một Tài khoản khác và cập nhật số tiền chênh lệch vào đó. Hoặc bạn có thể thêm số tiền chênh lệch trực tiếp vào một trong các dòng Tài khoản hiện có.

Khi nhấp vào nút 'Make Difference Entry', một dòng mới sẽ được thêm vào bảng Tài khoản của Bút toán, với số tiền chênh lệch. Bạn có thể chỉnh sửa dòng đó để chọn Tài khoản phù hợp.

![Difference ENtry](/docs/v13/assets/img/articles/difference-entry.gif)

Sau khi chọn tài khoản cho dòng mới, bên nợ và bên có của bút toán sẽ khớp nhau, và bạn sẽ có thể Xác nhận Bút toán một cách chính xác.

{next}