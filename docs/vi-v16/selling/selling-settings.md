# Cài đặt Bán hàng

Cài đặt Bán hàng là nơi bạn có thể xác định các thuộc tính và kiểm tra điều kiện sẽ được áp dụng cho các danh mục chính và các giao dịch liên quan trong chu kỳ bán hàng.

Hãy cùng xem từng tùy chọn có sẵn trong Cài đặt Bán hàng trong ERPNext.

<img class="screenshot" alt="Selling Settings" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/selling-settings.png">

Để truy cập Cài đặt Bán hàng, hãy đi tới:
> Home > Selling > Settings > Selling Settings

## 1. Naming Series (Chuỗi đặt tên)
### 1.1 Customer Naming By (Đặt tên Khách hàng theo)

Khi một Khách hàng được Lưu, một ID duy nhất sẽ được tạo cho Khách hàng đó.

Theo mặc định, ID Khách hàng được tạo dựa trên Tên Khách hàng. Nếu bạn muốn Lưu Khách hàng bằng một chuỗi đặt tên, trong trường Customer Naming Series, hãy đặt giá trị là "Naming Series". Ví dụ về ID Khách hàng được lưu theo Naming Series - "CUST00001, CUST00002, CUST00003..." v.v.

Bạn có thể thiết lập Naming Series cho Khách hàng từ:

**Setup > Data > Naming Series**

### 1.2 Campaign Naming By (Đặt tên Chiến dịch theo)

Giống như đối với Khách hàng, bạn cũng có thể cấu hình phương pháp đặt tên cho danh mục Chiến dịch. Theo mặc định, một chiến dịch sẽ được Lưu với Tên Chiến dịch.

## 2. Defaults (Mặc định)
### 2.1 Default Customer Group and Territory (Nhóm khách hàng và Khu vực mặc định)

Chọn một Nhóm khách hàng mặc định sẽ được tự động cập nhật khi tạo Khách hàng mới.

Báo giá có thể được tạo cho cả Khách hàng và Khách hàng tiềm năng. Khi chuyển đổi một Báo giá thành một Đơn bán hàng được tạo cho một Khách hàng tiềm năng, hệ thống sẽ cố gắng chuyển đổi Khách hàng tiềm năng đó thành một Khách hàng. Khi tạo Khách hàng ở phía backend, các giá trị cho Nhóm khách hàng và Khu vực sẽ được lấy từ Cài đặt Bán hàng. Nếu không tìm thấy giá trị mặc định cho Nhóm khách hàng hoặc Khu vực, bạn sẽ nhận được thông báo kiểm tra yêu cầu Nhóm khách hàng hoặc Khu vực. Bạn cũng có thể chuyển đổi thủ công một Khách hàng tiềm năng thành một Khách hàng.

### 2.2 Default Price List (Bảng giá mặc định)

Bảng giá được thiết lập trong trường này sẽ được tự động cập nhật trong trường Bảng giá của các giao dịch bán hàng như Báo giá, Đơn bán hàng, Phiếu giao hàng và Hóa đơn.

### 2.3 Close Opportunity After Days (Đóng Cơ hội sau số ngày)

Nếu có nhiều Cơ hội có trạng thái khác với Mở, chúng sẽ được tự động đóng sau số ngày được đề cập trong trường này.

### 2.4 Default Quotation Validity Days (Số ngày hiệu lực Báo giá mặc định)

Báo giá gửi cho khách hàng chỉ có hiệu lực trong một số ngày nhất định. Trong Báo giá, bạn có thể cập nhật Ngày hết hạn một cách thủ công. Theo mặc định, Ngày hết hạn được tự động thiết lập là 30 ngày kể từ Ngày lập Báo giá. Bạn có thể thay đổi số ngày trong trường này tùy theo trường hợp kinh doanh của mình.

## 3. Requirement checks (Kiểm tra yêu cầu)
### 3.1 Sales Order Required (Yêu cầu Đơn bán hàng)

Nếu bạn muốn việc tạo Đơn bán hàng là bắt buộc trước khi tạo Hóa đơn, bạn nên đặt trường 'Sales Order Required' thành 'Yes'. Theo mặc định, tùy chọn này sẽ là 'No'.

Cấu hình này có thể được ghi đè cho một khách hàng cụ thể bằng cách bật hộp kiểm "Allow Sales Invoice Creation Without Sales Order" trong danh mục Khách hàng.

<img alt="Sales Order Required" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/so-required.png">

### 3.2 Delivery Note Required (Yêu cầu Phiếu giao hàng)

