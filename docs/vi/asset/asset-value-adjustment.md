<!-- add-breadcrumbs -->
# Điều chỉnh giá trị tài sản

**Nếu giá trị của một Tài sản thay đổi đột ngột do bất kỳ hư hỏng nào, nó có thể được ghi nhận bằng cách sử dụng Điều chỉnh giá trị tài sản.**

Trong trường hợp quản lý tài sản cố định, đôi khi giá trị của một tài sản cần được điều chỉnh. Ví dụ, nếu một chiếc máy tính xách tay bị hư hỏng vì lý do nào đó, giá trị của nó sẽ giảm xuống ngay lập tức. Và trong trường hợp đó, chúng ta phải điều chỉnh lại giá trị của tài sản.

Để truy cập vào Điều chỉnh giá trị tài sản, hãy đi tới:
> Home > Assets > Maintenance > Asset Value Adjustment

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Điều chỉnh giá trị tài sản, bạn nên tạo các mục sau trước:

1. [Asset](asset.md)
1. Bật 'Calculate Depreciation' trong biểu mẫu Asset

## 2. Cách tạo Điều chỉnh giá trị tài sản

1. Đi tới danh sách Điều chỉnh giá trị tài sản, nhấn vào New.
1. Chọn một Tài sản có giá trị cần được điều chỉnh.
1. Chọn một ngày.
1. Nhập giá trị hiện tại và giá trị mới của tài sản.
1. Lưu và Xác nhận.

<img class="screenshot" alt="Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-value-adjustment.png">


Khi Lưu, hệ thống sẽ ghi nhận một khoản "Lãi/Lỗ do đánh giá lại tài sản" và điều chỉnh giá trị của tài sản.
Bạn có thể thay đổi trung tâm chi phí và thêm một sổ tài chính (finance book).

Khi Xác nhận, một Bút toán sẽ được tạo trong tài khoản 'Accumulated Depreciations'.

### 3. Các chủ đề liên quan
1. [Asset Depreciation](asset-depreciation.md)
1. [Scrapping an Asset](scrapping-an-asset.md)

{next}