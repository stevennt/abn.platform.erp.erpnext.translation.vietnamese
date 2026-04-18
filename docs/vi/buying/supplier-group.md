<!-- add-breadcrumbs -->
# Nhóm nhà cung cấp
**Nhóm nhà cung cấp là một tập hợp các nhà cung cấp có những điểm tương đồng nhất định.**

Một nhà cung cấp có thể được phân biệt với nhà thầu hoặc nhà thầu phụ, những người thường bổ sung các đầu vào chuyên dụng cho các sản phẩm bàn giao. Nhà cung cấp còn được gọi là vendor. Có nhiều loại nhà cung cấp khác nhau dựa trên hàng hóa và sản phẩm mà họ cung cấp.

ERPNext cho phép bạn tạo các danh mục nhà cung cấp của riêng mình. Các danh mục này được gọi là Nhóm nhà cung cấp. Ví dụ, nếu các nhà cung cấp của bạn chủ yếu là các công ty dược phẩm và nhà phân phối hàng tiêu dùng nhanh (FMCG), bạn có thể tạo các Nhóm nhà cung cấp mới cho họ và đặt tên nhóm tương ứng.

Để truy cập Nhóm nhà cung cấp, hãy đi đến:
> Home Mua hàng > Nhà cung cấp > Nhóm nhà cung cấp

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Nhóm nhà cung cấp, bạn nên tạo các mục sau trước:

* [Nhà cung cấp](supplier.md)

## 2. Cách tạo Nhóm nhà cung cấp
1. Đi đến danh sách Nhóm nhà cung cấp, nhấn vào Mới.
1. Nhập tên cho Danh mục Nhà cung cấp mới của bạn.
1. Bạn có thể thiết lập Nhóm nhà cung cấp cha cho Nhóm nhà cung cấp này.
1. Tích vào ô Is Group sẽ biến nó thành một Nhóm nhà cung cấp cha.
1. Bạn cũng có thể chỉ định một Mẫu điều khoản thanh toán mặc định cho Nhóm nhà cung cấp. Điều này hữu ích trong trường hợp tất cả các nhà cung cấp phần cứng của bạn đều nhận một nửa thanh toán khi có đơn bán hàng và một nửa sau khi giao hàng.
1. Lưu.

<img class="screenshot" alt="Supplier Group" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/supplier-group.png">

Bạn có thể phân loại các nhà cung cấp của mình từ một loạt các lựa chọn có sẵn trong ERPNext. Chọn từ một tập hợp các tùy chọn có sẵn như Nhà phân phối, Điện, Phần cứng, Địa phương, Dược phẩm, Nguyên liệu thô, Dịch vụ, v.v. Việc phân loại nhà cung cấp thành các loại khác nhau sẽ tạo điều kiện thuận lợi cho việc kế toán và thanh toán.

## 3. Cây Nhóm nhà cung cấp

Bạn cũng có thể xây dựng Nhóm nhà cung cấp dưới dạng cấu trúc cây phân cấp, tương tự như Hệ thống tài khoản.

Để xem cấu trúc Cây, hãy nhấp vào **Tree** từ thanh bên. Để quay lại chế độ xem danh sách, chỉ cần chọn: **Menu > View List**.

<img class="screenshot" alt="Supplier Group" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/buying/supplier-group-tree.png">

Với [Phân quyền người dùng](../setting-up/users-and-permissions) mới, giờ đây bạn có thể áp dụng các quyền dựa trên phân cấp. Nghĩa là, nếu một Người dùng được phép xem nút cha của Nhóm nhà cung cấp, người đó sẽ mặc nhiên có quyền xem các nút con của nút cha đó.

Ví dụ, trong hình ảnh trên, giả sử quyền người dùng được áp dụng để một Người dùng xem tài liệu 'Distributor' (Nhà phân phối). Khi đó, người dùng cũng được phép xem các nút con của nó như 'Book Distributor' (Nhà phân phối sách), 'Electronic Distributor' (Nhà phân phối điện tử), v.v.

### 4. Các chủ đề liên quan
1. [Nhà cung cấp](supplier.md)

{next}