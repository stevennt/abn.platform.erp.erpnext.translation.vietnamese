<!-- add-breadcrumbs -->
# Mẫu in

**Với Mẫu in, bạn có thể thiết lập giao diện của các DocType khi in.**

Mọi giao dịch đều có một Mẫu in mặc định được gọi là 'Standard'. Bạn có thể thay đổi các Mẫu in bằng cách:

* Sử dụng biểu mẫu Mẫu in
* Sử dụng kịch bản Jinja/JS trong Mẫu in
* Sử dụng [Print Format Builder](print-format-builder.md) để tạo các mẫu in bằng giao diện người dùng (UI)
* Sử dụng Customize Form để ẩn/hiện các trường

Để truy cập Mẫu in, hãy đi tới:

> Home > Settings > Print Format

## 1. Cách tạo một Mẫu in
1. Đi tới Danh sách Mẫu in (Print Format List), nhấn vào New.
1. Nhập tên và chọn DocType mà Mẫu in này sẽ được sử dụng.
1. Module áp dụng sẽ được tự động lựa chọn.

  ![Print Format menu](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/print-format-menu.png)

1. Lưu.

Trong phần Cài đặt Kiểu dáng (Style Settings), có các tùy chọn để thay đổi các thiết lập về kiểu dáng. Với các tùy chọn này, bạn có thể thay đổi phông chữ, căn chỉnh các nhãn sang trái hoặc phải, thêm tiêu đề cho các phần, v.v.

Để thiết kế Mẫu in bằng Jinja/JS tùy chỉnh, hãy nhấp vào Custom Format. Nếu bạn chọn tùy chọn này, sẽ có một ô đánh dấu cho việc in thô (raw printing). Để biết thêm về in thô, [nhấp vào đây](raw-printing.md).

Nếu chế độ nhà phát triển (developer mode) được bật, bạn có thể chọn Standard là "yes" để đóng góp một mẫu in như một mẫu in tiêu chuẩn (thiết lập sẵn) trong hệ thống.

## 1.1 Sử dụng Customize form để thay đổi các mục trong Mẫu in
Các trường trong giao dịch và các bảng con của chúng có thể được ẩn/hiện bằng cách sử dụng Customize Form.
Ví dụ, nếu bạn muốn ẩn 'Item Code' khi in một Báo giá (Quotation), hãy nhấp vào biểu tượng in để vào màn hình in.

Đi tới Menu > Customize, chọn Quotation Item trong trường 'Enter Form Type'.
![Print Format Customize](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/print-format-customize1.png)

Để biết thêm, hãy truy cập trang [Customize Print Format](../../customize-erpnext/print-format.md).

Trong bảng các trường (fields table), mở rộng dòng 'Item Code', cuộn xuống và đánh dấu vào ô 'Print Hide'.
![Print Format Print Hide](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/print-format-customize2.png)


Một Mẫu in mới được tạo có thể được chọn trên màn hình in của một giao dịch. Từ đó, bạn có thể xem giao diện của nó và tiến hành in.
![Selecting a Print Format](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/print-format-selection.png)

## 2. Video
<div class="embed-container">
  <iframe src="https://www.youtube.com/embed/cKZHcx1znMc?start=82&rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
  </iframe>
</div>

### 3. Các chủ đề liên quan
1. [Print Style](print-style.md)
1. [Print Headings](print-headings.md)
1. [Letter Head](letter-head.md)
1. [Cheque Print Template](cheque-print-template.md)
1. [Disabling Line Breaks in Print Format Sections](../articles/print-format-sections.md)