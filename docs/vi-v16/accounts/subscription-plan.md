<!-- add-breadcrumbs -->
# Gói đăng ký

Gói đăng ký lưu trữ thông tin về Mặt hàng được đăng ký, giá của mặt hàng đó và chu kỳ thanh toán.

Để truy cập danh sách Gói đăng ký, hãy đi tới:
> Home > Accounting > Subscription Management > Subscription Plan

## 1. Cách tạo Gói đăng ký
Trước khi bạn có thể thiết lập một Đăng ký, bạn cần có một Gói đăng ký.

1. Đi tới danh sách Gói đăng ký và nhấn vào **Mới**.
1. Chọn **Mặt hàng** sẽ được đăng ký.
1. Chọn **Phương thức xác định giá** (Price Determination) là Cố định (Fixed) hoặc dựa trên [Bảng giá](../stock/price-lists.md).
1. Thiết lập **Chu kỳ thanh toán** (Billing Interval) là Hàng ngày, Hàng tuần, Hàng tháng, hoặc Hàng năm.
1. Thiết lập **Số lượng chu kỳ thanh toán** (Billing Interval Count). Nếu bạn chọn chu kỳ là Năm và số lượng là 5, việc thanh toán sẽ được thực hiện mỗi 5 năm một lần.
1. **Lưu**.
    ![Subscription Plan](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/subscription-plan.png)

Bạn cũng có thể thiết lập thêm các chi tiết thanh toán và liên kết với Cổng thanh toán (Payment Gateway).

Một Gói đăng ký được liên kết với một **Mặt hàng**, từ đó một **Hóa đơn** bán hàng sẽ được tạo ra.

---

## 2. Các cập nhật mới trong phiên bản v16

Trong phiên bản v16, hệ thống quản lý tài chính và đăng ký được nâng cấp mạnh mẽ để hỗ trợ các nghiệp vụ phức tạp hơn:

### 2.1. Mẫu báo cáo tài chính (Financial Report Templates)
Người dùng có thể tùy chỉnh và lưu trữ các mẫu báo cáo tài chính riêng biệt, giúp việc trích xuất dữ liệu kế toán trở nên nhanh chóng và nhất quán hơn.

### 2.2. Bảng cân đối thử hợp nhất (Consolidated Trial Balance)
Hỗ trợ các doanh nghiệp có nhiều công ty con hoặc nhiều chi nhánh. Bạn có thể xem bảng cân đối thử hợp nhất từ tất cả các thực thể trong cùng một báo cáo duy nhất.

### 2.3. Tách chi phí dịch vụ trong Giá vốn hàng bán (COGS tách Service Expenses)
Cải tiến trong việc tính toán Giá vốn hàng bán (COGS). Hệ thống hiện cho phép tách biệt rõ ràng giữa chi phí hàng hóa và chi phí dịch vụ, giúp báo cáo lợi nhuận gộp chính xác hơn đối với các mô hình kinh doanh hỗn hợp.

### 2.4. Xem trước Sổ cái (Ledger Preview)
Trước khi thực hiện **Xác nhận** (Submit) một giao dịch, người dùng có thể xem trước các **Bút toán** (JE) sẽ được ghi nhận vào sổ cái. Điều này giúp giảm thiểu sai sót trong hạch toán kế toán.

### 2.5. Tự động chốt tồn kho (Automatic Closing Stock)
Hệ thống tự động tính toán và cập nhật giá trị tồn kho cuối kỳ, giúp việc chốt sổ tháng/năm trở nên nhanh chóng và chính xác mà không cần can thiệp thủ công quá nhiều.

### 2.6. Kế toán định kỳ (Periodic Accounting)
Hỗ trợ các phương thức kế toán định kỳ, cho phép ghi nhận các bút toán điều chỉnh, khấu hao hoặc phân bổ chi phí theo các khoảng thời gian đã thiết lập sẵn.

{next}