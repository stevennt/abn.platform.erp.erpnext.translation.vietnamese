<!-- add-breadcrumbs -->
# Bút toán thanh toán lương

**Bảng lương là tổng tất cả các khoản thù lao mà một doanh nghiệp phải trả cho nhân viên của mình trong một khoảng thời gian nhất định hoặc vào một ngày cụ thể.**

Trong ERPNext, Bút toán thanh toán lương cho phép xử lý lương hàng loạt cho nhân viên. Nói cách khác, là xử lý phiếu lương của tất cả nhân viên trong một lần thực hiện. Việc xử lý hàng loạt có thể áp dụng cho toàn Công ty hoặc dựa trên các danh mục: Chi nhánh, Phòng ban hoặc Chức danh.

Để truy cập Bút toán thanh toán lương, hãy đi đến:

> Home > Human Resources > Payroll > Payroll Entry



## 1. Cách tạo một Bút toán thanh toán lương


1. Đi đến danh sách Bút toán thanh toán lương, nhấp vào Mới.
1. Chọn Tần suất thanh toán lương.
1. Chọn Chi nhánh, Chức danh và Phòng ban để lọc nhân viên (tùy chọn).
1. Chọn Dự án (tùy chọn) nếu bạn muốn chạy bảng lương theo một dự án.
1. Chọn các ô kiểm 'Validate Attendance' (Xác nhận chấm công) và 'Salary Slip Based on Timesheet' (Phiếu lương dựa trên bảng chấm công) trong trường hợp bạn muốn khấu trừ lương dựa trên việc chấm công và nếu bạn cũng muốn xem xét bảng chấm công của nhân viên tương ứng.
1. Chọn Tài khoản thanh toán để thực hiện Bút toán ngân hàng.
1. Lưu.


Sau khi thông tin được lưu, hãy nhấp vào nút **Get Employees** để lấy danh sách Nhân viên mà Phiếu lương sẽ được tạo dựa trên các tiêu chí đã chọn.

Sau khi danh sách Nhân viên được lấy ra, hãy nhấp vào nút **Create Salary Slips** để tạo các Phiếu lương.

<img class="screenshot" alt="Payroll Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/payroll-entry-get-employees.png">

> **Lưu ý:** Nếu các Phiếu lương đã được tạo, hệ thống sẽ không tạo thêm bất kỳ Phiếu lương nào nữa. Bạn cũng có thể chỉ lưu biểu mẫu dưới dạng Nháp và tạo Phiếu lương sau.


## 2. Các tính năng

### 2.1 Trích trước lương

Sau khi kiểm tra các Phiếu lương, bạn có thể Xác nhận tất cả chúng cùng một lúc bằng cách nhấp vào nút **Submit Salary Slip**.

<img class="screenshot" alt="Payroll Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/payroll-entry.png">

Thao tác này cũng sẽ hạch toán tài khoản Phải trả lương mặc định đối với các Khoản mục chi phí tương ứng (như đã cấu hình trong Thành phần lương) để ghi nhận việc trích trước lương cho nhân viên.

**Trung tâm chi phí:**
Bạn có thể chọn Trung tâm chi phí trong Bút toán thanh toán lương để hạch toán các chi phí.

Nếu bạn muốn hạch toán chi phí cho nhiều trung tâm chi phí dựa trên Nhân viên/Phòng ban, bạn có thể thực hiện bằng cách thiết lập Trung tâm chi phí lương trong danh mục gốc Nhân viên/Phòng ban. Trung tâm chi phí được chỉ định trong danh mục gốc Nhân viên/Phòng ban sẽ được ưu tiên hơn Trung tâm chi phí được chọn trong Bút toán thanh toán lương.

<img class="screenshot" alt="Payroll Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/payroll-make-accrual-entry.png">

> **Lưu ý:** Việc Xác nhận các Phiếu lương riêng lẻ bằng tay sẽ không tạo Bút toán để ghi nhận trích trước lương.

### 2.2 Thanh toán lương

Bước cuối cùng là hạch toán Thanh toán lương.

Lương trong các doanh nghiệp thường được xử lý với tính bảo mật cực cao. Trong hầu hết các trường hợp, các công ty thực hiện một lệnh thanh toán duy nhất tới ngân hàng bao gồm tất cả các khoản lương và ngân hàng sẽ phân phối lương tới tài khoản lương của từng nhân viên.

Bằng cách này, chỉ có một bút toán thanh toán duy nhất trong sổ sách kế toán của công ty và bất kỳ ai có quyền truy cập vào tài khoản của công ty cũng sẽ không có quyền truy cập vào mức lương cá nhân.

Bút toán thanh toán lương là một Bút toán ghi nợ tổng các thành phần lương loại Thu nhập và ghi có tổng các thành phần lương loại Khấu trừ của tất cả Nhân viên vào tài khoản mặc định được thiết lập ở cấp độ Thành phần lương cho mỗi thành phần.

Để tạo chứng từ thanh toán lương từ Bút toán thanh toán lương, hãy nhấp vào nút **Make Bank Entry**.

Bút toán thanh toán lương sẽ dẫn bạn đến Bút toán với các bộ lọc liên quan để xem các Chứng từ bút toán nháp đã được tạo. Bạn sẽ phải thiết lập số tham chiếu và ngày cho các giao dịch và Xác nhận Bút toán.

<img class="screenshot" alt="Payroll Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/payroll-make-bank-entry.png">

> **Lưu ý:** Đối với các Thành phần lương là Phúc lợi linh hoạt và có tích chọn _Create Separate Payment Entry Against Benefit Claim_ (Tạo Bút toán thanh toán riêng cho yêu cầu phúc lợi), ERPNext sẽ hạch toán các Bút toán nháp riêng biệt.


## 3. Các chủ đề liên quan

1. [Thành phần lương](salary-component.md)
1. [Cấu trúc lương](salary-structure.md)
1. [Kỳ lương](payroll-period.md)
1. [Bút toán](../accounts/journal-entry.md)

{next}