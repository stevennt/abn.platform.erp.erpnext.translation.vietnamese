<!-- add-breadcrumbs -->
# Tài khoản Email

**Bạn có thể đồng bộ hóa tài khoản email của mình với ERPNext để gửi và nhận email từ ERPNext.**

Bạn có thể quản lý nhiều Tài khoản Email gửi và nhận trong ERPNext. Phải có ít nhất một tài khoản gửi mặc định và một tài khoản nhận mặc định. Nếu bạn đang sử dụng ERPNext cloud, email gửi mặc định sẽ do chúng tôi thiết lập.

Để truy cập Tài khoản Email, hãy đi tới:
> Home > Settings > Email Account

## 1. Điều kiện tiên quyết
Trước khi tạo một Tài khoản Email, bạn cần có một [Email Domain](email-domain.md). Tuy nhiên, bạn có thể bỏ qua bước tạo Email Domain nếu bạn đang sử dụng một trong các dịch vụ được liệt kê [tại đây](email-inbox.md#2-create-an-email-domain).

## 2. Cách tạo Tài khoản Email
1. Đi tới danh sách Email Account, nhấn vào New.
1. Nhập địa chỉ email kèm theo tên miền. [Domains](email-domain.md) cần phải được tạo để có thể tạo tài khoản email.
    Bạn không cần tạo domain nếu bạn đang đồng bộ hóa email từ một số nhà cung cấp nhất định được liệt kê [tại đây](email-inbox.md#2-create-an-email-domain).
1. Nhập mật khẩu tài khoản email.
1. Lưu.
Nếu thông tin đăng nhập chính xác, tài khoản email sẽ được đồng bộ hóa.

> Lưu ý: Đối với một số dịch vụ như Gmail, bạn có thể cần bật cài đặt để cho phép các ứng dụng kém an toàn hơn (less secure apps).

### 2.1 Các tùy chọn bổ sung khi tạo Tài khoản Email
1. **Use Different Email Login ID**: Sử dụng ID đăng nhập email và mật khẩu thay thế để truy cập tài khoản này. Ví dụ: nếu bạn có notifications@example.com và bạn muốn người dùng truy cập email này bằng một ID email khác, họ nên tích vào ô này. Người nhận sẽ thấy notifications@example.com là người gửi.
1. **Awaiting password**: Nếu bạn đang tạo tài khoản này thay mặt cho ai đó và chưa biết mật khẩu, hãy tích vào ô này. Khi người dùng kia đăng nhập, họ sẽ được yêu cầu nhập mật khẩu.
1. **Use ASCII encoding for password**: Tích vào đây sẽ sử dụng mã hóa ASCII cho mật khẩu.

## 3. Cấu hình Tài khoản Email
### 3.1 Tài khoản Email mặc định

ERPNext sẽ tạo sẵn các mẫu cho một loạt các tài khoản email theo mặc định. Không phải tất cả chúng đều được kích hoạt. Để kích hoạt, bạn phải thiết lập các chi tiết tài khoản email hợp lệ.

Có hai loại tài khoản email: gửi đi và nhận về. Tài khoản email gửi đi sử dụng dịch vụ SMTP để gửi email và email được lấy từ hộp thư của bạn bằng IMAP hoặc POP. Hầu hết các nhà cung cấp email như Gmail, Outlook hoặc Yahoo đều cung cấp các dịch vụ này.

<img class="screenshot" alt="Defining Criteria" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-account-list.png">

### 3.2 Tài khoản Email nhận

Để thiết lập Tài khoản Email nhận, hãy tích vào **Enable Incoming** và thiết lập các cài đặt POP3 của bạn; nếu bạn đang sử dụng dịch vụ email phổ biến, các cài đặt này sẽ được thiết lập sẵn cho bạn.

<img class="screenshot" alt="Incoming EMail" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-account-incoming.png">

Các tùy chọn sau đây có sẵn cho email nhận:

* **Use IMAP**
* **Use SSL**
* **Attachment Limit**
* **Default Incoming**: Nếu được tích, tất cả các phản hồi gửi đến công ty của bạn (ví dụ: replies@yourcomany.com) sẽ được chuyển đến tài khoản này.
* **Email Sync Option**: Lựa chọn đồng bộ hóa tất cả hoặc chỉ những email chưa xem.
* **Initial Sync Count**: Số lượng email cần đồng bộ hóa trong lần đầu tiên.

#### Đính kèm Email vào Tài liệu (Appending Emails To Documents)
Tính năng này sẽ tạo các tài liệu khi một email được gửi đến một tài khoản email cụ thể. Ví dụ: bạn có thể đính kèm support@example.com vào DocType Issue. Khi thực hiện việc này, bất cứ khi nào có email được gửi đến support@example.com, hệ thống sẽ tạo một Issue cho email đó. Tương tự, nếu bạn liên kết jobs@example.com, khi email được gửi đến jobs@example.com, một tài liệu Job Applicant sẽ được tạo.

Kích hoạt Automatic Linking trong Documents sẽ liên kết email với các tài liệu, để biết thêm chi tiết [nhấn vào đây](linking-emails-to-document.md).

### 3.3 Thông báo cho các tin nhắn chưa được phản hồi

Nếu bạn muốn ERPNext thông báo cho bạn nếu một email không được phản hồi trong một khoảng thời gian nhất định, bạn có thể thiết lập **Notify if Unreplied**. Tại đây, bạn có thể thiết lập số phút chờ đợi trước khi thông báo được gửi đi và thông báo đó sẽ được gửi cho ai.

<img class="screenshot" alt="Incoming EMail" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-account-unreplied.png">

#### Thiết lập Điều kiện Nhập cho Nhập Email (Setting Import Conditions for Email Import)

Tài khoản Email cho phép bạn thiết lập các điều kiện dựa trên dữ liệu của email nhận được. Email sẽ chỉ được nhập vào ERPNext nếu tất cả các điều kiện đều đúng. Ví dụ: nếu bạn muốn nhập một email nếu tiêu đề là "Some important email", bạn nhập `doc.subject == "Some important email"` vào ô điều kiện. Bạn cũng có thể thiết lập các điều kiện phức tạp hơn bằng cách kết hợp chúng, như được hiển thị trong ảnh chụp màn hình sau.

<img class="screenshot" alt="Incoming EMail Conditions" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-account-incoming-conditions.png">

### 3.4 Tài khoản Email gửi

Tất cả email được gửi từ hệ thống, dù là do người dùng gửi cho một liên hệ, qua thông báo hoặc qua email giao dịch, đều sẽ được gửi từ một Tài khoản Email gửi.

Để thiết lập một Tài khoản Email gửi, hãy tích vào **Enable Outgoing** và thiết lập các cài đặt máy chủ SMTP của bạn; nếu bạn đang sử dụng dịch vụ email phổ biến, các cài đặt này sẽ được thiết lập sẵn cho bạn.

<img class="screenshot" alt="Outgoing EMail" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-account-sending.png">

Các tùy chọn sau đây có sẵn cho email gửi:

* **Use TLS**
* **Port**
* **Disable SMTP server authentication**
* **Add Signature**: Chữ ký mặc định được đính kèm vào cuối mỗi email.
* **Default Outgoing**: Các thông báo và email hàng loạt sẽ được gửi từ máy chủ gửi này.
* **Always use Account's Email Address as Sender**: Địa chỉ email của tài khoản này sẽ được ghi nhận là người gửi cho các email gửi đi.
* **Send unsubscribe message in email**: Gửi một liên kết để hủy đăng ký...