<!-- add-breadcrumbs -->
# Quản lý phế liệu sản xuất

Phế liệu có nghĩa là chất thải không có giá trị kinh tế hoặc chỉ có giá trị của thành phần vật liệu cơ bản có thể thu hồi thông qua tái chế.

Phế liệu thường phát sinh vào cuối quá trình sản xuất. Ngoài ra, bạn cũng có thể thấy một số sản phẩm bị hư hỏng hoặc không thể sử dụng được do hết hạn hoặc vì một lý do nào khác, cần phải thanh lý thành phế liệu.

Trong ERPNext, khi kết thúc quá trình sản xuất, các mặt hàng phế liệu sẽ được hạch toán vào các kho phế liệu.

## Phế liệu trong Định mức nguyên vật liệu

Bạn có thể cập nhật số lượng phế liệu ước tính của một mặt hàng trong bảng Scrap của BOM. Nếu cần, bạn có thể chọn lại một mặt hàng nguyên liệu làm phế liệu.

<img class="screenshot" alt="Scrap in BOM" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/scrap-1.png">

## Phế liệu trong Phiếu sản xuất

Khi quá trình sản xuất hoàn tất, Phiếu sản xuất (Manufacture Entry) sẽ được tạo dựa trên Lệnh sản xuất. Trong phiếu này, mặt hàng phế liệu sẽ được lấy vào bảng Item, và chỉ có Kho đích (Target Warehouse) được cập nhật cho mặt hàng đó. Hãy đảm bảo rằng Giá trị tính giá (Valuation Rate) đã được cập nhật cho mặt hàng này để phục vụ mục đích hạch toán kế toán.

<img class="screenshot" alt="Scrap in Manufacture Entry" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/scrap-2.gif">

> Phế liệu từ BOM sẽ chỉ có hiệu lực nếu Phiếu sản xuất được tạo dựa trên BOM, chứ không phải dựa trên Phiếu chuyển vật tư. Điều này có thể cấu hình trong Cài đặt sản xuất (Manufacturing Settings).

<img class="screenshot" alt="Manufacturing Settings" src="https://docs.erpnext.com/docs/v13/assets/img/manufacturing/manufacturing-settings.png">