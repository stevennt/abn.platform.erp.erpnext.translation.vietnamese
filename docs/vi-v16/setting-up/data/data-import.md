[Home](../home.md) > [Data Import and Settings](../data-import-and-settings.md) > Công cụ Nhập dữ liệu

# Công cụ Nhập dữ liệu

**Công cụ Nhập dữ liệu cho phép bạn nhập các bản ghi từ tệp CSV/Excel.**

Công cụ Nhập dữ liệu là một cách dễ dàng để tải lên (hoặc chỉnh sửa) dữ liệu hàng loạt (đặc biệt là dữ liệu danh mục) vào hệ thống.

Để bắt đầu nhập dữ liệu, hãy đi tới:

> Home > Data Import and Settings > Import Data

Hoặc đi tới DocType bạn muốn nhập và nhấp vào Menu > Import:

<img alt="Start Import" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/data-import/task-menu-import.png">

Trước khi sử dụng Nhập dữ liệu, hãy **đảm bảo** rằng bạn đã chuẩn bị sẵn sàng tất cả dữ liệu của mình.

## 1. Chèn các bản ghi mới

Giả sử bạn muốn nhập danh sách Khách hàng từ hệ thống cũ vào ERPNext. Bước đầu tiên là tải xuống một mẫu để chúng ta có thể nhập dữ liệu.

### 1.1 Tải xuống Mẫu

1. Đi tới Danh sách Khách hàng, nhấp vào Menu > Import. Nhấp vào **New**.
1. Chọn Import Type là Insert New Records.
1. Nhấp vào **Lưu**.
1. Bây giờ, nhấp vào **Download Template**.
1. Khi chèn các bản ghi mới, mẫu sẽ để trống. Nếu bạn đã có một vài Khách hàng trong hệ thống, bạn có thể chọn Export Type là "5 Records" để xem định dạng mà bạn phải nhập dữ liệu vào mẫu.
1. Chọn File Type của mẫu xuất.
1. Chọn các trường mà bạn muốn điền thông tin chi tiết Khách hàng.
1. Nhấp vào **Export**.

![Download Template](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/data-import/download-template.gif)

### 1.2 Nhập dữ liệu vào Mẫu

Mẫu bạn tải xuống sẽ trông giống như thế này:

![Blank Template](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/data-import/blank-template-file.png)

Mở mẫu đã tải xuống trong một ứng dụng bảng tính (như Excel, Numbers, hoặc Libre Office) và nhập dữ liệu bên dưới các tiêu đề cột như sau:

![Customer Template with Data](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/data-import/customer-template-with-data.png)

Bây giờ, hãy lưu mẫu của bạn dưới dạng tệp Excel hoặc Comma Separated Values (CSV).

> Bạn có thể để trống cột ID khi chèn các bản ghi mới.

Khi bạn nhập mẫu này, mỗi hàng sẽ tạo thành một bản ghi Khách hàng trong hệ thống.


### 1.3 Nhập Mẫu

1. Sau khi cập nhật tệp mẫu, hãy quay lại biểu mẫu Data Import và đính kèm tệp bằng cách nhấp vào nút **Attach**.
1. Chọn tệp mẫu và nhấp vào **Upload**.
1. Sau khi tải lên thành công, nhấp vào **Start Import**.

![Upload Template File](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/data-import/upload-template-file.png)

Nếu có bất kỳ lỗi nào trong mẫu của bạn, chúng sẽ được hiển thị trong phần Cảnh báo (Warnings). Các cảnh báo sẽ được phân loại theo Hàng hoặc Cột cùng với số thứ tự của chúng để bạn có thể dễ dàng theo dõi trong mẫu và giải quyết chúng. Bạn phải giải quyết tất cả các cảnh báo trước khi có thể nhập dữ liệu.

![Import Warnings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/data-import/import-warnings.png)

