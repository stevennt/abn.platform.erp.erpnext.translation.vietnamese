<!-- add-breadcrumbs -->
# Mẫu Thuế theo Mặt hàng

**Mẫu Thuế theo Mặt hàng hữu ích cho việc tính thuế riêng biệt cho từng mặt hàng.**

Nếu một số Mặt hàng của bạn có mức thuế suất khác với mức thuế tiêu chuẩn được chỉ định trong bảng Thuế và Phí, bạn có thể tạo một Mẫu Thuế theo Mặt hàng và gán nó cho một [Mặt hàng](../stock/item.md) hoặc [Nhóm mặt hàng](../stock/item-group.md). Mức thuế được chỉ định trong Mẫu Thuế theo Mặt hàng sẽ được ưu tiên hơn mức thuế tiêu chuẩn được chỉ định trong bảng Thuế và Phí.

Ví dụ, nếu thuế GST 18% được thêm vào bảng Thuế và Phí trong Đơn bán hàng, thì nó sẽ được áp dụng cho tất cả các mặt hàng trong Đơn bán hàng đó. Tuy nhiên, nếu bạn cần áp dụng mức thuế suất khác cho một số mặt hàng, các bước được cung cấp dưới đây.

Để truy cập danh sách Mẫu Thuế theo Mặt hàng, hãy đi đến:
> Trang chủ > Kế toán > Thuế > Mẫu Thuế theo Mặt hàng

Giả sử chúng ta đang tạo một Đơn bán hàng. Chúng ta có mẫu [Thuế và Phí bán hàng](../selling/sales-taxes-and-charges-template.md) chuẩn cho GST 9%. Trong tất cả các Mặt hàng bán, có một Mặt hàng chỉ áp dụng 5% GST, trong khi một mặt hàng khác được miễn thuế (không chịu thuế). Bạn cần chọn Tài khoản thuế và thiết lập mức thuế ghi đè.

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Mẫu Thuế theo Mặt hàng, bạn nên tạo các mục sau trước:

1. [Mặt hàng](../stock/item.md)
1. Bật 'Automatically add Taxes and Charges from Item Tax Template' trong [Cài đặt tài khoản](accounts-settings.md)

## 2. Cách tạo Mẫu Thuế theo Mặt hàng
1. Đi đến danh sách Mẫu Thuế theo Mặt hàng và nhấn Mới.
1. Nhập tiêu đề cho Mẫu Thuế theo Mặt hàng.
1. Chọn một tài khoản và thiết lập mức thuế ghi đè. Thêm các dòng khác nếu cần.
1. Lưu.

Bây giờ Mẫu Thuế theo Mặt hàng đã sẵn sàng để được gán cho một Mặt hàng. Để thực hiện việc này, hãy đi đến Mặt hàng, phần Thuế mặt hàng và chọn một Mẫu Thuế theo Mặt hàng:

