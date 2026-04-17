<!-- add-breadcrumbs -->

# Báo cáo Sổ cái Kho

**Báo cáo Sổ cái Kho là một bản ghi chi tiết giúp theo dõi các biến động kho của một công ty.**

Các giao dịch nhập hoặc xuất liên quan đến Sản xuất, Mua hàng, Bán hàng và Chuyển kho được ghi lại trong Sổ cái Kho, sau đó sẽ được phản ánh trong Báo cáo Sổ cái Kho.

Báo cáo này phản ánh số lượng và giá trị của hàng tồn kho **được xuất, nhận hoặc chuyển** cùng với thông tin chi tiết về mặt hàng và kho hàng.

Báo cáo này có thể được tham chiếu khi hệ thống **Kiểm kê thường xuyên** được bật, vì báo cáo này phản ánh lịch sử của tất cả các giao dịch kho của bạn. Nó cung cấp một cái nhìn chi tiết hơn về các giao dịch kho.

## Các thuộc tính của Báo cáo Sổ cái Kho

* **Incoming Rate (Đơn giá nhập)**: Phản ánh giá trị thực tế của hàng tồn kho khi được đưa vào kho của bạn.
Nó phản ánh cùng một giá trị như đã nhập trong trường *Rate* của chứng từ.

* **Balance Value (Giá trị tồn kho)**: Đại diện cho tổng giá trị của lượng hàng tồn kho còn lại. Đây là tích của Giá trị tính giá (Valuation Rate) và Số lượng tồn (Balance Quantity) của một mặt hàng.

* **Valuation Rate (Giá trị tính giá)**: Được tính toán dựa trên phương pháp tính giá đã chọn.

Dưới đây là cách Báo cáo Sổ cái Kho hiển thị một **Phiếu kho** loại *Phiếu nhập vật tư*.

![Stock Ledger Report](/docs/v13/assets/img/stock/stock-ledger.png)

Nó hiển thị một mặt hàng **Chair** với số lượng *1000 đơn vị* với Đơn giá nhập (Giá cơ bản) là *Rs.3000* được nhận vào kho *Stores - L*, cùng với việc tính toán Giá trị tính giá và Giá trị tồn kho.

Bạn có thể nhấp vào **Voucher #** để mở chứng từ mà giao dịch này được tạo ra.

Sổ cái Kho được tạo ra từ các giao dịch sau:

-   Hóa đơn bán hàng, Hóa đơn mua hàng (khi đã chọn *Update Stock*)
-   Phiếu giao hàng
-   Phiếu nhập hàng
-   Phiếu kho
-   Đối chiếu tồn kho

Bạn có thể thêm các trường từ các DocType đã đề cập ở trên bằng cách nhấp vào Menu > Add Column.