<!-- add-breadcrumbs -->
# Bút toán

**Bút toán là một bút toán được thực hiện trong sổ cái và nó cho biết các tài khoản bị ảnh hưởng.**

Bút toán là một giao dịch đa mục đích, nơi có thể lựa chọn các tài khoản nợ và tài khoản có.

Tất cả các loại bút toán kế toán khác ngoài các giao dịch Bán hàng và Mua hàng đều được thực hiện bằng cách sử dụng **Bút toán**. Một **Bút toán** là một giao dịch kế toán tiêu chuẩn ảnh hưởng đến nhiều Tài khoản và tổng số tiền nợ phải bằng tổng số tiền có. Bút toán tác động đến sổ cái chính.

Bút toán có thể được sử dụng để nhập các chi phí, bút toán kết chuyển đầu kỳ, bút toán đối ứng, thanh toán ngân hàng, bút toán thuế tiêu thụ, v.v. Ví dụ: hạch toán chi phí vận hành, chi phí trực tiếp như xăng dầu/vận chuyển, chi phí tạp phí, bút toán điều chỉnh và điều chỉnh số tiền hóa đơn.

> Lưu ý: Từ phiên bản 13 trở đi, chúng tôi đã giới thiệu sổ cái bất biến (immutable ledger), điều này thay đổi cách thức hủy các bút toán kế toán trong ERPNext. [Tìm hiểu thêm tại đây](articles/immutable-ledger-in-erpnext.md).

Để truy cập danh sách Bút toán, hãy đi đến:
> Home > Accounting > General Ledger > Journal Entry

