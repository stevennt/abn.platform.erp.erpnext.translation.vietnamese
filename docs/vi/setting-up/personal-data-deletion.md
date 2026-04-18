<!--add breadcrumbs-->

# Xóa dữ liệu cá nhân

Là một phần của việc tuân thủ GDPR, ERPNext có tính năng Xóa dữ liệu cá nhân.

Công cụ xóa dữ liệu cá nhân cho phép người dùng ẩn danh tất cả các dữ liệu nhận dạng cá nhân mà người dùng đã tạo ra trong quá trình sử dụng ERPNext. Nghĩa là, thông tin nhận dạng cá nhân sẽ được ngẫu nhiên hóa. Điều này bao gồm dữ liệu nhận dạng cá nhân từ tài khoản người dùng của bạn như: tên đăng nhập, họ tên, ngày sinh, số điện thoại, số di động, vị trí, sở thích, tiểu sử, chữ ký email, Email, Liên hệ, Địa chỉ, Liên lạc, v.v. Nó cũng bao gồm dữ liệu từ Khách hàng tiềm năng và Cơ hội, các chi tiết bạn đã lưu như số điện thoại, số di động, fax, website và tên.

Tuy nhiên, điều này loại trừ các dữ liệu mà pháp luật yêu cầu doanh nghiệp phải lưu giữ.

## 1. Cách yêu cầu xóa dữ liệu người dùng

1. Để bắt đầu xóa dữ liệu nhận dạng cá nhân, bạn cần truy cập [host-name]/request-to-delete-data (ví dụ: example.erpnext.com/request-to-delete-data) vào trường URL.

    <img class="screenshot" alt="Request Data Webform" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-deletion-request/request-to-delete-data-webform.png">

2. Nhập email liên kết với tài khoản ERPNext của bạn. Sau khi gửi yêu cầu, bạn sẽ nhận được phản hồi thành công.

    <img class="screenshot" alt="Deletion Request Success" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-deletion-request/deletion-request-success.png">

3. Thao tác này sẽ gửi một email có chứa liên kết xác nhận để xóa dữ liệu đến địa chỉ email liên kết với người dùng.

    <img class="screenshot" alt="Verification Email" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-deletion-request/verification-email.png">

4. Sau khi người dùng nhấp vào liên kết xác nhận, một thông báo xác nhận sẽ được hiển thị.
    <img class="screenshot" alt="Confirmed Verification" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-deletion-request/confirmed-verification.png">

## 2. Cách thức hoạt động của việc xóa dữ liệu cá nhân người dùng

Yêu cầu xóa dữ liệu được ghi lại trong DocType "Personal Data Deletion Request".

<img class="screenshot" alt="Personal Data Download Request Doctype" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-deletion-request/personal-data-deletion-request-doctype.png">

DocType này duy trì ba trạng thái để hoàn tất quy trình xóa dữ liệu người dùng.

### 2.1 Pending Verification (Chờ xác minh)
Trạng thái này cho biết người dùng đã yêu cầu xóa dữ liệu thông qua biểu mẫu web. Tuy nhiên, việc xác minh yêu cầu này vẫn đang chờ xử lý. Tìm kiếm "Personal Data Deletion Request" từ thanh tìm kiếm.

<img class="screenshot" alt="Pending Verification" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-deletion-request/pending-verification.png">

### 2.2 Pending Approval (Chờ phê duyệt)
Trạng thái này cho biết người dùng đã xác minh yêu cầu qua email. Điều này cho phép tùy chọn "Delete Data" (Xóa dữ liệu) cho Quản trị viên hệ thống (System Manager).

<img class="screenshot" alt="Pending Approval" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-deletion-request/pending-approval.png">

### 2.3 Deleted (Đã xóa)
Trạng thái này cho biết Quản trị viên hệ thống đã nhấp vào nút "Delete Data". Điều này có nghĩa là dữ liệu nhận dạng cá nhân của người dùng đã được ẩn danh.

<img class="screenshot" alt="Deleted User" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-deletion-request/deleted-user.png">

### 3. Các chủ đề liên quan
1. [Personal Data Download](personal-data-download.md)