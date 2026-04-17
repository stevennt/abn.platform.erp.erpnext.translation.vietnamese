<!-- add-breadcrumbs -->
# Ngân sách

**Ngân sách là một kế hoạch tài chính giúp kiểm soát các chi phí của Công ty.**

Trong ERPNext, bạn có thể thiết lập và quản lý ngân sách dựa trên Trung tâm chi phí hoặc Dự án. Điều này rất hữu ích trong việc kiểm soát các chi phí của bạn. Với phiên bản 12, bạn cũng có thể tạo các [Accounting Dimensions](/docs/v13/user/manual/en/accounts/accounting-dimensions) riêng biệt để gắn thẻ các giao dịch với các trường khác nhau.

Ví dụ, nếu bạn đang kinh doanh bán hàng trực tuyến, bạn có thể thiết lập ngân sách cho quảng cáo tìm kiếm và cấu hình ERPNext để dừng hoặc cảnh báo bạn khi chi tiêu vượt quá ngân sách đã đặt ra.

Ngân sách cũng rất tuyệt vời cho mục đích lập kế hoạch. Khi bạn đang lập kế hoạch cho Năm tài chính tiếp theo, bạn thường sẽ đặt mục tiêu doanh thu, dựa vào đó bạn sẽ thiết lập các chi phí của mình. Việc thiết lập ngân sách sẽ đảm bảo rằng các chi phí của bạn không vượt quá tầm kiểm soát tại bất kỳ thời điểm nào.

Để truy cập danh sách Ngân sách, hãy đi tới:
> Home > Accounting > Cost Center and Budgeting > Budget

## 1. Cách tạo Ngân sách mới
1. Đi tới danh sách Ngân sách và nhấn vào Mới.
1. Chọn đối tượng để lập ngân sách: Trung tâm chi phí, Dự án, hoặc [Accounting Dimensions](/docs/v13/user/manual/en/accounts/accounting-dimensions).
1. Trong bảng tài khoản, chọn tài khoản thu nhập/chi phí mà bạn muốn thiết lập ngân sách. Ví dụ, hãy thiết lập ngân sách cho chi phí điện thoại trong năm.
 ![Budget](/docs/v13/assets/img/accounts/budget.png)
1. Nhập Số tiền ngân sách cho tài khoản đó.
1. Lưu và Xác nhận.


## 2. Các tính năng
### 2.1 Phân bổ hàng tháng

Bạn cũng có thể xác định một bản ghi Phân bổ hàng tháng để phân bổ ngân sách giữa các tháng. Nếu bạn không thiết lập phân bổ hàng tháng, ERPNext sẽ tính toán ngân sách theo năm hoặc chia đều cho mỗi tháng.

![Monthly Distribution](/docs/v13/assets/img/accounts/monthly-budget-distribution.png)

### 2.2 Hành động kiểm soát (Cảnh báo)

Các hành động kiểm soát có thể được kích hoạt khi:

* Một [Material Request](/docs/v13/user/manual/en/stock/material-request) đang được xác nhận
* Một [Purchase Order](/docs/v13/user/manual/en/buying/purchase-order) đang được xác nhận
* Khi một chi phí thực tế đang được ghi sổ (thông qua bút toán hoặc hóa đơn mua hàng).

Bạn có thể thiết lập một hành động kiểm soát trong Ngân sách dựa trên Yêu cầu vật tư, Đơn mua hàng, hoặc dựa trên chi phí thực tế. Hơn nữa, bạn có thể thiết lập hành động kiểm soát cho ngân sách hàng năm hoặc hàng tháng.

![Control Actions](/docs/v13/assets/img/accounts/control-actions.png)

Có ba loại hành động kiểm soát.

* **Stop (Dừng)**: Hành động này sẽ không cho phép người dùng xác nhận giao dịch.
* **Warn (Cảnh báo)**: Hành động này sẽ hiển thị một thông báo cảnh báo nhưng vẫn cho phép người dùng xác nhận giao dịch.
* **Ignore (Bỏ qua)**: Hành động này sẽ không ngăn cản người dùng xác nhận giao dịch cũng như không hiển thị thông báo lỗi.

Bạn có thể thiết lập các hành động riêng biệt cho ngân sách hàng tháng và hàng năm. Nếu bạn vượt quá ngân sách, một cảnh báo sẽ được hiển thị:

![Budget Warning](/docs/v13/assets/img/accounts/budget-warning.png)

Lưu ý rằng một cảnh báo tương tự sẽ được kích hoạt cho bất kỳ loại giao dịch nào được thiết lập trong ngân sách cho các Tài khoản tương ứng.

## 3. Báo cáo chênh lệch ngân sách

Tại bất kỳ thời điểm nào, bạn có thể kiểm tra Báo cáo chênh lệch ngân sách để phân tích chi phí thực tế phát sinh so với ngân sách được phân bổ cho một trung tâm chi phí hoặc một dự án.

Để kiểm tra báo cáo Chênh lệch ngân sách, hãy đi tới:

> Home > Accounting > Cost Center and Budgeting > Budget Variance Report

![Budget Variance Report](/docs/v13/assets/img/accounts/budget-variance-report.png)

## 4. Video
Dưới đây là video hướng dẫn:
<div class="embed-container">
 <iframe src="https://www.youtube.com/embed/wWHkB0jlXNk?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
 </iframe>
</div>

## 5. Các chủ đề liên quan
1. [Cost Center](/docs/v13/user/manual/en/accounts/cost-center)
1. [Sales Invoice](/docs/v13/user/manual/en/accounts/sales-invoice)
1. [Purchase Invoice](/docs/v13/user/manual/en/accounts/purchase-invoice)

{next}