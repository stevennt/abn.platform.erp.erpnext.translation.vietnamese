<!-- add-breadcrumbs -->
# Quy tắc định giá

**Một Quy tắc định giá xác định các quy tắc chiết khấu/định giá được áp dụng dựa trên các điều kiện đã thiết lập.**

Một Quy tắc định giá có nhiều tùy chọn mà bạn có thể sử dụng để kiểm soát giá của một Mặt hàng. Các bộ lọc như số lượng, ngày tháng, nhóm và các điều kiện khác có thể được thiết lập.

Quy tắc định giá có phần tương tự như [Quy tắc thuế](tax-rule.md).

Dưới đây là một số trường hợp có thể được giải quyết bằng Quy tắc định giá:

- Theo chính sách bán hàng khuyến mãi, nếu Khách hàng mua hơn 10 đơn vị của một mặt hàng, họ sẽ được hưởng mức chiết khấu 20%.
- Đối với Khách hàng "XYZ", giá bán cho Mặt hàng cụ thể đó sẽ được cập nhật thành ###.
- Các Mặt hàng thuộc Nhóm mặt hàng cụ thể có cùng giá bán hoặc giá mua.
- Khách hàng thuộc Nhóm khách hàng cụ thể sẽ nhận được giá bán ###, hoặc % Chiết khấu trên Mặt hàng.
- Nhà cung cấp thuộc Nhóm nhà cung cấp cụ thể sẽ được áp dụng giá mua ###.

Để Chiết khấu và Giá trong Bảng giá được tự động áp dụng cho một Mặt hàng, hãy tạo các Quy tắc định giá cho mặt hàng đó.

Để truy cập danh sách Quy tắc định giá, hãy đi tới:
> Home > Accounting > Pricing Rule

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Quy tắc định giá, bạn nên tạo các mục sau trước:

1. [Mặt hàng](../stock/item.md)
1. [Nhóm mặt hàng](../stock/item-group.md)
1. [Khách hàng](../CRM/customer.md)
1. [Nhà cung cấp](../buying/supplier.md)

## 2. Cách tạo Quy tắc định giá
1. Đi tới danh sách Quy tắc định giá và nhấn New.
1. Thiết lập tiêu đề cho quy tắc.
1. Chọn Áp dụng cho (Apply On) từ Mã mặt hàng (Item Code), Nhóm mặt hàng (Item Group), Thương hiệu (Brand), hoặc Giao dịch (Transaction).
1. Chọn bạn muốn áp dụng Chiết khấu giá (Price discount) hay Chiết khấu sản phẩm (Product discount). Nếu bạn muốn tặng sản phẩm miễn phí, hãy chọn chiết khấu sản phẩm.
 ![Pricing Rule](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pricing-rule.png)

