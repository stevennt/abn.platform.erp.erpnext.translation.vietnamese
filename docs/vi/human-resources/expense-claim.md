<!-- add-breadcrumbs -->
# Yêu cầu thanh toán chi phí

**Yêu cầu thanh toán chi phí được thực hiện khi nhân viên chi tiền túi cho các khoản chi thay mặt cho công ty.**

Ví dụ, nếu họ đưa khách hàng đi ăn trưa, họ có thể tạo yêu cầu hoàn tiền thông qua biểu mẫu Yêu cầu thanh toán chi phí.

Để truy cập Yêu cầu thanh toán chi phí, hãy đi đến:

> Nhân sự > Yêu cầu thanh toán chi phí > Yêu cầu thanh toán chi phí

## 1. Điều kiện tiên quyết

1. [Nhân viên](employee.md)
1. [Phòng ban](department.md)
1. [Hệ thống tài khoản](../accounts/chart-of-accounts.md)


## 2. Cách tạo Yêu cầu thanh toán chi phí

1. Đi đến: Yêu cầu thanh toán chi phí > Mới.
1. Chọn Tên nhân viên trong trường 'Từ nhân viên'.
1. Chọn Người phê duyệt chi phí.
1. Nhập Ngày chi phí, Loại yêu cầu thanh toán chi phí và Số tiền.
1. Ngoài ra, bạn cũng có thể nhập Thuế và phí chi phí.
1. Trong Chi tiết kế toán, chọn Tài khoản phải trả mặc định của Công ty.
1. Lưu và Xác nhận.

<img class="screenshot" alt="Expense Claim" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/expense_claim.png">

Thiết lập ID nhân viên, ngày, danh sách các khoản chi và các loại thuế tương ứng cần được thanh toán và nhấn “Xác nhận” bản ghi.

<img class="screenshot" alt="Expense Claim" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/expense-claim-expenses.png">

Quy trình yêu cầu thanh toán chi phí
<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/5SZHJF--ZFY?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
</div>

### Phê duyệt chi phí

Người phê duyệt cho Yêu cầu thanh toán chi phí được chính Nhân viên lựa chọn. Nhân viên có thể chọn từ danh sách người dùng đã được cấu hình là _Người phê duyệt chi phí_ cho [Phòng ban](department.md) của họ.

Khi một Yêu cầu thanh toán chi phí mới được tạo, nếu người phê duyệt chi phí được chọn không có quyền truy cập, tài liệu sẽ được chia sẻ với người phê duyệt với quyền "xác nhận".

Sau khi lưu Yêu cầu thanh toán chi phí, Nhân viên nên [Giao tài liệu cho Người phê duyệt](../using-erpnext/assignment.md). Khi được giao, người dùng phê duyệt cũng sẽ nhận được thông báo qua email. Để tự động hóa thông báo email, bạn cũng có thể thiết lập Cảnh báo email.

Người phê duyệt Yêu cầu thanh toán chi phí có thể cập nhật “Số tiền được phê duyệt” so với Số tiền yêu cầu của Nhân viên. Khi xác nhận, Trạng thái phê duyệt phải được chuyển sang Đã phê duyệt hoặc Từ chối. Nếu Đã phê duyệt, Yêu cầu thanh toán chi phí sẽ được xác nhận. Nếu bị từ chối, ý kiến của Người phê duyệt chi phí có thể được thêm vào phần Ghi chú để giải thích lý do tại sao yêu cầu được phê duyệt hoặc bị từ chối.

### Hạch toán chi phí

Khi xác nhận Yêu cầu thanh toán chi phí, hệ thống sẽ hạch toán chi phí vào tài khoản chi phí và tài khoản nhân viên.
<img class="screenshot" alt="Expense Claim" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/expense_claim_book.png">

Người dùng có thể xem các yêu cầu thanh toán chi phí chưa thanh toán bằng cách sử dụng báo cáo "Yêu cầu thanh toán chi phí chưa yêu cầu"
<img class="screenshot" alt="Expense Claim" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/unclaimed_expense_claims.png">

### Thanh toán cho Yêu cầu thanh toán chi phí

Để thực hiện thanh toán cho yêu cầu thanh toán chi phí, người dùng phải nhấp vào Tạo > Thanh toán.

#### Yêu cầu thanh toán chi phí

<img class="screenshot" alt="Create Payment" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/expense_claim_create_payment.png">

#### Bút toán thanh toán

> Lưu ý: Số tiền này không nên được gộp chung với Lương vì khi đó số tiền sẽ bị tính thuế đối với Nhân viên.

<img class="screenshot" alt="Expense Claim" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/expense_claim_payment_entry.png">

Ngoài ra, một Bút toán thanh toán có thể được lập cho một nhân viên và tất cả các Yêu cầu thanh toán chi phí còn tồn đọng sẽ được đưa vào.

> Kế toán > Bút toán thanh toán > Bút toán thanh toán mới

Thiết lập Loại thanh toán là "Trả tiền", Loại đối tác là Nhân viên, Đối tác là nhân viên được thanh toán và tài khoản được dùng để thanh toán. Tất cả các yêu cầu thanh toán chi phí còn tồn đọng sẽ được đưa vào và số tiền thanh toán có thể được phân bổ cho từng khoản chi.

### Liên kết với Công việc & Dự án

* Để Liên kết Yêu cầu thanh toán chi phí với Công việc hoặc Dự án, hãy chỉ định Công việc hoặc Dự án khi thực hiện Yêu cầu thanh toán chi phí.

<img class="screenshot" alt="Expense Claim - Project Link" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/project/project-expense-claim-1.png">

Điều này sẽ cập nhật chi phí Dự án với các số tiền trong Yêu cầu thanh toán chi phí.

<img class="screenshot" alt="Expense Claim - Project Link" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/project/project-expense-claim-2.png">

{next}