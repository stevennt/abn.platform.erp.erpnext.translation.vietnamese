<!-- add-breadcrumbs -->
# Thông báo

**Bạn có thể cấu hình nhiều loại thông báo khác nhau trong hệ thống để nhắc nhở về các hoạt động quan trọng.**

1. Ngày hoàn thành của một Công việc (Task).
2. Ngày giao hàng dự kiến của một Đơn bán hàng.
3. Ngày thanh toán dự kiến.
4. Nhắc nhở theo dõi (follow up).
5. Nếu một Đơn hàng có giá trị lớn hơn một mức cụ thể được nhận hoặc gửi.
6. Thông báo hết hạn cho một Hợp đồng.
7. Hoàn thành/Thay đổi trạng thái của một Công việc (Task).

Để truy cập thiết lập thông báo, hãy đi tới:

> Home > Settings > Notification

## 1. Thiết lập một Cảnh báo

Để thiết lập một Thông báo:

1. Chọn DocType mà bạn muốn theo dõi các thay đổi.
2. Xác định các sự kiện bạn muốn theo dõi trong mục Send Alert On. Các sự kiện bao gồm:
    1. New: Khi một tài liệu mới thuộc loại đã chọn được tạo.
    2. Save/Submit/Cancel: Khi một tài liệu thuộc loại đã chọn được Lưu, Xác nhận hoặc Hủy.
    4. Days Before/Days After: Kích hoạt cảnh báo này vài ngày trước hoặc sau **Ngày tham chiếu (Reference Date).** Để thiết lập số ngày, hãy đặt **Days Before or After**. Điều này hữu ích trong việc nhắc nhở về các hạn chót sắp tới hoặc nhắc nhở bạn theo dõi một số Khách hàng tiềm năng hoặc Báo giá nhất định.
    3. Value Change: Khi một giá trị cụ thể trong loại đã chọn thay đổi.
    1. Method: Gửi thông báo khi một phương thức cụ thể được kích hoạt. Ví dụ: before_insert.
    1. Custom: Gửi thông báo đến một [Tài khoản Email](/docs/v13/user/manual/en/setting-up/email/email-account) đã chọn.
3. Thiết lập các Điều kiện (Conditions) bổ sung nếu cần.
4. Thiết lập người nhận của cảnh báo này. Người nhận có thể là một trường của tài liệu hoặc một danh sách các Địa chỉ Email cố định.
5. Soạn thảo nội dung tin nhắn.
1. Lưu.


