<!-- add-breadcrumbs -->
# Quyền người dùng

**Quyền người dùng là một cách để hạn chế quyền truy cập của người dùng vào các tài liệu cụ thể.**

Quyền dựa trên vai trò cho phép thiết lập quyền truy cập hoàn toàn (theo mặc định) đối với một loại tài liệu (DocType) như Hóa đơn, Đơn bán hàng, Báo giá, v.v. Điều này có nghĩa là khi bạn gán vai trò Người dùng Bán hàng cho một người dùng, họ có thể truy cập tất cả các Đơn bán hàng và Báo giá.

Quyền người dùng có thể được sử dụng để hạn chế quyền truy cập vào các tài liệu được chọn dựa trên các trường liên kết trong tài liệu. Ví dụ, giả sử bạn kinh doanh tại nhiều khu vực và bạn muốn hạn chế quyền truy cập của một số Người dùng Bán hàng nhất định đối với các Báo giá/Đơn bán hàng thuộc về một khu vực cụ thể. Điều này có thể được thực hiện thông qua Quyền người dùng. Các hạn chế có thể được thiết lập trên Khách hàng, Nhà cung cấp, Nhóm khách hàng, Nhóm nhà cung cấp, v.v.

Thiết lập Quyền người dùng đặc biệt hữu ích khi bạn muốn hạn chế dựa trên:

1. Cho phép người dùng truy cập dữ liệu thuộc về một Công ty
2. Cho phép người dùng truy cập dữ liệu liên quan đến một Khách hàng hoặc Khu vực cụ thể

Để truy cập Quyền người dùng, hãy đi tới:
> Home > User and Permissions > User Permissions


## 1. Cách tạo Quyền người dùng

1. Đi tới danh sách Quyền người dùng, nhấn vào Mới.
1. Chọn người dùng mà quy tắc cần được áp dụng.
2. Chọn loại tài liệu được cho phép (ví dụ "Company").
3. Tại mục For Value, chọn mục cụ thể mà bạn muốn cho phép (tên của "Company").
4. Nếu bạn tích vào 'Is Default', giá trị được chọn trong 'For Value' sẽ được sử dụng mặc định cho bất kỳ giao dịch nào trong tương lai của người dùng này. Nghĩa là nếu công ty 'Unico Plastics Inc.' được chọn làm 'For Value', Công ty này sẽ được thiết lập làm mặc định cho tất cả các giao dịch trong tương lai của người dùng này.

    <img src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/user-perms/new-user-permission.png" class="screenshot" alt="Creating a new user permission">

    > Lưu ý: Chỉ có thể thiết lập một quyền người dùng duy nhất làm mặc định cho một loại tài liệu cụ thể đối với một người dùng cụ thể.

## 2. Các hành động Quyền người dùng khác
### 2.1 Kiểm soát nâng cao

Trong phần Kiểm soát nâng cao, bạn có thể kiểm soát tốt hơn nơi Quyền người dùng được áp dụng.

### 2.1.1. Áp dụng cho (Applicable For)

Bạn có thể tùy chọn chỉ áp dụng quyền người dùng cho một loại tài liệu cụ thể bằng cách thiết lập Document Type sau khi bỏ tích ô Apply To All Document Types.
Việc thiết lập tùy chọn **Applicable For** sẽ làm cho quyền người dùng hiện tại chỉ có hiệu lực dưới Master Document Type đã chọn.

<img src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/user-perms/advanced-control.png" class="screenshot" alt="Applicable For">

Trong Quyền người dùng ở trên, người dùng sẽ chỉ có thể truy cập các Đơn bán hàng của công ty đã được chọn.

**Lưu ý:** Nếu **Applicable For** không được thiết lập, Quyền người dùng sẽ áp dụng cho tất cả các Document Type liên quan.

### 2.1.2. Ẩn các cấp con (Hide Descendants)

Giá trị của **Allow** có thể là một DocType có Chế độ xem cây (Tree View), trong đó sẽ có các bản ghi có mối quan hệ cha-con hoặc tổ tiên-hậu duệ.

Giả sử **For Value** là 'Unico Plastics Inc.', có một công ty con là 'Unico Toys'. Khi một Quyền người dùng được tạo cho 'Unico Plastics Inc.', quyền cho các cấp con của nó cũng sẽ được cấp.

**Hide Descendants** chỉ hiển thị khi chọn một DocType có Chế độ xem cây. Bằng cách bật hộp kiểm này, quyền cho các cấp con của **For Value** sẽ không được cấp.

<img src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/user-perms/hide-descendant-permissions.png" class="screenshot" alt="Hide Descendant Permissions">

Một người dùng có thể xem các bản ghi của 'Unico Plastics Inc.' sẽ không thể xem các bản ghi của 'Unico Toys'.

### 2.2 Bỏ qua Quyền người dùng trên một số trường nhất định

Một cách khác để cho phép mọi người xem các tài liệu đã bị hạn chế bởi Quyền người dùng là tích vào "Ignore User Permissions" trên một trường cụ thể bằng cách đi tới **Customize Form**.

Ví dụ, nếu bạn không muốn Tài sản bị hạn chế đối với bất kỳ người dùng nào, hãy chọn **Asset** trong loại biểu mẫu. Trong bảng các trường, mở rộng trường Company và tích vào "Ignore User Permissions".

<img src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/user-perms/ignore-user-permissions.png" class="screenshot" alt="Ignore User Permissions on specific properties">


### 2.3 Quyền nghiêm ngặt (Strict Permissions)

Điều này hạn chế quyền truy cập của người dùng vào tài liệu một cách nghiêm ngặt hơn.

Để biết thêm, hãy đi tới [trang Thiết lập hệ thống](/docs/v16/user/manual/en/setting-up/settings/system-settings#14-permissions).

### 2.4 Kiểm tra cách Quyền người dùng được áp dụng

Cuối cùng, sau khi bạn đã tạo mô hình phân quyền chặt chẽ, và bạn muốn kiểm tra cách nó áp dụng cho các người dùng khác nhau. Bạn có thể xem thông qua báo cáo **Permitted Documents for User**. Sử dụng báo cáo này, bạn có thể chọn **User** và loại tài liệu để xem những tài liệu nào mà một người dùng cụ thể có thể truy cập.

Tích vào hộp kiểm Show Permissions sẽ hiển thị các mức độ truy cập đọc/ghi/xác nhận và các mức độ khác.

<img src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/user-perms/permitted-documents.png" class="screenshot" alt="Permitted Documents for User report">

Lưu ý: Nếu bạn không thể truy cập Đơn bán hàng hoặc bất kỳ loại tài liệu nào khác trong danh sách này, hãy đảm bảo rằng bạn đã thiết lập [vai trò](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-based-permissions) một cách chính xác.

Ví dụ, người dùng Bruce bị hạn chế trong Công ty 'Unico Plastics Inc.'
![User restricted to Company](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/users-and-permissions/user-perms/user-restricted-to-company.png)

### 3. Các chủ đề liên quan
1. [Vai trò và Quyền hạn](/docs/v16/user/manual/en/setting-up/users-and-permissions/role-based-permissions)