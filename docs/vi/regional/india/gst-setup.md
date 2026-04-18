<!-- add-breadcrumbs -->
# Các tính năng GST trong ERPNext

### 1. Thiết lập GSTIN

Luật GST yêu cầu bạn phải duy trì mã số GSTIN cho tất cả các Nhà cung cấp của mình. Trong ERPNext, GSTIN được liên kết với **Địa chỉ**

![GSTIN in Customer](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/gstin-customer.gif)

**GST cho Địa chỉ Công ty của bạn**

Bạn cũng cần thiết lập Địa chỉ cho chính Công ty của mình và Mã số GST của Công ty.

Đi tới danh mục Công ty và thêm GSTIN vào địa chỉ mặc định của bạn.

![GST in Company](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/gstin-company.gif)

**Bao gồm mã số GSTIN trong Mẫu địa chỉ**

Mở bản ghi Mẫu địa chỉ cho Ấn Độ, thêm mã số GSTIN và Mã bang (State Code) tại đó nếu chưa có.

![GST in Address Template](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/address-template-gstin.png)

### 2. Thiết lập Mã HSN

Theo Luật GST, các hóa đơn chi tiết của bạn phải chứa Mã HSN liên quan đến Mặt hàng đó. ERPNext được cài đặt sẵn hơn 12.000 Mã HSN để bạn có thể dễ dàng chọn Mã HSN phù hợp trong Mặt hàng của mình.

![HSN in Item](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/hsn-item.gif)

### 3. Tạo các Tài khoản Thuế (Tax Masters)

Để thiết lập Thanh toán theo GST, bạn cần tạo 3 Tài khoản Thuế cho các đầu mục báo cáo GST khác nhau: CGST - Thuế GST Trung ương, SGST - Thuế GST Bang, IGST - Thuế GST Liên bang.

Đi tới **Hệ thống tài khoản** của bạn, dưới đầu mục Thuế và Phí (Duties and Taxes) của tài khoản, hãy tạo 3 Tài khoản.

**Lưu ý:** Thông thường mức thuế trong CGST và SGST bằng một nửa IGST. Ví dụ, nếu hầu hết các mặt hàng của bạn được lập hóa đơn ở mức 18%, thì hãy tạo IGST là 18%, còn CGST và SGST mỗi loại là 9%.

![GST Ledgers](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/gst-ledger.png)

### 4. Thêm các Tài khoản GST vào Cài đặt GST

Thêm tất cả các Tài khoản GST vào Cài đặt GST. Việc thêm các tài khoản này vào Cài đặt GST sẽ giúp hệ thống nhận diện tất cả các tài khoản GST và tạo các báo cáo GST.

Bạn cũng có thể bật tính năng "Làm tròn giá trị GST" (Round Off GST Values) trong trường hợp bạn muốn làm tròn các thành phần GST riêng lẻ trong hóa đơn.

![GST Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/gst-settings.png)

### 5. Tạo các Mẫu Thuế

Bạn sẽ phải tạo hai mẫu thuế cho cả bán hàng và mua hàng, một mẫu cho bán hàng trong bang và mẫu khác cho bán hàng ngoài bang.

Trong mẫu **GST trong bang (In State GST)** của bạn, hãy chọn 2 tài khoản: SGST và CGST.

![GST Tax Template](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/gst-tax-template.png)

Trong mẫu **GST ngoài bang (Out of State GST)** của bạn, hãy chọn IGST.

### 6. Lập Hóa đơn sẵn sàng cho GST

Nếu bạn đã thiết lập GSTIN cho Khách hàng và Nhà cung cấp, cũng như mẫu thuế của mình, bạn đã sẵn sàng để lập các Hóa đơn sẵn sàng cho GST!

Đối với **Hóa đơn bán hàng**,

1. Chọn đúng Khách hàng, Mặt hàng và địa chỉ nơi giao dịch diễn ra.
2. Kiểm tra xem GSTIN của Công ty và Nhà cung cấp đã được thiết lập chính xác chưa.
3. Kiểm tra xem Mã số HSN đã được thiết lập trong Mặt hàng chưa.
4. Chọn mẫu **GST trong bang** hoặc **GST ngoài bang** mà bạn đã tạo dựa trên loại giao dịch.
5. Lưu và Xác nhận Hóa đơn.

![GST Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/gst-invoice.gif)

### 7. In Hóa đơn Thuế GST

