<!-- add-breadcrumbs -->
# Hội viên

DocType Hội viên cho phép bạn ghi lại các chi tiết hội viên cho **Thành viên**.

Hội viên là một thuật ngữ dùng để chỉ bất kỳ tổ chức nào cho phép mọi người đăng ký, và thường yêu cầu họ phải trả phí hội viên hoặc "phí đăng ký".

## 1. Cách tạo Hội viên

Để tạo Hội viên mới, hãy đi tới:

> Phi lợi nhuận > Hội viên > Mới

<img class="screenshot" alt="Membership" src="https://docs.erpnext.com/docs/v13/assets/img/non_profit/membership/membership.png">

**Thành viên:** Thành viên là một trường liên kết lấy thông tin chi tiết của thành viên từ DocType Thành viên.

**Trạng thái hội viên:** Trạng thái hội viên là một trường lựa chọn bao gồm Mới, Hiện tại, Hết hạn, Đang chờ và Đã hủy. Trạng thái Hết hạn sẽ tự động được cập nhật khi thời hạn hội viên kết thúc.

**Phần Chi tiết ngày hội viên:** Phần này chứa thông tin liên quan đến ngày bắt đầu hội viên, ngày kết thúc và ngày trở thành thành viên.

**Chi tiết thanh toán:** Phần này chứa các chi tiết liên quan đến thanh toán. Nếu người đó đã thanh toán phí hội viên, ô đã thanh toán sẽ được đánh dấu, nếu không thì để trống. Số tiền được lấy dựa trên loại hội viên.

## 2. Các tính năng

## 2.1 Tạo Hóa đơn

Nếu bạn đã đánh dấu _Cho phép lập hóa đơn_ trong Cài đặt Hội viên, bạn sẽ thấy một nút để tạo Hóa đơn bán hàng từ biểu mẫu Hội viên.

## 3. Thanh toán Hội viên bằng RazorPay

Đối với các khoản thanh toán hội viên định kỳ, bạn có thể thiết lập đăng ký Razorpay cho các thành viên. Bạn có thể tìm thấy hướng dẫn thiết lập Razorpay [tại đây](/docs/v13/user/manual/en/erpnext_integration/razorpay-integration)

> Lưu ý: Tính năng này chỉ có sẵn từ Phiên bản 13 trở lên.

Bạn có thể làm theo các bước được liệt kê dưới đây để thiết lập đăng ký Razorpay cho các hội viên.

1. Thiết lập RazorPay
1. Thiết lập chi tiết thanh toán
1. Thiết lập các Gói
1. Nhập Thành viên hiện có
1. Thiết lập RazorPay Webhook
1. Thiết lập Website

## 3.1 Cài đặt Hội viên

Bạn có thể tìm thấy hướng dẫn thiết lập Razorpay [tại đây](/docs/v13/user/manual/en/erpnext_integration/razorpay-integration). Bạn có thể thiết lập thanh toán trong Cài đặt Hội viên trong mô-đun Phi lợi nhuận.

<img class="screenshot" alt="Membership" src="https://docs.erpnext.com/docs/v13/assets/img/non_profit/razorpay-enabled.png">

Việc đánh dấu _Cho phép RazorPay cho Hội viên_ sẽ hiển thị thêm cho bạn các tùy chọn cấu hình.

- **Chu kỳ thanh toán**: Đây là khoảng thời gian giữa các lần thanh toán. Bạn có thể chọn Thanh toán Hàng tháng hoặc Hàng năm.
- **Tần suất thanh toán**: Số chu kỳ thanh toán mà khách hàng sẽ bị tính phí. Ví dụ, nếu một khách hàng mua hội viên 1 năm nhưng được tính phí hàng tháng, giá trị này nên là 12.

<img class="screenshot" alt="Membership" src="https://docs.erpnext.com/docs/v13/assets/img/non_profit/membership/membership-settings.png">

Có các cấu hình khác dành cho việc Lập hóa đơn.

- **Cho phép lập hóa đơn**: Đánh dấu tùy chọn này sẽ cho phép tạo hóa đơn cho các hội viên bằng nút **Tạo Hóa đơn**.
- **Tự động tạo hóa đơn cho Biểu mẫu Web**: Nếu bạn đã thiết lập các biểu mẫu web tùy chỉnh, việc bật tùy chọn này sẽ tự động tạo Hóa đơn bán hàng khi thanh toán được chấp thuận.
- **Tạo Bút toán thanh toán**: Tự động tạo Bút toán thanh toán cho các Hóa đơn bán hàng được tạo từ Hội viên thông qua biểu mẫu web.

