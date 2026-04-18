<!-- add-breadcrumbs -->
# Lưu giữ tồn kho mẫu

**Tồn kho mẫu là một phần của Mặt hàng được lưu trữ để phục vụ phân tích hoặc kiểm tra chất lượng nếu có nhu cầu phát sinh sau này.**

Mặt hàng được lưu trữ tồn kho mẫu có thể là nguyên vật liệu, vật liệu đóng gói hoặc thành phẩm. Trong phiên bản v16, việc quản lý này được tối ưu hóa thông qua hệ thống [Kiểm tra chất lượng](qi.md) và khả năng truy xuất [Lô hàng](batch.md) chính xác hơn.

## 1. Điều kiện tiên quyết
Trước khi sử dụng tính năng lưu giữ mẫu, bạn cần thiết lập các danh mục sau:

* [Mặt hàng](item.md)
* [Lô hàng](batch.md)
* [Kho](warehouse.md)

## 2. Thiết lập Lưu giữ mẫu

### 2.1 Thiết lập Kho lưu giữ mẫu
Bạn nên tạo một Kho mới riêng biệt để lưu giữ các mẫu và không sử dụng kho này cho các hoạt động sản xuất hay xuất kho thông thường.

<img class="screenshot" alt="Sample Retention Warehouse" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/sample-warehouse.png">

### 2.2 Kích hoạt Lưu giữ mẫu trong danh mục Mặt hàng
Tính năng Lưu giữ mẫu hoạt động dựa trên quản lý [Lô hàng](batch.md). Do đó, mục "Has Batch No" (Có số lô) cần phải được kích hoạt. 

Trong danh mục [Mặt hàng](item.md), hãy tích chọn "Retain Sample" (Lưu giữ mẫu) và thiết lập "Maximum allowed samples" (Số lượng mẫu tối đa cho phép) cho mỗi lô hàng.

<img class="screenshot" alt="Retain Sample" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/retain-sample.png">

## 3. Quy trình thực hiện

### 3.1 Tạo Phiếu kho nhập mẫu
* Khi một [Phiếu kho](stock-entry.md) được tạo với mục đích Nhập vật tư (Material Receipt), đối với các mặt hàng đã kích hoạt tính năng Lưu giữ mẫu, trường "Sample Quantity" (Số lượng mẫu) sẽ xuất hiện. 
* Bạn cần chọn Số lô (Batch Number) tương ứng cho Mặt hàng. Lưu ý: Số lượng mẫu không được vượt quá số lượng mẫu tối đa đã thiết lập trong danh mục [Mặt hàng](item.md).

    <img class="screenshot" alt="Retain Sample" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/material-receipt-sample.png">

* Sau khi **Xác nhận** Phiếu kho này, nút 'Make Retention Stock Entry' (Tạo Phiếu kho lưu giữ) sẽ hiển thị. Nút này giúp tạo một Phiếu kho mới để chuyển số lượng mẫu từ kho chính sang kho lưu giữ mẫu đã thiết lập.

    ![Sample Retention Button](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/sample-retention-button.png)

* Khi nhấp vào nút này, hệ thống sẽ tạo một Phiếu kho mới loại 'Material Transfer' (Chuyển vật tư). Phiếu này sẽ chuyển phần hàng mẫu từ Kho nguồn (Kho vật tư) sang Kho đích (Kho lưu giữ mẫu). Hãy kiểm tra kỹ thông tin, nhấn **Lưu** và sau đó nhấn **Xác nhận**.

    <img class="screenshot" alt="Retain Sample" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/material-transfer-sample.png">

### 3.2 Theo dõi và Kiểm soát (Tính năng v16)
Với các cập nhật mới trong v16, việc quản lý mẫu được hỗ trợ chặt chẽ hơn:
* **Truy xuất nguồn gốc:** Sử dụng [Báo cáo truy xuất Số sê-ri/Lô hàng](serial-batch-traceability-report.md) để theo dõi chính xác vị trí và lịch sử của các mẫu trong kho.
* **Kế toán tồn kho:** Tính năng [Kế toán tồn kho theo Mặt hàng](item-level-stock-accounting.md) giúp tách biệt giá trị của hàng lưu kho và hàng kinh doanh, đảm bảo tính chính xác cho [Bút toán](je.md).

## 4. Các chủ đề liên quan
* [Kho](warehouse.md)
* [Lô hàng](batch.md)
* [Kiểm tra chất lượng](qi.md)
* [Phiếu kho](stock-entry.md)