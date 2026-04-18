<!-- add-breadcrumbs -->
# Triển khai Thuế VAT/Tiêu thụ đặc biệt cho UAE/KSA

### 1. Thiết lập Mã số đăng ký thuế cho Khách hàng, Nhà cung cấp và Công ty

Thiết lập Mã số đăng ký thuế trong trường Tax ID cho Khách hàng, Nhà cung cấp và Công ty.

1. Đối với Khách hàng
<img class="screenshot" alt="TRN in Customer" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/uae/tax-id-customer.png">

2. Đối với Công ty
<img class="screenshot" alt="TRN in Company" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/uae/tax-id-company.png">

### 2. Thiết lập Mã Thuế cho Sản phẩm
Thiết lập mã thuế trong danh mục mặt hàng, hệ thống sẽ tự động lấy mã tương tự trong hóa đơn bán hàng/mua hàng khi chọn một mặt hàng.

<img class="screenshot" alt="Tax Code in Item" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/uae/tax-code-item.png">
### 3. Các Mẫu Thuế Mặc định

ERPNext cung cấp cho bạn các mẫu thuế mặc định cho VAT (5%, 0%, miễn thuế) và thuế tiêu thụ đặc biệt (50%, 100%). Bạn có thể tự tạo [mẫu thuế](../../setting-up/setting-up-taxes.html.md) của riêng mình.

<img class="screenshot" alt="Default Tax Template" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/uae/uae-tax-templates.png">

### 3. Tạo Hóa đơn sẵn sàng cho VAT

Nếu bạn đã thiết lập TRN của Khách hàng và Nhà cung cấp, cũng như mẫu thuế của mình, bạn đã sẵn sàng để tạo các Hóa đơn sẵn sàng cho VAT!

Đối với **Hóa đơn bán hàng**,

1. Chọn đúng Khách hàng, Mặt hàng và địa chỉ nơi giao dịch sẽ diễn ra.
2. Kiểm tra xem TRN của Công ty và Nhà cung cấp đã được thiết lập chính xác chưa.
3. Kiểm tra xem Mã Thuế đã được thiết lập trong Mặt hàng chưa.
4. Chọn mẫu thuế mà bạn đã tạo dựa trên loại giao dịch.
5. Lưu và Xác nhận Hóa đơn.

<img class="screenshot" alt="VAT Invoice" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/uae/vat-invoice.gif">

### 4. In Hóa đơn Thuế

ERPNext cung cấp hai mẫu in mặc định:

1. Hóa đơn Thuế Đơn giản
<img class="screenshot" alt="Simplified Tax Invoice" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/uae/simplified-invoice.png">

2. Hóa đơn Thuế Chi tiết
<img class="screenshot" alt="Detailed Tax Invoice" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/uae/detailed-invoice.png">

### 5. Thiết lập Tài khoản VAT
Chọn các tài khoản sẽ được sử dụng để tạo hóa đơn VAT tại đây.

<img class="screenshot" alt="UAE VAT Account Settings" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/uae/uae-vat-account-settings.png">