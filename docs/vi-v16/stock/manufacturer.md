<!-- add-breadcrumbs -->
# Nhà sản xuất

**Một nhà sản xuất tạo ra hoặc sản xuất một Mặt hàng.**

Nhà sản xuất có thể không phải là cùng một cá nhân/công ty bán Mặt hàng đó dưới một [Thương hiệu](../selling/brand.md) cụ thể. Ví dụ, Unico Plastics có thể là Nhà sản xuất bàn chải nhựa nhưng nó có thể được bán dưới một Thương hiệu, chẳng hạn như Super Brushes.

Trong ERPNext v16, Nhà sản xuất được sử dụng để định danh các Mặt hàng bằng cách sử dụng một mã số bộ phận cụ thể, hỗ trợ quản lý chặt chẽ trong các quy trình [Tồn kho](../stock/introduction.md) và truy xuất nguồn gốc.

Để truy cập danh sách Nhà sản xuất, hãy đi đến:
> Trang chủ > Kho > Nhà sản xuất

## 1. Cách tạo Nhà sản xuất
1. Đi đến danh sách Nhà sản xuất và nhấn vào **Mới**.
1. Nhập tên Nhà sản xuất và nhập mô tả nếu cần.
1. Nhấn **Lưu**.

    ![Manufacturer](https://docs.erpnext.com/docs/v16/assets/img/stock/manufacturer.png)

Sau khi tạo Nhà sản xuất, thông tin này có thể được thiết lập trong biểu mẫu Mặt hàng với Mã số bộ phận của Nhà sản xuất để định danh.
![Manufacturer](https://docs.erpnext.com/docs/v16/assets/img/stock/manufacturer-part.png)

### 1.1 Chi tiết bổ sung
Các chi tiết sau có thể được thiết lập cho một Nhà sản xuất:

* Website
* Quốc gia
* Logo

## 2. Các tính năng nâng cao trong v16
Trong phiên bản v16, việc quản lý Nhà sản xuất kết hợp chặt chẽ với các tính năng quản lý kho hiện đại:

### 2.1 Truy xuất nguồn gốc Lô hàng/Số sê-ri (Serial/Batch Traceability)
Khi sử dụng Nhà sản xuất để định danh Mặt hàng, hệ thống cho phép truy xuất báo cáo chi tiết về [Lô hàng](../stock/batch-traceability.md) và Số sê-ri, giúp kiểm soát chính xác nguồn gốc sản phẩm từ nhà sản xuất đến khi xuất kho.

### 2.2 Quản lý Tồn kho và Giá vốn
* **Hệ thống Giữ hàng (Stock Reservation System):** Giúp quản lý việc giữ hàng cho các đơn hàng cụ thể dựa trên thông tin nhà sản xuất.
* **Kế toán theo Mặt hàng (Item-Level Stock Accounting):** Cho phép theo dõi giá trị tồn kho chính xác hơn cho từng Mặt hàng được sản xuất.
* **Chi phí thu mua (Landed Cost):** Tự động phân bổ chi phí liên quan vào giá trị [Tồn kho](../stock/introduction.md) khi nhập hàng từ Nhà sản xuất.

## 3. Các tính năng khác
### 3.1 Địa chỉ và Liên hệ

Một [Địa chỉ](../setup/address.md) và [Liên hệ](../setup/contact.md) có thể được thiết lập cho Nhà sản xuất này để phục vụ việc quản lý thông tin liên lạc và vận chuyển.

## 4. Các chủ đề liên quan
1. [Mặt hàng](item.md)
1. [Nhà cung cấp](../buying/supplier.md)
1. [Thương hiệu](../selling/brand.md)
1. [Tồn kho](../stock/introduction.md)