<!-- add-breadcrumbs -->
# Thương hiệu

**Thương hiệu dùng để định danh các mặt hàng với một tên gọi cụ thể.**

Thông thường, Thương hiệu là nhà sản xuất hoặc đơn vị đóng gói một sản phẩm cụ thể. Ví dụ, Apple là một thương hiệu sản xuất máy tính xách tay. Thương hiệu không nhất thiết phải là [Nhà sản xuất](/docs/v13/user/manual/en/stock/manufacturer) của một Mặt hàng, nó chỉ là tên gọi mà sản phẩm được bán ra. Ví dụ, nếu bạn sản xuất cốc nhựa, bạn có thể cấp phép cho một thương hiệu lớn để họ bán sản phẩm đó dưới Thương hiệu của họ.

Trong ERPNext, Thương hiệu có thể được gán cho các Mặt hàng để định danh và thiết lập một số giá trị mặc định.

Để truy cập danh sách Thương hiệu, hãy đi đến:

> Trang chủ > Bán hàng > Bán hàng > Thương hiệu

## 1. Cách tạo Thương hiệu
1. Đi đến danh sách Thương hiệu và nhấn vào Mới.
1. Nhập tên Thương hiệu và nhập mô tả nếu cần.
1. Lưu.

    ![Brand](/docs/v13/assets/img/selling/brand.png)

Giờ đây Thương hiệu này có thể được liên kết với các Mặt hàng khác nhau.

![Brand in Item](/docs/v13/assets/img/selling/brand-in-item.png)

## 2. Các tính năng
### 2.1 Thiết lập mặc định cho các Mặt hàng thuộc Thương hiệu này

![Brand Defaults](/docs/v13/assets/img/selling/brand-defaults.png)

Các giá trị mặc định sau đây có thể được thiết lập cho một Thương hiệu. Khi gán thương hiệu này cho một Mặt hàng, các giá trị mặc định đã thiết lập sẽ được tự động lấy ra khi thực hiện các giao dịch Bán hàng/Mua hàng với Mặt hàng thuộc Thương hiệu này.

* **Kho mặc định**: Kho mà từ đó Mặt hàng sẽ được lấy ra/lưu trữ tùy thuộc vào giao dịch.
* **Bảng giá mặc định**: Bảng giá được thiết lập ở đây sẽ được lấy ra trong các giao dịch Mua hàng/Bán hàng.

#### Mặc định Mua hàng
Khi thực hiện các giao dịch Mua hàng như Đơn mua hàng, Phiếu nhập hàng, hoặc Hóa đơn mua hàng, các giá trị mặc định được thiết lập ở đây sẽ được lấy ra khi chọn Mặt hàng thuộc Thương hiệu này.

* Trung tâm chi phí mua hàng mặc định
* Nhà cung cấp mặc định
* Tài khoản chi phí mặc định

#### Mặc định Bán hàng
Khi thực hiện các giao dịch Bán hàng như Đơn bán hàng, Phiếu giao hàng, hoặc Hóa đơn bán hàng, các giá trị mặc định được thiết lập ở đây sẽ được lấy ra khi chọn Mặt hàng thuộc Thương hiệu này.

* Trung tâm chi phí bán hàng mặc định
* Tài khoản thu nhập mặc định

## 3. Các chủ đề liên quan
1. [Đơn mua hàng](/docs/v13/user/manual/en/buying/purchase-order)
1. [Đơn bán hàng](/docs/v13/user/manual/en/selling/sales-order)
1. [Phiếu nhập hàng](/docs/v13/user/manual/en/stock/purchase-receipt)
1. [Phiếu giao hàng](/docs/v13/user/manual/en/stock/delivery-note)
1. [Hóa đơn bán hàng](/docs/v13/user/manual/en/accounts/sales-invoice)
1. [Hóa đơn mua hàng](/docs/v13/user/manual/en/accounts/purchase-invoice)

{next}