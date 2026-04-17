---
title: Cuộc hẹn
add_breadcrumbs: 1
show_sidebar: 0

metatags:
 description: Lập lịch Cuộc hẹn cho CRM trong ERPNext
 keywords: Lập lịch Cuộc hẹn , CRM, frappe, erpnext new features, erp, open source erp, free erp, security
---

# Cuộc hẹn

**Một cuộc hẹn là một cuộc họp được sắp xếp trước giữa một Khách hàng tiềm năng và một Nhân viên của Công ty bạn.**

Loại DocType Cuộc hẹn có thể được sử dụng để lập lịch và quản lý tương tác với một [Khách hàng tiềm năng](/docs/v16/user/manual/CRM/lead) hoặc một [Cơ hội](/docs/v16/user/manual/CRM/opportunity).

Để truy cập danh sách Cuộc hẹn, hãy đi tới:
> Home > CRM > Sales Pipeline > Appointment

## 1. Điều kiện tiên quyết

1. [Cài đặt đặt lịch Cuộc hẹn](/docs/v16/user/manual/CRM/appointment-booking-settings)
2. [Danh sách ngày lễ](/docs/v16/user/manual/human-resources/holiday-list)
3. [Nhân viên](/docs/v16/user/manual/human-resources/employee)
4. [Khách hàng tiềm năng](/docs/v16/user/manual/CRM/lead)
5. [Email](/docs/v16/user/manual/setting-up/email/email-account)

## 2. Cách tạo một Cuộc hẹn

1. Đi tới danh sách Cuộc hẹn, nhấn vào New
2. Chọn thời gian đã lên lịch của cuộc hẹn
3. Nhập chi tiết khách hàng
4. Trong các tài liệu liên kết, nếu bạn đã tạo Khách hàng tiềm năng cho Khách hàng đó, bạn có thể thiết lập tại đây. Nếu không, hệ thống sẽ tự động tạo một Khách hàng tiềm năng mới với thông tin khách hàng từ bước trước.
5. Lưu.
 ![New Appointment](https://docs.erpnext.com/docs/v16/assets/img/crm/new-appointment.png)

### 2.1 Tạo cuộc hẹn qua website

Khách hàng/Khách hàng tiềm năng của bạn có thể tạo cuộc hẹn bằng cách sử dụng trang web `yoursitename.com/book_appointment`.

Đầu tiên, họ cần chọn ngày, giờ.
![Appointment Webform](https://docs.erpnext.com/docs/v16/assets/img/crm/appointment-webform.png)

Sau đó, thêm các chi tiết khác:
![Appointment Details](https://docs.erpnext.com/docs/v16/assets/img/crm/appointment-details.png)

Hệ thống sẽ khớp email của khách hàng với các khách hàng tiềm năng trong hệ thống và nếu tìm thấy một kết quả phù hợp, nó sẽ được liên kết với tài liệu.
Nếu không tìm thấy khách hàng tiềm năng nào, cuộc hẹn sẽ được đánh dấu là "Unverified" (Chưa xác minh) và một email sẽ được gửi đến khách hàng để xác nhận email của họ.

## 3. Các tính năng

### 3.1 Tự động phân bổ (Autoassign)

Các cuộc hẹn được tự động phân bổ cho nhân viên theo danh sách `Agents` trong [Cài đặt đặt lịch Cuộc hẹn](/docs/v16/user/manual/CRM/appointment-booking-settings). Nhân viên có số lượng cuộc hẹn được giao ít nhất trong ngày diễn ra cuộc hẹn và đang rảnh vào thời gian đã lên lịch sẽ được phân bổ cuộc hẹn đó.

### 3.2 Xác nhận qua Email

Nếu không có khách hàng tiềm năng nào khớp trong hệ thống của bạn, một email sẽ được gửi đến địa chỉ email trong cuộc hẹn để xác nhận xem địa chỉ email đó có hợp lệ hay không. Sau khi xác nhận, một Khách hàng tiềm năng mới cũng sẽ được tạo trong hệ thống cùng với Cuộc hẹn.

{next}