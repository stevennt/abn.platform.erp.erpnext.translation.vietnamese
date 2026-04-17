<!-- add-breadcrumbs -->
# Tự động gửi Báo cáo qua Email

**Tính năng Tự động gửi Báo cáo qua Email sẽ tự động gửi các báo cáo cho tài liệu đã được chọn.**

Bạn có thể thiết lập **Tự động gửi Báo cáo qua Email** để gửi báo cáo theo các khoảng thời gian định kỳ. Các báo cáo này phải là các báo cáo đã được lưu dưới bất kỳ loại nào (Report Builder, Script hoặc Query Report).

Bạn có thể tìm thấy Tự động gửi Báo cáo qua Email tại:

> Trang chủ > Thiết lập > Tự động gửi Báo cáo qua Email

## 1. Cách tạo Tự động gửi Báo cáo qua Email
1. Đi tới danh sách Tự động gửi Báo cáo qua Email, nhấn vào Mới.
1. Chọn Báo cáo mà bạn muốn tạo email.
1. Chọn người dùng mà bạn muốn tạo báo cáo này (các quyền sẽ được áp dụng cho người dùng này).
1. Thiết lập Địa chỉ Email mà bạn muốn nhận báo cáo này và tần suất gửi báo cáo. Email sẽ được gửi vào lúc nửa đêm. Ngày sẽ được lặp lại trong trường hợp tần suất là hàng tuần/hàng tháng/hàng năm. Ví dụ: nếu ngày được chọn là ngày 7 và tần suất là hàng tháng, email sẽ được gửi vào ngày 7 hàng tháng.

 <img class="screenshot" alt="With Filters" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/auto-email-2.png">
1. Lưu.

Bạn có thể kiểm tra báo cáo bằng cách nhấn vào "Tải xuống" hoặc "Gửi ngay". Dưới đây là ví dụ về email bạn sẽ nhận được cho một báo cáo sổ cái:

<img class="screenshot" alt="Report by Email" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/auto-email-4.png">

## 2. Các tính năng

### 2.1 Lọc dữ liệu

* **Chỉ gửi nếu có dữ liệu**: Nếu được bật, email sẽ không được gửi nếu không có dữ liệu trong báo cáo.
* **Chỉ gửi các bản ghi được cập nhật trong X giờ qua**: Nếu đặt là 24, email sẽ chỉ chứa các bản ghi được cập nhật trong 24 giờ qua.
* **Số dòng**: Số lượng dòng sẽ được gửi trong email. Tối đa là 500.

### 2.2 Bộ lọc báo cáo
Nếu báo cáo của bạn có các bộ lọc, bạn sẽ có thể nhìn thấy chúng. Nhấp vào bảng để chỉnh sửa:

<img class="screenshot" alt="Edit Filters" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/email/auto-email-3.png">

Ví dụ: nếu email dành cho báo cáo 'Project Billing Summary' (Tóm tắt thanh toán dự án), hãy chọn Dự án. Khoảng ngày ở đây là khoảng ngày của báo cáo 'Project Billing Summary'.

### 2.3 Tin nhắn

Một tin nhắn cũng có thể được thêm vào để gửi kèm với báo cáo email. Ví dụ: 'Đây là Báo cáo Tóm tắt thanh toán dự án hàng tháng của bạn:'

Bạn cũng có thể thay đổi định dạng tệp mà báo cáo được tạo. Các tùy chọn có sẵn là HTML, XLSX và CSV.

### 2. Các chủ đề liên quan
1. [Email Digest](/docs/v13/user/manual/en/setting-up/email/email-digest)
1. [Document Follow](/docs/v13/user/manual/en/setting-up/email/document-follow)