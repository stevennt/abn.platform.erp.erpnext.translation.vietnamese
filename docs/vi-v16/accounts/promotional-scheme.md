<!-- add-breadcrumbs -->

# Chương trình khuyến mãi

**Chương trình khuyến mãi là một khoản chiết khấu tạm thời cho một hoặc nhiều mặt hàng.**

Các chương trình khuyến mãi giúp doanh nghiệp thành công hơn nhờ mức giá thấp hơn trong một khoảng thời gian giới hạn để thu hút thêm Khách hàng. Chúng có thể được cấu hình dễ dàng trong ERPNext. Một Chương trình khuyến mãi được liên kết với một [Pricing Rule](pricing-rule.md), dựa trên từng hệ thống mức (slab) để tạo ra Quy tắc định giá đó.

Khi tạo một Chương trình khuyến mãi, hệ thống sẽ tạo ra một [Pricing Rule](pricing-rule.md). Một Chương trình khuyến mãi có thể có nhiều Quy tắc định giá liên kết với nó. Trong ERPNext, Chương trình khuyến mãi là một cách dễ dàng hơn để quản lý giá trên nhiều Mặt hàng/Nhóm mặt hàng dựa trên các bên và điều kiện khác nhau.

Để truy cập danh sách Chương trình khuyến mãi, hãy đi tới:
> Home > Selling > Items and Pricing > Promotional Scheme

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Chương trình khuyến mãi, bạn nên tạo các mục sau trước:

1. [Item](../stock/item.md)
1. [Item Group](../stock/item-group.md)
1. [Customer](../selling/customer-list.md)
1. [Supplier](../buying/supplier.md)

## 2. Cách tạo Chương trình khuyến mãi

1. Đi tới danh sách Chương trình khuyến mãi và nhấn **New**.
1. Nhập tiêu đề cho quy tắc.
1. Chọn **Áp dụng cho (Apply On)** như Mã mặt hàng (Item Code), Nhóm mặt hàng (Item Group), Thương hiệu (Brand), hoặc Giao dịch (Transaction). Chọn Giao dịch sẽ áp dụng chương trình cho tổng số tiền của giao dịch.
1. Dựa trên 'Apply On', hệ thống sẽ cho phép bạn chọn Mã mặt hàng / Nhóm mặt hàng / Thương hiệu trong bảng.
1. Chọn xem chương trình dành cho Bán hàng (Selling), Mua hàng (Buying), hoặc cả hai và thiết lập thông tin bên liên quan.
1. Trong bảng **Mức chiết khấu giá (Price Discount Slabs)**, thiết lập chiết khấu giá, chiết khấu sản phẩm.
1. Người dùng cũng có thể áp dụng chiết khấu cho Mã mặt hàng / Nhóm mặt hàng / Thương hiệu khác bằng cách chọn giá trị cho trường **Áp dụng quy tắc cho mục khác (Apply Rule On Other)**.

 ![Promotional Scheme](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/promotional-schemes.png)

1. **Lưu**.

> Lưu ý: Khi **Lưu** một Chương trình khuyến mãi, một Quy tắc định giá mới sẽ được tạo.

### 2.1 Các trường bổ sung khi tạo Chương trình khuyến mãi

#### Điều kiện hỗn hợp (Mixed Conditions)
Nếu bạn chọn hai hoặc nhiều Mặt hàng và thiết lập Số lượng Tối thiểu và Tối đa. Chương trình khuyến mãi sẽ chỉ được áp dụng nếu tổng số lượng các Mặt hàng khớp với số lượng đã thiết lập. Ví dụ, bạn tạo một Chương trình khuyến mãi cho Mặt hàng 1 và Mặt hàng 2 và thiết lập Số lượng Tối thiểu và Tối đa là 30, Chương trình khuyến mãi sẽ chỉ được áp dụng nếu tổng số lượng là 30.

