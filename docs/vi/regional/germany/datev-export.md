<!-- add-breadcrumbs -->

Tất cả các **Bút toán sổ cái** có thể được xuất sang định dạng DATEV để gửi cho cố vấn thuế của bạn.

## Định dạng DATEV

DATEV eG của Đức là một hợp tác xã đã đăng ký của các ngành nghề thuế, kế toán và pháp lý. Định dạng DATEV là một giao diện tệp dựa trên CSV để nhập dữ liệu vào phần mềm DATEV Accounting. Tài liệu hướng dẫn về giao diện này có sẵn tại cổng thông tin dành cho nhà phát triển của DATEV:

- [DATEV format v7.0](https://developer.datev.de/portal/system/files/files/book/datev_format_v7.0.zip).

## Điều kiện tiên quyết

Để sử dụng tính năng Xuất DATEV, trước tiên bạn cần phải tạo:

- [Cài đặt DATEV](datev-settings.md)

## Bộ lọc

Trong phần bộ lọc, bạn có thể chọn công ty mà bạn muốn xuất các **Bút toán sổ cái**. Bạn cũng có thể thiết lập khung thời gian cho việc xuất dữ liệu. Thông thường, đây sẽ là tháng gần nhất.

![DATEV Export Filters](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/germany/datev-export-filters.png)

## Menu

Từ menu, bạn có thể mở [Cài đặt DATEV](datev-settings.md) hoặc tải xuống tệp xuất. Tệp xuất là một tệp nén ZIP chứa dữ liệu giao dịch từ bản xem trước cũng như dữ liệu danh mục (**Khách hàng**, **Nhà cung cấp**, **Tài khoản**).

![DATEV Export Menu](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/germany/datev-export-menu.png)

## Dữ liệu được xuất

Hiện tại, bạn có thể xuất các **Bút toán sổ cái** theo cách mà ERPNext tạo ra chúng. Ví dụ, việc hạch toán một **Hóa đơn bán hàng** sẽ tạo ra ba **Bút toán sổ cái**:

| Số tiền Nợ | Số tiền Có | Tài khoản | Đối ứng         |
|--------------|---------------|---------|-----------------|
| Số tiền tổng |               | Phải thu khách hàng | Tài khoản doanh thu |
|              | Số tiền thuế    | Thuế     | Khách hàng        |
|              | Số tiền ròng    | Doanh thu   | Khách hàng        |

Tuy nhiên, trong ERPNext, phía bên phải không nhất thiết phải là một **Tài khoản**. Nó cũng có thể là nhiều tài khoản, một **Khách hàng** hoặc một **Nhà cung cấp**. Do đó, chúng tôi sử dụng một tài khoản đối ứng tạm thời có thể được chỉ định trong [Cài đặt DATEV](datev-settings.md). Tất cả các Bút toán sổ cái đều được hạch toán đối ứng với tài khoản này. Các dòng trong bản Xuất DATEV sẽ trông giống như thế này:

| Số tiền       | Nợ hoặc Có | Tài khoản | Tài khoản đối ứng |
|--------------|-----------------|---------|-----------------|
| Số tiền tổng | Nợ           | Phải thu khách hàng | Tạm thời       |
| Số tiền thuế   | Có          | Thuế     | Tạm thời       |
| Số tiền ròng   | Có          | Doanh thu   | Tạm thời       |

> Vui lòng tham khảo ý kiến cố vấn thuế của bạn về việc liệu bạn có thể sử dụng dữ liệu này hay không và sử dụng như thế nào.