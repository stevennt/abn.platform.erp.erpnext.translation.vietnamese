<!--add breadcrumbs-->

# Tải xuống Dữ liệu Cá nhân

Là một phần của việc tuân thủ GDPR, ERPNext có tính năng Tải xuống Dữ liệu Cá nhân.

Công cụ tải xuống dữ liệu cá nhân cho phép người dùng tự động tải xuống tất cả dữ liệu cá nhân mà họ đã tạo ra trong quá trình sử dụng ERPNext. Điều này bao gồm các dữ liệu nhận dạng cá nhân từ tài khoản người dùng của bạn như: tên đăng nhập, họ tên, ngày sinh, số điện thoại, số di động, vị trí, sở thích, tiểu sử, chữ ký email, Email, Liên hệ, Địa chỉ, Liên lạc, v.v. Nó cũng bao gồm dữ liệu từ Khách hàng tiềm năng và Cơ hội, các chi tiết bạn đã lưu như số điện thoại, số di động, fax, website và tên.

## 1. Cách yêu cầu tải xuống dữ liệu người dùng

1. Để bắt đầu tải xuống dữ liệu, người dùng phải **đăng nhập** và truy cập [host-name]/request-data (ví dụ: erpnext.com/request-data) trên thanh URL.

    <img class="screenshot" alt="Request Data" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-download-request/request-data-webform.png">

2. Sau khi gửi yêu cầu, bạn sẽ nhận được phản hồi thành công.
    <img class="screenshot" alt="Request Data" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-download-request/download-request-succes.png">

3. Một email chứa liên kết tải xuống dữ liệu sẽ được gửi đến địa chỉ email liên kết với người dùng đó.
    <img class="screenshot" alt="Download Data Email" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-download-request/download-data-email.png">

Tệp có sẵn để tải xuống sẽ ở định dạng JSON.

## 2. DocType Yêu cầu Tải xuống Dữ liệu Cá nhân

Yêu cầu cũng được ghi lại trong DocType "Personal Data Download Request" (Yêu cầu Tải xuống Dữ liệu Cá nhân), liên kết tệp được gửi cho người dùng qua email cũng được đính kèm vào tài liệu này. Tìm kiếm "Personal Data Download Request" từ thanh tìm kiếm.

<img class="screenshot" alt="Personal Data Download Request Doctype" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/personal-data-download-request/personal-data-download-request-doctype.png">

### 3. Các chủ đề liên quan
1. [Xóa Dữ liệu Cá nhân](personal-data-deletion.md)