<!-- add-breadcrumbs -->
# Tự động tạo tệp JSON cho e-Way Bill từ Hóa đơn bán hàng

Theo quy định về GST, đơn vị vận chuyển nên mang theo e-Way Bill khi di chuyển hàng hóa từ nơi này sang nơi khác khi đáp ứng các điều kiện nhất định.

Để giúp đẩy nhanh quá trình tạo e-Way Bill, giờ đây bạn có thể tự động tạo một tệp JSON từ trang ERPNext của mình, tệp này có thể được sử dụng để tạo nhanh e-Way Bill trên <a href="https://ewaybillgst.gov.in">Hệ thống GST e-Way Bill</a>.


## Điều kiện tiên quyết

- Các Tài khoản GST phải được thiết lập trong DocType GST Settings.

- Các trường bắt buộc để tạo e-Way Bill hợp lệ phải được nhập trong Hóa đơn bán hàng. Để xác định các trường bắt buộc và biết thêm thông tin, bạn có thể tham khảo <a href="https://docs.ewaybillgst.gov.in/html/formatdownloadnew.html">lược đồ JSON</a>.

## Hướng dẫn

### Trên trang ERPNext của bạn:

1. Sau khi nhập các dữ liệu bắt buộc, hãy Xác nhận (Submit) Hóa đơn bán hàng.

1. Bây giờ bạn sẽ thấy một nút có nhãn **e-Way Bill JSON** dưới menu **Make** ở góc trên bên phải.

	![Create E-way Bill JSON](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/create-e-way-bill-json.png)

1. Nếu bạn muốn tạo tệp JSON cho nhiều hóa đơn, bạn có thể chọn các hóa đơn liên quan từ Danh sách Hóa đơn bán hàng và tìm nút **Generate e-Way Bill JSON** dưới menu **Actions** ở góc trên bên phải.

	![Create Multiple E-way Bill JSON](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/create-multiple-e-way-bill-json.png)

1. Khi nhấp vào nút này, dữ liệu của bạn sẽ được xác thực theo <a href="https://docs.ewaybillgst.gov.in/html/formatdownloadnew.html">lược đồ JSON</a> và tệp JSON được tự động tạo sẽ được tải xuống thiết bị của bạn.

### Trên Hệ thống GST e-Way Bill:

1. Đăng nhập vào <a href="https://ewaybillgst.gov.in">Hệ thống GST e-Way Bill</a> bằng thông tin đăng nhập của bạn.

1. Trong phần **e-Waybill** ở thanh bên trái, hãy nhấp vào **Generate Bulk**.

1. Chọn và tải lên tệp đã được tự động tạo. Bạn có thể yên tâm bỏ qua bất kỳ cảnh báo nào liên quan đến Số chứng từ (Document No.) do Hệ thống e-Way Bill đưa ra.

	<img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/ewb_warning.png">
	![](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/)

1. Hệ thống e-Way Bill hiện sẽ hiển thị mô tả về (các) e-Way Bill mà bạn đang cố gắng tạo. Nếu mọi thứ trông có vẻ ổn và không gặp lỗi nào, bạn có thể tiến hành tạo (các) e-Way Bill bằng cách nhấp vào nút **Generate**.

1. Bây giờ bạn sẽ có thể xem Số e-Way Bill được tạo cho (các) Hóa đơn bán hàng của mình. Vui lòng ghi lại số này vì nó sẽ hữu ích sau này.

1. Để in (các) e-Way Bill, hãy quay lại Trang tổng quan Hệ thống e-Way Bill bằng cách nhấp vào biểu tượng <i class='fa fa-home'></i> và chọn **Print EWB** trong phần **e-Waybill**.


Bây giờ bạn có thể nhập Số e-Way Bill vào Hóa đơn bán hàng của mình để tham chiếu sau này.

![E-way Bill Number in Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/e-way-bill-number-in-invoice.png)

{next}