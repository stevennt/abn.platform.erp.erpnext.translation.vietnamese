<!-- add-breadcrumbs -->
# Tự động lặp lại (Auto Repeat)

Tính năng Tự động lặp lại giúp bạn tạo một số chứng từ nhất định một cách tự động trong một khoảng thời gian cụ thể.

Từ phiên bản 12, bạn có thể Tùy chỉnh bất kỳ Form nào để làm cho các chứng từ có thể **lặp lại**.

Ví dụ: Giả sử bạn áp dụng hệ thống chi phí trả trước cho một số mặt hàng. Nó yêu cầu bạn phải tạo cùng một Bút toán hàng tháng để ghi có tài khoản Chi phí trả trước và ghi nợ tài khoản Chi phí. Bạn có thể tạo Bút toán đầu tiên một cách thủ công, sau đó tạo giao dịch tự động lặp lại cho nó.

Để truy cập Tự động lặp lại, hãy đi đến:
> Trang chủ > Cài đặt > Tự động hóa > Tự động lặp lại

## 1. Cách thiết lập Tự động lặp lại

### 1.1 Tùy chỉnh Form
1. Đi đến: **Trang chủ > Tùy chỉnh > Tùy chỉnh Form > Tùy chỉnh Form**.
2. Chọn form mà bạn muốn cho phép tạo các chứng từ có thể lặp lại.
3. Tích chọn 'Cho phép Tự động lặp lại' (Allow Auto Repeat) để cho phép tạo các chứng từ có thể lặp lại cho Form đó. Điều này là cần thiết để loại DocType chứng từ xuất hiện trong trường Tài liệu tham chiếu (Reference Document) dưới DocType Tự động lặp lại.

  ![Allow Auto Repeat](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/automation/allow-auto-repeat.png)

### 1.2 Thiết lập Tự động lặp lại
1. Đi đến **Trang chủ > Cài đặt > Tự động hóa > Tự động lặp lại > Mới**.
2. Chọn Loại Tài liệu tham chiếu, chẳng hạn như Bút toán hoặc Hóa đơn bán hàng, v.v.
3. Chọn Tài liệu tham chiếu. Đây là chứng từ cụ thể mà bạn muốn lặp lại.
4. Thiết lập Ngày bắt đầu và Ngày kết thúc (tùy chọn).
   Nếu không chỉ định Ngày kết thúc, các chứng từ định kỳ sẽ được tạo, trừ khi tính năng Tự động lặp lại bị vô hiệu hóa.
5. Thiết lập Tần suất để tạo các chứng từ có thể lặp lại
   (Hàng ngày, Hàng tuần, Hàng tháng, Hàng quý, Hàng nửa năm, Hàng năm).
6. Lưu.

### 1.3 Thiết lập Tự động lặp lại trực tiếp từ chứng từ
Bạn cũng có thể thiết lập một chứng từ Tự động lặp lại bằng cách nhấp vào tùy chọn **Lặp lại** (Repeat) từ **Menu** trên Thanh công cụ.

**Lưu ý**: Nếu một chứng từ đã được thiết lập Tự động lặp lại, tùy chọn Lặp lại sẽ không khả dụng.

![Repeat in Transactions](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/automation/repeat-option.png)

Khi bạn nhấp vào Lặp lại, một thông báo yêu cầu Tự động lặp lại sẽ hiện ra. Điền đầy đủ thông tin và nhấp vào Lưu.

![Auto Repeat Prompt](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/automation/auto-repeat-prompt.png)

## 2. Các tính năng


### 2.1 Xác nhận khi tạo

Nếu loại tài liệu tham chiếu có thể Xác nhận (submittable), bạn sẽ có một tùy chọn gọi là _Xác nhận khi tạo_ (Submit on Creation). Nếu tùy chọn này được tích, chứng từ của bạn sẽ được Xác nhận ngay khi được tạo.

![Auto Repeat Submit on Creation](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/automation/submit-on-creation.png)

### 2.2 Thông báo qua Email
Nếu bạn muốn thông báo cho một số liên hệ nhất định bất cứ khi nào các chứng từ định kỳ được tạo, bạn có thể tích vào 'Thông báo qua Email' (Notify by Email) trong phần Thông báo của Tự động lặp lại. Điều này sẽ gửi các chứng từ định kỳ được tạo tự động đến các Địa chỉ Email đã chỉ định. Các trường cho việc này được giải thích dưới đây:

