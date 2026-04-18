<!-- add-breadcrumbs -->
# Dự án

**Một Dự án là một phần việc được lập kế hoạch nhằm mục đích tìm kiếm thông tin về một thứ gì đó, tạo ra thứ gì đó mới, hoặc cải thiện một thứ gì đó.**

Trong ERPNext, quản lý dự án được điều hành theo nhiệm vụ. Bạn có thể tạo một Dự án và chia nhỏ nó thành nhiều Nhiệm vụ.

Một Dự án có phạm vi rộng, do đó có thể được chia thành các nhiệm vụ. Hãy coi việc phát triển một chiếc điện thoại thông minh mới cho năm tới là một Dự án. Khi đó, các công việc như thiết kế, làm mẫu, thử nghiệm, bàn giao, v.v. sẽ trở thành các nhiệm vụ trong dự án.

Trong khi mỗi nhiệm vụ trong một Dự án có thể được giao cho một cá nhân hoặc một nhóm cá nhân, việc phân công cũng có thể được thực hiện ở cấp độ dự án.

Các Nhiệm vụ này có thể được tạo trực tiếp từ chính Dự án hoặc một [Task](tasks.html.md) cũng có thể được tạo riêng biệt.

Để truy cập Dự án, hãy đi đến:

> Home > Projects > Projects > Project

<img class="screenshot" alt="Project" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/project/projects-project-intro.png">

## 1. Cách tạo một Dự án

  1. Đi đến danh sách Dự án và nhấn vào Mới.
  2. Thêm các chi tiết sau:
      * **Project Name**: Tiêu đề của Dự án.
      * **Status**: Trạng thái mặc định của Dự án sẽ là 'Open' (Mở), sau đó có thể được đổi thành 'Completed' (Hoàn thành) hoặc 'Cancelled' (Hủy).
      * **Expected End Date**: Nhập ngày mà bạn dự kiến hoàn thành dự án.
  3. Lưu.

### 1.1 Các tùy chọn bổ sung khi tạo Dự án

  1. **From Template**: Nếu bạn đã có [Project Template](project-template.md) sẵn có, bạn có thể chọn tạo dự án của mình bằng mẫu này.
  2. **Expected Start Date**: Nếu bạn đã có mốc thời gian cố định cho dự án, bạn có thể xác định cả Ngày bắt đầu dự kiến và Ngày kết thúc dự kiến trong biểu mẫu.
  3. **Project Type**: Bạn có thể phân loại các dự án của mình thành các [loại](project-type.md) khác nhau, ví dụ: Nội bộ hoặc Bên ngoài.
  4. **Priority**: Bạn có thể chọn mức độ ưu tiên của Dự án dựa trên mức độ quan trọng của nó. Bạn cũng có thể thêm nhiều mức độ ưu tiên khác.
  5. **Department**: Nếu dự án thuộc về hoặc được sở hữu bởi một [Department](../human-resources/department.md) trong tổ chức, bạn có thể thêm thông tin đó tại đây.
  6. **Is Active**: Một tab Có/Không, cho phép bạn thay đổi trạng thái hoạt động của dự án ở bất kỳ giai đoạn nào sau đó.
  7. **Completion Method**: Bạn có thể theo dõi % hoàn thành của dự án dựa trên một trong ba phương pháp: **Manual (Thủ công), Task Completion (Hoàn thành nhiệm vụ), Task Progress (Tiến độ nhiệm vụ) và Task Weight (Trọng số nhiệm vụ)**.

  <img class="screenshot" alt="Project 2" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/project/project-proj.png">

  Một số ví dụ về cách tính Phần trăm Hoàn thành dựa trên các Nhiệm vụ:

  | Project     | Activity     | % Progress     | Weight     | Status     |
  |:-----------:|:------------:|:--------------:|:----------:|:----------:|
  | SC001       | Build        | 100            | 0.4        | Completed  |
  | SC001       | Operate      | 100            | 0.2        | Completed  |
  | SC001       | Transfer     | 50             | 0.2        | Open       |

  | Method              | Formula                                            | Calculation                        | % Task Completed     |
  |:-------------------:|:--------------------------------------------------:|:----------------------------------:|:--------------------:|
  | **Manual**          | -                                                  |-                                   | Manual               |
  | **Task Completion** | Nhiệm vụ đã hoàn thành / Tổng số Nhiệm vụ          | 2/3                                | 66.66                |
  | **Task Progress**   | Tổng % Tiến độ của tất cả Nhiệm vụ / Tổng số Nhiệm vụ | (100+100+50)/3                     | 83.33                |
  | **Task Weight**     | Tổng của (Trọng số nhiệm vụ * % Tiến độ)           | (0.4 * 100 + 0.2 * 100 + 0.2 * 100)| 70                   |


**Lưu ý:** Nếu tổng trọng số của các Nhiệm vụ không phải là 100, thì kết quả tính toán sẽ được chia cho tổng trọng số.
Ví dụ, nếu tổng trọng số của các nhiệm vụ là 70, thì phần trăm hoàn thành = (70/0.8)% = 87.5%.


## 2. Các tính năng

### 2.1. Chi tiết Khách hàng, Người dùng và Ghi chú

* **Customer**: Nếu một Dự án đang được thực hiện cho một Khách hàng cụ thể, các chi tiết có thể được nhập vào đây.
* **Sales Order**: Nếu một Dự án dựa trên một [Sales Order](../selling/sales-order.md) từ Khách hàng, bạn có thể lấy thông tin tại đây. Điều này cho phép bạn cập nhật cho Khách hàng về Tiến độ của dự án theo Đơn bán hàng đã phát hành.
* **Users**: Bạn có thể thêm bất kỳ [website user](../setting-up/users-and-permissions/adding-users.md) nào để cấp quyền truy cập vào Dự án này. Ví dụ: bạn có thể thêm khách hàng của mình làm Website User, để họ có quyền truy cập vào dự án nhằm theo dõi tiến độ và/hoặc đưa ra bất kỳ ý kiến/nhận xét nào. Tương tự, một Nhà cung cấp hoặc một Nhân viên hợp đồng/Freelancer tham gia vào Dự án cũng có thể được thêm vào dưới dạng Người dùng.

  Hơn nữa, bạn cũng có thể mở rộng cửa sổ và chọn nếu bạn muốn gửi Email Chào mừng đến bất kỳ người dùng cụ thể nào hoặc cấp cho họ quyền Xem Đính kèm.

  Bạn có thể tìm hiểu thêm về việc cho phép người dùng xem dự án [tại đây](project-customer-portal.md).

* **Notes**: Bạn có thể thêm bất kỳ ghi chú bổ sung nào vào dự án.

  <img class="screenshot" alt="Project - Costing" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/project/projects-customer-users-notes.png">

### 2.2. Ngày bắt đầu và Ngày kết thúc

* **Actual Start Date**: Dựa trên Ngày bắt đầu thực tế của dự án, được theo dõi qua Timesheets, Ngày và Giờ bắt đầu thực tế của Dự án sẽ được ghi lại tự động.
* **Actual End Date**: Dựa trên Ngày kết thúc thực tế của dự án, được theo dõi qua lần cập nhật cuối cùng của Timesheet, Ngày và Giờ kết thúc thực tế của Dự án sẽ được ghi lại tự động. Để biết thêm về Timesheets, [nhấn vào đây](timesheets.md).

  <img class="screenshot" alt="Project - Costing" src="{{do