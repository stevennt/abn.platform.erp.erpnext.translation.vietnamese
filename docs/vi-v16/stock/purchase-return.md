<!-- add-breadcrumbs -->
# Trả hàng mua

**Một Mặt hàng đã mua được trả lại được gọi là Trả hàng mua.**

Với tính năng Trả hàng mua, bạn có thể trả lại sản phẩm cho Nhà cung cấp. Việc này có thể vì một số lý do như hàng lỗi, chất lượng không phù hợp, người mua không còn nhu cầu về hàng tồn kho, v.v.

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Trả hàng mua, bạn nên tạo các mục sau trước:

* [Mặt hàng](item.md)
* [Hóa đơn mua hàng](../accounts/purchase-invoice.md)

    Hoặc

    [Phiếu nhập hàng](purchase-receipt.md)


## 2. Cách tạo Trả hàng mua
1. Đầu tiên, hãy mở Phiếu nhập hàng gốc mà Nhà cung cấp đã giao Mặt hàng.

    <img class="screenshot" alt="Original Purchase Receipt" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/purchase-return-original-purchase-receipt.png">

1. Nhấp vào 'Create > Return', hệ thống sẽ mở một Phiếu nhập hàng mới với ô 'Is Return' đã được chọn. Số lượng Mặt hàng, Đơn giá và Thuế sẽ là các số âm.

    <img class="screenshot" alt="Return Against Purchase Receipt" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/purchase-return-against-purchase-receipt.png">

1. Khi **Xác nhận** Trả hàng mua, hệ thống sẽ giảm số lượng mặt hàng từ **Kho** đã nêu. Với các tính năng mới trong v16, hệ thống sẽ hỗ trợ **Truy xuất nguồn gốc Lô hàng/Số sê-ri** (Serial/Batch Traceability) để đảm bảo chính xác lô hàng được trả về. Để duy trì giá trị tồn kho chính xác, số dư tồn kho cũng sẽ được cập nhật dựa trên đơn giá mua ban đầu của các mặt hàng được trả lại.

    <img class="screenshot" alt="Return Stock Ledger" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/purchase-return-stock-ledger.png">

1. Trong Sổ cái, tài khoản Hàng tồn kho sẽ được ghi có và tài khoản Hàng đã nhận nhưng chưa lập hóa đơn sẽ được ghi nợ. Nhờ tính năng **Kế toán tồn kho theo từng Mặt hàng** (Item-Level Stock Accounting), việc theo dõi giá trị tồn kho sẽ trở nên chi tiết và chính xác hơn ngay tại thời điểm thực hiện.

    <img class="screenshot" alt="Return Stock Ledger" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/purchase-return-general-ledger.png">

Nếu tính năng Kiểm kê vĩnh viễn được bật, hệ thống cũng sẽ hạch toán **Bút toán** đối với tài khoản kho để đồng bộ số dư tài khoản kho với số dư tồn kho theo Sổ cái kho. Bạn có thể sử dụng tính năng **Xem trước Sổ cái** (Ledger Preview) để kiểm tra nhanh các tác động kế toán trước khi hoàn tất.

## 3. Tác động của việc Trả hàng qua Phiếu nhập hàng đối với Tồn kho
Khi tạo Trả hàng mua đối với một Phiếu nhập hàng:

* **Số lượng trả lại** trong Phiếu nhập hàng gốc cùng với bất kỳ Đơn mua hàng nào liên kết với nó sẽ được cập nhật.
* Hệ thống **Giữ chỗ tồn kho** (Stock Reservation) sẽ được điều chỉnh tương ứng để phản ánh chính xác lượng hàng thực tế có sẵn.
* Trạng thái của Phiếu nhập hàng gốc sẽ được đổi thành **Đã xuất trả** nếu được trả lại 100%:
  ![Return Issued](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/purchase-return-issue.png)

### 4. Các chủ đề liên quan
1. [Trả hàng bán](sales-return.md)
1. [Kiểm kê vĩnh viễn](perpetual-inventory.md)