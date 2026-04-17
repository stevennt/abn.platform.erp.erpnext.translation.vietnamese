<!-- add-breadcrumbs -->
# Tích hợp Google Calendar

ERPNext cung cấp tính năng tích hợp với Google Calendar để tất cả người dùng có thể đồng bộ hóa các Sự kiện Google Calendar của họ với ERPNext.


## Cách thiết lập Tích hợp Google Calendar

Để cho phép đồng bộ hóa với Google Calendar, bạn cần ủy quyền cho ERPNext để lấy dữ liệu Sự kiện Lịch từ Google. Việc thiết lập Tích hợp Google Calendar được thực hiện theo các bước sau:

- Tạo Thông tin xác thực OAuth 2.0 thông qua [Google Settings](/docs/v13/user/manual/en/erpnext_integration/google_settings).
- Trong danh sách Google Calendar, nhấn vào New. Nhập Tên Lịch (Calendar Name) và Người dùng (User) mà bạn muốn đồng bộ, sau đó nhấn Lưu (Save).
- Tùy thuộc vào dữ liệu bạn muốn đồng bộ, bạn có thể chọn các tùy chọn sau:
  - Pull from Google Calendar - Đồng bộ tất cả sự kiện từ Google Calendar sang ERPNext.
  - Push to Google Calendar - Đồng bộ tất cả sự kiện từ ERPNext sang Google Calendar.
- Bây giờ, nhấn vào **Authorize Calendar Access** để ủy quyền cho ERPNext lấy dữ liệu Sự kiện Lịch từ Google.
- Sau khi đã được Ủy quyền (Authorized), bạn có thể đồng bộ hóa Sự kiện Google Calendar một cách thủ công hoặc để ERPNext tự động đồng bộ Danh bạ Google hàng ngày.

## Cách sử dụng Tích hợp Google Calendar

### Tạo một Sự kiện trong ERPNext
- Sau khi Tích hợp Google Calendar thành công, tất cả các sự kiện được tạo trong ERPNext sẽ được đồng bộ nếu tùy chọn `Push to Google Calendar` được chọn.
- Tạo một Sự kiện trong ERPNext
  <img class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/erpnext_integrations/erpnext-gc.gif">
- Xóa một Sự kiện trong ERPNext
  <img class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/erpnext_integrations/gc-erpnext.gif">

### Đồng bộ hóa Sự kiện từ Google Calendar
- Sau khi Tích hợp Google Calendar thành công, tất cả các sự kiện trong Google Calendar sẽ được đồng bộ nếu tùy chọn `Pull from Google Calendar` được chọn.
- Đồng bộ hóa Sự kiện từ Google Calendar sang ERPNext
  <img class="screenshot" src="https://docs.erpnext.com/docs/v13/assets/img/erpnext_integrations/gc-sync.gif">