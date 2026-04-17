<!-- add-breadcrumbs -->
# Tích hợp Paytm

**Tích hợp Paytm cho phép xử lý các giao dịch với nhà cung cấp cổng thanh toán Paytm.**

Tích hợp Paytm tạo điều kiện thuận lợi cho việc xử lý thanh toán giữa cổng thanh toán Paytm và ERPNext. Khách hàng của bạn có thể chọn thanh toán từ bất kỳ thẻ tín dụng/thẻ ghi nợ, UPI, Netbanking hoặc Ví Paytm nào.

Để thiết lập Paytm, hãy đi tới:
> Integrations > Payments > Paytm Settings

## 1. Làm thế nào để lấy thông tin xác thực API Paytm của bạn?
1. Để kích hoạt thông tin xác thực API, bạn cần đăng nhập vào tài khoản Paytm của mình.
2. Sau đó, mở tùy chọn Developer Settings ở thanh bên.
3. Chọn tùy chọn API Keys, nó sẽ hiển thị hai loại thông tin chi tiết API (Test/Production).
4. Các thông tin chi tiết được đề cập trong Production API là thông tin xác thực mà bạn nên sử dụng trong Paytm Settings.

<img class="screenshot" alt="Razorpay Settings" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/paytm_credentials.png">


## 2. Thiết lập Paytm

Để kích hoạt dịch vụ thanh toán Paytm, bạn cần cấu hình tất cả các tham số bắt buộc mà bạn nhận được từ Paytm. Nếu bạn muốn sử dụng môi trường thử nghiệm (staging) của tích hợp này, bạn có thể chọn tùy chọn staging và sử dụng thông tin xác thực API dành cho nhà phát triển thử nghiệm do Paytm cung cấp.
<img class="screenshot" alt="Razorpay Settings" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/paytm_settings.png">

Khi kích hoạt tích hợp Paytm trong ERPNext, hệ thống sẽ tạo một bản ghi Payment Gateway và một Account Head trong Hệ thống tài khoản với loại Tài khoản là Bank như được thấy trong ảnh chụp màn hình sau.

<img class="screenshot" alt="Stripe COA" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/paytm_coa.png">

Ngoài ra, nó sẽ tạo một mục Payment Gateway Account. Payment Gateway Account là trung tâm cấu hình nơi bạn có thể thiết lập các Account Head và mẫu email Yêu cầu thanh toán mặc định để yêu cầu thanh toán từ khách hàng.

<img class="screenshot" alt="Payment Gateway Account" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/payment_gateway_account_paytm.png">

Sau khi cấu hình Payment Gateway Account, bạn sẽ có thể chấp nhận thanh toán trực tuyến qua Paytm.

## 3. Các loại tiền tệ giao dịch được hỗ trợ

Paytm sẽ chỉ hoạt động cho Công ty có Tiền tệ là INR (Rupee Ấn Độ).