<!-- add-breadcrumbs -->
#Quản lý tồn kho theo Lô hàng

Tập hợp các mặt hàng có cùng đặc tính và thuộc tính có thể được nhóm trong một Lô hàng duy nhất. Ví dụ, các mặt hàng dược phẩm được quản lý theo lô để có thể theo dõi cùng lúc ngày sản xuất và ngày hết hạn.

Để duy trì các lô hàng cho một Mặt hàng, bạn cần thiết lập 'Has Batch No' thành yes trong Danh mục Mặt hàng (Item Master).

<img alt="Batch Item" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/batchwise-stock-1.png">

Bạn có thể tạo một Lô hàng mới từ:

`Stock > Documents > Batch > New`

Đọc [Stock batch](/docs/v13/user/manual/en/stock/batch.html) để tìm hiểu thêm.

Đối với mặt hàng có quản lý theo lô, việc cập nhật Số lô (Batch No.) trong các giao dịch kho (Phiếu nhập hàng & Phiếu giao hàng) là bắt buộc.

#### Phiếu nhập hàng

Khi tạo Phiếu nhập hàng, bạn nên tạo Lô hàng mới hoặc chọn một Lô hàng đã có sẵn trong danh mục. Một Lô hàng có thể được liên kết với một Mặt hàng theo lô.

<img alt="Batch in Purchase Receipt" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/batchwise-stock-2.png">

#### Phiếu giao hàng

Xác định Lô hàng trong bảng Mặt hàng của Phiếu giao hàng. Nếu mặt hàng theo lô được thêm vào dưới dạng Gói sản phẩm (Product Bundle), bạn cũng có thể cập nhật Số lô của nó trong bảng Phiếu đóng gói.

<img alt="Batch in Delivery Note" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/batchwise-stock-3.png">

#### Báo cáo số dư tồn kho theo Lô hàng

Để kiểm tra báo cáo số dư tồn kho theo lô hàng, hãy đi tới:

Stock > Standard Reports > Batch-wise Balance History

<img alt="Batchwise Stock Balance" class="screenshot" src="{{docs_base_url}}/v13/assets/img/articles/batchwise-stock-4.png">

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/J0QKl7ABPKM?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

{next}