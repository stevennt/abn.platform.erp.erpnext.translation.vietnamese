<!-- add-breadcrumbs -->
# Chiết khấu hóa đơn

**Chiết khấu hóa đơn là hình thức sử dụng các hóa đơn bán hàng chưa thanh toán của công ty để làm tài sản thế chấp cho một khoản vay ngắn hạn, được cấp bởi ngân hàng hoặc công ty tài chính.**

Để truy cập danh sách Chiết khấu hóa đơn, hãy đi đến:
> Home > Accounting > Banking and Payments > Invoice Discounting

## 1. Điều kiện tiên quyết

Bạn cần tạo các tài khoản sổ cái sau để hạch toán các giao dịch chiết khấu hóa đơn.

* **Short Term Loan (Khoản vay ngắn hạn):** Một tài khoản thuộc nhóm 'Current Liabilities' > 'Loans (Liabilities)' để quản lý khoản vay.
* **Bank Account Charges (Phí tài khoản ngân hàng):** Một tài khoản chi phí cho các khoản phí do ngân hàng thu.
* **Accounts Receivable Credit Account (Tài khoản phải thu khách hàng tín dụng):** Một tài khoản kiểm soát loại phải thu.
* **Accounts Receivable Discounted Account (Tài khoản phải thu đã chiết khấu):** Một tài khoản phải thu cho các hóa đơn đã được chiết khấu.
* **Accounts Receivable Unpaid Account (Tài khoản phải thu chưa thanh toán):** Một tài khoản phải thu cho các hóa đơn đã được chiết khấu nhưng vẫn chưa được thanh toán ngay cả khi thời hạn vay đã kết thúc.

## 2. Cách hạch toán giao dịch Chiết khấu hóa đơn

1. Đi đến danh sách Invoice Discounting, nhấn vào New.
1. Nhập Posting Date (Ngày hạch toán) và Loan Start Date (Ngày bắt đầu khoản vay). Nhập Loan Period (Thời hạn vay) theo số ngày.
1. Chọn các hóa đơn bằng cách chọn thủ công trong bảng hoặc bằng cách nhấn vào nút 'Get Invoices' ở góc trên bên phải.
1. Chọn Short Term Loan Account (Tài khoản khoản vay ngắn hạn), Bank Account (Tài khoản ngân hàng), và Bank Charges Account (Tài khoản phí ngân hàng).
1. Chọn Accounts Receivable Credit Account (Tài khoản phải thu khách hàng tín dụng), Accounts Receivable Discounted Account (Tài khoản phải thu đã chiết khấu) và Accounts Receivable Unpaid Account (Tài khoản phải thu chưa thanh toán).
1. Nhấn Lưu (Save) sau đó Xác nhận (Submit).
1. Sau khi Xác nhận (Submit) biểu mẫu Chiết khấu hóa đơn, nhấn vào **Disburse Loan** (Giải ngân khoản vay).

 ![Disburse Loan in Invoice Discounting](https://docs.erpnext.com/docs/v13/assets/img/accounts/invoice-discounting.png)

1. Bạn sẽ được đưa đến màn hình [Journal Entry](journal-entry.md) (Bút toán). Lưu (Save) và Xác nhận (Submit) Bút toán này.

  ![Journal Entry](https://docs.erpnext.com/docs/v13/assets/img/accounts/invoice-discounting-journal-entry.png)

## 2. Các tính năng

### 2.1 Nhập hóa đơn
Nhấn vào nút 'Get Invoices' để nhập các hóa đơn. Bạn có thể nhập hóa đơn bằng cách lọc theo các tiêu chí nhất định.

* Hóa đơn được tạo cho một Khách hàng (Customer) cụ thể.
* Khoảng ngày mà các hóa đơn được lập.
* Số tiền tối thiểu và tối đa.

Bạn cũng có thể chỉ định kết hợp nhiều bộ lọc trên.

### 2.2 Tất toán khoản vay
Khi bạn hoàn trả khoản vay vào cuối thời hạn vay hoặc trước đó, bạn có thể cập nhật bằng cách nhấn vào nút 'Close Loan' (Tất toán khoản vay).
  ![Journal Entry](https://docs.erpnext.com/docs/v13/assets/img/accounts/invoice-discounting-close-loan.png)
Hệ thống sẽ lập Bút toán. Hãy kiểm tra và Xác nhận (Submit) nó.

### 2.3 Tự động cập nhật sổ cái khi kết thúc thời hạn vay
Nếu khoản vay không được hoàn trả vào cuối thời hạn vay, hệ thống sẽ tạo một Bút toán thông qua một công việc lập lịch (scheduled job) để chuyển giá trị từ 'Accounts Receivable Discounted Account' (Tài khoản phải thu đã chiết khấu) sang 'Accounts Receivable Unpaid Account' (Tài khoản phải thu chưa thanh toán). Điều này sẽ giúp dễ dàng theo dõi các hóa đơn đã được chiết khấu nhưng vẫn chưa được thanh toán khi kết thúc thời hạn vay.

{next}