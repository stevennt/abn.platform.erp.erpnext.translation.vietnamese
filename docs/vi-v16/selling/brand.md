<!-- add-breadcrumbs -->
# Thương hiệu

**Thương hiệu dùng để định danh các mặt hàng với một tên gọi cụ thể.**

Thông thường, Thương hiệu là nhà sản xuất hoặc đơn vị đóng gói một sản phẩm cụ thể. Ví dụ, Apple là một thương hiệu sản xuất máy tính xách tay. Thương hiệu không nhất thiết phải là [Nhà sản xuất](../stock/manufacturer.md) của một Mặt hàng, nó chỉ là tên gọi mà sản phẩm được bán ra. Ví dụ, nếu bạn sản xuất cốc nhựa, bạn có thể cấp phép cho một thương hiệu lớn để họ bán sản phẩm đó dưới Thương hiệu của họ.

Trong ERPNext v16, Thương hiệu có thể được gán cho các Mặt hàng để định danh, thiết lập các giá trị mặc định và hỗ trợ quản lý các tính năng nâng cao như [Dự trữ tồn kho](../stock/stock-reservation.md).

Để truy cập danh sách Thương hiệu, hãy đi đến:

> Trang chủ > Bán hàng > Bán hàng > Thương hiệu

## 1. Cách tạo Thương hiệu
1. Đi đến danh sách Thương hiệu và nhấn vào Mới.
1. Nhập tên Thương hiệu và nhập mô tả nếu cần.
1. Lưu.

    ![Brand](https://docs.erpnext.com/docs/v16/assets/img/selling/brand.png)

Giờ đây Thương hiệu này có thể được liên kết với các Mặt hàng khác nhau.

![Brand in Item](https://docs.erpnext.com/docs/v16/assets/img/selling/brand-in-item.png)

## 2. Các tính năng
### 2.1 Thiết lập mặc định cho các Mặt hàng thuộc Thương hiệu này

![Brand Defaults](https://docs.erpnext.com/docs/v16/assets/img/selling/brand-defaults.png)

Các giá trị mặc định sau đây có thể được thiết lập cho một Thương hiệu. Khi gán thương hiệu này cho một Mặt hàng, các giá trị mặc định đã thiết lập sẽ được tự động lấy ra khi thực hiện các giao dịch Bán hàng/Mua hàng với Mặt hàng thuộc Thương hiệu này.

* **Kho mặc định**: Kho mà từ đó Mặt hàng sẽ được lấy ra/lưu trữ tùy thuộc vào giao dịch.
* **Bảng giá mặc định**: Bảng giá được thiết lập ở đây sẽ được lấy ra trong các giao dịch Mua hàng/Bán hàng.

#### Mặc định Mua hàng
Khi thực hiện các giao dịch Mua hàng như [Đơn mua hàng](../buying/purchase-order.md), [Phiếu nhập hàng](../stock/purchase_receipt.md), hoặc [Hóa đơn mua hàng](../accounts/purchase_invoice.md), các giá trị mặc định được thiết lập ở đây sẽ được lấy ra khi chọn Mặt hàng thuộc Thương hiệu này.

* Trung tâm chi phí mua hàng mặc định
* Nhà cung cấp mặc định
* Tài khoản chi phí mặc định

#### Mặc định Bán hàng
Khi thực hiện các giao dịch Bán hàng như [Đơn bán hàng](sales-order.md), [Phiếu giao hàng](../stock/delivery_note.md), hoặc [Hóa đơn bán hàng](../accounts/sales_invoice.md), các giá trị mặc định được thiết lập ở đây sẽ được lấy ra khi chọn Mặt hàng thuộc Thương hiệu này.

* Trung tâm chi phí bán hàng mặc định
* Tài khoản thu nhập mặc định

### 2.2 Các tính năng mới trong v16
Trong phiên bản v16, việc quản lý Thương hiệu và Mặt hàng được tối ưu hóa để hỗ trợ quy trình kinh doanh phức tạp hơn:

* **Nút bấm SO/Quotation trên Khách hàng**: Tại form [Khách hàng](customer.md), các nút bấm để tạo nhanh [Đơn bán hàng](sales-order.md) hoặc Báo giá giúp rút ngắn quy trình bán hàng cho các mặt hàng thuộc thương hiệu đã chọn.
* **Cutoff date cho Phiếu giao hàng (DN) từ Đơn bán hàng (SO)**: Cho phép kiểm soát ngày chốt dữ liệu khi tạo [Phiếu giao hàng](../stock/delivery_note.md) từ [Đơn bán hàng](sales-order.md), giúp quản lý chính xác kỳ kế toán và tồn kho.
* **Dự trữ tồn kho (Stock Reservation)**: Hỗ trợ việc giữ hàng trong [Kho](../stock/warehouse.md) cho các mặt hàng thuộc Thương hiệu nhất định dựa trên các đơn hàng đã được [Xác nhận](sales-order.md), đảm bảo không bị xuất nhầm cho các đơn hàng khác.

## 3. Các chủ đề liên quan
1. [Đơn mua hàng](../buying/purchase-order.md)
1. [Đơn bán hàng](sales-order.md)
1. [Phiếu nhập hàng](../stock/purchase_receipt.md)
1. [Phiếu giao hàng](../stock/delivery_note.md)
1. [Hóa đơn bán hàng](../accounts/sales_invoice.md)
1. [Hóa đơn mua hàng](../accounts/purchase_invoice.md)

{next}