- **Người nhận (Recipients)**: Xác định ID Email của những người nhận email tạo chứng từ định kỳ.
- **Lấy liên hệ (Get Contacts)**: Nút này sẽ lấy các liên hệ được liên kết với chứng từ đã được thiết lập Tự động lặp lại và điền vào trường Người nhận.
- **Mẫu (Template)**: Bạn có thể chọn một Mẫu Email cho email này. Điều này cũng sẽ điền vào các trường Tiêu đề và Nội dung.
- **Tiêu đề (Subject)**: Tiêu đề cho Email của bạn (ví dụ: Việc cần làm định kỳ đã được tạo thành công).
- **Nội dung (Message)**: Nội dung được gửi trong Email.
- **Xem trước nội dung (Preview Message)**: Nút này sẽ hiển thị bản xem trước của nội dung.
- **Mẫu in (Print Format)**: Chọn một mẫu in để xác định chế độ xem chứng từ sẽ được gửi email cho khách hàng.

> **Lưu ý**: Nếu chứng từ mà bạn đang thiết lập Tự động lặp lại có thể Xác nhận, hãy đảm bảo rằng "Cho phép in bản Nháp" (Allow Print for Draft) đã được bật trong [Cài đặt in](../setting-up/print/print-settings.md) để nhận được chứng từ định kỳ mới trong Email Thông báo Tự động lặp lại. Nếu không bật tính năng này, bạn sẽ được thông báo về việc tạo chứng từ định kỳ nhưng không kèm theo chứng từ.

### 2.3 Lặp lại vào một ngày cụ thể
Nếu tần suất được thiết lập là Hàng tháng, Hàng quý, Hàng nửa năm hoặc Hàng năm, thì nó sẽ tạo các chứng từ định kỳ vào các tháng tương ứng vào cùng một ngày với 'Ngày bắt đầu' của Tự động lặp lại. Nếu bạn muốn tạo chứng từ định kỳ vào một ngày khác, bạn có thể thiết lập một trong các tùy chọn sau:

- **Lặp lại vào Ngày (Repeat on Day)**: Ngày trong tháng mà chứng từ định kỳ sẽ được tạo. Ví dụ: nếu tần suất là Hàng tháng và bạn nhập 7, thì nó sẽ tạo chứng từ định kỳ vào ngày 7 của tháng tương ứng.
- **Lặp lại vào Ngày cuối cùng của tháng (Repeat on Last Day of the Month)**: Tùy chọn này có sẵn vì ngày cuối cùng của mỗi tháng là khác nhau. Ví dụ: trong năm nhuận, ngày cuối cùng của tháng 2 là ngày 29, và là ngày 28 nếu không phải năm nhuận. Nếu bạn tích chọn tùy chọn này, nó sẽ tạo các chứng từ định kỳ vào ngày cuối cùng của các tháng tương ứng.

### 2.4 Khả năng chọn các ngày trong tuần cho Tự động lặp lại

> Được giới thiệu trong phiên bản 13

Tự động lặp lại với tần suất Hàng tuần cho phép bạn chọn các ngày mà bạn muốn các chứng từ định kỳ được tạo.

<img class="screenshot" alt="Auto Repeat Weekdays" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/automation/auto-repeat-weekdays.png">

### 2.5 Trang tổng quan

Bạn có thể xem lịch trình Tự động lặp lại trong Trang tổng quan của chứng từ Tự động lặp lại. Nếu bạn không chỉ định Ngày kết thúc, lịch trình sẽ chỉ hiển thị Ngày lập lịch tiếp theo.

![Auto Repeat Dashboard](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/automation/auto-repeat-dashboard.png)

### 2.6 Tần suất Tự động lặp lại trên thanh bên
Khi một chứng từ được thiết lập Tự động lặp lại, bạn có thể thấy tần suất Tự động lặp lại trên thanh bên.
Bạn có thể nhấp vào trạng thái để xem chứng từ Tự động lặp lại được liên kết.

![Auto Repeat Frequency](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/automation/auto-repeat-frequency.png)

### 2.7 Vô hiệu hóa Tự động lặp lại
Nếu bạn tích vào trường này, nó sẽ ngừng tạo các chứng từ định kỳ và hủy liên kết chứng từ Tự động lặp lại khỏi Tài liệu tham chiếu.

{next}