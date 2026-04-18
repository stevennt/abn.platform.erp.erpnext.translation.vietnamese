<!-- add-breadcrumbs -->
# Phòng ban

**Phòng ban là một khu vực chức năng chuyên biệt hoặc một bộ phận trong một tổ chức.**

Bạn có thể cấu hình các Phòng ban trong tổ chức của mình, thiết lập Danh sách chặn nghỉ phép (Leave Block List), cũng như Người phê duyệt nghỉ phép và Người phê duyệt chi phí cho phòng ban đó.

Để truy cập Phòng ban, hãy đi đến:

> Home > Nhân sự > Nhân viên > Phòng ban

Phòng ban là một dữ liệu chính có cấu trúc cây, điều này có nghĩa là bạn có thể tạo các phòng ban cha và các phòng ban con như hiển thị dưới đây:

<img class="screenshot" alt="Department Tree" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/department-tree.png">

> **Lưu ý:** Ô kiểm 'Is Group' cần được tích nếu Phòng ban đó là một phòng ban cha.


## 1. Điều kiện tiên quyết

Trước khi tạo một Phòng ban, bạn nên tạo các tài liệu sau:

* [Công ty](../setting-up/company-setup)
* [Danh sách chặn nghỉ phép](../human-resources/leave-block-list)

## 2. Cách tạo Phòng ban

1. Đi đến danh sách Phòng ban, nhấn vào **Mới**.
1. Nhập tên Phòng ban.
1. Chọn tên Công ty.
1. Chọn Danh sách chặn nghỉ phép (tùy chọn) áp dụng cho phòng ban này.
1. **Lưu**.

    <img class="screenshot" alt="Department" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/department.png">


## 3. Các tính năng

### 3.1 Người phê duyệt nghỉ phép và chi phí

Bạn có thể thiết lập Người phê duyệt nghỉ phép và Người phê duyệt chi phí cho một Phòng ban cụ thể tương ứng trong bảng 'Leave Approver' và 'Expense Approver'.

<img class="screenshot" alt="Leave and Expense Approver" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-and-expense.png">


> **Lưu ý:** Có thể thiết lập nhiều Người phê duyệt nghỉ phép và chi phí cho một Phòng ban cụ thể. Tuy nhiên, Người phê duyệt đầu tiên trong danh sách sẽ được thiết lập làm Người phê duyệt mặc định.





## 4. Các chủ đề liên quan

1. [Loại hình nhân viên](../human-resources/employment-type)
1. [Cấp bậc nhân viên](../human-resources/employee-grade)
1. [Chi nhánh nhân viên](../human-resources/branch)
1. [Chức danh nhân viên](../human-resources/designation)