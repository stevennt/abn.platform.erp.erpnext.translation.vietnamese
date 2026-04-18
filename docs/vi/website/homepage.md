<!-- add-breadcrumbs -->
# Trang chủ

**Trang chủ là trang đích mặc định của website của bạn.**

Phân hệ Website của ERPNext tạo ra một trang đích mặc định cho website của bạn. Bạn có thể tùy chỉnh nó trong Trang chủ.

Để truy cập trang Trang chủ trong ERPNext, hãy đi đến:

> Home > Website > Portal > Homepage

## 1. Cách thiết lập Trang chủ
1. Chọn Công ty.
1. Thiết lập Tiêu đề. Tiêu đề này sẽ được hiển thị trên Tab của Trình duyệt.
1. Cấu hình Phần Hero (Hero Section) như được giải thích trong phần tiếp theo.

![Homepage](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/homepage.png)
*Trang chủ*

> Hãy đảm bảo 'Trang chủ' mặc định của bạn được thiết lập là `home` trong Cài đặt Website để
> tính năng này hoạt động.

## 2. Phần Hero (Hero Section)

Có ba cách để bạn có thể tùy chỉnh giao diện của Phần Hero:

1. Câu khẩu hiệu (Tag Line) và Mô tả (Description) (Mặc định).
1. Trình chiếu Trang chủ (Homepage Slideshow).
1. Phần Hero Tùy chỉnh (Custom Hero Section).

### 2.1 Câu khẩu hiệu và Mô tả

Sau khi bạn thiết lập Câu khẩu hiệu, Mô tả và Hình ảnh Hero, bạn sẽ có một trang đầu với giao diện đẹp mắt. Bạn cũng có thể thay đổi URL cho nút Khám phá (Explore) trong mục **URL cho "Tất cả sản phẩm"**.

![Website Homepage](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/website-homepage.png)
*Trang chủ Website*

### 2.2 Trình chiếu Trang chủ

Thiết lập **Hero Section Based On** thành **Slideshow** và trường **Homepage Slideshow** sẽ xuất hiện.

![Homepage Slideshow Setting](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/homepage-slideshow-setting.png)
*Thiết lập Trình chiếu Trang chủ*

Bây giờ, hãy chọn một Slideshow hiện có hoặc tạo một cái mới như sau:

![Website Slideshow](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/website-slideshow.png)
*Trình chiếu Website*

> Để có kết quả tốt nhất, hãy đảm bảo tất cả các hình ảnh trình chiếu của bạn có cùng chiều cao và
> chiều rộng lớn hơn chiều cao.

![Website Homepage with Slideshow](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/website-homepage-slideshow.gif)

### 2.3 Phần Hero Tùy chỉnh

Loại Phần Hero thứ ba cho phép bạn viết mã HTML của riêng mình.

Thiết lập **Hero Section Based On** thành **Hero Section**.

Bây giờ hãy tạo một Phần Hero mới. Thiết lập **Section Based On** là **Custom HTML**.
Viết mã HTML tùy chỉnh của bạn vào trường Section HTML.

![Homepage Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/homepage-hero-custom.png)
*Cài đặt Trang chủ*

Bạn có thể viết bất kỳ mã đánh dấu [Bootstrap 4](https://getbootstrap.com/docs/v13/4.3/getting-started/introduction/) hợp lệ nào tại đây.

![New Hero Section](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/hero-custom.png)
*Phần Hero mới*

Nó sẽ trông giống như thế này:
![Homepage Hero Custom](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/website-homepage-custom.png)
*Phần Hero tùy chỉnh của Trang chủ*

## 3. Sản phẩm nổi bật

Bạn cũng có thể hiển thị các sản phẩm nổi bật trên Trang chủ bằng cách thêm chúng vào bảng Sản phẩm.

![Homepage Products Table](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/homepage-featured-products.png)
*Bảng Sản phẩm của Trang chủ*

Nó sẽ trông giống như thế này:
![Featured Products on Homepage](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/website-featured-products.png)
*Sản phẩm nổi bật trên Trang chủ*

## 4. Phần Trang chủ

Bạn có thể thêm các phần tùy chỉnh trên Trang chủ bằng cách tạo các Phần Trang chủ mới.

> Đi đến Website > Portal > Homepage Section

Một phần trang chủ có thể bao gồm các thẻ (cards) hoặc HTML tùy chỉnh. Thiết lập **Section Based On**
thành **Cards**.

![New Homepage Section](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/new-homepage-section.png)
*Phần Trang chủ mới*

Thêm chi tiết cho mỗi thẻ như Tiêu đề, Phụ đề, Hình ảnh, Nội dung và Đường dẫn trong bảng Section Cards.

Nó sẽ trông giống như thế này:
![Homepage Section](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/homepage-section.png)
*Phần Trang chủ*

Bạn cũng có thể kiểm soát thứ tự xuất hiện của các phần này bằng cách thiết lập
**Section Order**. Số 0 sẽ được hiển thị trước, sau đó đến 1, v.v.

> Để thêm các Phần với HTML tùy chỉnh, hãy tham khảo [Custom Hero Section](#23-custom-hero-section).

## 5. Trang chủ Tùy chỉnh

ERPNext cho phép bạn có một trang chủ hoàn toàn khác nếu bạn không muốn
sử dụng trang mặc định được mô tả ở trên.

Để thiết lập một trang chủ tùy chỉnh:

1. Tạo một [Web Page](web-page.md).
1. Đi đến Website > Setup > Website Settings.
1. Thiết lập Home Page làm `route` cho Web Page của bạn.
   ![](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/custom-homepage.png)

{next}