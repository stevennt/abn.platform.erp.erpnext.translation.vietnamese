<!-- add-breadcrumbs -->
# Thuộc tính mặt hàng

**Thuộc tính mặt hàng là các đặc tính được gán cho các Biến thể mặt hàng, dựa vào đó các Biến thể mặt hàng được tạo ra.**

Thuộc tính mặt hàng có thể là màu sắc, kích thước, chiều dài, v.v. Có thể định nghĩa nhiều thuộc tính như nhiều màu sắc khác nhau.

Trong phiên bản v16, việc quản lý thuộc tính kết hợp chặt chẽ với các tính năng mới như **Hệ thống giữ hàng (Stock Reservation System)** và **Báo cáo truy xuất nguồn gốc Lô/Số sê-ri (Serial/Batch Traceability Report)** để đảm bảo quản lý biến thể chính xác trong kho.

<img class="screenshot" alt="Attribute Master" src="https://docs.erpnext.com/docs/v16/assets/img/stock/item-attribute.png">

Để truy cập danh sách Thuộc tính mặt hàng, hãy đi đến:

> Home > Stock > Settings > Item Attribute

## 1. Cách tạo Thuộc tính mặt hàng
1. Đi đến danh sách Thuộc tính mặt hàng, nhấn vào **New**.
1. Nhập tên cho Thuộc tính.
1. Nhập các giá trị thuộc tính vào bảng.
1. **Lưu**.

Các giá trị thuộc tính có thể là dạng số hoặc không phải dạng số.

### 1.1 Thuộc tính không phải dạng số

Đối với các Thuộc tính không phải dạng số, hãy chỉ định các giá trị thuộc tính cùng với chữ viết tắt của nó trong bảng Giá trị thuộc tính.

<img class="screenshot" alt="Attribute Master" src="https://docs.erpnext.com/docs/v16/assets/img/stock/item-attribute-non-numeric.png">

### 1.2 Thuộc tính dạng số
Nếu thuộc tính của bạn là dạng số, hãy chọn **Numeric Values**. Chỉ định Khoảng (Range) và Giá trị bước nhảy (Increment Value). Trong ví dụ sau, chiều dài ống có khoảng từ 0.25 đến 3.0 và bước nhảy là 0.25, vì vậy các biến thể sẽ là 0.25, 0.5, 0.75...3.0.

<img class="screenshot" alt="Attribute Master" src="https://docs.erpnext.com/docs/v16/assets/img/stock/item-attribute-numeric.png">

## 2. Các tính năng nâng cao trong v16 liên quan đến Thuộc tính

Với việc quản lý thuộc tính chi tiết, người dùng có thể tận dụng các tính năng mới sau:

*   **Hệ thống giữ hàng (Stock Reservation System):** Cho phép giữ các biến thể mặt hàng cụ thể (dựa trên thuộc tính) để đảm bảo sẵn sàng cho các Đơn bán hàng (SO) hoặc yêu cầu vật tư (MR).
*   **Truy xuất nguồn gốc (Serial/Batch Traceability):** Theo dõi chính xác các biến thể mặt hàng theo Lô hàng (Batch) hoặc Số sê-ri thông qua các báo cáo chuyên sâu.
*   **Kế toán tồn kho theo từng mặt hàng (Item-Level Stock Accounting):** Tự động hóa việc ghi nhận giá trị kho dựa trên các biến thể đã được định nghĩa.

#### 2. Các chủ đề liên quan
1. [Biến thể mặt hàng](item-variants.md)