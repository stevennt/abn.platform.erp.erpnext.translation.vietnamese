# Mã Coupon

**Mã Coupon cho phép Khách hàng được hưởng chiết khấu trên các sản phẩm trong giỏ hàng.**

Mọi người đều yêu thích chiết khấu! Các mã coupon cung cấp các mức chiết khấu như vậy cũng vậy. Để khuyến khích Khách hàng mua hàng từ website thương mại điện tử, tính năng mã coupon rất thú vị.

Có những đại lý/trang web khác tạo ra Khách hàng tiềm năng cho các sản phẩm/mặt hàng/dịch vụ trên website thương mại điện tử ERPNext của bạn.

Khi Khách hàng tiềm năng đến từ các trang web khác HOẶC từ các email quảng cáo đến website ERPNext của bạn để mua hàng, bạn nên có khả năng:

	a) Theo dõi xem Khách hàng tiềm năng đến từ đối tác liên kết / Đối tác bán hàng nào, tức là [mã giới thiệu]
	(/docs/v16/user/manual/en/selling/sales-partner)

	b) Giảm giá (dựa trên Quy tắc định giá) cho toàn bộ đơn mua hàng, tức là Mã Coupon

Để truy cập danh sách Mã Coupon, hãy đi tới:

> Home > Accounting > Coupon Code


## 1. Điều kiện tiên quyết

1. Tính năng Mã Coupon cần được kích hoạt từ Cài đặt Giỏ hàng:

	> Home > Settings > Shopping Cart Settings

	<img class="screenshot" alt="Shopping Cart Settings to enable Coupon Code" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/coupon-code-shoppingcart-settings.png">

1. Tạo một Quy tắc định giá có bật cờ **Coupon Code Based**.

## 2. Cách tạo Mã Coupon

1. Đi tới danh sách Mã Coupon và nhấn vào Mới.
2. Nhập **Coupon Name** (Tên Coupon), ví dụ: "SAVE 20"
3. Trong mục **Coupon Type** (Loại Coupon), chọn từ Promotional (Khuyến mãi) hoặc Gift Card (Thẻ quà tặng).

	Promotional dùng để quảng bá một chương trình chung.

	Gift Card dùng để tạo ngẫu nhiên mã coupon và phân phối cho khách hàng/người dùng cụ thể.

4. **Coupon Code** là mã duy nhất chỉ đọc được viết bằng chữ in hoa, mã này được tạo dựa trên Loại Coupon & Tên Coupon.

	Đối với Loại Coupon:

	a) *Promotional*, nó sẽ loại bỏ tất cả khoảng trắng và lấy tối đa 8 ký tự đầu tiên. Ví dụ: SAVE20

	b) *GiftCard*, nó sẽ tạo mã ngẫu nhiên gồm 11 chữ số. Ví dụ: AP48K7CT9LP

    Nó có thể được sử dụng trên trang giỏ hàng trước khi đặt hàng để được hưởng chiết khấu.

4. Chọn [Pricing Rule](/docs/v16/user/manual/en/accounts/pricing-rule) có bật cờ **coupon code based**.

5. Nhấn Lưu

	<img class="screenshot" alt="Coupon Code Doctype" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/coupon-code.png">

## 3. Các tính năng

### 3.1 Hiệu lực và Sử dụng

1. **Valid From - To** - thời hạn hiệu lực của coupon
2. **Maximum Use** - Giới hạn số lần sử dụng mã coupon
3. **Used** - đối với mỗi Đơn bán hàng được Xác nhận với mã coupon, số lần đã sử dụng sẽ tăng thêm 1.
4. **Coupon Code Description** - có thể được sử dụng khi tạo Mẫu email để thông báo cho khách hàng tiềm năng về mã coupon và thông tin chương trình

	<img class="screenshot" alt="Pricing Rule Coupon Code Based" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/coupon-code-pricing-rule.png">



### 3.2 Mã Coupon có thể được áp dụng theo hai cách

1. Thông qua URL, mã coupon sẽ tự động được lấy từ tham số URL ("cc") và điền vào ô nhập mã Apply Coupon Code để người dùng dễ dàng áp dụng.

	http://xyz.erpnext.com/products/golden-ring?cc=SAVE5

2. Áp dụng mã một cách rõ ràng, bằng cách điền mã và nhấn nút "Apply Coupon Code" như hiển thị dưới đây trong trang giỏ hàng

	<img class="screenshot" alt="Shopping Cart Apply CouponCode" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/coupon-code-pricing-rule.png">

Giá sẽ được cập nhật sau khi áp dụng mã coupon thành công.


### 4. Các chủ đề liên quan

1. [Shopping Cart](/docs/v16/user/manual/en/website/shopping-cart)
2. [Pricing Rule](/docs/v16/user/manual/en/accounts/pricing-rule)