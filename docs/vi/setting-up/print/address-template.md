<!-- add-breadcrumbs -->
# Mẫu địa chỉ

**Mẫu địa chỉ có thể lưu trữ các định dạng địa chỉ khác nhau dựa trên khu vực.**

Mỗi khu vực có cách xác định địa chỉ riêng. Để quản lý nhiều định dạng địa chỉ cho các Chứng từ của bạn (như Báo giá, Hóa đơn mua hàng, v.v.), bạn có thể tạo các **Mẫu địa chỉ** theo từng quốc gia.

Để truy cập mẫu địa chỉ, hãy đi tới:
> Trang chủ > Cài đặt > Mẫu địa chỉ

Một Mẫu địa chỉ mặc định sẽ được tạo khi bạn thiết lập hệ thống. Bạn có thể chỉnh sửa mẫu đó hoặc tạo một mẫu mới. Mẫu mặc định này sẽ được áp dụng cho tất cả các quốc gia không có mẫu cụ thể.

Hãy xem xét trường hợp một khách hàng từ Hoa Kỳ, nơi 'County' (Hạt) là một phần của địa chỉ. Nếu bạn thiết lập 'county' trong mẫu địa chỉ cho Hoa Kỳ, thì nó sẽ hiển thị trong trường địa chỉ và do đó hiển thị trong bản xem trước bản in. Các trường như mã PIN có thể được đổi thành hiển thị là mã ZIP và các trường như county có thể được thêm vào bằng cách sử dụng Mẫu địa chỉ.

> Mẫu địa chỉ sẽ kiểm tra trường 'Country' (Quốc gia) trong danh mục địa chỉ chính để áp dụng các mẫu địa chỉ khác nhau cho các giao dịch.

## 1. Cách tạo Mẫu địa chỉ
1. Đi tới danh sách Mẫu địa chỉ, nhấn vào Mới.
1. Chọn một quốc gia.
1. Thay đổi CSS và Jinja nếu cần.
1. Lưu.

### 1.1 Jinja Templating
Công cụ tạo mẫu dựa trên HTML và hệ thống [Jinja Templating](http://jinja.pocoo.org/docs/v13/templates/). Tất cả các trường (bao gồm cả Trường tùy chỉnh) sẽ có sẵn để tạo mẫu.

Đây là mẫu Jinja mặc định:

    {% raw %}{{ address_line1 }}<br>
    {% if address_line2 %}{{ address_line2 }}<br>{% endif -%}
    {{ city }}<br>
    {% if state %}{{ state }}<br>{% endif -%}
    {% if pincode %}PIN:  {{ pincode }}<br>{% endif -%}
    {{ country }}<br>
    {% if phone %}Phone: {{ phone }}<br>{% endif -%}
    {% if fax %}Fax: {{ fax }}<br>{% endif -%}
    {% if email_id %}Email: {{ email_id }}<br>{% endif -%}{% endraw %}

Đây là một ví dụ:

<img class="screenshot" alt="Print Heading" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/address-format.png">

### 2. Các chủ đề liên quan
1. [Mẫu Điều khoản và Điều kiện](/docs/v13/user/manual/en/setting-up/print/terms-and-conditions)
1. [Mẫu in Séc](/docs/v13/user/manual/en/setting-up/print/cheque-print-template)