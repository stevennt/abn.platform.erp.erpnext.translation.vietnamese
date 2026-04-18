<!-- add-breadcrumbs -->

# Chi phí trả trước

**Chi phí trả trước là một khoản chi phí đã phát sinh nhưng chưa được tiêu dùng.**

Khoản chi phí này được ghi nhận là một tài sản cho đến khi hàng hóa hoặc dịch vụ liên quan được tiêu dùng; tại thời điểm đó, chi phí sẽ được tính vào chi phí hoạt động. Một khoản Chi phí trả trước ban đầu được ghi nhận là một tài sản, để nó xuất hiện trên bảng cân đối kế toán (thường là Tài sản ngắn hạn, vì nó chưa được sử dụng ngay bây giờ và có thể sẽ được tiêu dùng trong vòng một năm).

## 1. Cấu hình Kế toán trả trước

Trước khi bạn bắt đầu sử dụng kế toán trả trước, bạn nên lưu ý các cài đặt dưới đây để giúp bạn kiểm soát tốt hơn cách quản lý kế toán trả trước của mình.

![Deferred Accounting Settings](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/deferred-accounting-settings.png)

1. **Automatically Process Deferred Accounting Entry (Tự động xử lý bút toán kế toán trả trước):** Cài đặt này được bật theo mặc định. Trong trường hợp bạn không muốn các bút toán kế toán trả trước được hạch toán tự động, bạn có thể tắt cài đặt này. Nếu cài đặt này bị tắt, kế toán trả trước sẽ phải được xử lý thủ công bằng cách sử dụng [Process Deferred Accounting](process-deferred-accounting.md)

1. **Book Deferred Entries Based On (Hạch toán bút toán trả trước dựa trên):** Số tiền chi phí trả trước có thể được hạch toán dựa trên hai tiêu chí. Tùy chọn mặc định ở đây là "Days" (Ngày). Nếu chọn "Days", số tiền chi phí trả trước sẽ được hạch toán dựa trên số ngày trong mỗi tháng và nếu chọn "Months" (Tháng) thì nó sẽ được hạch toán dựa trên số tháng. **Ví dụ:** Nếu chọn "Days" và khoản chi phí $12,000 phải được trả trước trong khoảng thời gian 12 tháng, thì $986.30 sẽ dành cho tháng có 30 ngày và $1,019.17 sẽ được hạch toán cho tháng có 31 ngày. Nếu chọn "Months", $1,000 chi phí trả trước sẽ được hạch toán mỗi tháng bất kể số ngày trong tháng.

1. **Book Deferred Entries Via Journal Entry (Hạch toán bút toán trả trước qua Bút toán):** Theo mặc định, các Bút toán Sổ cái được hạch toán trực tiếp để ghi nhận chi phí trả trước đối với một hóa đơn. Để hạch toán khoản trả trước này thông qua Bút toán, tùy chọn này có thể được bật.

1. **Submit Journal Entries (Xác nhận Bút toán):** Tùy chọn này chỉ áp dụng nếu các bút toán kế toán trả trước được hạch toán thông qua Bút toán. Theo mặc định, các Bút toán cho việc hạch toán trả trước được giữ ở trạng thái Nháp và người dùng có thể sử dụng tính năng **Ledger Preview** để kiểm tra trước khi thực hiện **Xác nhận** thủ công. Nếu tùy chọn này được bật, các Bút toán sẽ được tự động **Xác nhận** mà không cần sự can thiệp của người dùng.

## 2. Cách sử dụng Chi phí trả trước

Ví dụ về Chi phí trả trước, Unico Plastics thanh toán $10,000 vào tháng Tư cho tiền thuê nhà tháng Năm. Họ hoãn khoản chi phí này tại thời điểm thanh toán (vào tháng Tư) vào tài khoản tài sản tiền thuê trả trước. Vào tháng Năm, Unico Plastics hiện đã tiêu dùng tài sản trả trước, vì vậy họ ghi có tài khoản tài sản tiền thuê trả trước và ghi nợ tài khoản chi phí tiền thuê nhà.

Các ví dụ khác về Chi phí trả trước là:

* Chi phí lãi vay được vốn hóa như một phần của tài sản cố định mà các chi phí đó đã phát sinh
* Bảo hiểm trả trước cho các tháng bảo hiểm trong tương lai
* Giá trị của tài sản cố định được tính vào chi phí trong suốt thời gian sử dụng hữu ích dưới hình thức khấu hao
* Chi phí phát sinh để đăng ký việc phát hành một công cụ nợ
* Giá trị của tài sản vô hình được tính vào chi phí trong suốt thời gian sử dụng hữu ích dưới hình thức phân bổ
* Đối với một Gói đăng ký Internet, số tiền được thanh toán trước và dịch vụ được cung cấp hàng tháng. Vì vậy, đó là Chi phí trả trước đối với Khách hàng.

Dưới đây là cách bạn có thể cấu hình kế toán Chi phí trả trước trong ERPNext để tự động hóa quy trình.

### 2.1 Mặt hàng

Trong danh mục Mặt hàng, tại phần Chi phí trả trước, hãy tích vào trường **Enable Deferred Expense (Bật Chi phí trả trước)**. Trong phần này, bạn cũng có thể chọn một tài khoản Chi phí trả trước (Tài khoản Tài sản, ưu tiên Tài sản ngắn hạn) cho mặt hàng cụ thể này và số tháng.

![Item With Deferred Expense](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/deferred-item-expense.png)

### 2.2 Hóa đơn mua hàng

Khi tạo Hóa đơn mua hàng cho Mặt hàng có Chi phí trả trước, thay vì hạch toán vào Tài khoản chi phí, tài khoản Chi phí trả trước (Tài khoản tài sản) sẽ được Ghi có bằng số tiền mua hàng. Hãy xem xét một ví dụ đơn giản về đăng ký Internet ở đây:

![Invoice With Deferred Expense](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/deferred-purchase-invoice.gif)

### 2.3 Bút toán

Dựa trên Ngày bắt đầu (From Date) và Ngày kết thúc (To Date) được thiết lập trong bảng Mặt hàng của Hóa đơn mua hàng, các Bút toán sẽ được tạo tự động vào cuối mỗi tháng (khi sử dụng tính năng **Periodic Accounting**). Nó sẽ ghi nợ giá trị từ tài khoản Chi phí trả trước và ghi có vào Tài khoản chi phí đã chọn cho một Mặt hàng trong Hóa đơn mua hàng.

{next}