Sau khi bạn đã giải quyết các cảnh báo, hãy nhấp vào **Start Import** một lần nữa để nhập dữ liệu. Sau khi nhập dữ liệu thành công, bạn sẽ thấy nhật ký của từng bản ghi đã được tạo trong phần Nhật ký Nhập (Import Log).

![Import Success](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/data-import/import-success.png)

## 2. Cập nhật các bản ghi hiện có

Giả sử bạn muốn cập nhật dữ liệu Khách hàng hàng loạt trong hệ thống của mình. Bước đầu tiên là tải xuống mẫu có sẵn dữ liệu.

### 2.1 Tải xuống Mẫu

1. Đi tới Danh sách Khách hàng, nhấp vào Menu > Import. Nhấp vào **New**.
1. Chọn Import Type là Update Existing Records.
1. Nhấp vào **Lưu**.
1. Bây giờ, nhấp vào **Download Template**.
1. Khi cập nhật các bản ghi hiện có, bạn phải xuất các bản ghi từ hệ thống với trường ID và các trường mà bạn muốn cập nhật. Bạn có thể chọn All Records hoặc Filtered Records tùy thuộc vào trường hợp của mình.
1. Chọn các trường mà bạn muốn cập nhật cho các bản ghi Khách hàng.
1. Nhấp vào **Export**.

### 2.2 Cập nhật dữ liệu trong Mẫu

Mẫu bạn tải xuống sẽ trông giống như thế này:

![Customer Template for Update](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/data-import/customer-template-for-update.png)

Bây giờ, hãy thay đổi các giá trị trong mẫu của bạn và lưu tệp dưới dạng Excel hoặc CSV.

> Khi xuất các bản ghi để cập nhật chúng, hãy đảm bảo rằng cột ID được xuất và không bị thay đổi. Các giá trị trong cột ID được sử dụng để xác định các bản ghi trong hệ thống. Bạn có thể cập nhật các giá trị ở các cột khác nhưng không được thay đổi cột ID.

### 2.3 Nhập Mẫu

Làm theo các bước trong phần [1.3 Nhập Mẫu](#13-nhập-mẫu) ở trên.

## 3. Nhập các bản ghi con (Child Records)

Dữ liệu trong ERPNext được lưu trữ trong các bảng giống như một bảng tính với các cột và hàng dữ liệu. Mỗi biểu mẫu như Đơn bán hàng có nhiều trường như Khách hàng, Công ty, v.v. Nó cũng có các bảng như bảng Mặt hàng, bảng thuế, v.v. Trong Nhập dữ liệu, tập hợp các trường trong Đơn bán hàng được coi là bảng chính và các hàng bên trong bảng con (bảng Mặt hàng) được coi là bảng con để nhập dữ liệu.

Mỗi biểu mẫu trong ERPNext có thể có nhiều bảng con liên kết với nó. Các bảng con được liên kết với các bảng cha và được triển khai khi có nhiều giá trị cho bất kỳ thuộc tính nào. Ví dụ: một Mặt hàng có thể có nhiều mức giá, một Hóa đơn bán hàng có nhiều Mặt hàng, Thuế, v.v.

Khi bạn xuất một tài liệu có các bảng con, ví dụ: mỗi hàng con sẽ xuất hiện trên một hàng riêng biệt nhưng nó được liên kết với một hàng cha duy nhất. Các giá trị tiếp theo trong các cột cha sẽ được để trống. Bạn phải đảm bảo rằng thứ tự này không bị phá vỡ khi bạn nhập chúng thông qua công cụ Nhập dữ liệu.

![Child Table Export](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/data-import/child-table-export.png)

## 4. Các tùy chọn Nhập

### 4.1 Nhập từ Google Sheets

Bạn cũng có thể nhập dữ liệu từ Google Sheets. Hãy nhập mẫu của bạn vào Google Sheets và nhập dữ liệu. Đảm bảo Google Sheet ở chế độ công khai. Bạn có thể kiểm tra điều này bằng cách mở URL Google Sheets trong cửa sổ trình duyệt.