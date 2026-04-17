---
title: Cài đặt LinkedIn
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Cài đặt LinkedIn cho Bài đăng trên Mạng xã hội
 keywords: Lập lịch Bài đăng trên Mạng xã hội, CRM, frappe, tính năng mới erpnext, erp, open source erp, free erp, security
---

# Cài đặt LinkedIn

Các cài đặt liên quan đến LinkedIn như OAuth có thể được cấu hình tại đây. ERPNext cần quyền truy cập vào API để chia sẻ bài đăng và việc này được thực hiện thông qua Giao thức Xác thực OAuth 2.0.

## 1. Cách thiết lập Ứng dụng LinkedIn Developer

Bạn phải có Ứng dụng LinkedIn Developer cho công ty của mình. ERPNext sẽ tương tác với Ứng dụng này để chia sẻ bài đăng.

### 1.1 Tạo Ứng dụng LinkedIn Developer

Tạo Ứng dụng bằng liên kết `https://www.linkedin.com/developers`, điền đầy đủ các chi tiết và xác minh nó. Ứng dụng đó cần có các sản phẩm sau:

1. Share on LinkedIn
2. Sign In with LinkedIn
3. Marketing Developer Platform
![LinkedIn Developer App Product](https://docs.erpnext.com/docs/v16/assets/img/crm/linkedin-dev-products.png)

### 1.2 Cấu hình Redirect URLs:

1. Đi tới Ứng dụng LinkedIn Developers của bạn, sau đó chọn tab **Auth**.
2. Trong phần **OAuth 2.0 settings**, thêm **Redirect URLs**:
`https://{yoursite}/api/method/erpnext.crm.doctype.linkedin_settings.linkedin_settings.callback`
3. Nhấp vào **Update** để thực hiện thay đổi.
![LinkedIn Redirect URL](https://docs.erpnext.com/docs/v16/assets/img/crm/linkedin-redirect-urls.png)

## 2. Cách thiết lập Cài đặt LinkedIn

Để truy cập Cài đặt LinkedIn, hãy đi tới:
> Home > CRM > Settings > LinkedIn Settings

![LinkedIn Settings](https://docs.erpnext.com/docs/v16/assets/img/crm/linkedin-settings.png)

### Company ID
Bạn lấy Company ID từ URL Công ty LinkedIn của mình.
![LinkedIn Company ID](https://docs.erpnext.com/docs/v16/assets/img/crm/linkedin-company-id.png)

### Consumer Key và Consumer Secret
Bạn lấy **Consumer Key** và **Consumer Secret** từ tài khoản LinkedIn Developer của mình, đi tới:
> `https://www.linkedin.com/developers/` > My Apps > `{Your App}` > Auth

![LinkedIn Client](https://docs.erpnext.com/docs/v16/assets/img/crm/linkedin-client.png)

Sau khi bạn **Lưu** tài liệu bằng cách điền **Company ID**, **Consumer Key**, và **Consumer Secret**, hệ thống sẽ chuyển hướng đến trang đăng nhập của LinkedIn. Bằng cách cung cấp thông tin đăng nhập LinkedIn hợp lệ và nhấp vào Allow (Cho phép), thành viên sẽ phê duyệt yêu cầu của ứng dụng để truy cập dữ liệu thành viên của họ và tương tác với LinkedIn thay mặt họ.
![Authorize LinkedIn](https://docs.erpnext.com/docs/v16/assets/img/crm/authorize-linkedin.jpg)

{next}