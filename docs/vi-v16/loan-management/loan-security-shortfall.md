<!-- add-breadcrumbs -->
# Thiếu hụt Tài sản đảm bảo Khoản vay
> Phiên bản 16

**Nếu tỷ lệ giá trị khoản vay trên tài sản đảm bảo giảm xuống dưới một giá trị cụ thể, một bản ghi Thiếu hụt Tài sản đảm bảo Khoản vay sẽ tự động được tạo cho khoản vay cụ thể đó.**

<img class="screenshot" alt="Loan Security Shortfall" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-security-shortfall-flow.png">

Để truy cập danh sách Thiếu hụt Tài sản đảm bảo Khoản vay, hãy đi tới:
> Home > Loan Management > Loan Security > Loan Security Shortfall

<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/loan-security-shortfall.png">


Một bản ghi Thiếu hụt Tài sản đảm bảo Khoản vay bao gồm các chi tiết về:

  * **Loan**: Khoản vay có sự thiếu hụt về tỷ lệ giá trị khoản vay trên tài sản đảm bảo.
  * **Shortfall Time**: Thời điểm bản ghi thiếu hụt được tạo.
  * **Status**: Trạng thái của việc thiếu hụt. *Pending* là trạng thái mặc định và nó sẽ chuyển sang *Complete* sau khi một khoản thanh toán được thực hiện hoặc tài sản đảm bảo bổ sung được thế chấp cho khoản vay để bù đắp phần thiếu hụt.
  * **Loan Amount**: Số tiền khoản vay là số tiền khoản vay còn lại được sử dụng để tính toán thiếu hụt.
  * **Security Value**: Giá trị tài sản đảm bảo là giá trị tài sản đảm bảo đang thế chấp hiện tại.
  * **Shortfall Amount**: Số tiền thiếu hụt là khoản chênh lệch giữa số tiền khoản vay và giá trị tài sản đảm bảo cần phải được hoàn trả để bù đắp phần thiếu hụt.

## 1. Tính năng

Tài sản đảm bảo Khoản vay bổ sung có thể được thế chấp cho một khoản vay ngay từ chính mục Thiếu hụt Tài sản đảm bảo Khoản vay thông qua nút **Add Loan Security** ở phía trên bên phải.

<img class="screenshot" alt="Loan Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/loan-management/shortfall-security.png">

{next}