![Item Tax In Item](https://docs.erpnext.com/docs/v13/assets/img/accounts/item-tax-in-item.png)

> Lưu ý: Khuyến nghị không sử dụng Mẫu Thuế bán hàng/mua hàng được chọn ở đây trong [Quy tắc thuế](tax-rule.md), vì nó có thể gây xung đột. Nếu bạn muốn sử dụng cùng mức thuế cho Quy tắc thuế và Mẫu Thuế theo Mặt hàng, hãy sử dụng một tên khác cho các Mẫu Thuế bán hàng/mua hàng.

### 2.1 Đề cập Thuế áp dụng trong danh mục Mặt hàng

Các mẫu thuế được thiết lập sẵn với các giá trị. Đối với các mặt hàng có mức thuế suất khác với các mặt hàng khác, bạn cần thay đổi nó trong danh mục Mặt hàng. Đi đến bảng thuế trong Mặt hàng, thêm một dòng, chọn loại thuế và thay đổi mức thuế. Bây giờ, mức thuế mới này sẽ ghi đè lên mẫu khi tạo đơn hàng/hóa đơn. Ví dụ, trong ảnh chụp màn hình dưới đây, bạn có thể thấy mức thuế được đặt là 5 và đó là mức thuế sẽ được áp dụng trong các giao dịch.

![Item-wise Tax](https://docs.erpnext.com/docs/v13/assets/img/accounts/item-wise-tax.png)

Đối với Mặt hàng được miễn thuế hoàn toàn, hãy ghi mức thuế là 0% trong danh mục Mặt hàng.

![Tax Exempted Item](https://docs.erpnext.com/docs/v13/assets/img/accounts/tax-exempted-item.png)

> Lưu ý: Để Mẫu Thuế theo Mặt hàng hoạt động, bạn cần đảm bảo rằng các loại thuế (tài khoản) được thiết lập trong Mẫu Thuế theo Mặt hàng (với mức thuế đã thay đổi) cũng có mặt trong Mẫu Thuế và Phí bán hàng.

> Nếu bạn muốn bao gồm nhiều mặt hàng với các mức thuế suất khác nhau, bạn cần ghi nhận chúng dưới các tài khoản thuế khác nhau. Ví dụ: VAT 14%, VAT 5%, v.v.

### 2.3 Tính toán Thuế trong giao dịch

Trong các giao dịch bán hàng như Báo giá, Đơn bán hàng và Hóa đơn bán hàng, thuế trên các mặt hàng được tính theo Mẫu Thuế và Phí bán hàng đã chọn. Tuy nhiên, nếu một số mặt hàng có liên kết với Mẫu Thuế theo Mặt hàng, thì thuế trên các mặt hàng đó sẽ được tính theo mức thuế được ghi trong Mẫu Thuế theo Mặt hàng thay vì mức thuế được ghi trong Mẫu Thuế và Phí bán hàng.

Ví dụ, trong ảnh chụp màn hình sau, bạn có thể thấy thuế được tính ở mức 3% mặc dù mức thuế theo Mẫu Thuế và Phí bán hàng là 6.25%.

![Tax Calculation](https://docs.erpnext.com/docs/v13/assets/img/accounts/tax-calculation.png)

### 2.4 Mẫu Thuế theo Mặt hàng cho từng Mặt hàng
Bạn cũng có thể chọn thủ công một Mẫu Thuế theo Mặt hàng khác nhau cho mỗi Mặt hàng trong một giao dịch:

![Select Item Tax Template](https://docs.erpnext.com/docs/v13/assets/img/accounts/select-item-tax-template.png)

### 2.5 Thuế theo mặt hàng trên một Nhóm mặt hàng
Bạn có thể gán Mẫu Thuế theo Mặt hàng cho một Nhóm mặt hàng bằng cách sửa đổi bảng Thuế mặt hàng trong phần Thuế mặt hàng bên trong tài liệu Nhóm mặt hàng.

![Item Tax Template in Item Group](https://docs.erpnext.com/docs/v13/assets/img/accounts/item-tax-template-in-item-group.png)

Mẫu Thuế theo Mặt hàng được áp dụng cho một Nhóm mặt hàng sẽ áp dụng cho tất cả các Mặt hàng trong nhóm đó, trừ khi một Mặt hàng riêng lẻ trong Nhóm mặt hàng đó đã được gán Mẫu Thuế theo Mặt hàng của riêng nó.


### 2.6 Hiệu lực của Thuế mặt hàng

<img class="screenshot" alt="Item Tax in Item Group" src="https://docs.erpnext.com/docs/v13/assets/img/accounts/item-tax-in-item.png">

Bạn cũng có thể gán hiệu lực cho các mẫu thuế như hiển thị trong hình ảnh trên.

* Dựa trên ngày hạch toán của giao dịch, một mẫu thuế hợp lệ sẽ được tự động lấy ra.
* Nếu có nhiều hơn một mẫu thuế hợp lệ, thì mẫu thuế hợp lệ đầu tiên từ bảng Thuế mặt hàng sẽ được lấy ra.
* Trong trường hợp không có mẫu thuế hợp lệ nào, thì mẫu thuế đầu tiên không có ngày 'Có hiệu lực từ' trong bảng Thuế mặt hàng sẽ được lấy ra.

> Lưu ý: Khi thêm các mặt hàng trong Hóa đơn mua hàng, ưu tiên đầu tiên sẽ được dành cho 'Ngày hóa đơn nhà cung cấp' thay vì 'Ngày hạch toán' để lấy Mẫu Thuế theo Mặt hàng hợp lệ.

### 2.5 Thuế mặt hàng dựa trên Giá ròng

![Item Tax Net Range](https://docs.erpnext.com/docs/v13/assets/img/accounts/item-tax-net-range.png)

- Đối với nhiều loại hàng hóa và mặt hàng, mức thuế được xác định dựa trên giá cuối cùng của mặt hàng sau khi áp dụng chiết khấu hoặc biên lợi nhuận. Ví dụ: Nếu một chiếc Áo thun được bán với giá ròng lớn hơn 500 Rs thì mức thuế áp dụng sẽ là 12%, nếu không thì sẽ là 5%.

- Bằng cách sử dụng mức giá ròng tối thiểu và tối đa trong thuế mặt hàng, quy trình này có thể được tự động hóa, dựa trên mức giá ròng cuối cùng của mặt hàng, thuế mặt hàng phù hợp sẽ được tự động áp dụng. Nếu