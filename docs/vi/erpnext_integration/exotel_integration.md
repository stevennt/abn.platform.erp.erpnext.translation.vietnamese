<!-- add-breadcrumbs -->

# Tích hợp Exotel

Tích hợp này cho phép bạn tích hợp Exotel vào tài khoản ERPNext của mình. Khách hàng tiềm năng và số điện thoại của họ được thu thập qua Exotel có thể được lưu trực tiếp vào ERPNext của bạn.

## 1. Các tính năng

- Theo dõi các cuộc gọi đến trong tài khoản ERPNext của bạn.
- Hiển thị cửa sổ bật lên (pop-up) thông tin khách hàng tiềm năng/khách hàng hiện có cho nhân viên khi có cuộc gọi đến.

## 2. Cách thiết lập

### 2.1 Thiết lập tài khoản Exotel của bạn

- Đăng nhập vào tài khoản Exotel của bạn và đi tới App Bazar.
- Tạo một App mới cho một luồng (flow) mới.
- Thiết lập luồng theo ý muốn của bạn.
- Trong connect API của bạn, dưới mục "Create popup..." và dán URL sau:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

![Connect Applet](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/exotel_integration/connect_applet.png)
![Call Popup Section](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/exotel_integration/create_popup_section.png)

> **Lưu ý:** Thay thế `<your-site>` trong URL bằng tên trang web của bạn. Ví dụ, nếu tên trang web là **frappe.erpnext.com** thì URL sẽ là:
`https://frappe.erpnext.com/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

- Sau đó, thêm một Passthru applet dưới mục "After Call Conversation ends" và dán URL sau:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_end_call`

![After Conversation Ends Section](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/exotel_integration/after_conversation_ends_section.png)

![After call ends section](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/exotel_integration/passthru_end_call.png)

> **Lưu ý:** Hãy đảm bảo đã tích chọn "Make Passthru Async".

- Tương tự, thêm một Passthru applet dưới mục "If nobody answers..." và dán URL sau:
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_missed_call`

![No Response Section](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/exotel_integration/no_response.png)

![After call ends section](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/erpnext_integrations/exotel_integration/passthru_missed_call.png)

> **Lưu ý:** Hãy đảm bảo đã tích chọn "Make Passthru Async".

- Lưu luồng (flow).
- Bây giờ, hãy gán ứng dụng mới tạo này cho ExoPhone mà bạn dùng để nhận các cuộc gọi kinh doanh.

### 2.2 Thiết lập trong ERPNext

- Từ Awesome Bar, đi tới 'Exotel Settings'.
- Thiết lập "Exotel SID" và "Exotel Token" của bạn. Bạn có thể tìm thấy Exotel API key và token tại [Exotel Dashboard](https://my.exotel.com/apisettings/site#api-credentials) của mình.
- Đi tới Communication Medium.
- Thêm ExoPhone của bạn và lên lịch cho số điện thoại đó. Dựa trên lịch trình này, nhân viên sẽ nhận được cửa sổ pop-up.