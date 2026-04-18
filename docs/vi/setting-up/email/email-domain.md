<!-- add-breadcrumbs -->
# Tên miền Email

**Tên miền email là tên của mạng/dịch vụ mà bạn đang sử dụng cho tài khoản email của mình.**

Bạn có thể bỏ qua bước này và chuyển thẳng đến phần tạo [Tài khoản Email](email-account.md) nếu bạn đang sử dụng một trong các dịch vụ được liệt kê [tại đây](email-inbox.md#2-create-an-email-domain).

Bạn có thể cấu hình Tên miền Email trong ERPNext để thiết lập dễ dàng cho tất cả các Tài khoản Email. Để tìm cài đặt Tên miền Email, hãy đi tới:

> Trang chủ > Thiết lập > Tên miền Email

**Tên miền Email của tôi là gì?:** Bạn có thể đã mua dịch vụ Email từ nhà cung cấp dịch vụ internet hoặc nhà cung cấp dịch vụ IT của mình. Ví dụ: nếu bạn truy cập hộp thư doanh nghiệp của mình với URL như http://mail.yourcompany.com, thì yourcompany.com chính là tên miền email của bạn.

Nếu bạn muốn gửi và nhận email trên tài khoản ERPNext của mình, bạn cần thiết lập đúng tên miền email. Bạn có thể đang sử dụng các dịch vụ thư miễn phí như GMail hoặc Yahoo. Trong trường hợp này, bạn không cần tạo tên miền, thay vào đó hãy chọn một nhà cung cấp dịch vụ từ danh sách. Tuy nhiên, bạn có thể phải cho phép quyền truy cập vào tài khoản GMail của mình cho ERPNext.

ERPNext tạo sẵn một tên miền email mẫu sử dụng example.com để bạn tham khảo. Bạn nên thêm tên miền mới của mình nếu muốn sử dụng nó trong tài khoản ERPNext.

<img class="screenshot" alt="Email Domain" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-domain.png">

## 1. Cách tạo một Tên miền Email
1. Đi tới danh sách Tên miền Email, nhấn vào Mới.
1. Nhập Địa chỉ Email Mẫu. Đây là nơi bạn nhập địa chỉ email doanh nghiệp của mình. Ví dụ: nếu ID email của bạn là yourname@yourcompanyname.com, bạn nên nhập địa chỉ này.
1. Máy chủ Email. Đây là URL của máy chủ thư hoặc dịch vụ email mà bạn đã mua. Ví dụ: nó có thể là mail.yourcompany.com hoặc imap.yourcompany.com.
1. Sử dụng IMAP. IMAP và POP là hai dịch vụ được hầu hết các máy chủ thư sử dụng cho email đến. Nếu máy chủ Email của bạn cho phép dịch vụ IMAP cho các email đến, hãy để tùy chọn này được chọn. Nếu không, hãy bỏ chọn.

1. Sử dụng SSL. Nếu máy chủ thư của bạn sử dụng giao thức truyền thông SSL (Secure Socket Layer), hãy để tùy chọn này được chọn.

    **Tôi có SSL không?:** Bạn có thể đã mua chứng chỉ SSL từ nhà cung cấp dịch vụ IT và họ có thể đã thiết lập SSL cho máy chủ thư của bạn. Nếu bạn đang sử dụng 'https' khi truy cập máy chủ thư qua trình duyệt, thì có thể bạn đã có thiết lập SSL.

1. Sử dụng SSL cho Email đi. Nếu máy chủ thư của bạn sử dụng SSL cho email đi, hãy bật tùy chọn này để sử dụng rõ ràng SSL cho các email gửi đi. Mặc định là cổng 465.

1. Thêm Email đi vào Thư mục Đã gửi. Nếu bạn không sử dụng các máy chủ thư tiêu chuẩn được cung cấp bởi GMail và các dịch vụ tương tự, bạn có thể cần bật tùy chọn này để thêm tất cả các email gửi đi vào hộp thư đến của tài khoản email. (Khuyến nghị cho các máy chủ email như Zimbra và CPanel).

1. Giới hạn Đính kèm (MB). Bạn có thể giới hạn kích thước của các tệp đính kèm trong email được gửi từ ERPNext.

1. SMTP Server là địa chỉ dịch vụ email gửi đi của máy chủ email của bạn.

1. Tích vào Sử dụng TLS nếu dịch vụ SMTP của bạn hỗ trợ TLS để bảo mật.

1. Cổng mặc định. Dịch vụ SMTP thường được thiết lập trên cổng 25. Nếu máy chủ email của bạn được thiết lập trên một số cổng khác, bạn có thể thiết lập tại đây.

### 1.1 Sau khi Lưu tên miền

Sau khi bạn nhấn Lưu, các cài đặt này sẽ được ERPNext xác thực và Tên miền Email sẽ được Lưu. Đôi khi việc này có thể mất vài giây và bạn có thể phải chờ đợi. Tên miền email này sau đó sẽ có sẵn trong một danh sách thả xuống gọi là Domain trong màn hình Tài khoản Email.

![Email domain in email account](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-domain1.png)

#### Đã nhập mọi thứ nhưng vẫn không thể thiết lập Tên miền Email?

Nếu bạn đã nhập và xác minh các cài đặt trên mà vẫn không thể thiết lập Tên miền Email, bạn có thể liên hệ với bộ phận hỗ trợ ERPNext trong tài khoản của mình để được trợ giúp.

### 2. Các chủ đề liên quan
1. [Tài khoản Email](email-account.md)
1. [Hộp thư Email](email-inbox.md)