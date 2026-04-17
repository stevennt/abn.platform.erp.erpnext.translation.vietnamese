<!-- add-breadcrumbs -->
# Cài đặt Giáo dục

**Cài đặt Giáo dục cho phép bạn thực hiện các thiết lập cơ bản cho Học viện, bao gồm xác định Năm học, Học kỳ và các thiết lập mặc định khác cho tài khoản ERPNext của bạn.**

Các thiết lập cấu hình này sẽ có tác động trong toàn bộ mô-đun.

Để truy cập Cài đặt Giáo dục, hãy đi đến:

> Trang chủ > Giáo dục > Cài đặt > Cài đặt Giáo dục

## 1. Các bước để cấu hình Cài đặt Giáo dục

1. Chọn **Năm học** hiện tại. Đây sẽ trở thành Năm học mặc định trong toàn bộ tài khoản của bạn.
2. Chọn **Học kỳ** hiện tại. Đây sẽ trở thành Học kỳ mặc định trong toàn bộ tài khoản của bạn.
3. Chọn ngày **Chốt Chấm công**. Bất kỳ dữ liệu chấm công nào được ghi nhận sau ngày này sẽ không có hiệu lực.
4. Chọn cách bạn muốn tạo **Hồ sơ Giảng viên**, sử dụng Họ và tên, sử dụng Chuỗi đặt tên hoặc sử dụng Mã nhân viên.
5. **Hồ sơ Giảng viên được tạo bởi**: Bạn có thể chọn cách hệ thống tự động tạo Hồ sơ Giảng viên trong ERPNext, cho dù đó là theo Họ và tên, theo Chuỗi đặt tên, hoặc theo Mã nhân viên.

 ![Education Settings](https://docs.erpnext.com/docs/v16/assets/img/education/education-seetings-1.png)

### 1.1. Cấu hình các Thuộc tính

* **Xác nhận Lớp cho Học sinh trong Nhóm học sinh**: Khi thêm học sinh vào một nhóm học sinh thông qua Lớp, hệ thống sẽ xác minh xem học sinh đó có thuộc lớp đó hay không. Nếu không khớp, lỗi sẽ hiển thị khi bạn **Lưu** Nhóm học sinh.
* **Xác nhận Lớp cho Học sinh trong Nhóm học sinh**: Khi thêm học sinh vào một nhóm học sinh thông qua Khóa học, hệ thống sẽ xác minh xem học sinh đó có đăng ký khóa học đó hay không. Nếu không khớp, lỗi sẽ hiển thị khi bạn **Lưu** Nhóm học sinh.
* **Bắt buộc chọn Học kỳ**: Khi được bật, tùy chọn này đảm bảo rằng khi tạo Đăng ký Chương trình thông qua [Công cụ Đăng ký Chương trình](../education/program-enrollment-tool), người dùng bắt buộc phải nhập Học kỳ.
* **Bỏ qua Tạo Người dùng cho Học sinh mới**: Theo mặc định, khi một học sinh mới được tạo, một Người dùng tương ứng cũng sẽ được tạo. Nếu bật tùy chọn này, hệ thống sẽ không tạo Người dùng mới khi tạo Học sinh mới.

### 1.2. Cài đặt LMS

Mô-đun Giáo dục được tích hợp sẵn Hệ thống Quản lý Học tập (LMS). Điều này cho phép các học viện xuất bản các chương trình của họ trên trang web. Các chương trình có thể chứa các bài viết văn bản định dạng phong phú, video và các bài kiểm tra. Tiến độ của từng học sinh có thể được theo dõi thông qua giao diện quản trị (desk) cũng như cổng thông tin dành cho học sinh.

Sau khi bạn **Bật** LMS cho mô-đun Giáo dục ERPNext, các cài đặt sau sẽ có sẵn để cấu hình:

1. **Tiêu đề LMS**: Nhập tiêu đề cho LMS của bạn (thường là tên Học viện).
2. **Mô tả**: Bạn có thể thêm mô tả tổng quan cho LMS của mình.

![Education Settings](https://docs.erpnext.com/docs/v16/assets/img/education/education-seetings-1.png)

Bạn có thể chuyển sang phần [Hoạt động LMS](../education/setting-up-lms) để thêm các khóa học, bài viết hoặc bài kiểm tra. Để truy cập cổng LMS, hãy sử dụng URL: `{yourdomainname}.erpnext.com/lms`

{next}