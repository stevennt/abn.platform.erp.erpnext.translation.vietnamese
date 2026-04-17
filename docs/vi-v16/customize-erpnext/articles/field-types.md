<!-- add-breadcrumbs -->
# Loại trường

Dưới đây là các loại trường bạn có thể xác định khi tạo mới hoặc khi sửa đổi các trường tiêu chuẩn.

#### Link

Trường Link được kết nối với một danh mục chính khác để lấy dữ liệu từ đó. Ví dụ, trong danh mục Báo giá, Khách hàng là một trường Link. Để biết thêm chi tiết, [nhấp vào đây](../user/manual/customize-erpnext/articles/creating-custom-link-field).

#### Dynamic Link

Trường Dynamic Link là trường có thể tìm kiếm và giữ giá trị của bất kỳ tài liệu/DocType nào. [Nhấp vào đây](../user/manual/customize-erpnext/articles/dynamic-link-fields) để tìm hiểu cách thức hoạt động của trường Dynamic Link.

#### Check

Trường này sẽ cho phép bạn có một ô đánh dấu (checkbox) tại đây.

![Check Field TYpe](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-check.png)

#### Select

Select sẽ là một trường danh sách thả xuống. Bạn có thể thêm nhiều kết quả trong trường Option, phân tách bằng dòng mới.

![Select Field Type](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-select.png)

#### Table

Table là một loại trường Link hiển thị một DocType khác ngay trong biểu mẫu hiện tại. Ví dụ, Bảng Mặt hàng trong Đơn bán hàng là một trường Table, được liên kết với DocType Mặt hàng Đơn bán hàng.

![Table Field Type](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-table.png)

#### Attach

Trường Attach cho phép bạn duyệt tìm một tệp từ Trình quản lý tệp và đính kèm tệp đó vào đây.

![Attach Field Type](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-attach.png)

#### Attach Image

Attach Image là trường mà bạn sẽ được phép đính kèm các hình ảnh định dạng jpeg, png, v.v. Hình ảnh này sẽ trở thành hình ảnh đại diện cho DocType cụ thể đó. Ví dụ, nếu bạn muốn có hình ảnh của một Mặt hàng trong DocType của nó, bạn có thể chọn trường của mình là trường Attach Image.

![Field Type Image](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-image.png)

#### Text Editor

Text Editor là một trường văn bản. Nó có các tùy chọn định dạng văn bản. Trong ERPNext, trường này thường được sử dụng để định nghĩa các Điều khoản và Điều kiện.

![Field Type Text Editor](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-text-editor.png)

#### Date

Trường này sẽ cho phép bạn nhập Ngày vào trường này.

![Field Type Date](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-date.png)

#### Date and Time

Trường này sẽ cung cấp cho bạn bộ chọn ngày và giờ. Ngày và giờ hiện tại (theo máy tính của bạn) được thiết lập theo mặc định.

![Field Type Date and Time](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-date-and-time.png)

#### Barcode

Trong trường này, bạn có thể chỉ định trường là Barcode để cho phép nhập số Mã vạch. Sau khi bạn thực hiện việc đó, Mã vạch sẽ tự động được tạo dựa trên số đó.

![Field Type Barcode](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-barcode.png)

#### Button

Loại trường này sẽ là một nút hành động, chẳng hạn như Lưu, Xác nhận, v.v.

![Field Type Button](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-button.png)

#### Code

Nếu Loại trường được chọn là code, bạn sẽ có thể nhập một đoạn Mã vào trường.

![Field Type Code](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-code.png)

#### Color

Bạn sẽ có tùy chọn chỉ định màu sắc cho Biểu mẫu này.

![Field Type Colour](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-colour.png)

#### Column Break

Vì ERPNext có nhiều bố cục cột, bằng cách sử dụng Column Breaks, bạn có thể chia một tập hợp các trường thành tối đa hai cột.

![Field Type Column Break](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-column-break.png)

#### Currency

Trường Currency giữ giá trị số, như Giá Mặt hàng, Số tiền, v.v. Trường Currency có thể có giá trị lên đến sáu chữ số thập phân. Ngoài ra, bạn có thể hiển thị ký hiệu tiền tệ cho trường Currency.

![Field Type Currency](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-currency.png)

#### Data

Trường data sẽ là một trường văn bản đơn giản. Nó cho phép bạn nhập giá trị lên đến 140 ký tự, khiến đây trở thành loại trường phổ biến nhất. Để bật các xác thực cho đầu vào Email, Tên hoặc Số điện thoại, hãy đặt tùy chọn thành "Email", "Name", "Phone" trong Settings > DocType.

![Field Type Data](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-data.png)

#### Float

Trường Float mang giá trị số, lên đến chín chữ số thập phân. Độ chính xác cho trường float được thiết lập thông qua [Thiết lập độ chính xác](../user/manual/customize-erpnext/articles/set-precision)

> Setup > Settings > System Settings

Thiết lập này sẽ được áp dụng cho tất cả các trường float.

![Field Type Float](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-float.png)

#### Geolocation

Sử dụng trường Geolocation để lưu trữ GeoJSON <a href="https://tools.ietf.org/html/rfc7946#section-3.3">feature_collection</a>. Lưu trữ các đa giác, đường thẳng và điểm. Về mặt nội bộ, nó sử dụng các thuộc tính tùy chỉnh sau để xác định một hình tròn.

Đọc [Trường Geolocation](../user/manual/customize-erpnext/articles/geolocation-field) để hiểu thêm.

![Field Type Geolocation](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-geolocation.png)

#### HTML

Bạn có thể chọn trường là trường HTML khi bạn muốn dữ liệu được nhập dưới định dạng HTML.

![Field Type HTML](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-html.png)

#### Image

Trường Image sẽ hiển thị một tệp hình ảnh được chọn trong một trường đính kèm khác.

Đối với trường Image, trong phần Option (trong Doctype), cần cung cấp tên của trường nơi tệp hình ảnh được đính kèm. Bằng cách tham chiếu đến giá trị trong trường đó, hình ảnh sẽ được hiển thị trong trường Image.

![Field Type Image](https://docs.erpnext.com/docs/v16/assets/img/customize/field-type-image.png)