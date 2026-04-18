<!-- add-breadcrumbs -->
# Thêm Biên lợi nhuận

Người dùng có thể áp dụng biên lợi nhuận trên Mặt hàng Báo giá và Mặt hàng Đơn bán hàng bằng hai tùy chọn sau:

1. **Quy tắc định giá:** Với phương pháp này, người dùng có thể áp dụng biên lợi nhuận trên Báo giá và Đơn bán hàng dựa trên các điều kiện thiết lập sẵn. Bạn có thể tìm thấy phần biên lợi nhuận trong Quy tắc định giá, nơi người dùng chọn Loại biên lợi nhuận là **Phần trăm** hoặc **Số tiền**, và áp dụng lên **Đơn giá** hoặc **Số tiền**. Hệ thống sẽ tự động áp dụng biên lợi nhuận vào Mặt hàng Báo giá và Mặt hàng Đơn bán hàng nếu Quy tắc định giá được kích hoạt.

Để thiết lập Quy tắc định giá, hãy đi tới:
`Selling > Setup > Pricing Rule` hoặc `Accounts > Setup > Pricing Rule`

#### Thêm Biên lợi nhuận trong Quy tắc định giá

![Adding Margin in Pricing Rule](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/margin-pricing-rule.png)

Tổng giá bán được tính như sau:
`Rate = Price List Rate + Margin Rate`

Vì vậy, để áp dụng Biên lợi nhuận, bạn cần phải có sẵn Bảng giá cho Mặt hàng.

Để thêm Bảng giá, hãy đi tới:
`Selling > Setup > Item Price` hoặc `Stock > Setup > Item Price`

#### Thêm Giá mặt hàng

![Adding Margin in Pricing Rule](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/margin-item-price-list.png)

2. **Áp dụng biên lợi nhuận trực tiếp trên Mặt hàng:** Nếu người dùng muốn áp dụng biên lợi nhuận mà không cần thông qua Quy tắc định giá, họ có thể sử dụng tùy chọn này. Trong Mặt hàng Báo giá và Mặt hàng Đơn bán hàng, người dùng có thể chọn Loại biên lợi nhuận và tỷ lệ hoặc số tiền tương ứng. Hệ thống sẽ tính toán biên lợi nhuận và cộng trực tiếp vào đơn giá trong Bảng giá để ra đơn giá cuối cùng của sản phẩm.

**Lưu ý mới trên v16:** 
* Tại màn hình thông tin **Khách hàng**, bạn có thể truy cập nhanh các nút **Báo giá** hoặc **Đơn bán hàng** để tạo nhanh các chứng từ liên quan.
* Đối với các chứng từ như **Đơn bán hàng**, hệ thống hỗ trợ tính năng **Giữ hàng tồn kho (Stock Reservation)** để đảm bảo hàng hóa được dành riêng cho đơn hàng, tránh tình trạng thiếu hụt khi thực hiện **Phiếu giao hàng (DN)**.
* Khi tạo **Phiếu giao hàng (DN)** từ **Đơn bán hàng (SO)**, hãy lưu ý kiểm tra **Ngày chốt (Cutoff date)** để đảm bảo việc xuất kho được ghi nhận chính xác vào kỳ kế toán mong muốn.

Để thêm biên lợi nhuận trực tiếp trên Báo giá hoặc Đơn bán hàng, hãy đi tới:
`Selling > Document > Quotation`

Thêm mặt hàng vào bảng và cuộn xuống phần **Loại biên lợi nhuận**.

#### Thêm Biên lợi nhuận trong Báo giá

![Adding Margin in Quotation](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/margin-quotation-item.png)

{next}