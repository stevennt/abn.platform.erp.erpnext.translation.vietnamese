<!-- add-breadcrumbs -->
# Gửi Email từ bất kỳ Tài liệu nào

Trong ERPNext, bạn có thể gửi bất kỳ tài liệu nào dưới dạng email (kèm theo tệp đính kèm PDF) bằng cách nhấp vào **Menu > Email** sau khi mở bất kỳ tài liệu nào.

<img class="screenshot" alt="Send Email" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/send-email.gif">

**Lưu ý:** Bạn phải thiết lập các [Tài khoản Email](/docs/v16/user/manual/en/setting-up/email/email-account) gửi đi để thực hiện việc này.

Sau khi bạn nhấp vào gửi, email sẽ được thêm vào hàng đợi email. Nó sẽ ở trạng thái Đang gửi (Sending) cho đến khi được Gửi (Sent). Trạng thái của email được hiển thị trong hàng đợi, nếu việc gửi thất bại, bạn có thể gửi lại bằng cách nhấp vào **Gửi ngay (Send Now)**.

![Email Queue](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-queue.png)

Các tùy chọn sau đây có sẵn khi gửi Email.

* **CC**: Bản sao (Carbon Copy) của email. Hữu ích khi bạn muốn giữ ai đó trong luồng hội thoại nhưng không muốn gửi email trực tiếp cho họ.
* **BCC**: Bản sao kín (Blind Carbon Copy) tương tự như CC nhưng những người khác trong luồng email sẽ không thể thấy rằng email cũng được gửi cho những người nhận BCC. Điều này hữu ích để ẩn địa chỉ email của một số người nếu bạn đang gửi email cho nhiều người không nhất thiết phải biết nhau.
* **Email Template**: Bạn có thể tạo các mẫu thiết lập sẵn để gửi các phản hồi tiêu chuẩn. Các Mẫu Email đã có sẵn trong hệ thống cho Thông báo gửi hàng, Thông báo trạng thái nghỉ phép và Thông báo phê duyệt nghỉ phép. Bạn có thể thiết lập Mẫu Email mặc định thông qua [Tùy chỉnh biểu mẫu](/docs/v16/user/manual/en/customize-erpnext/customize-form).
* **Send me a copy**: Tùy chọn này sẽ gửi một bản sao đến địa chỉ email của bạn. Nó hữu ích để đảm bảo rằng email đã được gửi mà không có bất kỳ lỗi nào.
* **Send Read Receipt**: Tích vào ô này sẽ gửi cho bạn một thông báo nếu người nhận đã đọc email. Trong trường hợp có nhiều người nhận, ngay cả khi chỉ có một người đã đọc email, bạn cũng sẽ nhận được thông báo.
* **Attach Document Print**: Đính kèm tệp PDF của tài liệu mà bạn đang gửi qua email.
* **Select Attachments**: Có thể thêm bất kỳ tệp đính kèm bổ sung nào tại đây.

Hai trường sau đây là các trường xuất hiện trên màn hình in:

![Email Print Options](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/email-print-options.png)

* **Select Print Format**: Mẫu in của tài liệu. Tìm hiểu thêm về Mẫu in [tại đây](/docs/v16/user/manual/en/setting-up/print/print-format).
* **Select Languages**: Ngôn ngữ mà tệp PDF sẽ được tạo.

### Các chủ đề liên quan
1. [Email Domain](/docs/v16/user/manual/en/setting-up/email/email-domain)
1. [Email Account](/docs/v16/user/manual/en/setting-up/email/email-account)
1. [Email Inbox](/docs/v16/user/manual/en/setting-up/email/email-inbox)