Để việc tạo Phiếu giao hàng là bắt buộc trước khi tạo Hóa đơn, bạn nên đặt trường này thành 'Yes'. Theo mặc định, tùy chọn này sẽ là 'No'.

Cấu hình này có thể được ghi đè cho một khách hàng cụ thể bằng cách bật hộp kiểm "Allow Sales Invoice Creation Without Delivery Note" trong danh mục Khách hàng.

<img alt="Delivery Note Required" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/dn-required.png">

### 3.3 Delivery Note Cutoff Date (Ngày chốt Phiếu giao hàng)

Trong phiên bản v16, bạn có thể thiết lập ngày chốt (Cutoff date) cho Phiếu giao hàng. Điều này giúp kiểm soát việc tạo Phiếu giao hàng từ Đơn bán hàng, đảm bảo các giao dịch không vượt quá một mốc thời gian nhất định đã được quy định.

### 3.4 Sales Update Frequency (Tần suất cập nhật bán hàng)
Tần suất mà tiến độ dự án và chi tiết giao dịch của công ty sẽ được cập nhật. Theo mặc định là cho Mỗi giao dịch, bạn cũng có thể thiết lập là Hàng ngày hoặc Hàng tháng nếu bạn có nhiều giao dịch mỗi ngày.

## 4. Other checks (Các kiểm tra khác)
### 4.1 Maintain Same Rate Throughout Sales Cycle (Duy trì cùng một Đơn giá trong suốt Chu kỳ bán hàng)

Nếu tùy chọn này được bật, ERPNext sẽ kiểm tra xem giá của một Mặt hàng có thay đổi trong Phiếu giao hàng hoặc Hóa đơn được tạo từ Đơn bán hàng hay không, tức là nó sẽ giúp bạn duy trì cùng một đơn giá trong suốt chu kỳ bán hàng.

Bạn có thể cấu hình hành động mà hệ thống nên thực hiện nếu không duy trì cùng một đơn giá trong trường "Action If Same Rate is Not Maintained":

- **Stop (Dừng)**: ERPNext sẽ ngăn bạn thay đổi giá bằng cách đưa ra thông báo lỗi kiểm tra.
- **Warn (Cảnh báo)**: Hệ thống sẽ cho phép bạn Lưu giao dịch nhưng sẽ cảnh báo bạn bằng một thông báo nếu đơn giá bị thay đổi.

### 4.2 Allow User to Edit Price List Rate in Transaction (Cho phép người dùng chỉnh sửa Đơn giá Bảng giá trong giao dịch)

Bảng mặt hàng trong các giao dịch bán hàng có một trường gọi là Đơn giá Bảng giá. Trường này theo mặc định là không thể chỉnh sửa trong tất cả các giao dịch bán hàng. Điều này nhằm đảm bảo rằng giá của một mặt hàng được lấy từ bản ghi Giá mặt hàng và người dùng không thể chỉnh sửa nó.

Nếu bạn cần Đơn giá được lấy từ Bảng giá của một mặt hàng có thể chỉnh sửa được, bạn nên bỏ chọn trường này.

### 4.3 Allow Item to be added multiple times in a transaction (Cho phép thêm Mặt hàng nhiều lần trong một giao dịch)
Đây là một kiểm tra điều kiện nhằm ngăn một mặt hàng bị thêm nhiều lần trong cùng một giao dịch khi không được chọn. Trong một số trường hợp, đây có thể là một nhu cầu rõ ràng, nếu vậy hãy tích vào hộp kiểm này.

### 4.4 Allow multiple Sales Orders against a Customer's Purchase Order (Cho phép nhiều Đơn bán hàng đối với một Đơn mua hàng của Khách hàng)
Tùy chọn này cho phép bạn tạo nhiều Đơn bán hàng khác nhau để đáp ứng cho cùng một Đơn mua hàng mà Khách hàng đã gửi.

### 4.5 Stock Reservation (Giữ hàng tồn kho)
Tính năng này cho phép hệ thống giữ lại một lượng Mặt hàng nhất định trong Kho dựa trên các Đơn bán hàng đã được Xác nhận. Điều này giúp đảm bảo rằng hàng hóa đã được cam kết cho khách hàng sẽ không bị bán cho người khác, giúp quản lý Tồn kho chính xác hơn trong quá trình lập kế hoạch bán hàng.

***

**Lưu ý về giao diện v16:**
- Trong danh mục Khách hàng, bạn sẽ thấy các nút bấm nhanh **SO/Quotation** để truy cập nhanh các Đơn bán hàng hoặc Báo giá liên quan của Khách hàng đó.