1. Đối với một mặt hàng duy nhất, chọn Mã mặt hàng và chọn các mặt hàng đó.
1. Nếu bạn muốn Quy tắc định giá được áp dụng cho tất cả các mặt hàng, hãy chọn 'Nhóm mặt hàng' và chọn **Tất cả nhóm mặt hàng** (nhóm mặt hàng cha).
1. Thiết lập mức chiết khấu/giá cần áp dụng. Để biết thêm, [hãy đi tới phần này](pricing-rule.md#35-price-discount-scheme).
1. Lưu.

### 2.1 Các tùy chọn bổ sung khi tạo Quy tắc định giá

#### Kho
Việc thiết lập một Kho ở đây sẽ khiến Quy tắc định giá chỉ được áp dụng nếu Mặt hàng được chọn từ Kho đã chỉ định tại đây.

#### Áp dụng quy tắc cho (Apply Rule On)
Dựa trên thuộc tính được chọn trong trường 'Apply On', bạn có thể thiết lập Quy tắc định giá dựa trên một trong các mục sau:

* [Mặt hàng](../stock/item.md)
* [Nhóm mặt hàng](../stock/item-group.md)
* Thương hiệu (Brand)
* Giao dịch (Transaction) (trên tổng số tiền của giao dịch)

Trong bảng này, bạn có thể chọn Mặt hàng/Nhóm mặt hàng/Thương hiệu cụ thể. Ví dụ, nếu bạn chọn Áp dụng cho 'Nhóm mặt hàng' và chọn 'Nguyên vật liệu' trong bảng, Quy tắc định giá này sẽ chỉ được áp dụng cho các Mặt hàng thuộc Nhóm 'Nguyên vật liệu'.

**UoM**: Quy tắc định giá sẽ chỉ áp dụng nếu Đơn vị tính (UoM) được thiết lập ở đây khớp với giao dịch.

#### Điều kiện (Condition)

Trong trường này, bạn có thể thêm một điều kiện bằng ngôn ngữ python để kiểm tra so với các giá trị trường trong DocType giao dịch, giống như ví dụ dưới đây cho Hóa đơn bán hàng:
```
customer=='Customer Name' and status!='Overdue'
```

Lưu ý rằng chỉ các điều kiện python trên một dòng mới hoạt động, sử dụng tên trường của DocType mục tiêu.

#### Điều kiện hỗn hợp (Mixed Conditions)
Nếu bạn chọn hai hoặc nhiều Mặt hàng và thiết lập Số lượng Tối thiểu và Tối đa. Quy tắc định giá sẽ chỉ được áp dụng nếu tổng số lượng của các Mặt hàng khớp với số lượng đã thiết lập. Ví dụ, bạn tạo một Quy tắc định giá cho Mặt hàng 1 và Mặt hàng 2 và thiết lập Số lượng Tối thiểu và Tối đa là 30, Quy tắc định giá sẽ chỉ áp dụng nếu tổng số lượng là 30.

#### Có tính lũy kế (Is Cumulative)
Bật tùy chọn này cho phép Quy tắc định giá được áp dụng lũy kế. Bạn cần thiết lập 'Số tiền tối thiểu' (Min Amt) và 'Số tiền tối đa' (Max Amt) cho việc này.

Xét một kịch bản trong đó Số tiền tối thiểu là 1.500 và Số tiền tối đa là 2.000. Bây giờ, nếu một giao dịch được tạo với số tiền 1.400 thì Quy tắc định giá sẽ không được áp dụng. Tuy nhiên, khi tạo hóa đơn thứ hai với số tiền 600, Quy tắc định giá sẽ được áp dụng. Điều này xảy ra vì tổng số tiền (lũy kế) của các hóa đơn cộng lại là 2.000. Lưu ý rằng chiết khấu sẽ chỉ được áp dụng cho giao dịch mới nhất vượt qua giới hạn lũy kế.

Điều này có thể hữu ích để giảm giá nếu một Khách hàng mua một Mặt hàng nhiều lần và bạn muốn thưởng cho họ bằng các mức chiết khấu/giá đặc biệt.

## 3. Các tính năng

### 3.1 Áp dụng quy tắc cho mục khác (Apply Rule On Other)
Tính năng này kiểm tra điều kiện trên Mặt hàng thứ nhất nhưng áp dụng quy tắc cho một Mặt hàng khác.

![Apply Pricing Rule on Other Item](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pricing-rule-on-other-item.png)

Ví dụ, thiết lập Mặt hàng 1 và Mặt hàng 2 trong bảng 'Áp dụng quy tắc cho' và thiết lập 'Áp dụng quy tắc cho mục khác' cho Mặt hàng 3. Bây giờ, nếu giao dịch có Mặt hàng 1, Mặt hàng 2 và Mặt hàng 3, Quy tắc định giá sẽ áp dụng cho Mặt hàng 3 vì hai Mặt hàng đầu tiên đã có mặt trong giao dịch.

### 3.2 Thông tin bên liên quan (Party Information)

Thiết lập xem Quy tắc định giá là dành cho việc Bán hay Mua Mặt hàng.

Dựa trên lựa chọn của bạn, bạn có thể thiết lập khả năng áp dụng cho một trong các danh mục chính sau.

* [Khách hàng](../CRM/customer.md)
* [Nhóm khách hàng](../CRM/customer-group.md)
* Khu vực (selling/territory)
* Đối tác bán hàng (selling/sales-partner)
* Chiến dịch (CRM/campaign)
* [Nhà cung cấp](../buying/supplier.md)
* Nhóm nhà cung cấp

### 3.3 Số lượng và Số tiền
Chỉ định số lượng tối thiểu, số lượng tối đa, số tiền tối thiểu hoặc số tiền tối đa của một Mặt hàng khi Quy tắc định giá này nên được áp dụng.

Lưu ý rằng nếu số lượng hoặc số tiền thấp hơn hoặc vượt quá các giới hạn được thiết lập ở đây, Quy tắc định giá sẽ không được áp dụng. Tuy nhiên, nó sẽ được áp dụng nếu bạn đã bật các tùy chọn Điều kiện hỗn hợp hoặc Lũy kế.

![Pricing Rule Quantity and Amount](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/pricing-rule-quantity-and-amount.png)

### 3.4 Hiệu lực (Validity)
Bạn cũng có thể thiết lập một khoảng thời gian để Quy tắc định giá có hiệu lực. Điều này hữu ích cho một s