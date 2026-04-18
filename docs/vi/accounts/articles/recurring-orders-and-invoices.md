<!-- add-breadcrumbs -->
# Đơn hàng và Hóa đơn định kỳ

Nếu bạn có hợp đồng với **Khách hàng** mà bạn cần lập hóa đơn cho Khách hàng theo tháng, quý, nửa năm hoặc hàng năm, bạn nên sử dụng tính năng định kỳ trong các đơn hàng và hóa đơn.

## 1. Xem xét một kịch bản

Gói đăng ký cho tài khoản ERPNext được lưu trữ của bạn yêu cầu gia hạn hàng năm. Chúng tôi sử dụng Đơn bán hàng để tạo các hóa đơn tạm tính (proforma invoices). Để tự động hóa việc lập hóa đơn tạm tính cho việc gia hạn, chúng tôi thiết lập Đơn bán hàng gốc là định kỳ. Hóa đơn tạm tính định kỳ sẽ được tạo tự động ngay trước khi tài khoản của khách hàng sắp hết hạn và cần gia hạn. Hóa đơn tạm tính định kỳ này cũng sẽ được gửi email tự động cho khách hàng.

Tính năng thiết lập chứng từ thành định kỳ có sẵn trong Đơn bán hàng, Hóa đơn bán hàng, Đơn mua hàng và Hóa đơn mua hàng.

## 2. Cách tạo đơn hàng/hóa đơn định kỳ
Tùy chọn thiết lập chứng từ thành định kỳ sẽ chỉ hiển thị sau khi nó đã được Xác nhận. Đây là tùy chọn **Lặp lại tự động** (Auto Repeat).

1. Nhấp vào nút + bên cạnh Lặp lại tự động.
1. Chọn DocType tham chiếu.
1. Chọn Chứng từ tham chiếu.
1. Thiết lập Ngày bắt đầu và Ngày kết thúc (tùy chọn).
1. Chọn tần suất như hàng ngày, hàng tuần, v.v.
1. Lưu.

Dưới đây là giải thích về các trường:

* **Từ ngày và Đến ngày:** Trường này xác định thời hạn hợp đồng với khách hàng.
* **Lặp lại vào ngày trong tháng:** Nếu loại định kỳ được thiết lập là Hàng tháng, thì đây sẽ là ngày trong tháng mà hóa đơn định kỳ sẽ được tạo.
* **Lặp lại vào ngày cuối cùng của tháng:** Các hóa đơn định kỳ sẽ được tạo vào ngày cuối cùng của mỗi tháng.
* **Thông báo qua Email:** Các địa chỉ Email (cách nhau bằng dấu phẩy) mà hóa đơn định kỳ sẽ được gửi đến khi được tự động tạo.

Đọc [Lặp lại tự động](../../automation/auto-repeat.md) để biết thêm chi tiết.

## 3. Xử lý ngoại lệ

Trong tình huống hóa đơn định kỳ không được tạo thành công, người dùng có vai trò Quản trị viên hệ thống (System Manager) sẽ được thông báo về việc này qua email. Việc không thể tạo hóa đơn định kỳ có thể do nhiều nguyên nhân như sai Địa chỉ Email được ghi trong trường Thông báo Email trong phần Định kỳ, v.v.

Khi nhận được thông báo, nếu nguyên nhân thất bại được khắc phục (như sửa lại Địa chỉ Email) trong vòng 24 giờ, thì hóa đơn định kỳ sẽ được tạo tự động. Nếu vấn đề không được khắc phục trong thời gian đã nêu, thì chứng từ cho tháng/năm đó phải được tạo thủ công.

### 4. Các chủ đề liên quan
1. [Hóa đơn bán hàng](../sales-invoice.md)
1. [Hóa đơn mua hàng](../purchase-invoice.md)
1. [Đơn bán hàng](../../selling/sales-order.md)
1. [Đơn mua hàng](../../buying/purchase-order.md)