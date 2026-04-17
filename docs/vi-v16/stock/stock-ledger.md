# Báo cáo Sổ cái Kho

**Báo cáo Sổ cái Kho là bản ghi chi tiết giúp theo dõi mọi biến động về số lượng và giá trị của hàng tồn kho trong doanh nghiệp.**

Các giao dịch nhập hoặc xuất liên quan đến Sản xuất, Mua hàng, Bán hàng và Chuyển kho được ghi lại trong Sổ cái Kho, sau đó sẽ được phản ánh trực tiếp trong Báo cáo Sổ cái Kho.

Báo cáo này phản ánh số lượng và giá trị của hàng tồn kho **được xuất, nhận hoặc chuyển** cùng với thông tin chi tiết về Mặt hàng và Kho.

Trong phiên bản v16, báo cáo này được cải tiến để hỗ trợ quản lý chặt chẽ hơn thông qua hệ thống **Giữ hàng (Stock Reservation)**, khả năng **Truy xuất nguồn gốc Lô hàng/Số Serial (Serial/Batch Traceability)** và **Tính giá vốn hàng nhập kho (Landed Cost)** cho Phiếu kho.

## Các thuộc tính của Báo cáo Sổ cái Kho

* **Incoming Rate (Đơn giá nhập)**: Phản ánh giá trị thực tế của hàng tồn kho khi được đưa vào kho. Giá trị này tương ứng với trường *Rate* trong chứng từ, đã bao gồm các chi phí cấu thành nếu sử dụng tính năng *Landed Cost*.

* **Balance Value (Giá trị tồn kho)**: Đại diện cho tổng giá trị của lượng hàng tồn kho còn lại. Đây là tích của Giá trị tính giá (Valuation Rate) và Số lượng tồn (Balance Quantity) của một Mặt hàng.

* **Valuation Rate (Giá trị tính giá)**: Được tính toán dựa trên phương pháp tính giá (như FIFO hoặc Moving Average) đã được thiết lập cho Mặt hàng.

* **Ledger Preview (Xem trước Sổ cái)**: Tính năng mới cho phép người dùng xem nhanh các bút toán kế toán liên quan trực tiếp đến giao dịch kho mà không cần chuyển sang sổ cái kế toán.

Dưới đây là ví dụ về cách Báo cáo Sổ cái Kho hiển thị một **Phiếu kho** loại *Phiếu nhập vật tư*.

![Stock Ledger Report](https://docs.erpnext.com/docs/v16/assets/img/stock/stock-ledger.png)

Ví dụ hiển thị một Mặt hàng **Chair** với số lượng *1000 đơn vị*, Đơn giá nhập (Giá cơ bản) là *3.000 VNĐ* được nhận vào Kho *Stores - L*, cùng với các tính toán về Giá trị tính giá và Giá trị tồn kho.

Bạn có thể nhấp vào **Voucher #** để mở trực tiếp chứng từ gốc đã tạo ra giao dịch này.

## Các giao dịch tạo biến động Sổ cái Kho

Sổ cái Kho được tự động cập nhật từ các giao dịch sau:

- **Hóa đơn** bán hàng, **Hóa đơn** mua hàng (khi chọn *Update Stock*)
- **Phiếu giao hàng** (DN)
- **Phiếu nhập hàng** (PR)
- **Phiếu kho** (SE)
- **Kiểm tra chất lượng** (QI)
- Đối chiếu tồn kho

## Các tính năng nâng cao trong v16

* **Truy xuất nguồn gốc (Traceability):** Dễ dàng theo dõi lịch sử di chuyển của một **Lô hàng (Batch)** hoặc **Số Serial** cụ thể từ lúc nhập kho đến khi xuất kho.
* **Quản lý Giữ hàng (Stock Reservation):** Theo dõi các lượng hàng đã được giữ chỗ cho các Đơn bán hàng (SO) hoặc lệnh sản xuất, giúp phân biệt giữa tồn kho thực tế và tồn kho khả dụng.
* **Kế toán theo Mặt hàng (Item-Level Stock Accounting):** Cung cấp cái nhìn chi tiết về giá trị tồn kho được phân bổ chính xác cho từng Mặt hàng dựa trên các chi phí bổ sung.

Bạn có thể tùy chỉnh hiển thị bằng cách nhấp vào **Menu > Add Column** để thêm các trường từ các DocType liên quan.