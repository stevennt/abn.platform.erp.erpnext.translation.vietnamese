<!-- add-breadcrumbs -->
# Bản dịch tùy chỉnh

**Với Bản dịch tùy chỉnh, người dùng có thể in các chứng từ của Khách hàng và Nhà cung cấp bằng ngôn ngữ địa phương của họ.**

Ví dụ, nếu bạn có các khách hàng từ Đức và Pháp muốn nhận Báo giá bằng tiếng Đức và tiếng Pháp, điều này hoàn toàn có thể thực hiện được bằng cách sử dụng Bản dịch tùy chỉnh.

## 1. Thiết lập Ngôn ngữ

Trong danh mục Khách hàng, hãy chọn Ngôn ngữ mặc định. Giả sử, ngôn ngữ mặc định cho Khách hàng là **Spanish**.

![Set Customer Language](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/set-customer-language.png)

Tương tự, bạn cũng có thể thiết lập ngôn ngữ mặc định trong danh mục Nhà cung cấp.

### 1.1 Xem trước bản in bằng ngôn ngữ của Đối tác

Trong phần Xem trước bản in của một giao dịch, các giá trị sẽ được dịch sang ngôn ngữ của đối tác.

Xem trước bản in Báo giá của Khách hàng bằng ngôn ngữ mặc định của khách hàng.

![Invoice in Customer Language](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/invoice-in-customer-language.png)

Xem trước bản in Báo giá của Nhà cung cấp bằng ngôn ngữ mặc định của nhà cung cấp.

### 1.2 Thay đổi ngôn ngữ in trong bản xem trước

Người dùng có tùy chọn để chọn một ngôn ngữ thay thế trong chế độ xem bản in.

![Select Language in Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/select-language-in-invoice.png)

## 2. Bản dịch tùy chỉnh

Người dùng có thể thiết lập các bản dịch tùy chỉnh của mình bằng biểu mẫu Bản dịch tùy chỉnh. Ví dụ, nếu một người dùng muốn thiết lập mô tả của một sản phẩm bằng ngôn ngữ của khách hàng (tiếng Tây Ban Nha). Để làm điều đó, hãy tạo một bản dịch mới với ngôn ngữ là Spanish, nhập dữ liệu nguồn và thông tin đã dịch.

> Home > Customization > Other > Custom Translations > New

![Translation](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/translation.png)

Bản dịch sẽ được áp dụng khi người dùng chọn ngôn ngữ là Spanish trong phần xem trước bản in của Báo giá nhà cung cấp. Lưu ý rằng không có bản dịch nào được áp dụng cho mô tả của mặt hàng thứ hai vì nó chưa được tạo trong danh sách Bản dịch.

![Translation in Transaction](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/translation-in-transaction.png)

### 3. Các chủ đề liên quan
1. [Address Template](address-template.md)
1. [Quotation](../../selling/quotation.md)
1. [Sales Order](../../selling/sales-order.md)

{next}