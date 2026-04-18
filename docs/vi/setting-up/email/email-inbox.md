<!-- add-breadcrumbs -->
# Hộp thư Email

**Sau khi một tài khoản email được thêm vào, hộp thư email sẽ có thể truy cập được.**

Việc điều hành một doanh nghiệp bao gồm nhiều hoạt động trao đổi email giao dịch với các bên như Khách hàng, Nhà cung cấp và các thành viên khác trong công ty. Tính năng Hộp thư Email cho phép bạn kéo tất cả các email kinh doanh vào tài khoản ERPNext của mình. Việc cho phép truy cập các email kinh doanh cùng với các chi tiết giao dịch khác giúp ERPNext trở thành một nền tảng duy nhất để truy cập tất cả thông tin kinh doanh tại một nơi.

Trong ERPNext, bạn có thể cấu hình Hộp thư Email cho từng Người dùng hệ thống (System User). Dưới đây là các bước chi tiết để cấu hình Hộp thư Email cho một Người dùng.

## 1. Tạo Người dùng

Bạn chỉ có thể cấu hình Hộp thư Email cho Người dùng hệ thống. Do đó, hãy đảm bảo rằng bạn đã thêm chính mình và đồng nghiệp của mình dưới dạng Người dùng và cấp cho họ các quyền cần thiết.

Để biết cách thêm Người dùng mới, hãy đi đến [trang Người dùng](../users-and-permissions/adding-users.md).

## 2. Tạo Tên miền Email

Tên miền Email cho các Dịch vụ sau đã có sẵn sẵn dùng và bạn có thể tiến hành trực tiếp để tạo [Tài khoản Email](email-account.md). Tìm hiểu thêm về cách tạo Tên miền Email [tại đây](email-domain.md).

* **Gmail**
* **Yahoo**
* **Sparkpost**
* **SendGrid**
* **Outlook.com**
* **Yandex.mail**

<img class="screenshot" alt="Email Service" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-service.png">

Để có thể gửi và nhận email vào tài khoản ERPNext của bạn từ các dịch vụ email khác (như WebMail hoặc Gmail), bạn nên thiết lập một Tên miền Email chính. Trong phần chính này, các chi tiết cổng email như Địa chỉ SMTP, Số cổng, chi tiết địa chỉ IMAP/POP3 sẽ được ghi lại. Nếu bạn đã từng cấu hình một ứng dụng email cục bộ (như Outlook), Tên miền Email chính cũng yêu cầu các chi tiết được nhập tương tự.

Để thêm Tên miền Email mới, hãy đi đến:

> Home > Settings > Emails > Email Domain > New

<img class="screenshot" alt="Email Domain" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-domain.png">

Tìm hiểu thêm về Tên miền Email [tại đây](email-domain.md). Sau khi bạn đã cấu hình Tên miền Email cho Dịch vụ Email của mình, nó sẽ được sử dụng để tạo các Tài khoản Email cho tất cả Người dùng trong tài khoản ERPNext của bạn.

## 3. Tài khoản Email

Tạo một Tài khoản Email dựa trên ID Email của Người dùng. Đối với mỗi Người dùng có tài khoản email cần được tích hợp với ERPNext, một Tài khoản Email chính cần được tạo.

Nếu bạn đang tạo một Tài khoản Email cho đồng nghiệp mà bạn không biết Mật khẩu Email của họ, hãy kiểm tra trường "Awaiting Password". Theo cài đặt này, một Người dùng (người mà Tài khoản Email được tạo cho họ) sẽ nhận được một thông báo yêu cầu nhập mật khẩu email khi truy cập vào tài khoản ERPNext của họ.

<img class="screenshot" alt="Email Password" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-password.png">

> Nếu bạn đang tạo một Tài khoản Email cho Hộp thư Email của một Người dùng, hãy để trống trường Append To.

Đọc [tài liệu về Tài khoản Email](email-account.md) để biết thêm chi tiết về cách thiết lập.

## 4. Liên kết Tài khoản Email trong thông tin Người dùng

Sau khi một Tài khoản Email được tạo cho một Người dùng, hãy chọn Tài khoản Email đó trong Người dùng. Điều này sẽ đảm bảo rằng các email được kéo từ ID Email nói trên sẽ chỉ có thể truy cập được bởi Người dùng này trong tài khoản ERPNext của bạn.

<img class="screenshot" alt="Email User Link" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-user-link.png">

Bạn có thể liên kết nhiều email với một người dùng.

## 5. Sử dụng Hộp thư Email

Nếu bạn đã cấu hình đúng Hộp thư Email như hướng dẫn ở trên, thì khi Người dùng đăng nhập, biểu tượng Hộp thư Email sẽ hiển thị. Thao tác này sẽ đưa người dùng đến chế độ xem Hộp thư Email trong tài khoản ERPNext. Tất cả các Email nhận được trên email đó sẽ được lấy về và liệt kê trong chế độ xem Hộp thư Email. Người dùng sẽ có thể mở email và thực hiện các hành động khác nhau trên chúng.

### 5.1 Thư mục

Trong ERPNext, bạn có thể liên kết nhiều Tài khoản Email với một Người dùng duy nhất. Để chuyển sang Hộp thư đến của một tài khoản email khác và truy cập các thư mục khác như Email đã gửi, Thư rác, Thùng rác, hãy nhấp vào tùy chọn Email Inbox ở thanh bên trái.

<img class="screenshot" alt="Email Folders" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-folders.png">

### 5.2 Hành động

Trên các email trong hộp thư đến, bạn có thể thực hiện các hành động khác nhau như Trả lời, Chuyển tiếp, Đánh dấu là Thư rác hoặc Thùng rác.

<img class="screenshot" alt="Email Actions" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-actions.png">

### 5.3 Liên kết lại

Bạn có thể liên kết lại một email với một tài liệu như Issue, Khách hàng tiềm năng, Cơ hội, v.v. dựa trên ngữ cảnh của email. Chọn loại tài liệu và tài liệu để liên kết email vào.

<img class="screenshot" alt="Make from Email" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/make-from-email.png">

### 6. Các chủ đề liên quan
1. [Tài khoản Email](email-account.md)
1. [Gửi Email](sending-email.md)
1. [Tên miền Email](email-domain.md)