<!-- add-breadcrumbs -->
# Quy đổi ngày nghỉ thành tiền

**Quy đổi ngày nghỉ thành tiền đề cập đến một khoản tiền nhận được để đổi lấy những ngày Nghỉ mà Nhân viên chưa sử dụng. Bạn có thể Xác nhận Quy đổi ngày nghỉ thành tiền cho các Loại nghỉ phép có thể quy đổi thành tiền.**

Để truy cập Quy đổi ngày nghỉ thành tiền, hãy đi tới:

> Home > Human Resources > Leaves > Leave Encashment


## 1. Điều kiện tiên quyết

Trước khi tạo Quy đổi ngày nghỉ thành tiền, bạn nên tạo các tài liệu sau:

1. [Employee](/docs/v16/user/manual/en/human-resources/leave-allocation)
1. [Leave Type](/docs/v16/user/manual/en/human-resources/leave-type)
1. [Leave Policy](/docs/v16/user/manual/en/human-resources/leave-policy)
1. [Leave Period](/docs/v16/user/manual/en/human-resources/leave-period)
1. [Salary Structure](/docs/v16/user/manual/en/human-resources/salary-structure)
1. [Salary Structure Assignment](/docs/v16/user/manual/en/human-resources/salary-structure-assignment)

## 2. Cách tạo Quy đổi ngày nghỉ thành tiền

1. Đi tới danh sách Leave Encashment, nhấn vào New.
1. Chọn Leave Period.
1. Chọn Employee. Sau khi chọn Employee, Phòng ban của Nhân viên sẽ tự động được lấy ra.
1. Chọn Leave Type mà ngày nghỉ sẽ được quy đổi thành tiền. Đảm bảo rằng Leave Type đó có thể quy đổi (ô 'Allow Encashment' trong Leave Type đã được tích chọn).
1. Chọn Encashment Date. Dựa trên ngày được chọn, số tiền sẽ được quy đổi trong Bút toán thanh toán lương (Payroll Entry) cụ thể đó.
1. Lưu và Xác nhận.

	<img class="screenshot" alt="Leave Encashment"
	src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-encashment-new.png">


> **Lưu ý:** Khi bạn chọn Employee và Leave Type, Số dư nghỉ phép (Leave Balance) và Số ngày có thể quy đổi (Encashable Days - là tổng số dư nghỉ phép trừ đi số ngày ngưỡng được thiết lập trong Leave Type) sẽ được hiển thị cùng với Số tiền quy đổi (Encashment Amount) dựa trên mức Quy đổi ngày nghỉ mỗi ngày được cấu hình trong Salary Structure được gán cho Nhân viên đó.


Khi Xác nhận Quy đổi ngày nghỉ thành tiền cho một Nhân viên, ERPNext sẽ tự động tạo một [Additional Salary](/docs/v16/user/manual/en/human-resources/additional-salary), khoản này sẽ được cộng vào Phiếu lương (Salary Slip) của Nhân viên khi xử lý bảng lương.



## 3. Các chủ đề liên quan

1. [Payroll Period](/docs/v16/user/manual/en/human-resources/payroll-period)
1. [Payroll Entry](/docs/v16/user/manual/en/human-resources/payroll-entry)
1. [Additional Salary](/docs/v16/user/manual/en/human-resources/additional-salary)