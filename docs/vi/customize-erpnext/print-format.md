<!-- add-breadcrumbs -->
# Tùy chỉnh Mẫu in

**Mẫu in là bố cục được tạo ra khi bạn muốn In hoặc gửi Email một giao dịch.**

Tính năng này rất hữu ích cho tất cả các giao dịch trong ERPNext như các giao dịch bán hàng và mua hàng, tài liệu nhân sự và nhiều hơn nữa.

Trong ERPNext, có ba loại Mẫu in, cụ thể là: Mẫu in Tiêu chuẩn, Mẫu in Tùy chỉnh và Mẫu in HTML.

## Mẫu in Tiêu chuẩn

Mỗi DocType có thể in được trong ERPNext sẽ có Mẫu in Tiêu chuẩn riêng được tạo bởi Frappe Framework. Vị trí các trường trong Mẫu in Tiêu chuẩn sẽ phụ thuộc vào vị trí của các trường tương ứng trong tài liệu.

![Standard Print Format](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-standard-print-format.png)

Mọi thay đổi đối với Mẫu in Tiêu chuẩn đều phải được thực hiện bằng cách sử dụng Customize Form. Bạn cũng có thể xem thêm về [thêm các trường vào Mẫu in](/docs/v13/user/manual/en/customize-erpnext/articles/making-fields-visible-in-print-format).

## Mẫu in Tùy chỉnh

Bạn cũng có thể tạo các Mẫu in tùy chỉnh của riêng mình bằng cách sử dụng công cụ gọi là [Print Format Builder](/docs/v13/user/manual/en/setting-up/print/print-format-builder). Công cụ này sẽ giúp bạn tạo một Mẫu in Tùy chỉnh đơn giản bằng cách kéo và thả các trường vào định dạng theo ý muốn của bạn.

![Customize Print Format](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-print-format.gif)

Để tạo các Mẫu in Tùy chỉnh, ERPNext đi kèm với một số mẫu được định nghĩa sẵn với ba phong cách, cụ thể là: Hiện đại (Modern), Đơn sắc (Monochrome) và Cổ điển (Classic).

Để tạo các phiên bản của bạn, hãy mở một mẫu có sẵn từ:

> Build > Views > Print Format

## Cài đặt In

Để chỉnh sửa/cập nhật cài đặt in và PDF của bạn, hãy đi tới:

> Settings > Print Settings

![Print Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/print-settings.png)

## Mẫu in HTML

Để tạo một Mẫu in HTML, bạn sẽ cần một số kiến thức về HTML, CSS và Python. Dưới đây là một ví dụ về cách một Mẫu in có thể được thiết kế với định dạng rất đặc thù.

![HTML Print Format](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/customize/customize-custom-print-format-1.png)

Các Mẫu in được cung cấp ở phía máy chủ (server-side) bằng cách sử dụng [Ngôn ngữ Template Jinja](http://jinja.pocoo.org/docs/v13/templates/). Tất cả các biểu mẫu đều có quyền truy cập vào đối tượng `doc`, đối tượng này chứa thông tin về tài liệu đang được định dạng. Bạn cũng có thể truy cập các tiện ích phổ biến thông qua module `frappe`. Để nhận được sự hỗ trợ khi tạo mẫu in dựa trên HTML, bạn có thể tham khảo [Diễn đàn Cộng đồng ERPNext](https://discuss.erpnext.com/), hoặc bắt đầu một bài đăng mới cho câu hỏi của bạn.

Để tạo kiểu (styling), [Bootstrap CSS Framework](http://getbootstrap.com/) được cung cấp và bạn có thể sử dụng đầy đủ các lớp (classes) của nó.

#### Tham khảo

1. [Jinja Templating Language: Reference](http://jinja.pocoo.org/docs/v13/templates/)
2. [Bootstrap CSS Framework](http://getbootstrap.com/)



#### Ví dụ

        {% raw %}<h3>{{ doc.select_print_heading or "Invoice" }}</h3>
        <div class="row">
            <div class="col-md-3 text-right">Customer Name</div>
            <div class="col-md-9">{{ doc.customer_name }}</div>
        </div>
        <div class="row">
            <div class="col-md-3 text-right">Date</div>
            <div class="col-md-9">{{ doc.get_formatted("invoice_date") }}</div>
        </div>
        <table class="table table-bordered">
            <tbody>
                <tr>
                    <th>Sr</th>
                    <th>Item Name</th>
                    <th>Description</th>
                    <th class="text-right">Qty</th>
                    <th class="text-right">Rate</th>
                    <th class="text-right">Amount</th>
                </tr>
                {%- for row in doc.items -%}
                <tr>
                    <td style="width: 3%;">{{ row.idx }}</td>
                    <td style="width: 20%;">
                        {{ row.item_name }}
                        {% if row.item_code != row.item_name -%}
                        <br>Item Code: {{ row.item_code}}
                        {%- endif %}
                    </td>
                    <td style="width: 37%;">
                        <div style="border: 0px;">{{ row.description }}</div></td>
                    <td style="width: 10%; text-align: right;">{{ row.qty }} {{ row.uom or row.stock_uom }}</td>
                    <td style="width: 15%; text-align: right;">{{
                        row.get_formatted("rate", doc) }}</td>
                    <td style="width: 15%; text-align: right;">{{
                        row.get_formatted("amount", doc) }}</td>
                </tr>
                {%- endfor -%}
            </tbody>
        </table>{% endraw %}

## Ghi chú

1. Để lấy các giá trị đã được định dạng ngày tháng và tiền tệ, hãy sử dụng `doc.get_formatted("fieldname")`
1. Đối với các chuỗi có thể dịch, hãy sử dụng `{{ '{{ _("This string is translated") }}' }}`

{next}