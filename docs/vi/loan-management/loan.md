<!-- add-breadcrumbs -->
# Khoản vay
> Được giới thiệu trong Phiên bản 13

**Bản ghi Khoản vay là tài khoản khoản vay chứa tất cả thông tin liên quan đến một khoản vay.**

Bản ghi Khoản vay đóng vai trò là một tài khoản khoản vay chứa tất cả chi tiết về người đăng ký, lịch trình trả nợ và thông tin trả nợ. Tất cả các chứng từ liên quan đến khoản vay như [Giải ngân khoản vay](/docs/v13/user/manual/en/loan-management/loan-disbursement), [Trả nợ khoản vay](/docs/v13/user/manual/en/loan-management/loan-repayment), v.v. đều được liên kết với một Khoản vay.

Để truy cập danh sách Khoản vay, hãy đi tới:
> Home > Loan Management > Loan > Loan

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Khoản vay, bạn nên tạo các mục sau trước:

* [Loại bảo đảm khoản vay](/docs/v13/user/manual/en/loan-management/loan-security-type)
* [Bảo đảm khoản vay](/docs/v13/user/manual/en/loan-management/loan-security)
* [Loại khoản vay](/docs/v13/user/manual/en/loan-management/loan-type)
* [Đơn đăng ký khoản vay](/docs/v13/user/manual/en/loan-management/loan-application)
* [Cam kết bảo đảm khoản vay](/docs/v13/user/manual/en/loan-management/loan-security-pledge)

## 2. Cách tạo một Khoản vay
1. Đi tới Danh sách Khoản vay, nhấp vào Mới.
1. Chọn Loại người đăng ký.
1. Chọn Người đăng ký.
1. Chọn Đơn đăng ký khoản vay nếu Đơn đăng ký khoản vay đã được tạo cho Người đăng ký đó. Tất cả chi tiết trong đơn đăng ký khoản vay sẽ tự động được lấy vào bản ghi Khoản vay.
1. Chọn Công ty.
1. Nhập ngày hạch toán.
1. Nếu loại người đăng ký là Nhân viên, hãy tích vào "Trả từ Lương" nếu khoản vay sẽ được hoàn trả từ lương.

  <img class="screenshot" alt="Make Loan" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-details.png">

1. Nhập Loại khoản vay. Tất cả các tài khoản khoản vay, phương thức thanh toán và các chi tiết khoản vay khác như khoản vay có kỳ hạn hay khoản vay theo yêu cầu sẽ được tự động lấy từ danh mục Loại khoản vay. Nếu là khoản vay có kỳ hạn, lịch trình trả nợ sẽ được tự động tạo sau khi Lưu chứng từ khoản vay.

  <img class="screenshot" alt="Make Loan" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-accounts.png">

  <img class="screenshot" alt="Make Loan" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-repayment-schedule.png">


1. Tích vào 'Is Secured Loan' nếu khoản vay là khoản vay có bảo đảm. Đồng thời chọn 'Loan Security Pledge' nếu khoản vay là khoản vay có bảo đảm.
1. Nhấp vào "Lưu" để lưu bản Nháp của Khoản vay.
1. Nhấp vào "Xác nhận" để xác nhận Cam kết bảo đảm khoản vay.
1. Sau khi Khoản vay được Xác nhận, số tiền khoản vay đã sẵn sàng để được giải ngân.



### 2.1. Các cách khác để tạo Khoản vay
Bạn cũng có thể tạo một Khoản vay từ một Đơn đăng ký khoản vay đã được phê duyệt thông qua nút **Create** ở góc trên bên phải.

<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/create-loan.png">

## 3. Các tính năng

### 3.1. Tạo Phiếu giải ngân
Sau khi Xác nhận chứng từ Khoản vay, nếu trạng thái là "Sanctioned" (Đã phê duyệt) và "Repay from Salary" không được tích, bạn có thể tạo [Giải ngân khoản vay](/docs/v13/user/manual/en/loan-management/loan-disbursement) từ chứng từ khoản vay thông qua nút **Create** ở góc trên bên phải.

<img class="screenshot" alt="Create Loan Disbursement" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/create-loan-disbursement.png">

### 3.2. Tạo Phiếu trả nợ
Nếu khoản vay đã được giải ngân toàn bộ hoặc một phần và "Repay from Salary" không được tích, bạn có thể tạo [Trả nợ khoản vay](/docs/v13/user/manual/en/loan-management/loan-repayment) từ chứng từ khoản vay thông qua nút **Create** ở góc trên bên phải.

<img class="screenshot" alt="Create Loan Repayment" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/create-loan-repayment.png">

### 3.3. Khấu trừ trả nợ khoản vay từ lương
Để tự động khấu trừ khoản trả nợ khoản vay từ Lương, hãy tích vào "Repay from Salary" trong Khoản vay. Nó sẽ xuất hiện dưới dạng Trả nợ khoản vay trong Phiếu lương và một bản ghi [Trả nợ khoản vay](/docs/v13/user/manual/en/loan-management/loan-repayment) cũng sẽ được tự động tạo cho mục đó.

<img class="screenshot" alt="Salary Slip Loan" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/salary-slip-loan.png">

{next}