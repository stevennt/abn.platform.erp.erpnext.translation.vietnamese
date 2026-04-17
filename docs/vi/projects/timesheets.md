<!-- add-breadcrumbs -->
# Timesheet

**Timesheet là bản ghi về số giờ mà một nhân viên đã dành để hoàn thành mỗi nhiệm vụ.**

Timesheet cũng có thể được sử dụng để tính toán các khoản có thể lập hóa đơn cho nhân viên, để tính lương của họ, hoặc để theo dõi đóng góp của một nhân viên đối với một Dự án hoặc một Nhiệm vụ.

Trong ERPNext, một Timesheet có thể hiển thị tài khoản của một nhân viên cụ thể đang làm việc trên nhiều Nhiệm vụ hoặc Dự án dưới dạng bảng.

<img class="screenshot" alt="Timesheet" src="https://docs.erpnext.com/docs/v13/assets/img/project/projects-timesheet.png">

Để truy cập Timesheet, hãy đi tới,

> Trang chủ > Dự án > Theo dõi thời gian > Timesheet

## 1. Cách tạo một Timesheet

  1. Đi tới danh sách Timesheet và Nhấp vào Mới.
  2. Nhập tên Công ty và Mã nhân viên.
  3. Thêm các chi tiết sau vào trường 'Time Sheets'.
      * **Activity Type**: Thêm loại hoạt động mà Timesheet đã được tạo cho loại đó.
      * **From Time**: Nhập ngày và giờ bắt đầu làm việc.
      * **Hrs**: Nhập số giờ mà Timesheet này được tạo. Một Timesheet cũng có thể được sử dụng để theo dõi giờ làm việc trong nhiều ngày.
      * **Project**: Nếu Timesheet này cần được gắn với một Dự án cụ thể, bạn có thể thêm tên Dự án tại đây.
      * **Bill**: Ô này cần được tích nếu Timesheet cụ thể này có thể lập hóa đơn.
  4. Nhấp vào 'Add Row' để thêm các Timesheet tương tự.
  5. Lưu.
  6. Sau khi lưu Timesheet, dựa trên các chi tiết được nhập trong các dòng Time Sheets khác nhau, Ngày bắt đầu, Ngày kết thúc và Tổng số giờ làm việc sẽ được cập nhật tự động. Nhấp Xác nhận.

### 1.1. Ngoài ra, một Timesheet cũng có thể được tạo từ một Nhiệm vụ theo cách sau:

  1. Đi tới Nhiệm vụ mà bạn muốn tạo Timesheet mới.
  2. Đi tới 'Timesheet' trong phần Hoạt động trên Trang tổng quan. Biểu tượng dấu cộng '+' ở đây sẽ chuyển hướng bạn đến trang tạo Timesheet.
  3. Làm theo các bước để tạo một Timesheet.

  <img class="screenshot" alt="Timesheet" src="https://docs.erpnext.com/docs/v13/assets/img/project/projects-timesheet-from-task.gif">

### 1.2. Bộ đếm thời gian trong Timesheet

**Bộ đếm thời gian có thể được sử dụng để ghi lại thời gian thực tế mà một nhân viên đã thực hiện để hoàn thành một hoạt động cụ thể trong một Timesheet.**

#### 1.2.1. Các bước để bắt đầu Bộ đếm thời gian:

- Trong một Timesheet, khi nhấp vào **Start Timer**, một hộp thoại sẽ hiện ra và bạn được yêu cầu nhập các chi tiết sau:
    * **Activity Type**: Hoạt động mà bạn đang ghi lại thời gian.
    * **Project**: Dự án mà bạn đang tạo Timesheet.
    * **Task**: Nhiệm vụ mà bạn đang ghi lại thời gian trong Timesheet.
    * **Expected Hrs**: Nhập số giờ dự kiến để hoàn thành Nhiệm vụ.

<img class="screenshot" alt="Timer in Progress" src="https://docs.erpnext.com/docs/v13/assets/img/project/projects-timer-in-timesheet.gif">

