<!-- add-breadcrumbs -->
# Desktop

**Ngay khi Người dùng đăng nhập vào hệ thống, họ sẽ thấy Màn hình chính, nơi tất cả các Module và Domain được liệt kê dưới dạng các thẻ (cards).**

Các thẻ này là sự thay thế cho các biểu tượng Module trước đây vốn có trong các phiên bản ERPNext trước phiên bản 12.

![New Desktop](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/desktop/desktop.png)

Các thẻ này có thể được phân thành bốn loại, cụ thể là:

- **Modules**: Đây là tất cả các module không phụ thuộc vào lĩnh vực chuyên biệt có sẵn trong ERPNext, dùng chung cho mọi loại hình doanh nghiệp. Các Module như Nhân sự (Human Resources), CRM, Mua hàng (Buying), Bán hàng (Selling), v.v. được xếp vào danh mục này.
- **Domains**: Đây là nơi bạn có thể tìm thấy tất cả các module chuyên biệt theo lĩnh vực như Giáo dục (Education) và Sản xuất (Manufacturing). Bạn có thể tìm hiểu thêm về tất cả các module chuyên biệt theo ngành tại [đây](/docs/v13/user/manual/en#3-industry-specific-modules).
- **Places**: Places là nơi bạn có thể tìm thấy các tính năng không chuyên biệt theo ngành và không cần thiết trong các hoạt động hàng ngày của công ty. Các tính năng như Website, Trang tổng quan (Dashboards) và Marketplace có thể được tìm thấy ở đây.
- **Administration**: Tại đây bạn có thể tìm thấy các module liên quan đến việc thiết lập và quản trị ERPNext của mình.

Các thẻ này cho phép điều hướng tốt hơn với các mục lối tắt trong menu thả xuống. Bạn có thể tùy chỉnh menu thả xuống này để thêm hoặc xóa các liên kết đến các DocType khác nhau của module đó.

![Desktop Dropdown](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/desktop/desktop-dropdown.png)

Bạn cũng có thể sắp xếp lại thứ tự cũng như hiển thị hoặc ẩn các thẻ module này.

![Drag and Drop](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/desktop/drag-and-drop.gif)

## Trang Module

Nhấp vào bất kỳ thẻ module nào sẽ đưa bạn đến trang module. Tại đây, người dùng có thể điều hướng qua tất cả các DocType, báo cáo và cài đặt liên quan đến một module cụ thể.

Ví dụ, đây là giao diện của trang module Kế toán (Accounting).

![Accounts Module](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/desktop/accounts-module-page.png)

### Điều hướng trang

Một số liên kết của các module này có thể được đánh dấu màu xám, việc nhấp vào các liên kết này sẽ không mở ra trang mới. Chúng được đánh dấu như vậy vì có một tài liệu phụ thuộc cần phải được tạo trước. Ví dụ, bạn sẽ cần lập một Hóa đơn bán hàng (Sales Invoice) trước khi truy cập vào sổ nhật ký bán hàng. Di chuột qua bất kỳ liên kết nào trong số này sẽ hiển thị một cửa sổ bật lên hướng dẫn người dùng đến tài liệu phụ thuộc đó.

![Muted Link in Module Page](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/desktop/module-link-hover.png)

Bạn cũng sẽ nhận thấy một chỉ báo màu sắc trước một số liên kết. Các chỉ báo này được sử dụng để thông báo cho người dùng nếu có bất kỳ tài liệu đang mở hoặc khẩn cấp nào cần được xem xét.

![Color Indicators](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/using-erpnext/desktop/color-indicator.png)

* Chỉ báo màu **đỏ** trong ví dụ trên cho biết có các tác vụ đang mở hoặc quá hạn trong danh sách.
* Tương tự, chỉ báo màu **xanh dương** có nghĩa là không có tác vụ nào đang mở.
* Chỉ báo màu **cam** có nghĩa là báo cáo chưa được truy cập hoặc chưa có tài liệu nào được tạo trong DocType tương ứng.

{next}