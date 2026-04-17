<!-- add-breadcrumbs -->
# Đối chiếu tồn kho

**Đối chiếu tồn kho là quá trình kiểm đếm và đánh giá vật tư/sản phẩm, được thực hiện định kỳ vào cuối năm.**

Việc này được thực hiện nhằm mục đích:

* Giữ cho số lượng kiểm kê thực tế và số lượng trên sổ sách đồng bộ với nhau.
* Định giá tồn kho để chuẩn bị cho các báo cáo kế toán.

Tính năng Đối chiếu tồn kho trong ERPNext v16 được sử dụng để:

* Hạch toán tồn kho đầu kỳ.
* Đối chiếu giữa số lượng trên sổ sách và số lượng thực tế.
* Hỗ trợ quản lý tồn kho nâng cao với hệ thống Giữ chỗ tồn kho (Stock Reservation), Truy xuất nguồn gốc Lô/Số sê-ri (Serial/Batch Traceability) và Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting).

Để truy cập danh sách Đối chiếu tồn kho, hãy đi tới:
> Home > Tồn kho > Công cụ > Đối chiếu tồn kho

## 1. Cách tạo Đối chiếu tồn kho để hạch toán tồn kho đầu kỳ

Sử dụng đối chiếu tồn kho, bạn có thể cập nhật số lượng của các mặt hàng cụ thể trong một kho tại một thời điểm cụ thể. Bạn cũng có thể thêm các Mặt hàng có Số sê-ri hoặc Lô hàng vào kho.

1. Đi tới danh sách Đối chiếu tồn kho, nhấn vào **Mới**.
2. Chọn Mục đích (Purpose) là 'Opening Stock'. Bạn có thể chỉnh sửa Ngày và Giờ hạch toán.
3. Chọn Mã mặt hàng (Item Code), Kho (Warehouse), Số lượng (Quantity), và Giá trị tính giá (Valuation Rate). Nếu có liên quan đến Số sê-ri / Lô hàng, hãy thêm vào.
4. Nếu bạn muốn tự động tạo Số sê-ri / Lô hàng, hãy để trống các trường đó.
    * Để tự động tạo Số sê-ri, bạn cần thiết lập "Serial Number Series" trong danh mục Mặt hàng.
    * Để tự động tạo Lô hàng, bạn cần bật ô "Automatically Create New Batch" trong danh mục Mặt hàng.
