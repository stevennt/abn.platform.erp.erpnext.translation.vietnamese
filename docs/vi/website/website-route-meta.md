<!-- add-breadcrumbs -->
# Website Route Meta

**Các thẻ meta tùy ý có thể được thêm vào các trang web của bạn bằng cách sử dụng Website Route Meta.**

Thẻ Meta là các thẻ ẩn cung cấp dữ liệu về trang của bạn cho các công cụ tìm kiếm và khách truy cập trang web. Khi được sử dụng đúng cách, các thẻ này có thể giúp tăng cường SEO và thứ hạng của bạn trên các công cụ tìm kiếm phổ biến. Các thẻ này sẽ được đặt trong phần `<head>` của trang. ERPNext cho phép bạn thêm các thẻ meta tùy ý vào các trang web của mình để cải thiện SEO cho các trang đó.

Để truy cập Website Route Meta, hãy đi tới:

> Home > Website > Web Site > Website Route Meta

## 1. Cách thêm thẻ meta vào một trang web

1. Đi tới danh sách Website Route Meta và nhấn vào New.
1. Nhập route (đường dẫn). Đảm bảo route không bắt đầu bằng dấu gạch chéo (`/`). Một Web Page cho route này phải tồn tại.
1. Thêm các cặp khóa-giá trị (key-value pairs) cho mỗi thẻ meta. Ví dụ: để thêm từ khóa vào trang web của bạn, hãy nhập "keywords" vào cột Key và thêm các từ khóa cách nhau bằng dấu phẩy vào cột Value.
1. Nhấn vào Lưu.

![New Website Route Meta](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/new-website-route-meta.png)
*New Website Route Meta*

Bây giờ nếu bạn kiểm tra mã nguồn của trang web, các thẻ meta sẽ trông giống như thế này:

```html
<meta name="description" content="Now with an 8-core processor, the 15-inch MacBook Pro is the fastest Mac notebook ever.">
<meta name="keywords" content="apple, macbook, macbook pro, intel, 8 core, fastest">
```

> **Lưu ý:** Thẻ Meta không chỉ giới hạn ở Web Page, mà chúng có thể được thêm vào bất kỳ route nào có trang web trong ERPNext.
>
> Ví dụ: Bạn có thể thêm thẻ meta vào các bài viết blog nếu bạn biết route mà bạn có thể lấy từ biểu mẫu Blog Post.

{next}