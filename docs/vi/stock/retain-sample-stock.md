<!-- add-breadcrumbs -->
# Lưu giữ tồn kho mẫu

**Tồn kho mẫu là một lô của bất kỳ Mặt hàng nào được lưu trữ để phân tích nếu có nhu cầu phát sinh sau này.**

Mặt hàng được lưu trữ tồn kho mẫu có thể là nguyên vật liệu, vật liệu đóng gói hoặc thành phẩm.

## 1. Điều kiện tiên quyết
Trước khi sử dụng tính năng lưu giữ mẫu, bạn nên tạo các mục sau trước:

* [Mặt hàng](/docs/v13/user/manual/en/stock/item)
* [Lô hàng](/docs/v13/user/manual/en/stock/batch)
* [Kho](/docs/v13/user/manual/en/stock/warehouse)

## 1. Cách thiết lập Kho lưu giữ mẫu trong Cài đặt kho

Bạn nên tạo một Kho mới riêng biệt để lưu giữ các mẫu và không sử dụng kho này trong sản xuất.

<img class="screenshot" alt="Sample Retention Warehouse" src="{{docs_base_url}}/v13/assets/img/stock/sample-warehouse.png">

### 1.2 Kích hoạt Lưu giữ mẫu trong danh mục Mặt hàng
Tính năng Lưu giữ mẫu dựa trên Lô hàng, do đó mục "Has Batch No" (Có số lô) cần phải được kích hoạt trước. Hãy tích chọn "Retain Sample" (Lưu giữ mẫu) và thiết lập "Maximum allowed samples" (Số lượng mẫu tối đa cho phép) cho một lô hàng.

<img class="screenshot" alt="Retain Sample" src="{{docs_base_url}}/v13/assets/img/stock/retain-sample.png">

### 1.3 Tạo Phiếu kho

* Bất cứ khi nào một [Phiếu kho](/docs/v13/user/manual/en/stock/stock-entry) được tạo với mục đích là Nhập vật tư (Material Receipt), đối với các mặt hàng đã được kích hoạt tính năng Lưu giữ mẫu, "Sample Quantity" (Số lượng mẫu) có thể được thiết lập trong Phiếu kho đó. Bạn cần chọn Số lô (Batch Number) cho (các) Mặt hàng. Số lượng mẫu không được vượt quá số lượng mẫu tối đa đã thiết lập trong danh mục Mặt hàng.

    <img class="screenshot" alt="Retain Sample" src="{{docs_base_url}}/v13/assets/img/stock/material-receipt-sample.png">

* Sau khi Xác nhận Phiếu kho này, nút 'Make Retention Stock Entry' (Tạo Phiếu kho lưu giữ) sẽ khả dụng để tạo một Phiếu kho khác nhằm chuyển các mặt hàng mẫu từ lô đã nêu sang kho lưu giữ mẫu đã thiết lập trong Cài đặt kho.

    ![Sample Retention Button](/docs/v13/assets/img/stock/sample-retention-button.png)

* Nhấp vào nút này sẽ dẫn bạn đến một Phiếu kho mới loại 'Material Transfer' (Chuyển vật tư). Phiếu này sẽ chuyển phần lưu giữ mẫu của bạn từ Kho đích (Kho vật tư) sang Kho lưu giữ mẫu. Bạn hãy kiểm tra tất cả thông tin, xác nhận và nhấn Xác nhận.

    <img class="screenshot" alt="Retain Sample" src="{{docs_base_url}}/v13/assets/img/stock/material-transfer-sample.png">

### 2. Các chủ đề liên quan
1. [Kho](/docs/v13/user/manual/en/stock/warehouse)