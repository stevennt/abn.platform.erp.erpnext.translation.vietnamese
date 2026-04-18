<!-- add-breadcrumbs -->

# Xử lý Đối chiếu Công nợ

**Xử lý Đối chiếu Công nợ là một công cụ giúp bạn gửi Đối chiếu Công nợ (Báo cáo Sổ cái) và Báo cáo Tuổi nợ (Báo cáo Tổng hợp Phải thu) dưới dạng PDF cho khách hàng của bạn hàng loạt qua email, có thể thực hiện thủ công hoặc tự động định kỳ.**

Tính năng này hữu ích khi bạn muốn gửi các cập nhật qua email cho khách hàng định kỳ về các giao dịch của họ (như Hóa đơn bán hàng). Trong tệp đính kèm PDF được gửi qua email cho khách hàng, đối với mỗi khách hàng, sẽ có các chi tiết như ngày hạch toán hóa đơn, số Hóa đơn bán hàng, chi tiết nợ và có, v.v. liên quan đến tài khoản của họ.

Mục đích của tính năng này là nhắc nhở nhiều khách hàng rằng họ có các hóa đơn chưa thanh toán đang chờ xử lý.

<br>
Để truy cập danh sách *Xử lý Đối chiếu Công nợ*, bạn có thể tìm kiếm trên thanh điều hướng hoặc đi đến:

> Home > Kế toán > Công cụ > Xử lý Đối chiếu Công nợ

## 1. Điều kiện tiên quyết

1. Công cụ sử dụng ID email của khách hàng để gửi báo cáo cho họ. Nếu không tìm thấy các mục email dưới đây trong Danh bạ Khách hàng, công cụ sẽ không cho phép bạn chọn Khách hàng tương ứng, vì vậy vui lòng đảm bảo các chi tiết sau đã được điền trong tài liệu Khách hàng.

    - Email Thanh toán của Khách hàng: Đây là mục bắt buộc và có thể được thiết lập trong [Danh bạ Khách hàng](https://docs.erpnext.com/docs/v16/user/manual/vi/crm/contact#1-cach-tao-lien-he) với tùy chọn "Is Billing Contact" được tích chọn.
    - Email Chính của Khách hàng: Mục này không bắt buộc, trừ khi bạn chọn "Send To Primary Contact" trong biểu mẫu.

2. Thiết lập Tài khoản Email với tính năng gửi thư đi (outgoing) đã được bật. Tìm hiểu thêm về điều này [tại đây](https://docs.erpnext.com/docs/v16/user/manual/vi/setting-up/email/email-account).


## 2. Cách tạo một mục Xử lý Đối chiếu Công nợ

1. Đi đến danh sách xem "Xử lý Đối chiếu Công nợ" bằng cách tìm kiếm trên thanh điều hướng và nhấp vào "Mới".

2. Nhập tên cho mục này để tham chiếu trong tương lai.

3. Thiết lập các bộ lọc Sổ cái cho các bản đối chiếu sẽ được gửi cho khách hàng.

    - Các bộ lọc "Từ ngày" và "Đến ngày" sẽ được ẩn và tự động điền động khi tùy chọn "Enable Auto Email" được chọn.
    - "Dự án" và "Trung tâm chi phí" là các trường [Table MultiSelect](https://docs.erpnext.com/docs/v16/user/manual/vi/customize-erpnext/articles/table-multiselect-field). Nghĩa là bạn có thể chọn nhiều Dự án và Trung tâm chi phí trong các bộ lọc Sổ cái.

    ![New Process Statement of Accounts](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/process-statement-of-accounts.png)

4. Trong phần "Khách hàng", bạn có tùy chọn để chọn khách hàng trong bảng con và lấy email chính cũng như email thanh toán của họ.

    - Trường "Select Customer By" cho phép bạn chọn khách hàng hàng loạt, bằng cách nhóm họ dựa trên "Nhóm khách hàng", "Vùng miền", "Đối tác bán hàng" và "Nhân viên bán hàng" bằng cách nhập lựa chọn và nhấp vào "Fetch Customers".
    - Trong các DocType dạng cây như "Vùng miền", "Nhân viên bán hàng" và "Nhóm khách hàng", khi chọn các giá trị nhóm, các khách hàng có giá trị con của các trường này cũng sẽ được lấy ra. Vì vậy, khi bạn chọn "India" làm vùng miền trong biểu mẫu, tất cả khách hàng có giá trị "Vùng miền" nằm dưới India trong cây Vùng miền sẽ được chọn.
    - Tùy chọn "Send To Primary Contact" sẽ gửi Đối chiếu Công nợ đến cả ID email liên hệ chính của khách hàng ngoài email thanh toán.

    ![Customer](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/psoa-customers.png)

5. Trong phần "Tùy chọn in", bạn có thể chọn 2 thứ:

    - Hướng in của tệp PDF, "Khổ ngang" hoặc "Khổ dọc".
    - Liệu bạn có muốn xem báo cáo tuổi nợ (Báo cáo Tổng hợp Phải thu), báo cáo hiển thị số tiền quá hạn theo 30/60/90/120 ngày cho các chứng từ (như Hóa đơn bán hàng), dựa trên "Hạn thanh toán" hoặc "Ngày hạch toán".

    ![Print Preference](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/psoa-print.png)

6. Phần "Cài đặt Email" cho phép bạn cấu hình cách bạn muốn gửi email. Có hai mục con trong phần này:

    ![Email Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/psoa-auto-email.png)

    - Khi chọn "Enable Auto Email", bạn sẽ thấy các tùy chọn để gửi báo cáo định kỳ tự động cho khách hàng trong mục này.
    - Bạn có thể chọn "Tần suất" mà email sẽ được gửi sau "Ngày bắt đầu" cho khách hàng. Các tùy chọn có sẵn là hàng tuần, hàng tháng và hàng quý.
    - Bạn cũng có thể chọn "Khoảng thời gian lọc" tính theo tháng. Ví dụ, nếu bạn đặt "Khoảng thời gian lọc" là '3', bạn sẽ nhận được báo cáo cho ba tháng gần nhất tính từ ngày hiện tại. Ở đây, ngày hiện tại đề cập đến ngày mà email được gửi đi.
    - Các email này không được gửi ngay lập tức, mà được gửi vào nửa đêm dưới dạng một tiến trình chạy ngầm.
    - Sau đó, bạn có thể chọn các trường "Tiêu đề", "CC Đến" và "Nội dung" của email. Nếu bạn không thiết lập giá trị cho các trường này, các giá trị mặc định sẽ được thiết lập như hiển thị bên dưới.

7. Xem lại các cài đặt của bạn và nhấp vào "Lưu".

Bây giờ, hãy đợi email được gửi nếu bạn đã bật "Enable Auto Email" hoặc nhấp vào "Send Emails" để gửi chúng ngay lập tức.

## 3. Các tính năng

### 3.1 Tải xuống PDF tổng hợp của tất cả khách hàng

Khi tạo một mục, có một nút ở trên cùng gọi là "Download" cho phép bạn xem báo cáo PDF tổng hợp của tất cả khách hàng. Bạn có thể sử dụng tính năng này để kiểm tra.

### 3.2 Gửi email thủ công

Khi tạo một mục, có một nút ở trên cùng gọi là "Send Emails" cho phép bạn kích hoạt việc gửi email thủ công cho khách hàng. Các email được đưa vào hàng đợi thông qua một công việc chạy ngầm, bạn có thể theo dõi trong DocType "Email Queue" với các tham chiếu DocType và Tài liệu. Bạn có thể làm điều này ngay cả khi "Enable Auto Email" đang bật.