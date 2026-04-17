<!-- add-breadcrumbs -->
# Yêu cầu Nghỉ bù


**Nghỉ bù là loại nghỉ phép được cấp cho Nhân viên để bù đắp cho việc làm thêm giờ hoặc làm việc vào các ngày lễ.**

 ERPNext cho phép Nhân viên yêu cầu Nghỉ bù thông qua chứng từ Yêu cầu Nghỉ bù. Điều kiện cần thiết là các ngày được đề cập trong Yêu cầu Nghỉ bù phải nằm trong Danh sách ngày lễ mặc định và Nhân viên đó cũng phải được ghi nhận Chấm công là Có mặt.

 > **Lưu ý:** Chỉ những Loại nghỉ phép được đánh dấu là 'Is Compensatory' mới có thể được chọn trong Yêu cầu Nghỉ bù.

Để truy cập Yêu cầu Nghỉ bù, hãy đi tới:

> Trang chủ > Nhân sự > Nghỉ phép > Yêu cầu Nghỉ bù


## 1. Điều kiện tiên quyết

Trước khi tạo Yêu cầu Nghỉ bù, cần phải tạo các chứng từ sau:

* [Nhân viên](/docs/v13/user/manual/en/human-resources/employee)
* [Kỳ nghỉ phép](/docs/v13/user/manual/en/human-resources/leave-period)
* [Loại nghỉ phép](/docs/v13/user/manual/en/human-resources/leave-type)
* [Chính sách nghỉ phép](/docs/v13/user/manual/en/human-resources/leave-policy)
* [Phân bổ nghỉ phép](/docs/v13/user/manual/en/human-resources/leave-allocation)
* [Danh sách ngày lễ](/docs/v13/user/manual/en/human-resources/holiday-list)
* [Chấm công](/docs/v13/user/manual/en/human-resources/attendance)


## 2. Cách tạo Yêu cầu Nghỉ bù

1. Đi tới danh sách Yêu cầu Nghỉ bù, nhấn vào Mới.
1. Chọn ID Nhân viên. Sau khi chọn, Tên Nhân viên và Phòng ban sẽ được tự động lấy dữ liệu.
1. Chọn Loại nghỉ phép.
1. Chọn Ngày bắt đầu làm việc và Ngày kết thúc làm việc. Đây là ngày (các ngày) mà Nhân viên đã làm việc trong một ngày Lễ.
1. Nhập Lý do.
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Compensatory Leave Request"
    src="https://docs.erpnext.com/docs/v13/assets/img/human-resources/compensatory-leave.png">



Khi Xác nhận Yêu cầu Nghỉ bù, ERPNext sẽ cập nhật bản ghi Phân bổ nghỉ phép cho loại nghỉ bù đó, cho phép Nhân viên đăng ký nghỉ loại này sau đó tùy thuộc vào số ngày nghỉ còn lại.


## 3. Các chủ đề liên quan

1. [Đơn xin nghỉ phép](/docs/v13/user/manual/en/human-resources/leave-application)
1. [Quy đổi ngày nghỉ thành tiền](/docs/v13/user/manual/en/human-resources/leave-encashment)
1. [Danh sách chặn nghỉ phép](/docs/v13/user/manual/en/human-resources/leave-block-list)