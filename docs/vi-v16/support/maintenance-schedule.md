<!-- add-breadcrumbs -->
# Lịch bảo trì

**Lịch bảo trì hiển thị tất cả các Lần thăm khám bảo trì sắp tới.**

Tất cả các máy móc đều yêu cầu bảo trì định kỳ, đặc biệt là những máy có nhiều bộ phận chuyển động, vì vậy nếu bạn kinh doanh dịch vụ bảo trì các loại máy này hoặc có chúng trong cơ sở của mình, đây là một công cụ hữu ích để lập kế hoạch lịch trình cho các hoạt động bảo trì.

Để tạo một Lịch bảo trì mới, hãy đi tới:

> Home > Support > Maintenance > Maintenance Schedule

Một Lịch bảo trì thường được tạo từ một Đơn bán hàng loại 'Maintenance'.

![SO Maintenance Schedule](https://docs.erpnext.com/docs/v16/assets/img/support/so-maintenance-schedule.png)

## 1. Điều kiện tiên quyết
* [Khách hàng](../user/manual/en/CRM/customer)
* [Mặt hàng](../user/manual/en/stock/item)

## 2. Cách tạo Lịch bảo trì
1. Đi tới Lịch bảo trì, nhấn vào New.
1. Chọn Khách hàng và các Mặt hàng cần thực hiện bảo trì.
1. Thiết lập ngày bắt đầu và ngày kết thúc.
1. Chọn Chu kỳ (Periodicity) để thiết lập tần suất các lần thăm khám sẽ diễn ra. Các tùy chọn là "Weekly" (Hàng tuần), "Monthly" (Hàng tháng), "Quarterly" (Hàng quý), "Half Yearly" (Nửa năm), "Yearly" (Hàng năm) và "Random" (Ngẫu nhiên). Lịch bảo trì sẽ được tạo dựa trên Chu kỳ đã chọn. Nếu chọn Random, các ngày sẽ được tạo ngẫu nhiên.
1. Số lượng lần thăm khám (Number of Visits) sẽ được thiết lập theo Chu kỳ đã chọn. Ví dụ: Nếu bạn chọn Weekly và thiết lập toàn bộ tháng giữa ngày bắt đầu và ngày kết thúc, 4 lần thăm khám là lý tưởng.
1. Chọn Nhân viên bán hàng thực hiện các lần thăm khám.
1. Lưu.
1. Sau khi Lưu, nhấn vào nút **Generate Schedule** để tạo Lịch bảo trì.
1. Xác nhận.

    ![Maintenance Schedule](https://docs.erpnext.com/docs/v16/assets/img/support/maintenance-schedule-1.png)

Nút **Generate Schedule** sẽ tạo một dòng riêng biệt cho mỗi hoạt động bảo trì. Mỗi Mặt hàng trong một Lịch bảo trì được phân bổ cho một Nhân viên bán hàng.

Khi tài liệu được Xác nhận, các sự kiện lịch sẽ được tạo cho Người dùng là Nhân viên bán hàng cho mỗi lần bảo trì.

## 3. Các chủ đề liên quan
1. [Số serial](../user/manual/en/stock/serial-no)
1. [Yêu cầu bảo hành](../user/manual/en/support/warranty-claim)
1. [Lần thăm khám bảo trì](../user/manual/en/support/maintenance-visit)
1. [Đơn bán hàng](../user/manual/en/selling/sales-order)

{next}