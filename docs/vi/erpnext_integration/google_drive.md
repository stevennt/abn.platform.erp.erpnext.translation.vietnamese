<!-- add-breadcrumbs -->
# Tích hợp Google Drive

ERPNext cung cấp tính năng tích hợp với Google Drive để tất cả người dùng có thể sao lưu dữ liệu của họ lên Google Drive.


## Cách thiết lập Tích hợp Google Drive

Để cho phép ERPNext tải các bản sao lưu lên Google Drive, bạn cần cấp quyền cho ERPNext tải tệp lên Google Drive. Việc thiết lập Tích hợp Google Drive được thực hiện theo các bước sau:

- Tạo Thông tin xác thực OAuth 2.0 thông qua [Google Settings](google_settings.md).
- Trong danh sách Google Drive, nhấn vào New. Nhập tên thư mục Backup để lưu các bản sao lưu lên Google Drive, tần suất sao lưu và email của người sẽ nhận thông báo về trạng thái sao lưu, sau đó nhấn Lưu. Bây giờ, hãy nhấn vào **Authorize Drive Access** để cấp quyền cho ERPNext đẩy các tệp lên Google Drive.
- Sau khi đã được Cấp quyền, bạn có thể lưu bản sao lưu của mình lên Google Drive.

## Cách sử dụng Tích hợp Google Drive

### Tải bản sao lưu lên Google Drive
- Sau khi Tích hợp Google Drive thành công, bạn có thể tải bản sao lưu hệ thống cũng như tất cả các tệp công khai và riêng tư của bạn lên Google Drive.
- Để sao lưu dữ liệu lên Google Drive, hãy nhấn vào **Take Backup**. Quá trình sao lưu sẽ chạy ngầm và bạn sẽ được thông báo về trạng thái sao lưu.
  <img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/google_drive.gif">

> **Lưu ý**: Nếu kích thước bản sao lưu đã nén vượt quá 1GB (Gigabyte), hệ thống sẽ tải bản sao lưu mới nhất hiện có lên Google Drive thay vì tạo một tệp sao lưu mới.