<!-- add-breadcrumbs -->
# Tải bản sao lưu

Trong ERPNext, bạn có thể tải bản sao lưu cơ sở dữ liệu một cách thủ công. Để lấy bản sao lưu cơ sở dữ liệu mới nhất, hãy đi tới:

> Trang chủ > Cài đặt > Tải bản sao lưu

Bản sao lưu có sẵn để tải xuống được cập nhật sau mỗi tám giờ. Nhấp vào liên kết để tải bản sao lưu tại một thời điểm nhất định.

<img class="screenshot" alt="Download Backup" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/download-backup-1.png">

Theo mặc định, ba bản sao lưu mới nhất sẽ có sẵn để tải xuống. Để thay đổi điều này, hãy nhấp vào "Thiết lập số lượng bản sao lưu". Thao tác này sẽ đưa bạn đến Cài đặt hệ thống, nơi bạn có thể thiết lập Số lượng bản sao lưu có sẵn để tải xuống tại một thời điểm.

<img class="screenshot" alt="Download Backup" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/download-backup-2.png">

## Tải bản sao lưu tệp tin

Nhấp vào Tải bản sao lưu tệp tin sẽ gửi một email kèm theo các liên kết để tải bản sao lưu cho cả tệp riêng tư và tệp công khai. [Email](../email) phải được cấu hình để tính năng này hoạt động.

<img class="screenshot" alt="Download Backup" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/download-backup-files.png">

## Tự động hóa sao lưu lên lưu trữ đám mây

Bạn cũng có thể tự động hóa việc sao lưu để tải trực tiếp lên nền tảng lưu trữ đám mây. Hiện tại, ERPNext hỗ trợ:

1. Amazon S3
1. [Dropbox](../../erpnext_integration/dropbox-backup.md)
1. [Google Drive](../../erpnext_integration/google_drive.md)