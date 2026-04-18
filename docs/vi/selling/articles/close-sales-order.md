<!-- add-breadcrumbs -->
#Đóng Đơn bán hàng

Trong các Đơn bán hàng đã được Xác nhận, bạn sẽ thấy tùy chọn **Stop** (Dừng). Việc dừng Đơn bán hàng sẽ hạn chế người dùng tạo Phiếu giao hàng và Hóa đơn bán hàng dựa trên đơn hàng đó.

![Close Option in Sales Order](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/close-option-in-sales-order.png)

####Tình huống

Một đơn hàng được nhận cho mười Tuabin gió. Đơn bán hàng cũng được tạo cho mười đơn vị. Do thiếu hụt hàng tồn kho, chỉ có bảy đơn vị được giao cho khách hàng. Ba đơn vị còn lại sẽ được giao sớm. Khách hàng thông báo rằng họ không cần giao các mặt hàng còn lại nữa, vì họ đã mua từ nhà cung cấp khác.

Trong trường hợp này, Phiếu giao hàng và Hóa đơn bán hàng sẽ chỉ được tạo cho bảy đơn vị. Và Đơn bán hàng nên được thiết lập ở trạng thái đã dừng (stopped).

![Closed Sales Order](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/closed-sales-order.png)

Khi Đơn bán hàng được thiết lập là đã dừng, bạn sẽ không thấy số lượng còn lại (trong trường hợp này là ba) hiển thị trong các báo cáo Chờ giao (Pending to Deliver) và Chờ xuất hóa đơn (Pending to Invoice). Để thực hiện các giao dịch tiếp theo dựa trên Đơn bán hàng đã dừng, trước tiên bạn phải chọn Unstop (Bỏ dừng) nó.

Bạn cũng sẽ tìm thấy chức năng tương tự trong Đơn mua hàng.

{next}

<!-- markdown -->