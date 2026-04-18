<!-- add-breadcrumbs -->
# Quy tắc vận chuyển

Danh mục Quy tắc vận chuyển giúp định nghĩa một quy tắc mà dựa vào đó, phí vận chuyển sẽ được áp dụng cho các giao dịch bán hàng.

Hầu hết các công ty (chủ yếu là bán lẻ) có phí vận chuyển được áp dụng dựa trên tổng hóa đơn. Nếu giá trị hóa đơn trên một mức nhất định, phí vận chuyển áp dụng sẽ thấp hơn. Nếu giá trị hóa đơn thấp hơn, phí vận chuyển áp dụng sẽ cao hơn một chút so với phí vận chuyển áp dụng cho hóa đơn có giá trị cao. Bạn có thể thiết lập Quy tắc vận chuyển để đáp ứng yêu cầu thay đổi phí vận chuyển dựa trên Tổng ròng của giao dịch bán hàng.

Để thiết lập Quy tắc vận chuyển, hãy đi tới:

`Bán hàng > Thiết lập > Quy tắc vận chuyển` hoặc `Kế toán > Thiết lập > Quy tắc vận chuyển`

#### Điều kiện Quy tắc vận chuyển

![Shipping Rule Conditions](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/shipping-rule-conditions.png)

Tham chiếu hình trên, bạn sẽ thấy rằng phí vận chuyển giảm dần khi giá trị tăng lên. Phí vận chuyển này sẽ chỉ được áp dụng nếu tổng giao dịch nằm trong một trong các khoảng trên.

#### Có hiệu lực cho các quốc gia

Bạn có thể thiết lập Phí vận chuyển có hiệu lực cho tất cả các quốc gia, hoặc chỉ định các Quốc gia cụ thể. Nếu các quốc gia cụ thể được đề cập, thì Phí vận chuyển sẽ chỉ được áp dụng nếu quốc gia của Khách hàng khớp với Quốc gia được đề cập trong Quy tắc vận chuyển.

![Country Specific Shipping Rules](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/country-specific-shipping-rules.gif)

#### Tài khoản vận chuyển

Nếu phí vận chuyển được áp dụng dựa trên Quy tắc vận chuyển, thì các giá trị khác như Tài khoản vận chuyển, Trung tâm chi phí cũng sẽ cần thiết để thêm dòng vào bảng Thuế và các khoản phí khác của giao dịch. Do đó, các chi tiết này cũng được theo dõi trong Quy tắc vận chuyển.

![Shipping Account](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/shipping-account.png)

#### Áp dụng Quy tắc vận chuyển

Dưới đây là một ví dụ về cách phí vận chuyển được tự động áp dụng trên Đơn bán hàng dựa trên Quy tắc vận chuyển.

![Shipping Rule in Sales Order](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/shipping-rule-in-sales-order.gif)

{next}