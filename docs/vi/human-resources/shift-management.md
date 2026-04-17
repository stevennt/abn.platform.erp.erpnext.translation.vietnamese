<!-- add-breadcrumbs -->
# Quản lý Ca làm việc

Phần Quản lý Ca làm việc của Nhân sự giúp Tổ chức của bạn quản lý các ca làm việc của nhân viên.

Để sử dụng Quản lý Ca làm việc trong ERPNext,

  1. Thiết lập Loại ca làm việc.
  2. Nhập Yêu cầu ca làm việc.
  3. Xem và Quản lý Phân công ca làm việc.

## 1. Loại ca làm việc

Tài liệu Loại ca làm việc cho phép bạn xác định các loại Ca làm việc khác nhau trong Tổ chức của mình và thiết lập chế độ tự động chấm công cho ca đó. Chế độ tự động chấm công sẽ đánh dấu chuyên cần dựa trên 'Employee Checkin' (Nhân viên điểm danh) cho các Nhân viên được phân công vào ca.

Để truy cập Loại ca làm việc, hãy đi đến:
> Home > Human Resources > Shift Management > Shift Type

1. Đi đến Danh sách Loại ca làm việc, Nhấp vào Mới.
2. Nhập Tên, Giờ bắt đầu và Giờ kết thúc
3. Lưu
<img class="screenshot" alt="Shift Type" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/new-shift-type.png">

## 2. Các tính năng

Ngoài việc xác định các ca làm việc khác nhau trong tổ chức, tài liệu Loại ca làm việc còn có cài đặt cho chế độ tự động chấm công. Chế độ tự động chấm công sẽ đánh dấu chuyên cần cho các nhân viên được phân công vào ca này dựa trên các bản ghi trong tài liệu 'Employee Checkin'. Việc Tự động chấm công cho tất cả các bản ghi loại ca làm việc được cố gắng thực hiện mỗi giờ một lần. Bạn cũng có thể kích hoạt chế độ tự động chấm công một cách thủ công cho một loại ca làm việc duy nhất bằng cách nhấn nút 'Mark Attendance' (Đánh dấu chuyên cần) trong tài liệu loại ca làm việc.
<img class="screenshot" alt="Shift Type" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/shift-type.png">

### 2.1 Giờ bắt đầu
Thời gian trong ngày khi ca làm việc này bắt đầu. Thời gian cần được nhập theo định dạng 24 giờ.

### 2.2 Giờ kết thúc
Thời gian trong ngày khi ca làm việc này kết thúc. Thời gian cần được nhập theo định dạng 24 giờ.

> Lưu ý: Đối với các trường hợp 'Giờ kết thúc' nhỏ hơn 'Giờ bắt đầu', ca làm việc được coi là ca đêm bắt đầu vào một ngày lịch này và kết thúc vào ngày lịch tiếp theo.

### 2.3 Danh sách ngày lễ
Các Ngày lễ áp dụng cho ca làm việc này có thể được chọn tại đây. Nếu để trống, danh sách ngày lễ mặc định từ tài liệu nhân viên hoặc công ty sẽ được tính đến.

### 2.4 Bật Tự động chấm công
Bạn có thể sử dụng tùy chọn này để bật việc đánh dấu chuyên cần cho các nhân viên được phân công vào ca này dựa trên các bản ghi 'Employee Checkin' của họ.

### 2.5 Cài đặt Tự động chấm công
Bạn có thể sử dụng các cài đặt sau để cấu hình Tự động chấm công theo yêu cầu của mình.

### Xác định Check-in và Check-out
Employee Check-in có thể không phải lúc nào cũng có loại nhật ký IN/OUT (Vào/Ra). Đối với các tình huống như vậy, bạn có thể sử dụng tùy chọn này để nhận được kết quả phù hợp từ hệ thống tự động chấm công.

1. Các bản ghi xen kẽ là IN và OUT trong cùng một ca làm việc:
	- Bản ghi đầu tiên được coi là IN, tiếp theo là OUT, bản ghi tiếp theo là IN, và cứ tiếp tục như vậy.
2. Dựa nghiêm ngặt vào Loại nhật ký trong Employee Checkin:
	- Việc check-in được xác định là IN hoặc OUT dựa nghiêm ngặt vào 'Log Type' trong bản ghi Employee Checkin.

