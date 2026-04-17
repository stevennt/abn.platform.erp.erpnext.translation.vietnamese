<!-- add-breadcrumbs -->
# Thiết lập PayPal

Cổng thanh toán là một dịch vụ cung cấp ứng dụng thương mại điện tử giúp ủy quyền các khoản thanh toán thẻ tín dụng cho các doanh nghiệp điện tử, nhà bán lẻ trực tuyến, mô hình kết hợp trực tuyến và trực tiếp (bricks and clicks), hoặc mô hình cửa hàng truyền thống (brick and mortar).

Cổng thanh toán tạo điều kiện thuận lợi cho việc chuyển giao thông tin giữa cổng thanh toán (như trang web, điện thoại di động hoặc dịch vụ phản hồi giọng nói tương tác) và Bộ xử lý đầu cuối (Front End Processor) hoặc ngân hàng thanh toán.

Để thiết lập PayPal,
`Khám phá > Tích hợp > Cài đặt PayPal`

#### Thiết lập PayPal

Để kích hoạt dịch vụ thanh toán PayPal, bạn cần cấu hình các tham số như API Username, API Password và Signature.

<img class="screenshot" alt="PayPal Settings" src="../assets/img/setup/integrations/paypal_settings.png">

Bạn cũng có thể thiết lập môi trường thanh toán thử nghiệm bằng cách cài đặt `Use Sandbox`.

Khi kích hoạt dịch vụ, hệ thống sẽ tạo bản ghi Cổng thanh toán và tài khoản trong Hệ thống tài khoản có loại tài khoản là Ngân hàng.

<img class="screenshot" alt="PayPal COA" src="../assets/img/setup/integrations/paypal_coa.png">

Ngoài ra, hệ thống cũng sẽ tạo một mục Tài khoản Cổng thanh toán. Tài khoản Cổng thanh toán là trung tâm cấu hình, từ đây bạn có thể thiết lập tài khoản từ Hệ thống tài khoản hiện có, và mẫu nội dung email Yêu cầu thanh toán mặc định.

<img class="screenshot" alt="Payment Gateway Account" src="../assets/img/setup/integrations/payment_gateway_account_paypal.png">

Sau khi kích hoạt dịch vụ và cấu hình Tài khoản Cổng thanh toán, hệ thống của bạn đã có thể chấp nhận các thanh toán trực tuyến.

#### Các loại tiền tệ giao dịch được hỗ trợ
AUD, BRL, CAD, CZK, DKK, EUR, HKD, HUF, ILS, JPY, MYR, MXN, TWD, NZD, NOK, PHP, PLN, GBP, RUB, SGD, SEK, CHF, THB, TRY, USD

## Lấy thông tin xác thực PayPal

#### Chữ ký API PayPal Sandbox
 - Đăng nhập vào tài khoản nhà phát triển PayPal, <a href="https://developer.paypal.com/">PayPal Developer Account</a>
 - Từ tab **Accounts**, tạo một tài khoản doanh nghiệp mới.
<img class="screenshot" alt="Payment Request" src="../assets/img/setup/integrations/setup-sanbox-1.png">

 - Từ hồ sơ tài khoản này, bạn sẽ nhận được thông tin xác thực API sandbox của mình.
<img class="screenshot" alt="Payment Request" src="../assets/img/setup/integrations/sanbox-credentials.png">


---

#### Chữ ký API Tài khoản PayPal
 - Đăng nhập vào Tài khoản PayPal và đi đến hồ sơ.
<img class="screenshot" alt="Payment Request" src="../assets/img/setup/integrations/api-step-1.png">

 - Từ mục **My Selling Tools**, đi đến **api Access**.
<img class="screenshot" alt="Payment Request" src="../assets/img/setup/integrations/api-step-2.png">

 - Tại trang API Access, chọn tùy chọn 2 để tạo thông tin xác thực API.
<img class="screenshot" alt="Payment Request" src="../assets/img/setup/integrations/api-step-3.png">