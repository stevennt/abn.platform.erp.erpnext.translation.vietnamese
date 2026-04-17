<!-- add-breadcrumbs -->
# Quy tắc Thuế

**Quy tắc Thuế tự động áp dụng thuế vào các giao dịch dựa trên các quy tắc đã thiết lập sẵn.**

Bạn có thể xác định [Mẫu Thuế](../selling/sales-taxes-and-charges-template.md) nào phải được áp dụng cho giao dịch Bán hàng / Mua hàng bằng cách sử dụng Quy tắc Thuế. Điều này được quyết định bởi các yếu tố khác nhau như Khách hàng, Nhóm khách hàng, Nhà cung cấp, Nhóm nhà cung cấp, Mặt hàng, Nhóm mặt hàng hoặc sự kết hợp của các yếu tố này.

Để truy cập danh sách Quy tắc Thuế, hãy đi tới:
> Home > Accounting > Taxes > Tax Rule

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Quy tắc Thuế, bạn nên tạo các mục sau trước:

1. [Mẫu Thuế và Phí Bán hàng](../selling/sales-taxes-and-charges-template.md)

    Hoặc

1. [Mẫu Thuế và Phí Mua hàng](../buying/purchase-taxes-and-charges-template.md)

## 2. Cách tạo Quy tắc Thuế
1. Đi tới danh sách Quy tắc Thuế và nhấn New.
1. Trong phần Tax Type, chọn loại thuế sẽ được áp dụng cho Bán hàng (Sales) hoặc Mua hàng (Purchase).
1. Chọn Mẫu Thuế (Tax Template) cần áp dụng.
1. Lưu.
 <img class="screenshot" alt="Tax Rule" src="https://docs.erpnext.com/docs/v16/assets/img/accounts/tax-rule.png">

Bạn có thể liệt kê các Mặt hàng trực tuyến bằng mô-đun Website. Việc chọn 'Use for Shopping Cart' sẽ sử dụng Quy tắc Thuế này cho cả các giao dịch trong Giỏ hàng. Để biết thêm, hãy truy cập trang [Giỏ hàng](../website/shopping-cart.md).

> Lưu ý: Khuyến nghị không sử dụng Mẫu Bán hàng/Mua hàng đã chọn ở đây trong [Mẫu Thuế Mặt hàng](item-tax-template.md), vì nó có thể gây xung đột. Nếu bạn muốn sử dụng cùng mức thuế cho Quy tắc Thuế và Mẫu Thuế Mặt hàng, hãy sử dụng một tên khác cho các Mẫu Thuế Bán hàng/Mua hàng.

## 3. Các tính năng
### 3.1 Tự động áp dụng Quy tắc Thuế dựa trên Khách hàng/Nhà cung cấp
Chọn một Khách hàng/Nhà cung cấp nếu thuế cần được áp dụng cho một đối tác cụ thể. Để trống là All Customer Groups/All Supplier Groups nếu Quy tắc Thuế này áp dụng cho tất cả Khách hàng/Nhà cung cấp.

Khi chọn một Khách hàng/Nhà cung cấp, địa chỉ Thanh toán và Giao hàng của họ sẽ được lấy tự động nếu đã được lưu trong danh mục Khách hàng/Nhà cung cấp.

### 3.2 Tự động áp dụng Quy tắc Thuế dựa trên Mặt hàng / Nhóm mặt hàng

Khi thiết lập một Mặt hàng hoặc Nhóm mặt hàng trong Quy tắc Thuế, Quy tắc Thuế này sẽ tự động được áp dụng cho các giao dịch mới có Mặt hàng/Nhóm mặt hàng đã chọn.

### 3.3 Thiết lập Danh mục Thuế
Việc thiết lập Danh mục Thuế cho phép áp dụng nhiều Quy tắc Thuế vào một giao dịch dựa trên các yếu tố khác nhau. Để biết thêm, hãy truy cập trang [Danh mục Thuế](tax-category.md).

### 3.4 Thời hạn hiệu lực
Thiết lập Ngày bắt đầu và Ngày kết thúc nếu thuế chỉ được áp dụng trong một khoảng thời gian cụ thể. Nếu để trống cả hai ngày, Quy tắc Thuế sẽ không có giới hạn thời gian.

### 3.5 Độ ưu tiên
Thiết lập số thứ tự ưu tiên tại đây sẽ quyết định thứ tự áp dụng Quy tắc Thuế trong trường hợp có nhiều Quy tắc Thuế có các tiêu chí tương tự. '1' là ưu tiên cao nhất, '2' có ưu tiên thấp hơn và cứ tiếp tục như vậy.

## 4. Quy tắc Thuế hoạt động như thế nào?

Hãy cùng cấu hình Quy tắc Thuế để hệ thống tự động áp dụng các mức thuế cụ thể khi khớp với một điều kiện nhất định. Ví dụ: nếu thành phố trong địa chỉ thanh toán của khách hàng là 'Malibu', thì mức thuế tiểu bang 6.25%, thuế quận 1% và thuế huyện 2.25% sẽ được áp dụng.

Tạo một Mẫu Thuế và Phí Bán hàng như hiển thị bên dưới.

![City Specific To Zipcode](https://docs.erpnext.com/docs/v16/assets/img/accounts/city-specific-tax.png)

Tạo một Quy tắc Thuế như hiển thị bên dưới.

![Tax Rule](https://docs.erpnext.com/docs/v16/assets/img/accounts/tax-rule.png)

Khi bạn chọn một khách hàng và địa chỉ thanh toán của khách hàng đó có thành phố là 'Malibu', hệ thống sẽ tự động áp dụng các loại thuế phù hợp.

![Tax Rule in Sales Invoice](https://docs.erpnext.com/docs/v16/assets/img/accounts/tax-rule-in-sales-invoice.gif)

## 5. Các chủ đề liên quan
1. [Quy tắc định giá](pricing-rule.md)
1. [Mẫu Thuế Mặt hàng](item-tax-template.md)
1. [Danh mục Thuế](tax-category.md)
1. [Khách hàng](../crm/customer.md)
1. [Nhà cung cấp](../buying/supplier.md)

{next}