<!-- add-breadcrumbs -->
# Tùy chỉnh Biểu mẫu

**Tùy chỉnh Biểu mẫu (Customize Form) là một công cụ cho phép bạn thực hiện các thay đổi đối với một Loại Biểu mẫu (Form Type) hoặc một Loại Tài liệu (DocType) trên giao diện người dùng.**

Công cụ này cho phép bạn chèn các [Trường tùy chỉnh (Custom Fields)](/docs/v16/user/manual/vi/customize-erpnext/custom-field) theo yêu cầu của mình hoặc tùy chỉnh các thuộc tính của các trường tiêu chuẩn.

Trước khi chúng ta bắt đầu tìm hiểu công cụ Tùy chỉnh Biểu mẫu, hãy [nhấp vào đây](https://frappe.io/docs/v16/user/en/understanding-doctypes) để hiểu về kiến trúc của các biểu mẫu trong ERPNext. Điều này sẽ giúp bạn sử dụng công cụ Tùy chỉnh Biểu mẫu hiệu quả hơn.

Để truy cập Tùy chỉnh Biểu mẫu, hãy đi tới:

> Home > Customization > Customize Form

Bạn cũng có thể đi tới chế độ xem danh sách của bất kỳ DocType nào và chọn Customize từ các tùy chọn Menu.

![Tùy chọn Customize trong Chế độ xem danh sách](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-option-in-list-view.png)


## 1. Cách Tùy chỉnh một Biểu mẫu

1. Nhấp vào Customize Form.
1. Bạn sẽ được chuyển hướng đến một trang nơi bạn được yêu cầu Nhập Loại Biểu mẫu (Enter Form Type).
1. Sau khi bạn nhập Loại Biểu mẫu vào trường này, trang sẽ mở rộng thêm và bạn sẽ có thể thấy nhiều tính năng khác nhau.

  ![Chọn DocType trong Customize Form](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-erpnext-custom-field-from-customize-form.gif)

### 1.1. Các tùy chọn khi đang Tùy chỉnh một Biểu mẫu

1. **Change Label (Thay đổi Nhãn)**: Trường này được lấy thông qua Bản dịch tùy chỉnh (Custom Translation). Bạn có thể thay đổi tên của trường để phù hợp với ngành nghề/ngôn ngữ của mình. Ví dụ: nếu bạn là một doanh nghiệp dịch vụ và bạn muốn thay đổi Nhãn từ 'Customer' thành 'Consumer', điều đó có thể được thực hiện thông qua [Custom Translation](/docs/v16/user/manual/vi/setting-up/print/custom-translations) và thay đổi đó sẽ được phản ánh tại đây.

  ![Thay đổi Nhãn](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-customize-form-label.png)

1. **Title Field (Trường Tiêu đề)**: Trường này có thể được sử dụng để tạo tiêu đề khi xem các danh sách. Bất kỳ trường loại "Data" nào cũng có thể được thiết lập làm Trường Tiêu đề khi xem các biểu mẫu trong chế độ xem danh sách. Ví dụ: nếu bạn muốn xem danh sách tất cả nhân viên của mình với trường Tiêu đề là 'Mã nhân viên' thay vì Tên nhân viên, điều đó có thể được cấu hình tại đây. Kiểm tra bài viết của chúng tôi về [Document title](/docs/v16/user/manual/vi/customize-erpnext/document-title) để biết thêm thông tin.

  *Tìm hiểu thêm về các loại trường [tại đây](/docs/v16/user/manual/vi/customize-erpnext/articles/field-types.html).*

1. **Default Print Format (Mẫu in mặc định)**: Đối với một DocType duy nhất, có thể có nhiều Mẫu in (Print Formats). Tại đây bạn có thể chọn Mẫu in mặc định cho DocType đã chọn. Ví dụ: một công ty có thể có các Tiêu đề thư (Letter Heads) khác nhau cho các mục đích khác nhau, điều này có thể được cấu hình thông qua các Mẫu in. Tuy nhiên, bạn có thể chọn hai Mẫu in mặc định khác nhau cho Đơn bán hàng (SO) và Thư bổ nhiệm (Appointment Letter). Kiểm tra [Custom Print Formats](/docs/v16/user/manual/vi/customize-erpnext/print-format) để biết thêm thông tin.
1. **Image Field (Trường Hình ảnh)**: Bạn có thể chọn một trường "Attach Image" cho Trường Hình ảnh của mình. Đây sẽ là Hình ảnh đại diện cho DocType cụ thể đó. Ví dụ: 'Trường Hình ảnh' cho một Nhân viên có thể là ảnh chân dung hoặc ảnh chụp thẻ ID của họ; điều này có thể được cấu hình tại đây.

  ![Trường Hình ảnh trong DocType](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-form-image-field.png)

1. **Max Attachments (Số lượng tệp đính kèm tối đa)**: Bạn có thể nhập số lượng tệp đính kèm tối đa có thể được thêm vào DocType này.
1. **Search Fields (Trường tìm kiếm)**: Khi tạo bất kỳ DocType nào, bạn có thể muốn liên kết một trường cụ thể với một DocType khác. Để thuận tiện cho việc lựa chọn, bạn cũng có thể đảm bảo rằng mình có thể thấy giá trị của một trường khác của DocType kia trong kết quả tìm kiếm. Để biết thêm thông tin [nhấp vào đây](/docs/v16/user/manual/vi/customize-erpnext/articles/search-record-by-specific-field).

1. **Sort Field (Trường sắp xếp)**: Các bản ghi trong Danh sách của bất kỳ DocType nào được tạo dựa trên Trường mà bạn thiết lập tại Trường sắp xếp ở đây. Ví dụ: đối với Mặt hàng (Item), nếu bạn muốn danh sách của mình được tạo theo Tên mặt hàng, bạn có thể cấu hình điều đó tại đây.

  ![Trường sắp xếp](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-sort-field.png)

1. **Sort Order (Thứ tự sắp xếp)**: Bạn có thể chọn xem bạn muốn Sắp xếp theo Thứ tự Tăng dần hay Thứ tự Giảm dần. Để hiểu rõ hơn về Trường sắp xếp và Thứ tự sắp xếp, hãy xem [Customizing Sorting Order in the List View](/docs/v16/user/manual/vi/customize-erpnext/articles/customizing-sorting-order-in-the-list-view).
1. **Default Email Template (Mẫu Email mặc định)**: Đối với một DocType duy nhất, có thể có nhiều [Mẫu Email (Email Templates)](/docs/v16/user/manual/vi/setting-up/email/email-template). Tại đây bạn có thể thiết lập Mẫu Email mặc định cho DocType đã chọn. Ví dụ: bạn có thể thiết lập một Mẫu Email mặc định khác cho Đơn bán hàng (SO) và Thư bổ nhiệm (Appointment Letter).

### 1.3. Các thuộc tính khác

* **Hide Copy (Ẩn bản sao)**: Khi hộp này được tích, nó sẽ hạn chế Người dùng tạo một 'Bản sao' của một Biểu mẫu cụ thể.
* **Is Table (Là bảng)**: Tùy chọn này chỉ khả dụng khi đang tùy chỉnh các Biểu mẫu hiện diện trong các bảng (table forms) trong hệ thống. Ví dụ: nếu bạn đang tạo một Bảng Mặt hàng để thêm vào một Biểu mẫu tùy chỉnh, bạn có thể bật tùy chọn này. Xem [Child Table](/docs/v16/user/manual/vi/customize-erpnext/articles/customizing-data-visibility-in-child-table) để biết thêm thông tin.
* **Quick Entry (Nhập nhanh)**: Cho phép người dùng tạo bản ghi mới thông qua một cửa sổ pop-up nhỏ thay vì phải mở toàn bộ trang biểu mẫu.