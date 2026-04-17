<!-- add-breadcrumbs -->
# Chứng nhận Khấu trừ Thấp hơn

Theo danh mục khấu trừ thuế, người chịu trách nhiệm thực hiện thanh toán được yêu cầu khấu trừ thuế tại nguồn theo các mức quy định. Thay vì thu thuế từ thu nhập của bạn vào một thời điểm sau đó, chính phủ muốn người thanh toán khấu trừ thuế trước và nộp vào ngân sách chính phủ. Tuy nhiên, cơ chế khấu trừ thuế tại nguồn này có thể gây khó khăn cho một số người nộp thuế có thể không có thu nhập chịu thuế trong năm tài chính đó.

Do đó, đối với những người nộp thuế như vậy, chính phủ cung cấp một tùy chọn để nhận chứng nhận xác nhận mức thuế TDS thấp hơn hoặc bằng 0 so với mức thuế được quy định trong danh mục khấu trừ thuế.

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Chứng nhận Khấu trừ Thấp hơn, bạn nên tạo và nghiên cứu các mục sau trước:

1. [Nhà cung cấp](/docs/v13/user/manual/en/buying/supplier)
1. [Danh mục Khấu trừ Thuế](/docs/v13/user/manual/en/accounts/tax-withholding-category)

## 2. Cách tạo Chứng nhận Khấu trừ Thấp hơn
1. Đi tới danh sách Chứng nhận Khấu trừ Thấp hơn và nhấn vào Mới.
1. Nhập Số chứng nhận.
1. Chọn Mã mục (Section Code).
1. Nhập [Năm tài chính](/docs/v13/user/manual/en/accounts/fiscal-year).
1. Chọn Nhà cung cấp có số PAN hợp lệ. Số PAN sẽ được tự động lấy khi chọn Nhà cung cấp.
1. Nhập ngày Có hiệu lực từ và Có hiệu lực đến.
1. Nhập mức thuế TDS theo chứng nhận và hạn mức chứng nhận.
1. Nhấn Lưu.

 ![Lower Deduction Certificate](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/lower-deduction-certificate.png)

## 3. Sử dụng Chứng nhận Khấu trừ Thấp hơn

### 3.1 Sử dụng trong Hóa đơn mua hàng

Trong ví dụ sau, chúng tôi đã chọn danh mục TDS là 'TDS - 194D - Individual' với mức thuế là 5%.

 ![Tax Withholding Category](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/tax-withholding-category.png)

1. Thiết lập Danh mục Khấu trừ Thuế cho Nhà cung cấp trong danh mục nhà cung cấp. Sau đó, khi chọn Nhà cung cấp đó, một ô kiểm sẽ hiển thị trong Hóa đơn mua hàng để chọn có áp dụng thuế hay không và danh mục TDS sẽ được tự động lấy.

 ![Supplier With Tax Withholding Category](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/supplier-with-tax-withholding-category.png)

1. Hãy tạo một hóa đơn trị giá 20.000. Khi Lưu hóa đơn, hệ thống sẽ tự động tính thuế và thêm vào bảng Thuế và Phí mua hàng. Mặc dù danh mục thuế được gán cho nhà cung cấp có mức thuế là 5%, nhưng mức thuế hiện hành là 1% như đã được ghi trong Chứng nhận Khấu trừ Thấp hơn.

 ![Lower TDS in Purchase Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/lower-tax-withholding-in-purchase-invoice.png)

### 4. Các chủ đề liên quan
1. [Danh mục Khấu trừ Thuế](/docs/v13/user/manual/en/accounts/tax-withholding-category)

{next}