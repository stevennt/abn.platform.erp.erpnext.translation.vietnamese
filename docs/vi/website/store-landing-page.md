<!-- add-breadcrumbs -->
# Trang đích Cửa hàng

Sau khi kích hoạt Giỏ hàng (Shopping Cart) cho ứng dụng của bạn, bạn có thể tạo một trang đích tùy chỉnh cho cửa hàng của mình bằng cách sử dụng [Trình xây dựng Trang Web](/docs/v13/user/manual/en/website/web-page-builder).

![Store Landing Page](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/store-landing-page.png)
*Trang đích Cửa hàng tùy chỉnh*

## 1. Cách tạo Trang đích Cửa hàng tùy chỉnh

1. Thực hiện theo các bước được đề cập tại đây để [tạo một Trang Web](/docs/v13/user/manual/en/website/web-page).
1. Thiết lập Đường dẫn (Route) cho trang của bạn (ví dụ: */store*).
1. Chọn Loại nội dung (Content Type) là **Page Builder**.
1. Nhấp vào Thêm hàng (Add Row) trong Bảng Khối xây dựng Trang (Page Building Blocks Table).
1. Chọn một Mẫu Web (Web Template).

	ERPNext đi kèm với một bộ mẫu web tiêu chuẩn tuyệt vời có thể được sử dụng để tạo Trang Web của bạn.

	Cấu hình cho trang trong ảnh chụp màn hình trên trông như thế này:

	![Store Web Templates](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/store-web-templates.png)
	*Các Khối xây dựng Trang Cửa hàng*

1. Thêm Giá trị.

	Nhấp vào nút Chỉnh sửa giá trị (Edit Values) ở bên phải của mỗi khối, và nhập các giá trị vào hộp thoại để thiết lập nội dung cho từng phần.

	Các Mẫu Web sẽ hữu ích để xây dựng trang đích cửa hàng của bạn là:

	- **Hero Slider (Trình trượt chính):**
		Có thể tạo tối đa 5 slide. Hình ảnh, tiêu đề, hành động chính, căn lề, chủ đề cho mỗi slide đều có thể cấu hình được.
		![Store Hero Slider](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/store-hero-slider.png)
		*Cấu hình Hero Slider*

	- **Product Category Cards (Thẻ Nhóm mặt hàng):**
		Có thể cấu hình tối đa 8 thẻ nhóm mặt hàng. Mỗi nhóm mặt hàng sẽ liên kết đến một [Nhóm mặt hàng](/docs/v13/user/manual/en/stock/item-group).
		Đảm bảo rằng tùy chọn **Show in Website** được tích trong biểu mẫu Nhóm mặt hàng để đường dẫn cho nhóm mặt hàng được tạo ra.

		![Store Product Category Cards](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/store-product-category.png)
		*Cấu hình Nhóm mặt hàng*

	- **Item Card Group (Nhóm thẻ Mặt hàng):**
		Phần này có thể được sử dụng để trưng bày các mặt hàng nổi bật của bạn. Có thể cấu hình tối đa 12 thẻ.
		Mỗi thẻ sẽ liên kết đến một [Mặt hàng](/docs/v13/user/manual/en/stock/item). Nếu mục **featured** được chọn, mặt hàng sẽ chiếm 2 cột không gian.

		![Store Item Card Group](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/store-item-card-group.png)
		*Cấu hình Thẻ Mặt hàng*


1. Xuất bản Trang Web của bạn.

	Trang web sẽ chỉ được xuất bản khi tùy chọn Xuất bản (Published) được tích.
	Sau khi trang đã được xuất bản, hãy nhấp vào **See on Website** ở thanh bên hoặc truy cập vào đường dẫn đã cấu hình để xem trang!

	![Store Page Published](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/website/store-page-published.png)
	*Xuất bản Trang Web của bạn*

1. Thiết lập làm Trang chủ.

	Thực hiện theo các bước [tại đây](/docs/v13/user/manual/en/website/articles/website-home-page) để thiết lập trang này làm trang chủ Website của bạn.