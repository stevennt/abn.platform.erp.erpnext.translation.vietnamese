<!-- add-breadcrumbs -->
# Thiết lập Braintree

Để thiết lập Braintree, hãy đi tới `Explore > Integrations > Braintree Settings`

## Thiết lập Braintree

Để kích hoạt Braintree trong tài khoản ERPNext của bạn, bạn cần cấu hình các tham số sau:

- Merchant ID
- Public Key
- Private Key

Bạn có thể thiết lập nhiều cổng thanh toán Braintree nếu cần. Việc lựa chọn tài khoản cổng thanh toán sẽ quyết định tài khoản Braintree nào được sử dụng để Thanh toán.

![Braintree Settings](https://docs.erpnext.com/docs/v16/assets/img/setup/integrations/braintree_account.png)

Khi kích hoạt dịch vụ, hệ thống sẽ tạo bản ghi Cổng thanh toán (Payment Gateway) và một tài khoản trong Hệ thống tài khoản với loại tài khoản là Ngân hàng.

![Braintree COA](https://docs.erpnext.com/docs/v16/assets/img/setup/integrations/braintree_coa.png)

Hệ thống cũng sẽ tạo một tài khoản cổng thanh toán. Bạn có thể thay đổi tài khoản ngân hàng mặc định nếu cần và tạo một mẫu cho yêu cầu Thanh toán.

![Payment Gateway Account](https://docs.erpnext.com/docs/v16/assets/img/setup/integrations/payment_gateway_account_braintree.png)

Sau khi cấu hình Tài khoản cổng thanh toán, hệ thống của bạn có thể chấp nhận Thanh toán trực tuyến thông qua Braintree.

## Các loại tiền tệ giao dịch được hỗ trợ

```
"AED","AMD","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BIF","BMD","BND","BOB",
"BRL","BSD","BWP","BYN","BZD","CAD","CHF","CLP","CNY","COP","CRC","CVE","CZK","DJF","DKK",
"DOP","DZD","EGP","ETB","EUR","FJD","FKP","GBP","GEL","GHS","GIP","GMD","GNF","GTQ","GYD",
"HKD","HNL","HRK","HTG","HUF","IDR","ILS","INR","ISK","JMD","JPY","KES","KGS","KHR","KMF",
"KRW","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LTL","MAD","MDL","MKD","MNT","MOP","MUR",
"MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","PAB","PEN","PGK","PHP",
"PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SEK","SGD","SHP","SLL",
"SOS","SRD","STD","SVC","SYP","SZL","THB","TJS","TOP","TRY","TTD","TWD","TZS","UAH","UGX",
"USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XCD","XOF","XPF","YER","ZAR","ZMK","ZWD"