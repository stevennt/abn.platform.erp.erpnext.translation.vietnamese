# Danh sách chặn nghỉ phép

**Danh sách chặn nghỉ phép là danh sách các ngày trong năm mà nhân viên không thể đăng ký nghỉ phép.**

 Để truy cập Danh sách chặn nghỉ phép, hãy đi tới:

> Home > Human Resources > Leaves > Leave Block List

ERPNext cho phép bạn xác định danh sách những Người phê duyệt nghỉ phép có thể phê duyệt Đơn xin nghỉ phép vào những ngày bị chặn trong trường hợp khẩn cấp. Bạn cũng có thể xác định xem danh sách này sẽ được áp dụng cho toàn bộ công ty hay cho bất kỳ bộ phận cụ thể nào.

## 1. Điều kiện tiên quyết

Trước khi bạn tạo Danh sách chặn nghỉ phép, bạn nên có sẵn các tài liệu sau:

* [Company](../setting-up/company-setup.md)
* [Department](department.md)
* [Leave Period](leave-period.md)
* [Holiday List](holiday-list.md)


## 2. Cách tạo Danh sách chặn nghỉ phép

1. Đi tới Leave Block list, và nhấn vào New.
1. Nhập Leave Block List Name.
1. Nhập Block Date và Reason trong bảng 'Leave Block List Dates'.
1. Nhập Users to approve Leave Applications for Blocked Days trong bảng 'Leave BLock List Allowed'.
1. Lưu.


    <img class="screenshot" alt="Leave Block List"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-block-list.png">

> **Lưu ý:** Bật tùy chọn 'Applies to Company' nếu bạn muốn Danh sách chặn nghỉ phép được áp dụng cho toàn bộ Công ty. Nếu không được chọn, danh sách sẽ phải được thêm vào từng [Department](department.md) nơi cần áp dụng.


## 3. Các chủ đề liên quan

1. [Leave Type](leave-type.md)
1. [Leave Period](leave-period.md)
1. [Leave Policy](leave-policy.md)
1. [Leave Allocation](leave-allocation.md)
1. [Leave Application](leave-application.md)