<!-- add-breadcrumbs -->
# Thiết lập Stripe

Để thiết lập Stripe,
`Khám phá > Tích hợp > Cài đặt Stripe`

#### Thiết lập Stripe

Để kích hoạt dịch vụ thanh toán Stripe, bạn cần cấu hình các tham số như Publishable Key, Secret Key.
<img class="screenshot" alt="Razorpay Settings" src="../assets/img/setup/integrations/stripe_setting.png">

Khi kích hoạt dịch vụ, hệ thống sẽ tạo bản ghi Cổng thanh toán (Payment Gateway) và tài khoản trong hệ thống tài khoản với loại tài khoản là Ngân hàng.

<img class="screenshot" alt="Stripe COA" src="../assets/img/setup/integrations/stripe_coa.png">

Ngoài ra, hệ thống cũng sẽ tạo một mục Tài khoản Cổng thanh toán (Payment Gateway Account). Tài khoản Cổng thanh toán là trung tâm cấu hình, từ đây bạn có thể thiết lập tài khoản từ hệ thống tài khoản hiện có, cũng như mẫu nội dung email Yêu cầu thanh toán mặc định.

<img class="screenshot" alt="Payment Gateway Account" src="../assets/img/setup/integrations/payment_gateway_account_stripe.png">

Sau khi cấu hình Tài khoản Cổng thanh toán, hệ thống của bạn đã có thể chấp nhận các thanh toán trực tuyến.

### Thiết lập các gói đăng ký

Nếu bạn cần tính phí định kỳ thay vì thanh toán một lần, bạn có thể sử dụng hệ thống đăng ký của Stripe.

Sau khi bạn đã tạo các gói thanh toán trong Stripe, hãy thêm một hoặc vài "Kế hoạch thanh toán" (Payment Plan) mới trong Frappe.

<img class="screenshot" alt="Payment Plan" src="../assets/img/setup/integrations/payment_plan.png">

Sau đó, khi bạn tạo yêu cầu thanh toán, hãy tích vào trường "Is a subscription" (Là một gói đăng ký) và hệ thống sẽ lấy các gói đăng ký tương ứng từ trong gói đăng ký đó.

<img class="screenshot" alt="Payment Request" src="../assets/img/setup/integrations/subscription_payment_request.png">

ERPNext sẽ tự động tạo một gói đăng ký mới cho Khách hàng này trong Stripe.

#### Các loại tiền tệ giao dịch được hỗ trợ
"AED", "ALL", "ANG", "ARS", "AUD", "AWG", "BBD", "BDT", "BIF", "BMD", "BND",
"BOB", "BRL", "BSD", "BWP", "BZD", "CAD", "CHF", "CLP", "CNY", "COP", "CRC", "CVE", "CZK", "DJF",
"DKK", "DOP", "DZD", "EGP", "ETB", "EUR", "FJD", "FKP", "GBP", "GIP", "GMD", "GNF", "GTQ", "GYD",
"HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "ISK", "JMD", "JPY", "KES", "KHR", "KMF",
"KRW", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "MAD", "MDL", "MNT", "MOP", "MRO", "MUR", "MVR",
"MWK", "MXN", "MYR", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "PAB", "PEN", "PGK", "PHP", "PKR",
"PLN", "PYG", "QAR", "RUB", "SAR", "SBD", "SCR", "SEK", "SGD", "SHP", "SLL", "SOS", "STD", "SVC",
"SZL", "THB", "TOP", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VND", "VUV", "WST",
"XAF", "XOF", "XPF", "YER", "ZAR"