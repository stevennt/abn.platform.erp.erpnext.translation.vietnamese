<!-- add-breadcrumbs -->
# Điều khoản thanh toán

**Một Điều khoản thanh toán giúp thiết lập lịch trình mà theo đó các khoản thanh toán sẽ được thực hiện.**

Một Điều khoản thanh toán xác định một hạn mức thanh toán cụ thể. Ví dụ: thanh toán 50% khi giao hàng và 50% khi giao mặt hàng. Bạn có thể lưu các điều khoản thanh toán của doanh nghiệp mình trên ERPNext và đưa chúng vào tất cả các chứng từ trong chu trình bán hàng/mua hàng. ERPNext sẽ thực hiện tất cả các bút toán Sổ cái tương ứng.

Trong ERPNext, biểu mẫu Điều khoản thanh toán chỉ xác định tỷ lệ phần trăm. Lịch trình thanh toán thực tế có thể được áp dụng dễ dàng bằng cách sử dụng Mẫu điều khoản thanh toán.

Bạn có thể sử dụng Điều khoản thanh toán trong các chứng từ sau:

- Hóa đơn bán hàng
- Hóa đơn mua hàng
- Đơn bán hàng
- Đơn mua hàng
- Báo giá

Để truy cập Điều khoản thanh toán, hãy đi tới:
> Home > Accounting > Accounting Masters > Payment Term

<img class="screenshot" alt="Payment Terms" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-terms.png">

## 1. Cách tạo Điều khoản thanh toán

1. Đi tới danh sách Điều khoản thanh toán và nhấn New.
1. Nhập tên cho Điều khoản thanh toán (ví dụ: 50% sau khi giao hàng).
1. Nhập tỷ lệ Hóa đơn (Invoice portion). Nếu bạn nhập 50, tỷ lệ sẽ là 50 phần trăm của Số tiền hóa đơn.
1. Chọn một loại Ngày đến hạn (Due Date).
1. Tại mục Credit Days, nhập số ngày mà sau đó số tiền còn lại phải được thanh toán.
1. Lưu.

Các trường được giải thích như sau:

* **Payment Term Name:** Tên của Điều khoản thanh toán này.
* **Due Date Based On:** Cơ sở để tính toán ngày đến hạn cho Điều khoản thanh toán. Ngày này được tính sau X số ngày kể từ **ngày hạch toán (posting date)** của hóa đơn/đơn hàng. Có ba tùy chọn:
 - **Day(s) after invoice date**: Ngày đến hạn sẽ được tính theo số ngày kể từ ngày hạch toán của hóa đơn. Ví dụ: nếu nhập 7 vào ngày 20, ngày đến hạn sẽ là ngày 27.
 - **Day(s) after the end of the invoice month**: Ngày đến hạn sẽ được tính theo số ngày kể từ ngày cuối cùng của tháng mà hóa đơn được tạo. Ví dụ: nếu nhập 7 vào tháng hiện tại và ngày cuối cùng của tháng là ngày 30, ngày đến hạn sẽ là ngày 7 của tháng tiếp theo.
 - **Month(s) after the end of the invoice month**: Ngày đến hạn sẽ được tính theo số tháng kể từ ngày cuối cùng của tháng mà hóa đơn được tạo. Ví dụ: nếu nhập 3 vào ngày 20 tháng 1, ngày đến hạn sẽ là ngày 20 tháng 3.
* **Invoice Portion:** Phần của tổng số tiền hóa đơn mà Điều khoản thanh toán này sẽ được áp dụng. Giá trị được đưa vào sẽ được coi là phần trăm, ví dụ: 50 = 50% Tổng cộng của hóa đơn/đơn hàng.
* **Credit Days (tùy chọn):** Số ngày hoặc tháng được phép nợ tùy thuộc vào tùy chọn được chọn trong trường Due Date Based On. 0 có nghĩa là không cho phép nợ.
* **Description:** (tùy chọn) Mô tả ngắn gọn về Điều khoản thanh toán.

### 1.1 Thiết lập Chiết khấu khi Thanh toán sớm

Bạn có thể thiết lập các điều khoản thanh toán có chiết khấu sao cho nếu việc thanh toán được thực hiện trong thời hạn quy định thì một phần số tiền/tỷ lệ phần trăm của giá trị hóa đơn sẽ được chiết khấu. Các trường sau đây xác định cấu hình chiết khấu:

* **Discount Type:** Mặc định là Phần trăm (Percentage). Bạn cũng có thể đổi thành Số tiền (Amount).
* **Discount:** Tính theo Phần trăm hoặc Số tiền (ví dụ: 10% hoặc ₹ 5,000).
* **Discount Validity Based On:** Trường này hoạt động tương tự như trường Due Date Based On ở phần trước.
* **Discount Validity:** Số ngày hoặc tháng mà khoản chiết khấu có hiệu lực so với ngày hóa đơn (ví dụ: 10 ngày sau ngày hóa đơn).

<img class="screenshot" alt="Payment Terms with Discount" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-terms-with-discount.png">

Giờ đây bạn có thể liên kết Điều khoản thanh toán với một Hóa đơn và khi tạo bút toán thanh toán cho hóa đơn đó, khoản chiết khấu sẽ được áp dụng tự động.

### 1.2 Điều khoản thanh toán trong các Chứng từ được chuyển đổi
Khi chuyển đổi hoặc sao chép các chứng từ trong chu trình bán hàng/mua hàng, các Điều khoản thanh toán đính kèm sẽ được sao chép. Khi tạo Đơn bán hàng từ một Báo giá, Ngày đến hạn trong Điều khoản thanh toán sẽ theo Báo giá, điều này cần phải được cập nhật lại.

Để dễ sử dụng, bạn cũng có thể thiết lập một Mẫu điều khoản thanh toán và chỉ cần chọn lại nó.

### 1.3 Thêm Điều khoản thanh toán vào Chứng từ

Sau khi bạn đã soạn xong Mẫu điều khoản thanh toán, bạn có thể sử dụng chúng trong các giao dịch mua và bán. Dựa trên giá trị được xác định cho Điều khoản thanh toán và giá trị giao dịch, lịch trình thanh toán sẽ được xác định, với Ngày đến hạn cho mỗi hạn mức thanh toán.

![Payment Schedule](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/payment-term-in-invoice.png)

Lưu ý: Lịch trình thanh toán có thể được hiển thị trong Chế độ xem in bằng cách sử dụng [Print Format Builder](../setting-up/print/print-format-builder.md).

### 2. Các chủ đề liên quan
1. [Sales Invoice](sales-invoice.md)
1. [Purchase Invoice](purchase-invoice.md)

{next}