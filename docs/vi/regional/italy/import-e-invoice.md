<!-- add-breadcrumbs -->

# Nhập hóa đơn điện tử từ Nhà cung cấp

> Được giới thiệu trong Phiên bản 13

Kể từ ngày 1 tháng 1 năm 2019, hóa đơn điện tử là bắt buộc đối với các doanh nghiệp trong nước thực hiện các giao dịch B2B và B2C nội địa tại Ý. ERPNext có tính năng để nhập hóa đơn của nhà cung cấp từ các tệp XML mà nhà cung cấp gửi cho chính phủ.

ERPNext có tính năng để nhập hóa đơn của nhà cung cấp từ các tệp XML mà nhà cung cấp gửi cho chính phủ. Sử dụng tính năng này, bạn có thể nhập hóa đơn điện tử của Nhà cung cấp vào ERPNext. Các thông tin chi tiết về nhà cung cấp như tên nhà cung cấp, địa chỉ và hóa đơn mua hàng sẽ được tạo tự động trong hệ thống từ các tệp XML.

## 1. Điều kiện tiên quyết
- Đơn vị tính (UOM) Kho mặc định phải được chỉ định trong DocType Cài đặt Kho (Stock Settings).
- Bật tính năng Kiểm tra tính duy nhất của hóa đơn nhà cung cấp (Check Supplier Invoice Uniqueness) trong DocType Cài đặt kế toán (Accounts Settings).
- Tạo một tệp Zip chứa tất cả các tệp XML hóa đơn của nhà cung cấp.

### 2. Cách sử dụng Nhập hóa đơn nhà cung cấp (Import Supplier Invoice)

1. Điều hướng đến DocType Nhập hóa đơn nhà cung cấp (Import Supplier Invoice) từ thanh tìm kiếm toàn cầu và nhập Dãy số hóa đơn (Invoice Series), Công ty (Company), Nhóm nhà cung cấp (Supplier Group), Tài khoản thuế (Tax Account), Mã mặt hàng (Item Code) và Bảng giá mua mặc định (Default Buying Price List).
    <img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/italy/import_einvoice.png">

   - Dãy số hóa đơn (Invoice Series) - Dãy số mà các Hóa đơn mua hàng mới sẽ được tạo theo đó.
   - Công ty (Company) - Công ty mà các Hóa đơn mua hàng mới sẽ được tạo cho công ty đó.
   - Nhóm nhà cung cấp (Supplier Group) - Nhóm nhà cung cấp mà các nhà cung cấp mới sẽ được tạo thuộc về.
   - Tài khoản thuế (Tax Account) - Tài khoản mà các khoản thuế sẽ được ghi nhận cho các Hóa đơn mua hàng được tạo.
   - Mã mặt hàng (Item Code) - Mã mặt hàng sẽ được sử dụng để tạo Hóa đơn mua hàng.
   - Bảng giá mua mặc định (Default Buying Price list) - Bảng giá mua mặc định sẽ được sử dụng cho Hóa đơn mua hàng.

2. Sau khi nhập các chi tiết trên, nhấn Lưu (Save).

3. Đính kèm tệp zip chứa các hóa đơn XML.

4. Nhấn vào Nhập hóa đơn (Import invoices) và các Hóa đơn mua hàng sẽ được tạo. Các Nhà cung cấp sẽ được tạo nếu họ chưa tồn tại trong hệ thống.
    <img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/italy/purchase_invoices_created.png">

5. Nếu việc nhập tệp hoàn tất thành công, bạn sẽ thấy trạng thái Nhập tệp hoàn tất (File Import Completed). Nếu có bất kỳ lỗi nào, bạn có thể xem chúng từ Nhật ký lỗi (Error Log).
    <img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/italy/file_import_completed.png">