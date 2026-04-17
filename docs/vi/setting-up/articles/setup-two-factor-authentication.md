<!-- add-breadcrumbs -->
#Thiết lập Xác thực hai yếu tố

##Bật Xác thực hai yếu tố (2FA)

Kích hoạt xác thực hai yếu tố bằng cách chạy lệnh sau.

`bench --site [sitename] set-config enable_two_factor_auth true`

Chỉ định các thông tin sau trong Cài đặt hệ thống (System Settings)

* Phương thức xác thực OTP (OTP App = TOTP sử dụng Token phần mềm hoặc Token phần cứng, trong khi Email/SMS = HOTP sử dụng Email hoặc SMS)
* Thời gian hết hạn của Mã QR trên máy chủ nếu chọn OTP App
* Tên nhà phát hành OTP (OTP Issuer Name).

<img alt="Enable Two Factor Auth" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/twofactor/twofactor-1.png">


Khi kích hoạt 2FA từ phần thiết lập, nó cũng sẽ được kích hoạt cho Vai trò (Role) "All". Bằng cách này, tất cả người dùng bao gồm cả Quản trị viên (Administrator) đều phải thực hiện xác thực cấp độ 2 bằng một mã token. Bằng cách bỏ chọn ô "Two Factor Authentication" trong vai trò "All" và bật nó trong các vai trò khác, nhu cầu đăng nhập bằng mã token có thể được giới hạn cho các vai trò cụ thể. 2FA không áp dụng cho đăng nhập của Người dùng Web (Web Users) và đăng nhập qua API.

<img alt="Role Enable Two Factor Auth" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/twofactor/twofactor-2.png">

Nếu sử dụng xác thực qua SMS, vui lòng đảm bảo rằng các cài đặt SMS của bạn đã được cập nhật.

<img alt="SMS Settings" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/twofactor/twofactor-3.png">

Nếu sử dụng Email, hãy đảm bảo rằng các cài đặt tài khoản Email gửi đi của bạn đã được cập nhật.

<img alt="Email Settings" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/twofactor/twofactor-4.png">

Khi người dùng mới cố gắng đăng nhập lần đầu tiên vào một hệ thống đã bật xác thực hai yếu tố và có tùy chọn xác thực là OTP App, một email sẽ được gửi kèm theo liên kết dẫn đến Mã QR.

<img alt="Email Notify Two Factor" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/twofactor/twofactor-5.png">
<img alt="QR Code Page" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/twofactor/twofactor-6.png">

Việc quét Mã QR bằng một ứng dụng xác thực như Google Authenticator sẽ đăng ký quyền truy cập cho người dùng và tự động bắt đầu tạo các mã token có thể được sử dụng để đăng nhập.

<img alt="Two Factor Scan App" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/twofactor/twofactor_app.jpeg">

Nếu sử dụng Email hoặc SMS làm phương thức xác thực, bạn cũng sẽ nhận được các thông báo.

<img alt="Email and SMS" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/articles/twofactor/twofactor-8.png">