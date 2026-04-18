<!-- add-breadcrumbs -->
# Tạm ứng Nhân viên

**Đôi khi nhân viên đi ra ngoài để thực hiện công việc của công ty và công ty sẽ thanh toán trước một số tiền cho các chi phí của họ. Đây là lúc nhân viên có thể tạo biểu mẫu Tạm ứng Nhân viên, nơi các chi tiết như Mục đích Chi phí và Số tiền Chi phí có thể được ghi lại.**

Sau khi Tạm ứng Nhân viên được tạo bởi Nhân viên, Người phê duyệt chi phí có thể xác nhận bản ghi tạm ứng sau khi kiểm tra. Sau khi Tạm ứng Nhân viên được xác nhận, kế toán sẽ thực hiện thanh toán và lập Bút toán thanh toán.

Để truy cập Tạm ứng Nhân viên, hãy đi đến:

> Human Resources > Expense Claims > Employee Advance

## 1. Điều kiện tiên quyết

1. [Nhân viên](employee.md)
1. [Phòng ban](department.md)
1. [Hệ thống tài khoản](../accounts/chart-of-accounts.md)

## 2. Cách tạo Tạm ứng Nhân viên
1. Đi đến: Employee Advance > New.
1. Chọn Nhân viên mà bạn cần tạm ứng.
1. Nhập Mục đích và Số tiền tạm ứng.
1. Chọn Tài khoản tạm ứng và Phương thức thanh toán.
1. Lưu.

    <img class="screenshot" alt="Expense Claim" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-advance.png">

> Lưu ý: Nhân viên chỉ có thể Lưu Tạm ứng Nhân viên chứ không thể Xác nhận nó. Nó chỉ có thể được xác nhận bởi Người phê duyệt chi phí.

## 3. Các tính năng

### 3.1 Xác nhận Tạm ứng Nhân viên

Bản ghi Tạm ứng Nhân viên có thể được tạo bởi bất kỳ Nhân viên nào nhưng họ không thể xác nhận bản ghi đó.

Sau khi lưu Tạm ứng Nhân viên, Nhân viên nên [Giao tài liệu cho Người phê duyệt](../using-erpnext/assignment.md). Khi được giao, người dùng phê duyệt cũng sẽ nhận được thông báo qua email. Để tự động hóa thông báo email, bạn cũng có thể thiết lập [Thông báo Email](../setting-up/notifications.html.md).

Sau khi kiểm tra, Người phê duyệt chi phí có thể Xác nhận (Chấp nhận) biểu mẫu Tạm ứng Nhân viên hoặc Từ chối yêu cầu.

### 3.2 Lập Bút toán thanh toán

##### Tạm ứng Nhân viên qua Bút toán thanh toán
Sau khi xác nhận bản ghi Tạm ứng Nhân viên, người dùng kế toán sẽ có thể tạo một [Bút toán thanh toán](../accounts/payment-entry.md) bằng cách sử dụng nút 'Create'.

Bút toán thanh toán sẽ trông như sau:

<img class="screenshot" alt="Employee Advance Payment via Payment Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-advance-payment-entry.png">

#### Tạm ứng Nhân viên qua Bút toán
Ngoài ra, một [Bút toán](../accounts/journal-entry.md) cũng có thể được tạo cho khoản Tạm ứng Nhân viên.


<img class="screenshot" alt="Employee Advance Payment via Journal Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-advance-journal-entry1.png">

> Lưu ý: Đảm bảo rằng Loại đối tác (Party Type) được chọn là Employee và Loại tham chiếu (Reference Type) được chọn là Employee Advance.

<img class="screenshot" alt="Employee Advance Payment via Journal Entry" src="https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/employee-advance-journal-entry2.png">

#### Tạm ứng Nhân viên đã được thanh toán
Khi xác nhận Bút toán thanh toán/Bút toán, số tiền đã thanh toán và trạng thái sẽ được cập nhật trong bản ghi Tạm ứng Nhân viên.

### 3.3 Điều chỉnh các khoản tạm ứng trên Yêu cầu thanh toán chi phí

Sau này khi nhân viên yêu cầu thanh toán chi phí, một bản ghi tạm ứng có thể được lấy trong [Yêu cầu thanh toán chi phí](expense-claim.md) và liên kết với bản ghi yêu cầu.


### 3.4 Hoàn trả Số tiền
Khi khoản tạm ứng được thanh toán cho Nhân viên, có ba tình huống xảy ra:

* Số tiền có thể chưa được sử dụng hết
* Toàn bộ số tiền đã được sử dụng hết
* Một phần số tiền đã được sử dụng


Tạo Tạm ứng Nhân viên, tạo một bút toán thanh toán để cho biết số tiền đã được thanh toán.

* Nếu số tiền chưa được sử dụng, hãy nhấp vào nút **Return** để hoàn trả số tiền Tạm ứng đã thanh toán
    ![Return Button](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/advance-return-button.png)
* Nếu toàn bộ khoản tạm ứng đã được sử dụng, nó sẽ được phản ánh trong trường Số tiền đã yêu cầu (Claimed Amount)
* Nếu chỉ một phần số tiền được yêu cầu và phần còn lại được hoàn trả, số tiền hoàn trả sẽ được hiển thị trong trường 'Returned Amount'.
    ![Return advance Amount](https://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/wwwhttps://raw.githubusercontent.com/frappe/erpnext_documentation/master/erpnext_documentation/www/docs/v13/assets/img/human-resources/advance-returned-amount.png)

## 4. Các chủ đề liên quan

1. [Yêu cầu thanh toán chi phí](expense-claim.md)



{next}