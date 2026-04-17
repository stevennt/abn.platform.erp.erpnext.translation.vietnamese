<!-- add-breadcrumbs -->
# Chuyển đổi sang Kiểm kê thường xuyên

Giá trị tồn kho theo phương pháp thường xuyên được kích hoạt mặc định trong hệ thống ERPNext v16.

Đối với những người dùng hiện đang áp dụng hệ thống kiểm kê định kỳ và muốn chuyển đổi sang hệ thống kiểm kê thường xuyên, vui lòng làm theo các bước được giải thích dưới đây.

### 1. Cách chuyển đổi sang Kiểm kê thường xuyên

1. Để kích hoạt Kiểm kê thường xuyên, hãy đảm bảo rằng Tài khoản hàng tồn kho (Stock in Hand Account) được đồng bộ với giá trị tồn kho thực tế trong (các) Kho của bạn. Để đồng bộ, bạn sẽ phải tạo một Bút toán cho số tiền chênh lệch đối ứng với tài khoản chi phí (thường được sử dụng trong Hóa đơn mua hàng).

  Ví dụ, khi kiểm kê thường xuyên chưa được kích hoạt, bạn chắc chắn đã ghi nhận Chi phí (Giá vốn hàng bán) thông qua các Hóa đơn mua hàng. Bây giờ, bạn sẽ phải tạo một Bút toán để chuyển giá trị của hàng tồn kho hiện có từ tài khoản chi phí sang tài khoản hàng tồn kho.

  Có (Cr.) Tài khoản chi phí ......... XXX

  Nợ (Dr.) Tài khoản hàng tồn kho ... XXX

  Việc này cũng có thể thực hiện theo chiều ngược lại nếu bạn đang chọn tài khoản hàng tồn kho trong Hóa đơn mua hàng.

2. Trước khi kích hoạt Kiểm kê thường xuyên, hãy đảm bảo rằng các Tài khoản Kho (sổ cái) đã được liên kết cho Kho hiện có. Tài khoản kho cho một Kho có thể được thiết lập ở ba cấp độ.

  * Ngay trong chính danh mục Kho (Warehouse master)
  * Trong danh mục Kho cha (Parent Warehouse master)
  * Tài khoản hàng tồn kho mặc định trong danh mục Công ty (Company master), nếu bạn chỉ duy trì một tài khoản hàng tồn kho cho tất cả các Kho.

3. Bút toán để cập nhật tài khoản Hàng đã nhận nhưng chưa lập hóa đơn (Stock Received but not Billed)

  Tài khoản "Hàng đã nhận nhưng chưa lập hóa đơn" là một tài khoản điều chỉnh phản ánh giá trị của hàng hóa mà Phiếu nhập hàng đã được Xác nhận, nhưng Hóa đơn mua hàng vẫn chưa được tạo. Một Bút toán cần được tạo để cập nhật giá trị của các Phiếu nhập hàng đang chờ lập hóa đơn vào tài khoản "Hàng đã nhận nhưng chưa lập hóa đơn".

  Để biết giá trị của hàng đã nhận nhưng chưa lập hóa hàng, bạn có thể tham khảo báo cáo "Hàng đã nhận chờ lập hóa đơn" (Received Items Pending for Billing) trong phân hệ Kế toán.

  Tạo một Bút toán như sau để cập nhật giá trị trong tài khoản Hàng đã nhận nhưng chưa lập hóa đơn.

  Có (Cr.) Hàng đã nhận nhưng chưa lập hóa đơn ........... XXX

  Nợ (Dr.) Tài khoản chi phí (COGS) .................. XXX

4. Thiết lập các tài khoản mặc định sau cho mỗi Công ty

  * Hàng đã nhận nhưng chưa lập hóa đơn (Stock Received But Not Billed)
  * Tài khoản điều chỉnh kho (Stock Adjustment Account)
  * Chi phí bao gồm trong định giá (Expenses Included In Valuation)
  * Trung tâm chi phí (Cost Center)
  * Kích hoạt Kiểm kê thường xuyên (Activate Perpetual Inventory)

5. Đi tới: **Home > Accounting > Company**

    <img class="screenshot" alt="Perpetual Inventory" src="https://docs.erpnext.com/docs/v16/assets/img/accounts/perpetual-1.png">

#### 2. Các tính năng mới trong v16 liên quan đến Kho

* **Hệ thống Giữ hàng (Stock Reservation System):** Cho phép giữ hàng trong Kho dựa trên các Đơn bán hàng (SO) để đảm bảo tính sẵn có.
* **Báo cáo Truy xuất Lô/Số Serial (Serial/Batch Traceability Report):** Theo dõi chi tiết lịch sử của từng Lô hàng hoặc Số Serial từ khi nhập kho đến khi xuất kho.
* **Chi phí mua hàng (Landed Cost) cho Phiếu kho:** Cho phép phân bổ các chi phí liên quan (vận chuyển, thuế...) trực tiếp vào giá trị của Phiếu kho (Stock Entry).
* **Kế toán hàng tồn kho theo từng Mặt hàng (Item-Level Stock Accounting):** Kiểm soát chi tiết giá trị sổ cái cho từng Mặt hàng cụ thể.
* **Xem trước Sổ cái (Ledger Preview):** Xem nhanh các bút toán liên quan trực tiếp từ giao diện quản lý kho.

#### 3. Các chủ đề liên quan
1. [Kế toán hàng tồn kho](https://docs.erpnext.com/docs/v13/user/manual/en/accounting-of-inventory-stock)
1. [Kiểm kê thường xuyên](https://docs.erpnext.com/docs/v13/user/manual/en/perpetual-inventory)