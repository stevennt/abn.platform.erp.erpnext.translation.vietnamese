# Kỳ nghỉ phép

**Kỳ nghỉ phép là một khoảng thời gian mà trong đó các ngày nghỉ được phân bổ.**

Hầu hết các công ty quản lý việc nghỉ phép dựa trên một Kỳ nghỉ phép, tương ứng với một năm dương lịch hoặc năm tài chính. Để truy cập Kỳ nghỉ phép, hãy đi đến:

> Home > Human Resources > Leaves > Leave Period

## 1. Điều kiện tiên quyết

Trước khi tạo Kỳ nghỉ phép, bạn nên tạo các mục sau:

* [Company](../setting-up/company-setup.md)
* [Holiday List](holiday-list.md)

## 2. Cách tạo Kỳ nghỉ phép

1. Đi đến danh sách Leave Period, nhấn vào New.
1. Nhập Ngày bắt đầu (From Date) và Ngày kết thúc (To Date) của Kỳ nghỉ phép.
1. Chọn tên Công ty mà Kỳ nghỉ phép này được áp dụng.
1. Lưu.

Kỳ nghỉ phép cũng cho phép bạn chọn một [Holiday List for Optional Leaves](holiday-list.md) (tùy chọn) để được xem xét khi phân bổ các ngày nghỉ tùy chọn cho giai đoạn đó.

> **Lưu ý:** 'Holiday List for Optional Leaves' không giống với 'Holiday List' thông thường. Danh sách này sẽ chỉ chứa danh sách các ngày lễ tùy chọn. 'Holiday List for Optional Leaves' có thể được tạo từ tài liệu [Holiday List](holiday-list.md). Bạn có thể tạo hai Holiday Lists cho một Kỳ nghỉ phép; một danh sách chứa các ngày lễ thông thường và danh sách kia dành cho các ngày lễ tùy chọn.

Ngoài ra, bạn có thể tích vào ô 'Is Active' nếu muốn kích hoạt Kỳ nghỉ phép cụ thể này.


<img class="screenshot" alt="Leave Period"
	src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-period.png">

## 3. Cấp phép nghỉ bằng Kỳ nghỉ phép

> Trong phiên bản 12, các ngày nghỉ có thể được cấp thông qua Kỳ nghỉ phép bằng nút "Grant Leaves". Trong phiên bản 13, các ngày nghỉ sẽ được cấp bằng cách sử dụng [Leave Policy Assignment](leave-policy-assignment.md).

Sau khi thông tin được lưu, Kỳ nghỉ phép cũng sẽ được sử dụng như một công cụ để giúp bạn cấp phép nghỉ cho một nhóm nhân viên.

Nút **Grant** sẽ tạo ra các Phân bổ nghỉ phép (Leave Allocations) dựa trên [Leave Policy](leave-policy.md) áp dụng cho từng Nhân viên. Bạn có thể phân bổ nghỉ phép dựa trên [Employee Grade](employee-grade.md), [Department](department.md) hoặc [Designation](designation.md) như hiển thị dưới đây.


<img class="screenshot" alt="Leave Period"
	src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/grant-button.gif">


## 3. Các chủ đề liên quan

1. [Leave Allocation](leave-allocation.md)
1. [Leave Policy](leave-policy.md)
1. [Leave Type](leave-type.md)