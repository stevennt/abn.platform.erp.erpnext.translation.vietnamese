<!-- add-breadcrumbs -->
# Chiến dịch Email

**Một Chiến dịch Email là một tập hợp các email được gửi một cách phối hợp đến các khách hàng tiềm năng hoặc liên hệ theo một lịch trình cụ thể.**

Chiến dịch Email vẫn là một trong những cách hiệu quả nhất để tiếp cận Khách hàng, Liên hệ hoặc Khách hàng tiềm năng của bạn và giữ chân họ. Ví dụ, bạn có thể thiết lập các Chiến dịch Email để giới thiệu sản phẩm của mình cho khách hàng, với mỗi email sẽ tiết lộ một tính năng thú vị của sản phẩm.

Để tạo một Chiến dịch Email, hãy đi tới:

 > Trang chủ > CRM > Chiến dịch > Chiến dịch Email

## 1. Điều kiện tiên quyết

Trước khi tạo và sử dụng Chiến dịch Email, các mục sau đây cần được tạo trước:

* [Chiến dịch](../CRM/campaign.md)
* [Khách hàng tiềm năng](../CRM/lead.md) hoặc [Liên hệ](../CRM/contact.md) hoặc [Nhóm Email](../CRM/email_group.md)

## 2. Cách tạo một Chiến dịch Email

1. Đi tới danh sách Chiến dịch Email, nhấn vào Mới.
2. Chọn [Chiến dịch](../CRM/campaign.md) mà bạn muốn thiết lập Chiến dịch Email.
3. Thiết lập 'Ngày bắt đầu' cho Chiến dịch Email.
4. Trong 'Chiến dịch Email dành cho', chọn xem bạn muốn thiết lập Chiến dịch Email cho một Khách hàng tiềm năng, một Liên hệ hay cho một Nhóm Email để gửi đến nhiều liên hệ email.
5. Trong 'Người nhận', chọn Khách hàng tiềm năng, Liên hệ hoặc Nhóm Email tương ứng mà bạn muốn bắt đầu Chiến dịch Email.
6. Trong 'Người gửi', chọn người dùng trong hệ thống sẽ là người gửi các email.
7. Lưu

    ![Email Campaign](https://docs.erpnext.com/docs/v16/assets/img/crm/email-campaign.png)

    Chiến dịch Email trên dành cho Chiến dịch sau:

    ![Campaign Schedule](https://docs.erpnext.com/docs/v16/assets/img/crm/campaign-email-schedule.png)

    **Lưu ý**: Trường **Gửi sau (ngày)** trong Chiến dịch quy định ngày mà email sẽ được gửi so với **Ngày bắt đầu** của **Chiến dịch Email**. Lưu ý 'Ngày kết thúc' trong Chiến dịch Email ở trên. Nó là '26-07-2019', tức là 4 ngày sau 'Ngày bắt đầu' '22-07-2029', vì Lịch trình Chiến dịch kết thúc vào ngày thứ 4.

### 2.1 Tạo nhiều Chiến dịch Email cho một Chiến dịch

Bạn cũng có thể tạo các Chiến dịch Email mới cho các Khách hàng tiềm năng hoặc Liên hệ khác nhau cho cùng một Chiến dịch thông qua Trang tổng quan Chiến dịch.

1. Đi tới Chiến dịch mà bạn muốn tạo các Chiến dịch Email.
2. Nhấp vào dấu + trước mục Chiến dịch Email để tạo một Chiến dịch Email mới cho Chiến dịch đó.

    ![Email Campaigns from Dashboard](https://docs.erpnext.com/docs/v16/assets/img/crm/campaign-dashboard.png)

## 3. Các tính năng

### 3.1 Liên kết liên lạc

Khi email được gửi đến các khách hàng tiềm năng hoặc liên hệ tương ứng, các Liên lạc sẽ được liên kết với tài liệu Chiến dịch Email. Bạn có thể xem tất cả các email đã được gửi trong tài liệu của mình.

![Linked Communication](https://docs.erpnext.com/docs/v16/assets/img/crm/email-campaign-linked-comm.png)

### 3.2 Hủy đăng ký Chiến dịch Email

Nếu một khách hàng tiềm năng hoặc liên hệ không muốn tiếp tục nhận email liên quan đến chiến dịch, họ có thể hủy đăng ký Chiến dịch Email thông qua liên kết hủy đăng ký được gửi kèm trong email.

![Unsubscribe Link](https://docs.erpnext.com/docs/v16/assets/img/crm/unsubscribe-link.png)

Khi khách hàng tiềm năng hoặc liên hệ hủy đăng ký, trạng thái của tài liệu Chiến dịch Email sẽ chuyển thành 'Đã hủy đăng ký'.

![Unsubscribed](https://docs.erpnext.com/docs/v16/assets/img/crm/email-campaign-unsubscribed.png)

### 3.3 Sử dụng các trường Khách hàng tiềm năng hoặc Liên hệ trong Mẫu Email

 Mẫu Email có ngữ cảnh của tài liệu mà bạn đã chỉ định trong trường 'Chiến dịch Email dành cho'. Nếu bạn muốn hiển thị các trường từ tài liệu Khách hàng tiềm năng hoặc Liên hệ của mình trong Mẫu Email, bạn sẽ phải sử dụng `doc.fieldname` cho trường đó.
 Ví dụ, nếu 'Chiến dịch Email dành cho' là 'Liên hệ', bạn có thể đề cập đến 'tên' (first name) của Liên hệ của bạn là `doc.first_name` trong Mẫu Email như hiển thị dưới đây:

<img class="screenshot" alt="Email Template Document" src="https://docs.erpnext.com/docs/v16/assets/img/crm/email-template-doc.png">

Khi đó, các email được gửi đi sẽ trông như thế này:

<img class="screenshot" alt="Email Campaign Doc Data" src="https://docs.erpnext.com/docs/v16/assets/img/crm/email-campaign-doc-data.png">

### 3.4 Chỉ báo trạng thái

Trạng thái cho biết tình trạng của Chiến dịch Email, các Trạng thái khác nhau bao gồm:

- **Đã lên lịch**: Khi Chiến dịch Email vẫn chưa bắt đầu nhưng đã được lên lịch vào một 'Ngày bắt đầu' trong tương lai.
- **Đang tiến hành**: Chiến dịch sẽ được đánh dấu là 'Đang tiến hành' trong khoảng thời gian từ 'Ngày bắt đầu' đến 'Ngày kết thúc' của chiến dịch.
- **Hoàn thành**: Sau 'Ngày kết thúc' của chiến dịch, trạng thái sẽ được chuyển thành 'Hoàn thành'.
- **Đã hủy đăng ký**: Khi Khách hàng tiềm năng hoặc Liên hệ hủy đăng ký khỏi Chiến dịch.

![Email Campaign Status](https://docs.erpnext.com/docs/v16/assets/img/crm/email-campaign-status.png)

## 4. Các chủ đề liên quan
1. [Chiến dịch](../CRM/campaign.md)
1. [Khách hàng tiềm năng](../CRM/lead.md)
1. [Liên hệ](../CRM/contact.md)

Tiếp theo: [Bản tin](../CRM/newsletter.md)