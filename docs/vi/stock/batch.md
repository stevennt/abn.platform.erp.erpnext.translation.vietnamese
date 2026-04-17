<!-- add-breadcrumbs -->
# Lô hàng

**Tính năng Lô hàng trong ERPNext cho phép bạn nhóm nhiều đơn vị của một Mặt hàng và gán cho chúng một giá trị/số/thẻ duy nhất gọi là Số lô.**

Việc này được thực hiện dựa trên Mặt hàng. Nếu Mặt hàng được quản lý theo lô, thì Số lô phải được ghi nhận trong mọi giao dịch kho. Số lô có thể được duy trì thủ công hoặc tự động. Tính năng này hữu ích để thiết lập ngày hết hạn cho nhiều Mặt hàng hoặc chuyển chúng cùng nhau đến các Kho khác nhau.

Để truy cập danh sách Số lô, hãy đi đến:
> Trang chủ > Kho > Số serial và Lô hàng > Lô hàng


## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Lô hàng, bạn nên tạo các mục sau trước:

* [Mặt hàng](item.md)
* Bật 'Has Batch No' trong danh mục Mặt hàng
    ![Batch No Enabled](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/batch-no-enabled.png)


## 2. Cách tạo Lô hàng mới

Để thiết lập mặt hàng là mặt hàng theo lô, trường "Has Batch No" phải được tích chọn trong danh mục Mặt hàng. Nếu bạn không chọn "Automatically Create New Batch" khi tạo Mặt hàng, bạn sẽ phải tạo các Lô hàng một cách thủ công trong quá trình thực hiện.

Để tạo danh mục Số lô mới cho một mặt hàng, hãy đi đến:

1. Đi đến danh sách Lô hàng, nhấn vào Mới.
1. Thiết lập Batch ID.
1. Chọn Mặt hàng.
1. Nếu có bất kỳ giao dịch nào đã được thực hiện với mặt hàng đó, số lô không thể được thiết lập hoặc hủy thiết lập.
1. Lưu.

Khi tính năng Lô hàng được bật cho một Mặt hàng, tùy chọn [giữ lại hàng mẫu (retain sample stock)](retain-sample-stock.md) cũng sẽ khả dụng.

### 2.1 Tự động tạo Lô hàng
Nếu bạn muốn tự động tạo lô hàng tại thời điểm làm Phiếu nhập hàng, bạn phải tích vào 'Automatically Create New Batch' trong danh mục Mặt hàng:

<img class="screenshot" alt="Item Setup for Batches" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/item_setup_for_batch.png">

## 3. Các tính năng
### 3.1 Chia tách và Di chuyển Lô hàng

Khi bạn mở một lô hàng, bạn sẽ thấy tất cả số lượng thuộc về lô đó trên trang.

<img class="screenshot" alt="Batch View" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/batch_view.png">

* Để di chuyển lô hàng từ Kho này sang Kho khác, bạn có thể nhấn vào nút **Move**.

* Bạn cũng có thể chia nhỏ lô hàng bằng cách nhấn vào nút **Split**. Việc này sẽ tạo ra một Lô hàng mới dựa trên Lô hàng này và số lượng sẽ được chia giữa các lô.

    ![Split Batch](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/batch_split.png)

* Nếu bạn thiết lập ngày hết hạn, Lô hàng sẽ hiển thị 'Not Expired' (Chưa hết hạn) cho đến ngày hết hạn, sau đó nó sẽ hiển thị 'Expired' (Đã hết hạn). Nếu không thiết lập ngày, Lô hàng sẽ hiển thị 'Not Set' (Chưa thiết lập).

### 3.2 Giao dịch Mặt hàng với Lô hàng

Danh mục Lô hàng nên được tạo trước khi tạo Phiếu nhập hàng.
Do đó, mỗi khi một Phiếu nhập hàng hoặc Lệnh sản xuất được tạo cho một mặt hàng theo lô,
bạn sẽ tạo Số lô của nó trước, sau đó mới chọn nó trong Đơn mua hàng hoặc Phiếu kho.

Trong mọi giao dịch kho (Phiếu nhập hàng, Phiếu giao hàng, Hóa đơn) với mặt hàng theo lô,
bạn nên cung cấp Số lô của Mặt hàng đó.

> Lưu ý: Trong các giao dịch kho, Batch ID sẽ được lọc dựa trên Mã mặt hàng, Kho,
Ngày hết hạn của Lô (so sánh với ngày hạch toán của giao dịch) và Số lượng thực tế trong Kho.
Khi tìm kiếm Batch ID mà không nhập giá trị trong trường Kho, bộ lọc Số lượng thực tế sẽ không được áp dụng.

### 4. Các chủ đề liên quan
1. [Số serial](serial-no.md)
1. [Nhập số dư tồn kho đầu kỳ cho Mặt hàng theo Số serial và Lô hàng](articles/opening-stock-balance-entry-for-serialized-and-batch-item.md)
1. [Quản lý tồn kho theo Lô hàng](articles/managing-batch-wise-inventory.md)