### Tính toán Giờ làm việc Dựa trên
Giờ làm việc có thể được tính bằng cách bao gồm các giờ nghỉ giữa ca hoặc loại trừ các giờ nghỉ.

Điều này có thể được cấu hình bằng các tùy chọn sau:

1. Check-in đầu tiên và Check-out cuối cùng:
	- Chọn tùy chọn này sẽ tính toán giờ làm việc bằng cách xem xét bản ghi Employee Checkin IN đầu tiên và OUT cuối cùng trong ca làm việc.
	- Trong trường hợp IN/OUT được xác định bằng các bản ghi xen kẽ, thì bản ghi Employee Checkin đầu tiên được coi là IN và bản ghi Employee Checkin cuối cùng được coi là OUT cho mục đích tính toán giờ làm việc.
2. Mọi lần Check-in và Check-out hợp lệ:
	- Chọn tùy chọn này sẽ loại trừ thời gian mà Nhân viên đã check-out.
	- Nghĩa là, chỉ thời gian mà nhân viên đang check-in mới được tính là giờ làm việc.

### Bắt đầu check-in trước giờ bắt đầu ca
Thông thường nhân viên sẽ check-in vài phút trước giờ bắt đầu ca làm việc. Để coi các lần check-in này là một phần của ca làm việc trong quá trình tính toán chuyên cần, bạn có thể thiết lập giá trị này một cách phù hợp.

### Cho phép check-out sau giờ kết thúc ca
Thông thường nhân viên sẽ check-out sau giờ kết thúc ca làm việc. Để coi các lần check-out này là một phần của ca làm việc trong quá trình tính toán chuyên cần, bạn có thể thiết lập giá trị này một cách phù hợp.

### Ngưỡng Giờ làm việc cho Nửa ngày
Nếu số giờ làm việc thực tế ít hơn giá trị được cung cấp trong trường hợp này, thì chuyên cần của nhân viên sẽ được đánh dấu là 'Nửa ngày'. Nếu bạn không bao giờ muốn đánh dấu Nửa ngày dựa trên giờ làm việc, bạn nên đặt giá trị này bằng không.

### Ngưỡng Giờ làm việc cho Vắng mặt
Nếu số giờ làm việc thực tế ít hơn giá trị được cung cấp trong trường hợp này, thì chuyên cần của nhân viên sẽ được đánh dấu là 'Vắng mặt'. Nếu bạn không bao giờ muốn đánh dấu Vắng mặt dựa trên giờ làm việc, bạn nên đặt giá trị này bằng không.

### Xử lý Chuyên cần Sau
Ngày mà chế độ 'Tự động chấm công' bắt đầu đánh dấu chuyên cần. Bạn nên đặt nó vào một ngày mà sau đó bạn đã có các bản ghi Employee Checkin cho ca làm việc này.

### Đồng bộ hóa Checkin lần cuối
Đây là thời điểm mà chuyên cần được đánh dấu dựa trên các bản ghi Employee Checkin. Bạn nên đặt nó vào một ngày và giờ mà tại đó Employee Checkin đã được đồng bộ hóa. Nếu không, một nhân viên có thể bị đánh dấu là vắng mặt do thiếu các bản ghi check-in.

# Yêu cầu ca làm việc


## 1. Điều kiện tiên quyết
Để tạo một Yêu cầu ca làm việc, các mục sau cần được tạo trước:

* [Nhân viên](/docs/v13/user/manual/en/human-resources/employee)
* [Loại ca làm việc](docs/user/manual/en/human-resources/shift-management#1-shift-type)

Yêu cầu ca làm việc được nhân viên sử dụng để yêu cầu một Loại ca làm việc cụ thể.

Để tạo một Yêu cầu ca làm việc mới, hãy đi đến:
> Human Resources > Shift Management > Shift Request


1. Đi đến Danh sách Yêu cầu ca làm việc, Nhấp vào Mới.
1. Chọn Nhân viên và Loại ca làm việc.
1. Thiết lập thời gian ca làm việc bằng cách sử dụng Từ ngày và Đến ngày.
1. Chọn Người phê duyệt. Nếu người phê duyệt được chọn không có quyền truy cập vào tài liệu Yêu cầu ca làm việc, nó sẽ được chia sẻ với người phê duyệt với quyền "Xác nhận".
1. Lưu.

	<img class="screenshot" alt="Shift Request" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/shift-request.png">

# Phân công ca làm việc

* Một khi