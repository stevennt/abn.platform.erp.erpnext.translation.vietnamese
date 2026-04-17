<!-- add-breadcrumbs -->
# Kế toán đa tiền tệ

**Việc thực hiện giao dịch bằng hai loại tiền tệ khác nhau được gọi là Kế toán đa tiền tệ.**

Trong ERPNext v16, bạn có thể thực hiện các bút toán kế toán bằng nhiều loại tiền tệ khác nhau. Ví dụ, nếu bạn có một tài khoản ngân hàng bằng ngoại tệ, bạn có thể thực hiện các giao dịch bằng loại tiền tệ đó và hệ thống sẽ chỉ hiển thị số dư ngân hàng bằng loại tiền tệ cụ thể đó.

Các tài khoản ngân hàng bằng ngoại tệ có thể dành cho các chi nhánh khác của công ty bạn hoặc tài khoản Phải thu/Phải trả cho Khách hàng/Nhà cung cấp nước ngoài.

## 1. Thiết lập
### 1.1 Thiết lập tiền tệ trong Hệ thống tài khoản
Để bắt đầu với kế toán đa tiền tệ, bạn cần chỉ định tiền tệ kế toán trong bản ghi Tài khoản. Bạn có thể xác định Tiền tệ từ [Hệ thống tài khoản](chart-of-accounts.md) khi tạo một Tài khoản.

