<!-- add-breadcrumbs -->
# Giao diện Website

ERPNext cung cấp các khả năng tùy chỉnh giao diện nâng cao để thay đổi diện mạo và cảm giác cho website của bạn, giúp nó phù hợp với thương hiệu của bạn.

> Trang chủ > Website > Thiết lập > Giao diện Website

## 1. Cách tạo Giao diện Website

1. Đi tới danh sách Giao diện Website và nhấn vào Mới.
1. Nhập Tên giao diện.
2. Tùy chỉnh giao diện của bạn.
3. Nhấn vào Lưu.

> **Lưu ý:** Hãy đảm bảo bạn đã thiết lập Giao diện Website trong Cài đặt Website để giao diện được áp dụng.

![Select Website Theme in Website Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/website-theme.png)

## 2. Các tính năng

### 2.1 Cấu hình Giao diện

Phần "Cấu hình Giao diện" dùng để khởi tạo một giao diện cơ bản. Tại đây bạn có thể chọn bảng màu, phông chữ và kiểu dáng nút bấm.

### 2.2 Bảng kiểu (Stylesheet)

Nếu bạn biết về [SCSS](https://sass-lang.com/guide) và [tùy chỉnh Bootstrap 5](https://getbootstrap.com/docs/5.0/customize/theming/), bạn có thể tự viết mã SCSS tùy chỉnh.

Trong trường "Ghi đè tùy chỉnh" (Custom Overrides), bạn có thể ghi đè các biến được định nghĩa bởi tệp giao diện của bất kỳ ứng dụng nào. Nội dung của trường này sẽ được bao gồm *trước khi* nhập bất kỳ SCSS nào khác. Ví dụ: biến `$spacer` được đặt mặc định là `1rem`. Chỉ cần định nghĩa lại thành `$spacer: 2rem;` để làm cho tất cả các khoảng cách lớn gấp đôi.

Trong trường "SCSS tùy chỉnh" (Custom SCSS), bạn có thể thêm các kiểu dáng riêng của mình. Phần này sẽ được bao gồm *sau khi* nhập các giao diện của ứng dụng. Bạn cũng có thể ghi đè bất kỳ kiểu dáng cụ thể nào. Ví dụ: nếu bạn không thích các nút bấm của chúng tôi, chỉ cần thêm đoạn mã sau:

```scss
.btn-primary {
    background-color: $teal;
    color: $orange;
}
```

### 2.3 Các tệp Giao diện được bao gồm

Nếu bạn xem qua giao diện mặc định được tạo bởi hộp thoại cấu hình, nó sẽ nhập `frappe/public/scss/website` và `erpnext/public/scss/website`. Đây là các tệp giao diện mặc định cho ứng dụng `frappe` và `erpnext`. Nếu bạn có cài đặt các ứng dụng khác, chúng cũng có thể cung cấp tệp `website.scss` riêng.

Phần "Các tệp Giao diện được bao gồm" liệt kê tất cả các ứng dụng đã cài đặt. Mỗi ứng dụng có thể mang theo tệp giao diện riêng của nó (`[app]/public/scss/website.scss`). Một giao diện có thể là đầy đủ, cung cấp kiểu dáng cho toàn bộ website, hoặc chỉ là một phần bổ sung. Ví dụ: nó có thể chỉ định kiểu dáng cho các thành phần mà nó giới thiệu. Bằng cách tích vào các ô, bạn có thể chọn giao diện nào sẽ được bao gồm trong website của mình.

![Included Theme Files](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/website-theme-included-theme-files.gif)

### 2.4 JS tùy chỉnh

Bạn cũng có thể viết JavaScript tùy chỉnh để chạy khi giao diện của bạn được áp dụng. Hãy sử dụng nó để thêm/xóa các lớp (classes) khỏi các thành phần, hoặc bất kỳ tập lệnh nào giúp bạn thay đổi diện mạo của các thành phần đó.

{next}