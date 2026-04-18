<!-- add-breadcrumbs -->
# Khắc phục lỗi Năm tài chính

Khi tạo bất kỳ bút toán nào, hệ thống sẽ kiểm tra xem các ngày (như Ngày hạch toán, Ngày giao dịch, v.v.) có thuộc về Năm tài chính đã chọn hay không. Nếu không, hệ thống sẽ hiển thị thông báo lỗi:

`Date ##-##-#### not in fiscal year`

Bạn có khả năng nhận được thông báo lỗi này nếu Năm tài chính của bạn có thay đổi, nhưng Năm tài chính mới vẫn chưa được thiết lập làm mặc định. Để đảm bảo Năm tài chính mới được tự động cập nhật trong các giao dịch, bạn nên thiết lập dữ liệu danh mục theo hướng dẫn dưới đây.

#### Tạo Năm tài chính mới

Chỉ Người dùng được gán vai trò Quản trị viên hệ thống (System Manager) mới có quyền tạo Năm tài chính mới. Để tạo Năm tài chính mới, hãy đi tới:

`Accounting > Accounting Masters > Fiscal Year`

Đọc [Fiscal Year](../fiscal-year.md) để tìm hiểu thêm.

#### Thiết lập Năm tài chính làm Mặc định

Sau khi Năm tài chính được Lưu, bạn sẽ thấy tùy chọn để thiết lập Năm tài chính đó làm Mặc định.

![Set Fiscal Year as Default](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/set-fiscal-year-as-default.png)

Năm tài chính mặc định cũng sẽ được cập nhật trong phần thiết lập Mặc định toàn cầu (Global Default). Bạn có thể cập nhật Năm tài chính mặc định một cách thủ công từ:

`Settings > Core > Global Default`

![Current Fiscal Year Setting in Global Defaults](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/current-fiscal-year-in-global-defaults.png)

Lưu Mặc định toàn cầu và Tải lại tài khoản ERPNext của bạn. Sau đó, Năm tài chính mặc định sẽ được tự động cập nhật trong các giao dịch của bạn.

Lưu ý: Trong các giao dịch, bạn có thể chọn thủ công Năm tài chính cần thiết từ phần More Info.

{next}