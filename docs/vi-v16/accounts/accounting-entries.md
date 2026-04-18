<!-- add-breadcrumbs -->
# Bút toán kế toán

Khái niệm về kế toán được giải thích thông qua một ví dụ dưới đây: Chúng ta sẽ lấy một "Quán trà" làm Công ty và xem cách hạch toán các bút toán kế toán cho hoạt động kinh doanh này.

Mama (Chủ quán trà) đầu tư 25.000 Rs để bắt đầu kinh doanh.
![JE](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/equity-journal-entry.png)

## 1. Đầu tư
Mama đầu tư 25.000 Rs vào Công ty với hy vọng thu được lợi nhuận. Nói cách khác, công ty có nghĩa vụ phải trả 25.000 Rs cho Mama trong tương lai. Vì vậy, tài khoản "Mama" là một tài khoản nợ phải trả và được ghi có. Số dư tiền mặt của Công ty sẽ tăng lên nhờ khoản đầu tư này. "Tiền mặt" là một tài sản của công ty và sẽ được ghi nợ.

  Công ty cần thiết bị (bếp, ấm trà, cốc, v.v.) và nguyên vật liệu (trà, đường, sữa, v.v.) ngay lập tức. Ông quyết định mua chúng từ một cửa hàng tạp hóa gần nhất, "Super Bazaar" mà chủ cửa hàng là một người bạn, để có thể mua chịu. Thiết bị tốn 2.800 Rs và nguyên vật liệu tốn 2.200 Rs. Ông thanh toán 2.000 Rs trong tổng chi phí là 5.000 Rs. Điều này có thể được ghi lại trong ERPNext bằng cách sử dụng [Payment Entry](payment-entry.md).

![JE](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-entry-gl.png)

## 2. Tài sản
Thiết bị là "Tài sản cố định" (vì chúng có thời gian sử dụng lâu dài) và nguyên vật liệu là "Tài sản lưu động" (vì chúng được sử dụng cho hoạt động kinh doanh hàng ngày) của công ty. Vì vậy, các tài khoản "Thiết bị" và "Tồn kho" đã được ghi nợ để tăng giá trị. Ông thanh toán 2.000, vì vậy tài khoản "Tiền mặt" sẽ giảm đi một khoản tương ứng, do đó được ghi có và ông có nghĩa vụ phải trả 3.000 Rs cho "Super Bazaar" sau đó, vì vậy Super Bazaar sẽ được ghi có 3.000 Rs.

  Mama (người phụ trách tất cả các bút toán) quyết định hạch toán doanh thu vào cuối mỗi ngày để có thể phân tích doanh số hàng ngày. Vào cuối ngày đầu tiên, quán trà bán được 325 tách trà, mang lại doanh thu ròng là 1.625 Rs. Chủ quán vui vẻ hạch toán doanh thu ngày đầu tiên của mình.

![JE](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/sales-invoice-gl.png)

## 3. Thu nhập
Thu nhập đã được hạch toán vào tài khoản "Doanh thu bán trà", tài khoản này được ghi có để tăng giá trị và cùng một số tiền đó sẽ được ghi nợ vào tài khoản "Tiền mặt". Giả sử, để pha 325 tách trà, chi phí là 800 Rs, vì vậy "Tồn kho" sẽ giảm (Cr) 800 Rs và chi phí sẽ được hạch toán vào tài khoản "Giá vốn hàng bán" với cùng số tiền đó.

Vào cuối tháng, công ty đã thanh toán tiền thuê sạp (5.000 Rs) và lương của một nhân viên (8.000 Rs), người đã gia nhập ngay từ ngày đầu tiên.

![JE](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/salary-journal-entry-gl.png)

## 4. Kết chuyển lợi nhuận

Khi tháng trôi qua, công ty mua thêm nhiều nguyên vật liệu cho hoạt động kinh doanh. Sau một tháng, ông hạch toán lợi nhuận để cân đối "Bảng cân đối kế toán" và "Báo cáo kết quả hoạt động kinh doanh". Lợi nhuận thuộc về Mama chứ không phải công ty, do đó nó là một khoản nợ phải trả của công ty (công ty phải trả khoản đó cho Mama). Khi Bảng cân đối kế toán chưa cân, tức là bên Nợ không bằng bên Có, thì lợi nhuận vẫn chưa được kết chuyển. Để kết chuyển lợi nhuận, các tài khoản lãi lỗ phải được thiết lập lại. Lãi/lỗ được chuyển sang tài khoản Nợ phải trả và báo cáo lãi lỗ sẽ bắt đầu mới. Việc này được thực hiện bằng cách sử dụng [Period Closing Voucher](period-closing-voucher.md).

**Giải thích**: Doanh thu ròng và chi phí của Công ty lần lượt là 40.000 Rs và 20.000 Rs. Vì vậy, công ty đạt lợi nhuận là 20.000 Rs. Để thực hiện bút toán kết chuyển lợi nhuận, tài khoản "Lãi hoặc Lỗ" đã được ghi nợ và tài khoản "Vốn chủ sở hữu" đã được ghi có. Số dư tiền mặt ròng của Công ty là 44.000 Rs và có một số nguyên vật liệu sẵn có trị giá 1.000 Rs.

### Các chủ đề liên quan
1. [Payment Entry](payment-entry.md)
1. [Advance Payment Entry](advance-payment-entry.md)
1. [Freeze Accounting Entries](articles/freeze-accounting-entries.md)
1. [Post Dated Cheque Entry](articles/post-dated-cheque-entry.md)
1. [Adjust Withhold Amount Payment Entry](articles/adjust-withhold-amount-payment-entry.md)
1. [Bulk Payment Entry](articles/bulk-payment-entry.md)
1. [Difference Entry Button](articles/difference-entry-button.md)

{next}