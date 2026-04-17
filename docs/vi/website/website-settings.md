<!-- add-breadcrumbs -->
# Cài đặt Website

Các cài đặt liên quan đến website như trang đích và giao diện toàn website có thể được cấu hình tại đây.

Để truy cập Cài đặt Website, hãy đi đến:
> Home > Website > Setup > Website Settings

## 1. Trang đích (Landing Page)

Cấu hình trang đích mặc định cho website của bạn bằng cách thiết lập trường **Home Page** thành đường dẫn (route) của trang đó. Bạn có thể nhập bất kỳ đường dẫn nào tại đây bao gồm các đường dẫn tiêu chuẩn như `home`, `about`, `contact`, `login`, `all-products`, và `blog`.

Bạn cũng có thể thiết lập một [Web Page](/docs/v13/user/manual/en/website/web-page) làm trang đích.

Nếu bạn muốn sử dụng [Homepage](/docs/v13/user/manual/en/website/homepage) của ERPNext, bạn phải thiết lập nó là `home`.

![Website Settings - Landing Page](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-landing-page.png)
*Website Settings - Landing Page*

Bạn cũng có thể thiết lập **Title Prefix** tại đây. Nó sẽ được thêm vào tiêu đề trình duyệt trên mọi trang. Bạn có thể nhập tên công ty của mình tại đây.

## 2. Giao diện Website (Website Theme)

Tạo một giao diện cá nhân hóa cho Website của bạn và thiết lập tại đây. Tìm hiểu thêm về cách cấu hình Website Theme [tại đây](/docs/v13/user/manual/en/website/website-theme).

## 3. Thương hiệu (Brand)

### 3.1 Logo Thương hiệu

Bạn có thể thiết lập logo thương hiệu cho website của mình trong phần này. Hãy tải lên Brand Image trước, sau đó nhấp vào nút "Set Banner from Image". Nó sẽ tạo ra một Banner HTML với logo bạn đã tải lên.

![Website Settings - Banner Image](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-banner-image.png)
*Website Settings - Banner Image*

### 3.2 Favicon

Bạn cũng có thể thiết lập favicon cho website của mình trong phần này. Nó sẽ xuất hiện ở phía bên trái của tab trình duyệt.

![Website Settings - Favicon](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-favicon.png)
*Website Settings - Favicon*

Xem website của bạn bằng cách nhấp vào **View Website** trên thanh hành động ở góc trên bên phải.

