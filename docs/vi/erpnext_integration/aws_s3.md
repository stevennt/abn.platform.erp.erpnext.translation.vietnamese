<!-- add-breadcrumbs -->

# Tải bản sao lưu lên Amazon S3

## Điều kiện tiên quyết

- [Tài khoản Email](../setting-up/email/email-account.md)

    Để nhận email thông báo khi sao lưu thất bại hoặc thành công, vui lòng tạo một **Tài khoản Email** trước.

## Tạo S3 bucket và thiết lập quyền truy cập

1. Tạo một s3 bucket mới.

    Trong phần cài đặt bucket, hãy bật "Block all public access" để giữ dữ liệu của bạn được riêng tư. Bạn có thể tùy chọn bật mã hóa (encryption), quản lý phiên bản (versioning) hoặc khóa đối tượng (object lock) tùy theo yêu cầu của mình (vui lòng tham khảo [tài liệu của Amazon](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)).

2. Mở Identity and Access Management (IAM).

    1. Tạo một chính sách (policy) mới cho dịch vụ "S3", cho phép các hành động (Actions) "ListBucket" và "PutObject".

    2. Tạo một người dùng (user) mới để truy cập bằng lập trình.

        ![Screenshot of "Add User" in AWS](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/s3_backup_add_user.png)

    3. Gán chính sách bạn vừa tạo cho người dùng mới.

    4. Sao chép access key và secret của người dùng.

Để tự động xóa các bản sao lưu cũ hoặc chuyển chúng sang lớp lưu trữ rẻ hơn, hãy xem [quản lý vòng đời](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).

## Thiết lập ERPNext

- Mở **S3 Backup Settings**.
- Tích chọn "Enable Automatic Backup".
- Dán access key và secret từ AWS vào.
- Thiết lập địa chỉ email để nhận thông báo khi sao lưu thất bại. Nếu bạn muốn nhận cả email khi sao lưu thành công, hãy bật "Send Email for Successful Backup".
- Chỉ định tên của bucket mà bạn đã tạo ở bước 1.
- Chọn tần suất bạn muốn thực hiện và tải lên các bản sao lưu. Tần suất có thể từ hàng tháng đến hàng ngày. Nếu bạn chỉ muốn thực hiện sao lưu thủ công, hãy đặt tần suất là "None".

![S3 Backup Settings in ERPNext](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/s3_backup_settings.png)