<!-- add-breadcrumbs -->
# Trợ cấp thôi việc

> Tính năng này được giới thiệu trong Phiên bản 13, sẽ là một phần của Phân hệ Bảng lương riêng biệt.

**Trợ cấp thôi việc được người sử dụng lao động chi trả cho nhân viên vì những dịch vụ mà họ đã thực hiện trong thời gian làm việc. Khoản này thường được thanh toán tại thời điểm nghỉ hưu nhưng có thể được thanh toán sớm hơn nếu đáp ứng được các điều kiện nhất định.**

Trong ERPNext, bạn có thể quản lý các Khoản thanh toán Trợ cấp thôi việc của nhân viên dựa trên các [Quy tắc trợ cấp thôi việc](gratuity.md) khác nhau tùy theo từng khu vực.

Để truy cập Trợ cấp thôi việc, hãy đi tới:

> Home > Payroll > Gratuity

## 1. Điều kiện tiên quyết

Trước khi tạo Trợ cấp thôi việc, bạn nên tạo các mục sau:

1. [Nhân viên](employee.md)
1. [Quy tắc trợ cấp thôi việc](gratuity.md)
1. [Thành phần lương](salary-component.md)

## 2. Cách tạo Trợ cấp thôi việc

1. Đi tới Gratuity > New
1. Chọn Nhân viên và Quy tắc trợ cấp thôi việc. Khi chọn, hệ thống sẽ tính toán Kinh nghiệm làm việc hiện tại và Tổng số tiền trợ cấp thôi việc dựa trên quy tắc trợ cấp thôi việc và ngày thôi việc.
1. Tích vào ô Pay via Salary Slip nếu bạn muốn thanh toán trợ cấp thôi việc thông qua Phiếu lương.
1. Lưu và Xác nhận

<img class="screenshot" alt="Gratuity" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/gratuity.png">

## 3. Các phương thức thanh toán Trợ cấp thôi việc

Trong ERPNext, chúng tôi cho phép bạn thanh toán số tiền thông qua Phiếu lương hoặc Bút toán thanh toán.

### 3.1 Thanh toán qua Phiếu lương
Để thanh toán số tiền Trợ cấp thôi việc qua Phiếu lương, bạn cần tích vào ô **Pay via Salary Slip**. Chọn **Payroll Date** (Ngày tính lương) và **Salary Component** (Thành phần lương), các mục này sẽ xuất hiện sau khi tích chọn.

<img class="screenshot" alt="payment conf via salary slip" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/payment-conf-via-salary-slip.png">

Sau khi Xác nhận, hệ thống sẽ tự động tạo Lương bổ sung (Additional Salary) với Ngày tính lương và Thành phần lương tương ứng.

<img class="screenshot" alt="gratuity payment via salary slip" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/gratuity-payment-via-salary-slip.png">

### Thanh toán qua Bút toán thanh toán
Để thanh toán số tiền Trợ cấp thôi việc qua Bút toán thanh toán, bạn cần đảm bảo rằng ô **Pay via Salary Slip** không được tích chọn. Sau đó, hệ thống sẽ cho phép bạn chọn **Payable Account** (Tài khoản phải trả), **Expense Account** (Tài khoản chi phí) và **Mode of Payment** (Phương thức thanh toán).

<img class="screenshot" alt="payment conf via payment entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/payment-conf-via-payment-entry.png">

Sau khi Xác nhận bản ghi, hãy nhấp vào nút "Create Payment Entry", nút này sẽ chuyển hướng bạn đến Biểu mẫu Bút toán thanh toán, hãy điền đầy đủ thông tin, Lưu và Xác nhận.

<img class="screenshot" alt="gratuity payment via payment entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/gratuity-payment-via-payment-entry.png">