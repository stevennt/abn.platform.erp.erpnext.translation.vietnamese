# Thuế và các khoản phí

Bạn có thể thêm [Quy tắc vận chuyển](../shipping-rule.md) tại đây cho các mặt hàng trong báo giá. Để thêm thuế vào Báo giá, bạn có thể chọn một [Mẫu thuế và phí bán hàng](../sales-taxes-and-charges-template.md) hoặc thêm thuế một cách thủ công trong bảng Thuế và phí bán hàng. Tổng thuế và các khoản phí sẽ được hiển thị bên dưới bảng. Nhấp vào Chi tiết thuế sẽ hiển thị tất cả các thành phần và số tiền.

<img class="screenshot" alt="Taxes in Quotation" src="https://docs.erpnext.com/docs/v16/assets/img/selling/quotation-taxes.png">

## Nhóm thuế
Nhóm thuế được liên kết với [Quy tắc thuế](../../accounts/tax-rule.md). Nhóm thuế này có thể được gán cho một Khách hàng, vì vậy khi khách hàng đó được chọn, Nhóm thuế sẽ được tự động lấy ra. Điều này sẽ lấy Mẫu thuế bán hàng được liên kết với Quy tắc thuế. Do đó, các dòng trong bảng Thuế sẽ được điền tự động. Nhóm thuế có thể được sử dụng để nhóm các khách hàng mà cùng một loại thuế sẽ được áp dụng. Ví dụ: Chính phủ, Tổ chức phi chính phủ (NGO), thương mại, v.v.

<img class="screenshot" alt="Tax Category" src="https://docs.erpnext.com/docs/v16/assets/img/selling/tax-category.gif">

## Các tính năng mới trong v16

### Nút bấm SO/Quotation trên Khách hàng
Trong giao diện Khách hàng, bạn có thể truy cập nhanh các [Đơn bán hàng](../selling/sales-order.md) hoặc Báo giá thông qua các nút bấm được tích hợp sẵn trên form Khách hàng để tối ưu hóa quy trình bán hàng.

### Ngày chốt (Cutoff date) cho Phiếu giao hàng (DN) từ Đơn bán hàng (SO)
Khi tạo Phiếu giao hàng (DN) từ Đơn bán hàng (SO), hệ thống v16 cho phép thiết lập Ngày chốt (Cutoff date). Tính năng này giúp kiểm soát chính xác thời điểm xuất kho và ghi nhận doanh thu, đảm bảo các mặt hàng không bị xuất quá hạn hoặc sai lệch kỳ kế toán.

### Giữ chỗ tồn kho (Stock Reservation)
Tính năng Giữ chỗ tồn kho cho phép bạn giữ lại một lượng [Mặt hàng](../stock/item.md) nhất định trong [Kho](../stock/warehouse.md) cho các [Đơn bán hàng](../selling/sales-order.md) cụ thể. Điều này giúp ngăn chặn việc các đơn hàng khác sử dụng mất lượng hàng đã được cam kết cho khách hàng, đảm bảo khả năng đáp ứng đơn hàng chính xác hơn.