<!-- add-breadcrumbs -->
# Đơn xin nghỉ phép

**Đơn xin nghỉ phép là một tài liệu chính thức được Nhân viên tạo để xin nghỉ phép trong một khoảng thời gian cụ thể.**

ERPNext cho phép nhân viên của bạn đăng ký nghỉ phép thông qua Đơn xin nghỉ phép và được phê duyệt bởi Người phê duyệt nghỉ phép.

Để truy cập Đơn xin nghỉ phép, hãy đi tới:

> Home > Human Resources > Leaves > Leave Application

## 1. Điều kiện tiên quyết

Trước khi bạn tạo Đơn xin nghỉ phép, bạn nên có sẵn các tài liệu sau:

* [Department](department.md)
* [Leave Period](leave-period.md)
* [Holiday List](holiday-list.md)
* [Leave Type](leave-type.md)
* [Leave Policy](leave-policy.md)
* [Leave Allocation](leave-allocation.md)

## 2. Cách tạo Đơn xin nghỉ phép

1. Đi tới danh sách Leave Application, nhấn vào New.
1. Một bảng về Số ngày nghỉ được phân bổ (Allocated Leaves) sẽ được hiển thị. Dựa trên số ngày nghỉ đã sử dụng, số ngày nghỉ còn lại sẽ được hiển thị cho mỗi Loại nghỉ phép.

     <img class="screenshot" alt="Leave Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-app.png">


1. Chọn Tên nhân viên (Employee Name) và Loại nghỉ phép (Leave Type).
1. Thiết lập thời gian nghỉ bằng Ngày bắt đầu (From Date) và Ngày kết thúc (To Date). Dựa trên các ngày đã chọn, các trường 'Tổng số ngày nghỉ' (Total Leave Days) và 'Số ngày nghỉ còn lại trước khi đăng ký' (Leave Balance Before Application) sẽ được hiển thị.
1. Nếu xin nghỉ nửa ngày, hãy chọn ô 'Nghỉ nửa ngày' (Half Day).
1. Nhập Lý do nghỉ phép (Reason for Leave).

    <img class="screenshot" alt="Leave Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-app1.png">


1. Chọn Người phê duyệt nghỉ phép (Leave Approver).
1. Chọn Ngày ghi sổ (Posting Date) của Đơn xin nghỉ phép.
1. Tích vào ô 'Theo dõi qua Email' (Follow via Email) để gửi thông báo về Đơn xin nghỉ phép cho Người phê duyệt nghỉ phép.
1. Bạn cũng có thể liên kết Phiếu lương (Salary Slip) của Nhân viên trong Đơn xin nghỉ phép để lưu hồ sơ.

    <img class="screenshot" alt="Leave Application" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-app3.png">

1. Nhấn vào Lưu (Save). Sau khi Nhân viên lưu Đơn xin nghỉ phép, trạng thái của Đơn xin nghỉ phép sẽ chuyển sang 'Mở' (Open), và một email sẽ được gửi đến Người phê duyệt nghỉ phép để phê duyệt. Mẫu thông báo phê duyệt nghỉ phép có thể được cấu hình trong [HR Settings](hr-settings.md) tại phần Leave Settings.
1. Sau khi Người phê duyệt nghỉ phép nhận được email, họ có thể Phê duyệt (Approve), Từ chối (Reject), hoặc Hủy (Cancel) Đơn xin nghỉ phép. Sau khi việc này hoàn tất, Người phê duyệt nghỉ phép có thể Xác nhận (Submit) Đơn xin nghỉ phép. Khi được Xác nhận, trạng thái của tài liệu sẽ thay đổi tương ứng, và một email sẽ được gửi cho Nhân viên để thông báo về việc này.


> **Lưu ý:** Đơn xin nghỉ phép không thể được Xác nhận nếu Lương đã được xử lý cho khoảng thời gian nghỉ đó.

Quy trình luồng công việc của Đơn xin nghỉ phép được tóm tắt dưới đây:

