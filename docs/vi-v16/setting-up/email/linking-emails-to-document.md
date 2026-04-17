<!-- add-breadcrumbs -->
# Liên kết Email với Tài liệu

**Một email có thể được liên kết với nhiều tài liệu trong ERPNext.**

Việc này có thể được thực hiện theo hai cách sau:

- Tổng hợp Email trong Liên hệ (Contact), Khách hàng (Customer), Nhà cung cấp (Supplier).
- Liên kết Email tự động.

## 1. Tổng hợp Email cho Khách hàng và Nhà cung cấp

Việc Tổng hợp Email diễn ra trong Liên hệ, Khách hàng và Nhà cung cấp. Tất cả các Email được gửi hoặc nhận từ một Liên hệ có thể được xem trong Dòng thời gian (Timeline) của Liên hệ đó cũng như được liên kết với Dòng thời gian của Khách hàng hoặc Nhà cung cấp tương ứng. Để bật tính năng Tổng hợp Email, hãy thực hiện các bước sau:

1. Trong một Liên hệ, hãy thêm các Liên kết (Links) cho Khách hàng hoặc Nhà cung cấp tương ứng.

    <img class="screenshot" alt="Add Customer/Supplier in Contact" src="../assets/img/setup/email/contact-link.png">

2. Bây giờ, khi một Email được gửi đến hoặc nhận từ Liên hệ có liên kết với Khách hàng hoặc Nhà cung cấp, email đó sẽ được liên kết với Khách hàng hoặc Nhà cung cấp được đề cập trong phần Liên kết của Liên hệ.

    <img class="screenshot" alt="With Filters" src="../assets/img/setup/email/email_aggregation.gif">

## 2. Liên kết Email tự động với Tài liệu

Liên kết Email tự động sẽ liên kết một Email với Tài liệu được chỉ định thông qua Địa chỉ Email duy nhất được hệ thống tạo ra cho tài liệu đó. Nếu một Email được gửi hoặc nhận bằng Địa chỉ Email duy nhất này, hệ thống sẽ liên kết Email đó với Tài liệu.

1. Bật Liên kết Email tự động trong Tài khoản Email (Email Account). Tính năng này chỉ có thể được sử dụng với một Tài khoản Email tại một thời điểm.

    <img class="screenshot" alt="Add Customer/Supplier in Contact" src="../assets/img/setup/email/enable_email_link.png">

2. Sau khi tính năng này được bật, bạn sẽ thấy một ID Email duy nhất được tạo ra bằng cách sử dụng ID Email được đề cập trong Tài khoản Email.

3. Bây giờ bạn có thể sao chép ID Email bằng cách nhấp vào nó và bạn có thể gửi hoặc nhận Email bằng ID Email duy nhất này. Nếu một Email chứa ID Email duy nhất này trong phần Người nhận (Recipients), Cc hoặc Bcc, hệ thống sẽ liên kết Email đó với Tài liệu đã được chỉ định.

    <img class="screenshot" alt="Add Customer/Supplier in Contact" src="../assets/img/setup/email/email_link.gif">

### 3. Các chủ đề liên quan
1. [Báo cáo Email tự động](../user/manual/en/setting-up/email/auto-email-reports)
1. [Gửi Email từ bất kỳ Tài liệu nào](../user/manual/en/setting-up/email/sending-email)
1. [Theo dõi Tài liệu](../user/manual/en/setting-up/email/document-follow)


{next}