Để in Hóa đơn Thuế theo hướng dẫn của GSTN, vui lòng chọn mẫu in **Hóa đơn Thuế GST (GST Tax Invoice)**. Mẫu in này bao gồm địa chỉ công ty, mã số GSTIN, Mã HSN/SAC và bảng phân bổ thuế theo từng mặt hàng. Và khi in, hãy chọn giá trị chính xác của trường Bản sao Hóa đơn (Invoice Copy) để ghi rõ đó là bản dành cho Khách hàng, Nhà cung cấp hay Đơn vị vận chuyển.

![Sample GST Tax Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/sample-gst-tax-invoice.png)

### 8. Các giao dịch GST

#### 8.1 Hoàn thuế đầu vào (Reversal of Input Tax Credit)

Để hạch toán hoàn thuế ITC, hãy đi tới DocType Bút toán và thực hiện các bước sau:

1. Chọn "Loại bút toán" (Entry Type) là "Hoàn thuế ITC" (Reversal Of ITC).
2. Trong "Loại hoàn thuế" (Reversal Type), chọn "Theo quy tắc 42 & 43 của Quy tắc CGST" hoặc "Khác" tùy theo loại hoàn thuế.
3. Chọn Địa chỉ Công ty (GSTIN) phù hợp mà ITC đang được hoàn lại.
4. Điền các tài khoản và số tiền vào các Bút toán kế toán như hiển thị bên dưới.
5. Lưu và Xác nhận.

![Reversal of Input Tax Credit](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/reversal-of-itc.png)

### 9. Thiết lập thuế suất đảo ngược (reverse charge) và hạch toán hóa đơn mua hàng có thuế suất đảo ngược

#### 9.1 Thêm các tài khoản thuế suất đảo ngược trong Cài đặt GST

Thêm các tài khoản thuế suất đảo ngược cho GST như trong hình dưới đây và tích chọn "Là tài khoản thuế suất đảo ngược" (Is Reverse Charge Account) như trong hình. Thay vì dùng tài khoản thuế suất đảo ngược riêng biệt, tài khoản thuế GST đầu ra (Output GST) dùng cho bán hàng cũng có thể được đánh dấu là tài khoản thuế suất đảo ngược.

![GST Reverse Charge Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/gst-reverse-charge-setting.png)

#### 9.2 Lập hóa đơn mua hàng có tính thuế suất đảo ngược

Để lập các hóa đơn mua hàng có tính thuế suất đảo ngược, vui lòng thực hiện các bước sau:

* Chọn Nhà cung cấp và thêm các mặt hàng vào hóa đơn như bình thường.

* Tại phần Chi tiết GST, chọn "Áp dụng thuế suất đảo ngược" (Reverse Charge Applicable) là "Y".
* Nếu thuế GST đã trả đủ điều kiện để được khấu trừ thuế đầu vào, trong phần "Điều kiện hưởng ITC" (Eligibility for ITC), hãy chọn "ITC trên thuế suất đảo ngược" (ITC on Reverse Charge).
* "Thêm" các loại thuế bằng cách sử dụng các đầu mục tài khoản Thuế đầu vào thông thường.

![Reverse Charge](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/reverse-charge-add.png)

* "Khấu trừ" cùng một số tiền thuế đó bằng cách sử dụng các tài khoản thuế suất đảo ngược để số thuế GST thực tế phải trả cho nhà cung cấp bằng 0.

![Reverse Charge](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/reverse-charge-deduct.png)

* Lưu và Xác nhận.

Để tránh việc phải chọn tài khoản thủ công và tự động hóa quy trình này, vui lòng thực hiện các bước dưới đây:

* Tạo Danh mục Thuế (Tax Category) cho thuế suất đảo ngược.

![Reverse Charge Tax Category](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/reverse-charge-tax-category.png)

* Cập nhật danh mục thuế trong các danh mục Nhà cung cấp liên quan.

![Supplier Tax Category](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/supplier-tax-category.png)

* Tạo Mẫu Thuế và Phí Mua hàng (Purchase Taxes and Charges template) cho thuế suất đảo ngược.

![Reverse Charge Template](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/reverse-charge-template.png)

* Sau khi cấu hình này hoàn tất, khi chọn nhà cung cấp, Mẫu Thuế và Phí Mua hàng phù hợp sẽ được áp dụng.

### Báo cáo

ERPNext đi kèm với hầu hết các báo cáo bạn cần để...