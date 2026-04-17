<!-- add-breadcrumbs -->
<!-- title: Cài đặt Nhân sự -->

# Cài đặt Nhân sự

**Cài đặt Nhân sự cho phép thiết lập các cài đặt chung cho các tài liệu liên quan đến Nhân sự.**

Để truy cập Cài đặt Nhân sự, hãy đi tới:
> Home > Human Resources > Settings > HR Settings

Có nhiều cài đặt khác nhau có sẵn trong Cài đặt Nhân sự.

## 1. Cài đặt Nhân viên

<img class="screenshot" alt="Previous Work Experience" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/hr-settings1.png">

### 1.1. Tuổi nghỉ hưu:
Bạn có thể nhập tuổi nghỉ hưu (tính theo năm) cho nhân viên của mình.

### 1.2 Tài liệu Nhân viên được tạo bởi
Việc đặt tên cho các tài liệu nhân viên dựa trên giá trị được chọn trong trường này.

* **Naming Series**: Các tài liệu nhân viên được tạo sẽ được đặt tên theo chuỗi đặt tên được chọn trong trường 'Series'.
* **Employee Number**: Trường Số nhân viên sẽ hiển thị khi chọn tùy chọn này, và việc đặt tên cho tài liệu nhân viên sẽ dựa trên trường này.
* **Full Name**: Tài liệu nhân viên được đặt tên theo họ tên đầy đủ của nhân viên.

### 1.3 Dừng Nhắc ngày sinh nhật
Một email sẽ được gửi đến tất cả nhân viên của công ty khi có một nhân viên có ngày sinh nhật. Để dừng việc gửi email này, bạn có thể chọn tùy chọn này.

### 1.4 Bắt buộc Người phê duyệt chi phí trong Yêu cầu thanh toán chi phí
Trong tài liệu Yêu cầu thanh toán chi phí (Expense Claim), trường 'Người phê duyệt chi phí' (Expense Approver) sẽ được đặt thành bắt buộc khi chọn tùy chọn này.

> Cài đặt Bảng lương (Payroll Settings) sẽ là một phần của Cài đặt Nhân sự cho đến phiên bản 12. Trong phiên bản 13, Cài đặt Bảng lương sẽ là một phần của mô-đun mới, Payroll.

## 2. Cài đặt Bảng lương

<img class="screenshot" alt="Previous Work Experience" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/hr-settings2.png">

#### 2.1 Tính Ngày làm việc của Bảng lương Dựa trên
Số ngày làm việc trong Phiếu lương có thể được tính dựa trên Đơn xin nghỉ phép hoặc hồ sơ Chấm công. Bạn có thể chọn tùy chọn dựa trên những gì bạn muốn để tính ngày làm việc.

#### 2.2 Số giờ làm việc tối đa đối với Bảng chấm công
Đối với các phiếu lương dựa trên bảng chấm công, bạn có thể thiết lập số giờ tối đa được phép cho một bảng chấm công duy nhất. Đặt giá trị này bằng không để vô hiệu hóa việc kiểm tra này.

### 2.3 Bao gồm ngày lễ trong Tổng số Ngày làm việc
Nếu được chọn, tổng số ngày làm việc sẽ bao gồm cả ngày lễ, và điều này sẽ làm giảm giá trị lương mỗi ngày.

### 2.4 Vô hiệu hóa Làm tròn Tổng số
Bạn có thể bật tùy chọn này để vô hiệu hóa việc làm tròn tổng số tiền trong phiếu lương.

### 2.5 Tỷ lệ Lương ngày cho Nửa ngày
Dựa trên tỷ lệ này, lương cho Nửa ngày sẽ được tính toán. Ví dụ, nếu giá trị được đặt là 0.75, thì ba phần tư mức lương sẽ được cấp cho việc đi làm nửa ngày.

### 2.6 Gửi Phiếu lương qua Email cho Nhân viên
Một email kèm theo phiếu lương sẽ được gửi đến địa chỉ email ưu tiên của nhân viên tương ứng khi Xác nhận phiếu lương.

### 2.7 Mã hóa Phiếu lương trong Email
File PDF phiếu lương được gửi cho nhân viên sẽ được mã hóa bằng Chính sách mật khẩu đã nêu.

### 2.8 Chính sách mật khẩu
Trường này sẽ hiển thị và trở thành bắt buộc khi chọn tùy chọn trên để mã hóa phiếu lương trong email.

Dưới đây là một ví dụ về cách thiết lập Chính sách mật khẩu cho file PDF phiếu lương.

**Ví dụ:**

```
SAL-{first_name}-{date_of_birth.year}
```

Điều này sẽ tạo ra một mật khẩu như SAL-Jane-1972

## 3. Cài đặt Nghỉ phép

<img class="screenshot" alt="Previous Work Experience" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/hr-settings3.png">

### 3.1 Mẫu Thông báo Phê duyệt Nghỉ phép
Khi tạo hoặc cập nhật một đơn xin nghỉ phép có người phê duyệt nghỉ phép, một email sẽ được gửi đến người phê duyệt này để thông báo về đơn xin nghỉ phép mới. Mẫu email được sử dụng cho mục đích này có thể được chọn tại đây.

### 3.2 Mẫu Thông báo Trạng thái Nghỉ phép
Khi Xác nhận/Hủy một đơn xin nghỉ phép, nhân viên sẽ nhận được một email với trạng thái đã cập nhật của đơn xin nghỉ phép của họ. Mẫu email được sử dụng cho mục đích này có thể được chọn tại đây.

### 3.3 Bắt buộc Người phê duyệt Nghỉ phép trong Đơn xin nghỉ phép
Trong tài liệu Đơn xin nghỉ phép, trường 'Người phê duyệt nghỉ phép' sẽ được đặt thành bắt buộc khi chọn tùy chọn này.

### 3.4 Hiển thị Nghỉ phép của Tất cả Thành viên trong Bộ phận trên Lịch
Các ngày nghỉ đã được phê duyệt của tất cả nhân viên trong cùng một bộ phận sẽ được hiển thị trong chế độ xem lịch khi chọn tùy chọn này.

### 3.5 Tự động Quy đổi Nghỉ phép thành Tiền
Nếu được chọn, hệ thống sẽ tạo một bản ghi Nháp Quy đổi nghỉ phép thành tiền khi hết hạn phân bổ nghỉ phép cho tất cả các Loại nghỉ phép có thể quy đổi thành tiền.

### 3.6 Hạn chế Đơn xin nghỉ phép lùi ngày
Nếu được chọn, hệ thống sẽ không cho phép tạo đơn xin nghỉ phép lùi ngày.

> Được giới thiệu trong phiên bản 13

### 3.7 Tự động Phân bổ Nghỉ phép Dựa trên Chính sách Nghỉ phép
Nếu được chọn, các ngày nghỉ sẽ được cấp cho nhân viên một cách tự động dựa trên ngày Có hiệu lực theo Phân bổ Chính sách Nghỉ phép hiện tại.

## 4. Cài đặt Tuyển dụng

### 4.1 Kiểm tra Vị trí trống khi Tạo Thư mời làm việc
Khi tạo một thư mời làm việc cho một vị trí cụ thể, các vị trí trống có trong kế hoạch nhân sự cho vị trí đó sẽ được kiểm tra để cảnh báo người dùng tránh tuyển dụng quá mức cho một vị trí cụ thể.

{next}