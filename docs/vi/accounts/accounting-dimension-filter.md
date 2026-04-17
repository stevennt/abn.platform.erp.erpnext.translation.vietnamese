<!-- add-breadcrumbs -->
# Bộ lọc Chiều kế toán

> Được giới thiệu trong Phiên bản 13

Trong ERPNext, bạn có thể kiểm soát việc gắn thẻ các chiều kế toán khác nhau đối với một tài khoản cụ thể.
Bạn có thể cho phép hoặc hạn chế một số chiều kế toán nhất định đối với một tài khoản bằng cách sử dụng bộ lọc chiều kế toán.

Để truy cập danh sách Bộ lọc Chiều kế toán, hãy đi đến:
> Home > Accounting > Accounting Dimension Filters

## 1. Cách tạo Bộ lọc Chiều kế toán trong ERPNext.

1. Đi đến danh sách Bộ lọc Chiều kế toán và nhấn vào Mới.
1. Chọn Chiều kế toán mà bạn muốn áp dụng hạn chế.
1. Chọn "Allow" (Cho phép) hoặc "Restrict" (Hạn chế) trong trường Allow Or Restrict dựa trên loại hạn chế mà bạn muốn áp dụng.
1. Thêm các tài khoản mà hạn chế sẽ được áp dụng trong bảng Accounts. Tùy chọn, bạn cũng có thể tích vào ô "Is Mandatory" nếu chiều kế toán đó cần phải là bắt buộc đối với bất kỳ tài khoản cụ thể nào.
1. Thêm các giá trị chiều kế toán trong bảng Dimensions sẽ được cho phép hoặc hạn chế cho các tài khoản đã nêu.

<img alt="Create accounting dimension filter" class="screenshot" src="{{docs_base_url}}/v13/assets/img/accounts/accounting-dimension-filter.png">


## 2. Các tính năng

### 2.1 Lọc các chiều kế toán trong các giao dịch

Dựa trên các hạn chế được áp dụng cho tài khoản, chỉ những chiều được cho phép mới được lọc và hiển thị trong các giao dịch.

![Accounting Dimension With Filters](/docs/v13/assets/img/accounts/accounting-dimension-with-filters.png)

### 2.2 Kiểm tra tính hợp lệ cho các Chiều không hợp lệ và Chiều bắt buộc

Trong trường hợp thiếu bất kỳ chiều bắt buộc nào hoặc một chiều bị hạn chế được gắn với bất kỳ tài khoản áp dụng nào, hệ thống sẽ không cho phép Xác nhận giao dịch đó cho đến khi chiều kế toán chính xác được chọn.

<img alt="Invalid Dimension" class="screenshot" src="{{docs_base_url}}/v13/assets/img/accounts/invalid-dimension.png">

<img alt="Mandatory Dimension" class="screenshot" src="{{docs_base_url}}/v13/assets/img/accounts/mandatory-dimension.png">


### Các chủ đề liên quan
1. [Cost Center](/docs/v13/user/manual/en/accounts/cost-center)
1. [Budgeting](/docs/v13/user/manual/en/accounts/budgeting)
1. [Accounting Dimensions](/docs/v13/user/manual/en/accounts/accounting-dimensions)

{next}