<!-- add-breadcrumbs -->
# Đơn thanh toán

**Đơn thanh toán là một chứng từ nội bộ để ghi lại các khoản thanh toán hàng loạt cho Nhà cung cấp.**

Trong các tập đoàn lớn, quyết định thanh toán cho Nhà cung cấp được thực hiện bởi một người như Quản lý mua hàng. Việc thực hiện thanh toán được thực hiện bởi Kế toán (Người dùng kế toán).

Đơn thanh toán là sự trao đổi thông tin giữa Quản lý mua hàng và Kế toán để thông báo cho Kế toán tiến hành Thanh toán.

Trong ERPNext v16, bằng cách sử dụng Đơn thanh toán, bạn có thể lấy nhiều Hóa đơn đã được tạo cho một Nhà cung cấp. Ngoài ra, hệ thống v16 hỗ trợ xem trước Bút toán (Ledger Preview) trước khi Xác nhận để đảm bảo tính chính xác của dữ liệu kế toán.

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Đơn thanh toán, bạn nên tạo các chứng từ sau trước:

1. [Đơn mua hàng](../buying/purchase-order.md)

 Hoặc

1. [Hóa đơn mua hàng](../accounts/purchase-invoice.md)

## 2. Cách tạo Đơn thanh toán
1. Đi tới danh sách Đơn thanh toán và nhấn vào **Mới**.
1. Chọn tài khoản ngân hàng của Công ty.
1. Nhấn vào nút **Lấy từ** và chọn Hóa đơn mua hàng. Áp dụng bộ lọc nếu cần và chọn các Hóa đơn cần thanh toán.
 ![Payment Order Fetch](https://docs.erpnext.com/docs/v16/assets/img/accounts/payment-order-fetch.png)
1. Các Hóa đơn sẽ được lấy vào Đơn thanh toán.
 ![Payment Order Fetch](https://docs.erpnext.com/docs/v16/assets/img/accounts/payment-order.png)
1. Kiểm tra thông tin và nhấn **Lưu**.
1. **Xem trước Bút toán (Ledger Preview):** Trước khi thực hiện, bạn có thể kiểm tra các bút toán kế toán sẽ được tạo để đảm bảo khớp với các báo cáo tài chính như Bảng cân đối thử hợp nhất (Consolidated Trial Balance).
1. Nhấn **Xác nhận** Đơn thanh toán. Bây giờ, bạn sẽ thấy một nút để thực hiện các Bút toán thanh toán hàng loạt.
 ![Payment Order Fetch](https://docs.erpnext.com/docs/v16/assets/img/accounts/payment-order-submit.png)

 {next}