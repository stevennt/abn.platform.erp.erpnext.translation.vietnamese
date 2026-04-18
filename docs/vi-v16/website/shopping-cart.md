<!-- add-breadcrumbs -->
# Giỏ hàng

Ngoài việc liệt kê các sản phẩm của bạn, ERPNext còn cho phép bạn bán chúng thông qua
Giỏ hàng.

Để kích hoạt Giỏ hàng, hãy đi tới:

> Trang chủ > Website > Portal > Shopping Cart Settings

![Shopping Cart Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/shopping-cart-settings.png)
*Shopping Cart Settings*

Bạn thậm chí có thể xây dựng một **trang đích (landing page)** cho cửa hàng của mình tại một đường dẫn tùy chỉnh (ví dụ: /*store*).
Đọc [tài liệu hướng dẫn](../user/manual/website/store-landing-page) để tìm hiểu cách thực hiện!

Dưới đây là một số tùy chọn cấu hình:

1. **Show Price**: Hiển thị Đơn giá Mặt hàng trên trang sản phẩm.
1. **Show Stock Availability**: Hiển thị xem Mặt hàng còn trong kho hay không.
1. **Show Stock Quantity**: Hiển thị số lượng tồn kho hiện có trên trang sản phẩm.
1. **Show Configure Button**: Hiển thị nút cấu hình nếu Mặt hàng có các biến thể.
   Nút này có thể được sử dụng để thu hẹp lựa chọn mặt hàng cụ thể dựa trên các Thuộc tính.
1. **Show Contact Us Button**: Hiển thị nút liên hệ để Khách hàng có thể sử dụng
   để hỏi về Mặt hàng. Nó sẽ tạo một Khách hàng tiềm năng trong hệ thống.

## 1. Loại Mặt hàng

Giỏ hàng hoạt động khác nhau đối với các Mặt hàng có và không có biến thể.

### 1.1 Mặt hàng không có biến thể

Các Mặt hàng không có biến thể sẽ có trang sản phẩm riêng và nút **Thêm vào giỏ hàng**.
Thông tin tồn kho cũng sẽ được hiển thị nếu tùy chọn này được bật trong
Shopping Cart Settings.

![Item without Variants](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/item-without-variants.png)
*Mặt hàng không có biến thể*

### 1.2 Mặt hàng có biến thể

Vì các Mẫu Mặt hàng (Item Templates) không thể được mua trực tiếp, nên sẽ có nút Cấu hình để
chọn biến thể cụ thể và thêm vào giỏ hàng.

![Item with Variants](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/item-with-variants.gif)
*Mặt hàng có biến thể*

## 2. Báo giá từ Giỏ hàng

Nếu tính năng thanh toán bị vô hiệu hóa, khi khách hàng thêm một mặt hàng vào giỏ hàng, họ có thể nhấp
vào nút **Yêu cầu báo giá** để nhận báo giá cho mặt hàng đó. Một [Báo giá](../user/manual/selling/quotation)
sẽ được tạo trong hệ thống.

![Cart Quotation](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/cart-quotation.png)
*Báo giá từ giỏ hàng*

## 3. Thanh toán Giỏ hàng

Bạn có thể kích hoạt thanh toán từ phần **Checkout Settings** trong
Shopping Cart Settings. Bạn phải có [Tích hợp PayPal](../user/manual/erpnext_integration/paypal-integration)
hoặc [Tích hợp Razorpay](../user/manual/erpnext_integration/razorpay-integration)
để cho phép thanh toán.

![Cart Checkout Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/cart-checkout-settings.png)
*Cài đặt thanh toán giỏ hàng*

![Cart Checkout](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/cart-checkout.png)
*Thanh toán giỏ hàng*