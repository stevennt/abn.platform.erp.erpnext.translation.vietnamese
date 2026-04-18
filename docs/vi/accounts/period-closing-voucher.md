<!-- add-breadcrumbs -->
# Bút toán khóa sổ kỳ

**Bút toán khóa sổ kỳ cho biết rằng lãi/lỗ của một kỳ kế toán đã được cân đối và sổ sách có thể bắt đầu một chu kỳ mới.**

Vào cuối mỗi năm hoặc (hàng quý hoặc thậm chí hàng tháng), sau khi hoàn tất kiểm toán, bạn có thể khóa sổ kế toán của mình. Điều này có nghĩa là bạn thực hiện tất cả các bút toán đặc biệt như:

  * Khấu hao
  * Thay đổi giá trị Tài sản
  * Thuế và nợ phải trả hoãn lại
  * Cập nhật nợ xấu

Sau đó ghi nhận Lãi hoặc Lỗ.

Bằng cách này, số dư trong các Tài khoản Thu nhập và Chi phí của bạn sẽ trở về bằng không. Bạn bắt đầu một Năm tài chính (hoặc kỳ) mới với Bảng cân đối kế toán đã được cân đối và tài khoản Lãi và Lỗ mới. Trong ERPNext, sau khi thực hiện tất cả các bút toán đặc biệt thông qua Bút toán cho năm tài chính hiện tại, bạn nên đưa tất cả các tài khoản Thu nhập và Chi phí về bằng không thông qua Bút toán khóa sổ kỳ.

Để truy cập danh sách Bút toán khóa sổ kỳ, hãy đi đến:
> Home > Accounting > Opening and Closing > Period Closing Voucher

## 1. Cách tạo Bút toán khóa sổ kỳ

1. Đi đến danh sách Bút toán khóa sổ kỳ và nhấn vào New.
1. Thiết lập ngày hạch toán (posting date).
1. Chọn tài khoản, thông thường đây là tài khoản 'Reserves and Surplus'.
1. Nhập ghi chú nếu có.
1. Lưu và Xác nhận.
  ![Period Closing Voucher](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/period-closing-voucher.png)

### 1.2 Giải thích các trường

* **Transaction Date** sẽ là ngày tạo Bút toán khóa sổ kỳ.
* **Posting Date** sẽ là ngày mà bút toán này được thực hiện. Nếu Năm tài chính của bạn kết thúc vào ngày 31 tháng 12, thì ngày đó nên được chọn làm Posting Date trong Bút toán khóa sổ kỳ.
* **Closing Fiscal Year** sẽ là năm mà bạn đang thực hiện khóa báo cáo tài chính.

### 1.3 Điều gì xảy ra khi Xác nhận?
Bút toán khóa sổ kỳ sẽ tạo các bút toán kế toán (GL Entry). Điều này sẽ đưa tất cả các Tài khoản Thu nhập và Chi phí của bạn về bằng không và chuyển số dư Lãi/Lỗ vào Tài khoản kết chuyển.

Bạn nên chọn một tài khoản nợ phải trả như Reserves and Surplus, hoặc bất kỳ tài khoản Dự trữ doanh thu nào hoặc vào tài khoản Vốn chủ sở hữu làm Tài khoản kết chuyển.

![Period Closing Voucher ledger](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/period-closing-voucher-ledger.png)

> **Lưu ý:** Nếu các bút toán kế toán được thực hiện trong một Năm tài chính đang khóa, ngay cả sau khi Bút toán khóa sổ kỳ đã được tạo cho Năm tài chính đó, bạn vẫn nên tạo một Bút toán khóa sổ kỳ khác. Bút toán sau này sẽ chỉ chuyển số dư P&L còn tồn đọng vào Tài khoản kết chuyển.

### 2. Các chủ đề liên quan
1. [Fiscal Year](fiscal-year.md)
1. [Tax Withholding Category](tax-withholding-category.md)
1. [Accounting Period](accounting-period.md)

{next}