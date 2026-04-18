<!-- add-breadcrumbs -->
# Danh sách ngày lễ

**Danh sách ngày lễ là một danh sách chứa các ngày nghỉ lễ.**

Hầu hết các tổ chức đều có một Danh sách ngày lễ tiêu chuẩn cho nhân viên của họ. Tuy nhiên, một số tổ chức có thể có các danh sách ngày lễ khác nhau dựa trên Địa điểm hoặc Phòng ban khác nhau. Trong ERPNext, bạn có thể cấu hình nhiều Danh sách ngày lễ và chỉ định chúng cho nhân viên dựa trên yêu cầu của mình.

Để truy cập Danh sách ngày lễ, hãy đi đến:

> Home > Human Resources > Leaves > Holiday List

## 1. Cách tạo Danh sách ngày lễ

1. Đi đến Danh sách ngày lễ, nhấn vào **Mới (New)**.
2. Nhập Tên Danh sách ngày lễ. Tên này có thể dựa trên Năm tài chính hoặc Địa điểm hoặc Phòng ban tùy theo yêu cầu.
3. Chọn Ngày bắt đầu và Ngày kết thúc cho Danh sách ngày lễ.

    <img class="screenshot" alt="Holiday List" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/holiday-list-1.png">

## 2. Các tính năng

Một số tính năng bổ sung trong Danh sách ngày lễ như sau:

### 2.1 Thêm ngày nghỉ hàng tuần

Bạn có thể nhanh chóng thêm các ngày nghỉ hàng tuần trong Danh sách ngày lễ như sau:

1. Trong phần 'Add Weekly Holidays', chọn ngày trong trường Weekly Off.
2. Nhấn vào nút 'Add to Holidays'.
3. **Lưu (Save)**.

Sau khi các ngày nghỉ hàng tuần được thêm vào, chúng sẽ được hiển thị trong bảng Holidays.

> **Lưu ý:** Bạn có thể thêm nhiều ngày trong phần Weekly Off.

<img class="screenshot" alt="Holiday List" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/holiday-list-2.gif">

Bạn cũng có thể thêm các ngày cụ thể (như ngày lễ hội) một cách thủ công bằng cách nhấp vào tùy chọn 'Add row' trong bảng Holidays.

<img class="screenshot" alt="Holiday List" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/holiday-list-3.png">

> **Lưu ý:** Mỗi khi một ngày lễ mới được cập nhật trong bảng Holidays, trường Tổng số ngày lễ (Total Holidays) sẽ được cập nhật.

### 2.2 Danh sách ngày lễ trong Công ty

Bạn có thể thiết lập một Danh sách ngày lễ mặc định ở cấp công ty trong danh mục Công ty tại trường 'Default Holiday List'.

<img class="screenshot" alt="Holiday List" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/default-holiday-list-company.png">

### 2.3 Danh sách ngày lễ trong Nhân viên

Nếu bạn đã tạo nhiều Danh sách ngày lễ, hãy chọn một Danh sách ngày lễ cụ thể cho một Nhân viên trong danh mục Nhân viên tương ứng.

Khi một Nhân viên đăng ký Nghỉ phép, những ngày được ghi trong Danh sách ngày lễ sẽ không được tính, vì chúng đã là ngày lễ.

> **Lưu ý:** Nếu bạn đã chỉ định một Danh sách ngày lễ trong danh mục Nhân viên, thì Danh sách ngày lễ đó sẽ được ưu tiên so với Danh sách ngày lễ mặc định của Công ty.

Bạn có thể tạo bao nhiêu danh sách ngày lễ tùy thích. Ví dụ, nếu bạn có một nhà máy, bạn có thể có một danh sách cho công nhân nhà máy và một danh sách khác cho nhân viên văn phòng. Bạn có thể quản lý giữa nhiều danh sách bằng cách liên kết một Danh sách ngày lễ với Nhân viên tương ứng.

### 2.4 Danh sách ngày lễ trong Trạm làm việc

Bạn cũng có thể thiết lập một Danh sách ngày lễ ở cấp trạm làm việc như được hiển thị trong ảnh chụp màn hình dưới đây.

<img class="screenshot" alt="Holiday List" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/holiday-list-workstation.png">

Các ngày trong Danh sách ngày lễ được gắn trong danh mục [Workstation](/docs/v16/user/manual/en/manufacturing/workstation) sẽ được coi là những ngày mà Trạm làm việc sẽ đóng cửa.

## 3. Các chủ đề liên quan

1. [Leave Allocation](/docs/v16/user/manual/en/human-resources/leave-allocation)
1. [Leave Period](/docs/v16/user/manual/en/human-resources/leave-period)
1. [Leave Policy](/docs/v16/user/manual/en/human-resources/leave-policy)
1. [HR Settings](/docs/v16/user/manual/en/human-resources/hr-settings)