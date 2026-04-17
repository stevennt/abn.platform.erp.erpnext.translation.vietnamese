<!-- add-breadcrumbs -->
# Biến thể Mặt hàng

**Biến thể Mặt hàng là một phiên bản của một Mặt hàng với các thuộc tính khác nhau như kích thước hoặc màu sắc.**

Ví dụ: Giả sử áo thun là một Mặt hàng và nó có các kích thước và màu sắc khác nhau như nhỏ, vừa, lớn và đỏ, xanh dương, xanh lá. Trong ERPNext, áo thun sẽ được coi là một mẫu Mặt hàng (Item template) và mỗi biến thể sẽ là một Biến thể Mặt hàng (Item Variant).

Một chiếc áo thun *màu xanh dương* cỡ *nhỏ* thay vì chỉ là một chiếc áo thun. Các biến thể mặt hàng cho phép bạn coi các phiên bản *nhỏ*, *vừa* và *lớn* của một chiếc áo thun là các biến thể của cùng một Mặt hàng 'áo thun'.

Nếu không có Biến thể Mặt hàng, bạn sẽ phải coi các phiên bản *nhỏ*, *vừa* và *lớn* của một chiếc áo thun là ba Mặt hàng riêng biệt.

## 1. Sử dụng Biến thể Mặt hàng

Biến thể có thể dựa trên hai yếu tố:

1. Thuộc tính Mặt hàng
1. Nhà sản xuất

> Mẹo: Sau khi mẫu mặt hàng được tạo, khi bạn cập nhật mẫu này, tất cả các biến thể cũng sẽ được cập nhật tương ứng.

### 1.1 Tạo Mẫu Biến thể Mặt hàng

1. Để sử dụng Biến thể Mặt hàng trong ERPNext, hãy tạo một Mặt hàng và tích vào 'Has Variants' trong phần Variants.

1. Mặt hàng đó sau đó sẽ được gọi là 'Template' (Mẫu). Một Mẫu như vậy không còn giống hệt như một 'Mặt hàng' thông thường nữa. Ví dụ, bản thân nó (Mẫu) không thể được sử dụng trực tiếp trong bất kỳ giao dịch nào (Đơn bán hàng, Phiếu giao hàng, Hóa đơn mua hàng).

1. Chỉ có các Biến thể của Mặt hàng (_áo thun màu xanh dương cỡ nhỏ_) mới có thể được sử dụng trong thực tế. Do đó, tốt nhất là nên quyết định xem một mặt hàng 'Có biến thể' (Has Variants) hay không ngay khi tạo nó.
    <img class="screenshot" alt="Has Variants" src="https://docs.erpnext.com/docs/v16/assets/img/stock/item-has-variants.png">

1. Khi chọn 'Has Variants', một bảng sẽ xuất hiện. Hãy chỉ định các thuộc tính biến thể cho Mặt hàng trong bảng. Trong trường hợp thuộc tính có Giá trị số, bạn có thể chỉ định phạm vi và tạo các khoảng dựa trên các giá trị tăng dần.
    <img class="screenshot" alt="Valid Attributes" src="https://docs.erpnext.com/docs/v16/assets/img/stock/item-attributes.png">
> Lưu ý: Bạn không thể thực hiện các Giao dịch đối với một 'Mẫu'.

### 1.2 Tạo các Biến thể Mặt hàng dựa trên Thuộc tính Mặt hàng
Để tạo 'Biến thể Mặt hàng' từ một 'Mẫu', hãy nhấp vào 'Create'. Từ đó, chọn tạo một biến thể duy nhất hoặc nhiều biến thể. Chọn đơn lẻ (Single) rất đơn giản, nơi bạn chỉ tạo một hoặc nhiều thuộc tính và một Mặt hàng sẽ được tạo ra. Khi chọn nhiều biến thể (multiple variants), hãy tích vào các thuộc tính và nhiều mặt hàng sẽ được tạo ra. Ví dụ, nếu bạn chọn Màu sắc: Đỏ, Xanh lá và Kích thước: Nhỏ, Vừa, Lớn, thì 6 biến thể sẽ được tạo ra.

Tạo nhiều biến thể trong ERPNext:

<img class="screenshot" alt="Make Variants" src="https://docs.erpnext.com/docs/v16/assets/img/stock/make-multiple-variants.png">

Để tìm hiểu thêm về cách thiết lập thuộc tính, hãy xem [Thuộc tính Mặt hàng](item-attribute.md)

### 1.3 Biến thể Mặt hàng dựa trên Nhà sản xuất

Để thiết lập các biến thể dựa trên Nhà sản xuất, trong mẫu Mặt hàng của bạn, hãy đặt "Variants Based On" là "Manufacturers".
Trong trường hợp này, để tạo các biến thể, hãy nhấp vào Create > Make Variant. Hệ thống sẽ nhắc bạn chọn một Nhà cung cấp. Bạn cũng có thể tùy chọn nhập Mã phụ tùng của Nhà sản xuất (Manufacturer Part Number).

<img class='screenshot' alt='Setup Item Variant by Manufacturer' src='https://docs.erpnext.com/docs/v16/assets/img/stock/select-mfg-for-variant.png'>

Việc đặt tên cho biến thể sẽ dựa trên tên (ID) của Mặt hàng mẫu với một hậu tố số. Ví dụ: "Screwdriver" sẽ có biến thể là "Screwdriver-1".

## 2. Cập nhật Biến thể Mặt hàng dựa trên Mẫu
Đi đến: **Home > Stock > Items and Pricing > Item Variant Settings**. Các trường hiển thị ở đây cũng sẽ được sao chép sang các biến thể. Theo mặc định, tất cả các trường đều được hiển thị, hãy xóa bất kỳ hàng nào bạn không muốn cập nhật từ mẫu mặt hàng sang các biến thể.

## 3. Video

### 3.1 Tạo Biến thể Mặt hàng từng cái một
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/kogIricF40I?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 3.2 Tạo Biến thể Mặt hàng hàng loạt
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/SngZtDIMdiQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### 4. Các chủ đề liên quan
1. [Nhóm mặt hàng](item-group.md)
1. [Thuộc tính Mặt hàng](item-attribute.md)
1. [Giá Mặt hàng](item-price.md)
1. [Mã hóa Mặt hàng](articles/item-codification.md)