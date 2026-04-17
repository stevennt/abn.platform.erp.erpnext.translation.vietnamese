<!-- add-breadcrumbs -->
#Tích hợp RazorPay

Cổng thanh toán là một dịch vụ cung cấp ứng dụng thương mại điện tử giúp ủy quyền các thanh toán thẻ tín dụng cho các doanh nghiệp điện tử, nhà bán lẻ trực tuyến, mô hình kết hợp trực tuyến và trực tiếp (bricks and clicks), hoặc các cửa hàng truyền thống (brick and mortar).

Cổng thanh toán tạo điều kiện thuận lợi cho việc chuyển giao thông tin giữa cổng thanh toán (như trang web, điện thoại di động hoặc dịch vụ phản hồi giọng nói tương tác) và Bộ xử lý đầu cuối (Front End Processor) hoặc ngân hàng thanh toán.

Để thiết lập RazorPay,

`Explore > Integrations > RazorPay Settings`

<img class="screenshot" alt="Razorpay Settings" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/razorpay-api.gif">

#### Thiết lập RazorPay

Để kích hoạt dịch vụ thanh toán RazorPay, bạn cần cấu hình các tham số như API Key, API Secret

<img class="screenshot" alt="Razorpay Settings" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/razorpay_settings.png">

Khi kích hoạt dịch vụ, hệ thống sẽ tạo bản ghi Cổng thanh toán (Payment Gateway) và tài khoản trong Hệ thống tài khoản với loại tài khoản là Ngân hàng.

<img class="screenshot" alt="Razorpay COA" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/razorpay_coa.png">

Ngoài ra, hệ thống cũng sẽ tạo một mục Tài khoản Cổng thanh toán (Payment Gateway Account). Tài khoản Cổng thanh toán là trung tâm cấu hình, từ đây bạn có thể thiết lập tài khoản từ Hệ thống tài khoản hiện có, cũng như mẫu nội dung email yêu cầu thanh toán mặc định.

<img class="screenshot" alt="Payment Gateway Account" src="https://docs.erpnext.com/docs/v13/assets/img/setup/integrations/payment_gateway_account_razorpay.png">

Sau khi kích hoạt dịch vụ và cấu hình Tài khoản Cổng thanh toán, hệ thống của bạn đã có thể chấp nhận các thanh toán trực tuyến.

#### Hỗ trợ các loại tiền tệ giao dịch

RazorPay sẽ chỉ hoạt động cho công ty có `INR (Rupee Ấn Độ)` là Tiền tệ.