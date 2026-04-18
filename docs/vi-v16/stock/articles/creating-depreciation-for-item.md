<!-- add-breadcrumbs -->
# Bút toán khấu hao

**Câu hỏi:** Một Mặt hàng Tài sản cố định đã được mua và lưu trữ trong kho. Làm thế nào để tạo khấu hao cho Mặt hàng Tài sản cố định đó?

**Trả lời:** Bạn có thể hạch toán bút toán khấu hao tài sản cho mặt hàng tài sản cố định thông qua Phiếu Đối chiếu tồn kho [/docs/v16/user/manual/vi/stock/opening-stock.html].

#### Bước 1:

Trong tệp đính kèm, hãy điền vào các cột thích hợp:

- **Item Code** (Mã mặt hàng) có giá trị cần được khấu hao.
- **Warehouse** (Kho) nơi mặt hàng được lưu trữ.
- **Qty (Số lượng)** Để trống cột này.
- **Valuation Rate** (Giá trị tính giá) sẽ là giá trị của mặt hàng sau khi khấu hao.

<img alt="reorder level" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/fixed-asset-dep-1.gif">

Sau khi cập nhật Giá trị tính giá cho một mặt hàng, hãy quay lại Đối chiếu tồn kho và tải lên tệp .csv đã lưu.

#### Bước 2:

Chọn tài khoản chi phí cho khấu hao trong mục **Difference Account** (Tài khoản chênh lệch). Giá trị được ghi nhận trong tài khoản khấu hao sẽ là khoản chênh lệch giữa giá trị tính giá cũ và giá trị tính giá mới của mặt hàng tài sản cố định, đây chính là số tiền khấu hao thực tế.

<img alt="reorder level" class="screenshot" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/articles/fixed-asset-dep-2.png">

#### Video hướng dẫn Đối chiếu tồn kho

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/0yPgrtfeCTs" frameborder="0" allowfullscreen></iframe>
</div>