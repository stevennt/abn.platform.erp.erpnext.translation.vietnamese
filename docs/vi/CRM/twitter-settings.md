---
title: Cài đặt Twitter
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Cài đặt Twitter cho Bài đăng trên Mạng xã hội
 keywords: Lập lịch Bài đăng trên Mạng xã hội, CRM, frappe, tính năng mới erpnext, erp, open source erp, free erp, security
---

# Cài đặt Twitter

Các cài đặt liên quan đến Twitter như OAuth có thể được cấu hình tại đây. ERPNext cần quyền truy cập vào API để chia sẻ bài đăng và việc này được thực hiện thông qua Giao thức Xác thực OAuth 2.0.

## 1. Cách thiết lập Ứng dụng Twitter

Bạn phải có Ứng dụng Twitter cho công ty của mình. ERPNext tương tác với Ứng dụng này để chia sẻ Tweet.

### 1.1 Tạo Ứng dụng Nhà phát triển Twitter (Twitter Developer App)

Tạo Ứng dụng bằng liên kết `https://developer.twitter.com/` và kiểm tra xem Ứng dụng đã có quyền truy cập **Read and write** (Đọc và ghi) hay chưa.
![Twitter App Permission](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/twitter-app-permission.png)

### 1.2. Cấu hình Callback URL
1. Chọn Ứng dụng của bạn và đi tới **App Details**.
2. Sau đó đi tới **Edit** và nhấp vào **Edit Details**.
3. Thêm URL trang web của bạn vào mục **Callback URLs** như sau:
`https://{yoursite}/api/method/erpnext.crm.doctype.twitter_settings.twitter_settings.callback`
4. Nhấp **Lưu** để thực hiện thay đổi.

![Twitter App Callback URL](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/twitter-callback-url.png)


## 2. Cách thiết lập Cài đặt Twitter

Để truy cập Cài đặt Twitter, hãy đi tới:
> Trang chủ > CRM > Settings > Twitter Settings

![Twitter Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/twitter-settings.png)

### 2.1 API Key và API Key Secret

Bạn lấy **API Key** và **API Key Secret** từ tài khoản Nhà phát triển Twitter của mình bằng cách đi tới:
> `https://developer.twitter.com/` > My Apps > `{Your App}` > Keys and tokens

![Twitter Keys Tokens](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/twitter-key-token.png)

Sau khi bạn Lưu tài liệu bằng cách điền **API Key** và **API Key Secret**, hệ thống sẽ chuyển hướng đến trang đăng nhập của Twitter. Sau khi cung cấp thông tin đăng nhập Twitter hợp lệ và nhấp vào **Authorize app**, thành viên sẽ phê duyệt yêu cầu của ứng dụng để truy cập dữ liệu thành viên của họ và tương tác với Twitter.
![Twitter Authorize App](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/twitter-authorize-app.png)

{next}