- Sau khi bạn đã hoàn thành Nhiệm vụ, hãy nhấp vào Complete. Một mục mới sẽ được tạo trong Timesheet, và thời gian sẽ được ghi lại dưới dạng một dòng Time Sheet trong Bảng Time Sheets trong Timesheet.

- Nếu thời gian vượt quá 'Expected Hrs', một hộp cảnh báo sẽ xuất hiện.

<img class="screenshot" alt="Timer Exceeded" src="https://docs.erpnext.com/docs/v13/assets/img/project/projects-timer-time-exceed.png">


### 1.3. Các tùy chọn bổ sung khi tạo Timesheet

Khi được mở rộng, Timesheet cho phép bạn nhập các chi tiết sau:

   * **Expected Hours**: Nhập thời gian dự kiến cần thiết để hoàn thành các Nhiệm vụ trong các dòng Time Sheets.
   * **To Time**: Nhập ngày và giờ mà công việc đã được hoàn thành.
   * **Completed**: Ô này cần được tích nếu Nhiệm vụ đã được hoàn thành khi đang xác nhận Timesheet.
   * **Task**: Nếu Timesheet này cần được gắn với một Nhiệm vụ cụ thể, bạn có thể thực hiện tại đây.
   * **Billing Hours**: Số giờ mà khách hàng cần được lập hóa đơn cho Timesheet này.
   * **Billing Rate**: Đơn giá mà khách hàng cần được lập hóa đơn cho công việc này.
   * **Costing Rate**: Đây là chi phí thực tế của công việc đã thực hiện. Nó được lấy từ chi phí hoạt động (trên mỗi nhân viên) hoặc từ loại hoạt động và có thể được chỉnh sửa.
   * **Billing Amount**: Số tiền lập hóa đơn được tự động tính toán dựa trên số giờ có thể lập hóa đơn và Đơn giá lập hóa đơn.
   * **Costing Amount**: Số tiền chi phí được tự động tính toán dựa trên số giờ và đơn giá chi phí.

   <img class="screenshot" alt="Timesheet" src="https://docs.erpnext.com/docs/v13/assets/img/project/projects-time-sheet-expansion.png">

## 2. Các tính năng

### 2.1 Chi tiết lập hóa đơn

* **Total Billable Hours**: Dựa trên Timesheet, Tổng số giờ có thể lập hóa đơn sẽ được tự động lấy tại đây.
* **Total Billable Amount**: Dựa trên Timesheet, Tổng số tiền có thể lập hóa đơn sẽ được tự động lấy tại đây.
* **Total Billed Hours**: Sau khi Timesheet đã được xác nhận, bạn sẽ có tùy chọn để tạo một Hóa đơn bán hàng từ Timesheet. Số giờ mà Khách hàng sẽ được lập hóa đơn sẽ được lấy tại đây, và sau khi Hóa đơn bán hàng được xác nhận, Tổng số giờ đã lập hóa đơn sẽ được lấy.
* **Total Billed Amount**: Tương tự như cách lấy Tổng số giờ đã lập hóa đơn, Tổng số tiền đã lập hóa đơn cũng sẽ được lấy.
* **Total Costing Amount**: Dựa trên Timesheet, Tổng số tiền chi phí, như được chỉ định bởi Nhân viên, sẽ được gắn tại đây.
* **% Amount Billed**: Sau khi Timesheet được xác nhận, và một [Sales Invoice](/docs/v13/user/manual/en/projects/sales-invoice-from-timesheet) được tạo từ Timesheet, tỷ lệ phần trăm của Số tiền so với Tổng số tiền có thể lập hóa đơn đã được tính cho Tổng số tiền đã lập hóa đơn sẽ được tính toán và hiển thị tại đây.

<img class="screenshot" alt="Timesheet" src="https://docs.erpnext.com/docs/v13/assets/img/project/projects-timesheet-billing-details.png">

## 3. Sau khi Lưu Timesheet

Sau khi một Timesheet được lưu và xác nhận, các chi tiết như Đơn giá lập hóa đơn và Đơn giá chi phí sẽ bị khóa và không thể thay đổi. Các DocType sau có thể được tạo sau khi xác nhận một Timesheet.

 * [Sales Invoice](/doc