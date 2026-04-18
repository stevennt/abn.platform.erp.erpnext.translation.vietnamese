<!-- add-breadcrumbs -->
# Trạm làm việc

**Một Trạm làm việc lưu trữ thông tin liên quan đến nơi thực hiện các hoạt động của trạm làm việc.**

Dữ liệu liên quan đến chi phí vận hành, tiền thuê, tiền điện có thể được lưu trữ tại đây.

> Lưu ý: Một Công đoạn có thể diễn ra tại nhiều Trạm làm việc khác nhau.

> Một Công đoạn diễn ra tại một Trạm làm việc. Công đoạn là công việc được thực hiện và Trạm làm việc là nơi/máy móc nơi công việc đó được thực hiện. Ví dụ, nấu chảy là một Công đoạn có thể được thực hiện tại 10 Trạm làm việc khác nhau.

Để truy cập danh sách Trạm làm việc, hãy đi đến:

> Home > Manufacturing > Bill of Materials > Workstation

## 1. Cách tạo một Trạm làm việc
1. Đi đến danh sách Trạm làm việc, nhấn vào Mới.
1. Nhập tên cho Trạm làm việc.
1. Trong phần Chi phí vận hành (Operating Costs), nhập các thông tin sau nếu phù hợp:
 * Chi phí điện (Electricity Cost)
 * Chi phí thuê (Rent Cost)
 * Chi phí vật tư tiêu hao (Consumable Cost)
 * Tiền lương (Wages)
1. Lưu.

Tùy chọn, bạn có thể nhập mô tả cho Trạm làm việc.

![Workstation](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/workstation.png)

Có thể thêm các khung giờ mà Trạm làm việc sẽ hoạt động. Khi thêm một Danh sách ngày nghỉ (Holiday list), các ngày được liệt kê là ngày nghỉ sẽ không được tính là ngày làm việc của Trạm làm việc.
![Workstation Hours](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/workstation-hours.png)

Sau khi Lưu Trạm làm việc, các hành động sau có thể được thực hiện đối với nó:
![Workstation submit](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/workstation-submit.png)

## 2. Các tính năng
### 2.1 Năng lực sản xuất
Năng lực sản xuất là tổng số công việc có thể được thực hiện cùng một lúc tại trạm làm việc tương ứng.

<img class="screenshot" alt="Work Order" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/manufacturing/work_station_capacity.png">

### 2.2 Giờ làm việc
Trong bảng Giờ làm việc (Working Hours), bạn có thể thêm thời gian bắt đầu và kết thúc cho một Trạm làm việc. Ví dụ, một Trạm làm việc có thể hoạt động từ 9 giờ sáng đến 1 giờ chiều, sau đó từ 2 giờ chiều đến 5 giờ chiều. Bạn cũng có thể chỉ định giờ làm việc dựa trên các ca làm việc. Khi lập lịch cho một [Work Order](work-order.md), hệ thống sẽ kiểm tra tính khả dụng của Trạm làm việc dựa trên giờ làm việc đã chỉ định.

### 2.3 Danh sách ngày nghỉ
1. Có thể thêm một [Holiday List](../human-resources/holiday-list.md) để loại trừ việc tính các ngày này cho Trạm làm việc.


> Lưu ý: Bạn có thể bật làm thêm giờ cho một Trạm làm việc trong [Manufacturing Settings](manufacturing-settings.md)

## 3. Video
<div class="embed-container">
 <iframe src="https://www.youtube.com/embed/UVGfzwOOZC4?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
 </iframe>
</div>

## 4. Các chủ đề liên quan
1. [Bill Of Materials](bill-of-materials.md)
1. [Operation](operation.md)
1. [Routing](routing.md)
1. [Work Order](work-order.md)
1. [Job Card](job-card.md)

{next}