### 1.1 Thiết lập Tiêu đề
Bạn có thể lấy dữ liệu của một trường cụ thể bằng cách sử dụng `doc.[field_name]`. Để sử dụng nó trong tiêu đề/tin nhắn, bạn phải bao quanh nó bằng `{% raw %}{{ }}{% endraw %}`. Đây được gọi là các thẻ [Jinja](http://jinja.pocoo.org/). Ví dụ, để lấy tên của một tài liệu, bạn sử dụng `{% raw %}{{ doc.name }}{% endraw %}`. Ví dụ sau đây sẽ gửi một email khi Lưu một Công việc (Task) với Tiêu đề là "TASK#### đã được tạo"

<img class="screenshot" alt="Setting Subject" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/notifications/email-alert-subject.png">

### 1.2 Thiết lập Điều kiện

Thông báo cho phép bạn thiết lập các điều kiện dựa trên dữ liệu trường trong tài liệu của mình. Ví dụ, nếu bạn muốn nhận một Email nếu một Khách hàng tiềm năng (Lead) được Lưu với trạng thái là "Interested", bạn nhập `doc.status == "Interested"` vào ô điều kiện. Bạn cũng có thể thiết lập các điều kiện phức tạp hơn bằng cách kết hợp chúng.

<img class="screenshot" alt="Setting Condition" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/notifications/email-alert-condition.png">

Ví dụ trên sẽ gửi một Thông báo khi một Công việc (Task) được Lưu với trạng thái "Open" và "Ngày kết thúc dự kiến" của Công việc đó là ngày hiện tại hoặc trước ngày nó được Lưu.


### 1.3 Thiết lập Tin nhắn

Bạn có thể sử dụng cả Thẻ Jinja (`{% raw %}{{ doc.[field_name] }}{% endraw %}`) và các thẻ HTML trong ô soạn thảo tin nhắn.

    {% raw %}<h3>Đơn hàng quá hạn</h3>

    <p>Giao dịch {{ doc.name }} đã quá Hạn thanh toán. Vui lòng thực hiện các hành động cần thiết.</p>

    <!-- show last comment -->
    {% if comments %}
    Bình luận cuối cùng: {{ comments[-1].comment }} bởi {{ comments[-1].by }}
    {% endif %}

    <h4>Chi tiết</h4>

    <ul>
    <li>Khách hàng: {{ doc.customer }}
    <li>Số tiền: {{ doc.total_amount }}
    </ul>{% endraw %}


### 1.4 Thiết lập một Giá trị sau khi Cảnh báo được thiết lập

Đôi khi để đảm bảo rằng Thông báo không bị gửi nhiều lần, bạn có thể định nghĩa một thuộc tính tùy chỉnh (thông qua Customize Form) như "Notification Sent" và sau đó thiết lập thuộc tính này sau khi cảnh báo được gửi bằng cách đặt trường **Set Property After Alert**.

Sau đó, bạn có thể sử dụng thuộc tính đó làm điều kiện trong các quy tắc **Condition** để đảm bảo email không bị gửi nhiều lần.

<img class="screenshot" alt="Setting Property in Notification" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/notifications/email-alert-subject.png">

### 1.5 Ví dụ

1. Định nghĩa Tiêu chí
    <img class="screenshot" alt="Defining Criteria" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/notifications/email-alert-1.png">

1. Thiết lập Người nhận và Tin nhắn
    <img class="screenshot" alt="Set Message" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/notifications/email-alert-2.png">


---

## 2. Thông báo Slack

Nếu bạn muốn thông báo của mình được gửi đến một kênh Slack chuyên dụng, bạn cũng có thể chọn tùy chọn "Slack" trong các tùy chọn kênh và chọn URL Slack Webhook phù hợp.

### 2.1 Slack Webhook URL

Một URL Slack webhook là một URL trỏ trực tiếp đến một kênh Slack.

Để tạo URL webhook, bạn cần tạo một Ứng dụng Slack (Slack App) mới:

1. Truy cập https://api.slack.com/slack-apps.
2. Nhấp vào "Create a Slack App".
    <img class="screenshot" alt="Set Message" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/notifications/slack_notification_1.png">

3. Đặt tên cho Ứng dụng của bạn và chọn không gian làm việc (workspace) phù hợp.
    Sau khi ứng dụng của bạn được tạo, hãy đi tới phần "Incoming Webhooks" và thêm một Webhook mới vào Workspace.
    <img class="screenshot" alt="Set Message" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/notifications/slack_notification_2.png">

4. Sao chép liên kết đã tạo, quay lại ERPNext và sử dụng nó để tạo một Slack Webhook URL mới trong Integrations > Slack Webhook URL.
    <img class="screenshot" alt="Set Message" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/notifications/slack_notification_3.png">

5. Chọn Slack và kênh Slack của bạn trong các trường channel và Slack channel trong thông báo của bạn.


### 2.2 Định dạng Tin nhắn

Không giống như tin nhắn Email, Slack không cho phép định dạng HTML.

Thay vào đó, bạn có thể sử dụng định dạng markdown: [Tài liệu Slack](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages)

Ví dụ:
    {% raw %}
    *Đơn hàng quá hạn*

    Giao dịch {{ doc.name }} đã quá Hạn thanh toán. Vui lòng thực hiện các hành động cần thiết.


    {% if comments %}
    Bình luận cuối cùng: {{ comments[-1].comment }} bởi {{ comments[-1].by }}
    {% endif %}

    *Chi tiết*