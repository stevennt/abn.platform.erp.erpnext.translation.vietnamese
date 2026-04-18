<!-- add-breadcrumbs -->
# Báo giá

**Báo giá là ước tính chi phí của các sản phẩm/dịch vụ mà bạn đang bán cho khách hàng tương lai hoặc khách hàng hiện tại.**

Trong một giao dịch bán hàng, khách hàng có thể yêu cầu một bản ghi chú về các sản phẩm hoặc dịch vụ mà bạn dự định cung cấp cùng với giá cả và các điều khoản hợp tác khác. Bản này có nhiều tên gọi như "Đề xuất", "Ước tính", "Hóa đơn tạm tính" hoặc **Báo giá**.

Để truy cập danh sách Báo giá, hãy đi đến:
> Home > Selling > Sales > Quotation

Một quy trình bán hàng điển hình trông như sau:

![Make Quotation from Opportunity](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/selling-flow-quo.png)

Một Báo giá bao gồm các chi tiết về:

  * Người nhận Báo giá
  * Các Mặt hàng và số lượng bạn đang cung cấp.
  * Đơn giá mà các mặt hàng được chào bán.
  * Các loại thuế áp dụng.
  * Các chi phí khác (như vận chuyển, bảo hiểm) nếu có.
  * Thời hạn hiệu lực của hợp đồng.
  * Thời gian giao hàng.
  * Các điều kiện khác.

> Mẹo: Hình ảnh hiển thị rất tốt trên Báo giá. Hãy đảm bảo các mặt hàng của bạn có đính kèm hình ảnh.


## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Báo giá, bạn nên tạo các thông tin sau trước:

* [Khách hàng](../CRM/customer.md)
* [Khách hàng tiềm năng](../CRM/lead.md)
* [Mặt hàng](../stock/item.md)

## 2. Cách tạo Báo giá
1. Đi đến danh sách Báo giá, nhấn vào Mới.
2. Chọn Báo giá dành cho Khách hàng hay Khách hàng tiềm năng từ trường 'Quotation To'.
3. Nhập tên Khách hàng/Khách hàng tiềm năng.
1. Nhập ngày Có hiệu lực, sau ngày này số tiền báo giá sẽ được coi là không còn hiệu lực.
1. Loại đơn hàng có thể là Bán hàng, Bảo trì, hoặc Giỏ hàng. Giỏ hàng dành cho giỏ hàng trên website và không nhằm mục đích được tạo từ đây.
4. Thêm các Mặt hàng và số lượng của chúng vào bảng mặt hàng, giá sẽ được tự động lấy từ Giá mặt hàng. Bạn cũng có thể lấy các mặt hàng từ một Cơ hội bằng cách nhấn vào Lấy mặt hàng từ > Cơ hội.
5. Thêm các loại thuế và phí bổ sung nếu áp dụng.
6. Lưu.

Bạn cũng có thể tạo Báo giá từ một Cơ hội như sau.

![Make Quotation from Opportunity](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/make-quote-from-opp.png)

## 3. Các tính năng

### 3.1 Địa chỉ và Liên hệ
Trong phần này có bốn trường:

* **Địa chỉ Khách hàng:** Đây là địa chỉ Thanh toán của khách hàng.
* **Địa chỉ Giao hàng:** Địa chỉ nơi các mặt hàng sẽ được giao đến.
* **Người liên hệ:** Nếu khách hàng của bạn là một tổ chức, bạn có thể thêm người cần liên hệ vào trường này.
* **Vùng miền:** Khu vực mà khách hàng thuộc về. Mặc định là Tất cả các vùng.

### 3.2 Tiền tệ và Bảng giá
Bạn có thể thiết lập tiền tệ mà báo giá/đơn bán hàng sẽ được gửi đi. Nếu bạn thiết lập một Bảng giá, thì giá mặt hàng sẽ được lấy từ bảng đó. Việc tích vào Bỏ qua Quy tắc định giá sẽ bỏ qua các Quy tắc định giá đã thiết lập trong Accounts > Pricing Rule.

Đọc về [Bảng giá](../stock/price-lists.md)
và [Giao dịch đa tiền tệ](../accounts/articles/managing-transactions-in-multiple-currency.md)
để biết thêm chi tiết.

