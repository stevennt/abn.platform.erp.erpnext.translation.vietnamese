<!-- add-breadcrumbs -->
# Đối chiếu thanh toán

**Đối chiếu thanh toán được sử dụng để liên kết các khoản thanh toán với hóa đơn.**

Trong các kịch bản phức tạp, đặc biệt là trong ngành hàng hóa vốn, đôi khi không có liên kết trực tiếp giữa các khoản thanh toán và hóa đơn. Bạn gửi hóa đơn cho Khách hàng và Khách hàng gửi cho bạn các khoản thanh toán gộp hoặc các khoản thanh toán dựa trên một lịch trình nào đó không liên kết với các hóa đơn của bạn.

Trong những trường hợp như vậy, bạn có thể khớp các khoản Thanh toán với Hóa đơn bằng cách sử dụng Đối chiếu thanh toán.

Để truy cập Đối chiếu thanh toán, hãy đi đến:
> Home > Kế toán > Ngân hàng và Thanh toán > Đối chiếu thanh toán với Hóa đơn

## 1. Cách khớp Thanh toán với Hóa đơn
1. Đi đến Đối chiếu thanh toán.
1. Chọn một Công ty.
1. Chọn Loại đối tác (Party Type) và chọn Đối tác (Party). Tài khoản Phải thu/Phải trả sẽ được chọn tự động.
1. Chọn tài khoản Ngân hàng/Tiền mặt mà các khoản thanh toán cần được đối chiếu.
1. Nếu bạn muốn lọc các bản ghi, hãy chọn một khoảng ngày cho các hóa đơn.
1. Nhấp vào nút **Lấy các mục chưa đối chiếu (Get Unreconciled Entries)**.
1. Thao tác này sẽ lấy tất cả các Bút toán thanh toán và Hóa đơn bán hàng chưa được liên kết từ Khách hàng đó vào một bảng.
1. Xóa bất kỳ mục nào không mong muốn.
1. Chọn Số hóa đơn.
1. **Số tiền (Amount)** là số tiền mà đối tác đã thanh toán, **Số tiền phân bổ (Allocated Amount)** là số tiền bạn muốn phân bổ để đối chiếu.
1. Nhấp vào **Đối chiếu (Reconcile)**. Bạn sẽ thấy một thông báo ghi là 'Successfully Reconciled'.

Bạn sẽ nhận được một thông báo ghi là 'Amount allocated successfully'

![Payment Reconciliation Tool](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-reconciliation-tool.png)

## 2. Các tính năng mới trong v16 (Lưu ý)
Trong phiên bản v16, quy trình đối chiếu được tối ưu hóa để hỗ trợ các báo cáo tài chính nâng cao:
* **Xem trước Bút toán (Ledger Preview):** Trước khi thực hiện **Xác nhận (Submit)** đối chiếu, bạn có thể xem trước các tác động của bút toán để đảm bảo tính chính xác.
* **Hỗ trợ Báo cáo Tài chính:** Việc đối chiếu chính xác giúp đảm bảo dữ liệu cho các mẫu Báo cáo tài chính (Financial Report Templates) và Bảng cân đối số phát sinh hợp nhất (Consolidated Trial Balance) được cập nhật tức thời.

### 3. Các chủ đề liên quan
1. [Yêu cầu thanh toán (Payment Request)](payment-request.md)
1. [Hóa đơn bán hàng (Sales Invoice)](sales-invoice.md)
1. [Hóa đơn mua hàng (Purchase Invoice)](purchase-invoice.md)

{next}