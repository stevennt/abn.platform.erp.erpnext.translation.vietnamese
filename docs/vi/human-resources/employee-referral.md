<!-- add-breadcrumbs -->

# Giới thiệu nhân viên

> Được giới thiệu trong Phiên bản 13

Tuyển dụng nội bộ là một trong những quy trình tốt nhất để tuyển dụng, đồng thời giúp tiết kiệm công sức và chi phí.
Giới thiệu nhân viên là quy trình mà các nhân viên hiện tại giới thiệu một ứng viên phù hợp từ mạng lưới của họ cho một chức danh/vị trí đang trống.

Trong ERPNext, bạn có thể quản lý việc Giới thiệu nhân viên.

Để truy cập Giới thiệu nhân viên, hãy đi đến:

> Human Resources > Recruitment > Employee Referral


## 1. Điều kiện tiên quyết
1. [Employee](employee.md)
1. [Additional Salary](additional-salary.md)
1. [Job Applicant](job-applicant.md)

## 2. Cách tạo Giới thiệu nhân viên
1. Đi đến Employee Referral > Add Employee Referral.
1. Điền các thông tin cơ bản của người mà bạn muốn giới thiệu như Tên, Họ, Email, v.v.
1. Chọn Employee trong mục Referrer.
1. Lưu và Xác nhận.


<img class="screenshot" alt="Leave Allocations"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-referral.png">

## 3. Các tính năng

### 3.1 Tạo Job Applicant và tự động đồng bộ trạng thái từ Job Applicant
Khi bạn xác nhận một tài liệu giới thiệu nhân viên, trạng thái ban đầu sẽ là "Pending". Sau khi xác nhận tài liệu, nút "Create Job Applicant" sẽ xuất hiện ở góc trên bên phải.

Nhấp vào nút này sẽ tạo một **Job Applicant** mới với trạng thái "Open". Trạng thái của tài liệu **Employee Referral** sẽ chuyển thành "In Process".

<img class="screenshot" alt="Leave Allocations"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/create-job-applicant.png">

Khi ai đó thay đổi trạng thái của **Job Applicant** thành "Hold" hoặc "Replied", trạng thái của **Employee Referral** vẫn sẽ là "In Process". Nếu trạng thái của **Job Applicant** chuyển thành "Accepted" hoặc "Rejected", trạng thái của tài liệu **Employee Referral** cũng sẽ lần lượt chuyển thành "Accepted" hoặc "Rejected".

### 3.2 Quản lý tiền thưởng giới thiệu
Nhiều công ty cung cấp tiền thưởng cho nhân viên của họ cho những trường hợp giới thiệu như vậy. ERPNext cho phép bạn theo dõi việc thanh toán tiền thưởng cho nhân viên vì sự giới thiệu của họ.

Đối với tiền thưởng giới thiệu, bạn cần tích vào ô "Is applicable for referral bonus" trước khi xác nhận tài liệu. Sau khi xác nhận tài liệu, nút "Create Additional Salary" sẽ xuất hiện ở góc trên bên phải, nếu trạng thái là "Accepted".

<img class="screenshot" alt="Leave Allocations"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/referral-bonus.png">

Khi nhấp vào, nó sẽ chuyển hướng bạn đến biểu mẫu Additional salary, nơi bạn cần chọn Salary component và Payroll date, sau đó bạn cần lưu và xác nhận tài liệu.

<img class="screenshot" alt="Leave Allocations"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/create-referral-bonus.png">