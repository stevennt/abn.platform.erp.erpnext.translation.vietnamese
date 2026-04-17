<!-- add-breadcrumbs -->
# Danh mục Khấu trừ Thuế tại nguồn

**Danh mục Khấu trừ Thuế tại nguồn là Thuế khấu trừ tại nguồn.**

Theo quy định này, người chịu trách nhiệm thanh toán có nghĩa vụ khấu trừ thuế tại nguồn theo các mức thuế suất quy định. Thay vì nhận thuế từ thu nhập của bạn vào một thời điểm sau đó, chính phủ muốn người thanh toán khấu trừ thuế trước và nộp vào ngân sách nhà nước.

Để truy cập danh sách Danh mục Khấu trừ Thuế tại nguồn, hãy đi tới:
> Trang chủ > Kế toán > Thuế > Danh mục Khấu trừ Thuế tại nguồn

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Danh mục Khấu trừ Thuế tại nguồn, bạn nên tạo các mục sau trước:

1. [Nhà cung cấp](../buying/supplier.md)
1. [Khách hàng](https://docs.erpnext.com/docs/v13/user/manual/en/CRM/customer)

## 2. Cách tạo Danh mục Khấu trừ Thuế tại nguồn
Trong ERPNext, các Danh mục Khấu trừ Thuế tại nguồn cho hầu hết các trường hợp đã có sẵn theo mặc định, tuy nhiên, bạn có thể tạo thêm nếu cần.

1. Đi tới danh sách Danh mục Khấu trừ Thuế tại nguồn và nhấn vào Mới.
1. Nhập một tên duy nhất, ví dụ: Section 194C Individual.
1. Nhập Tên danh mục (Cổ tức, Phí chuyên gia, v.v.,).
1. Nhập Tỷ lệ khấu trừ thuế cho một [Năm tài chính](fiscal-year.md).
1. Bạn có thể thiết lập ngưỡng cho một hóa đơn đơn lẻ hoặc tổng của tất cả các hóa đơn.
1. Chọn một tài khoản cho Công ty của bạn để thuế được ghi có vào đó.
1. Thêm thêm các công ty và tài khoản khác nếu cần.
1. Lưu.

 ![Tax withholding Category](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/tax-withholding-category.png)

Trong phần chi tiết kế toán, tài khoản TDS được thêm cho mỗi Công ty trong hệ thống.

### 2.1 Gán Khấu trừ Thuế cho Nhà cung cấp

Sau khi Lưu, nó có thể được gán cho một Nhà cung cấp:

 ![Tax withholding Category in Supplier](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/tax-withholding-category-in-supplier.png)

### 2.2 Ngưỡng hoạt động như thế nào?
Xét một Nhà cung cấp được áp dụng Danh mục Khấu trừ Thuế tại nguồn.

Ví dụ, giả sử mức thuế suất 5% sẽ được áp dụng cho hóa đơn có Ngưỡng đơn lẻ là 20.000 và Ngưỡng lũy kế là 30.000. Nếu một hóa đơn được tạo với tổng cộng là 20.000 thì ngưỡng đơn lẻ sẽ được kích hoạt và mức thuế 5% sẽ được tính.

Nhưng nếu số tiền hóa đơn tổng cộng là 15.000 thì sẽ không có thuế nào được tính vì nó chưa vượt quá ngưỡng. Nếu một hóa đơn khác lại được tạo cho cùng một nhà cung cấp với tổng số tiền là 15.000 thì mặc dù nó không vượt quá Ngưỡng đơn lẻ, các khoản phí vẫn sẽ bị khấu trừ vì tổng của hóa đơn trước và hóa đơn này cộng lại là 30.000, bằng với Ngưỡng lũy kế đã chỉ định.

## 3. Sử dụng Khấu trừ Thuế
### 3.1 Sử dụng trong Hóa đơn mua hàng
Trong ví dụ sau, chúng tôi đã chọn 'TDS - 194C - Individual' có ngưỡng đơn lẻ là 30.000, ngưỡng lũy kế là 1,00,000 và tỷ lệ là 1%.

1. Nếu **Nhà cung cấp** đã được thiết lập trường khấu trừ thuế, thì khi chọn Nhà cung cấp đó, một hộp kiểm sẽ hiển thị trong Hóa đơn mua hàng để chọn có áp dụng thuế hay không.

![Tax Withholding Category in Purchase Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/tax-withholding-category-in-purchase-invoice.png)

1. Hãy tạo một hóa đơn trị giá 90.000. Việc Lưu hóa đơn sẽ tự động tính toán thuế và thêm nó vào bảng thuế.

 ![Tax Withholding Category in Purchase Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/withheld-tax-calculation-in-purchase-invoice.png)

1. Để thấy hiệu quả của Ngưỡng lũy kế, hãy tạo một hóa đơn trị giá 10.000 và Xác nhận nó.

  ![Tax Withholding Category Cumulative Threshhold](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/tax-withholding-category-cumulative-threshold.png)

 Mặc dù số tiền hóa đơn không vượt quá Ngưỡng đơn lẻ (30.000), chúng ta thấy rằng thuế đã được tính. Điều này là do hóa đơn trước và hóa đơn hiện tại cộng lại là 1,10,000, vượt quá Ngưỡng lũy kế. Do đó, thuế dựa trên tỷ lệ được cung cấp trong **Danh mục Khấu trừ Thuế tại nguồn** được áp dụng tương ứng.

> Lưu ý: Khi Xác nhận hóa đơn, ba Bút toán sổ cái được tạo ra:

>1. Thứ nhất là ghi nợ từ tài khoản chi phí
>1. Thứ hai là ghi có vào tài khoản Phải trả người bán
>1. Thứ ba là ghi có vào tài khoản được chọn trong Danh mục Khấu trừ Thuế tại nguồn.

### 3.2 Thiết lập TCS - Section 20C(1H) cho các khách hàng đủ điều kiện
Trong ví dụ sau, chúng tôi đã tạo một Danh mục Khấu trừ Thuế tại nguồn cho [TCS - Section 20C(1H)](https://taxguru.in/income-tax/faqs-tcs-sales-goods-section-206c1h.html) và thiết lập nó cho một khách hàng đủ điều kiện.

1. Trước tiên, chúng tôi sẽ tạo một Danh mục Khấu trừ Thuế tại nguồn tên là **TCS - Section 20C(1H)** và chúng tôi thiết lập ngưỡng lũy kế là 50 Lakhs theo đề án.

![Tax Withholding Category For TCS](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/tax-withholding-category-for-tcs.png)

1. Nếu một **Khách hàng** dự kiến vượt ngưỡng doanh số 50 Lakh trong Năm tài chính hiện tại, thì chúng ta có thể thiết lập Danh mục Khấu trừ Thuế tại nguồn của khách hàng đó thành TCS - Section 20C(1H) để tự động tính toán TCS trên việc bán hàng hóa đối với các hóa đơn của khách hàng.

 ![TCS in Customer](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/tcs-eligible-customer.png)

1. Hãy tạo một hóa đơn trị giá 50 Lakhs cho khách hàng đủ điều kiện. Việc Lưu hóa đơn sẽ tự động tính toán thuế và thêm nó vào bảng thuế.

 ![TCS Calculation in Sales Invoice](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/accounts/tcs-invoice.png)

 Vì hóa đơn vượt quá Ngưỡng lũy kế (50 Lakhs), chúng ta thấy rằng thuế đã được tính. Do đó, thuế dựa trên tỷ lệ được cung cấp trong **Danh mục Khấu trừ Thuế tại nguồn** được áp dụng tương ứng. Lưu ý rằng, theo đề án, TCS được tính trên số tiền vượt quá ngưỡng, tức là 0.075 % của 10 Lakhs.

### 4. Các chủ đề liên quan
1. [Quy tắc Thuế](tax-rule.md)
1. [Nhà cung cấp](../buying/supplier.md)
1. [Khách hàng](https://docs.erpnext.com/docs/v13/user/manual/en/CRM/customer)

{next}