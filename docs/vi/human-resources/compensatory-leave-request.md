<!-- add-breadcrumbs -->
# Yêu cầu Nghỉ bù


**Nghỉ bù là loại nghỉ phép được cấp cho Nhân viên để bù đắp cho việc làm thêm giờ hoặc làm việc vào các ngày lễ.**

 ERPNext cho phép Nhân viên yêu cầu Nghỉ bù thông qua chứng từ Yêu cầu Nghỉ bù. Điều kiện cần thiết là các ngày được đề cập trong Yêu cầu Nghỉ bù phải nằm trong Danh sách ngày lễ mặc định và Nhân viên đó cũng phải được ghi nhận Chấm công là Có mặt.

 > **Lưu ý:** Chỉ những Loại nghỉ phép được đánh dấu là 'Is Compensatory' mới có thể được chọn trong Yêu cầu Nghỉ bù.

Để truy cập Yêu cầu Nghỉ bù, hãy đi tới:

> Trang chủ > Nhân sự > Nghỉ phép > Yêu cầu Nghỉ bù


## 1. Điều kiện tiên quyết

Trước khi tạo Yêu cầu Nghỉ bù, cần phải tạo các chứng từ sau:

* [Nhân viên](employee.md)
* [Kỳ nghỉ phép](leave-period.md)
* [Loại nghỉ phép](leave-type.md)
* [Chính sách nghỉ phép](leave-policy.md)
* [Phân bổ nghỉ phép](leave-allocation.md)
* [Danh sách ngày lễ](holiday-list.md)
* [Chấm công](attendance.md)


## 2. Cách tạo Yêu cầu Nghỉ bù

1. Đi tới danh sách Yêu cầu Nghỉ bù, nhấn vào Mới.
1. Chọn ID Nhân viên. Sau khi chọn, Tên Nhân viên và Phòng ban sẽ được tự động lấy dữ liệu.
1. Chọn Loại nghỉ phép.
1. Chọn Ngày bắt đầu làm việc và Ngày kết thúc làm việc. Đây là ngày (các ngày) mà Nhân viên đã làm việc trong một ngày Lễ.
1. Nhập Lý do.
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Compensatory Leave Request"
    src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/compensatory-leave.png">



Khi Xác nhận Yêu cầu Nghỉ bù, ERPNext sẽ cập nhật bản ghi Phân bổ nghỉ phép cho loại nghỉ bù đó, cho phép Nhân viên đăng ký nghỉ loại này sau đó tùy thuộc vào số ngày nghỉ còn lại.


## 3. Các chủ đề liên quan

1. [Đơn xin nghỉ phép](leave-application.md)
1. [Quy đổi ngày nghỉ thành tiền](leave-encashment.md)
1. [Danh sách chặn nghỉ phép](leave-block-list.md)