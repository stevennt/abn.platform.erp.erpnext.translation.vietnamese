<!-- add-breadcrumbs -->

# Sao chép và Dán nhiều bản ghi từ Excel

**Nếu bạn có một chuỗi các bản ghi được lưu trong một bảng tính excel cần được ánh xạ vào một Bảng con (Child Table) trong ERPNext, bạn có thể thực hiện việc đó bằng tính năng này.**

Giả sử, bạn có một danh sách các mặt hàng được lưu trong một bảng tính Excel, và bạn cần sao chép danh sách đó vào Bảng con 'Items' trong Đơn bán hàng.

## Các bước để Sao chép và Dán các bản ghi từ excel

* Chuẩn bị dữ liệu nguồn trong Excel hoặc trình soạn thảo văn bản với mỗi cột được phân tách bằng một dấu tab.

 ![Copy Pasting](https://docs.erpnext.com/docs/v13/assets/img/using-erpnext/using-copy-paste-1.png)

* Kéo chuột để chọn các bản ghi, sau đó nhấp vào nút menu sao chép hoặc nhấn Ctrl + C (Cmd + C) để:

 Trường hợp 1. Cột đầu tiên của bảng tính excel sẽ là tiêu đề cột và nội dung trong đó.

 Trường hợp 2. Khi không có tiêu đề cột được xác định, dữ liệu sẽ được ánh xạ vào các cột đang hiển thị.

 ![Copy Pasting](https://docs.erpnext.com/docs/v13/assets/img/using-erpnext/using-copy-paste-4.png)

* Đặt con trỏ vào trường nhập liệu mục tiêu của bảng con, và dán dữ liệu vào. Khác với tính năng nhập liệu thông qua tải tệp lên, tính năng sao chép & dán này sẽ tự động kích hoạt các sự kiện thay đổi trường (field change events).

 ![Copy Pasting](https://docs.erpnext.com/docs/v13/assets/img/using-erpnext/using-copy-paste-3.gif)

Để đảm bảo hiệu suất, bạn chỉ nên dán không quá 100 bản ghi trong mỗi lần thực hiện.

{next}