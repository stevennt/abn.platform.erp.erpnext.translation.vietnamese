<!-- add-breadcrumbs -->
# Phân bổ Chính sách Nghỉ phép

> Được giới thiệu trong Phiên bản 16

Phân bổ Chính sách Nghỉ phép trong ERPNext được sử dụng để phân bổ các loại nghỉ phép cho nhân viên dựa trên các chính sách đã được tạo. Để truy cập Phân bổ Chính sách Nghỉ phép, hãy đi đến:

> Home > Human Resources > Leaves > Leave Policy Assignment

## 1. Điều kiện tiên quyết

Trước khi tạo Phân bổ Chính sách Nghỉ phép, bạn nên tạo các mục sau:

* [Nhân viên](/docs/v16/user/manual/en/human-resources/employee)
* [Chính sách nghỉ phép](/docs/v16/user/manual/en/human-resources/leave-policy)

## 2. Cách tạo Phân bổ Chính sách Nghỉ phép

1. Đi đến Leave Policy Assignment, nhấn vào New.
1. Chọn Nhân viên và Chính sách nghỉ phép.
1. Chọn Phân bổ dựa trên các tùy chọn sau nếu cần:
    * Nếu "Assignment based on" được đặt là Leave Period, bạn cần chọn Leave Period tương ứng. Ngày Effective From và Effective To sẽ được thiết lập tự động dựa trên Leave Period đã chọn.
    * Nếu "Assignment based on" được đặt là Joining Date, ngày Effective From sẽ được thiết lập theo Ngày gia nhập của nhân viên.
    * Nếu "Assignment based on" được để trống, bạn sẽ phải thiết lập ngày Effective From và Effective To một cách thủ công.
1. Lưu và Xác nhận.

<img class="screenshot" alt="Leave Policy Assignment"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-policy-assignment.png">

Khi xác nhận, Leave Allocation sẽ được tự động tạo dựa trên [Chính sách nghỉ phép](/docs/v16/user/manual/en/human-resources/leave-policy) như hiển thị dưới đây.

<img class="screenshot" alt="Leave Allocations"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/granted-leaves.png">

## 3. Tính năng
### 3.1 Phân bổ Chính sách Nghỉ phép hàng loạt

ERPNext cũng cho phép tạo nhiều Phân bổ Chính sách Nghỉ phép cho nhiều nhân viên cùng lúc.

1. Đi đến danh sách Leave Policy Assignment, nhấn vào Bulk Leave Policy Assignment.
1. Một hộp thoại sẽ xuất hiện, hãy Chọn Nhân viên. Bạn có thể lọc nhân viên dựa trên Công ty (Company) và Phòng ban (Department) hoặc bạn cũng có thể sử dụng các bộ lọc tiêu chuẩn bằng cách nhấn vào Add Filters.
1. Chọn Chính sách nghỉ phép và các ngày Effective From, Effective To.
1. Nhấn vào Assign.

<img class="screenshot" alt="Bulk Leave Policy Assignment" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/bulk-leave-policy-assignment.png">

Khi bạn nhấn vào Assign, hệ thống sẽ tự động tạo và xác nhận Leave Policy Assignment, đồng thời phân bổ nghỉ phép dựa trên Chính sách nghỉ phép.