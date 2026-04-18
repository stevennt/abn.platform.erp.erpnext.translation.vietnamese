<!-- add-breadcrumbs -->
# Trang Sản phẩm

ERPNext cung cấp các trang sản phẩm cho các Mặt hàng bán hàng của bạn, chúng có thể được cấu hình từ
Mặt hàng (Item Master).

Trang Sản phẩm được xây dựng cho một Mặt hàng. Nếu bạn chưa tạo bất kỳ Mặt hàng nào, hãy đi đến:
> Trang chủ > Kho > Mặt hàng và Giá bán > Mặt hàng

## 1. Cách cấu hình Trang Sản phẩm
1. Nhập Mã mặt hàng, Tên mặt hàng, Nhóm mặt hàng và Đơn giá bán.
    ![New Item](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/new-item.png)
1. Nhấp vào nút **Edit in full page** để mở biểu mẫu.
1. Đi đến phần Website và bật **Show in Website**.
1. Nhấp vào Lưu.
1. Xem Trang Sản phẩm của bạn bằng cách nhấp vào **Show on Website** ở thanh bên.

> Đọc [tài liệu về Mặt hàng](../stock/item.md) để tìm hiểu thêm.

### 1.1 Mặt hàng có Biến thể

Nếu bạn có một Mặt hàng có nhiều biến thể, ví dụ: Apple iPhone XR
với các màu sắc và dung lượng lưu trữ khác nhau, bạn có thể tạo một Mặt hàng Mẫu (Template Item).

Đi đến phần Variants và bật **Has Variants** và thêm các
thuộc tính vào bảng thuộc tính.

![Item with Variants](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/item-with-variants.png)
*Mặt hàng có Biến thể*

> Tìm hiểu thêm về cách tạo Mặt hàng có Biến thể [tại đây](../stock/item-variants.md)

## 2. Các tính năng

### 2.1 Mô tả Website

Bạn có thể thêm **Mô tả Website** từ phần Thông số kỹ thuật Website.
Nó sẽ chỉ hiển thị trên trang sản phẩm của bạn.

![Item Website Description](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/item-website-description.png)
*Mô tả Website của Mặt hàng*

### 2.2 Hình ảnh và Trình chiếu

Bạn có thể thêm các hình ảnh và trình chiếu khác nhau để hiển thị trên website của mình từ
phần Website.

![Item Image and Slideshow](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/item-image-slideshow.png)
*Hình ảnh và Trình chiếu của Mặt hàng*

### 2.3 Thông số kỹ thuật Mặt hàng

Bạn có thể thêm các Thông số kỹ thuật của Mặt hàng trong phần Thông số kỹ thuật Website. Nó
sẽ hiển thị dưới dạng một bảng trên Trang Sản phẩm của bạn.

![Item Website Specifications](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/item-website-specifications.png)
*Thông số kỹ thuật Website của Mặt hàng*

### 2.4 Xuất bản Mặt hàng

Để xuất bản mặt hàng của bạn, hãy đi đến phần Website và bật **Show in Website**.

![Publish Item](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/publish-item.png)
*Xuất bản Mặt hàng*

Bây giờ bạn sẽ thấy liên kết **See on Website** ở thanh bên. Nhấp vào đó để xem
trang sản phẩm của bạn.

![Product Page](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/product-page.png)
*Trang Sản phẩm*

### 2.5 HTML Tùy chỉnh

Bạn có thể tùy chỉnh thêm Trang Sản phẩm của mình bằng cách thêm HTML Tùy chỉnh trong trường Nội dung Website của phần Thông số kỹ thuật Website.

![Custom Website Content](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/custom-website-content.png)
*Nội dung Website Tùy chỉnh*

![Product Page with Custom Content](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/product-page-with-custom-content.png)
*Trang Sản phẩm với Nội dung Tùy chỉnh*

### 2.6 Kho Website
Tính năng này có sẵn trong [Mặt hàng](../stock/item.md#318-website). Chọn một kho hiện có hoặc tạo một kho mới cho các giao dịch thông qua website của bạn. Kho này sẽ khác với các Kho ngoại tuyến của bạn. Tồn kho cho bất kỳ giao dịch trực tuyến nào sẽ được trừ vào Kho được thiết lập trong phần Kho Website.

> Lưu ý: Nếu Kho Website không được thiết lập và mục 'Maintain Stock' cho một Mặt hàng được tích chọn, trang sản phẩm sẽ liệt kê Mặt hàng đó là 'Không có trong kho'.

{next}