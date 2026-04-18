<!-- add-breadcrumbs -->
# Quản lý tồn kho theo Lô hàng

Tập hợp các mặt hàng có cùng đặc tính và thuộc tính có thể được nhóm trong một Lô hàng duy nhất. Ví dụ, các mặt hàng dược phẩm được quản lý theo lô để có thể theo dõi cùng lúc ngày sản xuất và ngày hết hạn.

Để duy trì các lô hàng cho một Mặt hàng, bạn cần thiết lập 'Has Batch No' thành "Yes" trong Danh mục Mặt hàng (Item Master).

<img alt="Batch Item" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/batchwise-stock-1.png">

Bạn có thể tạo một Lô hàng mới từ:

`Kho > Chứng từ > Lô hàng > Mới`

Đọc [Lô hàng](batch.html) để tìm hiểu thêm.

Đối với mặt hàng có quản lý theo lô, việc cập nhật Số lô (Batch No.) trong các giao dịch kho (Phiếu nhập hàng & Phiếu giao hàng) là bắt buộc.

#### Phiếu nhập hàng (PR)

Khi tạo Phiếu nhập hàng, bạn nên tạo Lô hàng mới hoặc chọn một Lô hàng đã có sẵn trong danh mục. Một Lô hàng có thể được liên kết với một Mặt hàng theo lô.

<img alt="Batch in Purchase Receipt" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/batchwise-stock-2.png">

#### Phiếu giao hàng (DN)

Xác định Lô hàng trong bảng Mặt hàng của Phiếu giao hàng. Nếu mặt hàng theo lô được thêm vào dưới dạng Gói sản phẩm (Product Bundle), bạn cũng có thể cập nhật Số lô của nó trong bảng Phiếu đóng gói.

<img alt="Batch in Delivery Note" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/batchwise-stock-3.png">

#### Các tính năng nâng cao trong v16

Trong phiên bản v16, việc quản lý lô hàng và tồn kho được tăng cường với các tính năng sau:

*   **Hệ thống Giữ hàng (Stock Reservation System):** Cho phép giữ trước số lượng tồn kho theo Lô hàng hoặc Số sê-ri cho các Đơn bán hàng (SO) hoặc Lệnh sản xuất, giúp đảm bảo khả năng cung ứng.
*   **Báo cáo Truy xuất nguồn gốc Số sê-ri/Lô hàng (Serial/Batch Traceability Report):** Cung cấp cái nhìn toàn diện về lịch sử di chuyển của một Lô hàng cụ thể từ khi nhập kho đến khi xuất kho.
*   **Chi phí cập bến cho Phiếu kho (Landed Cost cho Stock Entry):** Cho phép phân bổ các chi phí mua hàng (vận chuyển, thuế,...) trực tiếp vào giá trị của Lô hàng khi thực hiện Phiếu kho.
*   **Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting):** Tối ưu hóa việc theo dõi giá trị tồn kho chi tiết đến từng mặt hàng và lô hàng cụ thể.
*   **Xem trước Sổ cái (Ledger Preview):** Cho phép kiểm tra nhanh các bút toán (JE) liên quan đến biến động của Lô hàng ngay tại giao diện quản lý kho.

#### Báo cáo số dư tồn kho theo Lô hàng

Để kiểm tra báo cáo số dư tồn kho theo lô hàng, hãy đi tới:

`Kho > Báo cáo tiêu chuẩn > Lịch sử số dư theo Lô hàng`

<img alt="Batchwise Stock Balance" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/batchwise-stock-4.png">

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/J0QKl7ABPKM?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

{next}