![Set Currency in Account](https://docs.erpnext.com/docs/v16/assets/img/accounts/set-default-currency-in-ledger.png)

### 1.2 Tài khoản mới với tiền tệ khác
Bạn cũng có thể chỉ định/sửa đổi tiền tệ bằng cách mở các bản ghi Tài khoản cụ thể cho các Tài khoản hiện có.

![Update Currency in Ledger](https://docs.erpnext.com/docs/v16/assets/img/accounts/update-currency-in-ledger.png)

### 1.3 Tiền tệ cho Khách hàng/Nhà cung cấp
Đối với Khách hàng/Nhà cung cấp (Đối tác), bạn cũng có thể xác định tiền tệ thanh toán của họ trong bản ghi đối tác. Nếu tiền tệ kế toán của đối tác khác với Tiền tệ của Công ty, bạn nên chỉ định Tài khoản Phải thu/Phải trả mặc định bằng loại tiền tệ đó.

![Billing Currency in Customer](https://docs.erpnext.com/docs/v16/assets/img/accounts/customer-billing-currency.png)

### 1.4 Sau khi thiết lập
Sau khi bạn xác định Tiền tệ trong (các) tài khoản bắt buộc và chọn các tài khoản liên quan trong bản ghi Đối tác, bạn đã sẵn sàng để thực hiện các giao dịch đối với chúng. Nếu tiền tệ tài khoản của đối tác khác với tiền tệ của Công ty, hệ thống sẽ hạn chế việc thực hiện giao dịch với đối tác đó.

Bạn cần thay đổi tiền tệ sang tiền tệ của đối tác trong giao dịch (Đơn bán hàng hoặc Đơn mua hàng/Hóa đơn). Nếu tiền tệ tài khoản của đối tác giống với tiền tệ của công ty, bạn có thể thực hiện giao dịch cho Đối tác đó bằng bất kỳ loại tiền tệ nào. Nhưng các bút toán kế toán (Bút toán sổ cái) sẽ luôn được thực hiện bằng Tiền tệ tài khoản của Đối tác.

> **Lưu ý**: Đảm bảo rằng tài khoản chính xác với tiền tệ đã được thiết lập trong trường 'Debit To' khi lập hóa đơn/thanh toán.

Bạn có thể thay đổi tiền tệ kế toán trong bản ghi Đối tác/Tài khoản trước khi thực hiện bất kỳ giao dịch nào đối với chúng. Sau khi đã thực hiện các bút toán kế toán, hệ thống sẽ không cho phép bạn thay đổi tiền tệ cho cả bản ghi Đối tác/Tài khoản. Trong trường hợp thiết lập đa công ty, tiền tệ kế toán của đối tác phải giống nhau cho tất cả các công ty.

## 2. Tỷ giá hối đoái
Khi làm việc với nhiều loại tiền tệ, ERPNext có trang Trao đổi tiền tệ để quản lý tỷ giá hối đoái. Nó cho phép bạn lưu các báo giá tỷ giá hối đoái mà bạn yêu cầu. Để biết thêm, hãy truy cập trang [Trao đổi tiền tệ](currency-exchange.md).

Đối với các giao dịch ngoại tệ, ERPNext kiểm tra tỷ giá hối đoái từ:

1. Từ Trao đổi tiền tệ cho bất kỳ bản ghi khớp nào (nếu được tạo bởi Người dùng).
2. Nếu bước này thất bại, ERPNext sẽ cố gắng lấy tỷ giá hối đoái thị trường hiện tại từ [Frankfurter](https://www.frankfurter.app).
3. Nếu bước này vẫn thất bại, thì tỷ giá hối đoái sẽ phải được nhập thủ công.

Các tỷ giá trong danh mục Trao đổi tiền tệ được lấy dựa trên việc 'Cho phép tỷ giá hối đoái cũ' có được bật trong Cài đặt kế toán hay không. Để biết thêm, hãy truy cập trang [Cài đặt kế toán](accounts-settings.md).

## 3. Giao dịch

### 3.1 Hóa đơn bán hàng

Trong Hóa đơn bán hàng, tiền tệ giao dịch phải giống với tiền tệ kế toán của Khách hàng nếu tiền tệ kế toán của Khách hàng khác với tiền tệ của Công ty. Nếu không, bạn có thể chọn bất kỳ loại tiền tệ nào trong Hóa đơn bán hàng. Khi chọn Khách hàng, hệ thống sẽ lấy Tài khoản Phải thu từ Khách hàng/Công ty. Tiền tệ của tài khoản phải thu phải giống với tiền tệ kế toán của Khách hàng.

Giờ đây, trong Hóa đơn, Số tiền đã thanh toán sẽ được nhập bằng tiền tệ giao dịch, thay vì Tiền tệ của Công ty như trước đây. Số tiền xóa nợ cũng sẽ được nhập bằng tiền tệ giao dịch.

Số tiền còn lại và Số tiền tạm ứng sẽ luôn được tính toán và hiển thị bằng Tiền tệ tài khoản của Khách hàng. Các số tiền đã thanh toán sẽ được phản ánh trong [Bút toán thanh toán](payment-entry.md):

![Multi-currency in Payment Entry](https://docs.erpnext.com/docs/v16/assets/img/accounts/multi-currency-in-payment-entry.png)

### 3.2 Hóa đơn mua hàng

Tương tự, trong Hóa đơn mua hàng, các bút toán kế toán sẽ được thực hiện dựa trên tiền tệ kế toán của Nhà cung cấp. Số tiền còn lại và Số tiền tạm ứng cũng sẽ được hiển thị bằng tiền tệ kế toán của nhà cung cấp. Số tiền xóa nợ giờ đây sẽ được nhập bằng tiền tệ giao dịch.

### 3.3 Bút toán

Trong Bút toán, bạn có thể thực hiện các giao dịch bằng các loại tiền tệ khác nhau. Có một ô đánh dấu 'Đa tiền tệ' để cho phép các bút toán đa tiền tệ. Chỉ khi tùy chọn 'Đa tiền tệ' được chọn, bạn mới có thể chọn các tài khoản có các loại tiền tệ khác nhau.

![Multi-currency in Journal Entry](https://docs.erpnext.com/docs/v16/assets/img/accounts/multi-currency-journal-entry.png)

Trong bảng Tài khoản, khi chọn một tài khoản ngoại tệ, hệ thống sẽ hiển thị phần Tiền tệ và tự động lấy Tiền tệ tài khoản và Tỷ giá hối đoái. Bạn có thể thay đổi/sửa đổi Tỷ giá hối đoái sau đó một cách thủ công. Số tiền Nợ/Có nên được nhập bằng Tiền tệ tài khoản, hệ thống sẽ tự động tính toán và hiển thị số tiền Nợ/Có bằng Tiền tệ của Công ty.

![Company and Transaction Currency in Journal Entry](https://docs.erpnext.com/docs/v16/assets/img/accounts/company-and-transaction-currency-in-journal-entry.png)

*Lưu ý: Trong phiên bản v16, bạn có thể sử dụng tính năng **Ledger Preview** để xem trước các bút toán trước khi thực hiện **Xác nhận (Submit)** để đảm bảo tính chính xác của tỷ giá và số tiền quy đổi.*