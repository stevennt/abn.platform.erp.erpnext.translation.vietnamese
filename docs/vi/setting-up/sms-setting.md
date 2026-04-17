<!-- add-breadcrumbs -->
# Cài đặt SMS

**Bạn có thể đăng ký với một nhà cung cấp SMS để gửi tin nhắn SMS đến các số điện thoại di động.**

Để tích hợp SMS vào ERPNext, hãy liên hệ với một Nhà cung cấp Cổng SMS (SMS Gateway Provider) có cung cấp HTTP API. Họ sẽ tạo một tài khoản cho bạn và cung cấp tên đăng nhập cũng như mật khẩu duy nhất.

Để truy cập cài đặt SMS, hãy đi đến:
> Trang chủ > Cài đặt > Cài đặt SMS

Để cấu hình Cài đặt SMS trong ERPNext, hãy tìm hiểu HTTP API của họ (tài liệu mô tả phương thức truy cập giao diện SMS của họ từ các ứng dụng bên thứ ba). Trong tài liệu này, bạn sẽ nhận được một URL được sử dụng để gửi SMS bằng yêu cầu HTTP. Sử dụng URL này, bạn có thể cấu hình Cài đặt SMS trong ERPNext.

Ví dụ về URL Cổng SMS:

    http://instant.smses.com/web2sms.php?username=<USERNAME>&password;=<PASSWORD>&to;=<MOBILENUMBER>&sender;=<SENDERID>&message;=<MESSAGE>


<img class="screenshot" alt="SMS Setting 2" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/sms-settings2.jpg">

> Lưu ý: Đối với URL Cổng SMS, chỉ bao gồm chuỗi ký tự trước dấu "?".

Ví dụ:

    http://instant.smses.com/web2sms.php?username=abcd&password;=abcd&to;=9900XXXXXX&sender;
    =DEMO&message;=THIS+IS+A+TEST+SMS

URL trên sẽ gửi SMS từ tài khoản abcd đến số điện thoại 9900XXXXXX với ID người gửi là DEMO và nội dung tin nhắn là "THIS IS A TEST SMS".

Lưu ý rằng một số tham số trong URL là cố định. Bạn sẽ nhận được các giá trị cố định từ Nhà cung cấp SMS của mình như tên đăng nhập, mật khẩu, v.v. Các giá trị cố định này nên được nhập vào bảng Tham số cố định (Static Parameters).

<img class="screenshot" alt="SMS Setting" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/sms-settings1.png">

### Các chủ đề liên quan
1. [Tài khoản Email](/docs/v13/user/manual/en/setting-up/email/email-account)
1. [Thông báo](/docs/v13/user/manual/en/setting-up/notifications)