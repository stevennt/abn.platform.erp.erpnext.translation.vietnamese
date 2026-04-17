<!-- add-breadcrumbs -->
# Hóa đơn bán hàng từ Timesheet

Khách hàng có thể được lập hóa đơn dựa trên tổng số giờ mà một nhân viên đã làm việc cho khách hàng đó. Số giờ làm việc thực tế có thể tính phí có thể được theo dõi thông qua [Timesheet](../projects/timesheets.md).

**Một hóa đơn bán hàng có thể được tạo từ mỗi Timesheet đã được Xác nhận bởi nhân viên để dùng cho việc lập hóa đơn cho khách hàng.**

<img class="screenshot" alt="Sales Invoice" src="https://docs.erpnext.com/docs/v16/assets/img/project/projects-sales-invoice-from-timesheet.png">

## 1. Cách tạo Hóa đơn bán hàng từ Timesheet

  1. Sau khi Timesheet đã được Xác nhận, hãy nhấp vào 'Create Sales Invoice'.
  2. Nhập Mã mặt hàng (Item Code) và tên của Khách hàng cần lập hóa đơn dựa trên Timesheet này. Mặt hàng có thể là Sản phẩm hoặc Dịch vụ. Nhấp vào 'Create Sales Invoice'.
  3. Tất cả các chi tiết của Timesheet sẽ được tự động điền vào Hóa đơn bán hàng.
  4. Ngày và giờ hạch toán sẽ được đặt theo thời gian hiện tại, bạn có thể chỉnh sửa sau khi tích vào ô kiểm bên dưới Posting Time.
  5. Tùy chọn, bạn có thể bao gồm các khoản thanh toán cho POS hoặc chuyển nó thành một phiếu giảm giá (credit note).
  6. Lưu và Xác nhận.

Để lấy thông tin tự động vào Hóa đơn bán hàng, hãy nhấp vào nút **Get items from**. Thông tin có thể được lấy từ Đơn bán hàng, Phiếu giao hàng hoặc Báo giá. Các chi tiết như Đơn mua hàng của Khách hàng (Customer PO), Địa chỉ và Số điện thoại liên hệ, Tiền tệ và Bảng giá, các Mặt hàng sẽ được tự động điền.

*Lưu ý trong phiên bản v16: Hệ thống hỗ trợ các nút bấm SO/Quotation trực tiếp trên form Khách hàng để tối ưu hóa quy trình bán hàng.*

<img class="screenshot" alt="Sales Invoice" src="https://docs.erpnext.com/docs/v16/assets/img/project/timesheet/timesheet-billing-to-sales-invoice.gif">

## 2. Các tính năng

Các chi tiết bổ sung khi tạo Hóa đơn bán hàng từ một Timesheet:

  * **Accounting Dimensions**: Accounting Dimensions cho phép bạn gắn các giao dịch vào một Khu vực, Chi nhánh, Dự án, v.v. cụ thể. Điều này giúp xem các báo cáo kế toán riêng biệt dựa trên các tiêu chí đã chọn. Để biết thêm, hãy truy cập trang [Accounting Dimensions](../accounts/accounting-dimensions.md).
  * **Time Sheet List**: Vì Dự án được tạo từ một Timesheet, các chi tiết của Timesheet sẽ được tự động lấy ra. Bạn có thể nhấp vào 'Add Row' để thêm nhiều Timesheet khác vào Hóa đơn này.
  * **Stock Reservation (Giữ hàng tồn kho)**: Trong phiên bản v16, khi tạo các chứng từ liên quan đến bán hàng, bạn có thể sử dụng tính năng Giữ hàng để đảm bảo các Mặt hàng có sẵn trong Kho cho các đơn hàng đã xác nhận.
  * **Cutoff Date cho Phiếu giao hàng**: Khi lập Phiếu giao hàng (DN) từ Đơn bán hàng (SO), hệ thống v16 cho phép thiết lập ngày chốt (Cutoff date) để kiểm soát chính xác thời điểm xuất kho và ghi nhận doanh thu.

Tất cả các chi tiết khác có thể được thêm vào giống như khi bạn thêm vào bất kỳ [Hóa đơn bán hàng](../accounts/sales-invoice.md) nào.

## 3. Sau khi xác nhận

Sau khi bạn đã Xác nhận Hóa đơn bán hàng, các chi tiết như 'Total Billed Hours' (Tổng số giờ đã lập hóa đơn), 'Total Billed Amount' (Tổng số tiền đã lập hóa đơn) và '% Amount Billed' (% Số tiền đã lập hóa đơn) sẽ được cập nhật trong Timesheet. Ngoài ra, một [Phiếu lương](../projects/salary-slip-from-timesheet.md) cũng có thể được tạo từ Timesheet.

{next}