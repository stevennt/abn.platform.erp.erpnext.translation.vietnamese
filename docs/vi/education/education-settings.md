<!-- add-breadcrumbs -->
# Cài đặt Giáo dục

**Cài đặt Giáo dục sẽ cho phép bạn thực hiện thiết lập cơ bản cho Học viện của mình, trong đó bạn có thể xác định Năm học, Học kỳ và các thiết lập mặc định khác cho tài khoản ERPNext của mình.**

Các thiết lập cấu hình này sẽ có tác động trong toàn bộ mô-đun.

Để truy cập Học kỳ, hãy đi đến:

> Trang chủ > Giáo dục > Cài đặt > Cài đặt Giáo dục

## 1. Các bước để cấu hình Cài đặt Giáo dục

1. Chọn Năm học hiện tại. Đây sẽ trở thành Năm học mặc định trong toàn bộ tài khoản của bạn.
2. Chọn Học kỳ hiện tại. Đây sẽ trở thành Học kỳ mặc định trong toàn bộ tài khoản của bạn.
3. Chọn ngày Chốt Chấm công. Bất kỳ dữ liệu chấm công nào được ghi nhận sau Ngày Chốt Chấm công sẽ không có hiệu lực.
4. Chọn cách bạn muốn tạo Hồ sơ Giảng viên, sử dụng Họ và tên, sử dụng Chuỗi đặt tên hoặc sử dụng Mã nhân viên.
5. **Hồ sơ Giảng viên được tạo bởi**: Bạn có thể chọn cách bạn muốn Hồ sơ Giảng viên được tạo trong hệ thống ERPNext của mình, cho dù đó là theo Họ và tên, theo Chuỗi đặt tên, hoặc theo Mã nhân viên.

 ![Education Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-seetings-1.png)

### 1.1. Cấu hình các Thuộc tính

* **Xác nhận Lớp cho Học sinh trong Nhóm học sinh**: Khi thêm học sinh vào một nhóm học sinh thông qua Lớp, hệ thống sẽ xác minh xem học sinh đó có thuộc lớp đó hay không, và nếu không đúng, một lỗi sẽ hiển thị khi Lưu Nhóm học sinh.
* **Xác nhận Lớp cho Học sinh trong Nhóm học sinh**: Khi thêm học sinh vào một nhóm học sinh thông qua Khóa học, hệ thống sẽ xác minh xem học sinh đó có đăng ký khóa học đó hay không, và nếu không đúng, một lỗi sẽ hiển thị khi Lưu Nhóm học sinh.
* **Bắt buộc chọn Học kỳ**: Khi được bật, tùy chọn này sẽ đảm bảo rằng khi tạo Đăng ký Chương trình thông qua [Công cụ Đăng ký Chương trình](program-enrollment-tool.md), người dùng phải nhập Học kỳ.
* **Bỏ qua Tạo Người dùng cho Học sinh mới**: Bất cứ khi nào một học sinh mới được tạo, theo mặc định một Người dùng sẽ được tạo tương ứng. Nếu tùy chọn này được bật, sẽ không có Người dùng mới nào được tạo khi một Học sinh mới được tạo.

### 1.2. Cài đặt LMS

Mô-đun Giáo dục được tích hợp sẵn Hệ thống Quản lý Học tập (LMS). Điều này cho phép các học viện xuất bản các chương trình của họ trên trang web của mình. Các chương trình có thể chứa các bài viết văn bản định dạng phong phú, video và thậm chí cả các bài kiểm tra. Tiến độ của từng học sinh có thể được theo dõi thông qua desk cũng như cổng thông tin.

Sau khi bạn Bật LMS cho mô-đun Giáo dục ERPNext của mình, các cài đặt sau sẽ có sẵn để cấu hình:

1. **Tiêu đề LMS**: Nhập Tiêu đề cho LMS của bạn. Đó có thể là tên Học viện của bạn.
2. **Mô tả**: Bạn có thể thêm mô tả khóa học cho LMS của mình.

![Education Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/education/education-seetings-1.png)

Bạn có thể đi tiếp đến [Hoạt động LMS](setting-up-lms.md) để thêm các khóa học, bài viết hoặc bài kiểm tra cho LMS của mình. Để truy cập cổng LMS của bạn, bạn có thể truy cập URL, {yourdomainname}.erpnext.com/lms

{next}