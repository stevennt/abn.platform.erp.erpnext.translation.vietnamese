# Phân bổ nghỉ phép

**Phân bổ nghỉ phép cho phép bạn phân bổ một số lượng ngày nghỉ cụ thể của một loại nghỉ phép nhất định cho một Nhân viên.**

Để truy cập Phân bổ nghỉ phép, hãy đi tới:

> Trang chủ > Nhân sự > Nghỉ phép > Phân bổ nghỉ phép

## 1. Điều kiện tiên quyết

Trước khi tạo Phân bổ nghỉ phép, bạn nên tạo các tài liệu sau:

* [Nhân viên](/docs/v16/user/manual/vi/human-resources/employee)
* [Loại nghỉ phép](/docs/v16/user/manual/vi/human-resources/leave-type)
* [Kỳ nghỉ phép](/docs/v16/user/manual/vi/human-resources/leave-period)
* [Chính sách nghỉ phép](/docs/v16/user/manual/vi/human-resources/leave-policy)

## 2. Cách tạo Phân bổ nghỉ phép

1. Đi tới danh sách Phân bổ nghỉ phép, nhấn vào Mới.
1. Chọn Nhân viên, Loại nghỉ phép, Từ ngày và Đến ngày.
1. Nhập số lượng Nghỉ phép mới được phân bổ cho Loại nghỉ phép cụ thể đó.
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Leave Allocation"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-allocation.png">

> **Lưu ý:** Bật tùy chọn 'Cộng dồn ngày nghỉ chưa sử dụng từ các lần phân bổ trước' trong trường hợp bạn muốn chuyển số ngày nghỉ chưa sử dụng từ kỳ phân bổ trước cho Loại nghỉ phép cụ thể này.

### 2.1 Phân bổ nghỉ phép thông qua Kỳ nghỉ phép

 Các ngày nghỉ thường được phân bổ cho một [Kỳ nghỉ phép](/docs/v16/user/manual/vi/human-resources/leave-period) nhất định. Sau khi Kỳ nghỉ phép được tạo và Lưu, bạn có thể nhấn vào nút **Cấp** để tạo các Phân bổ nghỉ phép dựa trên [Chính sách nghỉ phép](/docs/v16/user/manual/vi/human-resources/leave-policy) áp dụng cho mỗi Nhân viên.

 <img class="screenshot" alt="Grant Leaves from Leave Period"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/grant-button.png">

 Bạn có thể phân bổ ngày nghỉ dựa trên [Cấp bậc nhân viên](/docs/v16/user/manual/vi/human-resources/employee-grade), [Phòng ban](/docs/v16/user/manual/vi/human-resources/department) hoặc [Chức danh](/docs/v16/user/manual/vi/human-resources/designation).

Sau khi được cấp, các ngày nghỉ sẽ tự động được phân bổ cho các Nhân viên đã chọn dựa trên Chính sách nghỉ phép được thiết lập trong hồ sơ [Nhân viên](/docs/v16/user/manual/vi/human-resources/employee) của họ. Bạn có thể kiểm tra các ngày nghỉ mới được phân bổ trong danh sách Phân bổ nghỉ phép.

<img class="screenshot" alt="Manual Leave Allocation"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/leave-allocation2.png">


## 3. Các chủ đề liên quan

1. [Đơn xin nghỉ phép](/docs/v16/user/manual/vi/human-resources/leave-application)
1. [Yêu cầu nghỉ bù](/docs/v16/user/manual/vi/human-resources/compensatory-leave-request)
1. [Quy đổi ngày nghỉ thành tiền](/docs/v16/user/manual/vi/human-resources/leave-encashment)
1. [Danh sách chặn nghỉ phép](/docs/v16/user/manual/vi/human-resources/leave-block-list)
1. [Danh sách ngày lễ](/docs/v16/user/manual/vi/human-resources/holiday-list)

{next}