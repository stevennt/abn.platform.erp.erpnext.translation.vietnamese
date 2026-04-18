<!-- add-breadcrumbs -->
# Trang Web

**Các nội dung tĩnh như Trang chủ, Giới thiệu, Liên hệ, các trang Điều khoản có thể được tạo bằng Trang Web.**

Để truy cập Trang Web, hãy đi tới:

> Home > Website > Web Site > Web Page

## 1. Cách tạo một Trang Web

1. Đi tới danh sách Trang Web và nhấn vào Mới.
1. Nhập Tiêu đề và thêm nội dung vào Phần chính. Đường dẫn (route) sẽ được tự động tạo nhưng bạn có thể thay đổi nó.
1. Nhấn Lưu.
1. Trang web sẽ chỉ được xuất bản khi mục **Published** được tích chọn.

![New Web Page](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/new-web-page.png)
*Trang Web Mới*

Xem Trang Web của bạn bằng cách nhấn vào **See on Website** ở thanh bên.

![Web Page](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-page.png)
*Trang Web*

### 1.1 Mẹo để tạo một Trang Web tốt

#### Tiêu đề

Điều đầu tiên cần thiết lập là tiêu đề của trang. Tiêu đề có trọng số lớn nhất đối với các công cụ tìm kiếm, vì vậy hãy chọn một tiêu đề phản ánh các từ khóa mà bạn đang hướng tới đối tượng khách hàng của mình. Đường dẫn (URL) sẽ được tự động tạo từ tiêu đề nhưng bạn có thể thay đổi nó.

#### Nội dung

Bạn có thể viết nội dung của mình bằng Văn bản định dạng (Rich Text), Markdown hoặc HTML. Nếu bạn muốn tạo các trang nội dung đơn giản, Rich Text và Markdown là những lựa chọn tuyệt vời.

> Tìm hiểu markdown trong vài phút tại [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

#### Hình ảnh

Đối với nội dung Rich Text, bạn có thể nhúng trực tiếp hình ảnh bằng trình soạn thảo. Đối với Markdown và HTML, bạn phải đính kèm hình ảnh vào tài liệu trước. Sau đó, lấy URL của hình ảnh bằng cách nhấp chuột phải vào tệp đính kèm và sao chép địa chỉ.

![Image Link](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/get-image-link.png)

Bây giờ, hãy thêm chúng vào Markdown hoặc HTML của bạn bằng cú pháp phù hợp.

```md
<!-- markdown -->
![Alt Text](/path/to/image-url.png)

<!-- html -->
<img src="/path/to/image-url.png" alt="Alt Text">
```

## 2. Các tính năng

### 2.1 Slideshow

Bạn cũng có thể thêm một Slideshow vào Trang Web của mình. Tham khảo cách tạo Slideshow tại [Homepage Slideshow](homepage.md#22-homepage-slideshow)

### 2.2 Xuất bản theo lịch trình

Bạn có thể lên lịch xuất bản các Trang Web nếu bạn thiết lập Ngày bắt đầu và Ngày kết thúc cho Trang Web của mình. Chúng sẽ được đặt ở trạng thái đã xuất bản trong phạm vi ngày đã chọn và sẽ tự động bị hủy xuất bản khi nằm ngoài phạm vi đó.

Các trang chưa xuất bản sẽ hiển thị lỗi `Error 404` khi được truy cập.

### 2.3 Javascript và CSS

Bạn có thể thêm một đoạn mã JS vào Trang Web của mình trong phần **Script**. Hãy đảm bảo viết mã của bạn bên trong hàm callback `frappe.ready`.

```js
frappe.ready(() => {
	// mã của bạn ở đây
});
```

Bạn có thể thêm định dạng CSS cho Trang Web của mình trong phần **Style**. Hãy kiểm tra các thành phần để xem các lớp (class) nào có sẵn để định dạng. Nếu bạn đang sử dụng nội dung HTML, bạn có thể sử dụng các lớp của riêng mình và định dạng chúng tại đây.

### 2.4 Thanh bên

Bạn có thể thêm một Thanh bên Website với các liên kết tùy chỉnh trên Trang Web của mình. Trong phần **Sidebar and Comments**, hãy bật **Show Sidebar**. Chọn một Thanh bên Website có sẵn hoặc tạo một cái mới.

![Web Page Sidebar](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-page-sidebar.png)
*Thanh bên Trang Web*

Thêm các liên kết và đường dẫn của chúng trong bảng Mục thanh bên (Sidebar Items).
![Website Sidebar](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/new-website-sidebar.png)
*Thanh bên Website*

![Web Page with Sidebar](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-page-with-sidebar.png)
*Trang Web có Thanh bên*

### 2.5 Bình luận

Bạn có thể bật tính năng bình luận trên Trang Web của mình, nơi mọi người có thể để lại bình luận cùng với Tên và Email của họ. Bật bình luận từ phần **Sidebar and Comments**.

![Web Page Comments](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-page-comments.gif)
*Bình luận Trang Web*

### 2.6 Tiêu đề đầu trang (Header)

Bạn có thể thêm HTML tùy chỉnh cho phần tiêu đề đầu trang của trang. Điều này sẽ ghi đè lên tiêu đề của Trang Web.

![Web Page Header](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-page-header.png)
*Tiêu đề đầu trang Trang Web*

![Web Page with Custom Header](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-page-with-custom-header.png)
*Trang Web với Tiêu đề đầu trang tùy chỉnh*

### 2.7 Đường dẫn điều hướng (Breadcrumbs)

Bạn có thể thêm một danh sách đường dẫn điều hướng trên Trang Web của mình. Những đường dẫn này sẽ được hiển thị ở phía trên trước phần tiêu đề đầu trang.

![Web Page Breadcrumbs](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-page-breadcrumbs.png)
*Đường dẫn điều hướng Trang Web*

![Web Page with Breadcrumbs](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-page-with-breadcrumbs.png)
*Trang Web có Đường dẫn điều hướng*

### 2.8 Thẻ Meta

Bạn cũng có thể thêm các Thẻ Meta vào Trang Web của mình. Bạn phải thêm khóa thuộc tính và giá trị của nó trong Bảng Thẻ Meta và nó sẽ tự động tạo các thẻ HTML `meta` trên Trang Web của bạn.

![Web Page Meta Tags](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/web-page-meta-tags.gif)
*Thẻ Meta Trang Web*

{next}