![Website with Brand and Favicon](https://docs.erpnext.com/docs/v13/assets/img/website/website-brand-and-favicon.png)
*Website with Brand and Favicon*

## 4. Thanh điều hướng trên (Top Bar)

Bạn có thể tùy chỉnh các mục menu trong thanh điều hướng (navbar) của website từ phần **Top Bar**.

![Website Setting - Top Bar](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-top-bar.png)
*Website Setting - Top Bar*

![Website Navbar Items](https://docs.erpnext.com/docs/v13/assets/img/website/website-navbar-items.png)
*Website Navbar Items*

## 5. Banner

Bạn có thể thêm một banner cố định vào website của mình, banner này sẽ được hiển thị phía trên thanh điều hướng trên tất cả các trang web. Bạn có thể viết bất kỳ mã HTML Bootstrap 4 hợp lệ nào tại đây.

![Website Settings - Banner](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-banner.png)
*Website Settings - Banner*

![Website Banner](https://docs.erpnext.com/docs/v13/assets/img/website/website-banner.png)
*Website Banner*

## 6. Chân trang (Footer)

Bạn có thể thêm thông tin địa chỉ và các liên kết theo danh mục vào chân trang của mình trong phần **Footer**.

![Website Settings - Footer Address](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-footer-address.png)
*Website Settings - Footer Address*

![Website Settings - Footer Links](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-footer-links.png)
*Website Settings - Footer Links*

![Website Footer](https://docs.erpnext.com/docs/v13/assets/img/website/website-footer.png)
*Website Footer*

## 7. Tích hợp Google

### 7.1 Google Indexing (Lập chỉ mục Google)

#### Cách thiết lập Google Indexing tự động

Để cho phép ERPNext yêu cầu các trình thu thập dữ liệu (crawler) của Google lập chỉ mục một trang web, bạn cần ủy quyền cho ERPNext gửi yêu cầu bất cứ khi nào người dùng yêu cầu dữ liệu. Tích hợp Google Drive được thiết lập theo các bước sau:

- Tạo Google OAuth 2.0 Credentials thông qua [Google Settings](/docs/v13/user/manual/en/erpnext_integration/google_settings)

- Bật tính năng lập chỉ mục (indexing) trong Website Settings

- Bây giờ, hãy nhấp vào **Authorize API Indexing Access** để ủy quyền cho ERPNext gửi yêu cầu xuất bản.

- Sau khi được Ủy quyền, một yêu cầu lập chỉ mục sẽ tự động được gửi khi tạo/cập nhật/xóa bất kỳ bài viết blog hoặc trang web mới nào được tạo bởi người dùng.

![Google Integrations](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-integrations.png)
*Google Integrations*

### 7.2 Google Analytics

Bạn có thể bật Google Analytics trên website của mình. Chỉ cần lấy [Google Analytics ID](https://support.google.com/analytics/answer/1008080?hl=en) từ Google Console của bạn và thiết lập tại đây.

Theo mặc định, Google Analytics sẽ thu thập địa chỉ IP đầy đủ của khách truy cập website của bạn. Bằng cách tích vào "Google Analytics Anonymize IP", ERPNext sẽ hướng dẫn Google Analytics ẩn danh địa chỉ IP trước khi nó được gửi đến máy chủ của Google. Bạn có thể tìm hiểu thêm về tác động của cài đặt này trong [tài liệu của Google](https://support.google.com/analytics/answer/2763052).

## 8. HTML Header

Bạn có thể sử dụng phần này để thiết lập các thẻ meta cho tất cả các trang web của mình. Một trường hợp sử dụng phổ biến là thêm các thẻ xác minh trang web của Google.

![Website Settings - Header](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-header.png)
*Website Settings - Header*

## 9. Robots

Bạn có thể định nghĩa các quy tắc `robots.txt` trong phần này. Thông tin này được các trình thu thập dữ liệu web sử dụng để quyết định trang nào nên lập chỉ mục và trang nào nên bỏ qua.

![Website Settings - Robots](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-robots-txt.png)
*Website Settings - Robots*

> Tìm hiểu thêm về `robots.txt` tại [Moz - Robots.txt](https://moz.com/learn/seo/robotstxt)

## 10. Chuyển hướng (Redirects)

Bạn có thể định nghĩa việc ánh xạ các chuyển hướng đường dẫn tại đây. Việc ánh xạ trong ảnh chụp màn hình sau đảm bảo rằng nếu người dùng truy cập `https://apple.erpnext.com/iphone`, họ sẽ được chuyển hướng đến `https://apple.erpnext.com/products/iphone`.

ERPNext sẽ đưa ra phản hồi `301 Permanent Redirect` cho các đường dẫn này.

![Website Settings - Routes Redirects](https://docs.erpnext.com/docs/v13/assets/img/website/website-settings-route-redirects.png)
*Website Settings - Routes Redirects*

> Nếu bạn đang chuyển đổi website hiện tại của mình sang website dựa trên ERPNext, bạn có thể ánh xạ các đường dẫn cũ sang đường dẫn mới tại đây và các chuyển hướng này sẽ được Google ghi nhận, giúp bạn duy trì thứ hạng SEO.

## 11. Chat

Bạn có thể bật tính năng chat với khách truy cập website trong phần Chat. Widget chat sẽ được hiển thị giữa thời gian **From**