5. Tài khoản chênh lệch (Difference Account) sẽ được thiết lập là 'Temporary Opening'.
6. **Lưu** và **Xác nhận**.

    ![Opening Stock](https://docs.erpnext.com/docs/v16/assets/img/stock/opening_stock.png)

> Lưu ý: Tùy chọn Duy trì tồn kho (Maintain Stock) phải được bật trong danh mục Mặt hàng để tính năng này hoạt động.

## 2. Cách tạo Đối chiếu tồn kho để đối chiếu số lượng trên sổ sách và kiểm kê thực tế

Đối chiếu tồn kho là quá trình kiểm đếm và đánh giá hàng tồn kho, được thực hiện định kỳ và vào cuối năm nhằm định giá tổng tồn kho để chuẩn bị các báo cáo kế toán. Trong quá trình này, lượng hàng thực tế sẽ được kiểm tra và ghi nhận vào hệ thống. Lượng hàng thực tế và lượng hàng trên hệ thống phải khớp nhau và chính xác. Nếu không khớp, bạn có thể sử dụng công cụ Đối chiếu tồn kho để đối chiếu số dư tồn kho và giá trị với thực tế.

Để đối chiếu tồn kho:

1. Đi tới danh sách Đối chiếu tồn kho, nhấn vào **Mới**.
2. Chọn Mục đích (Purpose) là 'Stock Reconciliation'. Bạn có thể chỉnh sửa Ngày và Giờ hạch toán.
3. Thiết lập Mã mặt hàng (Item Code), Kho (Warehouse).
4. Số lượng và Giá trị tính giá hiện tại sẽ được lấy ra, hãy thay đổi số lượng nếu cần.
5. Tài khoản chi phí trong Tài khoản chênh lệch (Difference Account) sẽ được mặc định là 'Stock Adjustment'.
6. Trung tâm chi phí (Cost Center) mặc định sẽ là 'Main', thay đổi nếu cần.
7. **Lưu** và **Xác nhận**.

    ![Stock Reconciliation](https://docs.erpnext.com/docs/v16/assets/img/stock/stock_recon.png)

## 3. Các tính năng nâng cao (v16)

### 3.1 Hệ thống Giữ chỗ tồn kho (Stock Reservation System)
Trong phiên bản v16, khi thực hiện đối chiếu hoặc kiểm kê, hệ thống hỗ trợ quản lý các mặt hàng đang được giữ chỗ cho các Đơn bán hàng (SO) hoặc lệnh sản xuất, giúp việc đối chiếu số lượng khả dụng (Available) và số lượng thực tế (Actual) trở nên chính xác hơn.

### 3.2 Truy xuất nguồn gốc Lô hàng/Số sê-ri (Serial/Batch Traceability)
Khi thực hiện đối chiếu tồn kho cho các mặt hàng có quản lý theo Lô hoặc Số sê-ri, bạn có thể sử dụng Báo cáo truy xuất nguồn gốc để đối chiếu chính xác từng mã định danh cụ thể, đảm bảo tính minh bạch trong quản lý chất lượng (QI).

### 3.3 Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting)
ERPNext v16 cho phép đối chiếu giá trị tồn kho chi tiết đến từng mặt hàng, giúp việc hạch toán các bút toán (JE) chênh lệch giá trị kho trở nên chính xác tuyệt đối theo từng dòng vật tư.

### 3.4 Xem trước Sổ cái (Ledger Preview)
Trước khi **Xác nhận** phiếu đối chiếu, người dùng có thể xem trước các tác động của bút toán đối chiếu lên sổ cái để đảm bảo các tài khoản chênh lệch được ghi nhận đúng như dự kiến.

## 4. Các tính năng khác

### 4.1 Tải dữ liệu qua Bảng tính

Nếu bạn có nhiều mặt hàng, bạn có thể tải lên chi tiết thông qua một bảng tính.

1. **Tải xuống Mẫu (Template)**
   Mở một Đối chiếu tồn kho mới và nhấn vào nút **Tải xuống** để tải xuống mẫu dưới định dạng CSV.

   <img class="screenshot" alt="Stock Reconciliation" src="https://docs.erpnext.com/docs/v16/assets/img/stock/stock-recon-1.png">

2. **Nhập dữ liệu vào mẫu CSV.**
   Định dạng CSV có phân biệt chữ hoa chữ thường. Không chỉnh sửa các tiêu đề đã được thiết lập sẵn trong mẫu. Trong cột Mã mặt hàng (Item Code) và Kho (Warehouse), hãy nhập chính xác Mã mặt hàng và Kho đã được tạo trong tài khoản ERPNext của bạn. Đối với số lượng, hãy nhập mức tồn kho mà bạn muốn thiết lập cho mặt hàng đó tại một kho cụ thể.

   <img class="screenshot" alt="Stock Reconciliation" src="https://docs.erpnext.com/docs/v16/assets/img/stock/stock-reco-data.png">

3. **Tải tệp CSV có chứa dữ liệu lên bằng cách nhấn vào nút 'Upload'.**

   <img class="screenshot" alt="Stock Reconciliation" src="https://docs.erpnext.com/docs/v16/assets/img/stock/stock-recon-2.png">

4. **Xem lại, Lưu và Xác nhận.**

   <img class="screenshot" alt="Stock Reconciliation" src="https://docs.erpnext.com/docs/v16/assets/img/stock/stock-reco-upload.gif">

5. **Kiểm tra Báo cáo Sổ cái kho (Stock Ledger Report) để xem số dư tồn kho đã được cập nhật.**

   <img class="screenshot" alt="Stock Reconciliation" src="https://docs.erpnext.com/docs/v16/assets/img/stock/stock-reco-ledger.png">

### 4.2 Lấy Số dư tồn kho và Giá trị tính giá tại một Ngày và Giờ cụ thể

Bạn có thể nhập số dư tồn kho và giá trị tính giá tại một ngày và giờ cụ thể từ một Kho được chọn bằng cách nhấn vào nút **Mặt hàng (Items)**. Bạn có thể cập nhật Số lượng và Giá trị tính giá khi cần thiết.

<img class="screenshot" alt="Stock Reconciliation Items Button" src="https://docs.erpnext.com/docs/v16/assets/img/stock/stock_reconciliation_items_button.gif">

## 5. Cách thức hoạt động của Đối chiếu tồn kho

Một khi phiếu Đối chiếu tồn kho được **Xác nhận** để cập nhật số lượng tại một ngày và giờ cụ thể cho một mặt hàng trong kho, nó sẽ không bị thay đổi bởi các giao dịch kho sau đó, ngay cả khi các giao dịch đó có ngày hạch toán trước ngày đối chiếu tồn kho. Nói cách khác, các bút toán lùi ngày sẽ không làm thay đổi số lượng tồn kho sau khi một bút toán Đối chiếu tồn kho đã được **Xác nhận**.