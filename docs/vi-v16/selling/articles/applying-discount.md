<!-- add-breadcrumbs -->
# Áp dụng Chiết khấu

Có nhiều cách để áp dụng Chiết khấu cho một mặt hàng trong các giao dịch bán hàng. Điều này có thể được thực hiện trong tất cả các giao dịch bán hàng và mua hàng.

## 1. Chiết khấu trên Đơn giá của Bảng giá cho một mặt hàng

Bạn có thể tìm thấy trường Chiết khấu trong bảng Mặt hàng của một giao dịch, hãy nhấp vào mũi tên hướng xuống ở phía bên phải của hàng. Chiết khấu có thể được áp dụng dưới dạng phần trăm hoặc một số tiền cố định dựa trên Đơn giá của Bảng giá của Mặt hàng đó.

![Discount on Price List Rate](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/discount-on-price-list-rate.png)

Tính năng Chiết khấu (%) có sẵn trong tất cả các giao dịch bán hàng và mua hàng.

Nếu bạn muốn áp dụng chiết khấu (dưới dạng Phần trăm) thường xuyên cho một số lượng nhất định, bạn nên sử dụng "Quy tắc định giá". Hãy đọc tài liệu [Quy tắc định giá](../../accounts/pricing-rule.md) để tìm hiểu thêm.

## 2. Chiết khấu trên Tổng ròng hoặc Tổng cộng

Trong phần "Chiết khấu bổ sung" (của "Đơn bán hàng" hoặc "Hóa đơn" tương tự), bạn có thể áp dụng Chiết khấu dưới dạng một số tiền cố định hoặc một tỷ lệ phần trăm trên tổng giá trị của việc bán hàng.

![Additional Discount](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/additional-discount.png)

### 2.1 Chiết khấu trên "Tổng ròng"

Nếu Chiết khấu được áp dụng trên **Tổng ròng**, thì Đơn giá ròng và Số tiền ròng của mặt hàng sẽ được tính toán theo Số tiền chiết khấu. Trường Đơn giá ròng và Số tiền ròng sẽ chỉ hiển thị nếu Chiết khấu được áp dụng bằng tính năng này.

![Discount on Net Total](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/discount-on-net-total.png)

### 2.2 Chiết khấu trên "Tổng cộng"

Nếu Chiết khấu được áp dụng dựa trên **Tổng cộng**, thì cùng với Đơn giá ròng và Số tiền ròng của mặt hàng, các khoản thuế cũng sẽ được tính toán lại theo Số tiền chiết khấu.

![Discount on Grand Total](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/discount-on-grand-total.png)

---

## 3. Các tính năng mới trong v16

### 3.1 Cutoff date cho Phiếu giao hàng (DN) từ Đơn bán hàng (SO)

Trong phiên bản v16, khi tạo Phiếu giao hàng (DN) từ Đơn bán hàng (SO), bạn có thể thiết lập **Ngày chốt (Cutoff date)**. Tính năng này giúp kiểm soát việc giao hàng theo từng giai đoạn hoặc theo các mốc thời gian cụ thể, đảm bảo các mặt hàng không được giao vượt quá thời hạn đã định trong kế hoạch.

### 3.2 Nút lệnh SO/Quotation trên Khách hàng

Để tối ưu hóa quy trình bán hàng, tại giao diện thông tin **Khách hàng**, hệ thống đã bổ sung các nút lệnh truy cập nhanh vào **Đơn bán hàng (SO)** và **Báo giá (Quotation)**. Điều này cho phép người dùng nhanh chóng kiểm tra lịch sử giao dịch hoặc tạo mới các tài liệu bán hàng mà không cần phải chuyển đổi qua lại giữa các menu.

### 3.3 Giữ chỗ tồn kho (Stock Reservation)

Tính năng **Giữ chỗ tồn kho (Stock Reservation)** cho phép bạn giữ lại một lượng Mặt hàng nhất định trong Kho để phục vụ cho các Đơn bán hàng (SO) hoặc các yêu cầu cụ thể khác. Khi một mặt hàng đã được giữ chỗ, số lượng này sẽ được trừ khỏi lượng hàng có sẵn để bán, giúp tránh tình trạng thiếu hụt hàng hóa khi thực hiện xác nhận đơn hàng.

{next}