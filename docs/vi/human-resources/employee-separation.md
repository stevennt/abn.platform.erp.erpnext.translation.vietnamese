# Nghỉ việc của Nhân viên

**Nghỉ việc của Nhân viên là tình huống khi thỏa thuận dịch vụ của một Nhân viên với tổ chức kết thúc và Nhân viên đó rời khỏi tổ chức.**

Nghỉ việc của Nhân viên được tạo cho một Nhân viên đã thôi việc hoặc bị chấm dứt hợp đồng khỏi tổ chức.

**Trường hợp sử dụng:** Giả sử sau đây là các hoạt động cần được thực hiện ngay khi một Nhân viên cần nghỉ việc khỏi tổ chức.

- Thu hồi máy tính xách tay
- Thanh toán các khoản nợ/công nợ
- Xóa tài khoản Email của Nhân viên
- Thu hồi thẻ căn cước/thẻ nhân viên


Trong ERPNext, các hoạt động tiêu chuẩn này có thể được theo dõi trong Mẫu Nghỉ việc của Nhân viên. Để truy cập Nghỉ việc của Nhân viên, hãy đi đến:

> Human Resources > Employee Lifecycle > Employee Separation

## 1. Điều kiện tiên quyết

Trước khi tạo Nghỉ việc của Nhân viên, bạn nên tạo các tài liệu sau:

* [Employee](employee.md)
* [Department](department.md)
* [Designation](designation.md)
* [Employee Grade](employee-grade.md)

## 2. Cách tạo Nghỉ việc của Nhân viên

1. Đi đến: Employee Separation > New.
1. Chọn Nhân viên. Sau khi Nhân viên được chọn, các thông tin Nhân viên tương ứng như Phòng ban, Chức danh và Cấp bậc Nhân viên sẽ tự động được lấy ra.
1. Chọn [Employee Separation Template](#31-employee-separation-template). Dựa trên mẫu được chọn, các thông tin như Phòng ban, Chức danh và Cấp bậc Nhân viên sẽ tự động được lấy ra (nếu đã được đề cập trong Mẫu Nghỉ việc).
1. Nhập Ngày Thư thôi việc.
1. Ngoài ra, bạn cũng có thể nhập Tóm tắt Phỏng vấn thôi việc.
1. Lưu và Xác nhận.


  <img class="screenshot" alt="Separation Template" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-separation.png">



> Lưu ý 1: Nếu Mẫu Nghỉ việc của Nhân viên chưa được tạo, bạn có thể điền trực tiếp thông tin nghỉ việc trong chính DocType Employee Separation.

> Lưu ý 2: 'Status' (Trạng thái) của Nghỉ việc của Nhân viên sẽ chuyển sang Completed (Hoàn thành) sau khi tất cả các Hoạt động liên quan đã hoàn tất.


## 3. Các tính năng

### 3.1 Mẫu Nghỉ việc của Nhân viên (Employee Separation Template)

Mẫu Nghỉ việc của Nhân viên là một bản thiết kế chứa danh sách các Hoạt động được định nghĩa trước cho việc Nghỉ việc của Nhân viên. Một Mẫu Nghỉ việc của Nhân viên có thể được tạo cho một Phòng ban, Chức danh và Cấp bậc Nhân viên cụ thể.

Để tạo một Mẫu Nghỉ việc của Nhân viên mới:

1. Đi đến: Human Resources > Employee Lifecycle > Employee Separation Template > New.
1. Nhập Phòng ban, Chức danh và Cấp bậc Nhân viên (tùy chọn).
1. Đề cập các Hoạt động để nghỉ việc. Đối với mỗi Hoạt động, bạn cũng có thể đề cập Người dùng hoặc Vai trò, hoặc một trong hai, người sẽ được giao Hoạt động này.

  <img class="screenshot" alt="Onboarding Template" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-separation-template.png">


### 3.2 Công việc và Phân công

Khi Xác nhận Nghỉ việc của Nhân viên, một [Project](/docs/v13/user/videos/learn/project-and-task) sẽ được tạo. Trong Dự án, các [Tasks](/docs/v13/user/videos/learn/project-and-task) cũng sẽ được tạo cho mỗi Hoạt động.

Bạn có thể xem các Dự án và Công việc đã tạo thông qua View > Project/ Tasks.


Ngoài ra, mỗi Hoạt động có thể được gán trọng số dựa trên tầm quan trọng của nó.

<img class="screenshot" alt="Tasks and Assignments" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-sep1.png">

Dựa trên tiến độ của các Công việc, tiến độ có thể được cập nhật trong quy trình Nghỉ việc của Nhân viên.


### 3.3 Trạng thái Nhân viên

Bạn có thể xem trực tiếp Nhân viên đã nghỉ việc thông qua DocType Employee Separation qua View > Employee sau khi biểu mẫu được xác nhận.


## 4. Các chủ đề liên quan

1. [Employee Onboarding](employee-onboarding.md)
1. [Employee Promotion](employee_promotion.md)
1. [Employee Separation](employee-separation.md)