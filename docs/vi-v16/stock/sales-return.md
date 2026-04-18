<!-- add-breadcrumbs -->
# Trả hàng bán

**Một Mặt hàng đã bán được trả lại được gọi là Trả hàng bán.**

Các doanh nghiệp thường xuyên phải xử lý việc trả lại hàng hóa đã bán. Hàng có thể được Khách hàng trả lại do các vấn đề về chất lượng, không giao hàng đúng ngày đã thỏa thuận, hoặc bất kỳ lý do nào khác.

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Trả hàng bán, bạn nên tạo các mục sau trước:

* [Mặt hàng](item.md)
* [Hóa đơn bán hàng](../accounts/sales-invoice.md) hoặc [Phiếu giao hàng](delivery-note.md)

## 2. Cách tạo Trả hàng bán

1. Đầu tiên, hãy mở Phiếu giao hàng / Hóa đơn bán hàng gốc mà Khách hàng đã trả lại Mặt hàng.

    <img class="screenshot" alt="Original Delivery Note" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/sales-return-original-delivery-note.png">

1. Sau đó, nhấp vào 'Create > Sales Return', hệ thống sẽ mở một Phiếu giao hàng mới với tùy chọn 'Is Return' được chọn, các Mặt hàng, Đơn giá và Thuế sẽ hiển thị là số âm.

    <img class="screenshot" alt="Return Against Delivery Note" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/sales-return-against-delivery-note.png">

1. Bạn cũng có thể tạo bút toán trả hàng dựa trên Hóa đơn bán hàng gốc để trả lại kho cùng với chứng từ ghi có, hãy kiểm tra tùy chọn "Update Stock" trong Hóa đơn bán hàng trả lại.

    <img class="screenshot" alt="Return Against Sales Invoice" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/sales-return-against-sales-invoice.png">

1. Khi Xác nhận Phiếu giao hàng trả lại / Hóa đơn bán hàng trả lại, hệ thống sẽ tăng số dư tồn kho trong Kho đã chỉ định. Với các tính năng mới của v16, hệ thống hỗ trợ truy xuất nguồn gốc theo Lô hàng (Batch) và Số sê-ri (Serial) để đảm bảo tính chính xác của Tồn kho.

    <img class="screenshot" alt="Return Stock Ledger" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/sales-return-stock-ledger.png">

1. Trong trường hợp Hóa đơn bán hàng trả lại, tài khoản Khách hàng sẽ được ghi có và tài khoản thu nhập cũng như tài khoản thuế liên quan sẽ được ghi nợ như được hiển thị trong Sổ cái. Bạn có thể sử dụng tính năng Xem trước Sổ cái (Ledger Preview) để kiểm tra nhanh các bút toán này.

    <img class="screenshot" alt="Return Stock Ledger" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/sales-return-general-ledger.png">

Nếu tính năng Kiểm kê vĩnh viễn (Perpetual Inventory) được bật, hệ thống cũng sẽ hạch toán bút toán đối với tài khoản kho để đồng bộ số dư tài khoản kho với số dư tồn kho theo Sổ cái kho. Ngoài ra, với tính năng Kế toán tồn kho theo từng Mặt hàng (Item-Level Stock Accounting), giá trị kho sẽ được quản lý chi tiết và chính xác hơn ngay khi Xác nhận chứng từ.

## 3. Tác động đối với Trả hàng kho thông qua Phiếu giao hàng
Khi tạo Trả hàng bán dựa trên một Phiếu giao hàng:

* **Số lượng trả lại** trong Phiếu giao hàng gốc cùng với bất kỳ Đơn bán hàng nào liên kết với nó sẽ được cập nhật.
* Hệ thống sẽ tự động cập nhật lại các lệnh Giữ hàng (Stock Reservation) nếu có để đảm bảo số lượng tồn kho khả dụng được phản ánh đúng thực tế.

* Trạng thái của Phiếu giao hàng gốc sẽ được chuyển thành **Return Issued** nếu được trả lại 100%:
  ![Return Issued](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/stock/sales-return-issue.png)

## 4. Các chủ đề liên quan
1. [Trả hàng mua](purchase-return.md)
1. [Kiểm kê vĩnh viễn](perpetual-inventory.md)