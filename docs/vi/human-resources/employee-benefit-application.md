<!-- add-breadcrumbs -->
#Đơn đăng ký phúc lợi nhân viên

Nhân viên có quyền hưởng các phúc lợi linh hoạt mà họ có thể nhận theo tỷ lệ (như một phần của Lương) hoặc dưới dạng một khoản tiền trọn gói khi họ yêu cầu hưởng phúc lợi. Để lựa chọn từ các phúc lợi linh hoạt khác nhau mà Nhân viên sẽ nhận theo tỷ lệ, nhân viên nên tạo một Đơn đăng ký phúc lợi nhân viên mới.

Để tạo một Đơn đăng ký phúc lợi nhân viên mới,

> Human Resources > Payroll > Employee Benefit Application > New Employee Benefit Application

<img class="screenshot" alt="Employee Benefit Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-benefit-application.png">

Tại đây, Nhân viên có thể xem Mức phúc lợi tối đa theo Phân bổ cấu trúc lương và sau đó chọn từ các Thành phần thu nhập thuộc Cấu trúc lương đã được phân bổ cho nhân viên. Họ cũng có thể nhập số tiền mà họ muốn nhận như một phần của Phiếu lương.

Dựa trên Đơn đăng ký phúc lợi nhân viên, Số tiền phúc lợi tối đa sẽ được phân bổ giữa các thành phần thu nhập linh hoạt khi tạo Phiếu lương. Nếu Nhân viên không Xác nhận Đơn đăng ký phúc lợi nhân viên trước khi xử lý bảng lương, Số tiền phúc lợi tối đa mà nhân viên được hưởng sẽ được phân bổ tỷ lệ cho từng thành phần linh hoạt có trong cấu trúc lương của Nhân viên.

> Lưu ý: Nhân viên chỉ có thể gửi một Đơn đăng ký phúc lợi nhân viên cho mỗi Kỳ lương.

Đơn đăng ký phúc lợi nhân viên phải bao gồm toàn bộ số tiền mà nhân viên được nhận theo Số tiền phúc lợi tối đa theo tỷ lệ. Tuy nhiên, nếu Cấu trúc lương của nhân viên bao gồm các Thành phần lương được thanh toán theo Yêu cầu phúc lợi nhân viên (Thành phần lương có _Pay Against Benefit Claim_), họ được phép gửi Đơn đăng ký phúc lợi nhân viên không bao gồm số tiền được phân bổ cho các thành phần đó.

Ngoài ra, lưu ý rằng những thành phần được nhận dựa trên Yêu cầu phúc lợi nhân viên cũng có thể là một phần của đơn đăng ký, nhưng sẽ chỉ được chi trả trọn gói, như một phần lương của họ khi Nhân viên gửi yêu cầu cho thành phần đó.

> Lưu ý: Việc tính Thuế thông thường không bao gồm các Phúc lợi linh hoạt vì trong hầu hết các trường hợp, các khoản này được miễn Thuế. Để tính thuế cho các thành phần này bất kỳ lúc nào trước kỳ lương cuối cùng, hãy sử dụng _Deduct Tax For Unclaimed Employee Benefits_ trong Payroll Entry / Salary Slip khi đang xử lý Lương.

{next}