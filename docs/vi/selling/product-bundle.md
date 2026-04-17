<!-- add-breadcrumbs -->
# Gói sản phẩm

**Gói sản phẩm là một danh mục chính nơi bạn có thể liệt kê các mặt hàng hiện có được đóng gói cùng nhau và bán dưới dạng một bộ (hoặc gói).**

Ví dụ, khi bạn bán một chiếc điện thoại thông minh, bạn cần đảm bảo rằng bộ sạc, cáp và que chọc sim được giao cùng với nó và mức tồn kho của các mặt hàng này sẽ bị ảnh hưởng.
Để giải quyết tình huống này, bạn có thể tạo một Gói sản phẩm cho mặt hàng chính, tức là điện thoại thông minh. Sau đó, liệt kê các mặt hàng được giao bao gồm điện thoại thông minh + bộ sạc + cáp + que chọc sim dưới dạng các "Mặt hàng con".

Gói sản phẩm có thể được xem như một "Định mức nguyên vật liệu" ở phía Bán hàng.

Dưới đây là các bước để thiết lập Gói sản phẩm và sử dụng nó trong các giao dịch bán hàng.

Để truy cập gói sản phẩm, hãy đi đến:
> Trang chủ > Bán hàng > Mặt hàng và Định giá > Gói sản phẩm

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Gói sản phẩm, bạn nên tạo các mục sau trước:

* [Mặt hàng](../stock/item.md)

## 2. Cách tạo Gói sản phẩm
1. Đi đến danh sách Gói sản phẩm, nhấn vào Mới.
2. Chọn Mặt hàng cha, tạo mới nếu chưa được tạo. Đảm bảo rằng mục Duy trì tồn kho không được chọn khi tạo Mặt hàng cha. Ví dụ: Bộ đồ ăn.
1. Nhập giá cho mặt hàng cha, giá này sẽ được lấy khi thực hiện giao dịch.
1. Bạn có thể nhập mô tả để sử dụng nội bộ.
3. Nhập các sản phẩm cần đóng gói vào bảng Mặt hàng và nhập số lượng của chúng.
4. Lưu.
<img class="screenshot" alt="Product Bundle" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/product-bundle.png">

### 2.1 Chọn Mặt hàng cha

Trong danh mục Gói sản phẩm, có hai phần. Phần "Mặt hàng cha" và Danh sách các mặt hàng sẽ được giao (Mặt hàng con).

"Mặt hàng cha" nên được xem như một vật chứa hoặc mặt hàng ảo chứ không phải là một sản phẩm vật lý.
"Mặt hàng cha" phải là một <b>mặt hàng không quản lý kho</b>. Để tạo một <b>mặt hàng không quản lý kho</b>, bạn phải bỏ chọn "Duy trì tồn kho" trong Biểu mẫu Mặt hàng.
Đây là một mặt hàng không quản lý kho vì không có tồn kho được duy trì cho nó mà chỉ duy trì cho các "Mặt hàng con".
Nếu bạn muốn duy trì tồn kho cho Mặt hàng cha, bạn phải tạo Định mức nguyên vật liệu (BOM) thông thường
và đóng gói chúng bằng các Giao dịch Phiếu kho.

### 2.2 Chọn Mặt hàng con

Trong bảng Mặt hàng, bạn sẽ liệt kê tất cả các mặt hàng con mà chúng ta quản lý tồn kho và sẽ được giao cho khách hàng.
Lưu ý: "Mặt hàng cha" chỉ là ảo, vì vậy sản phẩm chính của bạn (một chiếc điện thoại thông minh trong ví dụ của chúng ta) cũng phải được liệt kê trong Danh sách các Mặt hàng con (hoặc Gói hàng).

## 3. Các tính năng
### 3.1 Gói sản phẩm trong các Giao dịch bán hàng

Khi thực hiện các giao dịch Bán hàng (Hóa đơn bán hàng, Đơn bán hàng, Phiếu giao hàng), Mặt hàng cha sẽ được chọn trong bảng mặt hàng chính.

<img class="screenshot" alt="Product Bundle" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/selling/product-bundle.gif">

Khi chọn một Mặt hàng cha trong bảng mặt hàng chính, các mặt hàng con của nó sẽ được lấy vào bảng Phiếu đóng gói của giao dịch. Nếu mặt hàng con là mặt hàng có số serial, bạn sẽ có thể chỉ định Số serial của nó
ngay tại bảng Phiếu đóng gói. Khi Xác nhận giao dịch, hệ thống sẽ giảm mức tồn kho của các mặt hàng con từ kho được chỉ định trong bảng Phiếu đóng gói.

<div class="well"><b>Sử dụng Gói sản phẩm để Quản lý Ưu đãi/Chương trình:</b>
<br>
Điều này được phát hiện khi một khách hàng kinh doanh các sản phẩm dinh dưỡng yêu cầu một tính năng để quản lý các ưu đãi như "Mua một tặng một". Để quản lý điều này, ông ấy đã tạo một mặt hàng không quản lý kho để làm Mặt hàng cha. Trong phần mô tả mặt hàng, ông ấy nhập chi tiết ưu đãi kèm theo hình ảnh mặt hàng hiển thị ưu đãi đó. Sản phẩm có thể bán được được chọn trong Mục gói hàng với số lượng là hai. Do đó, mỗi khi họ bán một số lượng mặt hàng cha theo ưu đãi này, hệ thống sẽ trừ hai số lượng sản phẩm từ Kho.</div>

### 4. Các chủ đề liên quan
1. [Mặt hàng](../stock/item.md)

{next}