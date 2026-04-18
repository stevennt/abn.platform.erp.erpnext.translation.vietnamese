<!-- add-breadcrumbs -->
# Thêm Người dùng

Người dùng có thể được thêm bởi Quản trị viên hệ thống (System Manager). Để thêm người dùng, hãy đi tới:
> Trang chủ > Người dùng và Quyền > Người dùng

Có hai loại người dùng chính:

**Người dùng Website**: Khách hàng, Nhà cung cấp, Học sinh, v.v., những người chỉ có quyền truy cập vào cổng thông tin (portal) và không có quyền truy cập vào bất kỳ module nào.
**Người dùng Hệ thống**: Những người sử dụng ERPNext trong Công ty với quyền truy cập vào các module, dữ liệu công ty, v.v.

Đọc thêm về [sự khác biệt giữa người dùng hệ thống và người dùng website](/docs/v16/user/manual/en/setting-up/articles/difference-between-system-user-and-website-user).

Trong mục Người dùng, rất nhiều thông tin có thể được nhập vào. Để thuận tiện cho việc sử dụng, thông tin được nhập cho người dùng web là tối thiểu: Tên và Email.

Địa chỉ Email là khóa duy nhất (ID) để xác định Người dùng.

## 1. Cách Tạo Người dùng Mới

1. Đi tới danh sách Người dùng, nhấn vào Mới.
1. Thêm địa chỉ Email và tên của người dùng.
1. Lưu.

    <img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/add-user-details.png" alt="Add User Details">

Các chi tiết như Tên đăng nhập và Ngôn ngữ cũng có thể được thay đổi.

## 2. Các tính năng

### 2.1 Thiết lập Vai trò

Sau khi Lưu, bạn sẽ thấy một danh sách các vai trò và các ô đánh dấu bên cạnh chúng. Chỉ cần đánh dấu các vai trò mà bạn muốn người dùng có và Lưu tài liệu. Các vai trò có các quyền đã được định nghĩa trước, để biết thêm về vai trò, [nhấn vào đây](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-based-permissions). Bạn có thể thiết lập [Hồ sơ vai trò](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-and-role-profile) để sử dụng như một mẫu giúp chọn nhiều vai trò cùng lúc.

<img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/users/user-2.png" alt="User Roles">

### 2.2 Thông tin thêm
Thông tin thêm về nhân viên có thể được thiết lập từ phần này:

* Giới tính
* Điện thoại
* Số di động
* Ngày sinh
* Địa điểm
* Sở thích
* Tiểu sử
* Ảnh bìa

Đánh dấu vào 'Tắt âm thanh' sẽ tắt các âm thanh phát ra khi tương tác với các tài liệu. Người dùng có thể cần thực hiện Cài đặt > Tải lại để các thay đổi có hiệu lực.

### 2.3 Thay đổi Mật khẩu

* **Đặt Mật khẩu mới**: Với tư cách là Quản trị viên hệ thống, bạn có thể đặt mật khẩu mới cho người dùng nếu cần thay đổi.
* **Gửi Thông báo cập nhật mật khẩu**: Gửi thông báo email cho người dùng rằng mật khẩu của họ đã được thay đổi.
* **Đăng xuất khỏi tất cả thiết bị khi thay đổi Mật khẩu**: Khi thay đổi mật khẩu của người dùng, tùy chọn này sẽ đăng xuất người dùng khỏi máy tính và bất kỳ thiết bị di động nào mà họ có thể đã đăng nhập.

### 2.4 Theo dõi Tài liệu
Với tùy chọn này, bạn có thể theo dõi các tài liệu khác nhau trong hệ thống và nhận thông báo email khi chúng được cập nhật. Tìm hiểu thêm [tại đây](/docs/v16/user/manual/en/setting-up/email/document-follow).

### 2.5 Cài đặt Email

* **Gửi Thông báo cho các luồng Email**: Người dùng sẽ nhận được thông báo cho các cuộc hội thoại Email diễn ra trong các loại tài liệu như Cơ hội.
* **Gửi cho tôi một bản sao của Email gửi đi**: Gửi cho người dùng một bản sao của các email mà họ gửi. Điều này hữu ích để theo dõi xem email đã được gửi hay chưa.
* **Cho phép trong các lượt Nhắc tên**: Cho phép tên của người dùng này xuất hiện trong các cuộc hội thoại luồng để họ có thể được nhắc tên bằng ký tự '@'.
* **Chữ ký Email**: Thêm chữ ký email tại đây sẽ thiết lập nó làm mặc định cho tất cả các email gửi đi của người dùng. Điều này khác với chân trang được thiết lập từ [Thông tin chính của Công ty](/docs/v16/user/manual/en/setting-up/company-setup).

### 2.6 Hộp thư Email

Đăng ký người dùng vào các danh sách gửi thư khác nhau của công ty bạn từ phần này. Thêm một dòng mới và chọn danh sách gửi thư để chỉ định người dùng này. Ví dụ, danh sách gửi thư có thể là tuyển dụng, hỗ trợ, bán hàng, v.v. Để biết thêm về Hộp thư Email, [nhấn vào đây](/docs/v16/user/manual/en/setting-up/email/email-inbox).

### 2.7 Cho phép Truy cập Module

Người dùng sẽ có quyền truy cập vào tất cả các module mà họ có quyền truy cập dựa trên vai trò. Nếu bạn muốn hạn chế quyền truy cập của một số module nhất định cho người dùng này, hãy bỏ đánh dấu các module từ danh sách này.

<img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/users/user-3.png" alt="User Block Module">

#### 2.7.1 Hồ sơ Module

Hồ sơ vai trò đóng vai trò như một mẫu để lưu trữ và lựa chọn quyền truy cập vào nhiều module. Hồ sơ vai trò này sau đó có thể được gán cho một Người dùng. Ví dụ, Người dùng Nhân sự sẽ có quyền truy cập vào nhiều module như Nhân sự, Bảng lương, v.v. Hồ sơ vai trò rất hữu ích để cung cấp quyền truy cập vào nhiều module cùng một lúc khi thêm nhiều người dùng.

<img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/users/module-profile.png" alt="Module Profile">

### 2.8 Cài đặt Bảo mật

* **Phiên làm việc đồng thời**: Số lượng phiên đăng nhập đồng thời mà người dùng được phép. Bạn có thể sử dụng cùng một bộ thông tin đăng nhập cho nhiều người dùng bằng cách cho phép nhiều phiên hơn. Điều này có thể bị hạn chế từ [Cài đặt hệ thống](/docs/v16/user/manual/en/setting-up/settings/system-settings#15-security) trên phạm vi toàn cầu. Đối với tài khoản đám mây, tổng số phiên làm việc đồng thời không được vượt quá tổng số người dùng đã đăng ký.
* **Loại Người dùng**: Nếu người dùng có bất kỳ vai trò nào được đánh dấu ngoại trừ Khách hàng, Nhà cung cấp, Bệnh nhân hoặc Học sinh, họ sẽ tự động trở thành Người dùng Hệ thống. Trường này chỉ đọc.
* **Đăng nhập Sau, Đăng nhập Trước**: Nếu bạn muốn cấp quyền truy cập hệ thống cho người dùng chỉ trong giờ làm việc, hoặc trong những ngày cuối tuần, hãy chỉ định tại đây. Ví dụ, nếu giờ làm việc là từ 10 giờ sáng đến 6 giờ chiều, hãy đặt giờ Đăng nhập Sau, Đăng nhập Trước.