#### Có tính lũy kế (Is Cumulative)
Bật tùy chọn này cho phép Chương trình khuyến mãi được áp dụng theo kiểu lũy kế. Bạn cần thiết lập 'Min Amt' (Số tiền tối thiểu) và 'Max Amt' (Số tiền tối đa) cho việc này.

Xét một kịch bản trong đó Số tiền tối thiểu là 1.500 và Số tiền tối đa là 2.000. Bây giờ, nếu một giao dịch được tạo với số tiền 1.400 thì Chương trình khuyến mãi sẽ không được áp dụng. Tuy nhiên, khi tạo hóa đơn thứ hai với số tiền 600, Chương trình khuyến mãi sẽ được áp dụng. Điều này xảy ra vì tổng số tiền (lũy kế) của các hóa đơn cộng lại là 2.000. Lưu ý rằng chiết khấu sẽ chỉ được áp dụng cho giao dịch mới nhất vượt qua hạn mức lũy kế.

Điều này có thể hữu ích để giảm giá nếu một Khách hàng mua một Mặt hàng nhiều lần và bạn muốn thưởng cho họ bằng các mức chiết khấu/giá đặc biệt.

## 3. Các tính năng

### 3.1 Áp dụng chương trình cho mặt hàng khác (Apply Scheme On Other Item)
Tính năng này kiểm tra điều kiện trên Mặt hàng đầu tiên nhưng áp dụng chương trình/chiết khấu/đơn giá cho một Mặt hàng khác.

Ví dụ, thiết lập Mặt hàng 1 và Mặt hàng 2 trong bảng 'Apply Rule On' và thiết lập 'Apply Rule On Other' là Mặt hàng 3. Bây giờ, nếu giao dịch có Mặt hàng 1, Mặt hàng 2 và Mặt hàng 3, Quy tắc định giá sẽ được áp dụng cho Mặt hàng 3 vì hai Mặt hàng đầu tiên đã có mặt trong giao dịch.

### 3.2 Thông tin bên liên quan (Party Information)

Thiết lập xem Chương trình khuyến mãi dành cho việc Bán hay Mua Mặt hàng.

Dựa trên lựa chọn của bạn, bạn có thể thiết lập khả năng áp dụng cho một trong các danh mục chính sau.

* [Customer](../selling/customer-list.md)
* [Customer Group](../CRM/customer-group.md)
* [Territory](../selling/territory.md)
* [Sales Partner](../selling/sales-partner.md)
* [Campaign](../CRM/campaign.md)
* [Supplier](../buying/supplier.md)
* Nhóm Nhà cung cấp (Supplier Group)

### 3.3 Hiệu lực (Validity)
Bạn cũng có thể thiết lập một khoảng ngày mà Chương trình khuyến mãi có hiệu lực. Điều này hữu ích cho các chương trình khuyến mãi bán hàng. Nếu để trống các ngày, Chương trình khuyến mãi sẽ không có giới hạn về khung thời gian.

**Tiền tệ (Currency)**: Thiết lập một Tiền tệ ở đây sẽ khiến Chương trình khuyến mãi chỉ được áp dụng khi Tiền tệ trong giao dịch giống với Tiền tệ đã thiết lập.

### 3.4 Mức chiết khấu giá (Price Discount Slabs)

**Mô tả quy tắc (Rule Description)**: Nhập mô tả để ghi chú về nội dung của Chương trình khuyến mãi này.

#### Số lượng và Số tiền
Chỉ định số lượng tối thiểu, số lượng tối đa, số tiền tối thiểu hoặc số tiền tối đa của một Mặt hàng khi Chương trình khuyến mãi này được áp dụng.

Lưu ý rằng nếu số lượng hoặc số tiền thấp hơn hoặc vượt quá các hạn mức được thiết lập ở đây, Chương trình khuyến mãi sẽ không được áp dụng. Tuy nhiên, nó sẽ được áp dụng nếu bạn đã bật các tùy chọn Điều kiện hỗn hợp (Mixed Conditions) hoặc Lũy kế (Cumulative).

### Thiết lập Chiết khấu/Đơn giá
* **Đơn giá (Rate)**: