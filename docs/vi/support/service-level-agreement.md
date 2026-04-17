<!-- add-breadcrumbs -->
# Thỏa thuận mức độ dịch vụ

**Thỏa thuận mức độ dịch vụ (SLA) là một hợp đồng giữa nhà cung cấp dịch vụ (nội bộ hoặc bên ngoài) và người dùng cuối về mức độ dịch vụ được mong đợi từ nhà cung cấp dịch vụ.**

SLA dựa trên kết quả đầu ra, mục đích của nó cụ thể là để xác định khung thời gian mà Khách hàng sẽ nhận được dịch vụ. SLA không xác định cách thức dịch vụ đó được cung cấp hoặc thực hiện.

Để truy cập danh sách Thỏa thuận mức độ dịch vụ, hãy đi tới:
> Trang chủ > Hỗ trợ > Thỏa thuận mức độ dịch vụ > Thỏa thuận mức độ dịch vụ

## 1. Điều kiện tiên quyết

Trước khi tạo và sử dụng Thỏa thuận mức độ dịch vụ, bạn nên tạo/cập nhật các mục sau trước:

* [Danh sách ngày nghỉ](/docs/v13/user/manual/en/human-resources/holiday-list)

* Bật **Track Service Level Agreement** trong Cài đặt hỗ trợ

    ![Service Level Agreement](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/sla-setting.png)

## 2. Cách tạo Thỏa thuận mức độ dịch vụ
1. Đi tới danh sách Thỏa thuận mức độ dịch vụ, nhấn vào Mới.
1. Nhập tên cho Mức độ dịch vụ.
1. Chọn một nhóm Nhân viên sẽ xử lý một Mức độ dịch vụ cụ thể.
1. Thiết lập Danh sách ngày nghỉ. Thỏa thuận mức độ dịch vụ sẽ không được áp dụng vào những ngày được đề cập trong Danh sách ngày nghỉ.
1. 'Enable' (Bật) xác định xem Thỏa thuận mức độ dịch vụ được bật hay tắt.
1. Tích vào 'Default Service Level Agreement' (Thỏa thuận mức độ dịch vụ mặc định) sẽ áp dụng SLA này cho một khách hàng nếu họ không được chỉ định một SLA cụ thể nào khác.
1. Entity Type (Loại thực thể): Thỏa thuận mức độ dịch vụ có thể được chỉ định cho Khách hàng/Nhóm khách hàng/Khu vực, cho phép bạn áp dụng Thỏa thuận mức độ dịch vụ dựa trên các yếu tố này.
1. Entity (Thực thể): Chọn Khách hàng/Nhóm khách hàng/Khu vực cụ thể.
1. Start / End Date (Ngày bắt đầu / Ngày kết thúc): Xác định hiệu lực của thỏa thuận.
1. Priorities (Mức độ ưu tiên): Bạn có thể thiết lập nhiều Mức độ ưu tiên của Vấn đề cùng với Thời gian phản hồi và Thời gian giải quyết (tính bằng giờ và phút).

    ![Service Level](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/priorities.png)
1. Default Priority (Mức độ ưu tiên mặc định): Mức độ ưu tiên được chọn trong bảng Priorities sẽ được áp dụng trong Thỏa thuận mức độ dịch vụ.
1. Support Hours (Giờ hỗ trợ): Bao gồm các Ngày trong tuần mà dịch vụ Hỗ trợ được cung cấp. Có Giờ bắt đầu và Giờ kết thúc của ngày làm việc.

    ![SLA Support Hours](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/sla-support-hours.png)
1. Lưu.

    ![SLA](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/sla.png)

## 3. Các tính năng
### 3.1 Áp dụng cho các Vấn đề mới

Sau khi một SLA được Lưu, nó sẽ được áp dụng cho các Vấn đề được tạo bởi Khách hàng/Khu vực theo tùy chọn bạn đã chọn trong 'Entity Type'.

![SLA in Issue](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/sla-entity-type.png)

### 3.2 Đặt lại (Resetting) một SLA
Một SLA cũng có thể được đặt lại cho đến khi thời gian không bị quá hạn. Ví dụ: nếu SLA là 3 ngày, bạn chỉ có thể đặt lại SLA trong vòng 3 ngày kể từ khi Vấn đề được tạo. Sau đó, Mức độ dịch vụ sẽ hiển thị là thất bại (failed).

![SLA Issue](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/reset-sla.gif)

### 3.3 Thời gian phản hồi / giải quyết trong Vấn đề
Thời gian để phản hồi một Vấn đề và thời gian để giải quyết sẽ được hiển thị:
    ![SLA in Issue](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/sla-in-issue.png)

Các thời gian này dựa trên khung thời gian được thiết lập trong trường 'Priority' (Mức độ ưu tiên) trong bảng Priorities của Mức độ dịch vụ.


### 3.4 Tạm dừng SLA theo Trạng thái
Từ phiên bản 13 trở đi, ERPNext cho phép bạn tạm dừng SLA đối với các vấn đề khi bạn đang chờ đợi một sự kiện nào đó xảy ra. Bạn có thể làm điều này bằng cách chọn một trạng thái được cấu hình trong bảng "Pause SLA On" (Tạm dừng SLA khi) này.

* Thiết lập các trạng thái mà bạn muốn tạm dừng SLA trong tài liệu SLA. Bạn cũng có thể thêm các trạng thái tùy chỉnh tại đây.
    <img class="screenshot" alt="Service Level" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/pause-sla.png">
* Khi trạng thái được chuyển sang bất kỳ trạng thái nào ở trên, các trường giải quyết và phản hồi sẽ được bỏ trống và các chỉ số trên trang tổng quan sẽ thay đổi thành:
    <img class="screenshot" alt="Service Level" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/hold-indicator.png">
* Khi trạng thái của vấn đề chuyển trở lại trạng thái không tạm dừng (trạng thái không được cấu hình trong bảng "Pause SLA On"), trường **Total Hold time** (Tổng thời gian tạm dừng) sẽ được thiết lập trong tài liệu Vấn đề của bạn.
    <img class="screenshot" alt="Service Level" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/support/total-hold-time.png">
Thời gian Phản hồi và Giải quyết sẽ được tính toán lại bằng cách cộng thêm thời gian tạm dừng, từ đó khởi động lại bộ đếm thời gian SLA của bạn.

> Lưu ý: DocType Service Level đã bị loại bỏ trong phiên bản 13 và tất cả các chức năng hiện chỉ được xử lý thông qua DocType Thỏa thuận mức độ dịch vụ.

{next}