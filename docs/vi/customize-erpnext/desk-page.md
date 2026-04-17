<!-- add-breadcrumbs -->
# Trang Desk

Khi bạn đăng nhập, bạn sẽ được hiển thị giao diện Desk. Nó có một thanh bên cố định được sắp xếp theo các danh mục. Mỗi mục trên thanh bên sẽ liên kết đến một trang gọi là Trang Desk.

Một Trang Desk đại diện cho một module (ví dụ: CRM trong ERPNext). Một Trang Desk bao gồm các thành phần sau:

- Một phần trang tổng quan cho module cụ thể đó.
- Một phần lối tắt cho các danh mục chính, giao dịch hoặc các trang thường xuyên được sử dụng.
- Một phần danh mục chính nơi tất cả các báo cáo và danh mục chính được nhóm và liệt kê.

<img alt="Standard Desk Page" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/customize/standard-desk-page.png">

## Trang Desk Tiêu chuẩn

Mỗi module trong ERPNext đều có Trang Desk Tiêu chuẩn riêng, được tạo sẵn với các lối tắt và liên kết phù hợp.

<img alt="Desk Page List" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/customize/desk-page-list.png">

Mọi tùy chỉnh đối với Trang Desk Tiêu chuẩn đều có thể được thực hiện bằng tùy chọn Tùy chỉnh Trang Desk ở góc trên bên phải của Trang Desk.

> Lưu ý: Những tùy chỉnh này sẽ dành riêng cho từng người dùng và chỉ hiển thị với người dùng đó.

<img alt="Customize Desk Page" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/customize/customize-desk-page.png">

## Trang Desk Tùy chỉnh

Bạn cũng có thể tạo các Trang Desk của riêng mình bằng cách chỉ cần tạo một tài liệu Trang Desk mới.

<img alt="New Desk Page" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/customize/new-desk-page.png">

1. Đi tới danh sách Trang Desk và nhấn vào Mới.

1. **Name**: Văn bản bạn nhập ở đây sẽ được hiển thị trên thanh bên.

1. **Module**: Chọn module mà Trang Desk này sẽ đại diện.

1. ***Is Standard***: Nếu được chọn, Trang Desk này sẽ được hiển thị trên thanh bên. Nếu không, nó sẽ được coi là một phiên bản tùy chỉnh của một Trang Desk Tiêu chuẩn.

1. ***Extends Another Page***: Nếu được chọn, Trang Desk này sẽ được coi là một phiên bản tùy chỉnh của một Trang Desk khác.

1. ***Is Default***: Nếu được chọn, Trang Desk này sẽ là Trang Desk mặc định được hiển thị cho tất cả người dùng đối với một module cụ thể.

1. ***Dashboard***: Thêm một Trang tổng quan để hiển thị ở phía trên cùng của Trang Desk.

1. ***Shortcuts***: Thêm các Lối tắt đến một trang, báo cáo hoặc danh sách cụ thể sẽ được hiển thị bên dưới trang tổng quan.

1. ***Link Cards***: Bạn có thể thêm các thẻ hiển thị một danh sách liên kết đến một trang, báo cáo hoặc danh sách cụ thể. Bạn phải thêm chúng theo định dạng JSON cụ thể như hiển thị trong hình dưới đây.

<img alt="Desk Page Card" class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/customize/desk-page-card.png">

{next}