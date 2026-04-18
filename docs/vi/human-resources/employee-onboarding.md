# Tiếp nhận Nhân viên

**Trong quá trình tuyển dụng một Nhân viên, có một tập hợp các hoạt động tiêu chuẩn cần được thực hiện. Tính năng này giúp bạn duy trì danh mục các hoạt động này và tạo ra một tập hợp các nhiệm vụ tại thời điểm tuyển dụng mỗi Nhân viên.**

Tiếp nhận Nhân viên được tạo cho một Ứng viên xin việc, người đã được phê duyệt để tuyển dụng.

**Trường hợp sử dụng:** Giả sử sau đây là các hoạt động cần được thực hiện ngay khi một ứng viên xin việc được phê duyệt để tuyển dụng.

- Thực hiện kiểm tra lý lịch chuyên môn và pháp lý
- Tạo hồ sơ Nhân viên
- Tạo Tài khoản Email
- Tạo thẻ căn cước
- Phân bổ nghỉ phép


Trong ERPNext, các hoạt động tiêu chuẩn này có thể được theo dõi trong Mẫu Tiếp nhận Nhân viên. Để truy cập Tiếp nhận Nhân viên, hãy đi đến:

> Human Resources > Employee Lifecycle > Employee Onboarding

## 1. Điều kiện tiên quyết

Trước khi tạo Tiếp nhận Nhân viên, bạn nên tạo các tài liệu sau:

* [Job Applicant](job-applicant.md)
* [Employee](employee.md)
* [Department](department.md)
* [Designation](designation.md)
* [Employee Grade](employee-grade.md)

## 2. Cách tạo Tiếp nhận Nhân viên

1. Đi đến: Employee Onboarding > New.
1. Chọn Ứng viên xin việc. Sau khi Ứng viên xin việc được chọn, Nhân viên tương ứng sẽ tự động được lấy dữ liệu.
1. Chọn [Employee Onboarding Template](#31-employee-onboarding-template). Dựa trên mẫu được chọn, các thông tin như Phòng ban, Chức danh và Cấp bậc Nhân viên sẽ tự động được lấy (nếu đã được đề cập trong Mẫu Tiếp nhận).
1. Nhập Ngày gia nhập.
1. Lưu và Xác nhận.


  <img class="screenshot" alt="Onboarding Template" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-onboarding1.png">



> Lưu ý 1: Nếu chưa tạo Mẫu Tiếp nhận Nhân viên, bạn có thể điền trực tiếp thông tin tiếp nhận trong chính DocType Employee Onboarding.

> Lưu ý 2: 'Trạng thái' của Tiếp nhận Nhân viên sẽ chuyển sang Hoàn thành sau khi tất cả các Hoạt động liên quan đã hoàn tất.


## 3. Các tính năng

### 3.1 Mẫu Tiếp nhận Nhân viên

Mẫu Tiếp nhận Nhân viên là một bản kế hoạch chứa danh sách các Hoạt động được xác định trước để Tiếp nhận Nhân viên. Một Mẫu Tiếp nhận Nhân viên có thể được tạo cho một Phòng ban, Chức danh và Cấp bậc Nhân viên cụ thể.

Để tạo một Mẫu Tiếp nhận Nhân viên mới:

1. Đi đến: Human Resources > Employee Lifecycle > Employee Onboarding Template > New.
1. Nhập Phòng ban, Chức danh và Cấp bậc Nhân viên (tùy chọn).
1. Đề cập các Hoạt động để tiếp nhận. Đối với mỗi Hoạt động, bạn cũng có thể đề cập Người dùng hoặc Vai trò, hoặc một trong hai, người mà Hoạt động này sẽ được giao.

  <img class="screenshot" alt="Onboarding Template" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/onboarding-template.png">


### 3.2 Nhiệm vụ và Phân công

Khi Xác nhận Tiếp nhận Nhân viên, một [Project](../projects/project.md) sẽ được tạo. Trong Dự án, các [Tasks](../projects/tasks.md) cũng sẽ được tạo cho mỗi Hoạt động.

Bạn có thể xem các Dự án và Nhiệm vụ đã được tạo như hiển thị dưới đây:

<img class="screenshot" alt="Onboarding Template" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/project-task.png">

Ngoài ra, mỗi Hoạt động có thể được gán trọng số dựa trên tầm quan trọng của nó.

<img class="screenshot" alt="Tasks and Assignments" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-onboarding3.png">

Dựa trên tiến độ của các Nhiệm vụ, tiến độ có thể được cập nhật trong quy trình Tiếp nhận Nhân viên.


### 3.3 Tạo Nhân viên

Bạn có thể tạo trực tiếp một Nhân viên thông qua DocType Employee Onboarding (nếu chưa được tạo) sau khi tất cả các nhiệm vụ tiếp nhận bắt buộc đã hoàn thành.

<img class="screenshot" alt="Onboarding Template" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/onboarding-employee.png">


## 4. Các chủ đề liên quan

1. [Employee Promotion](employee_promotion.md)
1. [Employee Separation](employee-separation.md)
1. [Employee Transfer](employee_transfer.md)