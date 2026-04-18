<!-- add-breadcrumbs -->
# Hóa đơn điện tử theo GST

> Được giới thiệu trong phiên bản 13

Hóa đơn điện tử đã được giới thiệu để tiêu chuẩn hóa quy trình lập hóa đơn. Tất cả các hệ thống ERP và phần mềm phải đáp ứng định dạng hóa đơn do GSTN quy định. Nó cũng cung cấp một mức độ tự động hóa trong việc điền các báo cáo GSTR.

Theo hệ thống hóa đơn điện tử mới, các doanh nghiệp có doanh thu cao hơn ₹50Cr phải thực hiện xác thực điện tử tất cả các hóa đơn giữa doanh nghiệp với doanh nghiệp (B2B) với GSTN bằng cách tạo Số tham chiếu hóa đơn (IRN) duy nhất.

Để giúp tự động hóa quy trình Hóa đơn điện tử, chúng tôi đã tích hợp ERPNext với Nhà cung cấp dịch vụ GST (GSP) để bạn có thể dễ dàng xác thực Hóa đơn bán hàng ERPNext với GSTN.

## 1. Điều kiện tiên quyết

- Bạn phải có tài khoản đã đăng ký trên [cổng thông tin](https://einvoice1.gst.gov.in/) E-Invoice.
- Các tài khoản GST phải được thiết lập trong DocType "GST Settings".

> Lưu ý: Việc sử dụng tích hợp này để tự động hóa quy trình sẽ phát sinh thêm phí. Vui lòng liên hệ với Đội ngũ Kinh doanh ERPNext để biết thêm thông tin.

## 2. Thiết lập Hóa đơn điện tử

### 2.1 Lấy thông tin đăng nhập

1. Đăng nhập vào [cổng thông tin](https://einvoice1.gst.gov.in/) E-Invoice bằng tên người dùng và mật khẩu của bạn. Đăng ký tên người dùng và mật khẩu nếu bạn chưa tạo tài khoản.
1. Nhấp vào "API registration" ở thanh bên.
1. Nhấp vào "User Credentials" từ danh sách được mở rộng.
1. Nhấp vào "Create API User".
1. Nhấp vào "Through GSP" và chọn "Adequare Info Private Limited".
1. Tạo tên người dùng và mật khẩu sẽ được sử dụng để xác thực với GSP.

### 2.2 Thiết lập ERPNext

Đi tới "E-Invoice Settings" và nhấp vào hộp kiểm "Enable".

1. **GSTIN**: Mã số GSTIN mà công ty của bạn đã đăng ký trên cổng thông tin hóa đơn điện tử.
1. **Username**: Tên người dùng đã tạo ở bước trước để xác thực với GSP.
1. **Password**: Mật khẩu đã tạo ở bước trước để xác thực với GSP.

### 2.3 Tạo IRN

Tạo một Hóa đơn bán hàng và để nó ở trạng thái Nháp. Nhấp vào nhóm nút **E-Invoicing** và sau đó nhấp vào **Generate IRN**. Nếu Hóa đơn bán hàng không có bất kỳ lỗi xác thực nào, IRN sẽ được tạo và cập nhật trong Hóa đơn bán hàng. Bây giờ bạn có thể Xác nhận hóa đơn và in Hóa đơn điện tử kèm hình ảnh mã QR bằng cách chọn Mẫu in "GST E-Invoice" khi in.

![Generate IRN in Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/generate-irn-in-invoice.png)

Sau khi quá trình tạo IRN thành công, mã QR và IRN sẽ được lưu trong Hóa đơn bán hàng. Một khi các thông tin này đã được tạo, các trường trong Hóa đơn bán hàng không thể chỉnh sửa được nữa.

![IRN in Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/irn-in-invoice.png)

Bạn có thể in Hóa đơn điện tử bằng Mẫu in GST E-Invoice mặc định. Hoặc bạn có thể tự chỉnh sửa mẫu in của riêng mình để bao gồm các trường hóa đơn điện tử.

![E Invoice Print Format](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/einv-print-format.png)

### 2.4 Hủy IRN

Nếu bạn đã tạo IRN cho một hóa đơn có dữ liệu sai, bạn có thể hủy nó bằng nút **Cancel IRN** trong nhóm nút E-Invoicing. Nhấp vào đó sẽ mở ra một cửa sổ bật lên yêu cầu lý do hủy và ghi chú.

![E Invoice Cancel IRN Button](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/einv-cancel-irn-button.png)

Sau khi bạn hủy IRN, hóa đơn sẽ trông giống như thế này.

![E Invoice WIth IRN Cancelled](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/einv-cancelled-irn.png)

## 3. Lệnh vận chuyển điện tử (E-Way bill)

### 3.1 Tạo Lệnh vận chuyển điện tử

Hóa đơn điện tử giúp giảm bớt bước bổ sung liên quan đến việc tạo Lệnh vận chuyển điện tử. Giờ đây bạn có thể cung cấp **Thông tin đơn vị vận chuyển** cùng với việc tạo IRN để tạo Lệnh vận chuyển cho hóa đơn. Bạn có thể tìm thấy phần Thông tin đơn vị vận chuyển ở phần dưới của hóa đơn. Bạn phải chọn **Đơn vị vận chuyển**, **Phương thức vận chuyển** và **Khoảng cách** để tạo Lệnh vận chuyển điện tử. Bạn cũng có thể tạo Lệnh vận chuyển điện tử sau khi đã tạo IRN và Xác nhận hóa đơn.

![E Invoice Generate Eway Bill](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/einv-generate-ewaybill-button.png)

Bạn sẽ thấy một cửa sổ bật lên với thông tin liên quan trước khi gửi:
![E Way Bill Dialog](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/einv-gen-ewaybill-dialog.png)

### 3.2 Hủy Lệnh vận chuyển điện tử

Quy trình tương tự như việc hủy IRN. Nhấp vào Cancel E-Way Bill và sau đó nhập lý do và ghi chú cho việc hủy.

![Cancel E-way Bill](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/einv-cancel-ewaybill-button.png)

<img class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/regional/india/einv_cancelled_ewaybill.png">

{next}