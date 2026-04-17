<!-- add-breadcrumbs -->
# Địa chỉ

Bạn có thể ghi lại các địa chỉ liên kết với Khách hàng tiềm năng, Khách hàng, Nhà cung cấp, Cổ đông, Đối tác bán hàng hoặc Kho.

Bạn cũng có thể thêm một Địa chỉ như một bản ghi độc lập mà không cần liên kết với bất kỳ thực thể nào được liệt kê ở trên.

Để truy cập danh sách Địa chỉ, hãy đi đến:
> Home > CRM > Address

## 1. Cách tạo Địa chỉ

1. Đi đến danh sách Địa chỉ và nhấn vào Mới.
1. Chọn Loại Địa chỉ.
1. Nhập chi tiết vào Dòng địa chỉ 1, Dòng địa chỉ 2, Thành phố/Thị trấn, Huyện, Bang, Quốc gia.
1. Nhập Địa chỉ Email, Điện thoại và Fax.
1. Nhập Link DocType và Link Name để liên kết địa chỉ này với khách hàng, nhà cung cấp, v.v.
4. Lưu.
    ![Contact](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/address.png)

Bạn cũng có thể thêm Địa chỉ từ bản ghi Khách hàng hoặc Nhà cung cấp bằng cách nhấp vào nút "New Address" như hiển thị bên dưới.

![Add Address From Customer](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/add-address-from-customer.png)

Để Nhập nhiều địa chỉ từ bảng tính, hãy sử dụng [Công cụ Nhập dữ liệu](/docs/v13/user/manual/en/setting-up/data/data-import).

---
## 2. Các tính năng

### 2.1 Liên kết một Địa chỉ với nhiều Thực thể

Một địa chỉ có thể được liên kết với nhiều khách hàng hoặc nhiều nhà cung cấp.

Một địa chỉ cũng có thể được liên kết với cả khách hàng và nhà cung cấp cùng một lúc.

![Link One Address to Multiple Entities](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/link-address-to-multiple-entities.png)

### 2.2 Tiêu đề Địa chỉ

Nếu địa chỉ không được liên kết với bất kỳ thực thể nào, bạn cần thêm tiêu đề một cách thủ công.

Nếu địa chỉ được liên kết với một thực thể như khách hàng hoặc nhà cung cấp, tiêu đề sẽ được tạo tự động theo định dạng 'Tên thực thể-Loại địa chỉ'.

![Address Title](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/address-title.png)

### 2.3 Địa chỉ Thanh toán ưu tiên và Địa chỉ Giao hàng ưu tiên

Nếu bạn tích vào 'Preferred Shipping Address', địa chỉ sẽ tự động được thêm vào Địa chỉ giao hàng trong các giao dịch Đơn bán hàng, Hóa đơn bán hàng và Phiếu giao hàng.

Tương tự, nếu bạn tích vào 'Preferred Billing Address', địa chỉ sẽ tự động được thêm vào Địa chỉ thanh toán trong các giao dịch Đơn bán hàng, Hóa đơn bán hàng và Phiếu giao hàng.

### 2.4 Bản địa hóa GST cho Ấn Độ
Nếu khách hàng hoặc nhà cung cấp đã đăng ký theo GST, bạn có thể nhập GSTIN và GST State trong Địa chỉ. Hãy đảm bảo GSTIN được nhập đúng định dạng.
![GST Details in Address](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/gst-details-in-address.png)

Trong các giao dịch bán hàng, cùng với địa chỉ, GSTIN cũng sẽ được lấy ra.

![GST Details in Sales Order](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/gst-details-in-sales-order.png)

Bạn cũng có thể thêm địa chỉ của các cơ sở thuộc công ty của mình. Tích vào 'Is Your Company Address', chọn Công ty trong Link DocType, và Tên công ty trong Link Name cho các địa chỉ như vậy, sau đó bạn có thể chọn chúng trong Hóa đơn bán hàng GST để in địa chỉ của chính mình.

![Company Address](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/crm/company-address.png)

> GSTIN cần được thêm vào Địa chỉ chứ không phải trong Khách hàng/Nhà cung cấp, vì một Khách hàng/Nhà cung cấp có thể có nhiều GSTIN (mỗi bang nơi họ kinh doanh sẽ có một mã riêng).


### 3. Các chủ đề liên quan
1. [Khách hàng](/docs/v13/user/manual/en/CRM/customer)
1. [Nhà cung cấp](/docs/v13/user/manual/en/buying)
1. [Đối tác bán hàng](/docs/v13/user/manual/en/selling)

{next}