Việc đánh dấu _Cho phép lập hóa đơn_ sẽ cho phép bạn cấu hình Công ty và Tài khoản nợ cho các hóa đơn của mình. Đánh dấu **Tạo Bút toán thanh toán** sẽ cho phép bạn cấu hình Tài khoản thanh toán.

- **Gửi Xác nhận Hội viên**: Nếu tùy chọn này được bật, bạn sẽ có tùy chọn gửi một thông báo xác nhận về việc trở thành Hội viên cho thành viên sau khi hóa đơn đã được tạo.
- **Mẫu email**: Bạn có thể cấu hình mẫu email cho thông báo xác nhận và thiết lập tại đây.

Nếu _Gửi Xác nhận Hội viên_ được bật, bạn có thể bật _Gửi Hóa đơn kèm Email_ để gửi Hóa đơn cùng với thông tin Hội viên. Bạn cũng có thể cấu hình các mẫu in cho Hội viên và Hóa đơn riêng biệt tại đây.

## 3.2 Thiết lập các Gói

Loại hội viên tương ứng với gói RazorPay của bạn. Bạn có thể đọc thêm về Gói Hội viên [tại đây](/docs/v13/user/manual/en/non_profit/membership_type)

<img class="screenshot" alt="Membership" src="https://docs.erpnext.com/docs/v13/assets/img/non_profit/plan.png">

Khi các tùy chọn đăng ký Razorpay được kích hoạt, bạn sẽ thấy trường **ID Gói**. Đây là nơi bạn có thể thêm ID gói từ Razorpay.

> Lưu ý: Bạn phải thêm tất cả các gói đang hoạt động và các gói cũ để việc thanh toán diễn ra liền mạch.

## 3.3 Nhập Thành viên

Nếu bạn đã có sẵn các thành viên, bạn có thể nhập họ bằng [Công cụ Nhập dữ liệu](/docs/v13/user/manual/en/setting-up/data/data-import). Dưới đây là [video hướng dẫn](https://www.youtube.com/watch?v=WlGD35DM5LI) về việc này.

Bạn cần nhập thành viên với các trường sau.

1. **Tên thành viên**: Họ tên đầy đủ của thành viên
1. **Loại hội viên**: Tên của gói mà họ đăng ký
1. **Địa chỉ Email**: ID Email được sử dụng cho các giao dịch Razorpay
1. **ID Đăng ký**: ID Đăng ký được cung cấp bởi RazorPay
1. **ID Khách hàng**: ID Đăng ký được cung cấp bởi RazorPay
1. **Mã số thuế (PAN) của Thành viên**: Trường này là tùy chọn

> Lưu ý: Các đăng ký RazorPay sẽ chỉ được theo dõi đối với những thành viên có dữ liệu tồn tại trong danh sách Thành viên.

Đây là giao diện của một thành viên trong ERPNext.
<img class="screenshot" alt="Membership" src="https://docs.erpnext.com/docs/v13/assets/img/non_profit/member.png">


## 3.4 Thiết lập webhook

Bạn có thể thiết lập một webhook từ bảng điều khiển RazorPay trong phần cài đặt. Bạn có thể đọc thêm về webhook trong RazorPay [tại đây](https://razorpay.com/docs/v13/webhooks/). Webhook này sẽ thông báo cho trang ERPNext của bạn bất cứ khi nào một đăng ký mới được tạo hoặc được gia hạn.

<img class="screenshot" alt="Membership" src="https://docs.erpnext.com/docs/v13/assets/img/non_profit/razorpay-webhook.png">

Bạn sẽ cần các chi tiết sau để thiết lập webhook.

### 3.4.1 URL Webhook

Sau đây là URL cho trang ERPNext của bạn. Đây là điểm cuối (endpoint) mà RazorPay sẽ sử dụng để thông báo về bất kỳ hoạt động nào liên quan đến đăng ký.

```sh
https://<your-site>/api/method/erpnext.non_profit.doctype.membership.membership.trigger_razorpay_subscription