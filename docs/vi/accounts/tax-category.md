<!-- add-breadcrumbs -->
# Nhóm thuế

**Nhóm thuế cho phép áp dụng một hoặc nhiều Quy tắc thuế vào các giao dịch dựa trên các tiêu chí khác nhau.**

Nếu bạn muốn áp dụng các loại thuế khác nhau dựa trên Nhóm thuế, hãy tạo Nhóm thuế từ:

> Trang chủ > Kế toán > Thuế > Nhóm thuế

## 1. Điều kiện tiên quyết
Trước khi tạo và sử dụng Nhóm thuế, bạn nên tạo các mục sau trước:

1. [Quy tắc thuế](/docs/v13/user/manual/en/accounts/tax-rule)

## 2. Nhóm thuế hoạt động như thế nào
Việc tạo Nhóm thuế rất đơn giản, hãy đi tới danh sách Nhóm thuế, nhấn vào Mới và nhập tên.

- Một Nhóm thuế có thể được liên kết với một hoặc nhiều [Quy tắc thuế](/docs/v13/user/manual/en/accounts/tax-rule).
- Nhóm thuế này có thể được gán cho một Khách hàng, vì vậy khi Khách hàng đó được chọn, Nhóm thuế sẽ được tự động lấy ra. Điều này cũng áp dụng cho Nhà cung cấp.
- Việc này sẽ lấy Mẫu thuế bán hàng được liên kết với Quy tắc thuế. Do đó, các dòng trong bảng Thuế sẽ được tự động điền đầy đủ.
- Nhóm thuế có thể được sử dụng để nhóm các Khách hàng mà cùng một loại thuế sẽ được áp dụng. Ví dụ: Chính phủ, Tổ chức phi chính phủ (NGO), thương mại, v.v.

  ![Nhóm thuế trong Hóa đơn bán hàng](/docs/v13/assets/img/accounts/tax-category-in-invoice.gif)

> Mẹo: Một Nhóm thuế có thể được gán cho nhiều Quy tắc thuế. Vì vậy, bạn có thể tạo các tổ hợp khác nhau để áp dụng thuế tự động vào các giao dịch.

## 3. Gán Nhóm thuế
Nhóm thuế được xác định tự động trong một giao dịch thông qua Địa chỉ của Đối tác hoặc Thông tin chính của Đối tác (Khách hàng/Nhà cung cấp). Bạn có thể gán Nhóm thuế dựa trên:

1. [Khách hàng](/docs/v13/user/manual/en/CRM/customer)
1. [Nhà cung cấp](/docs/v13/user/manual/en/buying/supplier)
1. [Địa chỉ](/docs/v13/user/manual/en/CRM/address) Thanh toán hoặc Giao hàng.
  Bạn có thể chọn ưu tiên Địa chỉ thanh toán hay Địa chỉ giao hàng bằng cách thay đổi tùy chọn 'Determine Address Tax Category From' trong Cài đặt kế toán. Nhóm thuế được xác định từ Địa chỉ của Đối tác trước. Nếu Địa chỉ không được gán bất kỳ Nhóm thuế nào, thì Nhóm thuế của Đối tác sẽ được sử dụng.
      ![Địa chỉ Nhóm thuế](/docs/v13/assets/img/accounts/tax-category-in-address.png)
1. [Mặt hàng](/docs/v13/user/manual/en/stock/item#316-item-tax)
1. Bạn cũng có thể chọn Nhóm thuế một cách thủ công trong một giao dịch.

## 4. Nhóm thuế có tác động gì trong một giao dịch?

* Các Mẫu thuế Mặt hàng cụ thể cho Nhóm thuế đó sẽ được tự động thiết lập cho các mặt hàng.
* Bạn có thể tạo [Quy tắc thuế]({{docs_base_url}}/user/manual/en/accounts/tax-rule) để tự động thiết lập một Mẫu Thuế và Phí Bán hàng / Mua hàng cụ thể dựa trên các Nhóm thuế khác nhau trong giao dịch.

## 5. Các chủ đề liên quan
1. [Quy tắc thuế](/docs/v13/user/manual/en/accounts/tax-rule)
1. [Khách hàng](/docs/v13/user/manual/en/CRM/customer)
1. [Nhà cung cấp](/docs/v13/user/manual/en/buying/supplier)
1. [Địa chỉ](/docs/v13/user/manual/en/CRM/address)

{next}