<!-- add-breadcrumbs -->
# Thiết lập fairlogin

fairlogin là một nhà cung cấp oAuth tuân thủ GDPR của fairkom.eu.

Để thiết lập fairlogin làm nhà cung cấp oAuth, hãy đi đến:
> Home > Integrations > Social Login Key

## Thiết lập keycloak

fairlogin dựa trên keycloak, vì vậy các tham số có thể tương tự cho bất kỳ cài đặt oAuth tùy chỉnh nào hỗ trợ keycloak.

Tại đó, bạn thêm một client mới, chọn open-id làm client protocol và nhập địa chỉ instance ERPNext của bạn làm Root, Redirect và Base URL.

Việc thêm dịch vụ ERNext của bạn dưới dạng một client đang được [cung cấp dưới dạng dịch vụ bởi fairkom](https://erp.fairkom.net/cloud/fairlogin-client).

![ERPnext keycloak Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/fairloginKeycloakERPnext.png)

## Thiết lập fairlogin

Để kích hoạt fairlogin làm một tùy chọn đăng nhập ERPNext, bạn cần cấu hình các tham số sau:

- Base URL https://id.fairkom.net/auth/realms/fairlogin/
- Authorize URL https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/auth
- Redirect URL /api/method/frappe.integrations.oauth2_logins.login_via_fairlogin
- Access Token URL https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/token
- API Endpoint https://id.fairkom.net/auth/realms/fairlogin/protocol/openid-connect/userinfo

![ERPnext fairlogin Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/fairloginERPnextSettings.png)

Khi kích hoạt dịch vụ, hệ thống sẽ cho phép đăng nhập bằng bất kỳ tài khoản fairlogin nào.

Vai trò mặc định của người dùng mới là Blogger (hiện đang được thiết lập cứng).