### 3.3 Bảng Mặt hàng
Bảng này có thể được mở rộng bằng cách nhấp vào hình tam giác ngược ở phía ngoài cùng bên phải của bảng.

* Khi chọn Mã mặt hàng, các thông tin sau sẽ được tự động lấy về: tên mặt hàng, mô tả, bất kỳ hình ảnh nào nếu có thiết lập, số lượng mặc định là 1, và đơn giá. Bạn có thể thêm chiết khấu trong phần Chiết khấu và Biên lợi nhuận.
* **Trong phần Chiết khấu và Biên lợi nhuận**, bạn có thể thêm biên lợi nhuận bổ sung hoặc đưa ra mức chiết khấu. Cả hai đều có thể được thiết lập dựa trên số tiền hoặc phần trăm. Đơn giá cuối cùng sẽ được hiển thị bên dưới trong phần Đơn giá. Bạn có thể chỉ định một Mẫu thuế mặt hàng được tạo riêng cho một mặt hàng.
* **Trọng lượng mặt hàng** sẽ được lấy về nếu đã được thiết lập trong danh mục Mặt hàng.
* Trong phần **Kho và Tham chiếu**, kho sẽ được lấy từ danh mục Mặt hàng, đây là kho nơi có tồn kho của bạn.
* Trong phần **Lập kế hoạch**, bạn có thể thấy Số lượng dự kiến và số lượng thực tế hiện có. Để biết thêm về các trường này, [nhấp vào đây](../stock/projected-quantity.md). Nếu bạn nhấp vào nút 'Số dư kho', nó sẽ đưa bạn đến một DocType nơi bạn có thể tạo báo cáo tồn kho cho mặt hàng đó.
* **Giỏ hàng**, ghi chú bổ sung dành cho các giao dịch trên website. Các ghi chú về mặt hàng sẽ được lấy về đây khi được thêm thông qua giỏ hàng. Ví dụ: làm món ăn cay hơn. *Được giới thiệu trong v12*
* **Ngắt trang** Sẽ tạo một điểm ngắt trang ngay trước mặt hàng này khi in.

* Bạn có thể chèn các hàng bên dưới/bên trên, nhân bản, di chuyển hoặc xóa các hàng trong bảng này.

* Mẹo: Bạn cũng có thể Tải xuống bảng mặt hàng dưới định dạng CSV và Tải lên cho một giao dịch khác.

Tổng số lượng, đơn giá và trọng lượng tịnh của tất cả các mặt hàng sẽ được hiển thị bên dưới bảng mặt hàng. Đơn giá hiển thị ở đây là giá trước thuế.

### 3.4 Thuế và Phí
Để thêm thuế vào Báo giá, bạn có thể chọn [Mẫu Thuế và Phí bán hàng](sales-taxes-and-charges-template.md) hoặc thêm thuế thủ công trong bảng Thuế và Phí bán hàng.

Tổng thuế và phí sẽ được hiển thị bên dưới bảng. Nhấp vào Chi tiết thuế sẽ hiển thị tất cả các thành phần và số tiền.

![Taxes in Quotation](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/quotation-taxes.png)

Để thêm thuế tự động thông qua Danh mục thuế, hãy truy cập [trang này](../accounts/tax-category.md).

#### Quy tắc vận chuyển
Quy tắc vận chuyển giúp thiết lập chi phí vận chuyển một Mặt hàng. Chi phí thường sẽ tăng theo khoảng cách vận chuyển. Để biết thêm, hãy truy cập trang [Quy tắc vận chuyển](shipping-rule.md).

### 3.5 Chiết khấu bổ sung
Ngoài việc đưa ra chiết khấu cho từng mặt hàng, bạn có thể thêm một khoản chiết khấu cho toàn bộ báo giá trong phần này. Khoản chiết khấu này có thể dựa trên Tổng cộng, tức là sau thuế/phí hoặc Tổng ròng, tức là trước thuế/phí. Chiết khấu bổ sung có thể được áp dụng dưới dạng phần trăm hoặc số tiền.

Đọc [Áp dụng chiết khấu](articles/applying-discount.md) để biết thêm chi tiết.

### 3.6 Điều khoản thanh toán
Đôi khi việc thanh toán không được thực hiện cùng một lúc. Tùy thuộc vào thỏa thuận, một nửa