## 1. Cách tạo một Bút toán
1. Đi đến danh sách Bút toán, nhấn vào New.
1. Loại bút toán (Entry Type) mặc định sẽ là 'Journal Entry'. Đây là loại bút toán đa mục đích. Truy cập [mục 3](journal-entry.md#3-journal-entry-types) để biết thêm về các loại bút toán.
1. Bạn có thể thay đổi Ngày hạch toán (Posting Date).
1. Mở rộng bảng, chọn một Tài khoản mà số tiền sẽ được ghi nợ.
1. Các chi tiết trên cũng có thể được thêm từ [Mẫu Bút toán](journal-entry-template.md) với trường 'From Template'.
1. Chọn Loại đối tượng (Party Type) và Đối tượng (Party) nếu đây là bút toán ghi nợ cho khách nợ.
1. Thêm một dòng nơi số tiền sẽ được ghi có.
1. Lưu ý rằng, cuối cùng, tổng số tiền nợ và số tiền có phải bằng nhau.
1. Lưu và Xác nhận.

![Journal Entry](https://docs.erpnext.com/docs/v13/assets/img/accounts/journal-entry.png)


**Sổ tài chính (Finance Book)**: Bạn có thể hạch toán bút toán này vào một [Sổ tài chính](finance-book.md) cụ thể. Nếu để trống trường này, Bút toán này sẽ hiển thị trong tất cả các Sổ tài chính.

### 1.1 Nhập nhanh (Quick Entry)
Khi tạo Bút toán, nút **Nhập nhanh (Quick Entry)** có thể được nhìn thấy ở góc trên bên phải. Điều này giúp việc tạo Bút toán trở nên dễ dàng hơn một chút. Nhập số tiền, chọn các tài khoản, thêm ghi chú. Điều này sẽ tự động điền bảng 'Accounting Entries' với các chi tiết đã chọn.

![Quick Entry](https://docs.erpnext.com/docs/v13/assets/img/accounts/quick-journal-entry.png)

## 2. Các tính năng
### 2.1 Bút toán kế toán

* **Chiều kích kế toán (Accounting Dimensions)**: Một Dự án hoặc Trung tâm chi phí có thể được liên kết tại đây để theo dõi chi phí riêng biệt. Để biết thêm, [truy cập trang này](accounting-dimensions.md).
  ![Accounting Dimension](https://docs.erpnext.com/docs/v13/assets/img/accounts/journal-entry-accounting-dimension.png)

* **Số tài khoản ngân hàng (Bank Account No)**: Nếu bạn đã thêm một [Tài khoản ngân hàng](bank-account.md), số liên kết với tài khoản ngân hàng đó sẽ được lấy ra.
* **Loại tham chiếu (Reference Type)**: Nếu Bút toán kế toán này liên quan đến một giao dịch khác, nó có thể được tham chiếu tại đây. Chọn Loại tham chiếu và chọn chứng từ cụ thể. Ví dụ: nếu bạn đang tạo một Bút toán đối ứng với một Hóa đơn bán hàng cụ thể. Liên kết Bút toán này với hóa đơn đó. Số tiền "còn nợ" của hóa đơn đó sẽ bị ảnh hưởng.

  ![Reference](https://docs.erpnext.com/docs/v13/assets/img/accounts/journal-entry-reference.png)

Dưới đây là các chứng từ có thể được chọn trong Bút toán dưới phần Loại tham chiếu:

  * [Hóa đơn bán hàng](sales-invoice.md)
  * [Hóa đơn mua hàng](purchase-invoice.md)
  * Bút toán (Journal Entry)
  * [Đơn bán hàng](../selling/sales-order.md)
  * [Đơn mua hàng](../buying/purchase-order.md)
  * [Yêu cầu thanh toán chi phí](https://docs.erpnext.com/docs/v13/user/manual/en/human-resources/expense-claim)
  * [Tài sản](https://docs.erpnext.com/docs/v13/user/manual/en/asset/asset)
  * [Khoản vay](https://docs.erpnext.com/docs/v13/user/manual/en/loan-management/loan)
  * [Bút toán lương](https://docs.erpnext.com/docs/v13/user/manual/en/human-resources/payroll-entry)
  * [Tạm ứng nhân viên](https://docs.erpnext.com/docs/v13/user/manual/en/human-resources/employee-advance)
  * [Đánh giá lại tỷ giá hối đoái](exchange-rate-revaluation.md)
  * [Chiết khấu hóa đơn](invoice_discounting.md)

* **Là tạm ứng (Is Advance)**: Nếu đây là một khoản thanh toán tạm ứng bởi Khách hàng, hãy đặt tùy chọn này thành 'Yes'. Điều này hữu ích khi bạn đã liên kết một biểu mẫu 'Loại tham chiếu' với Bút toán này. Việc chọn “Yes” sẽ liên kết Bút toán này với giao dịch được chọn trong trường 'Reference Name'. Để biết thêm, hãy truy cập trang [Bút toán thanh toán tạm ứng](advance-payment-entry.md).

* **Ghi chú người dùng (User Remark)**: Bất kỳ ghi chú bổ sung nào về bút toán đều có thể được thêm vào trường này.

### 2.2 Đảo ngược Bút toán (Reverse Journal Entry)
Trong bất kỳ Bút toán nào đã được Xác nhận, có một nút chuyên dụng để đảo ngược Bút toán. Khi nhấp vào nút 'Reverse Journal Entry', hệ thống sẽ tạo một Bút toán mới bằng cách đảo ngược số tiền nợ và có đối với các tài khoản tương ứng.

![Reverse Journal Entry](https://docs.erpnext.com/docs/v13/assets/img/accounts/reverse-journal-entry.png)

### 2.3 Bút toán chênh lệch (Difference Entry)
“Chênh lệch” là phần chênh lệch còn lại sau khi cộng tất cả số tiền nợ và có.

Theo hệ thống kế toán bút toán kép, tổng số tiền nợ phải bằng tổng số tiền có.

Số này phải bằng không nếu Bút toán muốn được “Xác nhận”. Nếu số này khác không, bạn có thể nhấp vào “Make Difference Entry” và hệ thống sẽ tự động thêm một dòng mới với số tiền cần thiết để làm cho tổng bằng không. Chọn tài khoản để ghi nợ/có và tiếp tục.

  ![Make Difference](https://docs.erpnext.com/docs/v13/assets/img/accounts/journal-entry-make-difference-entry.png)

### 2.4 Tham chiếu (Referencing)

Một Số tham chiếu có thể được nhập thủ công và một Ngày tham chiếu có thể được thiết lập. Khi nhập một Số tham chiếu tại đây, một 'Ghi chú' sẽ được hiển thị, ví dụ:

> Lưu ý: nhà cung cấp

> Tham chiếu