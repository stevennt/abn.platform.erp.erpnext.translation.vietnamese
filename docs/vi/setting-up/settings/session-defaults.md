<!-- add-breadcrumbs -->
# Thiết lập mặc định của phiên (Session Defaults)

**Thiết lập mặc định của phiên là các giá trị mặc định có thể cấu hình được thiết lập trong suốt phiên làm việc của người dùng.**

Hãy xem xét một kịch bản khi bạn có 8 công ty được thiết lập trong tài khoản của mình và bạn phải chọn trường 'Công ty' mỗi khi tạo một Đơn bán hàng mới. Đây là một quá trình rất tốn thời gian khi bạn phải xử lý nhiều Đơn bán hàng hàng ngày.

## 1. Cách tạo Thiết lập mặc định của phiên

### 1.1 Thiết lập Cấu hình mặc định của phiên

1. Đi tới Thiết lập mặc định của phiên (Session Default Settings). Tại đó, bạn có thể thấy một bảng cho các Thiết lập mặc định của phiên.
2. Nhấp vào 'Thêm dòng' (Add Row).
3. Chọn DocType mà bạn muốn thiết lập Thiết lập mặc định của phiên.
4. Lưu.

    <img class="screenshot" alt="Session Defaults Settings" src="https://docs.erpnext.com/docs/v13/assets/img/setup/settings/session-defaults-settings.png">

### 1.2 Thiết lập các Giá trị mặc định của phiên

1. Nhấp vào menu 'Cài đặt' (Settings) trên thanh công cụ. Bạn sẽ tìm thấy tùy chọn 'Thiết lập mặc định của phiên' (Session Defaults) tại đó. Nhấp vào nó.

    <img class="screenshot" alt="Session Defaults Menu" src="https://docs.erpnext.com/docs/v13/assets/img/setup/settings/session-defaults-menu.png">

2. Một thông báo 'Thiết lập mặc định của phiên' (Session Defaults) sẽ xuất hiện. Hãy thiết lập các giá trị mặc định cho các trường tương ứng và Lưu.

    <img class="screenshot" alt="Session Defaults Prompt" src="https://docs.erpnext.com/docs/v13/assets/img/setup/settings/session-defaults-prompt.png">

Sau khi lưu, các giá trị mặc định sẽ được áp dụng ở mọi nơi.

Bạn có thể mở một Đơn bán hàng mới và kiểm tra. Trường công ty đã được thiết lập theo Công ty mặc định.

<img class="screenshot" alt="Session Defaults Set" src="https://docs.erpnext.com/docs/v13/assets/img/setup/settings/session-defaults-set-1.png">

Mở một Công việc (Task) mới. Trường 'Dự án' (Project) đã được thiết lập theo Dự án mặc định.

<img class="screenshot" alt="Session Default Set" src="https://docs.erpnext.com/docs/v13/assets/img/setup/settings/session-defaults-set-2.png">

Mở một báo cáo, ví dụ: Sổ cái (General Ledger). Bộ lọc Công ty đã được thiết lập theo Công ty mặc định.

<img class="screenshot" alt="Session Default " src="https://docs.erpnext.com/docs/v13/assets/img/setup/settings/session-defaults-set-3.png">

## 2. Các tính năng

### 2.1 Các giá trị mặc định được xóa khi đăng xuất

Các giá trị mặc định được thiết lập cho người dùng cụ thể đó trong phiên làm việc đang diễn ra. Sau khi đăng xuất, các giá trị mặc định này sẽ được xóa sạch.

### 2.2 Hiển thị nút 'Cài đặt' (Settings)

Nút Cài đặt chỉ hiển thị đối với Quản trị viên hệ thống (System Manager) hoặc người có quyền truy cập vào 'Thiết lập mặc định của phiên' (Session Default Settings). Nút này sẽ dẫn bạn đến Thiết lập mặc định của phiên, nơi bạn có thể thêm hoặc xóa các loại tài liệu (document types) mà bạn muốn thiết lập Thiết lập mặc định của phiên.

<img class="screenshot" alt="Session Defaults Prompt" src="https://docs.erpnext.com/docs/v13/assets/img/setup/settings/settings-button.png">

### 3. Các chủ đề liên quan
1. [Thiết lập mặc định toàn cầu (Global Defaults)](/docs/v13/user/manual/en/setting-up/settings/global-defaults)
1. [Cài đặt hệ thống (System Settings)](/docs/v13/user/manual/en/setting-up/settings/system-settings)