- Nhân viên đăng ký nghỉ phép thông qua Đơn xin nghỉ phép.
- Người phê duyệt nhận được thông báo qua email. Để làm điều này, ô "Follow via Email" phải được tích chọn.
- Người phê duyệt xem xét Đơn xin nghỉ phép.
- Người phê duyệt phê duyệt/từ chối/hủy Đơn xin nghỉ phép.
- Nhân viên nhận được thông báo về trạng thái Đơn xin nghỉ phép của mình.

## 3. Các tính năng

### 3.1 Thiết lập Người phê duyệt nghỉ phép

Người phê duyệt nghỉ phép là người dùng có thể phê duyệt Đơn xin nghỉ phép của một Nhân viên. Trong phiên bản ERPNext 12, Người phê duyệt nghỉ phép có thể được thiết lập ở hai cấp độ:

* **Cấp độ Phòng ban:** Người phê duyệt nghỉ phép cho mỗi phòng ban có thể được cấu hình trong danh mục [Department](department.md). Có thể thiết lập nhiều Người phê duyệt nghỉ phép trong một Phòng ban. Người phê duyệt nghỉ phép đầu tiên trong danh sách sẽ được coi là Người phê duyệt mặc định.


    <img class="screenshot" alt="Leave Application - Leave Approvers" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-app4.png">

    Khi một Nhân viên thuộc một phòng ban cụ thể đăng ký nghỉ phép, những Người phê duyệt nghỉ phép được thiết lập trong danh mục phòng ban của Nhân viên đó sẽ được coi là Người phê duyệt của họ.


* **Cấp độ Nhân viên:**
Người phê duyệt nghỉ phép cũng có thể được thiết lập theo từng Nhân viên trong danh mục nhân viên.


 <img class="screenshot" alt="Leave Application - Leave Approvers" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-level-approvers.png">


Nếu Người phê duyệt nghỉ phép được thiết lập ở cả cấp độ Nhân viên và cấp độ Phòng ban, thì Người phê duyệt cấp Nhân viên sẽ được coi là Người phê duyệt mặc định trong trường hợp này.

Khi một Đơn xin nghỉ phép mới được tạo, nếu người phê duyệt được chọn không có quyền truy cập, tài liệu sẽ được chia sẻ với người phê duyệt với quyền "submit".

 **Mẹo:** Nếu bạn muốn tất cả người dùng có thể tự tạo Đơn xin nghỉ phép của riêng họ, bạn có thể thiết lập "Mã nhân viên" (Employee ID) của họ làm quy tắc khớp (match rule) trong cài đặt Quyền Đơn xin nghỉ phép (Leave Application Permission). Kiểm tra [Setting Up Permissions](../setting-up/users-and-permissions/user-permissions.html.md) để biết thêm thông tin.

> **Ghi chú bổ sung:**

>* Thời gian Đơn xin nghỉ phép phải nằm trong một kỳ Phân bổ nghỉ phép (Leave Allocation period) duy nhất. Trong trường hợp bạn xin nghỉ kéo dài qua các kỳ phân bổ nghỉ phép, bạn phải tạo hai bản ghi Đơn xin nghỉ phép khác nhau.
>* Thời gian Đơn xin nghỉ phép phải nằm trong kỳ Phân bổ nghỉ phép mới nhất.
>* Nhân viên không thể đăng ký nghỉ phép vào những ngày đã được thêm vào [Leave Block List](leave-block-list.md).

Để hiểu cách ERPNext cho phép bạn cấu hình nghỉ phép cho nhân viên, hãy kiểm tra [Leaves](leave-management-intro.md).


## 3. Các chủ đề liên quan

1. [Leave Type](leave-type.md)
1. [Leave Period](leave-period.md)
1. [Leave Policy](leave-policy.md)
1. [Leave Allocation](leave-allocation.md)
1. [Leave Block List](leave-block-list.md)