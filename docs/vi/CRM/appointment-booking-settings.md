# Cài đặt Đặt lịch hẹn

Bạn có thể tìm thấy tất cả các cài đặt liên quan đến việc đặt lịch hẹn trong Cài đặt Đặt lịch hẹn.

![Appointment Booking Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/appointment-booking-settings.png)

## 1. Cho phép lập lịch hẹn

Ô đánh dấu này sẽ cho phép lập lịch hẹn và cũng cho phép kích hoạt Route `/book_appointment` cho người dùng website (khách hàng của bạn). Khách hàng của bạn sẽ thấy một giao diện cổng thông tin. Để biết thêm chi tiết, hãy truy cập [Trang Lịch hẹn](/docs/v13/user/manual/en/CRM/appointment)

## 2. Chi tiết về Nhân viên hỗ trợ

Trong phần này, bạn có thể thêm chi tiết về các nhân viên hỗ trợ, chẳng hạn như giờ làm việc và ngày nghỉ của họ.

### 2.1 Khả dụng của các khung giờ

Tại đây bạn có thể thiết lập khung thời gian mà các nhân viên hỗ trợ của bạn có sẵn để tham gia một cuộc hẹn. Cài đặt này được thiết lập theo từng ngày trong tuần. Mỗi hàng đại diện cho một khối thời gian liên tục, bạn có thể có nhiều mục nhập cho mỗi ngày trong tuần.

Ví dụ: nếu nhân viên của bạn làm việc từ Thứ Hai đến Thứ Sáu, từ 9 giờ sáng đến 5 giờ chiều nhưng có nghỉ trưa lúc 1 giờ 30 chiều trong nửa giờ. Bạn sẽ cần tạo hai mục nhập cho mỗi ngày. Một mục từ 9 giờ sáng đến 1 giờ 30 chiều và một mục khác từ 2 giờ chiều đến 5 giờ chiều.

### 2.2 Nhân viên hỗ trợ

Đây là danh sách các nhân viên hỗ trợ sẽ được **tự động chỉ định** cho các cuộc hẹn. Số lượng cuộc hẹn có thể tồn tại trong một khung giờ cũng phụ thuộc vào số lượng nhân viên trong danh sách này.

### 2.3 Danh sách ngày nghỉ

Bạn có thể liên kết một [danh sách ngày nghỉ](https://erpnext.com/docs/v13/user/manual/en/human-resources/holiday-list) tại đây để áp dụng cho lịch hẹn. Nếu ngày đó là ngày nghỉ, việc lập lịch hẹn vào ngày đó sẽ không được cho phép.

## 3. Chi tiết cuộc hẹn

Phần này chứa các chi tiết về chính các cuộc hẹn.

### 3.1 Thời lượng cuộc hẹn (phút)

Thời lượng của cuộc hẹn tính bằng phút. Thông số này được sử dụng để tính toán các khung giờ hẹn cho cổng thông tin web. Việc thay đổi thông số này không ảnh hưởng đến các cuộc hẹn đã được tạo trước khi thay đổi.

### 3.2 Thông báo qua Email

Khi bật ô đánh dấu này, một email sẽ được gửi đến những người tham gia cuộc hẹn, cụ thể là nhân viên của bạn và khách hàng vào ngày diễn ra cuộc hẹn. Việc thay đổi ô đánh dấu này không ảnh hưởng đến các cuộc hẹn đã được tạo trước khi thay đổi.

### 3.3 Số ngày có thể đặt lịch hẹn trước

Đây là số ngày mà cuộc hẹn có thể được đặt trước. Nếu Danh sách ngày nghỉ được cung cấp ở trên kết thúc trước ngày được tính toán bằng số ngày này, việc lập lịch hẹn sẽ bị dừng lại tại thời điểm kết thúc danh sách ngày nghỉ.


## 4. Cài đặt thành công

### 4.1 URL chuyển hướng thành công

Đây là URL mà người dùng sẽ được chuyển hướng đến sau khi tạo cuộc hẹn thành công thông qua Cổng thông tin Web. Việc chuyển hướng này sẽ không xảy ra khi tạo cuộc hẹn từ trong giao diện Desk UI.
Để trống để chuyển về trang chủ. URL này là tương đối so với URL của trang web, ví dụ: "about" sẽ chuyển hướng đến "https://yoursitename.com/about"

{next}