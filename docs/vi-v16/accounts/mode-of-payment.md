<!-- add-breadcrumbs -->
# Phương thức thanh toán

**Phương thức thanh toán lưu trữ phương tiện mà qua đó các khoản thanh toán được thực hiện hoặc nhận được.**

Để truy cập danh sách Phương thức thanh toán, hãy đi đến:
> Trang chủ > Kế toán > Thiết lập > Phương thức thanh toán

## 1. Cách tạo Phương thức thanh toán
1. Đi đến danh sách Phương thức thanh toán và nhấn vào **Mới**.
1. Nhập tên cho Phương thức thanh toán.
1. Thiết lập loại là Tiền mặt, Ngân hàng hoặc Chung. Điều này hữu ích để biết phương thức thanh toán được sử dụng trong [Điểm bán hàng (PoS)](point-of-sales.md).
1. Thiết lập Tài khoản thanh toán mặc định cho tất cả các công ty.
1. Nhấn **Lưu**.

    ![Mode of Payment](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/mode-of-payment.png)

> **Mẹo**: Việc thiết lập Tài khoản mặc định sẽ giúp tài khoản này được tự động lấy vào trong [Thanh toán](payment-entry.md).

![Mode of Payment](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/mode-of-payment-in-payment-entry.gif)

> **Lưu ý**: Khi thực hiện [Thanh toán](payment-entry.md), tài khoản ngân hàng mặc định sẽ được lấy theo thứ tự sau nếu đã được thiết lập:

>       * Biểu mẫu Công ty
>       * Tài khoản mặc định của Phương thức thanh toán
>       * Tài khoản ngân hàng mặc định của [Khách hàng](customer.md)/[Nhà cung cấp](supplier.md)
>       * Chọn thủ công trong [Thanh toán](payment-entry.md)

## 2. Các chủ đề liên quan
1. [Thanh toán](payment-entry.md)
1. [Yêu cầu thanh toán](payment-request.md)

{next}