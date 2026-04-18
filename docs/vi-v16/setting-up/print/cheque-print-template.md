<!-- add-breadcrumbs -->
# Mẫu in Séc

**Mẫu in Séc cho phép định nghĩa các mẫu dành cho séc ngân hàng.**

Hoạt động kinh doanh bao gồm việc thực hiện thanh toán cho nhiều bên khác nhau như Nhà cung cấp và nhân viên. Thanh toán có thể được thực hiện qua nhiều hình thức như tiền mặt, NEFT hoặc séc. Nếu bạn thực hiện thanh toán bằng séc, bạn cũng có thể tạo một Mẫu in để in Séc từ ERPNext dựa trên Thanh toán.

Để truy cập Mẫu in Séc, hãy đi tới:
> Trang chủ > Kế toán > Mẫu in Séc

Sử dụng Mẫu in Séc, bạn có thể tạo một Mẫu in mới cho séc. Nó sẽ được tạo dựa trên định dạng séc do ngân hàng của bạn cung cấp.

Một mẫu séc:

<img class="screenshot" alt="Sample Cheque" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/sample-cheque.jpg">


## 1. Cách tạo Mẫu in Séc
1. Đi tới danh sách Mẫu in Séc, nhấn vào **Mới**.
1. Bạn có thể thiết lập vị trí của các mục khác nhau trong tờ séc.
1. **Lưu**.

Trong Mẫu in Séc, đối với mỗi giá trị (ví dụ: Người thụ hưởng, Ngày), các tọa độ chính xác được cung cấp dựa trên nơi giá trị đó cần được in trên tờ séc. Tọa độ được cung cấp theo đơn vị centimet. Dưới đây là hình ảnh minh họa cấu trúc:

<img class="screenshot" alt="Sample Cheque" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/cheque-1.png">

### 1.1 Tạo định dạng mới bằng cách quét (Scanning)

Để tăng tốc việc tạo định dạng in séc mới, bạn có thể tải lên một hình ảnh quét của tờ séc. Dựa trên hình ảnh quét của tờ séc, hệ thống sẽ tự động cập nhật tọa độ cho từng giá trị như tên bên thụ hưởng, số tiền, ngày tháng, số tiền bằng chữ, v.v.

### 1.2 Tạo Mẫu in mới bằng thủ công
Nếu bản xem trước trông ổn, hãy nhấn vào nút **Tạo Mẫu in** để tạo một Mẫu in mới để in séc. Dựa trên các giá trị được cung cấp trong Mẫu in Séc, hệ thống sẽ tự động tạo một mã HTML cho Mẫu in của tờ séc.

Bạn có thể cung cấp tọa độ cho từng giá trị một cách thủ công dựa trên nơi bạn muốn in trên tờ séc và tùy chỉnh bằng HTML/CSS.

#### Xem trước
Dựa trên các tọa độ được cung cấp cho tất cả các giá trị, một bản xem trước sẽ được hiển thị để biết các giá trị sẽ được in như thế nào trên tờ séc.

<img class="screenshot" alt="Sample Cheque" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/cheque-2.png">

### 1.3 In Séc

Mẫu in mới được tạo cho tờ séc sẽ hiển thị trong biểu mẫu Thanh toán. Sau khi tạo Thanh toán, bạn sẽ có thể in chi tiết giao dịch lên tờ séc.

<img class="screenshot" alt="Sample Cheque" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/setup/print/cheque-3.gif">

### 2. Các chủ đề liên quan
1. [Mẫu địa chỉ](../user/manual/en/setting-up/print/address-template)
1. [Mẫu Điều khoản và Điều kiện](../user/manual/en/setting-up/print/terms-and-conditions)