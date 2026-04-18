<!-- add-breadcrumbs -->
# Cài đặt Đăng ký

Trang Cài đặt Đăng ký cho phép cấu hình các thiết lập cho các gói đăng ký ERPNext của bạn.

Để truy cập danh sách Đăng ký, hãy đi tới:
> Home > Accounting > Subscription Management > Subscription Settings

* **Grace Period (Thời gian gia hạn)**: Số ngày trôi qua sau ngày lập hóa đơn trước khi hủy đăng ký hoặc đánh dấu đăng ký là chưa thanh toán.

* **Cancel Invoice After Grace Period (Hủy hóa đơn sau thời gian gia hạn)**: Thay vì hiển thị 'Chưa thanh toán', Đăng ký sẽ bị hủy trong ERPNext nếu Khách hàng không thanh toán.

![Subscription](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/subscription-settings.png)

---

## Các tính năng mới trong phiên bản v16

Trong phiên bản v16, phân hệ Kế toán đã được nâng cấp mạnh mẽ với các tính năng quản lý tài chính chuyên sâu:

### 1. Mẫu Báo cáo Tài chính (Financial Report Templates)
Cho phép người dùng tùy chỉnh và tạo các mẫu báo cáo tài chính riêng biệt, giúp việc trích xuất dữ liệu từ Sổ cái trở nên linh hoạt và phù hợp hơn với nhu cầu đặc thù của từng doanh nghiệp.

### 2. Bảng cân đối thử hợp nhất (Consolidated Trial Balance)
Hỗ trợ các doanh nghiệp có nhiều công ty con hoặc nhiều pháp nhân. Tính năng này cho phép xem bảng cân đối thử tổng hợp từ tất cả các thực thể trong cùng một màn hình, giúp kiểm soát dòng tiền và tài sản toàn hệ thống.

### 3. Tách chi phí dịch vụ khỏi Giá vốn hàng bán (COGS tách Service Expenses)
Cải tiến trong việc tính toán Giá vốn hàng bán (COGS). Giờ đây, hệ thống cho phép tách biệt chi phí dịch vụ ra khỏi giá vốn hàng hóa vật chất, giúp báo cáo lợi nhuận gộp chính xác hơn đối với các mô hình kinh doanh kết hợp bán hàng và dịch vụ.

### 4. Xem trước Sổ cái (Ledger Preview)
Trước khi thực hiện **Xác nhận (Submit)** một giao dịch (như Hóa đơn hoặc Bút toán), người dùng có thể xem trước các dòng bút toán sẽ được ghi vào Sổ cái. Điều này giúp giảm thiểu sai sót kế toán và tiết kiệm thời gian chỉnh sửa sau khi đã xác nhận.

### 5. Tự động tính Giá trị tồn kho cuối kỳ (Automatic Closing Stock)
Hệ thống tự động tính toán và cập nhật giá trị tồn kho cuối kỳ dựa trên các nghiệp vụ **Kho (Stock)** và **Lô hàng (Batch)**, giúp việc chốt sổ cuối tháng/năm diễn ra nhanh chóng và chính xác mà không cần can thiệp thủ công quá nhiều.

### 6. Kế toán định kỳ (Periodic Accounting)
Hỗ trợ các phương pháp kế toán định kỳ, cho phép ghi nhận các bút toán điều chỉnh, khấu hao hoặc phân bổ chi phí theo các chu kỳ thời gian đã thiết lập sẵn, đảm bảo tính kịp thời của báo cáo tài chính.

{next}