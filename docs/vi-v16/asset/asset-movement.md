<!-- add-breadcrumbs -->
# Di chuyển Tài sản

**Di chuyển Tài sản đề cập đến việc di chuyển một Tài sản từ Vị trí này sang Vị trí khác.**

Trong ERPNext, bạn có thể theo dõi vị trí của tài sản hoặc người được cấp phát tài sản đó. Để theo dõi, bạn cần tạo một giao dịch Di chuyển Tài sản bất cứ khi nào tài sản được di chuyển từ vị trí này sang vị trí khác. Bạn cũng có thể theo dõi việc cấp phát tài sản cho bất kỳ nhân viên nào.

Để truy cập danh sách Di chuyển Tài sản, hãy đi đến:
> Home > Assets > Assets > Asset Movement

<img class="screenshot" alt="Asset Movement" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-movement.png">

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Di chuyển Tài sản, bạn nên tạo các mục sau trước:

* [Tài sản](/docs/v16/user/manual/vi/asset/asset)
* [Vị trí tài sản](/docs/v16/user/manual/vi/asset/asset-location)


## 2. Cách tạo Di chuyển Tài sản
1. Đi đến danh sách Di chuyển Tài sản, nhấn vào **Mới (New)**.
1. Chọn Mục đích (Purpose) từ 'Issue' (Cấp phát), 'Receipt' (Nhận) hoặc 'Transfer' (Chuyển). Các trường bắt buộc sẽ thay đổi dựa trên mục đích.
1. Chọn một ngày.
1. Chọn các Tài sản bạn muốn di chuyển. Vị trí hiện tại / Người quản lý (Custodian) sẽ được tự động lấy dữ liệu.
1. Chọn Loại tài liệu tham chiếu (Reference Document Type) (Tùy chọn).
1. Chọn Tên tài liệu tham chiếu (Reference Document Name) (Tùy chọn).
1. **Lưu (Save)**.
1. **Xác nhận (Submit)**.

Để thực hiện Di chuyển Tài sản cho nhiều tài sản cùng lúc, bạn nên đi đến Danh sách Tài sản, chọn các tài sản cần di chuyển và nhấn vào **Make Asset Movement** từ menu Actions ở phía trên bên trái.

<img class="screenshot" alt="Move Multiple Assets" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-movement-using-button.png">

Ngoài ra còn có nút **Transfer Asset** ở phía trên bên phải của biểu mẫu Tài sản để bắt đầu Di chuyển Tài sản. Nó sẽ tự động điền các trường có sẵn từ Biểu mẫu Tài sản.

<img class="screenshot" alt="Move Single Asset" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/asset/asset-movement-using-transfer-asset-button.png">

{next}