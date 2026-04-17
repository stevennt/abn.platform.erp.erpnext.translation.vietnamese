<!-- add-breadcrumbs -->
# Cài đặt Google

Để kích hoạt các Tích hợp Google, ERPNext cần quyền truy cập vào API để đồng bộ hóa dữ liệu thông qua giao thức Xác thực OAuth 2.0.

## Cách thiết lập Cài đặt Google

### Đối với Google Calendar, Google Contacts, Google Drive

Để cho phép đồng bộ hóa với Google Calendar, Google Contacts hoặc Google Drive, bạn cần ủy quyền cho ERPNext lấy dữ liệu từ Google. Dưới đây là ví dụ về cách thiết lập Tích hợp Google Contacts.

1. Tạo một dự án mới trên Google Cloud Platform và tạo thông tin xác thực OAuth 2.0 mới.
<img class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/google_contacts_project_creation.gif">
- Kích hoạt Truy cập API trong Thư viện API cho Tích hợp mà bạn muốn kết nối.
  - Google Calendar: **Calendar API**
  - Google Contacts: **People API**
  - Google Drive: **Drive API**

 <img class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/api.gif">
- Trong **API & Services > Credentials**, tạo một Credential mới và chọn **Create OAuth client ID**.
- Chọn Application Type là **Web Application**.
- Thêm `https://{yoursite}` vào Authorized JavaScript origins.
- Thêm `https://{yoursite}?cmd=frappe.integrations.doctype.{integration_name}.{integration_name}.google_callback` làm URI chuyển hướng được ủy quyền (authorized redirect URI).
  - Bạn cần thay thế `integration_name` bằng một trong các tên sau:
     - Google Calendar: **google\_calendar**
     - Google Contacts: **google\_contacts**
     - Google Drive: **google\_drive**
  - Ví dụ: đối với Google Contacts, URL sẽ là `https://{yoursite}?cmd=frappe.integrations.doctype.google_contacts.google_contacts.google_callback`

 <img class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/google_contacts_oauth.gif">
- Thêm Client ID và Client Secret của bạn vào Cài đặt Google tại **Home > Integrations > Google Services > Google Settings**.

### Đối với Google Maps

Để cho phép đồng bộ hóa với Google Maps, bạn cần tạo một API key vì Google Maps không cần quyền truy cập vào dữ liệu từ Google.

1. Tạo một dự án mới trên Google Cloud Platform và tạo API Key mới.
- Kích hoạt Truy cập API trong Thư viện API cho Directions API và sau đó thêm API Key vào Cài đặt Google tại **Home > Integrations > Google Services > Google Settings**.
<img class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/erpnext_integrations/api_key.gif">