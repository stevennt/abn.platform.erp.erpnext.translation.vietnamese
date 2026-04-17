<!-- add-breadcrumbs -->
# Chấm công tự động

> Được giới thiệu trong Phiên bản 12

Chấm công tự động ghi nhận việc chấm công cho các Nhân viên được phân công vào một ca làm việc dựa trên các bản ghi trong tài liệu 'Employee Checkin' và [Auto Attendance Settings](/docs/v13/user/manual/en/human-resources/shift-management#25-auto-attendance-settings) của ca làm việc đó.

Việc Chấm công tự động cho mỗi bản ghi 'Shift Type' sẽ được thử thực hiện mỗi giờ một lần. Bạn cũng có thể kích hoạt chấm công tự động một cách thủ công cho một loại ca làm việc duy nhất bằng cách nhấn nút 'Mark Auto Attendance' trong tài liệu Shift Type.

> Lưu ý: [Shift Type](/docs/v13/user/manual/en/human-resources/shift-management#shift-type) cần được thiết lập và phân công cho Nhân viên trước khi tạo các bản ghi 'Employee Checkin'. Việc chấm công sẽ chỉ được thực hiện bởi Chấm công tự động đối với các bản ghi check-in được tạo sau khi đã thiết lập và phân công Nhân viên vào loại ca làm việc của họ.

## Các bước thiết lập Chấm công tự động
Bạn có thể thiết lập Chấm công tự động bằng cách làm theo các bước dưới đây:

1. [Thiết lập Shift Type với tính năng Chấm công tự động được bật](#1-define-shift-type-with-auto-attendance-enabled)
1. [Phân công các ca làm việc này cho Nhân viên](#2-assign-these-shifts-to-employees)
1. [Thiết lập trường Attendance Device ID trong Nhân viên](#3-setup-attendance-device-id-field-in-employee)

### 1. Thiết lập Shift Type với tính năng Chấm công tự động được bật
Để có thể chấm công từ danh sách nhật ký Check-in/Check-out, bạn cần thiết lập các ca làm việc có bật trường "Enable Auto Attendance". Sau khi bạn bật tùy chọn này, bạn sẽ thấy phần "Auto Attendance Settings". Vui lòng điền phần này theo yêu cầu của bạn cho ca làm việc đó.

Vui lòng tham khảo liên kết sau để biết thêm về từng trường trong phần cài đặt Auto Attendance: [Auto Attendance Settings](/docs/v13/user/manual/en/human-resources/shift-management#25-auto-attendance-settings)

### 2. Phân công các ca làm việc này cho Nhân viên
Sau khi bạn đã thiết lập một ca làm việc, bạn sẽ phải phân công ca này cho các nhân viên.

Bạn có thể phân công ca này cho một nhân viên bằng một trong hai phương pháp sau:

1. Sử dụng Shift Assignment

    Bạn có thể sử dụng [Shift Assignment](/docs/v13/user/manual/en/human-resources/shift-management#shift-assignment) để phân công ca làm việc cho nhân viên theo khoảng thời gian từ ngày này đến ngày kia.

1. Sử dụng trường Default Shift trong Nhân viên

    Đôi khi bạn muốn phân công một ca làm việc cho một nhân viên cho tất cả các ngày.

    Bạn có thể làm điều này bằng cách thiết lập trường sau trong Nhân viên: `Employee > ATTENDANCE AND LEAVE DETAILS > Default Shift`

> Lưu ý: Việc thiết lập Shift Assignment sẽ được ưu tiên hơn so với ca làm việc mặc định. Nghĩa là khi ca làm việc mặc định được thiết lập, ca đó sẽ được coi là ca làm việc của nhân viên cho tất cả các ngày nếu không có Shift Assignment.


### 3. Thiết lập trường Attendance Device ID trong Nhân viên
Các hệ thống sinh trắc học thường có ID riêng cho nhân viên. Tuy nhiên, Employee Checkin trong ERPNext cần được ánh xạ với một nhân viên.

Để ánh xạ nhân viên với ID của họ trong hệ thống sinh trắc học, bạn cần thiết lập trường sau với giá trị phù hợp: `Employee > ATTENDANCE AND LEAVE DETAILS > Attendance Device ID (Biometric/RF tag ID)`

Sau khi hoàn tất các bước trên, giờ đây bạn có thể nhập Employee Checkin và bắt đầu tạo chấm công tự động.

Vui lòng tham khảo bài viết này để biết thêm về việc nhập Employee Checkin từ một hệ thống bên ngoài: [Integrating ERPNext With Biometric Attendance Devices](/docs/v13/user/manual/en/setting-up/articles/integrating-erpnext-with-biometric-attendance-devices)

## Dưới đây là một số câu hỏi thường gặp liên quan đến Chấm công tự động.

### Chấm công tự động xác định ca làm việc cho một Nhân viên như thế nào?
Ca làm việc của một Nhân viên vào một ngày cụ thể được xác định theo các bước sau:

- Ca làm việc được phân công cho Nhân viên vào ngày đã cho trong tài liệu 'Shift Assignment'.
- Nếu không tìm thấy thông tin trên, ca làm việc sẽ được lấy từ trường 'Default Shift' của tài liệu 'Employee'.
- Cuối cùng, nếu cũng không tìm thấy ca làm việc trong tài liệu 'Employee', thì giả định rằng Nhân viên đó không thuộc về bất kỳ ca làm việc nào vào ngày đã cho và không có lần chấm công nào được thực hiện bởi Chấm công tự động.

### Chấm công tự động xác định Danh sách ngày lễ cho một Nhân viên như thế nào?
Danh sách ngày lễ của một Nhân viên được xác định theo các bước sau:

- Nếu 'Shift Type' được xác định của Nhân viên có danh sách ngày lễ, thì danh sách này sẽ được sử dụng.
- Nếu không, danh sách ngày lễ sẽ được lấy từ trường 'Holiday List' trong tài liệu Nhân viên hoặc từ trường 'Default Holiday List' của tài liệu Công ty, theo thứ tự đó.

Lưu ý: Danh sách ngày lễ cần được Chấm công tự động xác định chính xác để không đánh dấu Vắng mặt cho Nhân viên vào các ngày lễ.