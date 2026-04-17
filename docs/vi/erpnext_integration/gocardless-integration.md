<!-- add-breadcrumbs -->
# Thiết lập GoCardless

Để thiết lập GoCardless, hãy đi tới `Explore > Integrations > GoCardless Settings`

## Thiết lập GoCardless

Để kích hoạt GoCardless trong tài khoản ERPNext của bạn, bạn cần cấu hình các tham số sau: Access Token và tùy chọn (nhưng rất được khuyến khích) là Webhooks Secret key.


Bạn có thể thiết lập nhiều cổng thanh toán GoCardless nếu cần. Việc lựa chọn tài khoản cổng thanh toán sẽ quyết định tài khoản GoCardless nào được sử dụng để thanh toán.

![GoCardless Settings](https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/gocardless_account.png)

Khi kích hoạt dịch vụ, hệ thống sẽ tạo một bản ghi Cổng thanh toán (Payment Gateway) và một tài khoản trong Hệ thống tài khoản với loại tài khoản là Ngân hàng.

![GoCardless COA](https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/gocardless_coa.png)

Nó cũng sẽ tạo một tài khoản cổng thanh toán. Bạn có thể thay đổi tài khoản ngân hàng mặc định nếu cần và tạo một mẫu cho yêu cầu thanh toán.

![Payment Gateway Account](https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/payment_gateway_account_gocardless.png)

Sau khi cấu hình Tài khoản cổng thanh toán, hệ thống của bạn có thể chấp nhận các thanh toán trực tuyến thông qua GoCardless.

## Quy trình thanh toán SEPA

Khi một khoản thanh toán SEPA mới được khởi tạo, khách hàng sẽ được yêu cầu nhập số IBAN (hoặc số tài khoản địa phương) và xác nhận một ủy thác SEPA (SEPA mandate).

Sau khi xác nhận ủy thác, một yêu cầu thanh toán sẽ được gửi đến GoCardless và được xử lý.

Nếu khách hàng đã có một ủy thác SEPA hợp lệ, thay vì gửi yêu cầu thanh toán cho khách hàng, yêu cầu thanh toán sẽ được gửi trực tiếp đến GoCardless mà không cần khách hàng phải xác nhận lại.
Khách hàng sẽ chỉ nhận được một email xác nhận từ GoCardless thông báo rằng một khoản thanh toán đã được xử lý.


## Hủy ủy thác

Bạn có thể thiết lập một Webhook trong GoCardless để tự động vô hiệu hóa các ủy thác đã bị hủy hoặc hết hạn trong ERPNext.

URL Endpoint cho webhook của bạn nên là:

`https://yoursite.com/api/method/erpnext.erpnext_integrations.doctype.gocardless_settings.webhooks`


Trong trường hợp này, đừng quên cấu hình Webhooks Secret Key trong cài đặt tài khoản GoCardless của bạn trong ERPNext.


## Các loại tiền tệ giao dịch được hỗ trợ
	"EUR", "DKK", "GBP", "SEK"