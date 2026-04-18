# Mẫu Email

Mỗi email được gửi đi đều khác nhau nhưng một số email nhất định có thể được tiêu chuẩn hóa, thường được gọi là Mẫu Email hoặc Câu trả lời tiêu chuẩn.

Để truy cập danh sách Mẫu Email, hãy đi tới:
> Trang chủ > Cài đặt > Email > Mẫu Email

## 1. Cách tạo Mẫu Email
1. Đi tới danh sách Mẫu Email, nhấn vào Mới.
1. Nhập tên cho Mẫu Email này.
1. Nhập Tiêu đề cho Mẫu Email này.
1. Phản hồi (Response) là nội dung tiêu chuẩn của email sẽ là một phần của mẫu này.
1. Lưu.

<img class="screenshot" alt="Email Template" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-template-example.png">

**DocType liên kết:** (tùy chọn) DocType liên kết với mẫu này.

### 1.1 Cách sử dụng Mẫu Email
Bạn có thể sử dụng Mẫu Email này trong các Email được gửi từ ERPNext tại trường "CC, BCC & Email Template" trong phần email của tài liệu. ERPNext sẽ lấy tiêu đề và nội dung phản hồi theo mẫu đã chọn.

Bạn có thể thiết lập Mẫu Email Mặc định cho mỗi loại tài liệu thông qua [Tùy chỉnh Biểu mẫu](../../customize-erpnext/customize-form.md).

### 1.2 Cách lấy tên trường (fieldnames)
Các tên trường mà bạn có thể sử dụng trong mẫu email của mình là các trường trong tài liệu mà bạn đang gửi email. Bạn có thể tìm thấy các trường của bất kỳ tài liệu nào thông qua [Tùy chỉnh Biểu mẫu](../../customize-erpnext/customize-form.md) và chọn loại tài liệu (ví dụ: Đơn bán hàng)

### 1.3 Sử dụng HTML để xây dựng mẫu

Có một ô kiểm `Sử dụng HTML` mà bạn có thể bật để chuyển từ trình soạn thảo văn bản sang trình soạn thảo mã nguồn. Điều này cho phép kiểm soát chi tiết hơn đối với nội dung email và giúp dễ dàng sử dụng cho các tính năng như vòng lặp trong Jinja.

### 1.4 Tạo mẫu (Templating)
Các mẫu được biên dịch bằng Jinja. Để tìm hiểu thêm về Jinja, hãy [truy cập trang này](https://jinja.palletsprojects.com/en/2.10.x/).

## 2. Các chủ đề liên quan
1. [Tài khoản Email](email-account.md)
1. [Hộp thư Email](email-inbox.md)