# Trường Table MultiSelect

Trường Table MultiSelect rất giống với trường Link. Sự khác biệt chính là trường Table MultiSelect cho phép bạn chọn nhiều giá trị cùng lúc.

Hãy cùng xem xét một ví dụ để hiểu rõ hơn. Giả sử bạn muốn giao một công việc (ToDo) cho nhiều người dùng, như hiển thị dưới đây:

<img alt="Table MultiSelect Field" class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/articles/table-multiselect-field.png">

Bạn có thể thêm trường Table MultiSelect bằng các bước sau:

## Bước 1: Tạo một DocType con.

Tạo một DocType mới, tích chọn các ô 'Is Child Table' và 'Editable Grid', sau đó thêm một trường có kiểu 'Link' như hiển thị dưới đây.

Thiết lập trường link là bắt buộc. Đảm bảo rằng trường trong bảng con đã được tích chọn "In List View".

<img alt="DocType for Table MultiSelect" class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/articles/doctype-for-table-multi-select.png">

## Bước 2: Thêm một trường có kiểu 'Table MultiSelect'.

Tạo một trường có kiểu 'Table MultiSelect' và thêm DocType đã tạo ở bước đầu tiên vào phần 'options'.

<img alt="Field with type Table MultiSelect" class="screenshot" src="https://docs.erpnext.com/docs/v16/assets/img/articles/multi-select-field.png">

Bạn có thể xóa bất kỳ giá trị nào đã chọn bằng cách nhấp vào dấu x bên cạnh giá trị đó hoặc đặt con trỏ chuột cạnh giá trị và nhấn phím Backspace.

Trường này chỉ cho phép mỗi giá trị được chọn duy nhất một lần.

> Lưu ý: Không thể thêm trường Table MultiSelect vào các DocType con.

{next}