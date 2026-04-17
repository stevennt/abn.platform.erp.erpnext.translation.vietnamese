<!-- add-breadcrumbs -->
# Tích hợp Google Contacts

ERPNext cung cấp tính năng tích hợp với Google Contacts để tất cả người dùng có thể đồng bộ hóa danh bạ Google của họ với ERPNext.

## Cách thiết lập Tích hợp Google Contacts

Để cho phép đồng bộ hóa với Google Contacts, bạn cần ủy quyền cho ERPNext lấy dữ liệu Danh bạ từ Google. Việc thiết lập Tích hợp Google Contacts được thực hiện theo các bước sau:

- Tạo Thông tin xác thực OAuth 2.0 thông qua [Google Settings](/docs/v16/user/manual/en/erpnext_integration/google_settings).
- Trong danh sách Google Contacts, nhấn vào **New**. Nhập Email Tài khoản Google mà bạn muốn đồng bộ hóa và sau đó nhấn **Lưu**. Bây giờ, hãy nhấn vào **Authorize Contacts Access** để ủy quyền cho ERPNext lấy dữ liệu Danh bạ từ Google.

## Cách sử dụng Tích hợp Google Contacts

### Tạo Danh bạ trong ERPNext
- Sau khi Tích hợp Google Contacts thành công, tất cả các danh bạ được tạo trong ERPNext sẽ được đồng bộ hóa nếu mục `Push to Google Contacts` được chọn.

Tạo một Danh bạ trong ERPNext:
<img class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/google_contacts_create_contact.gif">

Nó sẽ được hiển thị trong Google Contacts:
<img class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/google_contacts_create_contact_!.gif">

### Đồng bộ hóa Danh bạ từ Google Contacts
- Sau khi Tích hợp Google Contacts thành công, tất cả các danh bạ trong Google Contacts sẽ được đồng bộ hóa nếu mục `Pull from Google Contacts` được chọn.
  <img class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/google_contacts_contact_sync.gif">