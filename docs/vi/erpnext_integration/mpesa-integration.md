<!-- add-breadcrumbs -->
# Tích hợp M-Pesa

**Tích hợp M-Pesa cho phép xử lý các giao dịch với nhà cung cấp cổng thanh toán M-Pesa.**

Tích hợp M-Pesa tạo điều kiện thuận lợi cho việc xử lý thanh toán giữa ứng dụng M-Pesa và ERPNext. Tích hợp M-Pesa chỉ hoạt động với POS để hỗ trợ các thanh toán tương ứng. Tính năng này không hoạt động với giỏ hàng.

Để thiết lập M-Pesa, hãy đi đến:
> Integrations > Payments > M-Pesa Settings

## 1. Làm thế nào để lấy thông tin xác thực M-Pesa của bạn?
1. Để kích hoạt thông tin xác thực API, bạn cần đăng nhập vào tài khoản M-Pesa của mình.
2. Sau đó, mở phần Go Live của ứng dụng và làm theo các bước để được phê duyệt ứng dụng.
3. Khi tất cả các trường hợp kiểm thử đều đạt yêu cầu và kết quả mong đợi khớp với kết quả cuối cùng, bạn cần nộp tài liệu và làm theo các bước để nhận thông tin xác thực cuối cùng cho ứng dụng của mình.
4. Các chi tiết được đề cập trong phần Production URL và Credentials là thông tin xác thực mà bạn nên sử dụng trong M-Pesa Settings.

<img class="screenshot" alt="Mpesa Credentials" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/mpesa_credentials.png">


## 2. Thiết lập M-Pesa

Để kích hoạt M-Pesa Express, bạn cần cấu hình tất cả các tham số bắt buộc mà bạn đã nhận được từ M-Pesa. Nếu bạn muốn sử dụng môi trường staging của tích hợp, bạn có thể chọn tùy chọn staging và sử dụng thông tin xác thực staging do M-Pesa cung cấp bằng cách tạo một ứng dụng riêng biệt cho việc đó.
<img class="screenshot" alt="Mpesa Settings" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/mpesa_settings.png">

Khi kích hoạt tích hợp M-Pesa trong ERPNext, hệ thống sẽ tạo một bản ghi Cổng thanh toán (Payment Gateway) và một tài khoản trong Hệ thống tài khoản với loại Tài khoản là Ngân hàng như được thấy trong ảnh chụp màn hình sau.

<img class="screenshot" alt="Mpesa COA" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/mpesa_coa.png">

<img class="screenshot" alt="Mpesa POS Settings" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/mpesa_pos_settings.png">

Nó cũng sẽ tạo một Phương thức thanh toán (Mode of Payment) với cùng tên và tài khoản như cổng thanh toán, cùng với một số trường tùy chỉnh trong Cài đặt POS để xử lý các thanh toán POS.

<img class="screenshot" alt="Payment Gateway Account" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/payment_gateway_account_mpesa.png">

Sau khi cấu hình Tài khoản Cổng thanh toán, bạn sẽ có thể chấp nhận các thanh toán trực tuyến thông qua M-Pesa.


## 3. Thanh toán POS qua M-Pesa

Khi thiết lập hồ sơ POS với phương thức thanh toán M-Pesa, phần thanh toán POS sẽ hiển thị thêm một phần thông tin bổ sung. Phần này chứa hai trường đã được tự động thiết lập khi thêm cài đặt M-Pesa.

<img class="screenshot" alt="POS Additional Information" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/additional-information.png">

Ngay khi người dùng POS điền số điện thoại của Khách hàng, họ có thể khởi tạo một yêu cầu thanh toán từ Khách hàng. Một yêu cầu sẽ được gửi đến ứng dụng di động M-Pesa của Khách hàng được liên kết với số điện thoại đã chỉ định. Sau khi thanh toán được người dùng xử lý, người dùng sẽ được nhắc bởi một hộp thoại xác nhận để Xác nhận thanh toán.

## 4. Số dư tài khoản M-Pesa

Số dư tài khoản liên kết với một tài khoản M-Pesa cá nhân có thể được truy xuất thông qua nút Get Account Balance. Thao tác này sẽ tải chi tiết số dư tài khoản M-Pesa vào Trang tổng quan.

<img class="screenshot" alt="POS Account Balance" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/integrations/mpesa_account_balance.png">


## 5. Các loại tiền tệ giao dịch được hỗ trợ

M-Pesa sẽ chỉ hoạt động cho Công ty có Tiền tệ Công ty là KSH (Shilling Kenya).