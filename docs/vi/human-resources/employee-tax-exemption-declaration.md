<!-- add-breadcrumbs -->
# Khai báo Miễn thuế cho Nhân viên

**Miễn thuế là việc miễn các khoản thuế đối với thu nhập, tài sản hoặc giao dịch mà lẽ ra phải đánh thuế đối với Nhân viên.**

Vào đầu Kỳ Bảng lương, nhân viên có thể khai báo số tiền miễn thuế mà họ sẽ yêu cầu từ mức lương chịu thuế của mình. ERPNext cho phép bạn chỉ định danh mục/danh mục phụ miễn thuế, số tiền miễn thuế và các thông tin liên quan khác trong biểu mẫu Khai báo Miễn thuế cho Nhân viên.


Để truy cập Khai báo Miễn thuế cho Nhân viên, hãy đi đến:

> Home > Human resources > Employee Tax and Benefits > Employee Tax Exemption Declaration


## 1. Điều kiện tiên quyết

Trước khi tạo Khai báo Miễn thuế cho Nhân viên, bạn nên tạo các mục sau:

* [Employee](employee.md)
* [Employee Tax Exemption Category](#31-employee-tax-exemption-category)
* [Employee Tax Exemption Sub Category](#32-employee-tax-exemption-category)


## 2. Cách tạo Khai báo Miễn thuế cho Nhân viên

Để tạo một Khai báo Miễn thuế cho Nhân viên mới:

1. Đi đến: Employee Tax Exemption Declaration > New.
1. Chọn Exemption Sub Category và Exemption Category.
1. Nhập Maximum Exemption Amount và Declared Amount.
1. Lưu và Xác nhận.

    <img class="screenshot" alt="Employee Tax Exemption Declaration" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-tax-exemption-declaration.png">

Tổng số tiền miễn thuế sẽ được miễn trừ khỏi thu nhập chịu thuế hàng năm của nhân viên khi tính toán các khoản khấu trừ thuế trong Bảng lương.

> **Lưu ý:** Nhân viên chỉ có thể gửi một bản Khai báo Miễn thuế cho Nhân viên cho mỗi Kỳ Bảng lương.

## 3. Các tính năng

###3.1 Danh mục Miễn thuế cho Nhân viên (Employee Tax Exemption Category)

Các khoản miễn trừ thu nhập chịu thuế thường được giới hạn cho các khoản chi tiêu thuộc các danh mục cụ thể do Chính phủ hoặc các cơ quan quản lý quyết định. ERPNext cho phép bạn cấu hình các danh mục khác nhau được phép miễn thuế. Ví dụ (tại Ấn Độ) có thể là 80G, 80C, B0CC, v.v.

Bạn có thể cấu hình Employee Tax Exemption Category bằng cách đi đến, **Employee Tax and Benefits > Employee Tax Exemption Category**

 <img class="screenshot" alt="Employee Tax Exemption Category" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-tax-exemption-sub-category1.png">


### 3.2 Danh mục phụ Miễn thuế cho Nhân viên (Employee Tax Exemption Sub-Category)

Dưới mỗi danh mục, có thể có nhiều mục mà việc miễn thuế được cho phép. Ví dụ, tại Ấn Độ, các danh mục phụ dưới 80C có thể là Phí Bảo hiểm Nhân thọ.

Bạn có thể cấu hình Employee Tax Exemption Category bằng cách đi đến, **Employee Tax and Benefits > Employee Tax Exemption Sub-Category**

 <img class="screenshot" alt="Employee Tax Exemption Category" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-tax-exemption-category1.png">


### 3.3 Miễn thuế HRA (Khu vực - Ấn Độ)

Đối với năm tài chính hiện tại, tại Ấn Độ, khoản miễn thuế Phụ cấp Thuê nhà (HRA) từ thu nhập chịu thuế là mức thấp nhất trong các mức sau:

* Số tiền thực tế mà người sử dụng lao động phân bổ cho HRA.
* Tiền thuê nhà thực tế trả trừ đi 10% lương cơ bản.
* 50% lương cơ bản, nếu nhân viên đang ở tại một thành phố lớn (40% đối với thành phố không phải là đô thị lớn).

Là một phần của Khai báo Miễn thuế cho Nhân viên, nhân viên cũng có thể điền thông tin Miễn thuế HRA. ERPNext sẽ tính toán mức miễn thuế đủ điều kiện cho HRA và thực hiện miễn trừ khi tính toán thu nhập chịu thuế.

Nhập Monthly House Rent (Tiền thuê nhà hàng tháng) và đánh dấu vào ô 'Rented in Metro City' nếu áp dụng, sau đó xác nhận biểu mẫu. Mức Miễn thuế HRA Hàng năm và Hàng tháng sẽ được tự động tính toán.

Sau khi bản khai báo được gửi, bạn có thể gửi bằng chứng miễn thuế của mình bằng cách nhấp vào nút _Submit Proof_.


<img class="screenshot" alt="Employee Tax Exemption Declaration" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/hra-exemption.png">

> Lưu ý: Thành phần HRA cần được cấu hình trong danh mục Công ty (Company) trong phần HRA Settings để tính năng miễn thuế HRA hoạt động.


## 4. Các chủ đề liên quan

1. [Employee Tax Exemption Proof Submission](employee-tax-exemption-proof-submission.md)
1. [Employee Benefit Application](employee-benefit-application.md)
1. [Employee Benefit Claim](employee-benefit-claim.md)

{next}