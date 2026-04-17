<!-- add-breadcrumbs -->
# Hạn mức tín dụng

**Hạn mức tín dụng là số tiền tối đa mà bạn sẵn lòng cung cấp cho một Khách hàng.**

Hạn mức tín dụng là số tiền tối đa mà một tổ chức tài chính hoặc bên cho vay khác sẽ cấp cho con nợ đối với một hạn mức tín dụng cụ thể. Từ góc độ của Khách hàng, đó là số lượng hàng hóa hoặc dịch vụ tối đa mà họ có thể nhận được mà không cần thanh toán trước tiền mặt.

Bạn có thể thiết lập Hạn mức tín dụng trong Khách hàng, Nhóm khách hàng và trong Công ty.
Khi một Đơn bán hàng hoặc một Hóa đơn bán hàng được Xác nhận, Hạn mức tín dụng sẽ được kiểm tra.

Thứ tự ưu tiên để kiểm tra Hạn mức tín dụng như sau:

* Hạn mức tín dụng được thiết lập trong Khách hàng
* Hạn mức tín dụng được thiết lập trong Nhóm khách hàng
* Hạn mức tín dụng được thiết lập trong Công ty

## 1. Cách thiết lập Hạn mức tín dụng
1. Đi đến: **Selling > Sales > Customer > Customer**.
1. Trong phần Credit Limit and Payment Terms, hãy thiết lập Hạn mức tín dụng.
1. Nếu bạn để Hạn mức tín dụng ở giá trị mặc định là 0, nó sẽ không có tác dụng.
1. Lưu.

 ![Customer Credit Limit](https://docs.erpnext.com/docs/v13/assets/img/accounts/customer-credit-limit.png)

## 2. Các tính năng
### 2.1 Kiểm soát viên tín dụng (Credit Controller)
Bạn có thể cho phép người dùng có một vai trò cụ thể ghi đè lên việc kiểm tra Hạn mức tín dụng và Xác nhận một Đơn bán hàng hoặc Hóa đơn bán hàng ngay cả khi Hạn mức tín dụng của Khách hàng đã được sử dụng hết.

Để thiết lập vai trò Kiểm soát viên tín dụng:

1. Đi đến: **Accounting > Settings > Accounts Settings**
1. Thiết lập vai trò trong trường Credit Controller.

![Credit Manager](https://docs.erpnext.com/docs/v13/assets/img/accounts/credit-manager-role.png)

### 2.2 Bỏ qua kiểm tra Hạn mức tín dụng cho Đơn bán hàng

Đối với các khách hàng cụ thể, bạn có thể thiết lập để hạn mức tín dụng được kiểm tra dựa trên tổng số tiền của các hóa đơn bán hàng chưa thanh toán thay vì dựa trên các đơn bán hàng. Bạn có thể thực hiện việc này bằng cách tích vào ô 'Bypass credit limit check at Sales Order' trong phần 'Credit Limit and Payment Terms' của khách hàng.

![Credit Limit Bypass in Sales Order](https://docs.erpnext.com/docs/v13/assets/img/accounts/customer-credit-limit-bypass.png)

### 2.3 Hạn mức tín dụng cho Nhóm khách hàng
Để thiết lập Hạn mức tín dụng ở cấp độ Nhóm khách hàng:

1. Đi đến **Selling > Customers > Customer Group**.
1. Mở Nhóm khách hàng và thiết lập Hạn mức tín dụng.

### 2.4 Hạn mức tín dụng cho Công ty
Khi thiết lập Hạn mức tín dụng ở cấp độ Công ty, tất cả các Khách hàng sẽ được áp dụng Hạn mức tín dụng này trên phạm vi toàn cầu.

Để thiết lập Hạn mức tín dụng ở cấp độ Công ty:

1. Đi đến **Accounting > Masters and Accounts > Company**.
1. Mở Công ty và thiết lập Hạn mức tín dụng.

### 3. Các chủ đề liên quan
1. [Payment Entry](payment-entry.md)
1. [Customer](https://docs.erpnext.com/docs/v13/user/manual/en/CRM/customer)

{next}