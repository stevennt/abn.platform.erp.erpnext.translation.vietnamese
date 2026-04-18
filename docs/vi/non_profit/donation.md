<!-- add-breadcrumbs -->
# Quyên góp

> Được giới thiệu trong phiên bản 13

DocType Quyên góp cho phép bạn ghi lại chi tiết quyên góp cho **Nhà tài trợ**.

## 1. Điều kiện tiên quyết

Trước khi tạo một khoản Quyên góp, trước tiên bạn cần tạo một [Nhà tài trợ](donor.md).

## 2. Cách tạo một khoản Quyên góp

Để tạo một khoản Quyên góp mới, hãy đi tới:

> Non Profit > Donation > New

<img class="screenshot" alt="Donation" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/non_profit/donation.png">

1. Chọn Nhà tài trợ. Tên và Email của Nhà tài trợ sẽ được tự động lấy ra.
2. Thiết lập Ngày quyên góp.
3. Thiết lập Số tiền và Phương thức thanh toán.
4. Lưu và Xác nhận.

## 3. Các tính năng

### 3.1 Bút toán thanh toán cho Quyên góp

Sau khi xác nhận một khoản quyên góp, bạn có thể tạo một Bút toán thanh toán cho khoản đó bằng cách sử dụng nút **Create Payment Entry**.

### 3.2 RazorPay cho Quyên góp

Bạn có thể thiết lập RazorPay để thu tiền quyên góp. Bạn có thể tìm thấy hướng dẫn thiết lập razorpay [tại đây](../erpnext_integration/razorpay-integration.md).

Bạn có thể làm theo các bước được liệt kê dưới đây để thiết lập Razorpay cho các khoản quyên góp.

1. Thiết lập RazorPay
1. Thiết lập RazorPay Webhook

#### 3.2.1 Thiết lập RazorPay

Bạn có thể tìm thấy hướng dẫn thiết lập razorpay [tại đây](../erpnext_integration/razorpay-integration.md).

Để thu tiền quyên góp, bạn cần thiết lập một số giá trị mặc định trong phần Cài đặt Phi lợi nhuận (Non Profit Settings) trong [Non Profit Settings](non_profit_settings.md)

1. **Default Company**: Công ty này sẽ được thiết lập cho các khoản Quyên góp được tạo thông qua webhook.
1. **Default Donor Type**: Loại Nhà tài trợ này sẽ được thiết lập cho Nhà tài trợ được tạo thông qua webhook Quyên góp.
1. **Automate Donation Payment Entries**: Bạn có thể bật tính năng này để tự động tạo Bút toán thanh toán cho các mục Quyên góp được tạo thông qua webhook.

Nếu _Automate Donation Payment Entries_ được bật, bạn sẽ phải thiết lập Tài khoản Nợ mặc định và Tài khoản Thanh toán Quyên góp cho Bút toán thanh toán.

<img class="screenshot" alt="Donation Settings" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/non_profit/donation-settings.png">

#### 3.2.2 Thiết lập webhook

Bạn có thể thiết lập một webhook từ bảng điều khiển RazorPay trong phần Cài đặt. Bạn có thể đọc thêm về webhooks trong RazorPay [tại đây](https://razorpay.com/docs/v13/webhooks/). Webhook này sẽ thông báo cho trang ERPNext của bạn bất cứ khi nào một khoản quyên góp mới được tạo.

<img class="screenshot" alt="Donation Webhook" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/non_profit/donation-webhook.png">

Bạn sẽ cần các chi tiết sau để thiết lập webhook.

1. **Webhook URL**: Sau đây là URL cho trang ERPNext của bạn. Đây là điểm cuối (endpoint) mà RazorPay sẽ sử dụng để thông báo về bất kỳ khoản quyên góp mới nào được tạo.

    ```sh
    https://<your-site>/api/method/erpnext.non_profit.doctype.donation.donation.capture_razorpay_donations
    ```

2. **Secret**: Để bảo mật điểm cuối API của bạn, tốt nhất là luôn tạo và thiết lập một Webhook Secret cho điểm cuối API. Để làm việc này, trên trang ERPNext của bạn, bạn có thể nhấp vào nút **Donations > Generate Webhook Secret** trong phần Non Profit Settings. Sao chép mã secret và dán nó vào trường secret trên bảng điều khiển RazorPay để thiết lập webhook.

3. **Event**: Bạn phải bật sự kiện `payment.captured`.

4. **Active**: Tích vào đây để kích hoạt webhook.

Với các bước này, webhook của bạn đã được kích hoạt.

{next}